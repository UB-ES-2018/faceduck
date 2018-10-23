<template>
  <div id='SearchUsers'>
    <div v-if="nores">
        <h3>No Users found</h3>
    </div>
    <div class="results-list" v-else>
      <div class="results-item" v-for="result in results" :key="result.username">
        <div class="border-b-1 row">
          <div class="results-item-text col-8">
          <h3><a href="#"> {{result.name}} {{result.surname}}</a></h3>
          <h4>{{result.email}}</h4>
          <p>Gender: {{result.gender}}, born: {{result.birthday}}</p>
          </div>
          <div class="col-4 friend-button" v-if="result.id !== user.id">
            <FriendButton 
              v-bind:name="result.name"
              v-bind:userId="result.id"/>
          </div>
        </div>
      </div>
    </div>   
  </div>   
</template>

<script>
import FriendButton from "./FriendButton.vue";

export default {
  data() {
    return {
      results: [],
      nores: false, //ugly way to hide nothing found message
      user: JSON.parse(localStorage.getItem("user"))
    };
  },
  components: {
    FriendButton
  },
  mounted() {
    this.$root.$on("getUserResults", (event) => {
      // console.log(event)
      this.results = event.results;
      this.nores = (event.results.length === 0);
    });
  },
  methods: {
  }
};
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

.friend-button
  display: flex
  justify-content: center
  align-items: center

</style>