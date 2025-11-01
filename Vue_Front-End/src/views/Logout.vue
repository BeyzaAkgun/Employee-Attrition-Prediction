<template>
    <button class="logout-button" @click="logout">Logout</button>
</template>
<script>
import axios from 'axios';
import VuexStore from '../store/VuexStore'
export default{
  methods:{
    logout(){
      try{
      
        VuexStore.state.isAuth=false;
        VuexStore.dispatch('setAuth', false);
        localStorage.setItem('isAuth', false);
       
        window.location.reload();
        window.location.href = '/';
    }catch(err){
      console.log(err);
      alert("Some error occured.");
    }
    },
  }
}

</script>

<style scoped>
.logout-button{
  background-color: #ff6347;
  color: #fff;
  border: none;
  border-radius: 5px;
  padding: 10px 20px;
  font-size: 16px;
  cursor: pointer;
  transition: background-color 0.3s, transform 0.2s;
}
.logout-button:hover{
  background-color: #e74c3c;
  transform: scale(1.05);
}
</style>