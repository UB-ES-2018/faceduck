<template>
    <div class="container">
    <div class="backbox">
      <div class="loginMsg">
        <div class="textcontent">
          <p class="title">Don't have an account?</p>
          <p>Sign up to save all your graph.</p>
          <button id="switch1">Sign Up</button>
        </div>
      </div>
      <div class="signupMsg visibility">
        <div class="textcontent">
          <p class="title">Have an account?</p>
          <p>Log in to see all your collection.</p>
          <button id="switch2">LOG IN</button>
        </div>
      </div>
    </div>
    <!-- backbox -->

    <div class="frontbox">
      <div class="login">
        <h2>LOG IN</h2>
        <div class="inputbox">
          <input type="text" name="email" placeholder="  EMAIL">
          <input type="password" name="password" placeholder="  PASSWORD">
        </div>
        <p>FORGET PASSWORD?</p>
        <button>LOG IN</button>
      </div>

      <div class="signup hide">
        <h2>SIGN UP</h2>
        <div class="inputbox">
          <input type="text" name="fullname" placeholder="  FULLNAME">
          <input type="text" name="email" placeholder="  EMAIL">
          <input type="password" name="password" placeholder="  PASSWORD">
        </div>
        <button>SIGN UP</button>
      </div>

    </div>
    <!-- frontbox -->
  </div>
</template>


<script>
export default {
    name: 'LoginSignin',
  props: {}
}
var $loginMsg = $('.loginMsg'),
  $login = $('.login'),
  $signupMsg = $('.signupMsg'),
  $signup = $('.signup'),
  $frontbox = $('.frontbox');

$('#switch1').on('click', function() {
  $loginMsg.toggleClass("visibility");
  $frontbox.addClass("moving");
  $signupMsg.toggleClass("visibility");

  $signup.toggleClass('hide');
  $login.toggleClass('hide');
})

$('#switch2').on('click', function() {
  $loginMsg.toggleClass("visibility");
  $frontbox.removeClass("moving");
  $signupMsg.toggleClass("visibility");

  $signup.toggleClass('hide');
  $login.toggleClass('hide');
})

setTimeout(function(){
  $('#switch1').click()
},1000)

setTimeout(function(){
  $('#switch2').click()
},3000)

</script>

<style <style lang="sass" scoped>

body
  background-color: #A8A8A8
  font-family: 'Roboto', sans-serif

.container
  //border:1px solid white
  width: 600px
  height: 350px
  position: absolute
  top: 50%
  left: 50%
  transform: translate(-50%, -50%)
  display: inline-flex

.backbox
  background-color: #404040
  width: 100%
  height: 80%
  position: absolute
  transform: translate(0, -50%)
  top: 50%
  display: inline-flex

.frontbox
  background-color: white
  border-radius: 20px
  height: 100%
  width: 50%
  z-index: 10
  position: absolute
  right: 0
  margin-right: 3%
  margin-left: 3%
  transition: right .8s ease-in-out

.moving
  right: 45%

.loginMsg, .signupMsg
  width: 50%
  height: 100%
  font-size: 15px
  box-sizing: border-box

.loginMsg .title, .signupMsg .title
  font-weight: 300
  font-size: 23px

.loginMsg p, .signupMsg p
  font-weight: 100

.textcontent
  color: white
  margin-top: 65px
  margin-left: 12%

.loginMsg button, .signupMsg button
  background-color: #404040
  border: 2px solid white
  border-radius: 10px
  color: white
  font-size: 12px
  box-sizing: content-box
  font-weight: 300
  padding: 10px
  margin-top: 20px

/* front box content

.login, .signup
  padding: 20px
  text-align: center

.login h2, .signup h2
  color: #35B729
  font-size: 22px

.inputbox
  margin-top: 30px

.login input, .signup input
  display: block
  width: 100%
  height: 40px
  background-color: #f2f2f2
  border: none
  margin-bottom: 20px
  font-size: 12px

.login button, .signup button
  background-color: #35B729
  border: none
  color: white
  font-size: 12px
  font-weight: 300
  box-sizing: content-box
  padding: 10px
  border-radius: 10px
  width: 60px
  position: absolute
  right: 30px
  bottom: 30px
  cursor: pointer

/* Fade In & Out

.login p
  cursor: pointer
  color: #404040
  font-size: 15px

.loginMsg, .signupMsg
  //opacity: 1;
  transition: opacity .8s ease-in-out

.visibility
  opacity: 0

.hide
  display: none

</style>
