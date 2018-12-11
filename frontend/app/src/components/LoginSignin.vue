<template>
<div class="login-signin">
  
  <div class="pretabies">
    <div class="backbox">
      <div class="loginMsg" v-bind:toggleClass="{visible: !loginVisible }">
        <div class="textcontent">
          <p class="title">Don't have an account?</p>
          <p>Sign up and find your friends.</p>
          <button id="switch1" v-on:click="showSignUp">SIGN UP</button>
        </div>
      </div>
      <div class="signupMsg">
        <div class="textcontent">
          <p class="title">Have an account?</p>
          <p>Log in to meet your friends.</p>
          <button id="switch2" v-on:click="showLogIn">LOG IN</button>
        </div>
      </div>
    </div>
  
    <div class="tabies">
      <button v-on:click="showSignUp" v-bind:class="{ 'bu-shadow': loginVisible }">Sign Up</button>
      <button v-on:click="showLogIn" v-bind:class="{ 'bu-shadow': !loginVisible }">Log In</button>
    </div>
    
    <div class="frontbox" v-bind:class="{ moving: !loginVisible }">
      
      <div class="login" v-bind:class="{ hide: !loginVisible }">
        
        <h2>Log In</h2>
        
        <form class="inputbox" v-on:submit="submitLogin">
          <input type="text"
                 name="email"
                 v-model="login.email"
                 placeholder="Email"
                 required>
          <input type="password"
                 name="password"
                 v-model="login.password"
                 placeholder="Password"
                 required>
          
          <button type="submit" v-on:click="failedLogin = false"
                  v-bind:class="{ shaking: failedLogin }">LOG IN</button>
        </form>
        
      </div>
      
      <div class="signup" v-bind:class="{ hide: loginVisible }">
        
        <h2>Sign Up</h2>
        
        <div>
          <div class="success" v-if="successfulSignup">
            You signed up correctly
            
            <button class="login-now" v-on:click="showLogIn">LOGIN NOW!</button>
          </div>
          
          <form class="inputbox" v-on:submit="submitSignup" v-bind:class="{ hide: successfulSignup }">
            <input type="text"
                   name="username"
                   v-model="signup.username"
                   placeholder="Username"
                   required>
            <div class="inline-input">
              <input type="text"
                     name="name"
                     v-model="signup.name"
                     placeholder="Name"
                     required>
              <input type="text"
                     name="surname"
                     v-model="signup.surname"
                     placeholder="Surname"
                     required>
            </div>
            <input type="email"
                   name="email"
                   v-model="signup.email"
                   placeholder="Email"
                   required>
            <input type="password"
                   name="password"
                   v-model="signup.password"
                   placeholder="Password"
                   required>
            <FormDate v-model="signup.birthday" required/>
            <select name="gender" v-model="signup.gender" required>
              <option value="" disabled selected>Select one…</option>
              <option value="male" >Male</option>
              <option value="female">Female</option>
              <option value="other">Other</option>
            </select>
            <button type="submit"
                    v-on:click="failedSignup = false"
                    v-bind:class="{ shaking: failedSignup }">SIGN UP</button>
          </form>
        </div>
        
      </div>
    </div>
    
  </div>
  
</div>

</template>


<script>
import FormDate from "./FormDate.vue"
//import Datepicker from "vuejs-datepicker/";
var host = window.location.hostname;
var apiSignupUrl = '//' + host + ':5000/user';
var apiLoginUrl  = '//' + host + ':5000/session';

export default {
  name: 'LoginSignin',
  components:{
   //Datepicker,
   FormDate,
  },
  data() {
    return {
      loginVisible: false,
      successfulSignup: false,
      failedSignup: false,
      failedLogin: false,
      login: {
        email: "",
        password: ""
      },
      signup: {
        username:"",
        name: "",
        surname: "",
        email: "",
        password: "",
        birthday: "",
        gender: ""
      }
    }
  },
  computed: {
    signupVisible() {
      return !this.loginVisible;
    }
  },
  methods: {
    showSignUp() {
      this.loginVisible = false;
    },

    showLogIn() {
      this.loginVisible = true;
    },
    submitSignup(e) { 
      e.preventDefault();
      fetch(apiSignupUrl, {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify(this.signup)
      }).catch(() => this.failedSignup = true)
      .then((response) => {
        if (response.ok) {
          this.successfulSignup = true;
        } else {
          // ToDo: highlight bad fields
          this.failedSignup = true;
        }
      });
    },
    submitLogin(e) {
      e.preventDefault();
      fetch(apiLoginUrl, {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify(this.login)
      }).catch(() => this.failedSignup = true)
      .then((response) => {
        if (response.ok) {
          response.json().then((json) => {
            localStorage.setItem("access-token",
              json["access-token"]);
            localStorage.setItem("user",
              JSON.stringify(json["user"]));
            this.$router.push("/wall");
          });
        } else {
          // ToDo: highlight bad fields
          this.failedLogin = true;
        }
      });
    }
  },
};
</script>

<style lang="sass" scoped>
@import '../assets/global.sass';

