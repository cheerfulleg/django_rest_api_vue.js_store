<template>
<div class="v-man-page">
  <h1>Test Shop</h1>
  <div>
    <router-link  class="catalog-link" :to="{name: 'catalog'}"><h2>Go to Catalog</h2></router-link>
  </div>
</div>
</template>

<script>
export default {
  name: "vMain"
}
</script>

<style>
.catalog-link {
  text-decoration: none;
  font-size: 40px;
  position: relative;
  top: 100px;
}
</style>
