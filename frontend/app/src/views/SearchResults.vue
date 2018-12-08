<template>
    <div id="SearchResults">
      <NavBar/>
      
      <h1>Search results</h1>
      <div class="container">
        <div class="row justify-content-center">
          <SearchUsers class="col-8"/>
        </div>
        <PostList/>
      </div>
    </div>   
</template>

<script>
// SearchBar unimported, as it is now in the navbar
// import SearchBar from "../components/SearchBar.vue";
import NavBar from "../components/NavBar.vue";
import SearchUsers from "../components/SearchUsers.vue";
import PostList from "../components/PostList.vue";

export default {
    name: "SearchResults",
    data() {
        return {}
    },
    components: {
      // SearchBar,
      NavBar,
      SearchUsers,
      PostList
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
