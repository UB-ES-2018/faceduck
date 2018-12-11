
<template>
<form class="visibility-form input-group">
  <div class="form-control"><i class="fas fa-globe-africa"></i></div>
  <select class="form-control custom-select" id="VisField" name="VisF" v-on:change="setValue()" v-model="visibility" required>
    <option value="" disabled selected>Select one…</option>
    <option value="public">Public</option>
    <option value="loggedin">Logged Only</option>
    <option value="friends">Friends Only</option>
    <option value="private">Only For Me</option>
  </select>
</form>
</template>

<script scoped>
export default {
    name: 'VisibilityField',
    data() {
        return {
            visibility:'friends'
        }
    },
    methods:{
        setValue /* istanbul ignore next */ (){
            this.$root.$emit("visibilityChange", {
                visibility: this.visibility
            });
        }
    }
}
</script>

<style lang="sass" scoped>
@import '../assets/global.sass';

.visibility-form
  width: auto

.visibility-form > div
  width: 40px
  flex: none
  //color: $accent3
  //background-color: $darkgray

.visibility-form > select
  flex: none
  width: auto
  font-size: 15px
</style>

