<template>
    <div class="row justify-content-md-center">
        <div class="post-item col-sm-6">
            <div class="post-username">
                <a v-bind:href="'/profile/' + post.author.username" v-if="!post.special">
                    {{post.author.username}}
                </a>
                <span v-else>{{post.author.username}}</span>
            </div>
            <div class="post-text">{{post.text}}</div>
            <div class="post-image" v-if="post['image-url']">
                <img v-bind:src="post['image-url']" width="100%" />
            </div>
            <!-- FUTURE: reaction counts -->
            <EmotionButtons v-bind:post="post" v-if="!post.special"/>
            <!-- FUTURE: comments -->
        </div>
    </div>
</template>

<script>
import EmotionButtons from "./EmotionButtons.vue";

export default {
    name: "PostItem",
    props: ["post"],
    data() {
        return { interval: false }
    },
    created() {
        this.check();
    },
    updated() {
        this.check();
    },
    methods: {
        check() {
            if (this.post["image-url"]) {
                fetch(this.post["image-url"])
                .then(response => {
                    if (!response.ok) 
                        this.post["image-url"] = "";
                })
                .catch(err => {});
            }

            clearInterval(this.interval);
            if (this.post.special == "duckload") {
                this.interval = setInterval(() => {
                    if (this.post.text.length < 48) 
                        this.post.text += "🐤";
                    else this.post.text = "🐤";
                }, 80);
            }
        }
    },
    beforeDestroy() {
        clearInterval(this.interval);
    },
    components: {
        EmotionButtons
    }
}
</script>

<style lang="sass" scoped>
.post-item
    border-radius: 3px
    webkit-border-radius: 2px
    border: 1px #666 solid
    padding: 10px
    
    background-color: #eee
    color: #333
    text-align: left
    max-height: 50rem
    
    overflow-y: scroll
    overflow-wrap: break-word;

.post-username
    font-weight: bold

.post-text
    text-align: left

.post-image
    margin: 10px 0
</style>