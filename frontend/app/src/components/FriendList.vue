<template>
<div class="friend-list">
  <ul class="list-group"><!-- actual bootstrap class 😅 -->
    <a>Your friends:</a>
    <li class="list-group-item"
        
	v-for="result in results" :key="result.username">
      <a v-bind:href="'/user/'+ result.username">{{result.username}}: {{result.name}} {{result.surname}}</a>
    </li>
    <li class="list-group-item" v-if="nores">
      No friends found
    </li>
  </ul>
</div> 
</template>


<script>
var friendsAPI = 'http://' + window.location.hostname + ':5000/user/friends'; //Backend friends search
export default {
  data() {
    return {
      results: [],
      nores: false,
      user: JSON.parse(localStorage.getItem("user"))
    };
  },
  mounted() {
    this.getFriends();
    this.$root.$on("getFriends", (event) => {
      // console.log(event)
      this.results = event.results;
      this.nores = (event.results.length === 0);
    });
  },
  methods: {
        //wip
        
        getFriends() {
          fetch(friendsAPI, {
            method: "GET",
            headers: {
              "Content-Type": "application/json",
              "Authorization": "Bearer " + localStorage.getItem("access-token"),
            }
          }).then(res => res.json())
          .then(data => {
            this.$root.$emit("getFriends", {
              results: data
            });
          });
        },
    }
};
</script>

