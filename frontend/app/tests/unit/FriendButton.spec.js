import { mount } from '@vue/test-utils';
import FriendButton from "@/components/FriendButton.vue";

describe("FriendButton.vue", () => {
	it("does something", () => {
		const wrapper = mount(FriendButton);
	});
	it("renders a request button", () => {
		const wrapper = mount(FriendButton);

		expect(wrapper.find("button").text()).toMatch(/Add [^\s]* as a friend/);
	});
});