import Vue from "vue";
import Router from "vue-router";
import vCatalog from "@/components/catalog/vCatalog";
import vCart from "@/components/cart/vCart";
import vMainPage from "@/components/main-page/vMainPage";

Vue.use(Router);

let router = new Router({
    routes: [
        {
          path: '/',
          name: 'mainPage',
            component: vMainPage
        },
        {
            path: '/catalog',
            name: 'catalog',
            component: vCatalog
        },
        {
            path: '/cart',
            name: 'cart',
            component: vCart,
            props: true
        }
    ]
});

export default router;
