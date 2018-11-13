<template>
    <div class="post-list container">
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
            _query: "",
            fetch_options: ""
        };
    },
    created() {
        if (this.query)
            this._query = this.query.trim();
        else
            this._query = "";

        this.fetchPosts();
        this.$root.$on("postEvent", (event) => {
            if (event && event.query) this._query = event.query.trim();
            this.fetchPosts();
        });
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
                if (this.authorId)
                    body["author-id"] = this.authorId;

                else /*if (this._query)*/ {
                    if (this._query.indexOf(" ") == -1 
                        && this._query.lastIndexOf("#") == 0)
                        body["tag"] = this._query.slice(1);
                    else
                        body["query"] = this._query;
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
            
            fetch(api, this.fetch_options)
            .then(res => res.json())
            .then(res => {
                if (res.length > 0)
                    this.list = res;
                else
                    this.list = [{
                        "author": {
                            "username": "No posts found"
                        },
                        "text": "",
                        "special": "no-posts"
                    }];
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

.post-list > .row
    margin-bottom: 12px

</style>