<template>
    <div id="CreateGroup">
        <NavBar/>
    </div>
</template>

<script>
    import NavBar from "../components/NavBar.vue";

    var host = window.location.hostname;
    var apiPostFormUrl = '//' + host + ':5000/post';

    export default {
        name: "CreateGroup",
        data() {
            return {
            }
        },
        components: {
            NavBar,
        },
        created() {
        
        },
    
    }
</script>
