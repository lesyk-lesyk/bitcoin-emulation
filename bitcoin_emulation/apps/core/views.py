from django.shortcuts import render, render_to_response, redirect
from django.core.context_processors import csrf
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django import forms

from models import Product
from models import KeyPair, Block, Transaction, Input, Output

import hashlib
import binascii
import CompactFIPS202 as keccak
import ecc as ECC

def loginview(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('core/login.html', c)

def logoutview(request):
    logout(request)
    return redirect('/login/')

def auth_and_login(request, onsuccess='/', onfail='/login/'):
    user = authenticate(username=request.POST['email'], password=request.POST['password'])
    if user is not None:
        login(request, user)
        return redirect(onsuccess)
    else:
        return redirect(onfail)

def save(request, onsuccess='/'):
    if request.user.is_authenticated():
         user = request.user
         print user

def create_user(username, email, password):
    user = User(username=username, email=email)
    user.set_password(password)
    user.save()

    return user

def user_exists(username):
    user_count = User.objects.filter(username=username).count()
    if user_count == 0:
        return False
    return True

def sign_up_in(request):
    post = request.POST
    if not user_exists(post['email']): 
        user = create_user(username=post['email'], email=post['email'], password=post['password'])
    	return auth_and_login(request)
    else:
    	return redirect("/login/")

@login_required(login_url='/login/')
def shop(request):
    userMail = request.user.email
    products = Product.objects.filter(in_shop=True)
    return render_to_response('core/shop.html', {'userMail': userMail, 'products': products})

@login_required(login_url='/login/')
def buy_product(request, product_id):
    user = request.user
    balance = get_balance(user)
    product = Product.objects.get(pk=product_id)

    if balance < product.price:
        return HttpResponse('You dont have enough money! You balance is %s bitcoins.' % balance)
    
    product.in_shop = False
    product.save()
    tr = Transaction(block=None)
    tr.save()

    out = Output(transaction=tr, address_x=product.public_x, address_y=product.public_y, amount=product.price)
    out.save()

    print 'balance:', balance
    print 'product price:', product.price
    
    price_tmp = product.price
    for keypair in user.keypair_set.filter(status='active'):
        price_tmp = price_tmp - keypair.amount

        print 'price_tmp:', price_tmp
        print 'keypair.amount:', keypair.amount


        message = keypair.public_x + keypair.public_y
        signature = ECC.sign_message(int(keypair.private, 0), message)

        signature_r, signature_s = signature

        keypair.status = 'expired'
        keypair.save()
        inp = Input(transaction=tr, address_x=keypair.public_x, address_y=keypair.public_y, signature_r=signature_r, signature_s=signature_s)
        inp.save()
        if price_tmp >= 0:
            pass
        else:
            price_tmp = price_tmp * (-1)
            private, public = ECC.make_keypair()
            public_x, public_y = public
            kp = KeyPair(owner=user, private=hex(private), public_x=hex(public_x), public_y=hex(public_y), amount=price_tmp)
            kp.save()
            change = Output(transaction=tr, address_x=hex(public_x), address_y=hex(public_y), amount=price_tmp)
            change.save()
            break
    # inp = Input(transaction=tr, address_x=hex(public_x), address_y=hex(public_y))


    return HttpResponse('Transaction for bying %s was created.' % product.name)

def get_transactions_hash(transactions):
    hashes_sum = ''
    for transaction in transactions:
        hashes_sum += get_trans_hash(transaction)
    return get_hash_str(hashes_sum)

def get_trans_hash(transaction):
    inputs = transaction.input_set.all().values()
    outputs = transaction.output_set.all().values()
    return get_hash_str(get_hash_str(inputs)+get_hash_str(outputs))

def get_hash_str(s_value):
    hash_v = keccak.SHA3_512(bytearray(str(s_value).encode('utf-8')))
    hash_hex = binascii.hexlify(hash_v)
    return hash_hex

# def verify_transactions(transactions):
#     for transaction in transactions:
#         inputs = transaction.input_set.all()
#         for _input in inputs:
#             message = _input.address_x + _input.address_y
#             print _input.address_x, _input.address_y
#             # print (int(_input.address_x, 16), int(_input.address_y, 16))
#             print message
#             print (_input.signature_r, _input.signature_s)
#             sign_res = ECC.verify_signature((_input.address_x, _input.address_y), message, (_input.signature_r, _input.signature_s))
#             if  sign_res == 'signature matches':
#                 print 'ok'
#             else:
#                 print 'bad'

import random
REWARD = 150
@login_required(login_url='/login/')
def mine(request):
    user = request.user
    prev_block = Block.objects.latest('timestamp')

    a = random.randrange(1, 99999999999)
    for i in range(a, a+2000):
        hex_val = prev_block.block_hash + hex(i)
        new_block_hash = keccak.SHA3_512(bytearray(str(hex_val).encode('utf-8')))
        new_block_hash_hex = binascii.hexlify(new_block_hash)

        if str(new_block_hash_hex).startswith('0000'):
            transactions = Transaction.objects.filter(status="pending")
            if len(transactions) < 1:
               return HttpResponse('No transactions')
            public_x, public_y = gen_key_pairs(user, REWARD)
            
            new_block = Block(prev_hash=get_block_hash(prev_block), nonce=i)
            new_block.save()
            new_block.block_hash = get_block_hash(new_block)
            new_block.save()

            tr = Transaction(block=new_block, status='done')
            tr.save()
            ou = Output(transaction=tr, address_x=hex(public_x), address_y=hex(public_y), amount=REWARD)
            ou.save()
            done_transactions(transactions, new_block)

            transactions_hash = get_transactions_hash(transactions)
            new_block.transactions_hash = transactions_hash
            new_block.save()
            
            return HttpResponse('Congratulations, %s' % new_block_hash_hex)
    return HttpResponse('try again')

def get_block_hash(block):
    value = str(block.timestamp) + str(block.prev_hash) + str(block.nonce)
    value_hash = keccak.SHA3_512(bytearray(str(value).encode('utf-8')))
    value_hex = binascii.hexlify(value_hash)
    return value_hex

    
def done_transactions(transactions, new_block):
    for trans in transactions:
        trans.status = 'done'
        trans.block = new_block
        trans.save()

def verify_block_transactions(block_id):
    block = Block.objects.get(pk=block_id)
    print block.block_hash

@login_required(login_url='/login/')
def user_cabinet(request):
    userMail = request.user.email
    balance = get_balance(request.user)

    # all_transactions = Transaction.objects.all()
    # get_transactions_hash(all_transactions)
    # verify_block_transactions()

    return render_to_response("core/user-cabinet.html", {
            'userMail': userMail,
            'balance': balance
        })

def get_balance(user):
    user_keys = user.keypair_set.filter(status='active')
    blocks = Block.objects.all()

    balance = 0

    for keypair in user_keys:
        for block in blocks:
            for tran in block.transaction_set.all():
                for output in tran.output_set.all():
                    if keypair.public_x == output.address_x and keypair.public_y == output.address_y:
                        balance = balance + output.amount

    return balance

def gen_key_pairs(user, amount):
    private, public = ECC.make_keypair()
    public_x, public_y = public
    kp = KeyPair(owner=user, private=hex(private), public_x=hex(public_x), public_y=hex(public_y), amount=amount)
    kp.save()
    return public_x, public_y

@login_required(login_url='/login/')
def create_first(request):
    user = request.user

    tr = Transaction(block=None, status='done')
    tr.save()


    private, public = ECC.make_keypair()
    public_x, public_y = public

    kp = KeyPair(owner=user, private=hex(private), public_x=hex(public_x), public_y=hex(public_y), amount=400)
    kp.save()

    ou = Output(transaction=tr, address_x=hex(public_x), address_y=hex(public_y), amount=400)
    ou.save()

    private, public = ECC.make_keypair()
    public_x, public_y = public

    kp = KeyPair(owner=user, private=hex(private), public_x=hex(public_x), public_y=hex(public_y), amount=200)
    kp.save()

    ou = Output(transaction=tr, address_x=hex(public_x), address_y=hex(public_y), amount=200)
    ou.save()    

    block = Block()
    block.save()
    block.block_hash = get_block_hash(block)
    block.save()

    tr.block = block
    tr.save()

    return HttpResponse('First block created! :)')


class AddProductForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    desc = forms.CharField(label='Description', max_length=500)
    price = forms.IntegerField(min_value=0)

@login_required(login_url='/login/')
def add_product(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = AddProductForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            if request.user.is_authenticated():
                user = request.user
                product_name = form.cleaned_data['name']
                product_desc = form.cleaned_data['desc']
                product_price = form.cleaned_data['price']
                public_x, public_y = gen_key_pairs(user, 0)
                p = Product(id=None, name=product_name, desc=product_desc, price=product_price, owner=user, public_x=hex(public_x), public_y=hex(public_y))
                p.save()
                print p
            # redirect to a new URL:
            return redirect('/shop') 

    # if a GET (or any other method) we'll create a blank form
    else:
        form = AddProductForm()

    return render(request, "core/add-product.html", {'form': form})
