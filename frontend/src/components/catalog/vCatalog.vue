<template>
  <div class="v-catalog">
    <h1>CATALOG</h1>
    <vLoader
        v-if="loading"
        :loading="loading"/>
    <div v-else class="filters">
      <v-select
          :selected="selected"
          :options="categories"
          @select="sortByCategories"
      />

      <div class="range-slider">
        <input
            type="range"
            min="0"
            max="10000"
            step="10"
            v-model.number="minPrice"
            @change="setRangeSlider">
        <input
            type="range"
            min="0"
            max="10000"
            step="10"
            v-model.number="maxPrice"
            @change="setRangeSlider"
        >
      </div>
      <div class="range-values">
        <p>Min: {{ minPrice }}</p>
        <p>Max: {{ maxPrice }}</p>
      </div>
    </div>

    <div class="v-catalog__list">
      <v-catalog-item v-for="product in filteredProducts"
                      :key="product.article"
                      :product_data="product"
                      @addToCart="addToCart"
      />
    </div>
  </div>
</template>
<script>
import vCatalogItem from "@/components/catalog/vCatalogItem";
import {mapActions, mapGetters} from "vuex";
import vSelect from "@/components/vSelect";
import vLoader from "@/components/vLoader";


export default {
  name: "vCatalog",
  components: {vCatalogItem, vSelect, vLoader},
  data() {
    return {
      categories: [],
      selected: 'Все',
      sortedProducts: [],
      minPrice: 0,
      maxPrice: 10000,
      loading: false
    }
  },
  methods: {
    addToCart(data) {
      this.ADD_TO_CART(data)
    },
    ...mapActions([
      'GET_PRODUCTS_FROM_API',
      'GET_CATEGORIES_FROM_API',
      'ADD_TO_CART'
    ]),
    sortByCategories(category) {
      let vm = this;

      this.sortedProducts = [...this.PRODUCTS];
      this.sortedProducts = this.sortedProducts.filter((item) => {
        return item.price >= vm.minPrice && item.price <= vm.maxPrice;
      })
      if (category) {
        this.sortedProducts = this.sortedProducts.filter((item) => {
          vm.selected = category.name
          return item.category === category.name
        })
      }
    },
    setRangeSlider() {
      if (this.minPrice > this.maxPrice) {
        let tmp = this.maxPrice;
        this.maxPrice = this.minPrice;
        this.minPrice = tmp;
      }
      this.sortByCategories()
    },
    sortProductsBySearchValue(value) {
      this.sortedProducts = [...this.PRODUCTS];
      if (value) {
        this.sortedProducts = this.sortedProducts.filter((item) => {
          return item.name.toLowerCase().includes(value.toLowerCase())
        })
      } else {
        this.sortedProducts = this.PRODUCTS;
      }
    },
    setCategories(){
      this.categories = this.CATEGORIES
    }
  },
  watch: {
    SEARCH_VALUE() {
      this.sortProductsBySearchValue(this.SEARCH_VALUE)
    }
  }
  ,
  computed: {
    ...mapGetters([
          'PRODUCTS',
          'CATEGORIES',
          'CART',
          'IS_MOBILE',
          'IS_DESKTOP',
          'SEARCH_VALUE'
        ]),
    filteredProducts() {
      if (this.sortedProducts.length) {
        return this.sortedProducts;
      } else {
        return this.PRODUCTS;
      }
    }
  }
  ,
  mounted() {
    this.loading = true;
    this.GET_PRODUCTS_FROM_API()
        .then((response) => {
          if (response.data) {
            this.sortByCategories()
            this.sortProductsBySearchValue(this.SEARCH_VALUE)
          }
        }).finally(() => this.loading = false);
    this.GET_CATEGORIES_FROM_API()
        .then((response) => {
          if (response.data) {
            this.setCategories()
          }
        });
  },

}
</script>


<style lang="scss">
.v-catalog {
  &__list {
    margin-top: 10px;
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
    align-items: center;
  }

  &__link_to_cart {
    position: absolute;
    top: 20px;
    right: 100px;
    padding: $padding*2;
    border: solid 1px black;
  }
  &__link_to_homepage {
    position: fixed;
    top: 120px;
    right: 10px;
    padding: $padding*2;
    border: solid 1px #aeaeae;
    background: #ffffff;
  }
}

.filters {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.range-slider {
  width: 300px;
  margin: auto 16px;
  text-align: center;
  position: relative;
  left: 600px;
}
.range-slider svg, .range-slider input[type=range] {
  position: absolute;
  left: 0;
  bottom: 0;

}
input[type=range]::-webkit-slider-thumb {
  //z-index: 1;
  position: relative;
  top: 2px;
  margin-top: -7px;
  background: #000;
}

.range-values {
  margin-top: 20px;
  margin-right: $margin*2;
}
</style>
