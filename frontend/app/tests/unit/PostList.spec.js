import { mount } from "@vue/test-utils";
import PostList from "@/components/PostList.vue";

const factory = (values = {}) => {
	return mount(PostList, {
		propsData: { ...values }
	});
};

describe("PostList.vue", () => {
	it("shows a ducklist", () => {
		const wrapper = factory();
		expect(wrapper.findAll (".post-list").isEmpty()).toBeFalsy();
		expect(wrapper.findAll (".post-list>div")).toHaveLength(1);
	});

	it("covers the newsfeed branch", () => {
		const wrapper = factory({
			newsfeed: true
		});
		expect(wrapper.findAll (".post-list").isEmpty()).toBeFalsy();
		expect(wrapper.findAll (".post-list>div")).toHaveLength(1);
	});

	it("covers the user-id branch", () => {
		const wrapper = factory({
			authorId: "25ce2570-729f-47de-8d1d-b29ed06dd808"
		});
		expect(wrapper.findAll (".post-list").isEmpty()).toBeFalsy();
		expect(wrapper.findAll (".post-list>div")).toHaveLength(1);
	});

	it("handles `addPost` event", () => {
		const wrapper = factory();

		wrapper.vm.$root.$emit("addPost", {
			post: {
				"author": {
					username: "This is a test"
				},
				"text": "Testing yay!"
			}
		});

		expect(wrapper.findAll (".post-list").isEmpty()).toBeFalsy();
		expect(wrapper.findAll (".post-list>div")).toHaveLength(2);
	});

	it("handles `postEvent` event", () => {
		const wrapper = factory({
			query: "the old query"
		});

		wrapper.vm.$root.$emit("postEvent", {
			query: "the new query"
		});

		expect(wrapper.findAll (".post-list").isEmpty()).toBeFalsy();
	});
});