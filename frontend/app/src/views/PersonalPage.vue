<template>

<div id="user-page" >
  <NavBar class="navbar"/>
  
  <div class="containerPhoto">
    <div class="personal-photo">
      <img name="photo" class="photo" v-show="hasImage" v-bind:src="post['image-url']" />
      <ImageUploader class="image-uploader" v-if="isUser" uploader-id="personal-image-uploader" />
    </div>
    <div class="username" v-bind:userName="user.username">
      {{ user.username }}
    </div>
  </div>
  
  <main>
    <FriendList class="friend-list" v-bind:userId="this.userid"/>
    <GroupList class="group-list" v-bind:userId="this.userid"/>
    
    <div class="post-wall">
      <PostForm class="post-form"/>
      <PostList class="post-list" v-bind:authorId="this.user.id"/>
    </div>
  </main>
</div>

</template>

<script>
import NavBar from "../components/NavBar.vue";
import PostForm from "../components/PostForm.vue";
import PostList from "../components/PostList.vue";
import ImageUploader from "../components/ImageUploader";
import FriendList from "../components/FriendList.vue";
import GroupList from "../components/GroupList.vue";

var host = window.location.hostname
var apiPutImageUrl = 'http://' + host + ':5000/user'; //Backend ip
export default {
    name: 'PersonalPage',
    components: {
        NavBar,
        PostForm,
        PostList,
        ImageUploader,
        FriendList,
        GroupList
    },
    data() {
        return {
            user: {},
            post: {
                "image-url": '',
            },
            hasImage: false,
            userid: '',
            isUser: true,
        }
    },
    created() {
        this.userHasImage()
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
                        response.json().then(res => {
                            console.log(res)
                            localStorage.setItem("user",
                                                 JSON.stringify(res))
                            this.hasImage = true           
                        })
                    }
                }).catch(() => {});
            
        },
        getUser() {
            this.userid=this.$route.params.userid
            this.isUser = false
            fetch(apiPutImageUrl+'/'+this.userid,{
                method: "GET",
                headers:{
                     "Authorization": "Bearer " + localStorage.getItem("access-token"),
                    "Content-Type": "application/json",
                }
            }).then((response)=>{
                if(response.ok){
                    response.json().then(res=>{
                        this.user = res
                        if(res.hasOwnProperty("image-url")){
                            this.hasImage = true
                            this.post["image-url"] = res["image-url"]
                        }else{
                            this.hasImage = false
                        }
                    })
                }
            });
        },
        refreshUser(){
            this.user = JSON.parse(localStorage.getItem("user"))
        },
        
        userHasImage() {
            var user = JSON.parse(localStorage.getItem("user"));
            
            console.log(user)
            if (this.$route.path === '/profile') {
                this.user = user;
                this.userid=this.user.id
                if (user.hasOwnProperty("image-url")) {
                    this.post["image-url"] = user["image-url"]
                    this.hasImage = true
                }
                console.log(this.hasImage)
            } else {
                this.userid=this.$route.params.userid
                if (user.id == this.$route.params.userid) {
                    if (user.hasOwnProperty("image-url")) {
                        this.post["image-url"] = user["image-url"]
                        this.hasImage = true
                    }
                } else {
                    this.getUser()
                }
                console.log(this.hasImage)
            }
        }
    },
    mounted() {
        this.$root.$on("imageUpload", (event) => {
            if (event.emitter === "personal-image-uploader") {
                this.post["image-url"] = event.url;
                this.hasImage = true
                this.putImage()
                
            }
        });
    }
}

</script>

<style lang="sass" scoped>
@import '../assets/global.sass';

#user-page
  min-width: 320px
  width: 100vw
  
.containerPhoto
  display: flex
  flex-direction: column
  align-items: center
  padding-top: 2.2rem
  min-width: 100%
  //background: #ffb511
  background:  #FFDC3333 
  //box-shadow: inset 0 -80px 80px -80px black, inset 0 80px 80px -80px black
  border-bottom: 5px solid $accent3
  //background-image: url(../assets/h2.jpg)
  //background-position: center;
  //background-repeat: no-repeat;
  //background-size: cover;

.containerPhoto > .personal-photo
  position: relative
  border-radius: 100%
  background-color: gray
  width: 100px
  height: 100px
  overflow: hidden
  
.personal-photo > .photo
  height: inherit
  width: inherit

.personal-photo:hover > .photo
  display: none

.personal-photo > .image-uploader
  position: absolute
  right: calc(50% - 21px)
  top: calc(50% - 19px)
  display: none
  
.personal-photo:hover > .image-uploader
  display: block
  
.containerPhoto > .username
  color: black
  font-size: 24px
  margin-top: .8rem
  margin-bottom: .8rem
  width: auto

#user-page > main
  display: grid
  margin-top: 1.8rem
  grid-gap: 15px
  grid-template-columns: 2fr minmax(305px, 700px) minmax(180px, 300px) 1fr;
  grid-template-rows: auto auto auto;
  @media screen and (max-width: $break-small)
    display: flex
    flex-direction: column

#user-page > main > *
  @media screen and (max-width: $break-small)
    margin-right: 15px
    margin-left: 15px
    //margin-bottom: 15px

#user-page > main > .friend-list
  grid-column: 3 / 4
  grid-row: 1 / 2
  height: auto

#user-page > main > .group-list
  grid-column: 3 / 4
  grid-row: 2 / 3
  height: auto

#user-page > main > .post-wall
  grid-column: 2 / 3
  grid-row: 1 / 4
  width: auto;

</style>