.login-signin
  position: relative
  height: auto
  display: flex
  flex-direction: column
  align-items: center
  width: 100%
  @media screen and (min-width: $break-login)
    display: inline-flex
    width: 60%
    max-width: 700px
    min-width: 650px
 
.pretabies
  position: relative
  height: auto
  display: flex
  flex-direction: column
  align-items: center
  width: auto
  @media screen and (min-width: $break-login)
    display: inline-flex
    width: 60%
    max-width: 700px
    min-width: 650px
  
.backbox
  display: none
  @media screen and (min-width: $break-login)
    display: inline-flex
    background-color: $background
    width: 90%
    height: 100%
    
.tabies
  display: flex
  flex-direction: row
  box-shadow: 3px 3px 5px #888888;
  border-radius: 8px 8px 0 0
  background-color: $gray
  width: 100%
  @media screen and (min-width: $break-login)
    display: none

.tabies > button
  border: 0.5px solid $darkestprimary
  border-bottom: 0
  border-radius: 8px 8px 0 0
  background-color: $lightgray
  padding: 15px
  padding-top: 8px
  padding-bottom: 3px
  margin-bottom: -2px
  z-index: 1
  color: $darkgray
  font-size: 22px
  font-weight: bold
  outline: none
  width: 50%
  &:first-child
    border-radius: 8px 0 0 0
    border-right: 0
  &:last-child
    border-radius: 0 8px 0 0
    border-left: 0.5px solid $darkgray

.bu-shadow
  background-color: $gray
  opacity: 0.7
  border-bottom: 0.5px solid $darkgray

.frontbox
  position: relative
  height: 100%
  border: 0.5px solid $darkestprimary
  box-shadow: 3px 3px 5px #888888;
  border-radius: 0 0 20px 20px
  background-color: $lightgray
  @media screen and (min-width: $break-login)
    height: auto
    border-radius: 20px
    width: 50%
    position: absolute
    right: 0
    margin-right: 3%
    margin-left: 3%
    transition: right .8s ease-in-out
    
.moving
  @media screen and (min-width: $break-login)
    right: 50%
    

.loginMsg, .signupMsg
  width: 75%
  height: 100%
  font-size: 15px
  box-sizing: border-box
  
.loginMsg .title, .signupMsg .title
  font-weight: 300
  font-size: 23px
  
.loginMsg p, .signupMsg p
  font-weight: 100
  
.textcontent
  color: $darkestgray
  margin-top: 65px
  margin-left: 5%
  
.loginMsg button, .signupMsg button
  background-color: $background
  border: 2px solid $darkestgray
  border-radius: 10px
  color: $darkestgray
  font-size: 12px
  box-sizing: content-box
  font-weight: 300
  padding: 10px
  margin-top: 20px
  
/* front box content */
  
.login
  z-index: 1
  //height: 100%
  width: 100%
  position: absolute
  
.signup
  height: 100%
  @media screen and (min-width: $break-login)
    height: auto
  
.login, .signup
  padding: 20px
  text-align: center
  
.login h2, .signup h2
  display: none
  @media screen and (min-width: $break-login)
    display: inline
    color: $darkgray
    font-size: 26px
    font-weight: bold
  
.inputbox
  margin-top: 18px
  
.login input, .signup input, .signup select
  display: block
  width: 100%
  height: 40px
  background-color: white
  color: $darkgray
  border: 0.5px solid $gray
  margin-bottom: 20px
  font-size: 12px

.signup > div
  position: relative

.inputbox button[type="submit"]
  background-color: #ffb511
  border: none
  color: #ffffff
  font-size: 12px
  font-weight: bold
  box-sizing: content-box
  padding: 10px
  border-radius: 10px
  width: 60px
  bottom: -10%
  cursor: pointer
  
button.login-now 
  background-color: #ffb511
  border: none
  color: white
  font-size: 12px
  font-weight: bold
  box-sizing: content-box
  padding: 10px
  border-radius: 10px
  margin-top: 10px
  width: 100px
  cursor: pointer
  
.inline-input 
  display: flex
  width: 100%
  position: relative
  & input:not(:last-child)
    margin-right: 5%
    width: 41%
  & input:last-child
    width: 54%

input
  padding-left: 10px
      
input::placeholder
  font-size: 15px
    
.success
  position: absolute
  width: 100%
  display: flex
  flex-direction: column
  align-items: center
  z-index: 2
  color: #008000
  font-weight: bold
  text-align: center
  
/* Fade In & Out */
  
.login p
  cursor: pointer
  color: #404040
  font-size: 15px

.loginMsg, .signupMsg
  //opacity: 1;
  transition: opacity .5s ease-in-out

.visibility
  opacity: 0

/* Button shake */

.shaking
  animation: shake 0.82s cubic-bezier(.36,.07,.19,.97) both;

@keyframes shake 
  10%, 90% 
    transform: translate3d(-1px, 0, 0);
  
  20%, 80% 
    transform: translate3d(2px, 0, 0);

  30%, 50%, 70% 
    transform: translate3d(-4px, 0, 0);

  40%, 60% 
    transform: translate3d(4px, 0, 0);

.hide
  opacity: 0
  z-index: -1


</style>
