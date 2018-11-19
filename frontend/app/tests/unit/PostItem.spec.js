import { mount } from "@vue/test-utils";
import PostItem from "@/components/PostItem.vue";

const factory = (values = {
	post: {
	    "author": {
	      "id": "90ada2f2-1b5d-4319-9c55-77ea566015e4",
	      "username": "john"
	    },
	    "id": "82c45212-b2cc-4699-b7cc-5ba55e7f262e", 
	    "text": "unit testing"
	}
}) => {
	return mount(PostItem, {
		propsData: { ...values }
	});
};

describe("PostItem.vue", () => {
	it("renders the post text", () => {
		const wrapper = factory();

		expect(wrapper.find(".post-text").text()).toEqual("unit testing");
	});

	it("renders the post author", () => {
		const wrapper = factory();

		expect(wrapper.find(".post-username a").exists()).toBeTruthy();
		expect(wrapper.find(".post-username a").text()).toEqual("john");
	});

	it("has a link to the post author profile", () => {
		const wrapper = factory();

		expect(wrapper.find(".post-username a").attributes("href")).toEqual("/profile/john");
	})
});