<template>
    <div class="options">
    
    
    
        <div class="option active" v-on:click="addCount" v-bind:class="{active: (count%4==0)}" style="--optionBackground:url(https://66.media.tumblr.com/6fb397d822f4f9f4596dff2085b18f2e/tumblr_nzsvb4p6xS1qho82wo1_1280.jpg);">
    
            <div class="shadow"></div>
    
    
    
            <div class="label">
    
    
    
                <div class="icon">
    
    
    
                    <i class="fas fa-walking"></i>
    
    
    
                </div>
    
    
    
                <div class="info">
    
    
    
                    <div class="main">Blonkisoaz</div>
    
    
    
                    <div class="sub" style="font-size:1vw;">Omuke trughte a otufta hola estoy haciendo pruebas con este codigo
    
    
    
                    </div>
    
    
    
                </div>
    
    
    
            </div>
    
    
    
        </div>
    
    
    
        <div class="option" v-on:click="addCount" v-bind:class="{active: (count%4==1)}" style="--optionBackground:url(https://66.media.tumblr.com/8b69cdde47aa952e4176b4200052abf4/tumblr_o51p7mFFF21qho82wo1_1280.jpg);">
    
    
    
            <div class="shadow"></div>
    
    
    
            <div class="label">
    
    
    
                <div class="icon">
    
    
    
                    <i class="fas fa-snowflake"></i>
    
    
    
                </div>
    
    
    
                <div class="info">
    
    
    
                    <div class="main">Oretemauw</div>
    
    
    
                    <div class="sub">Omuke trughte a otufta</div>
    
    
    
                </div>
    
    
    
            </div>
    
    
    
        </div>
    
    
    
        <div class="option" v-on:click="addCount" v-bind:class="{active: (count%4==2)}" style="--optionBackground:url(https://66.media.tumblr.com/5af3f8303456e376ceda1517553ba786/tumblr_o4986gakjh1qho82wo1_1280.jpg);">
    
    
    
            <div class="shadow"></div>
    
    
    
            <div class="label">
    
    
    
                <div class="icon">
    
    
    
                    <i class="fas fa-tree"></i>
    
    
    
                </div>
    
    
    
                <div class="info">
    
    
    
                    <div class="main">Iteresuselle</div>
    
    
    
                    <div class="sub">Omuke trughte a otufta</div>
    
    
    
                </div>
    
    
    
            </div>
    
    
    
        </div>
    
    
    
        <div class="option" v-on:click="addCount" v-bind:class="{active: (count%4==3)}" style="--optionBackground:url(https://66.media.tumblr.com/5516a22e0cdacaa85311ec3f8fd1e9ef/tumblr_o45jwvdsL11qho82wo1_1280.jpg);">
    
    
    
            <div class="shadow"></div>
    
    
    
            <div class="label">
    
    
    
                <div class="icon">
    
    
    
                    <i class="fas fa-tint"></i>
    
    
    
                </div>
    
    
    
                <div class="info">
    
    
    
                    <div class="main">Idiefe</div>
    
    
    
                    <div class="sub">Omuke trughte a otufta</div>
    
    
    
                </div>
    
    
    
            </div>
    
    
    
        </div>
    
    
    
        <div class="option" v-on:click="addCount" v-bind:class="{active: (count%4==4)}" style="--optionBackground:url(https://66.media.tumblr.com/f19901f50b79604839ca761cd6d74748/tumblr_o65rohhkQL1qho82wo1_1280.jpg);">
    
    
    
            <div class="shadow"></div>
    
    
    
            <div class="label">
    
    
    
                <div class="icon">
    
    
    
                    <i class="fas fa-sun"></i>
    
    
    
                </div>
    
    
    
                <div class="info">
    
    
    
                    <div class="main">Inatethi</div>
    
    
    
                    <div class="sub">Omuke trughte a otufta</div>
    
    
    
                </div>
    
    
    
            </div>
    
    
    
        </div>
    
    
    
    </div>
</template>

<style lang="scss" scoped>

$optionDefaultColours: #ED5565,#FC6E51,#FFCE54,#2ECC71,#5D9CEC,#AC92EC;

body {
   display:flex;
   flex-direction:row;
   justify-content:center;
   align-items:center;
   overflow:hidden;
   
   height:100vh;
   
   font-family: 'Roboto', sans-serif;
   .credit {
      position: absolute;
      bottom:20px;
      left:20px;
      
      color:#000;
   }
   .options {
      display:flex;
      flex-direction:column;
      align-items:stretch;
      overflow:hidden;

      min-height:300px;
      max-height:15000px;
      height:calc(100% - 100px);
      
      width:900px;
      
      @for $i from 1 through 4 {
         @media screen and (max-height:798px - $i*80) {
            min-height:600px - $i*80;
            .option:nth-child(#{6-$i}) {
               display:none;
            }
         }
      }
      
      .option {
         position: relative;
         overflow: hidden;

         min-height:60px;
         margin:10px;

         background:var(--optionBackground, var(--defaultBackground, #E6E9ED));
         background-size:auto 120%;
         background-position:center;

         cursor: pointer;

         transition:.5s cubic-bezier(0.05, 0.61, 0.41, 0.95);

         @for $i from 1 through length($optionDefaultColours) {
            &:nth-child(#{$i}) {
               --defaultBackground:#{nth($optionDefaultColours, $i)};
            }
         }
         &.active {
            flex-grow:100;
            transform:scale(1);
            
            max-height:600px;
            height: 25vw;
            margin:0px;
            border-radius:40px;
            
            background-size:auto 200%;
            .shadow {
               box-shadow:inset 0 -120px 120px -120px black, inset 0 -120px 120px -100px black;
            }
            .label {
               bottom: 50px;
               left: 10px;
               .info >div {
                  width: 95%;
                  opacity: 1;
                  text-align: justify;
                  text-justify: inter-word;
               }
            }
         }
         &:not(.active) {
            flex-grow:10;
            
            background-size:auto 1000%;
            border-radius:30px;
            .shadow {
               bottom:-40px;
               box-shadow:inset 0 -120px 0px -120px black, inset 0 -120px 0px -100px black;
            }
            .label {
               bottom:10px;
               left:10px;
               .info >div {
                  left:20px;
                  opacity:0;
               }
            }
         }
         .shadow {
            position: absolute;
            bottom:0px;
            left:0px;
            right:0px;
            
            height:120px;
            
            transition:.5s cubic-bezier(0.05, 0.61, 0.41, 0.95);
         }
         .label {
            display:flex;
            position: absolute;
            right:0px;

            height:15vw;
            transition:.5s cubic-bezier(0.05, 0.61, 0.41, 0.95);
            .icon {
               display:flex;
               flex-direction:row;
               justify-content:center;
               align-items:center;
               
               min-width:40px;
               max-width:40px;
               height:40px;
               border-radius:100%;

               background-color:white;
               color:var(--defaultBackground);
            }
            .info {
               display:flex;
               flex-direction:column;
               justify-content:center;
               
               margin-left:10px;
               margin-right:0px;
               color:white;
               white-space: post;
               >div {
                  position: relative;
                  
                  transition:.5s cubic-bezier(0.05, 0.61, 0.41, 0.95), opacity .5s ease-out;
               }
               .main {
                  font-weight:bold;
                  font-size:1.2rem;
               }
               .sub {
                  transition-delay:.1s;
               }
            }
         }
      }
   }
}     
</style>
<script>
    export default {
    
        name: 'PostView',

        data :{
            count: 0,
        },

        methods: {
            
            addCount() {
                this.count++;
    
            }
   
        },


    
    };
</script>
