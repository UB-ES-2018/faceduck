<template>
	<div>
        
		<div>
			<ul class="icons" v-on:mouseover="isVisible = true;"
                    v-on:mouseout="isVisible = false;">
				<li><i class="fa fa-thumbs-up" aria-hidden="true"><span> Like </span></i></li>
                <ul class="emotions" id="emotions"
                    v-show="isVisible"><!--&lt;EmotionButtons/&gt;-->
                    <li><img src="http://www.northamericangoldwings.com/community/forums/uploads/reactions/facebook-love-png-44003.png" class="react"></li>
                    <li><img src="http://www.freeiconspng.com/uploads/facebook-live-love-png-1.png" class="react"></li>
                    <li><img src="http://clipart.info/images/ccovers/1499793248facebook-haha.png" class="react"></li>
                    <li><img src="https://cdn4.iconfinder.com/data/icons/reaction/32/angry-512.png" class="react"></li>
                    <li><img src="http://clipart.info/images/ccovers/1499793247facebook-sad-emoji-like-png.png" class="react"></li>
                </ul>
            </ul>
            
		</div>
	</div>
</template>

<script>
export default {
	name: "EmotionButtons",
	props: ["post"],
	data() {
		return {
            isVisible: false,
        }
	},
	methods: {
		mouseOver: function() {
			this.isVisible = true
		}
	}
}
</script>

<style lang="sass" scoped>

.emotions
    position: absolute
    background-color: #fff
    border: 1px solid #9b9797
    left: 9%
    border-radius: 100px
    width: 300px
    

.emotions li
    padding: 10px
    margin: 0 auto
    cursor: pointer

.react
    width: 25px
    height: 25px
    transition: all .2s ease-in-out

.react:hover
    transform: scale(1.7)


.icons
    display: block
    height: 26px

.icons li
    padding: 10px
    padding-top: 5px
    text-align: center
    cursor: pointer
    
ul li
    list-style-type: none
    float: left
    display: block

.fa
	width: 100px
    height: 100px
    color: #ffb511


</style>