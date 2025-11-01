<template>
    
    <div class="login-container">
    <div class="login-header" style="color: white">Register</div>
    <form @submit.prevent="signUp">
      <div class="input-group">
        <label for="name" style="color: white">Name:</label>
        <input v-model="HumanResources.name" type="text" id="name" name="name" required>
      </div>
      <div class="input-group">
        <label for="name" style="color: white">Surname:</label>
        <input v-model="HumanResources.surname" type="text" id="name" name="name" required>
      </div>  
      <div class="input-group">
        <label for="email" style="color: white">Email:</label>
        <input v-model="HumanResources.email" type="email" id="email" name="email" required>
      </div>
      <div class="input-group">
        <label for="password" style="color: white">Password:</label>
        <input v-model="HumanResources.password" type="password" id="password" name="password" required>
      </div>
      <button class="login-btn">Register</button>
    </form>
  </div>

  </template>
  <script>
  
  import axios from 'axios';
  import  mapActions from 'vuex'
  import VuexStore from '../store/VuexStore'
  //const { setAuth, setToken, setUser } = mapActions(['setAuth', 'setToken', 'setUser']);
  
  
  export default {
    name:'register',
    data() {
    return {
      HumanResources:{
          name: '',
          surname: '',  
          email: '',
          password: ''
        }
    };
    }, 
    methods:{
       async signUp(){

           try{
            //const store = VuexStore;
              console.log(this.user); 
              const response = await axios.post("http://localhost:8080/api/register",this.HumanResources
                 ).then(res => {
              console.log(res.data);
             // VuexStore.commit('setUser', this.user);
             // localStorage.setItem('user', this.user);
            //localStorage.setItem('users', JSON.stringify(VuexStore.state.users));
            //To retrieve the data:
            //const users = JSON.parse(localStorage.getItem('users'));
              this.$router.push({name: 'login'});
            });
              
            }
            catch(error){
              console.error(error);
              alert(error.response.data.message);
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