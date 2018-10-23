<template>
  <div id="PersonalWall">
    <NavBar/>
    <h1>This is the Wall</h1>
    <div class="container" align="center">
      <SearchBar redirect/>
      <PostForm/>
      <PostView/>
      <PostsView/>
    </div>
  </div>
</template>

<script>
import NavBar from "../components/NavBar.vue";
import PostForm from "../components/PostForm.vue";
import PostView from "../components/PostView.vue";
import SearchBar from "../components/SearchBar.vue";
import PostsView from "../components/PostsView.vue";

var host = window.location.hostname;
var apiSearchPost = '//' + host + ':5000/post/search';

export default {
  name: 'PersonalWall',
  components: {
    NavBar,
    PostForm,
    PostView,
    SearchBar,
    PostsView,

  },
  data() {
    return {
      user: JSON.parse(localStorage.getItem("user"))
    }
  },
  created() {
    this.getPost()
  },
  updated() {
    this.getPost()
  },
  methods: {
    getPost() {
      fetch(apiSearchPost, {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + localStorage.getItem("access-token"),
          },
          body: JSON.stringify({"author-id": JSON.parse(localStorage.getItem("user"))["id"]})
      }).then(res => res.json())
      .then(data => {
          this.$root.$emit("getPosts", {
            results: data,
          }); 
      }); 
    }
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