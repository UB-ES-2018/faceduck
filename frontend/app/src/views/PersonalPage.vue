<template>
  <div id="PersonalPage" >
    <nav class="navbar navbar-dark bg-dark">
        <h1 class="title">Faceduck</h1>
        <fieldset class="actions">
            <button class="button" v-on:click='logOutButton'> Log Out </button>
        </fieldset>
    </nav>
    <div class="container" align="center">
        <div class="photo"></div>
        <div class="username">Patata</div>
    </div>
    <div align="center">
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
  font-size: 150%

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

.container
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
    font-size: 5vh

</style>

<script>
import PostForm from "../components/PostForm.vue";
import PostView from "../components/PostView.vue";

export default {
  name: 'PersonalPage',
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
		logout () {
			localStorage.removeItem("access-token");
			this.$router.push("/");
		}
	}
}

</script>