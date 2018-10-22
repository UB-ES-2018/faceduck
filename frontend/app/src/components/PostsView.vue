<template>
    <div class="options" v-if="!nores"> 
    <!-- The below v-on:click and v-bind are not working right now, the idea was to open and close the post -->

        <div class="option active" v-for="result in results" :key="result.id">
            
            <div class="shadowy"></div>
            <!--Closing shadow-->
            
            <div class="label">
            
                <div class="icon"></div>
                <!--Closing icon-->
            
                <div class="info">
            
                    <div class="main">{{result.author.username}}</div>
            
                    <div class="sub">{{result.text}}</div>

                    <div class="image" v-if="result['image-url']">

      	        		<img v-bind:src="result['image-url']" width="100%" height="100%"/>

        			</div>
                    <!--Closing image-->
            
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

        name: 'PostsView',

        data(){
            return{
                results: [],
                nores: false,
            }
        },
    	mounted: function() {
      		this.$root.$on('getPosts', (text) => { // here you need to use the arrow function
                this.results = text.results;
                this.nores = (text.results.length === 0);
            })
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
</style>