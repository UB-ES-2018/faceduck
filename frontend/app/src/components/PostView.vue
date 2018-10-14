<template>

    <div class="options"> <!-- The below v-on:click and v-bind are not working right now, the idea was to open and close the post -->

        <div class="option active" v-on:click= "showPost = !showPost" v-bind:class="{ active: isActive }">
            
            <div class="shadow"></div> <!--Closing shadow-->
            
            <div class="label">
            
                <div class="icon"> </div> <!--Closing icon-->
            
                <div class="info">
            
                    <div class="main">Nickname</div>
            
                    <div class="sub">Post: Omuke trughte a otuftaaegae rgioaeg earg eaori aegeirg aerka erigjk eargoae gaekjg aerig roinikun kj iuj jiukj ik ik liu i ikjhj ivyghj jtryhjkn tyiubin tufyvgubhin ertyguihoi cfyvgubhinj rtyvubnij tyuboinjo tyuybinjomk tvuybinj tvyubinj tvuybiunjomk ytvubinj tytvubinj ytvubino rcytvubhnij cyvgubhinj cryvtgubhnij tcyvtgbuhnij rtcyvtubyhinj tcyvgbuhj rcttyvgubhj cfyvgubhjn cyvbuhnj f yvgbuhnj ybuinjmok tyvbuonimjo tyubnimo tvyubnimo tybunimo vtybuonij cvtybuonij cvytbuoni tvbuynimo vtybunim ybuinm bnijmk yuobnij tvubynijpm vtbuynijmo vuybinjom yyuo hij tyuyohi jy ghjyvg uhj
                        Post: Omuke trughte a otuftaaegae rgioaeg earg eaori aegeirg aerka erigjk eargoae gaekjg aerig roinikun kj iuj jiukj ik ik liu i ikjhj ivyghj jtryhjkn tyiubin tufyvgubhin ertyguihoi cfyvgubhinj rtyvubnij tyuboinjo tyuybinjomk tvuybinj tvyubinj tvuybiunjomk ytvubinj tytvubinj ytvubino rcytvubhnij cyvgubhinj cryvtgubhnij tcyvtgbuhnij rtcyvtubyhinj tcyvgbuhj rcttyvgubhj cfyvgubhjn cyvbuhnj f yvgbuhnj ybuinjmok tyvbuonimjo tyubnimo tvyubnimo tybunimo vtybuonij cvtybuonij cvytbuoni tvbuynimo vtybunim ybuinm bnijmk yuobnij tvubynijpm vtbuynijmo vuybinjom yyuo hij tyuyohi jy ghjyvg uhj
                        Post: Omuke trughte a otuftaaegae rgioaeg earg eaori aegeirg aerka erigjk eargoae gaekjg aerig roinikun kj iuj jiukj ik ik liu i ikjhj ivyghj jtryhjkn tyiubin tufyvgubhin ertyguihoi cfyvgubhinj rtyvubnij tyuboinjo tyuybinjomk tvuybinj tvyubinj tvuybiunjomk ytvubinj tytvubinj ytvubino rcytvubhnij cyvgubhinj cryvtgubhnij tcyvtgbuhnij rtcyvtubyhinj tcyvgbuhj rcttyvgubhj cfyvgubhjn cyvbuhnj f yvgbuhnj ybuinjmok tyvbuonimjo tyubnimo tvyubnimo tybunimo vtybuonij cvtybuonij cvytbuoni tvbuynimo vtybunim ybuinm bnijmk yuobnij tvubynijpm vtbuynijmo vuybinjom yyuo hij tyuyohi jy ghjyvg uhj
                        Post: Omuke trughte a otuftaaegae rgioaeg earg eaori aegeirg aerka erigjk eargoae gaekjg aerig roinikun kj iuj jiukj ik ik liu i ikjhj ivyghj jtryhjkn tyiubin tufyvgubhin ertyguihoi cfyvgubhinj rtyvubnij tyuboinjo tyuybinjomk tvuybinj tvyubinj tvuybiunjomk ytvubinj tytvubinj ytvubino rcytvubhnij cyvgubhinj cryvtgubhnij tcyvtgbuhnij rtcyvtubyhinj tcyvgbuhj rcttyvgubhj cfyvgubhjn cyvbuhnj f yvgbuhnj ybuinjmok tyvbuonimjo tyubnimo tvyubnimo tybunimo vtybuonij cvtybuonij cvytbuoni tvbuynimo vtybunim ybuinm bnijmk yuobnij tvubynijpm vtbuynijmo vuybinjom yyuo hij tyuyohi jy ghjyvg uhj
                        Post: Omuke trughte a otuftaaegae rgioaeg earg eaori aegeirg aerka erigjk eargoae gaekjg aerig roinikun kj iuj jiukj ik ik liu i ikjhj ivyghj jtryhjkn tyiubin tufyvgubhin ertyguihoi cfyvgubhinj rtyvubnij tyuboinjo tyuybinjomk tvuybinj tvyubinj tvuybiunjomk ytvubinj tytvubinj ytvubino rcytvubhnij cyvgubhinj cryvtgubhnij tcyvtgbuhnij rtcyvtubyhinj tcyvgbuhj rcttyvgubhj cfyvgubhjn cyvbuhnj f yvgbuhnj ybuinjmok tyvbuonimjo tyubnimo tvyubnimo tybunimo vtybuonij cvtybuonij cvytbuoni tvbuynimo vtybunim ybuinm bnijmk yuobnij tvubynijpm vtbuynijmo vuybinjom yyuo hij tyuyohi jy ghjyvg uhj
                        Post: Omuke trughte a otuftaaegae rgioaeg earg eaori aegeirg aerka erigjk eargoae gaekjg aerig roinikun kj iuj jiukj ik ik liu i ikjhj ivyghj jtryhjkn tyiubin tufyvgubhin ertyguihoi cfyvgubhinj rtyvubnij tyuboinjo tyuybinjomk tvuybinj tvyubinj tvuybiunjomk ytvubinj tytvubinj ytvubino rcytvubhnij cyvgubhinj cryvtgubhnij tcyvtgbuhnij rtcyvtubyhinj tcyvgbuhj rcttyvgubhj cfyvgubhjn cyvbuhnj f yvgbuhnj ybuinjmok tyvbuonimjo tyubnimo tvyubnimo tybunimo vtybuonij cvtybuonij cvytbuoni tvbuynimo vtybunim ybuinm bnijmk yuobnij tvubynijpm vtbuynijmo vuybinjom yyuo hij tyuyohi jy ghjyvg uhj
                        Post: Omuke trughte a otuftaaegae rgioaeg earg eaori aegeirg aerka erigjk eargoae gaekjg aerig roinikun kj iuj jiukj ik ik liu i ikjhj ivyghj jtryhjkn tyiubin tufyvgubhin ertyguihoi cfyvgubhinj rtyvubnij tyuboinjo tyuybinjomk tvuybinj tvyubinj tvuybiunjomk ytvubinj tytvubinj ytvubino rcytvubhnij cyvgubhinj cryvtgubhnij tcyvtgbuhnij rtcyvtubyhinj tcyvgbuhj rcttyvgubhj cfyvgubhjn cyvbuhnj f yvgbuhnj ybuinjmok tyvbuonimjo tyubnimo tvyubnimo tybunimo vtybuonij cvtybuonij cvytbuoni tvbuynimo vtybunim ybuinm bnijmk yuobnij tvubynijpm vtbuynijmo vuybinjom yyuo hij tyuyohi jy ghjyvg uhj
                    </div>
            
                </div> <!--Closing info-->
            
            </div> <!--Closing lavel-->
        
        </div> <!--Closing .option 0-->
    
    </div> <!--Closing .options-->

</template>

<style lang="sass" scoped>

    body

        .options

            width: 61%
            .option 
                overflow-y: scroll
                position: relative
                overflow: hidden
    
                background: white
    
                &.active 
                    overflow-y: scroll
                    margin: 4%
                    
                    height: 15em

                    border-radius: 20px

                    .shadow 
    
                        box-shadow: inset 0 -120px 120px -120px black, inset 0 -120px 120px -100px black
    
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
    
                    .shadow 
    
                        bottom: -40px
    
                        box-shadow: inset 0 -120px 0px -120px black, inset 0 -120px 0px -100px black
    
                    .label 
    
                        bottom: 10px
    
                        left: 10px
    
                        .info>div 
    
                            left: 20px
    
                            opacity: 0
    
                .shadow 
    
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

<script>

    export default {

        name: 'PostView',

        data(){
            return{
                isActive: false,
            }
            

        },

        methods: {
    
            showPost() {
    
                this.isActive = !this.isActive;
    
            }
   
        },
    
    };

</script>
