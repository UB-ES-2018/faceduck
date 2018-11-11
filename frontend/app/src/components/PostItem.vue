<template>
    <div class="row justify-content-center">
        <div class="post-item col-xl-7 col-lg-8 col-md-10 col-sm-12">
            <div class="post-username">
                <a v-bind:href="'/profile/' + post.author.username" v-if="!post.special">
                    {{post.author.username}}
                </a>
                <span v-else>{{post.author.username}}</span>
            </div>
            <div class="post-text" v-html="richText"></div>
            <div class="post-image" v-if="post['image-url']">
                <img v-bind:src="post['image-url']"/>
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
    computed: {
        richText() {
            var text = this.post.text;
            text = text.replace(/<.*script/, "&lt;script");
            var tags = text.match(/#[^\s]+/g);

            if (!tags) return text;

            for (var i = 0; i < tags.length; i++) {
                var tokens = text.split(tags[i]);
                for (var j = 0; j < tokens.length - 1; j++) {
                    tokens[j] += '<a href="/search?query=';
                    tokens[j] += encodeURIComponent(tags[i]);
                    tokens[j] += '">';
                    tokens[j+1] = '</a>' + tokens[1];
                    text = tokens.join(tags[i]);
                }
            }
            return text;
        }
    },
    mounted() {
        this.special();
    },
    updated() {
        this.special();
    },
    methods: {
        special() {
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
    border-radius: 8px
    webkit-border-radius: 8px
    border: 1px #666 solid
    padding: 10px 20px
    
    background-color: #eee
    color: #333
    text-align: left
    max-height: 30rem
    
    overflow-y: scroll
    overflow-wrap: break-word;

.post-username
    font-weight: bold

.post-text
    text-align: left

.post-image
    margin: 10px 0
    text-align: center

img
    max-width: 100%
    border: 1px #aaa solid
    padding: 4px
    border-radius: 3px
    
</style>