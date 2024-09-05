=-<template>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.5.0/font/bootstrap-icons.css" rel="stylesheet" />
  <nav class="navbar navbar-expand-lg navbar-light bg-light">
            <div class="container px-4 px-lg-5">
                <a class="navbar-brand" href="/"><img src="@/assets/music_pro.png"/></a>
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation"><span class="navbar-toggler-icon"></span></button>
                <div class="collapse navbar-collapse" id="navbarSupportedContent">
                    <ul class="navbar-nav me-auto mb-2 mb-lg-0 ms-lg-4">
                        <li class="nav-item"><a class="nav-link" aria-current="page" href="/">Tienda</a></li>
                        <li class="nav-item"><a class="nav-link" href="/about">Sobre nosotros</a></li>
                        <li class="nav-item dropdown" v-if="userAdmin">
                            <a class="nav-link dropdown-toggle" id="navbarDropdown" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">Panel de control</a>
                            <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
                                <li><a class="dropdown-item" href="/seller/warehouse-stock">Revisar stock</a></li>
                                <li><a class="dropdown-item" href="/purchase/orders">Ver pedidos</a></li>
                                <li><a class="dropdown-item" href="/create/product">Crear producto</a></li>
                            </ul>
                        </li>
                        <li class="nav-item dropdown" v-if="userSeller">
                            <a class="nav-link dropdown-toggle" id="navbarDropdown" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">Panel de control</a>
                            <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
                                <li><a class="dropdown-item" href="/seller/warehouse-stock">Revisar stock</a></li>
                            </ul>
                        </li>
                        <li class="nav-item dropdown" v-if="warehouseman">
                            <a class="nav-link dropdown-toggle" id="navbarDropdown" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">Panel de control</a>
                            <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
                                <li><a class="dropdown-item" href="/purchase/orders">Ver pedidos</a></li>
                            </ul>
                        </li>
                    </ul>
                    <div class="d-flex flex-row">
                        <div class="p-2">
                            <button class="btn btn-outline-dark" type="button" v-on:click="goToShoppingCart">
                            <i class="bi-cart-fill me-1"></i>
                            Carro
                            <!--
                            <span v-if="shoppingList > 0" class="badge" id="total-notif" v-text="shoppingList"></span>
                            
                            <span class="badge" id="total-notif" v-text="shoppingList"></span>
                            -->
                        </button>
                        </div>
                        <div class="p-2">
                            <button class="btn btn-danger" type="button" v-on:click="closeSession">Cerrar sesión</button>
                        </div>
                    </div>
                </div>
            </div>
        </nav>
  <section class="h-100" style="background-color: #eee;">
  <div class="container h-100 py-5">
    <div class="row d-flex justify-content-center align-items-center h-100">
      <div class="col-10">

        <div class="d-flex justify-content-between align-items-center mb-4">
          <h3 class="fw-normal mb-0 text-black">Carro de compras</h3>
          <p v-if="userLogged">User loggued: {{userLogged}}</p>
          <!--
          <div>
            <p class="mb-0"><span class="text-muted">Sort by:</span> <a href="#!" class="text-body">price <i
                  class="fas fa-angle-down mt-1"></i></a></p>
          </div>
        -->
        </div>
        <div class="card rounded-3 mb-4" v-for="prod, i in CartProducts" :key="prod.id">
          <div class="card-body p-4">
            <div class="row d-flex justify-content-between align-items-center">
              <div class="col-md-2 col-lg-2 col-xl-2">
                <!-- <img v-bind:src="require('@' + '/assets/products/' + prod.prod_id +'.jpg')" class="img-fluid rounded-3" alt="Cotton T-shirt"> -->
                <img class="img-fluid rounded-3" v-bind:src="prod.image" alt="Cotton T-shirt" />
              </div>
              <div class="col-md-3 col-lg-3 col-xl-3">
                    <p class="lead fw-normal mb-2">{{prod.title}}</p>
                <!--
                <p><span class="text-muted">Size: </span>M <span class="text-muted">Color: </span>Grey</p>
              -->
              </div>
              <div class="col-md-3 col-lg-3 col-xl-2 d-flex">
                    <p class="lead fw-normal text-white-50 mb-0">Cantidad: {{prod.quantity}}</p>
         <!--       <p class="lead fw-normal text-white-50 mb-0">Cantidad: {{quantity}}</p>  -->
                <!--
                  <p v-if="userLogged">{{quantity}}</p>
                <button class="btn btn-link px-2"
                  onclick="this.parentNode.querySelector('input[type=number]').stepDown()">
                  <i class="fas fa-minus"></i>
                </button>
                <input id="form1" min="0" name="quantity" value="2" type="number"
                  class="form-control form-control-sm" />
                <button class="btn btn-link px-2"
                  onclick="this.parentNode.querySelector('input[type=number]').stepUp()">
                  <i class="fas fa-plus"></i>
                </button>
              -->
              </div>
              <div class="col-md-3 col-lg-2 col-xl-2 offset-lg-1">
       <!--         <h5 class="mb-0">${{ new Intl.NumberFormat('es-cl').format(price) }}</h5>  -->
                    <h5 class="mb-0">${{ new Intl.NumberFormat('es-cl').format(prod.price) }}</h5>
              </div>
              <div class="col-md-1 col-lg-1 col-xl-1 text-end">
                <button class="btn btn-danger btn-sm rounded-0" v-on:click="removeCartProduct(user_id, prod.prod_id)" type="button" data-toggle="tooltip" data-placement="top" title="Delete"><i class="fa fa-trash"></i></button>
              </div>
            </div>
          </div>
        </div>

        <div class="card mb-4">
          <div class="card-body p-4 d-flex flex-row">
            <div class="form-outline flex-fill">
              <input type="text" id="form1" class="form-control form-control-lg" />
              <label class="form-label" for="form1">Codigo de descuento</label>
            </div>
            <button type="button" class="btn btn-outline-warning btn-lg ms-3">Aplicar</button>
          </div>
        </div>

        <div class="card">
          <div class="card-body">
            <button type="button" class="btn btn-warning btn-block btn-lg" v-on:click="payOrder">Proceder al pago</button>
          </div>
        </div>

      </div>
    </div>
  </div>
