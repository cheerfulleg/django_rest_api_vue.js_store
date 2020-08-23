import Vue from "vue";
import Vuex from "vuex";
import getters from "@/store/getters/getters";
import apiRequests from "@/store/actions/apiRequests";
import commonActions from "@/store/actions/commonActions";
import mutations from "@/store/mutations/mutations";

Vue.use(Vuex);

const actions = {...commonActions, ...apiRequests}

let store = new Vuex.Store({
    state: {  //данные
        products: [],
        cart: [],
        categories: [],
        isMobile: false,
        isDesktop: true,
        searchValue: ''
    },
    mutations,  //тут меняеться state sync
    actions, //async
    getters//путь до информации в state
});

export default store;
