<template>
    <div class="logs">
        <div class="l-frame">
            <span >Login history:</span>
            <div class="l-list" v-for="log in logs" :key="log">
                <div class="l-info">
                    <span>[{{log.date}}] IP {{log.ip}}, using {{log.device}} </span><!--WARNING - get real author-->
                <font v-if="log.state==true" color='green'>[Success]</font>
            <font v-else color='red'>[Failed]</font>
                </div>

            </div>
            

            
        </div>
        <button class="l-back" onclick="location.href='/wall'">Back</button>
    </div>



</template>


<script>
var host = window.location.hostname
var commentAPI = 'http://' + host + ':5000/login_logs'; //Backend  logs retrieving

export default {
	name: "Login_logs",
	props: {
        logs: [],
        //user: JSON.parse(localStorage.getItem("user"))
	},
	data() {
		return {
			authors: [],
            commentText: ""
		}
	},
	mounted() {
		if(this.count!=0){
            this.getLogs();
        }
    },
	methods: {
		getLogs: function(){
            fetch(commentAPI , {
            method: "GET",
            headers: {
                "Content-Type": "application/json",
                "Authorization": "Bearer " + localStorage.getItem("access-token"),
            }
          }).then(res => res.json())
          .then(data => {
            this.logs = data;
          });
        },
	}
}

</script>


<style lang="sass" scoped>
.logs
  
  margin-left: auto
  margin-right: auto
  width: auto
  height: auto
  background-color: rgb(241, 241, 241)
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

.logs button
  background-color: #ffb511
  border: none
  color: black
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