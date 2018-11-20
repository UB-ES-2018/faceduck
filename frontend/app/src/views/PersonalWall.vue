<template>
  <div id="PersonalWall">
    <NavBar/>
    <div class="container" align="center">
      <!--<SearchBar redirect/>-->
      <PostForm/>
      <PostList newsfeed/>
    </div>
  </div>
</template>

<script>
import NavBar from "../components/NavBar.vue";
import SearchBar from "../components/SearchBar.vue";
import PostForm from "../components/PostForm.vue";
import PostList from "../components/PostList.vue";

export default {
  name: 'PersonalWall',
  components: {
    NavBar,
    SearchBar,
    PostForm,
    PostList
  },
  data() {
    return {};
  }
}

</script>

<style lang="sass" scoped>

  .title
    font-family: "Avenir", Helvetica, Arial, sans-serif
    text-align: center
    color: #ffb511
    text-shadow: 3px 3px #555
    font-size: 25px

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