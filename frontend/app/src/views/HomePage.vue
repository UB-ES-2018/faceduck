<template>
<div id="head">
  <div id="HomePage">
    <div>
      <h1 class="title">Faceduck</h1>          
    </div>
  </div>
  <LoginSignin/>
  </div>
  
</template>

<script>
import LoginSignin from "../components/LoginSignin.vue";

export default {
  name: 'HomePage',
  components: {
    LoginSignin,
  },
};
</script>

<style lang="sass" scoped> 
#head
  top: 25%

#HomePage
  width: 50%
  transform: translate(-50%, -50%)
  position: absolute
  top: 10%
  left: 50%
  padding: 40px 0
  border-radius: 10px

.title
  font-family: "Avenir", Helvetica, Arial, sans-serif
  -webkit-font-smoothing: antialiased
  -moz-osx-font-smoothing: grayscale
  text-align: center
  color: #ffb511
  text-shadow: 3px 3px #555
  position: relative
  font-size: 450%

.but_sign
  font-size: 100%
  display: inline-block
  padding: 0.4em 1.2em
  border: 0.094em solid #ffb451
  border-radius: 0.625em
  background-color: #ffb511
  box-shadow: 0 0.375em 0.313em -0.313em rgba(0, 0, 0, 0.8), inset 0 0.063em rgba(255, 255, 255, 0.4), inset 0 -0.15em rgba(0, 0, 0, 0.15)
  color: #FFF
  text-decoration: none
  text-transform: uppercase
  text-shadow: 0 0.063em #000
  cursor: pointer
  font: bold 1.8rem "Avenir"
  &:not(last-child)
    margin-right: 10px
  &:hover
    background-color: #ffb516
    box-shadow: 0 0.125em 0.05em -0.05em rgba(255, 255, 255, 0.4), inset 0 0.063em rgba(255, 255, 255, 0.4), inset 0 -0.15em rgba(0, 0, 0, 0.15)
  &:active
    box-shadow: inset 0 0 1.094em #ffb451, inset 0 0.063em #ffb351, inset 0 -0.188em #ffe451, 0 0.063em rgba(255, 255, 255, 0.4)
</style>

