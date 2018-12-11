<template>

<div id="HomePage">
  <h1>Faceduck</h1>
  
  <LoginSignin class="login-signin"/>
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
@import '../assets/global.sass';

#HomePage
  width: 100vw

#HomePage > h1
  margin: 0
  padding-top: 30px
  padding-bottom: 20px
  font-family: "Avenir", Helvetica, Arial, sans-serif
  -webkit-font-smoothing: antialiased
  -moz-osx-font-smoothing: grayscale
  text-align: center
  color: $primary
  text-shadow: 3px 3px #555
  position: relative
  font-size: 15vw
  @media screen and (min-width: $break-small)
    font-size: 84px;
//#HomePage > .login-signin

</style>

