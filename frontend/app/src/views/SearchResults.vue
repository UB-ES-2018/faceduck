<template>
    <div id='SearchResults'>
      <h1>Search results</h1>
      <SearchBar/>
      <template v-if="nores">
          <h3>Nothing found</h3>
      </template>
      <div class="results-list" v-else>
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

import SearchBar from "../components/SearchBar.vue";

export default {
    name: "SearchResults",
    data() {
        return{
            results: [],
            nores: false,//ugly way to hide nothing found message
        };
    },
    mounted() {
      this.$root.$on("getResults", (event) => {
        console.log(event)
        this.results = event.results;
        this.nores = (event.results.length === 0);
      });
    },
    components: {
      SearchBar
    }
}
</script>

<style lang="sass" scoped>
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