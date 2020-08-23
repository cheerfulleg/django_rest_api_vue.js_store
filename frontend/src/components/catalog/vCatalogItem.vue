<template>
  <div class="v-catalog-item">
    <v-popup
      v-if="isInfoPopupVisible"
      @closePopup="closeInfoPopup"
      @btnAction="addToCart"
      btnTitle="Add to cart"
      :popupTitle="product_data.name"
    >
      <div>
        <img :src="product_data.image"
             :alt="product_data.image"
             class="v-catalog-item__image"
             @click="showPopupInfo"
        >
        <p class="v-catalog-item__name">Name: {{ product_data.name }}</p>
        <p class="v-catalog-item__price">Price: {{ product_data.price | toFixed | formattedPrice}}</p>
      </div>
    </v-popup>

    <img :src="product_data.image"
         :alt="product_data.image"
         class="v-catalog-item__image">
    <p class="v-catalog-item__name">Name: {{ product_data.name }}</p>
    <p class="v-catalog-item__price">Price: {{ product_data.price | toFixed | formattedPrice}}</p>
    <div>
      <button
          class="v-catalog-item__show-info btn"
          @click="showPopupInfo"
      >
        Show info
      </button>
    </div>
    <button class="v-catalog-item__add_to_cart_btn btn"
            @click="addToCart">
      Add to cart
    </button>
  </div>
</template>

<script>
import vPopup from "@/components/popup/vPopup";
import toFixed from "@/filters/toFixed";
import formattedPrice from "@/filters/priceFormat";
export default {
  name: "vCatalogItem",
  components: {vPopup},
  props: {
    product_data: {
      type: Object,
      default() {
        return {}
      }
    },

  },
  data() {
    return {
      isInfoPopupVisible: false
    }
  },
  methods: {
    addToCart() {
      this.$emit('addToCart',this.product_data)
    },
    showPopupInfo() {
      this.isInfoPopupVisible = !this.isInfoPopupVisible;
    },
    closeInfoPopup() {
      this.isInfoPopupVisible = false
    }
  },
  filters: {
    toFixed,
    formattedPrice
  }

}
</script>

<style lang="scss">
.v-catalog-item {
  flex-basis: 25%;
  box-shadow: 0 0 8px 0 #e0e0e0;
  padding: $padding*2;
  margin-bottom: $margin*2;
  margin-left: $margin;
  margin-right: $margin;

  &__show-info{
    margin-bottom: 5px;
    background: #aeaeae !important;
  }

  &__image {
    width: 100px;
  }
}
</style>
