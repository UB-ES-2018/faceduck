<template>
  <div id="PersonalWall">
    <div>
      <h1>This is the Wall</h1>
    </div>
    <div class="container" align="center">
      <PostView/>
    </div>
  </div>
</template>

<script>
import PostView from "../components/PostView.vue";

export default {
  name: 'PersonalWall',
  components: {
    PostView,
  },
};
</script>