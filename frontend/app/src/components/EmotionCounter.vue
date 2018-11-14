<template>
    <div class="emotions" id="emotions" v-show="isVisible"><!--&lt;EmotionButtons/&gt;-->
        <li v-if="visible.like"><img src="http://www.northamericangoldwings.com/community/forums/uploads/reactions/facebook-love-png-44003.png" class="react"> {{like}} </li>
        <li v-if="visible.love"><img src="http://www.freeiconspng.com/uploads/facebook-live-love-png-1.png" class="react"> {{love}} </li>
        <li v-if="visible.laughing"><img src="http://clipart.info/images/ccovers/1499793248facebook-haha.png" class="react"> {{laughing}} </li>
        <li v-if="visible.angry"><img src="https://cdn4.iconfinder.com/data/icons/reaction/32/angry-512.png" class="react"> {{angry}} </li>
        <li v-if="visible.sad"><img src="http://clipart.info/images/ccovers/1499793247facebook-sad-emoji-like-png.png" class="react"> {{sad}} </li>
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
            visible: {
                like: false,
                love: false,
                laugh: false,
                angry: false,
                sad: false
            }
        }
    },

    created() {
        this.updateVisibleReactions();

        this.$root.$on("showReaction", (event) => {
            if (JSON.stringify(event.post.id).localeCompare(JSON.stringify(this.post.id)) == 0) {
                this.post = event.post;
                this.updateVisibleReactions();
            }
        });
    },

    methods: {
        updateVisibleReactions() {
            //var reactions = JSON.stringify(this.post["reactions-count"]);
            var i;
            var reaction;
            for (i in JSON.stringify(this.post["reactions-count"])) {
                reaction = JSON.stringify(this.post["reactions-count"][i]["reaction"]);
                
                if (reaction.localeCompare('"like"') == 0) {
                    this.visible.like = true;
                    this.like = JSON.stringify(this.post["reactions-count"][i]["count"]);

                } else if (reaction.localeCompare('"love"') == 0) {
                    this.visible.love = true;
                    this.love = JSON.stringify(this.post["reactions-count"][i]["count"]);
                    
                } else if (reaction.localeCompare('"laughing face"') == 0) {
                    this.visible.laughing = true;
                    this.laughing = JSON.stringify(this.post["reactions-count"][i]["count"]);

                } else if (reaction.localeCompare('"angry face"') == 0) {
                    this.visible.angry = true;
                    this.angry = JSON.stringify(this.post["reactions-count"][i]["count"]);

                } else if (reaction.localeCompare('"sad crying face"') == 0) {
                    this.visible.sad = true;
                    this.sad = JSON.stringify(this.post["reactions-count"][i]["count"]);
                } 
            }
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