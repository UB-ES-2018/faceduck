<template>
    <div id='GroupForm'>
        <div class="container">
            <form class='inputbox' v-on:submit="submitGroup">
                <fieldset class="inputs">
                    <p><b>Group Name</b></p>
                    <textarea cols="5" rows="1" type="text" name="name" id="text-box" v-model="group.name" placeholder="Name"></textarea>
                </fieldset> 
                <fieldset class="actions">
                    <button type="submit"> Create </button>
                </fieldset>
            </form>
        </div>
    </div>
</template>

<script>
    var host = window.location.hostname;
    var apiCreateGroupUrl = '//' + host + ':5000/group';
    
    export default {
        name: 'GroupForm',
        data() {
            return {
                group: {
                    name: '',
                },
            }
        },
        beforeCreate() {
            
        },
        methods: {
            submitGroup(e) {
                /* istanbul ignore next */
                e.preventDefault();
                fetch(apiCreateGroupUrl, {
                    method: "POST",
                    headers: {
                        "Authorization": "Bearer " + localStorage.getItem("access-token"),
                        "Content-Type": "application/json",
                    },
                    body: JSON.stringify(this.group),
                })
                .then((response) => {
                    if (response.ok) {
                        response.json().then(resp => {
                            this.$router.push("/group/" + resp.id); // Vamos a la pagina del grupo recien creado
                        }) 
                        
                    }
                }).catch(() => {});
            },
        
        },
    };
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
        left: 40% 
        cursor: pointer

</style>
