# Custom Vue.js components

## FriendButton

This component shows different buttons depending on the friendship status between the logged-in user (Alice) and another user (Bob). The component has to be used inside another person's profile, never ours.

*DANGER: including this component and setting the userId prop to the logged-in user's id is not advised and will have an UNDEFINED BEHAVIOUR*

- Props:
	- "userId": String, required. The id of the person whose profile is shown, for API request purposes
	- "name": String, required. The name of the person whose profile is shown (e.g., Bob)

Usage: The button is displayed on Bob's profile.

```html
<FriendButton name="Bob" userId="bobs-id"/>
```

Clearly, the userId and name should be templated by the use of ```user.id``` and ```user.name```. Boolean props must be v-binded, see [https://vuejs.org/v2/guide/components-props.html#Passing-a-Boolean]
