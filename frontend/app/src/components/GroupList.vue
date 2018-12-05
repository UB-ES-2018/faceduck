<template>
	<div class="group-list">
		<ul class="list-group"><!-- actual bootstrap class 😅 -->
			<li class="list-group-item"
				v-for="group in groups" v-bind:key="group.id">
				<a v-bind:href="'/group/' + group.id">
					{{group.name}}
				</a>
			</li>
			<li class="list-group-item" v-if="groups.length == 0">
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
	props: ["userId"],
	data() {
		return {
			groups: []
		}
	},
	created() {
		this.fetchGroups();
	},
	methods: {
		fetchGroups() {
			var user_id = this.userId;
			if (user_id === undefined) {
				user_id = JSON.parse(localStorage.getItem("user")).id;
			}

			/* istanbul ignore next */
			fetch(apiGetUser + user_id, {
				method: "GET",
				"Authorization": "Bearer " + localStorage.getItem("access-token"),
			}).then(res => res.json())
			.then(user => {
				if (user.groups !== undefined)
					this.groups = user.groups;
				else
					this.groups = [];
			});
		}
	}
}
</script>

<style scoped>

</style>