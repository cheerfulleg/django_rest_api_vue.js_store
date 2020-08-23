<template>
  <div class="v-header">
    <router-link :to="{name: 'mainPage'}">
      <img src="../../assets/logo.png" alt="logo">
    </router-link>
    <router-link :to="{name: 'cart', params: {cart_data: CART}}">
      <div class="v-catalog__link_to_cart">Cart: {{ CART.length }}</div>
    </router-link>
    <div class="search-field">
      <label for="search_input"></label><input
          id="search_input"
          class="search_input"
          type="text"
          v-model="searchValue"
      >
      <button class="search_btn">
        <i class="material-icons" @click="searchItem(searchValue)">search</i>
      </button>
    </div>
  </div>
</template>

<script>
import {mapActions, mapGetters} from "vuex"

export default {
  name: "vHeader",
  data() {
    return {
      searchValue: ''
    }
  },
  methods: {
    ...mapActions([
      'GET_SEARCH_VALUE_TO_VUEX'
    ]),
    searchItem(value) {
      this.GET_SEARCH_VALUE_TO_VUEX(value);
      if (this.$route.path !== '/catalog') {
        this.$router.push('/catalog')
      }
      this.searchValue = ''
    }
  },
  computed: {
    ...mapGetters([
      'SEARCH_VALUE',
      'CART'
    ])
  }
}
</script>

<style lang="scss">
.v-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background: $green-bg;
  padding: 16px;
  position: fixed;
  width: 100%;
  top: 0;
  left: 0;
  z-index: 8;

  img {
    width: 50px;
    height: 50px;
  }

  .search-field {
    padding: 16px;
    position: relative;
    right: 200px;
    display: flex;
    justify-content: center;
    align-items: center;
  }

  .search_input {
    border: 1px solid black;
    background: #f3f3f3;
  }

  .search_btn {
    margin-left: 16px;
    background: transparent;
    border: none;
  }
}


</style>
