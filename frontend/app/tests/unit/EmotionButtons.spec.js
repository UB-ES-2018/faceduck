import { mount } from "@vue/test-utils";
import EmotionButtons from "@/components/EmotionButtons.vue";

const factory = (values = {
	post: {}
}) => {
	return mount(EmotionButtons, {
		propsData: { ...values }
	});
};

describe("EmotionButtons.vue", () => {
	it("hides emotion buttons", () => {
		const wrapper = factory();
		
		expect(wrapper.find("#emotions").isVisible()).toBeFalsy();
	});

	it("shows emotion buttons on hover", () => {
		const wrapper = factory();

		wrapper.find(".icons").trigger("mouseover");
		expect(wrapper.find("#emotions").isVisible()).toBeTruthy();
	});

	it("adds highlight to selected emotion", () => {
		const wrapper = factory({
			post: {
				"user-reaction": [
					{
						"user-id": "483cf810-9cb2-4aea-99d1-aacf054de9d7",
						"reaction": "like"
					},
					{
						"user-id": global.user.id,
						"reaction": "love"
					},
					{
						"user-id": "7a7ac104-ae01-4ccf-b7da-bdef4ad65339",
						"reaction": "angry face"
					}
				]
			}
		});

		expect(wrapper.find("li[data-selected] img").attributes("src"))
			.toContain("love");
	});

	it("calls the api when a button is clicked", () => {
		const wrapper = factory();

		wrapper.findAll(".emotions img").filter((img) => {
			img.trigger("click");
			expect(global.fetch).toHaveBeenCalled();
		});
	})
});