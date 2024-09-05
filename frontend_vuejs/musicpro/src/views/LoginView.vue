<template>
  <body>
  <div class="container">
    <div class="row">
      <div class="col-sm-9 col-md-7 col-lg-5 mx-auto">
        <div class="card border-0 shadow rounded-3 my-5">
          <div class="card-body p-4 p-sm-5">
            <h5 class="card-title text-center mb-5 fw-light fs-5">Login</h5>
            <form v-on:submit.prevent="login">
              <div class="form-floating mb-3">
                <!--<input type="email" v-model="email" class="form-control" id="floatingInput" placeholder="name@example.com">-->
                <input type="text" v-model="username" class="form-control" id="floatingInput">
                <label for="floatingInput">Username</label>
              </div>
              <div class="form-floating mb-3">
                <input type="password" v-model="password" class="form-control" id="floatingPassword" placeholder="Password">
                <label for="floatingPassword">Password</label>
              </div>

              <div class="form-check mb-3">
                <input class="form-check-input" type="checkbox" value="" id="rememberPasswordCheck">
                <label class="form-check-label" for="rememberPasswordCheck">
                  Remember password
                </label>
                <p>¿Aún no tienes una cuenta? <a href="/signup">Haz click aquí</a></p>
              </div>
              <div class="d-grid">
                <button class="btn btn-primary btn-login text-uppercase fw-bold" type="submit">Login</button>
              </div>
              <hr class="my-4">
            </form>
          </div>
        </div>
      </div>
    </div>
  </div>
</body>
</template>

<script>


  import {setUserLogged, setUserSeller, setUserAdmin, setWarehouseMan} from '../functions';
  import axios from 'axios'
  
    export default{
    data(){
      return{
        password:'',
        username:''
      }
    },
    methods:{
      login(){
        axios.post("/login2", {
          username: this.username,
          password: this.password
        }).then((response) => {
          var status = response.data['status'];
          //const data = response.data;
          //console.log(status);
          if(status){
            var user_id = response.data['user_id'];
            setUserLogged(user_id);
            var is_seller = response.data['is_seller'];
            if (is_seller == true){
              setUserSeller(is_seller);
            }
            if (response.data['is_admin'] == true){
              setUserAdmin(response.data['is_admin']);
            }
            if (response.data['warehouseman'] == true){
              setWarehouseMan(response.data['warehouse']);
            }
            //console.log(user_id);
            window.location.href='/';
          }else{
            alert(response.data['message']);
            //console.log("no encontre usuario");
            //return false;
          };
        });
        },
      }
    }
  
    /*

import {show_alerta, enviarSolicitud} from '../functions';
  import axios from 'axios'
  
    export default{
    data(){
      return{
        password:'',
        username:''
      }
    },
    methods:{
      login(){
        axios.post("/login2", {
          username: this.username,
          password: this.password
        }).then((response) => {
          const data = response.data;
          console.log(data);
        });
        },
      }
    }


import {show_alerta, enviarSolicitud, setUserLogged, traerUserID} from '../functions';
export default{
    data(){
      return{
        username:'',
        password:'',
        url:'http://127.0.0.1:5000/login'
      }
    },
    methods:{
        login(){
            var parametros = {username:this.username,password:this.password};
            enviarSolicitud('POST',JSON.stringify(parametros),this.url,'Logeado');
        },
        async login2() {
          const parametros = {username:this.username,password:this.password};
        // POST request using fetch with async/await
          const requestOptions = {
          method: "POST",
          body: JSON.stringify(parametros)
          };
        const response = await fetch("http://127.0.0.1:5000/login", requestOptions);
        //const data = await response.json();
        const data = await response.json()
        console.log(data);
        }
    }
  }

*/

  
</script>
