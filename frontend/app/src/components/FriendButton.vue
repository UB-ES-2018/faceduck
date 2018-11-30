<template>
    <div class="friend-button">
        <button class="btn btn-warning btn-sm" 
            v-if="!friends && !requested"
            v-on:click="requestFriendship">
            <i class="fas fa-user-plus"></i>
            Add {{name}} as a friend
        </button>

        <div v-if="!friends && requested && !requester">
            {{name}} wants to befriend you<br>
            <button class="btn btn-danger btn-sm"
                v-on:click="deleteFriendship">
                <i class="fas fa-user-times"></i>
                Reject
            </button>&nbsp; 
            <button class="btn btn-success btn-sm"
                v-on:click="acceptFriendship">
                <i class="fas fa-user-check"></i>
                Accept
            </button>
        </div>

        <div v-if="!friends && requested && requester">
            You asked {{name}} to be friends<br>
            <button class="btn btn-danger btn-sm"
                v-on:click="deleteFriendship">
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
            v-on:mouseleave="unfriendHover = false"
            v-on:click="deleteFriendship">
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

var host = window.location.hostname
var friendshipAPI = 'http://' + host + ':5000/user/friends'; //Backend ip

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
    mounted() {
        /* istanbul ignore next */
        this.checkFriendship()
        .then(data => {
            switch /* istanbul ignore next */ (data["state"]) {
                default:
                    this.friends = false;
                    this.requested = false;
                    this.requester = false;
                    break;
                case "pending":
                    this.friends = false;
                    this.requested = true;
                    this.requester = data["user_id"] === this.user.id;
                    break;
                case "friends":
                    this.friends = true;
                    break;
            }
        });
    },
    methods: {
        checkFriendship /* istanbul ignore next */ () {
            return fetch(friendshipAPI + "/" + this.user.id + "/" + this.userId, {
            headers: {
              "Authorization": "Bearer " + localStorage.getItem("access-token"),
            }
            }).then(res => res.json());
        },
        requestFriendship /* istanbul ignore next */ (event) {
            event.preventDefault();
            this.checkFriendship().then(data => {
                if (data["state"] === "pending" && data["user_id"] === this.userId && data["target_id"] === this.user.id) {
                    this.acceptFriendship(event);
                } else {
                    fetch(friendshipAPI, {
                        method: "POST",
                        headers: {
                          "Content-Type": "application/json",
                          "Authorization": "Bearer " + localStorage.getItem("access-token"),
                        },
                        body: JSON.stringify({
                            "target_id": this.userId
                        })
                    }).then(res => res.json())
                    .then(data => {
                        if (data["state"] === "pending") {
                            this.friends = false;
                            this.requested = true;
                            this.requester = true;
                        }
                    });
                }
            });
        },
        acceptFriendship /* istanbul ignore next */ (event) {
            event.preventDefault();
            fetch(friendshipAPI, {
                method: "PUT",
                headers: {
                  "Content-Type": "application/json",
                  "Authorization": "Bearer " + localStorage.getItem("access-token"),
                },
                body: JSON.stringify({
                    "target_id": this.userId,
                    "state": "friends"
                })
            }).then(res => res.json())
            .then(data => {
                if (data["state"] === "friends") {
                    this.friends = true;
                }
            });
        },
        deleteFriendship /* istanbul ignore next */ (event) {
            event.preventDefault();
            fetch(friendshipAPI, {
                method: "DELETE",
                headers: {
                  "Content-Type": "application/json",
                  "Authorization": "Bearer " + localStorage.getItem("access-token"),
                },
                body: JSON.stringify({
                    "target_id": this.userId
                })
            }).then((response) => {
                if (response.ok) {
                    this.friends = false;
                    this.requested = false;
                }
            });
        }
    }
}

</script>

<style lang="sass" scoped>
    
.friend-button
    text-align: center

.friends
    width: 200px

</style>