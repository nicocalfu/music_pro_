<template>
  <body>
  <div class="container">
    <div class="row">
      <div class="col-sm-9 col-md-7 col-lg-5 mx-auto">
        <div class="card border-0 shadow rounded-3 my-5">
          <div class="card-body p-4 p-sm-5">
            <h5 class="card-title text-center mb-5 fw-light fs-5">Sign Up</h5>
            <form v-on:submit.prevent="register">
              <div class="form-floating mb-3">
                <!--<input type="email" v-model="email" class="form-control" id="floatingInput" placeholder="name@example.com">-->
                <input type="text" v-model="username" class="form-control" id="usernameInput">
                <label for="floatingInput">Username</label>
              </div>
              <div class="form-floating mb-3">
                <!--<input type="email" v-model="email" class="form-control" id="floatingInput" placeholder="name@example.com">-->
                <input type="text" v-model="email" class="form-control" id="emailInput">
                <label for="floatingInput">Email address</label>
              </div>
              <div class="form-floating mb-3">
                <input type="password" v-model="password" class="form-control" id="floatingPassword" placeholder="Password">
                <label for="floatingPassword">Password</label>
              </div>
              <div class="form-check mb-3">
                <p>¿Ya tienes una cuenta? <a href="/login">Haz click aquí</a></p>
              </div>
              <div class="d-grid">
                <button class="btn btn-primary btn-login text-uppercase fw-bold" type="submit">Sign Up!</button>
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
import {setUserLogged} from '../functions';
  import axios from 'axios'
  
    export default{
    data(){
      user_id:'';
      return{
        email:'',
        password:'',
        username:''
      }
    },
    methods:{
      register(){
        axios.post("http://127.0.0.1:5000/register", {
          email: this.email,
          username: this.username,
          password: this.password
        }).then((response) => {
          var status = response.data['status'];
          if(status){
            console.log(response);
            setUserLogged(response.data['user_id']);
            window.location.href='/';
          }
          else{
            alert(response.data['message']);
            console.log("Error en el registro de usuario");
          }
        });
        }
      }
    }

  
</script>
