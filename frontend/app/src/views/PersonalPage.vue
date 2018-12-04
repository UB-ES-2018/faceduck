<template>
  <div id="PersonalPage">
    <NavBar/>
    <div class="containerPhoto" align="center">
      <img class="photo" v-if="hasImage" v-bind:src="post['image-url']" />
      <ImageUploader v-if="!hasImage" uploader-id="personal-image-uploader" />
      <div class="username" v-bind:userName="user.username">
        {{ user.username }}
      </div>
    </div>
    <div class="container" align="center">
      <PostForm/>
      <PostList v-bind:authorId="user.id" />
    </div>
  </div>
</template>

<script>
  import NavBar from "../components/NavBar.vue";
  import PostForm from "../components/PostForm.vue";
  import PostList from "../components/PostList.vue";
  import ImageUploader from "../components/ImageUploader";
  var host = window.location.hostname
  var apiPutImageUrl = 'http://' + host + ':5000/user'; //Backend ip
  export default {
    name: 'PersonalPage',
    components: {
      NavBar,
      PostForm,
      PostList,
      ImageUploader
    },
    data() {
      return {
        user: JSON.parse(localStorage.getItem("user")),
        post: {
          "image-url": '',
        },
        hasImage: false,
      }
    },
    created() {
      var user = JSON.parse(localStorage.getItem("user"));
      if (this.$route.path === '/profile') {
        if (user["image-url"] != '') {
          this.post["image-url"] = user["image-url"]
          this.hasImage = true
        }
      } else {
        if (user.username == this.$route.username) {
          if (user.getItem("image-url") != '') {
            this.post["image-url"] = user["image-url"]
            this.hasImage = true
          }
        } else {
          this.getUser()
        }
      }
  
    },
    updated() {},
    methods: {
      putImage() {
        var post = this.post;
        fetch(apiPutImageUrl, {
            method: "PUT",
            headers: {
              "Authorization": "Bearer " + localStorage.getItem("access-token"),
              "Content-Type": "application/json",
            },
            body: JSON.stringify(post)
          })
          .then((response) => {
            if (response.ok) {
              localStorage.removeItem("user");
              localStorage.setItem("user",
                JSON.stringify(response["user"]));
              console.log(localStorage.getItem("user"))
              this.hasImage = true
            }
          }).catch(() => {});
      },
      getUser() {
        return true;
      }
    },
    mounted() {
      this.$root.$on("imageUpload", (event) => {
        if (event.emitter === "personal-image-uploader") {
          this.post["image-url"] = event.url;
          this.putImage()
        }
      });
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