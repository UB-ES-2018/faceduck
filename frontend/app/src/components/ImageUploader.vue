<template>
<form class="uploader" enctype="multipart/form-data" ref="image_form">
  <button class="form-control far fa-image"></button>
  <input type="file"
         accept="image/*" 
         ref="image"
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
        /* istanbul ignore next */
        this.$root.$on("clearImageUpload", () => {
            this.$refs.image_form.reset();
        });
    },
    methods: {
        handleFileUpload /* istanbul ignore next */ () {
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

<style lang="sass" scoped>

.uploader
  position: relative;
  display: inline-block;
  overflow: hidden;

.uploader > button
  position: relative;
  display: inline-block;
  width: auto
  overflow: hidden;
  float: left;
  clear: left;

.uploader input[type=file]
  display: block;
  position: absolute;
  left: 0;
  top: 0;
  height: 100%
  width: 100%
  opacity: 0;
  z-index: 2;
  cursor: pointer;

</style>

