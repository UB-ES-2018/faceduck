<template>
  <div id="app">
    <nav>
    </nav>
    <router-view/>
  </div>
</template>

<style lang="sass">
@import url("https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css");

html 
  height: 100%
  background-color: #404040


body 
  background-color: #404040
  height: 100%
  display: flex


#app 
  font-family: 'Avenir', Helvetica, Arial, sans-serif
  -webkit-font-smoothing: antialiased
  -moz-osx-font-smoothing: grayscale
  text-align: center
  color: #ffb511
  margin: 0
  background-color: #404040
  flex-grow: 1


nav 
  a 
    font-weight: bold
    color: #ffb511
    &.router-link-exact-active 
      color: #42b983
    
  

</style>
