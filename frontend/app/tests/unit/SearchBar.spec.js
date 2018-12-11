import { mount } from '@vue/test-utils';
import SearchBar from "@/components/SearchBar.vue";

describe("SearchBar.vue", () => {
	it("does something", () => {
		const wrapper = mount(SearchBar);
	});

	it("renders a button and handles its clicking", () => {
		const wrapper = mount(SearchBar);

		expect(wrapper.find("button").exists()).toBeTruthy();
		wrapper.find("button").trigger("click");
	});
});