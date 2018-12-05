<template>
    <div id="CreateGroup">
        <NavBar/>
        <div class="container">
            <form class='inputbox'>
                <fieldset class="inputs">
                    <p><b>Group Name</b></p> <!--HAY QUE GUARDAR EL NOMBRE PARA LUEGO PODER ENVIARLO-->
                    <textarea cols="5" rows="1" type="text" name="name" id="text-box" placeholder="Name"></textarea>
                </fieldset>
            </form>
            
            <p><b>Add people</b></p>
            <div v-for="friend in friends" :key="friend" class="form-group">
                <input type="checkbox" class="form-check-input" v-on:click="members.push(friend)"> 
                <label name="friend" value="friend" class="form-check-label">{{ friend }}</label>
            </div>
            
            <form class='inputbox' v-on:submit="submitGroup">    
                <fieldset class="actions">
                    <button type="submit"> Create </button>
                </fieldset>
            </form>
        </div>
    </div>
</template>

<script>
    import NavBar from "../components/NavBar.vue";

    var host = window.location.hostname;
    var apiGetFriendsUrl = '//' + host + ':5000/user/friends/' + JSON.parse(localStorage.getItem("user"))["id"];
    var apiCreateGroupUrl = '//' + host + ':5000/group';

    export default {
        name: "CreateGroup",
        data() {
            return {
                friends: ["Maria", "Pablo", "Mario", "Choripan"], // ESTO TENDRIAN QUE SER LOS AMIGOS DEL USER
                group: {
                    name:"",
                },
                groupID: "",
                members: [],
            }
        },
        components: {
            NavBar,
        },
        created() {
            fetch(apiGetFriendsUrl, {
                method: "GET",
                headers: {
                    "Authorization": "Bearer " + localStorage.getItem("access-token"),
                },
            })
            .then((response) => {
                if (response.ok) { // REVISAR ESTO
                    //alert(JSON.stringify(response));
                    
                }
            }).catch(() => {});
            
        },
        methods: {
            submitGroup() {
                fetch(apiCreateGroupUrl, {
                    method: "POST",
                    headers: {
                        "Authorization": "Bearer " + localStorage.getItem("access-token"),
                        "Content-Type": "application/json",
                    },
                    //body: JSON.stringify(group)
                })
                .then((response) => {
                    if (response.ok) {    
                        //response.json().then((json) => {
                            //alert(JSON.stringify(response));
                            //groupID = response.id;
                            //apiCreateGroupUrl = apiCreateGroupUrl + groupID + "/members";
                        //});
                    }
                }).catch(() => {});

                /*for (i in members){
                    fetch(apiCreateGroupUrl, {
                        method: "POST",
                        headers: {
                            "Content-Type": "application/json",
                        },
                        //body: JSON.stringify(i) // HAY QUE PASARLE EL ID
                    })
                    .then((response) => {
                        if (response.ok) {    
                            response.json().then((json) => {
                                //alert(JSON.stringify(response));
                                this.$router.push("/group/" +  response.id); // VAMOS A LA PAG DEL GRUPO
                            });
                        }
                    }).catch(() => {});
                }*/
            },
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