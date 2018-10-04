<template>
    <div id='PostForm'>
        <form id='PostF'>
            <input type="PostTitle" name="title" v-model="post.title" placeholder="Title">
            <input type="PostText" name="text" v-model="post.text" placeholder="Text in here">
            <button class='postbutton'> POST </button>
        </form>
    </div>
</template>

<style lang="sass" scoped>
.postbutton button[type="submit"]
  background-color: #ffb511
  border: none
  color: white
  font-size: 12px
  font-weight: bold
  box-sizing: content-box
  padding: 10px
  border-radius: 10px
  width: 60px
  position: absolute
  right: 30px
  bottom: 30px
  cursor: pointer
</style>

<script>
    export default {
        name: 'PostForm',
        data() {
            return {
                loginVisible: false,
                successfulSignup: false,
                failedSignup: false,
                failedLogin: false,
                post: {
                    title: "",
                    text: ""
                }
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
                }).then((response) => {
                    if (response.ok) {
                        this.successfulSignup = true;
                    } else {
                        // ToDo: highlight bad fields
                        this.failedSignup = true;
                    }
                }).catch((r) => this.failedSignup = true);
            },
            submitLogin(e) {
                e.preventDefault();
                fetch(apiLoginUrl, {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify(this.login)
                }).then((response) => {
                    if (response.ok) {
                        // DO AUTHENTICATION
                    } else {
                        // ToDo: highlight bad fields
                        this.failedLogin = true;
                    }
                }).catch((r) => this.failedSignup = true);
            }
        },
    }
</script>
