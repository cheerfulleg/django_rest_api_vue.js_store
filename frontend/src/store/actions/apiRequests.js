import axios from "axios";

export default {
    GET_PRODUCTS_FROM_API({commit}) {
        return axios('http://localhost:8000/api/items/', {
            method: "GET"
        })
            .then((products) => {
                commit('SET_PRODUCTS_TO_STATE', products.data);
                return products;
            })
            .catch((error) => {
                console.log(error);
                return error;
            });
    },
    GET_CATEGORIES_FROM_API({commit}) {
        return axios('http://localhost:8000/api/categories/', {
            method: "GET"
        })
            .then((categories) => {
                commit('SET_CATEGORIES_TO_STATE', categories.data);
                return categories;
            })
            .catch((error) => {
                console.log(error);
                return error;
            });
    },
    // ToDo make axios post to api
}
