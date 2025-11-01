<template>
    <div class="login-container">
    <div class="login-header" style="color: white;">Login</div>
    <form @submit.prevent="login">
      <div class="input-group">
        <label for="email" style="color: white;">Email:</label>
        <input v-model="LoginRequest.email" type="email" id="email" name="email" required>
      </div>
      <div class="input-group">
        <label for="password" style="color: white;">Password:</label>
        <input v-model="LoginRequest.password" type="password" id="password" name="password" required>
      </div>
      <button class="login-btn">Login</button>
    </form>
  </div>
  </template>
  <script>
  import axios from 'axios';
  import {Store, mapActions, storeKey} from 'vuex'
  import VuexStore from '../store/VuexStore'
  import { useStore } from 'vuex'; // Import the useStore function
  const { setAuth } = mapActions(['setAuth']);
  export default {
    name:'login',
    data() {
    return {
        LoginRequest:{
          email: '',
          password: '',
        }
    };
    },
    methods:{
        login(){
           try{
            //const store = VuexStore; 
                    const response = axios.post("http://localhost:8080/api/login",this.LoginRequest
                    ).then(res => {
                      console.log(res.data); 
                    if(res.data == true){
                    VuexStore.dispatch('setAuth', res.data);
                    VuexStore.state.isAuth=res.data;
                    localStorage.setItem('isAuth', res.data);
                         
                    window.location.reload();
                    window.location.href = '/upload';
  
                    }
                    else{
                      alert("Not a valid user.");
                    }
                         })
                       
            }
            catch(err){
                alert("Not a valid user.");
            }
        }
    }
  }
  </script>
  <style>
  .login-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100vh;
  background-color: #020230;
  }
  
  .login-header {
  font-size: 24px;
  margin-bottom: 20px;
  }
  
  .login-form {
  width: 300px;
  }
  
  .input-group {
  margin-bottom: 15px;
  }
  
  .input-group label {
  display: block;
  font-weight: bold;
  margin-bottom: 5px;
  }
  
  .input-group input {
  width: 100%;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
  }
  
  .login-btn {
  background-color: #007bff;
  color: #fff;
  border: none;
  border-radius: 5px;
  padding: 10px;
  font-size: 16px;
  cursor: pointer;
  width: 100%;
  }
  
  .login-btn:hover {
  background-color: #0056b3;
  }
  </style>