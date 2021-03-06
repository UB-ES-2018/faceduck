<template>
    <div id="user-page">
        <NavBar class="navbar" />
    
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
            <FriendList class="friend-list" v-bind:userId="this.userid" />
            <GroupList class="group-list" v-bind:userId="this.userid" />
            <button class="group-button" v-if="isUser" v-on:click="createGroup"> Create Group </button>
            <div class="post-wall">
                <PostForm class="post-form" />
                <PostList class="post-list" v-bind:authorId="this.user.id" />
            </div>
        </main>
    </div>
</template>

<script>
    import FriendList from "../components/FriendList.vue";
    import GroupList from "../components/GroupList.vue";
    import NavBar from "../components/NavBar.vue";
    import PostForm from "../components/PostForm.vue";
    import PostList from "../components/PostList.vue";
    import ImageUploader from "../components/ImageUploader";
    
    var host = window.location.hostname
    var apiPutImageUrl = 'http://' + host + ':5000/user'; //Backend ip
    export default {
        name: 'PersonalPage',
        components: {
            FriendList,
            GroupList,
            NavBar,
            PostForm,
            PostList,
            ImageUploader
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
            /* istanbul ignore next */
            this.$router.push(0)
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
                                localStorage.setItem("user",
                                    JSON.stringify(res))
                                this.hasImage = true
                            })
                        }
                    }).catch(() => {});
    
            },
            getUser() {
                this.userid = this.$route.params.userid
                this.isUser = false
                fetch(apiPutImageUrl + '/' + this.userid, {
                    method: "GET",
                    headers: {
                        "Authorization": "Bearer " + localStorage.getItem("access-token"),
                        "Content-Type": "application/json",
                    }
                }).then((response) => {
                    if (response.ok) {
                        response.json().then(res => {
                            this.user = res
                            this.userid = res.id
                            if (res.hasOwnProperty("image-url")) {
                                this.hasImage = true
                                this.post["image-url"] = res["image-url"]
                            } else {
                                this.hasImage = false
                            }
                        })
                    }
                });
            },
            refreshUser() {
                this.user = JSON.parse(localStorage.getItem("user"))
            },
    
            userHasImage() {
                var user = JSON.parse(localStorage.getItem("user"));
    
                if (this.$route.path === '/profile') {
                    this.user = user;
                    this.userid = user.id
                    if (user.hasOwnProperty("image-url")) {
                        this.post["image-url"] = user["image-url"]
                        this.hasImage = true
                    }
                } else {
                    this.userid = this.$route.params.userid
                    if (user.id === this.$route.params.userid) {
                        this.user = user
                        if (user.hasOwnProperty("image-url")) {
                            this.post["image-url"] = user["image-url"]
                            this.hasImage = true
                        }
                    } else {
                        this.getUser()
                    }
                }
            },
            createGroup() {
                /* istanbul ignore next */
                this.$router.push('/group');
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
  background: $lightestprimary
  border-bottom: 5px solid $primary

.containerPhoto > .personal-photo
  position: relative
  border-radius: 100%
  background-color: $darkgray
  width: 100px
  height: 100px
  overflow: hidden
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
  
.personal-photo > .photo
  position: relative
  height: inherit
  z-index: 1
  
.personal-photo:hover > .photo
  opacity: 0.2;

.personal-photo > .image-uploader
  position: absolute
  right: calc(50% - 21px)
  top: calc(50% - 19px)
  z-index: 0
  
.personal-photo:hover > .image-uploader
  z-index: 1
  
.containerPhoto > .username
  color: $darkestgray
  font-size: 24px
  margin-top: .8rem
  margin-bottom: .8rem
  width: auto

#user-page > main
  display: grid
  margin-top: 1.8rem
  grid-gap: 15px
  grid-template-columns: 2fr minmax(305px, 700px) minmax(180px, 300px) 1fr;
  grid-template-rows: auto auto auto auto;
  @media screen and (max-width: $break-small)
    display: flex
    flex-direction: column
    & > *
      margin-bottom: 15px
    & > *:last-child
      margin-bottom: 0

#user-page > main > *
  @media screen and (max-width: $break-small)
    margin-right: 15px
    margin-left: 15px

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
  grid-row: 1 / 5
  width: auto

#user-page > main > .group-button
  grid-column: 3 / 4
  grid-row: 3 / 4
  height: 15%

button
  background-color: #ffb511
  border: none
  color: white
  font-size: 12px
  font-weight: bold
  box-sizing: content-box
  padding: 10px
  border-radius: 10px
  width: auto
  float: right
  cursor: pointer

</style>
