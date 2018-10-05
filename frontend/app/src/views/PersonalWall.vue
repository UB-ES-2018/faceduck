<template>
  <div id="PersonalWall">
    <h1>This is the Wall</h1>
    <PostForm/>
  </div>
</template>
<script>
import PostForm from "../components/PostForm.vue";

export default {
  name: 'PersonalWall',
  components: {
    PostForm,
  },
};
</script>