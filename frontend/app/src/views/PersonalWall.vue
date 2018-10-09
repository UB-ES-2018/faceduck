<template>
  <div id="PersonalWall">
    <h1>This is the Wall</h1>
  </div>
</template>

<script>

export default {
	name: "PersonalWall",
	data() {
		return {}
	},
	beforeCreate: function() {
		if (!localStorage.getItem("access-token")) {
			this.$router.push("/");
		}
	},
	methods: {
		logout: function() {
			localStorage.removeItem("access-token");
			this.$router.push("/");
		}
	}
}

</script>
