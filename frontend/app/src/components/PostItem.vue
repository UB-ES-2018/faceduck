<template>
    <div class="row justify-content-center">
        <div class="post-item">
            <div class="post-username" v-if="post.author && post.author.username">
                <a v-bind:href="'/profile/' + post.author.id" v-if="!post.special">
                    {{post.author.username}}
                </a>
                <span v-else>{{post.author.username}}</span>
            </div>
            <div class="post-text" v-if="post.text" v-html="richText"></div>
            <div class="post-image" v-if="post['image-url']">
                <img v-bind:src="post['image-url']"/>
            </div>
            <div class="reaction" v-if="!post.special">
                <EmotionCounter v-bind:post="post"/>
            </div>
            <div class="emotionsButton" v-if="!post.special && user">
                <EmotionButtons v-bind:post="post"/>
            </div>
            <CommentsView 
              v-bind:count="post['comments-count']"
              v-bind:post_id="post['id']"
              v-if="!post.special"/>
        </div>
    </div>
</template>

<script>
import EmotionButtons from "./EmotionButtons.vue";
import EmotionCounter from "./EmotionCounter.vue";
import CommentsView from "./CommentsView.vue";

export default {
    name: "PostItem",
    props: ["post"],
    data() {
        return { 
            interval: false,
            user: JSON.parse(localStorage.getItem("user"))
        }
    },
    computed: {
        richText() {
            var text = this.post.text;
            text = text.replace(/<.*script/, "&lt;script");
            var tags = text.match(/#[^\s]+/g);
            //console.log(this.post)
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
        /* istanbul ignore next */
        this.special();
    },
    methods: {
        special() {
            clearInterval(this.interval);
            /* istanbul ignore next */
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
        /* istanbul ignore next */
        clearInterval(this.interval);
    },
    components: {
        CommentsView,
        EmotionButtons,
        EmotionCounter,
    }
}
</script>

<style lang="sass" scoped>
@import '../assets/global.sass';

.post-item
  width: 100%
  border-radius: 8px
  webkit-border-radius: 8px
  border: 1px #666 solid
  padding: 10px 20px
  background-color: $lightgray
  color: $darkestgray
  text-align: left
  max-height: 30rem
  overflow-y: scroll
  overflow-wrap: break-word

.row
  margin-right: 0;
  margin-left: 0;

.post-username
  font-weight: bold

.post-text
  text-align: left
  white-space: pre-wrap;

.post-image
    margin: 10px 0
    text-align: center

img
    max-width: 100%
    border: 1px $darkgray solid
    padding: 4px
    border-radius: 3px

.reaction
    border-top: 1px solid $gray
    align: "right"

.emotionsButton
  border-top: 1px solid $gray
  position: relative
    
</style>
