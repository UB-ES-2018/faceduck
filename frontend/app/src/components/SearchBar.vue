<template>
    <div id="search-bar">
        <form class="inputbox" v-on:submit="submitQuery">
          <input type="text" placeholder="username" v-model="searchQuery">
          <button type="submit">Search</button>
        </form>
    </div>
</template>

<script>
var host = window.location.hostname
var apiUsersSearchUrl  = 'http://'+ host +':5000/user/search'; //Backend ip
var apiPostsSearchUrl  = 'http://'+ host +':5000/post/search'; //Backend ip

export default {
    props: {
      "redirect": Boolean
    },
    data() {
        return{
            searchQuery: ""
        };
    },
    mounted() {
      this.searchQuery = this.$route.query.query;
      this.getUsers();
      this.getPosts();
    },
    methods: {
        //wip
        submitQuery(e) {
          e.preventDefault();
          if (this.redirect) {
            this.$router.push("/search?query=" + this.searchQuery);
          } else {
            this.getUsers();
            this.getPosts();
          }
        },
        getUsers() {
          fetch(apiUsersSearchUrl, {
            method: "POST",
            headers: {
              "Content-Type": "application/json",
              "Authorization": "Bearer " + localStorage.getItem("access-token"),
            },
            body: JSON.stringify({query: this.searchQuery})
          }).then(res => res.json())
          .then(data => {
            this.$root.$emit("getUserResults", {
              results: data
            });
          });
        },
        getPosts() {
          fetch(apiPostsSearchUrl, {
            method: "POST",
            headers: {
              "Content-Type": "application/json",
              "Authorization": "Bearer " + localStorage.getItem("access-token"),
            },
            body: JSON.stringify({query: this.searchQuery})
          }).then(res => res.json())
          .then(data => {
            this.$root.$emit("getPostResults", {
              results: data
            });
          });
        },

        
    }
}
</script>

<style lang="sass" scoped>
.inputbox button
  background-color: #ffb511
  border: none
  color: white
  font-size: 12px
  font-weight: bold
  box-sizing: content-box
  padding: 10px
  border-radius: 10px
  width: 60px
  position: relative
  left: 1% 
  cursor: pointer

</style>