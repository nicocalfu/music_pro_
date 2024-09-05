<template>
    <link href="//maxcdn.bootstrapcdn.com/font-awesome/4.1.0/css/font-awesome.min.css" rel="stylesheet">
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
            <div class="container px-4 px-lg-5">
                <a class="navbar-brand" href="/"><img src="@/assets/music_pro.png"/></a>
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation"><span class="navbar-toggler-icon"></span></button>
                <div class="collapse navbar-collapse" id="navbarSupportedContent">
                    <ul class="navbar-nav me-auto mb-2 mb-lg-0 ms-lg-4">
                        <li class="nav-item"><a class="nav-link" aria-current="page" href="/">Tienda</a></li>
                        <li class="nav-item"><a class="nav-link active" href="/about">Sobre nosotros</a></li>
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
    <div class="about-section paddingTB60 gray-bg">
                <div class="container">
                    <div class="row">
                        <div class="col-md-7 col-sm-6">
                            <div class="about-title clearfix">
                                <h1>Sobre <span>Nosotros</span></h1>
                                <h3>Music Pro</h3>
                                <p class="about-paddingB">“MUSIC PRO” es una distribuidora, la cual su tienda central está ubicada en la comuna de Providencia en Santiago de Chile desde el año 1988 y tiene sedes repartidas por la región metropolitana, las cuales están se encuentran en Maipú desde el 2001, Santiago desde el 2003, y Vitacura desde el 2010, abarcando así una gran área de la región antes mencionada y haciendo más fácil su distribución de productos.  </p>
                                <p>Los distintos instrumentos y accesorios que se pueden encontrar en “MUSIC PRO” son diversos, van desde guitarras acústicas, guitarras eléctricas de 6 a 8 cuerdas, bajos activos y pasivos de 4 a 6 cuerdas, sets de batería, amplificadores, cabezales, accesorios y además artículos como audífonos, parlantes, interfaces, adaptadores, pedales, cuerdas, etc., lo cual es posible gracias a que “MUSIC PRO”  tiene trato con marcas reconocidas del área como Ibáñez, ESP, Gibson, Jackson Marshall, y muchas más que hacen que sea una tienda diversa y muy solicitada por la variedad y calidad de sus productos.  </p>
                        <div class="d-flex"> 
                                <div class="p-2"><a href="https://www.facebook.com/"><i id="social-fb" class="fa fa-facebook-square fa-3x social"></i></a></div>
                                <div class="p-2"><a href="https://twitter.com/"><i id="social-tw" class="fa fa-twitter-square fa-3x social"></i></a> </div>
                                <div class="p-2"><a href="https://plus.google.com/"><i id="social-gp" class="fa fa-google-plus-square fa-3x social"></i></a></div>
                        </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
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
      getProducts(){
        this.userAdmin = getUserAdmin();
        this.userSeller = getUserSeller();
        this.warehouseman = getWarehouseMan();
      },
      checkUser(){
        this.user_id = getUserLogged();
        if (this.user_id === undefined){
            alert('Please login first');
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
      }
    }
  }
</script>
