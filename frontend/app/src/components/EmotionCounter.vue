<template>
<div class="emotions" id="emotions" v-show="isVisible">
  <ul>
    <li v-if="like > 0"><img src="/emotions/like.png" class="react"> {{like}} </li>
    <li v-if="love > 0"><img src="/emotions/love.png" class="react"> {{love}} </li>
    <li v-if="laughing > 0"><img src="/emotions/laughing_face.png" class="react"> {{laughing}} </li>
    <li v-if="angry > 0"><img src="/emotions/angry_face.png" class="react"> {{angry}} </li>
    <li v-if="sad > 0"><img src="/emotions/sad_crying_face.png" class="react"> {{sad}} </li>
  </ul>
</div>
</template>

<script>
export default {
	name: "EmotionButtons",
    props: ["post"],
	data() {
		return {
            isVisible: true,
            like: 0,
            love: 0,
            laughing: 0,
            angry: 0,
            sad: 0,
            post_: {}
        }
    },

    created() {
        this.post_ = this.post;
        this.updateVisibleReactions();

        /* istanbul ignore next */
        this.$root.$on("showReaction", (event) => {
            if (event.post.id == this.post.id) {
                this.post_ = event.post;
                this.updateVisibleReactions();
            }
        });
    },

    methods: {
        resetCounts() {
            this.like = 0;
            this.love = 0;
            this.laughing = 0;
            this.angry = 0;
            this.sad = 0;
        },
        updateVisibleReactions() {
            //var reactions = JSON.stringify(this.post["reactions-count"]);
            
            this.resetCounts();
            if (this.post_["reactions-count"] == undefined) return;

            this.post_["reactions-count"].forEach((reaction) => {
                var reaction_name = reaction["reaction"];

                switch (reaction_name) {
                    default:
                    break;
                    case "like":
                        this.like = reaction["count"];
                        break;
                    case "love":
                        this.love = reaction["count"];
                        break;
                    case "laughing face":
                        this.laughing = reaction["count"];
                        break;
                    case "angry face":
                        this.angry = reaction["count"];
                        break;
                    case "sad crying face":
                        this.sad = reaction["count"];
                        break;
                }
            });
        }
    }
        
    
}
</script>

<style lang="sass" scoped>

.emotions
  padding: 0
  padding-top: 10px
  padding-bottom: 18px

.emotions > ul
  padding: 0
  
.react
  width: 25px
  height: 25px
  
div li
  list-style-type: none
  float: left
  padding: 0px 3px
  
</style>
