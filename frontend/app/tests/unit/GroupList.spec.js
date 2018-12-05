import { mount } from "@vue/test-utils";
import GroupList from "@/components/GroupList.vue";

const factory = () => {
	return mount(GroupList);
};

describe("GroupList.vue", () => {
	it("shows a `no groups` message", () => {
		const wrapper = factory();

		expect(wrapper.find(".list-group-item").text()).toMatch(/no groups yet/i);
	});

	it("tries to fetch user groups", () => {
		const wrapper = factory();

		expect(fetch).toHaveBeenCalled();
	});
});