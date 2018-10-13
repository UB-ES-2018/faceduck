<template>
    <div id='SearchUsers'>
        <form class="inputbox"   v-on:submit.prevent="send">
        <div>
            <input type="text" placeholder="username" v-model="searchQuery"  v-on:keyup.enter="getUsers">
            <button type="button" v-on:click="getUsers">Searh</button>
        </div>
        </form>
        <div class="results-list">
            <div class="results-item" v-for="result in results" :key="result.username">
                <div class="border-b-1">
                <div class="results-item-text">
                    <h3><a href="#"> {{result.name}} {{result.surname}}</a></h3>
                    <h4>{{result.email}}</h4>
                    <p>{{result.gender}}, born: {{result.birthday}}</p>
                </div>
                </div>

            </div>
        </div>   
    </div>   
</template>

<script>
var apiUsersSearchUrl  = 'http://localhost:5000/user/search'; //Backend ip

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
            fetch(apiUsersSearchUrl, {
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




h3
  font-size: 18px;
h4
  font-size: 16px;
  
.results-item
  border: 10px
  color: white
  font-size: 12px
  font-weight: bold
  box-sizing: content-box
  padding: 10px
  position: relative 
  cursor: pointer
  //text-align: left
  //width: 200px

.results-list
  


.border-b-1
  border-bottom: 1px solid rgba(225,225,225,.16)



</style>