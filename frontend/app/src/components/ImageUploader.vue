<template>
    <form enctype="multipart/form-data">
        <input type="file" 
               ref="image" 
               class=""
               accept="image/*" 
               v-on:change="handleFileUpload()">
    </form>
</template>

<script>
var host = window.location.hostname;
var apiUploadUrl = '//' + host + ':5000/media';

export default {
    name: "ImageUploader",
    props: ["uploader-id"],
    data() {
        return {}
    },
    created() {
        this.$root.$on("clearImageUpload", () => {
            this.$refs.image.files = [];
        });
    },
    methods: {
        handleFileUpload() {
            var formData = new FormData();
            formData.append('file', this.$refs.image.files[0]);
            
            fetch(apiUploadUrl, {
                method: "POST",
                headers: {
                    "Authorization": "Bearer " + localStorage.getItem("access-token"),
                    // If you add this, upload won't work
                    // SRC: https://stanko.github.io/uploading-files-using-fetch-multipart-form-data/
                    // "Content-Type": "multipart/form-data"
                },
                body: formData
            }).catch((r) => console.log(r))
            .then((response) => {
                if (response.ok) {
                    response.json().then((json) => {
                        this.$root.$emit("imageUpload", {
                            emitter: this.uploaderId,
                            url: json["media-url"]
                        });
                    });
                } else {
                    // try again? cry?
                }
            });
        }
    }
}
</script>