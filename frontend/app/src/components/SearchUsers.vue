<template>
    <div id='SearchUsers'>
        <form class="inputbox" >
        <div>
            <input type="text" placeholder="username">
            <button type="button" v-on:click="fakeJson">Searh</button>
        </div>
        </form>
        <div class="results">
            <p  v-for="result in results" :key="result.username">id{{result.id}}: {{result.name}} {{result.surname}} </p>
        </div>   
    </div>   
</template>

<script>
export default {
    data() {
        return{
            results: [],
        };
    },
    methods: {
        //wip
        getUsers() {
            fetch('your-api-here', { params: { keywords: this.keywords } })
                .then(function(response) {return response.json();}).then(function(rj){this.results=rj})
                .catch(error => {});
                console.log(this.results[0]);
        },
        //to emulate api call - json is in correct api format
        fakeJson(){
            this.results=[
            {
            "id":"01",
            "username": "fhgt",
            "email": "fucker@gmail.com",
            "name" : "Dmfdsfdsitri",
            "surname" : "Lalkov",
            "birthday" : "10.12.1981",
            "gender" : "male"
            },
            {
            "id": "02",
            "username": "d222",
            "email": "fucker@gmail.com",
            "name" : "MaMadfim",
            "surname" : "VoTrmpn",
            "birthday" : "10.12.1981",
            "gender" : "male"
            },
            {
            "id": "03",
            "username": "cd01",
            "email": "fucker@gmail.com",
            "name" : "Fenya",
            "surname" : "Baggins",
            "birthday" : "10.12.1981",
            "gender" : "male"
            },
            {
            "id": "04",
            "username": "fru456",
            "email": "fucker@gmail.com",
            "name" : "Sasha",
            "surname" : "Seriy",
            "birthday" : "10.12.1981",
            "gender" : "male"
            },
            {
            "id": "09186777",
            "username": "lastT",
            "email": "fucker@gmail.com",
            "name" : "Neveroyatniy",
            "surname" : "Alk",
            "birthday" : "10.12.1981",
            "gender" : "male"
            }

        ]


        }
    }
}
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

</style>