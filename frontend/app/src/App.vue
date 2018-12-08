<template>
<div id="app">
  <router-view/>
</div>
</template>

<style lang="sass">
@import url("https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css");
@import 'assets/global.sass';

body
  width: 100%
  height: 100%
  background-color: $background
  display: flex

#app 
  font-family: 'Avenir', Helvetica, Arial, sans-serif
  -webkit-font-smoothing: antialiased
  -moz-osx-font-smoothing: grayscale
  text-align: center
  color: #ffb511
  margin: 0
  background-color: $background
  flex-grow: 1

nav 
  a 
    font-weight: bold
    color: #ffb511
    &.router-link-exact-active 
      color: #42b983

</style>
