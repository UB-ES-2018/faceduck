<template>
    <div class="emotions" id="emotions" v-show="isVisible"><!--&lt;EmotionButtons/&gt;-->
        <img src="http://www.northamericangoldwings.com/community/forums/uploads/reactions/facebook-love-png-44003.png" class="react">  {{like}}
        <img src="http://www.freeiconspng.com/uploads/facebook-live-love-png-1.png" class="react" v-on:click="addReaction('love')">  {{love}}
        <img src="http://clipart.info/images/ccovers/1499793248facebook-haha.png" class="react" v-on:click="addReaction('laughing face')">  {{laughing}}
        <img src="https://cdn4.iconfinder.com/data/icons/reaction/32/angry-512.png" class="react" v-on:click="addReaction('angry face')">  {{angry}}
        <img src="http://clipart.info/images/ccovers/1499793247facebook-sad-emoji-like-png.png" class="react" v-on:click="addReaction('sad crying face')">  {{sad}}
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
        }
    },
    /**
    created() {
        if (this.query)
            this._query = this.query.trim();

        this.$root.$on("showReaction", (event) => {
            if (event && event.post)
                // unshift: push to position 0
                this.list.unshift(event.post);
                
        });
    }
    */
}
</script>

<style lang="sass" scoped>

.emotions
    height: 40px

.react
    width: 25px
    height: 25px
    

</style>