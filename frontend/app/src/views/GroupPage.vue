<template>
	<div></div>
</template>

<script>
export default {
	name: "GroupPage",
	data() {
		return {
			groupid: -1
		}
	},
	created() {
        this.groupid = this.$route.params.groupid;
	}
};
</script>

<style scoped>

</style>