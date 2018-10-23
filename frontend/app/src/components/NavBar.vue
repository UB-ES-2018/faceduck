<template>
<nav class="navbar navbar-light" style="background-color: pale-sky;">
    <h1 class="title">Faceduck</h1>
      <form class="form-inline">
        <div class="page mr-sm-2"> 
            <router-link to="/profile">{{user.username}}</router-link>
        </div>
        <div class="page my-2 mr-sm-2">
            <router-link to="/wall">Wall</router-link>
        </div>
        <button class="button" v-on:click="logout">Log Out</button>
    </form>
</nav>
</template>

<script>
export default {
    name: "NavBar",
    data() {
      return {
        user: JSON.parse(localStorage.getItem("user"))
      }
    },
    methods: {
        logout: function() {
            localStorage.removeItem("access-token");
            this.$router.push("/");
        },
    }
}
</script>

<style lang="sass" scoped>
.button
  background-color: #ffb511
  border: none
  color: white
  font-size: 12px
  font-weight: bold
  box-sizing: content-box
  padding: 10px
  border-radius: 10px
  width: 60px
  left: 40% 
  cursor: pointer
</style>