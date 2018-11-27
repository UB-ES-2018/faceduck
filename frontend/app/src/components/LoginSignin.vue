<template>
    <div class="container">
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
      <!-- backbox -->

      <div class="frontbox" v-bind:class="{ moving: !loginVisible }">
        <div class="login" v-if="loginVisible">
          <h2>LOG IN</h2>
          <form class="inputbox" v-on:submit="submitLogin">
            <input type="text" name="email" v-model="login.email"
              placeholder="  EMAIL">
            <input type="password" name="password" v-model="login.password"
              placeholder="  PASSWORD">
            <!--<p>FORGOT PASSWORD?</p>-->
            <button type="submit" v-on:click="failedLogin = false"
              v-bind:class="{ shaking: failedLogin }">LOG IN</button>
          </form>
        </div>

        <div class="signup" v-if="!loginVisible">
          <h2>SIGN UP</h2>
          <form class="inputbox" v-on:submit="submitSignup" v-if="!successfulSignup">
            <input type="text" name="username" v-model="signup.username" placeholder= " USERNAME" required>
            <div class="inline-input">
              <input type="text" name="name" v-model="signup.name"
                placeholder="  NAME" required>
              <input type="text" name="surname" v-model="signup.surname"
                placeholder="  SURNAME" required>
            </div>
            <input type="email" name="email" v-model="signup.email"
              placeholder="  EMAIL" required>
            <input type="password" name="password" v-model="signup.password"
              placeholder="  PASSWORD" required>
            <!--<datepicker :format="'dd/MM/yyyy'" v-model="signup.birthday"></datepicker>-->
            <FormDate v-model="signup.birthday" required/>
            <select name="gender" v-model="signup.gender" required>
              <option value="" disabled selected>Select one…</option>
              <option value="male" >Male</option>
              <option value="female">Female</option>
              <option value="other">Other</option>
            </select>
            <button type="submit" v-on:click="failedSignup = false"
              v-bind:class="{ shaking: failedSignup }">SIGN UP</button>
          </form>
          <div class="success" v-if="successfulSignup">
            You signed up correctly

            <button class="login-now" v-on:click="showLogIn">LOGIN NOW!</button>
          </div>
        </div>

      </div>
      <!-- frontbox -->
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

.container
  //border:1px solid white
  width: 600px
  height: 350px
  position: absolute
  top: 45%
  left: 50%
  transform: translate(-50%, -50%)
  display: inline-flex

.backbox
  background-color: $background
  width: 90%
  height: 100%
  position: absolute
  transform: translate(0, -50%)
  top: 50%
  display: inline-flex

.frontbox
  background-color: #ffffff
  border-radius: 20px
  height: 150%
  width: 50%
  z-index: 10
  position: absolute
  right: 0
  margin-right: 3%
  margin-left: 3%
  transition: right .8s ease-in-out

.moving
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

.login, .signup
  padding: 20px
  text-align: center

.login h2, .signup h2
  color: #ffb511
  font-size: 22px

.inputbox
  margin-top: 30px

.login input, .signup input, .signup select
  display: block
  width: 100%
  height: 40px
  background-color: $lightgray
  color: $darkgray
  border: none
  margin-bottom: 20px
  font-size: 12px


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
  & input:not(:last-child)
    margin-right: 5px
  & input
    width: 49%


.success
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

.hide
  display: none

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


</style>