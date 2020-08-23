<template>
  <div class="v-cart-item">
    <img :src="cart_item_data.image"
         :alt="cart_item_data.image"
         class="v-cart-item__image"
    />
    <div class="v-cart-item__info">
      <p>{{ cart_item_data.name }}</p>
      <p>{{ cart_item_data.article }}</p>
      <p>{{ cart_item_data.price | toFixed | formattedPrice}}</p>
    </div>
    <div class="v-cart-item__quantity">
      <p>Quantity:</p>
      <span>
          <span class="quantity_btn" @click="decrementItem"> - </span>
       {{ cart_item_data.quantity }}
        <span class="quantity_btn" @click="incrementItem"> + </span>
      </span>
    </div>
    <button @click="deleteFromCart">Delete</button>
  </div>
</template>

<script>
import toFixed from "@/filters/toFixed";
import formattedPrice from "@/filters/priceFormat";
export default {
  name: "vCartItem",
  props: {
    cart_item_data: {
      type: Object,
      default() {
        return {}
      }
    }
  },
  mounted() {
    this.$set(this.cart_item_data, 'quantity', 1)
  },
  methods: {
    deleteFromCart() {
      this.$emit('deleteFromCart')
    },
    decrementItem() {
      this.$emit('decrement');
    },
    incrementItem() {
      this.$emit('increment');
    }
  },
  filters: {
    toFixed,
    formattedPrice
  }
}
</script>

<style lang="scss">
.v-cart-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: nowrap;
  box-shadow: 0 0 8px 0 #e0e0e0;
  padding: $padding*2;
  margin-bottom: $margin*2;

  &__image {
    max-width: 50px;
  }
  .quantity_btn {
    cursor: pointer;
  }
}
</style>
