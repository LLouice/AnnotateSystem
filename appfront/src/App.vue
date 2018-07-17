<template>
  <div id="app">
    <Home msg="Welcome to Your Vue.js App"/>
  </div>
</template>

<script>
import Home from "./components/Home.vue";

export default {
  name: "app",
  components: {
    Home
  }
};
</script>

<style>
#app {
  font-family: "Source Sans Pro", "Helvetica Neue", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  height: 100%;
}
* {
  margin: 0;
  padding: 0;
}
</style>
