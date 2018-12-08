import { mount } from "@vue/test-utils";
import GroupList from "@/components/GroupList.vue";

const factory = (values = {}) => {
	return mount(GroupList, {
		propsData: { ... values }
	});
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

	it("tries to fetch user groups when user_id is present", () => {
		const wrapper = factory({
			userId: "a188bdaf-09b1-4937-ad8e-340d1543def8"
		});

		expect(fetch).toHaveBeenCalled();
	});

	it("renders the `groups` prop", () => {
		const wrapper = factory({
			groups: [
				{
					id: "a1883daf-02b1-4937-ad8d-340d1543dee8",
					name: "Group One"
				},
				{
					id: "fef3493f-5281-47c2-a10d-ec2396020e6e",
					name: "Group Two"
				}
			]
		});

		expect(wrapper.findAll(".list-group-item").length).toEqual(2);
		wrapper.findAll(".list-group-item").filter(item => {
			expect(item.text()).toMatch(/Group (One|Two)/);
		});
	})
});