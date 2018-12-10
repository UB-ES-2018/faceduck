<template>

<div id="personal-wall">
  <NavBar class="navbar"/>
  
  <div class="container2">
    <PostForm/>
    <PostList newsfeed/>
  </div>
</div>

</template>

<script>
import NavBar from "../components/NavBar.vue";
import PostForm from "../components/PostForm.vue";
import PostList from "../components/PostList.vue";
import SearchBar from "../components/SearchBar.vue";

export default {
  name: 'PersonalWall',
  components: {
    NavBar,
    PostForm,
    PostList,
    SearchBar
  },
  data() {
    return {};
  }
}

</script>

<style lang="sass" scoped>
@import '../assets/global.sass';

#personal-wall
  min-width: 320px
  width: 100vw

.container2
  width: 70%;
  min-width: 320px
  padding-right: 15px;
  padding-left: 15px;
  margin-top: 1.8rem
  margin-right: auto;
  margin-left: auto;
  @media screen and (min-width: 700px)
    max-width: 700px

</style>
