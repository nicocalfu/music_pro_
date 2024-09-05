<template>
  
        
        
        <!-- Favicon-->
        <link rel="icon" type="image/x-icon" href="assets/favicon.ico" />
        <!-- Bootstrap icons-->
        <link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.5.0/font/bootstrap-icons.css" rel="stylesheet" />
        
    
    
        <!-- Navigation-->
        <nav class="navbar navbar-expand-lg navbar-light bg-light">
            <div class="container px-4 px-lg-5">
                <a class="navbar-brand" href="/"><img src="@/assets/music_pro.png"/></a>
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation"><span class="navbar-toggler-icon"></span></button>
                <div class="collapse navbar-collapse" id="navbarSupportedContent">
                    <ul class="navbar-nav me-auto mb-2 mb-lg-0 ms-lg-4">
                        <li class="nav-item"><a class="nav-link active" aria-current="page" href="/">Tienda</a></li>
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
        <!-- Header-->
        <header class="bg-dark py-5">
            <div class="container px-4 px-lg-5 my-5">
                <div class="text-center text-white">
                    <h1 class="display-4 fw-bolder">Music Pro</h1>
                    <p class="lead fw-normal text-white-50 mb-0">Tú mejor opción</p>
                </div>
            </div>
        </header>
        <!-- Section-->
        <section class="py-5">
            <div class="container px-4 px-lg-5 mt-5">
                <div class="row gx-4 gx-lg-5 row-cols-2 row-cols-md-3 row-cols-xl-4 justify-content-center">               
                    <div class="col mb-5" v-for="prod, i in Products" :key="prod.id">
                        <div class="card h-100">
                            <img class="card-img-top" v-bind:src="prod.image" alt="..." />
                            <!-- Product image-->
                            <!-- <img class="card-img-top" v-bind:src="require('@' + '/assets/products/' + prod.id +'.jpg')" alt="..." /> -->
                            <!-- Product details-->
                            <div class="card-body p-4">
                                <div class="text-center">
                                    <!-- Product name-->
                                    <h5 class="fw-bolder">{{prod.title}}</h5>
                                    <!-- Product reviews-->
                                    <div class="d-flex justify-content-center small text-warning mb-2">
                                        {{prod.description}}
                                    </div>
                                    <!-- Product price-->
                                    ${{ new Intl.NumberFormat('es-cl').format(prod.price) }}
                                </div>
                            </div>
                            <!-- Product actions-->
                            <div class="card-footer p-4 pt-0 border-top-0 bg-transparent">
                                <div class="text-center"><a class="btn btn-outline-dark mt-auto" href="#" v-on:click="updateCart(user_id, prod.id)">Añadir al carro</a></div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>
        <!-- Footer-->
        <footer class="py-5 bg-dark">
            <div class="container"><p class="m-0 text-center text-white">Copyright &copy; Music Pro 2023</p></div>
            <div class="container"><p class="m-0 text-center text-white" v-if="userLogged">User loggued: {{userLogged}}</p></div>
        </footer>
    
</template>

<script>
  import {getUserLogged, setUserLogged, removeUserCookie, getUserAdmin, getUserSeller, getWarehouseMan} from '../functions';
  import axios from 'axios'
  export default{
    data(){
      user_id:'';
      shoppingList:0;
      return{shoppingList: 0, Products:null, userAdmin:null, userSeller:null, warehouseman: null}
    },
    /*
    beforeRouteEnter(to) {
        // redirect back home
        if(getUserLogged() == undefined){
            alert('Please login first');
            if (to.name !== 'Login') {
                return '/login'
            }
        }
    },
    */
    mounted(){
      this.getProducts();
      this.checkUser();
    },
    computed:{
        userLogged() {
            this.user_id = getUserLogged();
            return getUserLogged();
        }
    },
    methods:{
      productImage(prod_id){
        return "@/assets/products/"+prod_id+".jpg";
      },
      getProducts(){
        this.userAdmin = getUserAdmin();
        this.userSeller = getUserSeller();
        this.warehouseman = getWarehouseMan();
        axios.get('/listproducts').then(
          response =>
            this.Products = response.data
          )
      },
      checkUser(){
        this.user_id = getUserLogged();
        if (this.user_id === undefined){
            alert('Please login first');
            removeUserCookie();
            this.$router.push("/login");
        }
      },
      closeSession(){
        //window.location.href='/shoppingcart';
        removeUserCookie();
        this.$router.push("/login");
      },
      goToShoppingCart(){
        //window.location.href='/shoppingcart';
        setUserLogged(this.user_id);
        this.$router.push("/shoppingcart");
      },
      updateCart(user_id, prod_id){
        var url = "http://127.0.0.1:5000/updateShoppingCart/" + user_id;
        //console.log(prod_id)
        axios.put(url, {
          prod_id: prod_id,
          quantity: 1
        }).then((response) => {
          //var status = response.data['status'];
          //const data = response.data;
          this.shoppingList = this.shoppingList+1;
          console.log(response);
        });
      }
    }
  }
</script>
