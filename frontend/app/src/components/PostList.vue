<template>
    <div class="post-list container5">
        <PostItem 
            v-for="post in list" 
            v-bind:post="post"
            v-bind:key="post.id"/>
    </div>
</template>

<script>
import PostItem from "./PostItem.vue";

var ducklist = [{
    "author": {
        "username": "Retrieving lastest posts…"
    },
    "text": "",
    "special": "duckload"
}];

var noposts = [{
    "author": {
        "username": "No posts found"
    },
    "text": "",
    "special": "no-posts"
}];

var host = window.location.hostname;
var api = '//' + host + ':5000/post/search';

export default {
    name: "PostList",
    props: {
        "authorId": String,
        "query": String,
        "newsfeed": Boolean
    },
    data() {
        return {
            list: [],
            timeout: false,
            query_: "",
            fetch_options: ""
        };
    },
    created() {
        if (this.query)
            this.query_ = this.query.trim();
        else
            this.query_ = "";

        this.fetchPosts();
        /* istanbul ignore next */
        this.$root.$on("postEvent", (event) => {
            if (event && event.query) this.query_ = event.query.trim();
            this.fetchPosts();
        });
        /* istanbul ignore next */
        this.$root.$on("addPost", (event) => {
            if (event && event.post)
                // unshift: push to position 0
                this.list.unshift(event.post);
        });
    },
    methods: {
        configure() {
            var body = {};
            var fetch_options = {
                headers: {}
            };

            if (this.newsfeed) {
                fetch_options["method"] = "GET";
                api = '//' + host + ':5000/post/newsfeed';
            } else {
                api = '//' + host + ':5000/post/search';
                
                if (this.authorId)
                    body["author-id"] = this.authorId;

                else /*if (this.query_)*/ {
                    if (this.query_.indexOf(" ") == -1 
                        && this.query_.lastIndexOf("#") == 0)
                        body["tag"] = this.query_.slice(1);
                    else
                        body["query"] = this.query_;
                }

                fetch_options.headers["Content-Type"] = "application/json";
                fetch_options["body"] = JSON.stringify(body);
                fetch_options["method"] = "POST";
            }

            fetch_options.headers["Authorization"] = "Bearer " + localStorage.getItem("access-token");

            this.fetch_options = fetch_options;
        },
        fetchPosts() {
            this.configure();

            if (this.list.length === 0
                || this.list[0].special == "no-posts")
                this.list = ducklist;

            /* istanbul ignore next */
            fetch(api, this.fetch_options)
            .catch(() => {
                this.list = noposts;
            })
            .then(res => {
                if (!res.ok) this.list = noposts;
                return res;
            })
            .then(res => res.json())
            .then(res => {
                if (res.length > 0)
                    this.list = res;
                else {
                    if (this.list && this.list.length > 0 && this.list[0].special) {
                        this.list = noposts;
                    }
                }
            });
        }
    },
    components: {
        PostItem
    }
}
</script>

<style lang="sass" scoped>

.post-list
  margin-top: 20px
  padding-bottom: 20px
  padding-right: 0
  padding-left: 0

.post-list > .row
  margin-bottom: 12px

</style>
