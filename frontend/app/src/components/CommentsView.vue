<template>
    <div class="comments">
        <div class="c-cnt">{{count}} comment(s)</div>
        <div class="c-list" v-for="comment in comments" :key="comment.comment_id">
            <div class="c-info">
                <div class="c-main">{{comment.username}}: {{comment.text}}</div><!--WARNING - get real author-->
            </div>
        </div>
        
          <input type="c-text" placeholder="Your comment…" v-model="commentText">
          <button class="c-post" v-on:click="postComment(post_id)">Post</button>
        
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