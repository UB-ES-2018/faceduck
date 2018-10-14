<template>
  <div id="PersonalWall">
    <nav class="navbar navbar-light" style="background-color: pale-sky;">
        <h1 class="title">Faceduck</h1>
          <form class="form-inline">
            <div class="page mr-sm-2" v-on:click='profile'> User </div>
            <div class="page my-2 mr-sm-2" v-on:click='wall'>Wall</div>
            <button class="button" v-on:click='logout'> Log Out </button>
          </form>
    </nav>
    <h1>This is the Wall</h1>
    <div class="container" align="center">
      <PostForm/>
      <PostView/>
    </div>
  </div>
</template>

<style lang="sass" scoped>

.title
  font-family: "Avenir", Helvetica, Arial, sans-serif
  text-align: center
  color: #ffb511
  text-shadow: 3px 3px #555
  font-size: 25px

.page
  color: #ffb511
  cursor: pointer

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

<script>
import PostForm from "../components/PostForm.vue";
import PostView from "../components/PostView.vue";

export default {
  name: 'PersonalWall',
  components: {
    PostForm,
    PostView,

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
    profile () {
			this.$router.push("/profile");
    },
    wall () {
			this.$router.push("/wall");
		},
		logout: function() {
			localStorage.removeItem("access-token");
			this.$router.push("/");
		}
	}
}

</script>

