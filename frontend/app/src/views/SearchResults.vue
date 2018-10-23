<template>
    <div id="SearchResults">
      <NavBar/>
      <h1>Search results</h1>
      <div class="container">
        <SearchBar/>
        <div class="row justify-content-center">
          <SearchUsers class="col-8"/>
        </div>
        <div class="row justify-content-center">
          <SearchPosts class="col-8"/>
        </div>
      </div>
    </div>   
</template>

<script>

import NavBar from "../components/NavBar.vue";
import SearchBar from "../components/SearchBar.vue";
import SearchUsers from "../components/SearchUsers.vue";
import SearchPosts from "../components/SearchPosts.vue";

export default {
    name: "SearchResults",
    data() {
        return{
            results: [],
            nores: false,//ugly way to hide nothing found message
        };
    },
    mounted() {
      this.$root.$on("getResults", (event) => {
        console.log(event)
        this.results = event.results;
        this.nores = (event.results.length === 0);
      });
    },
    components: {
      NavBar,
      SearchBar,
      SearchUsers,
      SearchPosts
    }
}
</script>

<style lang="sass" scoped>
h3
  font-size: 18px;
h4
  font-size: 16px;
</style>

<style lang="sass">
    
.results-item
  border: 10px
  color: white
  font-size: 12px
  font-weight: bold
  box-sizing: content-box
  padding: 10px
  position: relative 
  cursor: pointer
  text-align: left
  //width: 200px

.results-list

.border-b-1
  border-bottom: 1px solid rgba(225,225,225,.16)
</style>