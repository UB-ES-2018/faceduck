<template>
  <div id="PersonalWall">
    <h1>This is the Wall</h1>
    
    <div class="container" align="center">
  	  <SearchBar redirect/>
      <PostForm/>
      <PostView/>
    </div>
  </div>
</template>

<script>
import PostForm from "../components/PostForm.vue";
import PostView from "../components/PostView.vue";
import SearchBar from "../components/SearchBar.vue";

export default {
  name: 'PersonalWall',
  components: {
    PostForm,
    PostView,
    SearchBar,
  },
  data() {
		return {}
	},
	beforeCreate: function() {
		if (!localStorage.getItem("access-token")) {
			this.$router.push("/");
		}
	},
	methods: {
		logout: function() {
			localStorage.removeItem("access-token");
			this.$router.push("/");
		}
	}
}

</script>

