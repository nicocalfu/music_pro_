from fireo import models as mdl

def check_email(field_val):
    if '@' in field_val:
        return True
    else:
        return False

class Users(mdl.Model):
    username = mdl.TextField(required=True)
    email = mdl.TextField(validator=check_email)
    password = mdl.TextField(required=True)
    is_admin = mdl.BooleanField(default=False)
    is_seller = mdl.BooleanField(default=False)
    warehouseman = mdl.BooleanField(default=False)
    accountant_auditor = mdl.BooleanField(default=False)


class Products(mdl.Model):
    title = mdl.TextField(required=True)
    description = mdl.TextField(required=False)
    price = mdl.NumberField(required=True)
    image = mdl.TextField(required=False)
    seller_id = mdl.TextField(required=False)
    stock = mdl.NumberField(required=True)


class ShoppingCart(mdl.Model):
    user_id = mdl.TextField(required=True)
    #additionDate = mdl.DateTime()
    #prod_id = mdl.TextField(required=False)
    #quantity = mdl.NumberField(required=False)

class ShoppingCartProducts(mdl.Model):
    prod_id = mdl.TextField(required=False)
    quantity = mdl.NumberField(required=False)

class PurchaseOrder(mdl.Model):
    user_id = mdl.TextField(required=False)
    addition_date = mdl.DateTime(required=False)
    product_dispatch = mdl.BooleanField(default=False)
    shipping_mode = mdl.TextField(required=False)

class PurchaseOrderProducts(mdl.Model):
    prod_id = mdl.TextField(required=True)
    quantity = mdl.NumberField(required=True)



