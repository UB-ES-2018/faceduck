<template>
  <div id="PersonalWall">
    <h1>This is the Wall</h1>
    
    <div class="container" align="center">
      <PostForm/>
      <PostView/>
    </div>
  </div>
</template>
<script>
import PostForm from "../components/PostForm.vue";
import PostView from "../components/PostView.vue";

export default {
  name: 'PersonalWall',
  components: {
    PostForm,
    PostView,

  },
};
</script>