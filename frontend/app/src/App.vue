<template>
  <div id="app">
    <nav>
      <router-link to="/">Home</router-link> |
      <router-link to="/about">About</router-link> |
      <router-link to="/wall">Wall</router-link>
    </nav>
    <router-view/>
  </div>
</template>

<style lang="sass">
@import '../node_modules/bootstrap/scss/bootstrap.scss';

html 
  height: 100%


body 
  background-color: #404040
  height: 100%
  display: flex


#app 
  font-family: 'Avenir', Helvetica, Arial, sans-serif
  -webkit-font-smoothing: antialiased
  -moz-osx-font-smoothing: grayscale
  text-align: center
  background-color: #404040
  color: #ffb511
  margin: 0
  flex-grow: 1


nav 
  a 
    font-weight: bold
    color: #ffb511
    &.router-link-exact-active 
      color: #42b983
    
  

</style>
