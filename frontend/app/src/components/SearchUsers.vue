<template>
<div id='SearchUsers'>
  
  <div class="results-item" v-if="nores">
    <h3>No Users found</h3>
  </div>
  
  <div class="results-item" v-for="result in results" :key="result.username" v-else>
    <div class="user-content">
      <h3><a :href="'/profile/'+result.id"> {{result.name}} {{result.surname}}</a></h3>
      <h4>{{result.email}}</h4>
      <p>Gender: {{result.gender}}, born: {{result.birthday}}</p>
    </div>
    
    <div class="friend-button-container" v-if="result.id !== user.id">
      <FriendButton class="friend-button"
        v-bind:name="result.name"
        v-bind:userId="result.id"/>
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
      console.log(event.results)
      this.results = event.results;
      this.nores = (event.results.length === 0);
    });
  },
  methods: {
  }
};
</script>

<style lang="sass" scoped>
@import '../assets/global.sass';

#SearchUsers
  width: 100%
  & > .results-item
    width: 100%
    border-radius: 8px
    border: 1px #666 solid
    padding: 10px 20px
    background-color: $lightgray
    text-align: left
    overflow-wrap: break-word
    margin-bottom: 12px
    display: flex
    flex-direction: row
    align-items: center
    justify-content: space-between
    &:last-child
      margin-bottom: 0
    & > .user-content
      & > h3
        font-size: 18px;
        color: $darkprimary
      & > h4
        font-size: 16px;
        color: $darkprimary
      & > p
        color: $darkprimary
    & > .friend-button-container
      display: flex
      justify-content: center
      align-items: center
      //& > .friend-button
      

.inputbox button
  background-color: $primary
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
