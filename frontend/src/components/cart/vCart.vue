<template>
  <div class="v-cart">
    <router-link :to="{name: 'catalog'}">
      <div class="v-catalog__link_to_homepage">Back to homepage</div>
    </router-link>
    <h2>CART</h2>
    <p v-if="!cart_data.length">No products in cart...</p>
    <v-cart-item
      v-for="(item, index) in cart_data"
      :key="item.article"
      :cart_item_data="item"
      @deleteFromCart="deleteFromCart(index)"
      @decrement="decrement(index)"
      @increment="increment(index)"
    />
    <div class="v-cart__total">
      <p class="total_name">Total:</p>
      <p>{{cartTotalCost | toFixed | formattedPrice}}</p>
    </div>
  </div>
</template>

<script>
import vCartItem from "@/components/cart/vCartItem";
import {mapActions} from "vuex"
import toFixed from "@/filters/toFixed";
import formattedPrice from "@/filters/priceFormat";
export default {
  name: "vCart",
  components: {vCartItem},
  props: {
    cart_data: {
      type: Array,
      default() {
        return []
      }
    }
  },
  methods: {
    ...mapActions([
      'DELETE_FROM_CART',
      'INCREMENT_CART_ITEM',
      'DECREMENT_CART_ITEM'
    ]),
    deleteFromCart(index) {
      this.DELETE_FROM_CART(index)
    },
    increment(index) {
      this.INCREMENT_CART_ITEM(index)
    },
    decrement(index) {
      this.DECREMENT_CART_ITEM(index)
    }
  },
  computed: {
    cartTotalCost() {
        let result = [];
      if (this.cart_data.length) {
        for (let item of this.cart_data) {
          result.push(item.price * item.quantity)
        }
        result = result.reduce((sum, el) => sum + el)
        return result;
      } else {
        return 0;
      }
    }
  },
  filters: {
    toFixed,
    formattedPrice
  }
}
</script>

<style lang="scss">
.v-cart{
  margin-bottom: 100px;

  &__total{
    position: fixed;
    bottom: 0;
    right: 0;
    left: 0;
    padding: $padding*2 $padding*3;
    display: flex;
    justify-content: center;
    background: #2e9615;
    color: #fff;
    font-size: 20px;
  }
  .total_name {
    margin-right: $margin*2;
  }
}
</style>
