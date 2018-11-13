<template>
  <div id="PersonalPage" >
    <NavBar/>
    <div class="containerPhoto" align="center">
        <div class="photo"></div>
        <div class="username" v-bind:userName="user.username">
          {{ user.username }}
        </div>
    </div>
    <div class="container" align="center">
       <PostForm/>
       <PostList v-bind:authorId="user.id"/>
    </div>
  </div>
</template>

<script>
import NavBar from "../components/NavBar.vue";
import PostForm from "../components/PostForm.vue";
import PostList from "../components/PostList.vue";

var host = window.location.hostname;
var apiSearchPost = '//' + host + ':5000/post/search';

export default {
  name: 'PersonalPage',
  components: {
    NavBar,
    PostForm,
    PostList
  },
  data() {
    return {
      user: JSON.parse(localStorage.getItem("user"))
    }
  },
  created() {},
  updated() {},
	methods: {}
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

.containerPhoto
    min-width: 100%
    background: #ffb511
    height: 25vh
    box-shadow: inset 0 -120px 120px -120px black, inset 0 -120px 120px -100px black
    
.photo
    border-radius: 100%
    background-color: gray
    height: 15vh
    width: 15vh

.username
    color: black
    font-size: 4vh

</style>