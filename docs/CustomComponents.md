# Custom Vue.js components

## FriendButton

This component shows different buttons depending on the friendship status between the logged-in user (Alice) and another user (Bob). The component has to be used inside another person's profile, never ours.

- Props:
	- "name": String, required. The name of the person whose profile is shown (e.g., Bob)
	- "friends": Boolean
	- "requested": Boolean. Tells whether a friendship request is open
	- "requester": Boolean. In case a request is open, tells whether the logged-in user opened it.

Usages: there are basically 4 cases. The button is displayed on Bob's profile.

- Alice and Bob are not friends:

```html
<FriendButton name="Bob"/>
```

- Alice has asked Bob to be her friend:

```html
<FriendButton name="Bob" requested requester/>
```

- Bob has asked Alice to be his friend:

```html
<FriendButton name="Bob" requested/>
```

- Bob and Alice are friends:

```html
<FriendButton name="Bob" friends/>
```

Clearly, the name should be templated by the use of ```{{name}}```. Boolean props must be v-binded, see [https://vuejs.org/v2/guide/components-props.html#Passing-a-Boolean]
