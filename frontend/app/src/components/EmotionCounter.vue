<template>
    <div class="emotions" id="emotions" v-show="isVisible"><!--&lt;EmotionButtons/&gt;-->
        <div v-if="post['reactions-count'][0]['reaction'] === 'like'"><img src="http://www.northamericangoldwings.com/community/forums/uploads/reactions/facebook-love-png-44003.png" class="react">  {{post['reactions-count'][0]['count']}}</div>
        <div v-if="post['reactions-count'][0]['reaction'] === 'love'"><img src="http://www.freeiconspng.com/uploads/facebook-live-love-png-1.png" class="react">  {{post['reactions-count'][0]['count']}}</div>
        <div v-if="post['reactions-count'][0]['reaction'] === 'laughing face'"><img src="http://clipart.info/images/ccovers/1499793248facebook-haha.png" class="react">  {{post['reactions-count'][0]['count']}}</div>
        <div v-if="post['reactions-count'][0]['reaction'] === 'angry face'"><img src="https://cdn4.iconfinder.com/data/icons/reaction/32/angry-512.png" class="react">  {{post['reactions-count'][0]['count']}}</div>
        <div v-if="post['reactions-count'][0]['reaction'] === 'sad crying face'"><img src="http://clipart.info/images/ccovers/1499793247facebook-sad-emoji-like-png.png" class="react">  {{post['reactions-count'][0]['count']}}</div>
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
    methods: {
        update() {
            
            this.like = post["reactions-count"][0]["reaction"]
            alert(this.like)
            for (i in post["reactions-count"]){
                alert(i["reaction"])
                if (i["reaction"].equals("like")){
                    this.data.like = i["count"]
                } else if (i["reaction"].equals("love")) {
                    this.love = i["count"]
                } else if (i["reaction"].equals("laughing")) {
                    this.laughing = i["count"]
                } else if (i["reaction"].equals("angry")) {
                    this.angry = i["count"]
                } else if (i["reaction"].equals("sad")) {
                    this.sad = i["count"]
                } 
            }
        },
    },
}
</script>

<style lang="sass" scoped>

.emotions
    height: 40px

.react
    width: 25px
    height: 25px
    

</style>