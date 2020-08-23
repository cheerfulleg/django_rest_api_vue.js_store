<template>
  <div class="v-main-wrapper">
    <v-header/>
    <router-view></router-view>
  </div>
</template>

<script>
import VHeader from "@/components/layouts/vHeader";
export default {
  name: "v-main-wrapper",
  components: {VHeader},
  // components: {vCatalog, vCart},
  props: {},  //то что прилетает из другого компонента
  data() {   //данные самого компонента
    return {
      title: "Main wrapper"
    }
  },
  computed: {},
  methods: {},  //штуки которые отвечают за клики, показы чего-либо, запуск анимаций...
  watch: {} //наблюдатели
}
</script>

<style>
.v-main-wrapper {
  margin: 0 auto;
}
</style>
