<template>

	<div class="group-list">
		<ul class="list-group"><!-- actual bootstrap class 😅 -->
			<li class="list-group-item"
				v-for="group in internalGroups" v-bind:key="group.id">
				<a v-bind:href="'/group/' + group.id">
					{{group.name}}
				</a>
			</li>
			<li class="list-group-item" v-if="internalGroups.length == 0">
				No groups yet!
			</li>
		</ul>

	</div>

</template>

<script>
var host = window.location.hostname
var apiGetUser  = '//'+ host +':5000/user/';

export default {
	name: "GroupList",
	props: ["userId", "groups"],
	data() {
		return {
			groups_: []
		}
	},
	computed: {
		internalGroups: {
			get: function() {
				if (this.groups) return this.groups;
				else return this.groups_;
			},
			set: function(groups) {
				this.groups_ = groups;
			} 
		}
	},
	mounted() {
		if (!this.groups) {
			this.fetchGroups();
		}
	},
	methods: {
		fetchGroups() {
			if (!this.userId) {
				user_id = JSON.parse(localStorage.getItem("user")).id;
			} else {
				var user_id = this.userId;
			}

			/* istanbul ignore next */
			fetch(apiGetUser + user_id, {
				method: "GET",
				"Authorization": "Bearer " + localStorage.getItem("access-token"),
			}).then(res => res.json())
			.then(user => {
				if (user.groups !== undefined)
					this.groups_ = user.groups;
				else
					this.groups_ = [];
			});
		}
	}
}
</script>

<style scoped>

</style>