</section>
</template>

<script>
  import {getUserLogged, removeUserCookie, getUserAdmin, getUserSeller, getWarehouseMan} from '../functions';
  import axios from 'axios';
  export default{
    data(){
      user_id:'';
      return{CartProducts:null, userAdmin:null, userSeller:null, warehouseman: null}
    },
    mounted(){
      this.getProductByShoppingCart();
      this.checkUser();
    },
    computed:{
        userLogged() {
            this.user_id = getUserLogged();
            return getUserLogged();
        }
    },
    methods:{
      checkUser(){
        this.user_id = getUserLogged();
        if (this.user_id === undefined){
            alert('Please login first');
            removeUserCookie();
            this.$router.push("/login");
        }
      },
      getProductByShoppingCart(){
        this.userAdmin = getUserAdmin();
        this.userSeller = getUserSeller();
        this.warehouseman = getWarehouseMan();
        var url = "http://127.0.0.1:5000/shoppingcart/" + this.user_id;
        axios.get(url).then((response) => {
          this.CartProducts = response.data;
          var status = response.data.status;
          //console.log(this.CartProducts[0].prod_id)
          //linea nueva prueba de codigo
          //if (status){
            for (let prod of this.CartProducts) {
              var url = "http://127.0.0.1:5000/products/" + prod.prod_id;
              axios.get(url).then((response) => {
                this.productInfo = response.data;
                prod.title = this.productInfo.title;
                prod.description = this.productInfo.description;
                prod.image = this.productInfo.image;
                prod.price = this.productInfo.price * prod.quantity;
              });
              //console.log(this.CartProducts);
            }
          //}
          //finaliza linea nueva
        });
      },
      payOrder(){  //procede a pagar y crea la orden de compra.
        axios.post("http://127.0.0.1:5000/createPurchaseOrder", {
          user_id: this.user_id
        }).then((response) => {
          axios.put("http://127.0.0.1:5000/apipayment", {
          price: 1,
          //title: this.title
          title: "titulo"
        }).then((response) => {
          console.log(response.data);
          window.location.href=response.data;
        });
        });
      },
      closeSession(){
        //window.location.href='/shoppingcart';
        removeUserCookie();
        this.$router.push("/login");
      },
      goToShoppingCart(){
        //window.location.href='/shoppingcart';
        this.$router.push("/shoppingcart");
      },
      removeCartProduct(user_id, prod_id){
        var url = "http://127.0.0.1:5000/deleteShoppingCartProducts/" + user_id;
        //console.log(prod_id)
        axios.put(url, {
          prod_id: prod_id
        }).then((response) => {
          this.$router.go()
          //console.log(response);
        });
      }
    }
  }
</script>



