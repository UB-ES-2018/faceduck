<template>
    <div id='SearchPost'>
        <template v-if="nores">
            <h3>No posts found</h3>
        </template>
        <div class="results-list" v-else>
            <div class="results-item" v-for="result in results" :key="result.id">
                <div class="border-b-1">
                <div class="results-item-text">
                    <h3><a href="#"> {{result.author.username}} </a></h3>
                    <h4>{{result.text}}</h4>
                </div>
                </div>

            </div>
            
        </div>   
    </div>   
</template>

<script>
export default {
  data() {
    return{
      results: [],
      nores: false,//ugly way to hide nothing found message
    };
  },
  mounted(){
    this.$root.$on("getPostResults", (event) => {
      //console.log(event)
      this.results = event.results;
      this.nores = (event.results.length === 0);
    });
  },
  methods: {        
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

.border-b-1
  border-bottom: 1px solid rgba(225,225,225,.16)
</style>