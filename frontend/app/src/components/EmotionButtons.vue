<template>
	<div>
        <ul class="icons" v-on:mouseover="isVisible = true;" v-on:mouseout="isVisible = false;">
            <li><i class="fa fa-thumbs-up"></i><span> Like </span></li>
            <ul class="emotions" id="emotions" v-show="isVisible"><!--&lt;EmotionButtons/&gt;-->
                <li v-bind:data-selected="selected == 'like'"><img 
                    src="/emotions/like.png" 
                    class="react" 
                    v-on:click="addReaction('like')"></li>
                <li v-bind:data-selected="selected == 'love'"><img 
                    src="/emotions/love.png" 
                    class="react" 
                    v-on:click="addReaction('love')"></li>
                <li v-bind:data-selected="selected == 'laughing face'"><img 
                    src="/emotions/laughing_face.png" 
                    class="react" 
                    v-on:click="addReaction('laughing face')"></li>
                <li v-bind:data-selected="selected == 'angry face'"><img 
                    src="/emotions/angry_face.png" 
                    class="react" 
                    v-on:click="addReaction('angry face')"></li>
                <li v-bind:data-selected="selected == 'sad crying face'"><img 
                    src="/emotions/sad_crying_face.png" 
                    class="react" 
                    v-on:click="addReaction('sad crying face')"></li>
            </ul>
        </ul>
	</div>
</template>

<script>

var host = window.location.hostname;
var user_id = 
    (JSON.parse(localStorage.getItem("user")) || {id: -1}).id;

export default {
	name: "EmotionButtons",
	props: ["post"],
	data() {
		return {
            isVisible: false,
            selected: "",
        }
    },
    created() {
        this.mapSelected(this.post);
        console.log(this.selected)
    },
    methods: {
        addReaction(reaction) {
            var apiAddReactionUrl = "//" + host + ":5000/post/";
            apiAddReactionUrl += this.post.id + "/reactions";

            fetch(apiAddReactionUrl, {
                method: "POST",
                headers: {
                    "Authorization": "Bearer " + localStorage.getItem("access-token"),
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({"reaction" : reaction})
            })
            .then((response) => {
                /* istanbul ignore next */
                if (response.ok) {
                    response.json().then((post) => {
                        this.mapSelected(post);
                        this.$root.$emit("showReaction", {
                            post: post
                        });
                    })
                }
            });
        },
        mapSelected(post) {
            if (post["user-reaction"] == undefined)
                this.selected = "";
            else {
                this.selected = "";
                post["user-reaction"].some((r) => {
                    if (r["user-id"] == user_id) {
                        this.selected = r["reaction"];
                        return true;
                    }
                });
            }
        }
    },
}
</script>

<style lang="sass" scoped>

.emotions
  position: absolute
  background-color: #fff
  border: 1px solid #9b9797
  left: 0%
  border-radius: 100px
  width: auto
  padding-left: 0
  overflow: hidden
  
.emotions li
  padding: 8px
  margin: 0 auto
  cursor: pointer
  
.emotions li[data-selected] 
  background-color: #4B0082
  
.react
  width: 25px
  height: 25px
  transition: all .2s ease-in-out
  
.react:hover
  transform: scale(1.7)
  
.icons
  height: 26px
  padding: 0px 0
  
.icons > li
  padding: 10px
  padding-top: 5px
  text-align: left
  cursor: pointer
  
ul li
  list-style-type: none
  float: left

.fa
  //width: 100px
  //height: 100px
  //color: #ffb511

</style>
