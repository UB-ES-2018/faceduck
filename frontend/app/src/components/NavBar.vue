<template>
    <nav class = 'navbar navbar-light'>
        <h1 class="title">Faceduck</h1>
        <SearchBar v-bind:redirect="!searchPage" v-if="user"/>
        <form class="form-inline" v-if="user">
    
            <div class="mr-sm-2">
                <router-link to="/profile">{{user.username}}</router-link>
            </div>
            <div class="mr-sm-2">
                <router-link to="/wall">Wall</router-link>
            </div>
            <div class="mr-sm-2">
                <router-link to="/login_logs">Logs</router-link>
            </div>
            <button class="button" v-on:click="logout">Log Out</button>
        </form>
    </nav>
</template>

<script>
    import SearchBar from "./SearchBar.vue";
    
    export default {
        name: "NavBar",
        data() {
            return {
                user: JSON.parse(localStorage.getItem("user")),
                searchPage: (this.$route.name === "search")
            }
        },
        methods: {
            logout: function() {
                localStorage.removeItem("access-token");
                localStorage.removeItem("user");
                this.$router.push("/");
            },
        },
        components: {
            SearchBar
        }
    }
</script>

<style lang="sass" scoped>
@import url("https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css");

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