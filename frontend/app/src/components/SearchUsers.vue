<template>
    <div id='SearchUsers'>
        <form class="inputbox"   v-on:submit.prevent="send">
        <div>
            <input type="text" placeholder="username" v-model="searchQuery"  v-on:keyup.enter="getUsers">
            <button type="button" v-on:click="getUsers">Searh</button>
        </div>
        </form>
        <div class="results">
            <p  v-for="result in results" :key="result.username">id{{result.id}}: {{result.name}} {{result.surname}} </p>
        </div>   
    </div>   
</template>

<script>
var apiUsersSearchUrl  = 'http://192.168.1.101:5000/user/search'; //Backend ip

export default {
    data() {
        return{
            results: [],
            searchQuery: "",
        };
    },
    methods: {
        //wip
        getUsers() {
            fetch(apiUsersSearchUrl+"?query="+this.searchQuery, {
                method: "POST",
                headers: {
                "Content-Type": "application/json"
                },
                body: JSON.stringify({query: this.searchQuery})
            }).then(res => res.json())
            .then(data => this.results = data);
            
        },
        
    }
}
</script>

<style lang="sass" scoped>




.inputbox button
  background-color: #ffb511
  border: none
  color: white
  font-size: 12px
  font-weight: bold
  box-sizing: content-box
  padding: 10px
  border-radius: 10px
  width: 60px
  position: relative
  left: 1% 
  cursor: pointer

</style>