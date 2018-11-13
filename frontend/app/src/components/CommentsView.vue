<template>
    <div class="comments">
        <div class="c-cnt" v-on:click="showComments=!showComments">{{count}} comment(s)
            <span v-if="!showComments">Show</span>
            <span v-else>Hide</span>
        </div>
        
        
        <div class="c-hidden" v-if="showComments">
            <div class="c-list" v-for="comment in comments" :key="comment.comment_id">
                <div class="c-info">
                    <div class="c-main">{{comment.username}}: {{comment.text}}</div><!--WARNING - get real author-->
                </div>
            </div>
            
        <input type="text" placeholder="Your comment…" v-model="commentText" v-on:keyup.enter="postComment(post_id)">
        <button class="c-post" v-on:click="postComment(post_id)">Post</button>
        </div>
        
    </div>



</template>


<script>
var host = window.location.hostname
var userAPI = 'http://' + host + ':5000/user/'; //Backend  user search by id
var commentAPI = 'http://' + host + ':5000/post/'; //Backend  user search by id

export default {
	name: "CommentsView",
	props: {
        comments: [],
        raw_comments: [],
        count: Number,
        post_id: String,
        showComments: false,
        //user: JSON.parse(localStorage.getItem("user"))
	},
	data() {
		return {
			authors: [],
            commentText: ""
		}
	},
	mounted() {
		if(this.count!=0){
            this.getComments(this.post_id);
        }
    },
	methods: {
		getAuthor: function(author_id, i) {
			fetch(userAPI + author_id, {
            method: "GET",
			headers: {
                "Content-Type": "application/json",
                "Authorization": "Bearer " + localStorage.getItem("access-token"),
            }
            }).then(res => res.json()).then(data => {
                this.raw_comments[i]['username'] = data.username;
                if (!this.raw_comments[i+1]){
                    this.comments=this.raw_comments;
                }
                //vm.$forceUpdate();
                });
                
		},
		postComment: function(post_id){
            fetch(commentAPI + post_id + "/" + "comments" , {
            method: "POST",
            headers: {
              "Content-Type": "application/json",
              "Authorization": "Bearer " + localStorage.getItem("access-token"),
            },
            body: JSON.stringify({text: this.commentText})
          });
            if(this.count !=0){
                this.comments[this.count]={'username':JSON.parse(localStorage.getItem("user"))['username'],'text': this.commentText };
            }else{
                var tmp=[];
                tmp.push({'username':JSON.parse(localStorage.getItem("user"))['username'],'text': this.commentText });
                this.comments=tmp;
            }
            this.count++;
            this.raw_comments=this.comments;
            this.comments=[];
            this.comments=this.raw_comments;
            this.commentText="";

        },
		getComments: function(post_id){
            fetch(commentAPI + post_id + "/" + "comments" , {
            method: "GET",
            headers: {
                 "Content-Type": "application/json",
              "Authorization": "Bearer " + localStorage.getItem("access-token"),
            }
          }).then(res => res.json())
          .then(data => {
            this.raw_comments = data;
            var i = 0;
            this.raw_comments.forEach(comment => {
                this.getAuthor(comment.user_id, i);
                i++;
            });
          });
        },
	}
}

</script>


<style lang="sass" scoped>
.comments
  color: black

.comments button
  background-color: #ffb511
  border: none
  color: white
  font-size: 12px
  font-weight: bold
  box-sizing: content-box
  padding: 10px
  border-radius: 10px
  width: 60px
  position: relative
  left: 1% 
  cursor: pointer

</style>