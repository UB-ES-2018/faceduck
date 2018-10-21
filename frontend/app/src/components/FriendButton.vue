<template>
	<div class="friend-button">
		<button class="btn btn-warning btn-sm" v-if="!friends && !requested">
			<i class="fas fa-user-plus"></i>
			Add {{name}} as a friend
		</button>

		<div v-if="!friends && requested && !requester">
			{{name}} wants to befriend you<br>
			<button class="btn btn-danger btn-sm">
				<i class="fas fa-user-times"></i>
				Reject
			</button>&nbsp;	
			<button class="btn btn-success btn-sm">
				<i class="fas fa-user-check"></i>
				Accept
			</button>
		</div>

		<div v-if="!friends && requested && requester">
			You asked {{name}} to be friends<br>
			<button class="btn btn-danger btn-sm">
				<i class="fas fa-user-times"></i>
				Cancel request
			</button>
		</div>

		<button v-if="friends"
			v-bind:class="{ 
				'btn-primary': !unfriendHover,
				'btn-danger': unfriendHover
			}" class="btn btn-sm friends"
			v-on:mouseenter="unfriendHover = true"
			v-on:mouseleave="unfriendHover = false">
			<span v-if="!unfriendHover">
				<i class="fas fa-user-friends"></i>
				{{name}} and you are friends
			</span>
			<span v-else>
				<i class="fas fa-user-times"></i>
				Revoke friendship
			</span>
		</button>
	</div>
</template>

<script>

export default {
	name: "FriendButton",
	props: {
		userId: String,
		name: String
	},
	data() {
		return {
			friends: false,
			requested: false,
			requester: false,
			unfriendHover: false,
			user: JSON.parse(localStorage.getItem("user"))
		}
	},
	methods: {
	}
}

</script>

<style lang="sass" scoped>
	
.friends
	width: 200px

</style>