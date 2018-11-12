<template>
    <div id='VisField'>
        <select name="VisF" v-model="this.visibility" required>
                      <option value="" disabled selected>Select one…</option>
                      <option value="Public">Public</option>
                      <option value="Logged">Logged Only</option>
                      <option value="Friends">Friends Only</option>
                      <option value="Private">Only For Me</option>
                    </select>
    </div>
</template>

<script>
    export default {
        name: 'VisField',
        data() {
            return {
                visibility: 'Friends',
            }
        }
    }
</script>
<style lang="sass" scoped>
    select
        position: relative
        left: 255px
        bottom: 10px
        height: 25px
        font-size: 15px
</style>

