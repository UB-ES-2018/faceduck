import { mount } from '@vue/test-utils';
import PostList from "@/components/PostList.vue";

describe("PostList.vue", () => {
	it("does something", () => {
		const wrapper = mount(PostList);
	});
	it("allows the newsfeed option", () => {
		const wrapper = mount(PostList, {
			propsData: {
				newsfeed: true
			}
		});
	});
	it("allows an authorId option", () => {
		const wrapper = mount(PostList, {
			propsData: {
				authorId: "90ada2f2-1b5d-4319-9c55-77ea566015e4"
			}
		});
	});
});