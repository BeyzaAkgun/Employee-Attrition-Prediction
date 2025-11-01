import './assets/main.css'

import { createApp, reactive } from 'vue'
import App from './App.vue'
import router from './router'
import VuexStore from './store/VuexStore'

const app = createApp(App);

const isAuthenticated = localStorage.getItem('isAuth') === 'true';


VuexStore.commit('setIsAuth', isAuthenticated);

 
//const isAuthenticated = VuexStore.state.isAuth;

//const token = VuexStore.state.token;
//VuexStore.commit('setIsAuth', isAuthenticated);
//VuexStore.commit('setIsToken', token);

const state = reactive({
    isAuthenticated
  });
app.provide('vuexStore', VuexStore);
app.provide('authState', state);
app.use(VuexStore) 
app.use(router)
app.mount('#app')

