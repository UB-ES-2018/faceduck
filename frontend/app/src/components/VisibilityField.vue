
<template>
    <div>
    <b-dropdown class="VisF" v-model="isPublic">
        <button class="button is-primary" type="button" slot="trigger">
            <template v-if="isPublic==0">
                <b-icon icon="account-multiple"></b-icon>
                <span>Friends</span>
            </template>
            <template v-if="isPublic==1">
                <b-icon icon="earth"></b-icon>
                <span>Public</span>
            </template>
            
            <template v-if="isPublic==2">
                <b-icon icon="account-multiple"></b-icon>
                <span>Only Logged</span>
            </template>
            <template v-if="isPublic==3">
                <b-icon icon="account"></b-icon>
                <span>Just Me</span>
            </template>
            <b-icon icon="menu-down"></b-icon>
        </button>

        <b-dropdown-item :value="1">
            <div class="media">
                <b-icon class="media-left" icon="earth"></b-icon>
                <div class="media-content">
                    <h3>Public</h3>
                    <small>Everyone can see</small>
                </div>
            </div>
        </b-dropdown-item>

        <b-dropdown-item :value="0">
            <div class="media">
                <b-icon class="media-left" icon="account-multiple"></b-icon>
                <div class="media-content">
                    <h3>Friends</h3>
                    <small>Only friends can see</small>
                </div>
            </div>
        </b-dropdown-item>
         <b-dropdown-item :value="2">
            <div class="media">
                <b-icon class="media-left" icon="account-multiple"></b-icon>
                <div class="media-content">
                    <h3>Only Logged</h3>
                    <small>Only logged users can see</small>
                </div>
            </div>
        </b-dropdown-item>
         <b-dropdown-item :value="3">
            <div class="media">
                <b-icon class="media-left" icon="account"></b-icon>
                <div class="media-content">
                    <h3>Just Me</h3>
                    <small>Only for me to see</small>
                </div>
            </div>
        </b-dropdown-item>
    </b-dropdown>
    </div>
</template>

<script>
    export default {
        name: 'VisField',
        data() {
            return {
                visibility: 'Friends',
                isPublic: 0,
            }
        }
    }
</script>
<style lang="sass" scoped>
    @import url("https://cdn.materialdesignicons.com/2.8.94/css/materialdesignicons.min.css")
    .VisF
        position: relative
        left: 252px
        bottom: 5px
</style>

