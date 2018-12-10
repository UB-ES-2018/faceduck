<template>
<form class="inputbox container3 post-form" v-on:submit="submitPost">
  <!--<div class="inline-input">-->

    <div class="post-options">
      <ImageUploader uploader-id="post-image-uploader" />
      <VisibilityField v-model='this.post.visibility' />
    </div>
    
   <textarea class="post-text inputs"
                cols="5"
                rows="5"
                type="text"
                name="post"
                id="text-box"
                v-model="post.text"
                placeholder="Say Something..."></textarea>
    <div class="post-image" v-if="post['image-url']">
      <img v-bind:src="post['image-url']"/>
    </div>
  
  <button class="post-submit actions" type="submit"> Post </button>
</form>
</template>

<script>
import ImageUploader from "./ImageUploader.vue";
import VisibilityField from "./VisibilityField.vue";
    
    var host = window.location.hostname;
    var apiPostFormUrl = '//' + host + ':5000/post';
    
    export default {
        name: 'PostForm',
        data() {
            return {
                post: {
                    "author-id": JSON.parse(localStorage.getItem("user"))["id"],
                    text: '',
                    "image-url": '',
                    visibility:'friends',
                }
            }
        },
        beforeCreate() {
            this.$root.$on("imageUpload", (event) => {
                if (event.emitter === "post-image-uploader") {
                    this.post["image-url"] = event.url;
                }
            });
            this.$root.$on("visibilityChange", (event) => {
                this.post.visibility = event.visibility;
            });
        },
        methods: {
            submitPost(e) {
                e.preventDefault();
                var post = this.post;
                fetch(apiPostFormUrl, {
                        method: "POST",
                        headers: {
                            "Authorization": "Bearer " + localStorage.getItem("access-token"),
                            "Content-Type": "application/json",
                        },
                        body: JSON.stringify(post)
                    })
                    .then((response) => {
                        if (response.ok) {
                            this.post["text"] = "";
                            this.post["image-url"] = "";
                            this.$root.$emit("clearImageUpload");
    
                            response.json().then((post) => {
                                this.$root.$emit("addPost", {
                                    post: post
                                });
                            })
                        }
                    }).catch(() => {});
            },
        },
        components: {
            ImageUploader,
            VisibilityField,
        }
    };
</script>

<style lang="sass" scoped>

.post-form
  display: grid
  grid-gap: 15px
  grid-template-columns: auto auto auto;
  grid-template-rows: auto auto auto auto;
  
.post-options
  display: flex
  flex-direction: row
  grid-column: 1 / 4
  grid-row: 1 / 1
  justify-self: end

.post-options > *
  margin-right: 10px
  &:last-child
    margin-right: 0
  
.post-text
  grid-column: 1 / 4
  grid-row: 2 / 2
  resize: none;
  overflow: auto;
  padding: 7px

.post-image
  grid-column: 1 / 4
  grid-row: 3 / 3

.post-image > img
  max-height: 300px
  border: 1px #aaa solid
  padding: 4px
  border-radius: 3px

.post-submit
  grid-column: 3 / 4
  grid-row: 4 / 4
  justify-self: end
  border: 0

.container3
  margin-left: auto
  margin-right: auto
  width: 100%
  height: auto
  //max-height: 30rem
  background-color: #ddd
  //background:rgb(241, 241, 241)
  color: black !important
  color: #333 !important
  font-family: 'Verdana'
  font-size: 18px
  padding-top: 20px
  padding-bottom: 25px
  padding: 20px
  //box-shadow: 0px 5px 10px 0px #333, 0px -3px 10px 0px #333
  //border-radius: .5em
  border-radius: 8px
  border: 1px #666 solid
  
.container > VisibilityField
  height: 100px

#text-box 
  background: #f2f2f2
  height: 1.5%
  height: 150px
  font-family: 'Merriweather Sans', sans-serif
  font-size: 14px
  border: 1px solid #82aee8
  border-radius: 5px
  box-shadow: 0 1px 1px #82aee8 inset
  width: 100%
  
#text-box:focus
  background-color: #fff
  border-color: #82aee8
  outline: none
  box-shadow: 0 0 0 1px #82aee8 inset
  box-sizing: border-box
  
.inputbox input
  display: flex
  width: 100%
  height: 40px
  background-color: #f2f2f2
  border: none
  margin-bottom: 20px
  font-size: 12px
  
.inputbox button[type="submit"]
  background-color: #ffb511
  border: none
  color: white
  font-size: 12px
  font-weight: bold
  box-sizing: content-box
  padding: 10px
  border-radius: 10px
  width: 60px
  float: right
  cursor: pointer
  
</style>
