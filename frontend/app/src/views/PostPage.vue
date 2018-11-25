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
    export default {
        name: "PostPage",
        data() {
            return {
                idpost: "",
                post: {},
            }
        },
        components: {
            PostItem,
            NavBar,
        },
        created() {
            this.idpost = this.$route.params.idpost
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
        },
    
    }
</script>
