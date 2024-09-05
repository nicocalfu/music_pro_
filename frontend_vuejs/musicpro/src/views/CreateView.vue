<template>
  <link href="//maxcdn.bootstrapcdn.com/font-awesome/4.1.0/css/font-awesome.min.css" rel="stylesheet">
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
                                <li><a class="dropdown-item active" href="/create/product">Crear producto</a></li>
                            </ul>
                        </li>
                        <li class="nav-item dropdown" v-if="userSeller">
                            <a class="nav-link dropdown-toggle" id="navbarDropdown" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">Panel de control</a>
                            <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
                                <li><a class="dropdown-item" href="/seller/warehouse-stock">Revisar stock</a></li>
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

  <div class="container">
    <div class="row">
      <div class="col-sm-9 col-md-7 col-lg-5 mx-auto">
        <div class="card border-0 shadow rounded-3 my-5">
          <div class="card-body p-4 p-sm-5">
            <h5 class="card-title text-center mb-5 fw-light fs-5">Crear producto</h5>
            <form v-on:submit.prevent="createProduct">
              <div class="form-floating mb-3">
                <!--<input type="email" v-model="email" class="form-control" id="floatingInput" placeholder="name@example.com">-->
                <input type="text" v-model="title" class="form-control" id="usernameInput">
                <label for="floatingInput">Titulo</label>
              </div>
              <div class="form-floating mb-3">
                <!--<input type="email" v-model="email" class="form-control" id="floatingInput" placeholder="name@example.com">-->
                <input type="text" v-model="description" class="form-control" id="emailInput">
                <label for="floatingInput">Descripcion</label>
              </div>
              <div class="form-floating mb-3">
                <!--<input type="email" v-model="email" class="form-control" id="floatingInput" placeholder="name@example.com">-->
                <input type="text" v-model="price" class="form-control" id="usernameInput">
                <label for="floatingInput">Precio</label>
              </div>
              <div class="form-floating mb-3">
                <input type="text" v-model="stock" class="form-control" id="usernameInput">
                <label for="floatingInput">Stock para ingresar</label>
              </div>
              <div class="form-floating mb-3">
                <input type="file" accept="image/*" @change="onFileChange" id="file-input">
              </div>
              <div class="d-grid">
                <button class="btn btn-primary btn-login text-uppercase fw-bold" type="submit">Crear producto!</button>
              </div>
              <hr class="my-4">
            </form>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import {getUserLogged, removeUserCookie, getUserSeller, getUserAdmin} from '../functions';
  import axios from 'axios'
  export default{
    data(){
      user_id:'';
      image: null;  //esto es nuevo 
      return{
        title:'',
        description:'',
        price:'',
        stock:'',
        Products:null, userAdmin:null, userSeller:null}
    },
    mounted(){
      this.checkUser();
    },
    computed:{
        userLogged() {
            this.user_id = getUserLogged();
            return getUserLogged();
        }
    },
    methods:{
      createProduct(){
        axios.post("http://127.0.0.1:5000/addProduct", {
          title: this.title,
          description: this.description,
          price: this.price,
          image: this.image,
          stock: this.stock,
          user_id: getUserLogged()
        }).then((response) => {
          var status = response.data['status'];
          if(status){
            alert('Producto creado correctamente!')
            this.$router.go();
          }
          else{
            console.log(response);
            alert("Error en la creacion de producto")
            this.$router.go();
          }
        });
      },
      closeSession(){
        //window.location.href='/shoppingcart';
        removeUserCookie();
        this.$router.push("/login");
      },
      checkUser(){
        this.userAdmin = getUserAdmin();
        this.userSeller = getUserSeller();
        if (this.userAdmin === undefined){
            alert('Por favor, inicia sesión con una cuenta de administrador.');
            removeUserCookie();
            this.$router.push("/login");
        }
      },
      goToShoppingCart(){
        //window.location.href='/shoppingcart';
        this.$router.push("/shoppingcart");
      },

      // esto es nuevo
      onFileChange(e) {
            const selectedImage = e.target.files[0];
            const reader = new FileReader();
            reader.readAsDataURL(selectedImage);
            reader.onload = e => {
                this.image = e.target.result
                //console.log(this.image)
            }
            //reader.readAsBinaryString(selectedImage)
            //console.log("file object", selectedImage);
        }

    }
  }
</script>
