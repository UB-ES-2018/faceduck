<template>
    <div class="emotions" id="emotions" v-show="isVisible"><!--&lt;EmotionButtons/&gt;-->
        <li v-if="like > 0"><img src="http://www.northamericangoldwings.com/community/forums/uploads/reactions/facebook-love-png-44003.png" class="react"> {{like}} </li>
        <li v-if="love > 0"><img src="http://www.freeiconspng.com/uploads/facebook-live-love-png-1.png" class="react"> {{love}} </li>
        <li v-if="laughing > 0"><img src="http://clipart.info/images/ccovers/1499793248facebook-haha.png" class="react"> {{laughing}} </li>
        <li v-if="angry > 0"><img src="https://cdn4.iconfinder.com/data/icons/reaction/32/angry-512.png" class="react"> {{angry}} </li>
        <li v-if="sad > 0"><img src="http://clipart.info/images/ccovers/1499793247facebook-sad-emoji-like-png.png" class="react"> {{sad}} </li>
        <!--
            v-if="post['reactions-count'][0]['reaction'] === 'love'"
            v-if="post['reactions-count'][0]['reaction'] === 'laughing face'"
            v-if="post['reactions-count'][0]['reaction'] === 'angry face'"
            v-if="post['reactions-count'][0]['reaction'] === 'sad crying face'"
        -->
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
            _post: {}
        }
    },

    created() {
        this._post = this.post;
        this.updateVisibleReactions();

        this.$root.$on("showReaction", (event) => {
            if (event.post.id == this.post.id) {
                this._post = event.post;
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
            if (this._post["reactions-count"] == undefined) return;

            this._post["reactions-count"].forEach((reaction) => {
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
    height: 40px
    padding: 4px 30px

.react
    width: 25px
    height: 25px
    
div li
    list-style-type: none
    float: left
    padding: 0px 3px

</style>