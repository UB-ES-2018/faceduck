<template>

    <div class="options"> 
    <!-- The below v-on:click and v-bind are not working right now, the idea was to open and close the post -->

        <div class="option active" v-if="isVisible">
            
            <div class="shadowy"></div>
            <!--Closing shadow-->
            
            <div class="label">
            
                <div class="icon"></div>
                <!--Closing icon-->
            
                <div class="info">
            
                    <div class="main">{{post.user}}</div>
            
                    <div class="sub">{{post.text}}</div>

                    <div class="image" v-if="post.image">

      	        		<img v-bind:src="post.image"/>

        			</div>
            
                </div>
                <!--Closing info-->
            
            </div>
            <!--Closing lavel-->
        
        </div>
        <!--Closing .option -->
    
    </div>
    <!--Closing .options-->

</template>

<script>

    var host = window.location.hostname;
    var apiPostFormUrl = '//' + host + ':5000/post';
      
    export default {

        name: 'PostView',

        data(){
            return{
                isVisible: false,
        		post: {
          			user:"",
	          		text:"",
        	  		image:""
        		},
	        	message: "",
            }
        },

        created: function() {
      		if (localStorage.getItem("isPostVisible") != null) {
        		this.isVisible = localStorage.getItem("isPostVisible")
      		}
      		//alert(this.isVisible)
    	},
    	mounted: function() {
      		this.$root.$on('showPost', (text) => { // here you need to use the arrow function
        	    //alert(text)
        	    if (text != null) {
          		    var lastPost = JSON.parse(localStorage.getItem("lastPost"));
              		this.isVisible = true;

              		this.post.text = lastPost["text"];
              		this.post.user = lastPost["author"]["username"];

    		    	//this.post.text = JSON.parse(localStorage.getItem("lastPost"))["text"];
		            //this.post.user = JSON.parse(localStorage.getItem("lastPost"))["author"]["username"];

              		this.post.image = lastPost["image-url"];
              		console.log(this.post)
              		//alert(this.post.user)  
        	    }
            })
        },

        methods: {
    
            showPostLast() {
                fetch(apiGetPost, {
            		method: "GET",
            		headers: {
              			"Content-Type": "application/json"
            		},
            		body: JSON.stringify(localStorage.getItem("lastPost"))
          	    }).catch((r) => alert(r))
          	    .then((response) => {
            		if (response.ok) {
              			response.json().then((json) => {
                			localStorage.setItem("lastPost",
               		   		JSON.stringify(json));
                			//alert(JSON.stringify(json))
              			});
            		} else {
              			// ToDo: highlight bad fields
            		}
            		//alert(JSON.stringify(this.post))
       		    });
    
            },
   
        },
    
    }

</script>

<style lang="sass" scoped>

    .options

        width: 61%

        .option
            position: relative
            overflow: hidden
            background: white
            overflow-y: scroll
            
            &.active 
                overflow-y: scroll
                margin: 4%
                    
                height: 15em

                border-radius: 20px

                .label 
                    width: 100%

                    .info>div 
    
                        width: 95%

                        opacity: 1
    
                        text-align: justify
    
                        text-justify: inter-word

                        color: #000
                        
            &:not(.active) 
    
                flex-grow: 10
    
                background-size: auto 1000%
    
                border-radius: 30px
    
                .shadowy 
    
                    bottom: -40px
    
                    .label 
    
                        bottom: 10px
    
                        left: 10px
    
                        .info>div 
    
                            left: 20px
    
                            opacity: 0
    
            .shadowy 
    
                position: absolute
    
                bottom: 0vh
    
                left: 0px
    
                right: 0px
    
                height: 120px
    
                transition: .5s cubic-bezier(0.05, 0.61, 0.41, 0.95) 
    
            .label 
    
                display: flex

                text-align: center
    
                .icon 
    
                    min-width: 40px
    
                    max-width: 40px
    
                    height: 40px
    
                    border-radius: 100%
    
                    background-color: gray

                .info 
    
                    margin-left: 10px
    
                    .main 
    
                        font-weight: bold
    
                        font-size: 1.2rem
    
                    .sub 
                        transition-delay: .1s