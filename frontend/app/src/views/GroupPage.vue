<template>
  <div id="GroupPage">
    <NavBar/>
    <div class="containerPhoto" align="center">
        <div class="photo"></div>
        <div class="groupname" v-bind:groupname="groupname">
          {{ groupname }}
        </div>
    </div>
    <button class="btn btn-warning btn-sm" id="Add" 
        v-on:click="addUserToGroup" v-show="!added">
        <i class="fas fa-user-plus"></i>
        Add to group
    </button>
    <button class="btn btn-danger btn-sm" id="Cancel"
        v-on:click="deleteUserFromGroup" v-show="added">
        <i class="fas fa-user-times"></i>
        Cancel
    </button>
  </div>
</template>

<script>
import NavBar from "../components/NavBar.vue";

var host = window.location.hostname;
var apiGroups = '//' + host + ':5000/group';

export default {
    name: 'GroupPage',
    data() {
        return {
            id: '',
            groupname: '',
            added: '',
            users: 0,

        }
    },
    created() {
        this.id = this.$route.params.idgroup; // Obtenemos el id del grupo de la URI
        this.getGroupInfo();
    },
    updated() {},
    components: {
        NavBar,
    },
    methods: {
        getGroupInfo() {
            var apiGetGroup = apiGroups + '/' + this.id;
            /* istanbul ignore next */
            fetch(apiGetGroup, {
                method: "GET",
                headers: {
                    "Content-Type": "application/json",
                },
            })
            .then((response) => {
                if (response.ok) {
                    response.json().then(resp => {
                        this.groupname=resp.name;
                        this.users = resp.users.length;
                        for(var i in resp.users){
                            if(resp.users[i].id == JSON.parse(localStorage.getItem("user"))["id"]){
                                this.added = true;
                            } else {
                                this.added = false;
                            }
                        }                            
                    }) 
                } else {
                    this.$router.push("/wall"); // Si hay un error volvemos a wall
                }
            }).catch();
        },
        addUserToGroup(e) {
            /* istanbul ignore next */
            e.preventDefault();
            /* istanbul ignore next */
            var apiAddUserUrl = apiGroups + '/' + this.id + '/members';
            /* istanbul ignore next */
            fetch(apiAddUserUrl, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
            })
            .then((response) => {
                if (response.ok) {
                    this.added = !this.added;
                }
            }).catch(() => {});
        },
        deleteUserFromGroup(e) {
            /* istanbul ignore next */
            e.preventDefault();
            /* istanbul ignore next */
            var apiDeleteUserUrl = apiGroups + '/' + this.id + '/members/'+ JSON.parse(localStorage.getItem("user"))["id"];
            /* istanbul ignore next */
            fetch(apiDeleteUserUrl, {
                method: "DELETE",
                headers: {
                    "Authorization": "Bearer " + localStorage.getItem("access-token"),
                    "Content-Type": "application/json",
                },
            })
            .then((response) => {
                if (response.ok) {
                    if(this.users==1){
                        this.$router.push("/wall");
                    }
                    this.added = !this.added;
                }
            }).catch(() => {});
        },
    },
}

</script>

<style lang="sass" scoped>

.title
  font-family: "Avenir", Helvetica, Arial, sans-serif
  text-align: center
  color: #ffb511
  text-shadow: 3px 3px #555
  font-size: 25px

.button
  background-color: #ffb511
  border: none
  color: white
  font-size: 12px
  font-weight: bold
  box-sizing: content-box
  padding: 10px
  border-radius: 10px
  width: 60px
  left: 40% 
  cursor: pointer

.containerPhoto
    min-width: 100%
    background: #ffb511
    height: 25vh
    box-shadow: inset 0 -120px 120px -120px black, inset 0 -120px 120px -100px black
    
.photo
    border-radius: 100%
    background-color: gray
    height: 15vh
    width: 15vh

.groupname
    color: black
    font-size: 4vh

</style>