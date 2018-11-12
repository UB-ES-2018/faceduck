<template>
	<div>  
        <ul class="emotions" id="emotions" v-show="isVisible"><!--&lt;EmotionButtons/&gt;-->
            <li><img src="http://www.northamericangoldwings.com/community/forums/uploads/reactions/facebook-love-png-44003.png" class="react"></li>
        </ul>
	</div>
</template>

<script>
export default {
	name: "EmotionButtons",
	props: ["post"],
	data() {
		return {
            isVisible: true,
        }
	}
}
</script>

<style lang="sass" scoped>

.emotions
    height: 26px

.emotions li
    padding: 10px

.react
    width: 25px
    height: 25px
    
ul li
    list-style-type: none
    float: left

</style>