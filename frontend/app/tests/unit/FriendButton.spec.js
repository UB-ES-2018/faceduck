import { mount } from "@vue/test-utils";
import FriendButton from "@/components/FriendButton.vue";

const factory = (values = {
	name: "John"
}) => {
	return mount(FriendButton, {
		propsData: { ...values }
	});
};

describe("FriendButton.vue", () => {
	it("renders a `request friendship` button", () => {
		const wrapper = factory();

		expect(wrapper.find("button").text()).toMatch(/Add John as a friend/);
	});
});