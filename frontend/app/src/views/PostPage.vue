<template>
    <div id="PostPage">
        <NavBar/>
        <PostItem v-bind:post="post" v-bind:key="idpost" />
    </div>
</template>

<script>
    import NavBar from "../components/NavBar.vue";
    import PostItem from "../components/PostItem.vue";
    var host = window.location.hostname;
    var apiPostFormUrl = '//' + host + ':5000/post';
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
                return this.$route.params.idpost
            },
            fetchData() {
                /* istanbul ignore next */
                fetch(apiPostFormUrl + '/' + this.idpost, {
                    method: "GET",
                    headers: {
                        "Content-Type": "application/json",
                        "Authorization": "Bearer " + localStorage.getItem("access-token"),
                    },
                }).then(res => {
                    if (res.ok) {
                        res.json().then(data => {
                            this.post = data
                        })
                        //console.log(this.post)
                    } else {
                        this.$router.push("/");
                    }
                })
            }
        },
        created() {
            this.idpost = this.setIdpost()
            this.fetchData()
        },
    
    }
</script>
