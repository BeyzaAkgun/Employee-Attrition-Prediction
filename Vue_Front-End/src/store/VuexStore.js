import Vuex from 'vuex';

const store = new Vuex.Store({
    state: {
      isAuth: false,
    },
    mutations: {
      setIsAuth(state, value) {
        state.isAuth = value;
      }
    },
    actions: {
        setAuth({ commit }, value) {
          commit('setIsAuth', value);
        } 
      }
    });
    
    export default store; 