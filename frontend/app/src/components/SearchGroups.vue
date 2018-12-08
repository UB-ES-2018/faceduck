<template>
    <div id="SearchGroups">
            <GroupList v-bind:groups="this.groups"/>
    </div>
</template>

<script>
var host = window.location.hostname
var apiGroupSearchUrl = 'http://' + host + ':5000/group/search'; //Backend ip
import GroupList from "./GroupList.vue";
export default {
    name: "SearchGroups",
    data() {
        return {
            groups: [],
            query:"",
            user:localStorage.getItem('user')
        }
    },
    methods: {
        fetchGroups() {
            console.log(this.query);
            fetch(apiGroupSearchUrl, {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json",
                        "Authorization": "Bearer " + localStorage.getItem("access-token"),
                    },
                    body: JSON.stringify({
                        query: this.query
                    })
                }).then(res => res.json())
                .then(data => {
                    this.groups = data
                });
        }
    },
    components:{
        GroupList
    },
    created() {
        this.$root.$on("groupEvent", (event) => {
            if (event && event.query) this.query = event.query.trim();
                this.fetchGroups();
        });
    }
}
</script>

