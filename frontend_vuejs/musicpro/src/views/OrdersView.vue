<template>
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
                                <li><a class="dropdown-item active" href="/purchase/orders">Ver pedidos</a></li>
                                <li><a class="dropdown-item" href="/create/product">Crear producto</a></li>
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
  <section class="pb-5 header text-center">
    <div class="container py-5 text-white">
        <header class="py-5">
            <h1 class="display-4">Ordenes de compra</h1>
            <!--
            <p class="font-italic mb-1">Use bootstrap button variants to create call to action buttons inside a table, that's just for design, I'm sure you can make them work.</p>
            <p class="font-italic">Snippet by
                <a class="text-white" href="https://bootstrapious.com/">
                    <u>Bootstrapious</u>
                </a>
            </p>
        -->
        </header>


        <div class="row">
            <div class="col-lg-7 mx-auto">
                <div class="card border-0 shadow">
                    <div class="card-body p-5">

                        <!-- Responsive table -->
                        <div class="table-responsive">
                            <table class="table m-0">
                                <thead>
                                    <tr>
                                        <th scope="col">ID de orden</th>
                                        <th scope="col">Despachada</th>
                                        <th scope="col">Despachar orden</th>
                                    </tr>
                                </thead>
                                <tbody v-for="prod, i in Products" :key="prod.id">
                                    <tr>
                                        <th scope="row">{{prod.id}}</th>
                                        <td><li class="list-inline-item" v-if=(prod.product_dispatch)><i class="fa fa-check"></i></li>
                                            <li class="list-inline-item" v-else><i class="fa fa-times"></i></li>
                                        </td>
                                        <td>
                                            <ul class="list-inline m-0">
                                                <li class="list-inline-item">
                                                    <button class="btn btn-primary btn-sm rounded-0" type="button" v-on:click="dispatchOrder(prod.id)" data-toggle="tooltip" data-placement="top" title="Despachar"><i class="fa fa-check-square"></i></button>
                                                </li>
                                            </ul>
                                        </td>
                                        <!-- Call to action buttons
                                        <td>
                                            <ul class="list-inline m-0">
                                                <li class="list-inline-item">
                                                    <button class="btn btn-primary btn-sm rounded-0" type="button" data-toggle="tooltip" data-placement="top" title="Add"><i class="fa fa-table"></i></button>
                                                </li>
                                                <li class="list-inline-item">
                                                    <button class="btn btn-success btn-sm rounded-0" type="button" data-toggle="tooltip" data-placement="top" title="Edit"><i class="fa fa-edit"></i></button>
                                                </li>
                                                <li class="list-inline-item">
                                                    <button class="btn btn-danger btn-sm rounded-0" type="button" data-toggle="tooltip" data-placement="top" title="Delete"><i class="fa fa-trash"></i></button>
                                                </li>
                                            </ul>
                                        </td>
                                        -->
                                    </tr>
                                </tbody>
                                
                            </table>

                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</section>
</template>

<script>
  import {getUserLogged, removeUserCookie, setUserLogged, getUserAdmin, getWarehouseMan} from '../functions';
  import axios from 'axios'
  export default{
    data(){
      user_id:'';
      shoppingList:0;
      return{shoppingList: 0, Products:null, userAdmin:null, warehouseman: null}
    },
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
        this.warehouseman = getWarehouseMan();
        axios.get('http://127.0.0.1:5000/listPurchaseOrders').then(
          response =>
            this.Products = response.data
          )
      },
      checkUser(){
        var userAdmin = getUserAdmin();
        var warehouseman = getWarehouseMan();
        if (userAdmin === undefined){
            if (warehouseman === undefined){
                alert('Por favor, inicia sesión con una cuenta de bodeguero.');
                removeUserCookie();
                this.$router.push("/login");
            }
        }
      },
      goToShoppingCart(){
        //window.location.href='/shoppingcart';
        setUserLogged(this.user_id);
        this.$router.push("/shoppingcart");
      },
      closeSession(){
        //window.location.href='/shoppingcart';
        removeUserCookie();
        this.$router.push("/login");
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
      },
      dispatchOrder(order_id){
        var url = "http://127.0.0.1:5000/dispatchOrder/" + order_id;
        axios.put(url).then((response) => {
          alert('Orden despachada!');
          this.$router.go();
        });
      }
    }
  }
</script>
