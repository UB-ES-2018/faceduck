<template>
    <div id="CreateGroup">
        <NavBar/>
        <GroupForm/>        
    </div>
</template>

<script>
    import NavBar from "../components/NavBar.vue";
    import GroupForm from "../components/GroupForm.vue";

    export default {
        name: "CreateGroup",
        components: {
            NavBar,
            GroupForm,
        },
    }
</script>

<style lang="sass" scoped>

    .container 
        margin-left: auto
        margin-right: auto
        width: 700px
        height: auto
        background:rgb(241, 241, 241)
        color:black !important
        font-family: 'Verdana'
        font-size: 18px
        padding-top: 20px
        padding-bottom: 25px
        -moz-box-shadow: 0px 5px 10px 0px #333, 0px -3px 10px 0px #333
        -webkit-box-shadow: 0px 5px 10px 0px #333, 0px -3px 10px 0px #333
        box-shadow: 0px 5px 10px 0px #333, 0px -3px 10px 0px #333
        -moz-border-radius: .5em
        -webkit-border-radius: .5em
        border-radius: .5em
        
    #text-box 
        background: #f2f2f2
        padding: 6px
        margin-top: -.25%
        margin-bottom: .25%
        height: 1.5%
        font-family: 'Merriweather Sans', sans-serif
        font-size: 14px
        border: 1px solid #82aee8
        -moz-border-radius: 5px
        -webkit-border-radius: 5px
        border-radius: 5px
        -moz-box-shadow: 0 1px 1px #82aee8 inset
        -webkit-box-shadow: 0 1px 1px #82aee8 inset
        box-shadow: 0 1px 1px #82aee8 inset
        width: calc(100% - 45px)

    #text-box:focus 
        background-color: #fff
        border-color: #82aee8
        outline: none
        -moz-box-shadow: 0 0 0 1px #82aee8 inset
        -webkit-box-shadow: 0 0 0 1px #82aee8 inset
        box-shadow: 0 0 0 1px #82aee8 inset
        -webkit-box-sizing: border-box
        -moz-box-sizing: border-box
        box-sizing: border-box

    fieldset 
        border: 0

    .inputbox input
        display: flex
        width: 100%
        height: 40px
        background-color: #f2f2f2
        border: none
        margin-bottom: 20px
        font-size: 12px

    .inputbox button[type="submit"]
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
        cursor: pointer

</style>