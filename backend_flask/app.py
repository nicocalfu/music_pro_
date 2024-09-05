from flask import Flask, request, jsonify, session
from passlib.hash import pbkdf2_sha256
from fireo.models import Model
from fireo.fields import TextField, NumberField
from flask_cors import CORS, cross_origin
from pykhipu.client import Client
import fireo
import uuid
import json
import datetime
import os
import re

from models import Users, Products, ShoppingCart, ShoppingCartProducts, PurchaseOrder, PurchaseOrderProducts

app = Flask(__name__)
CORS(app, supports_credentials=True)
app.secret_key = "private"

directory = os.path.dirname(os.path.abspath(__file__)) + "your json firebase key directory"
fireo.connection(from_file=directory)

@app.route('/')
def hello_world():
    return "Hello world"

@app.route('/apipayment', methods=['PUT'])
def apipayment():
    try:
        user_pay = request.get_json(force=True)
        product_price = user_pay['price']
        product_title = user_pay['title']
        client = Client(receiver_id='446951', secret='9505837bad0032c0bb9cefbe8e0bdd6e7ad82f5f')
        payment = client.payments.post(product_title, 'CLP', product_price)
        return(payment.payment_url)
    except:
        return jsonify({'status':False, 'message':'Payment error'})


#register the user
@app.route('/register', methods=['POST'])
def register_user():
    try:
        user_data = request.get_json(force=True)
        username = user_data['username']
        email = user_data['email']
        is_admin = False
        is_seller = False
        
        if len(user_data['password']) < 8:  
            return jsonify({'status':False, 'message':'Error: contraseña necesita minimo 8 caracteres'})
        if not re.search("[a-z]", user_data['password']):  
            return jsonify({'status':False, 'message':'Error: contraseña necesita por lo menos una minuscula'})
        if not re.search("[A-Z]", user_data['password']):  
            return jsonify({'status':False, 'message':'Error: contraseña necesita por lo menos una mayuscula'})
        if not re.search("[0-9]", user_data['password']):  
            return jsonify({'status':False, 'message':'Error: contraseña necesita por lo menos un numero'})
        
        password = pbkdf2_sha256.hash(user_data['password'])
        if 'is_admin' in user_data:
            is_admin = user_data['is_admin']
        if 'is_seller' in user_data:
            is_seller = user_data['is_seller']

        user_verification = Users.collection.filter('username', '==', username).get()

        if user_verification == None:
            u = Users()
            u.username = username
            u.email = email
            u.password = password
            u.is_admin = is_admin
            u.is_seller = is_seller
            u.save()
            s = ShoppingCart()
            s.user_id = u.id
            s.save()
            return jsonify({'status': True, 'message': "¡Registrado correctamente!", 'user_id': u.id})
        else:
            return jsonify({'status':False, 'message':'El nombre de usuario ingresado ya existe'})
    except:
        return jsonify({'status':False, 'message':'Error en el registro de usuario, verifique si el email ingresado es valido'})


#login user
@app.route('/login2', methods=['POST'])
@cross_origin(supports_credentials=True)
def login_user():
    credentials = request.json
    try:
        if credentials['username'] and credentials['password']:
            valid_credentials = pbkdf2_sha256.verify(credentials['password'], Users.collection.filter('username', '==', credentials['username']).get().password)
        else:
            valid_credentials = False
    except:
        valid_credentials = False

    if valid_credentials:
        session['username'] = credentials['username']
        user = Users.collection.filter('username', '==', credentials['username']).get()
        return jsonify({'status': valid_credentials, 'user_id': user.id, 'is_admin': user.is_admin, 'is_seller': user.is_seller, 'warehouseman': user.warehouseman})

    return jsonify({'message': "Error: verifique los datos ingresados"})

@app.route('/logout')
def logout_user():
    session.clear()
    return jsonify({'status': 'username' not in session})



@app.route('/products/<product_id>', methods=['GET'])  #trae productos por id de producto
def search_items(product_id):
    try:
        products=json.dumps(Products.collection.filter('id', '==', product_id).get().to_dict())
        products = json.loads(products)
        return products;
    except:
        return jsonify({'status':False, 'message':'The Item is not available.'})



@app.route('/listproducts', methods=['GET'])  #trae todos los productos
def list_products():
    try:
        lista=[]
        products = Products.collection.fetch()
        for product in products:
            lista.append(product.to_dict())
        return json.dumps(lista)
    except:
        return jsonify({'status':False, 'message':'No Items available.'})

@app.route('/listPurchaseOrders', methods=['GET'])
def list_purchase_orders():
    try:
        purchase_list=[]
        purchase_orders = PurchaseOrder.collection.fetch()
        for purchase_order in purchase_orders:
            purchase_list.append(purchase_order.to_dict())
        return json.dumps(purchase_list)
    except:
        return jsonify({'status':False, 'message':'No Items available.'})


