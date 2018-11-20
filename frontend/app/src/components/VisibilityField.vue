
<template>
    <!--<div>
        <b-dropdown class="VisF" v-model="visibility" @change="setValue()">
            <button class="button is-primary" type="button" slot="trigger">
                <template v-if="visibility==='friends'">
                    <b-icon icon="account-multiple"></b-icon>
                    <span>Friends</span>
        </template>

        <template v-if="visibility==='public'">
            <b-icon icon="earth">
            </b-icon>
            <span>Public</span>
        </template>
                    
        <template v-if="visibility==='logged'">
            <b-icon icon="account-multiple">
            </b-icon>
            <span>Only Logged</span>
        </template>

        <template v-if="visibility==='private'">
            <b-icon icon="account">
            </b-icon>
            <span>Just Me</span>
        </template>
            <b-icon icon="menu-down"></b-icon>
        </button>

        <b-dropdown-item :value="'public'" >
            <div class="media">
                <b-icon class="media-left" icon="earth"></b-icon>
                <div class="media-content">
                    <h3>Public</h3>
                    <small>Everyone can see</small>
                </div>
            </div>
        </b-dropdown-item>

        <b-dropdown-item :value="'friends'" >
            <div class="media">
                <b-icon class="media-left" icon="account-multiple"></b-icon>
                <div class="media-content">
                    <h3>Friends</h3>
                    <small>Only friends can see</small>
                </div>
            </div>
        </b-dropdown-item>
         <b-dropdown-item :value="'logged'" >
            <div class="media">
                <b-icon class="media-left" icon="account-multiple"></b-icon>
                <div class="media-content">
                    <h3>Only Logged</h3>
                    <small>Only logged users can see</small>
                </div>
            </div>
        </b-dropdown-item>
         <b-dropdown-item :value="'private'" >
            <div class="media">
                <b-icon class="media-left" icon="account"></b-icon>
                <div class="media-content">
                    <h3>Just Me</h3>
                    <small>Only for me to see</small>
                </div>
            </div>
        </b-dropdown-item>
    </b-dropdown>
    </div>-->
    <div id='VisField'>
        <select name="VisF" v-on:change="setValue()" v-model="visibility" required>
            <option value="" disabled selected>Select one…</option>
            <option value="public">Public</option>
            <option value="loggedin">Logged Only</option>
            <option value="friends">Friends Only</option>
            <option value="private">Only For Me</option>
        </select>
     </div>
</template>

<script scoped>
    //import 'buefy/dist/buefy.css';
export default {
    name: 'VisibilityField',
    data() {
        return { 
            visibility:'friends'
        }
    },
        /** props:{
           visible: String
            },
        
        }*/
    methods:{
        setValue(){
            this.$root.$emit("visibilityChange", {
                visibility: this.visibility
            });
        }
    }
        
}
</script>

<style lang="sass" scoped>
    //@import url("https://cdn.materialdesignicons.com/2.8.94/css/materialdesignicons.min.css")
    //@import '../../node_modules/buefy/dist/buefy.css'
    #VisField
         position: relative
         left: 255px
         bottom: 10px
         height: 25px
         font-size: 15px
    //.VisF
      //  position: relative
      //  left: 252px
      //  bottom: 5px
        
</style>

