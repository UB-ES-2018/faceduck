<template>
    <div class="logs">
        <div class="l-frame">
            <div class="l-list" v-for="log in logs" :key="log">
                <div class="l-info">
                    <div class="l-main">{{log.date}}, ip {{log.ip}}, using {{log.device}}, Success: {{log.state}} </div><!--WARNING - get real author-->
                </div>
            </div>
            
        </div>
        
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
.comments
  color: black

.comments button
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

</style>