@app.route('/updateShoppingCart/<user_id>', methods=['PUT']) #el carrito de compras se actualiza por id de usuario y edita cantidad de productos
def update_shoppingcart(user_id):
    try:
        prod_data = request.get_json(force=True)
        cart = ShoppingCart.collection.filter('user_id', '==', user_id).get()
        product_list = ShoppingCartProducts.collection.parent(cart.key).fetch()
        for ShoppingCartProduct in product_list:
            if(ShoppingCartProduct.prod_id == prod_data['prod_id']):
                ShoppingCartProduct.quantity = ShoppingCartProduct.quantity + prod_data['quantity']
                ShoppingCartProduct.update(ShoppingCartProduct.key)
                return jsonify({'status':True, 'message':'Cart Updated Successfully.'})  
        cart_product = ShoppingCartProducts(parent=cart.key)
        cart_product.prod_id = prod_data['prod_id']
        cart_product.quantity = prod_data['quantity']
        cart_product.save()
        return jsonify({'status':True, 'message':'Cart Updated Successfully.'})
    except:
        return jsonify({'status':False, 'message':'The Cart is not available.'})


@app.route('/deleteShoppingCartProducts/<user_id>', methods=['PUT']) #elimina productos del carrito de compras por id de usuario
def delete_shoppingcartproduct(user_id):
    try:
        prod_data = request.get_json(force=True)
        cart = ShoppingCart.collection.filter('user_id', '==', user_id).get()
        product_list = ShoppingCartProducts.collection.parent(cart.key).fetch()
        for ShoppingCartProduct in product_list:
            if(ShoppingCartProduct.prod_id == prod_data['prod_id']):
                ShoppingCartProducts.collection.delete(ShoppingCartProduct.key)
                return jsonify({'status':True, 'message':'Cart Updated Successfully.'})  
    except:
        return jsonify({'status':False, 'message':'The cart is not available.'})


@app.route('/shoppingcart/<user_id>', methods=['GET'])  #traer carrito de compras por id de usuario
def shoppingcart(user_id):
    try:
        cart = ShoppingCart.collection.filter('user_id', '==', user_id).get()
        products = ShoppingCartProducts.collection.parent(cart.key).fetch()
        lista=[]
        for ShoppingCartProduct in products:
             lista.append(ShoppingCartProduct.to_dict())
        return json.dumps(lista)
    except:
        return jsonify({'status':False, 'message':'The cart is not available.'})


@app.route('/addProduct', methods=['POST'])  #añadir nuevo producto a la BD
def add_product():
    prod_data = request.get_json(force=True)
    user = Users.collection.filter('id', '==', prod_data['user_id']).get()

    try:
        if user.is_admin or user.is_seller:
            #allow to add product
            title = prod_data['title']
            description = prod_data['description']
            price = prod_data['price']
            image = prod_data['image']
            stock = prod_data['stock']
            p = Products()
            p.title = title
            p.description = description
            p.price = price
            p.image = image
            p.stock = stock
            p.save()
            return jsonify({'status':True, 'message':'Item Added Successfully.'})
        else:
            return jsonify({'status':False, 'message':'Operation not permitted'})
    except:
        return jsonify({'status':False, 'message':'Operation not permitted'})

@app.route('/createPurchaseOrder', methods=['POST'])    #creacion de logica de orden de comprar, trae productos del carrito y registra la compra
def purchase_order():
    try:
        purchase_data = request.get_json(force=True)
        user_id = purchase_data['user_id']
        if(user_id != None):
            purchase_order = PurchaseOrder()
            purchase_order.user_id = user_id
            cart = ShoppingCart.collection.filter('user_id', '==', user_id).get()
            product_list = ShoppingCartProducts.collection.parent(cart.key).fetch()
            for ShoppingCartProduct in product_list:
                purchase_products = PurchaseOrderProducts(parent=purchase_order.key)
                purchase_products.prod_id = ShoppingCartProduct.prod_id
                purchase_products.quantity = ShoppingCartProduct.quantity
                purchase_products.save()
                #Editar stock producto
                product_stock = Products.collection.get(ShoppingCartProduct.prod_id)
                product_stock.stock = product_stock.stock - ShoppingCartProduct.quantity
                product_stock.update()
                #Actualizar carrito
                ShoppingCartProducts.collection.delete(ShoppingCartProduct.key)
            purchase_order.save()
            return jsonify({'status': True, 'message': "Purchase order successfully created"})
    except:
        return jsonify({'status':False, 'message':'Error in order creation'})


@app.route('/dispatchOrder/<order_id>', methods=['PUT']) 
def dispatch_order(order_id):
    try:
        order = PurchaseOrder.collection.filter('id', '==', order_id).get()
        order.product_dispatch = True
        order.update()
        return jsonify({'status': True, 'order.product_dispatch': order.product_dispatch})
    except:
        return jsonify({'status':False, 'message':'The cart is not available.'})

if __name__ == "__main__":
    app.run(debug=True)
