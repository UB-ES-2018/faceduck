<template>

<div id="SearchResults">
  <NavBar/>
  
  <div class="container2">
    <h2>Users</h2>
    <SearchUsers class="search-users"/>
    
    <h2>Posts</h2>
    <PostList class="post-list"/>
    
    <h2>Groups</h2>
    <SearchGroups class="search-groups"/>
  </div>
</div>

</template>

<script>
// SearchBar unimported, as it is now in the navbar
// import SearchBar from "../components/SearchBar.vue";
import NavBar from "../components/NavBar.vue";
import PostList from "../components/PostList.vue";
import SearchGroups from "../components/SearchGroups.vue";
import SearchUsers from "../components/SearchUsers.vue";

export default {
    name: "SearchResults",
    data() {
        return {}
    },
    components: {
      NavBar,
      PostList,
      SearchGroups,
      SearchUsers
    }
}
</script>

<style lang="sass">
@import '../assets/global.sass';

#SearchResults
  & h2
    margin-top: 25px
    margin-bottom: 15px
    font-size: 25px
    color: $darkprimary
  & > .container2
    width: 70%;
    min-width: 320px
    padding-right: 15px;
    padding-left: 15px;
    margin-top: 1.8rem
    margin-right: auto;
    margin-left: auto;
    margin-bottom: 25px
    @media screen and (min-width: 700px)
      max-width: 700px
    & > .post-list
      padding-bottom: 0
    & > .post-list > .row:last-child
      margin-bottom: 0

</style>
