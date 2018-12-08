<template>
    <div id="PostPage">
        <NavBar/>
        <PostItem v-bind:post="post" v-bind:key="idpost" />
    </div>
</template>

<script>
import PostItem from "../components/PostItem.vue";
import NavBar from "../components/NavBar.vue";
var host = window.location.hostname;
var apiPostFormUrl = '//' + host + ':5000/post';

// http://localhost:8080/post/82c45212-b2cc-4699-b7cc-5ba55e74262e
export default {
    name: "PostPage",
    data() {
        return {
            idpost: "",
            post: {},
        }
    },
    components: {
        NavBar,
        PostItem
    },
    methods: {
        setIdpost() {
            return this.$route.params.idpost;
        },
        fetchData() {
            var accessToken = localStorage.getItem("access-token");
            var headers = {};
            if (accessToken) {
                headers = {
                    "Content-Type": "application/json",
                    "Authorization": "Bearer: " + accessToken
                };
            }
            fetch(apiPostFormUrl + '/' + this.idpost, {
                method: "GET",
                headers: headers
            }).then(res => {
                if (res.ok) {
                    res.json().then(data => {
                        this.post = data;
                    });
                } else {
                    //this.$router.push("/");
                    console.log(res)
                }
            });
        }
    },
    created() {
        this.idpost = this.setIdpost();
        this.fetchData();
    },

}
</script>
