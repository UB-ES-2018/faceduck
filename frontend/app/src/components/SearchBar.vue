<template>
<form class="search-bar" v-on:submit="submitQuery">
  <input type="text" placeholder="Type to search…" v-model="searchQuery">
  <button type="submit">Search</button>
</form>
</template>

<script>
var host = window.location.hostname
var apiUsersSearchUrl  = 'http://'+ host +':5000/user/search'; //Backend ip

export default {
    props: {
      "redirect": Boolean
    },
    data() {
        return {
            searchQuery: ""
        };
    },
    mounted() {
      if (this.$route.name !== "search") return;
      if (this.$route.query.query !== undefined) {
        this.searchQuery = this.$route.query.query;
      }
      this.getUsers();
      this.getPosts();
    },
    methods: {
        //wip
        submitQuery(e) {
          e.preventDefault();
          this.$router.push("/search?query=" + encodeURIComponent(this.searchQuery));
          if (!this.redirect) {
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
          this.$root.$emit("postEvent", {
            "query": this.searchQuery
          });
        },
    }
}
</script>

<style lang="sass" scoped>
@import '../assets/global.sass';

$search-button-width: 100px
$search-border-radius: .4rem

.search-bar
  display: flex
  flex-direction: row
  align-items: center

.search-bar > *
  font-size: 17px
  padding: 6px 5px 4px 5px
  border: 1px solid grey

.search-bar > input
  padding-left: 10px
  border-radius: $search-border-radius 0 0 $search-border-radius
  width: calc(100% - #{$search-button-width})
  z-index: 0

.search-bar > button
  font-weight: bold
  margin-left: -5px
  border-radius: 0 $search-border-radius $search-border-radius 0
  width: $search-button-width
  background-color: $accent3
  color: white
  outline: none
  cursor: pointer

</style>
