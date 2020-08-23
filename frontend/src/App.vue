<template>
  <div id="app">
    <v-main-wrapper/>
  </div>
</template>

<script>
import VMainWrapper from "@/components/vMainWrapper";
import {mapActions, mapGetters} from 'vuex';

export default {
  name: 'App',
  components: {VMainWrapper},
  mounted() {
    let vm = this
    window.addEventListener('resize', () => {
      if (window.innerWidth > 767) {
        vm.SET_DESKTOP()
        console.log(vm.IS_DESKTOP, 'desktop',  vm.IS_MOBILE, 'mobile')
     } else {
        vm.SET_MOBILE()
        console.log(vm.IS_MOBILE, 'mobile',vm.IS_DESKTOP, 'desktop')
      }
    })
  },
  methods: {
    ...mapActions([
        'SET_MOBILE',
        'SET_DESKTOP',

    ])
  },
  computed: {
    ...mapGetters([
        'IS_MOBILE',
        'IS_DESKTOP'
    ])
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 160px;
}
</style>
