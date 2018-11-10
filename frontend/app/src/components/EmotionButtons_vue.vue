<template>
	<div>
		<ul class="emotions" id="emotions" v-bind:class="{'selected': isVisible}"> <!--&lt;EmotionButtons/&gt;-->
			<li><img src="http://www.northamericangoldwings.com/community/forums/uploads/reactions/facebook-love-png-44003.png" class="react"></li>
			<li><img src="http://www.freeiconspng.com/uploads/facebook-live-love-png-1.png" class="react"></li>
			<li><img src="http://clipart.info/images/ccovers/1499793248facebook-haha.png" class="react"></li>
			<li><img src="https://cdn4.iconfinder.com/data/icons/reaction/32/angry-512.png" class="react"></li>
			<li><img src="http://clipart.info/images/ccovers/1499793247facebook-sad-emoji-like-png.png" class="react"></li>
		</ul>
		<ul class="icons">
			<li v-on:click="mouseOver"><i class="fa fa-thumbs-up" aria-hidden="true" ><span> Like </span></i></li>
		</ul>
		</div>
</template>

<script>
export default {
	name: "EmotionButtons",
	props: ["post"],
	data: {
		isVisible: false,
		return: {}
	},
	methods: {
		mouseOver: function() {
			this.isVisible = !isVisible;
			

		}
	}
}
</script>

<style lang="sass" scoped>

.emotions
	display: none
    background-color: #fff
    border: 1px solid #9b9797
    border-radius: 100px
    float: left
    position: absolute
    left: 40px
    width: 264px
    z-index: 1000
    
.emotions.selected
	display: block

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
    position: absolute
    top: 89%
    margin: 20px auto

.icons li
    border-top: 1px solid #000
    padding: 0
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
    color: gray


</style>