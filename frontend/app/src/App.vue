<template>
  <div id="app">
    <div id="nav">
      <router-link to="/">Home</router-link> |
      <router-link to="/about">About</router-link> |
      <router-link to="/wall">Wall</router-link> |
      <router-link to="/vue">Vue</router-link>
    </div>
    <router-view/>
  </div>
</template>

<style lang="scss">
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  background-color: #434547;
  color: #ffb511;
}
#nav {
  a {
    font-weight: bold;
    color: #ffb511;
    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
</style>
