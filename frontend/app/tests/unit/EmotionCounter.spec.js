import { mount } from "@vue/test-utils";
import EmotionCounter from "@/components/EmotionCounter.vue";

const factory = (values = {
	post: {}
}) => {
	return mount(EmotionCounter, {
		propsData: { ...values }
	});
};

describe("EmotionCounter.vue", () => {
	it("shows nothing when post has no reactions", () => {
		const wrapper = factory();
		
		expect(wrapper.findAll("#emotions li")).toEqual({});
	});

	it("displays emotion counts properly", () => {
		const wrapper = factory({
			post: {
				"reactions-count": [
					{
						reaction: "like",
						count: 2
					},
					{
						reaction: "love",
						count: 3
					},
					{
						reaction: "angry face",
						count: 5
					},
					{
						reaction: "sad crying face",
						count: 11
					},
					{
						reaction: "laughing face",
						count: 17
					},
					{
						reaction: "wrong emotion",
						count: 1
					}
				]
			}
		});

		expect(wrapper.findAll(".emotions li")).toHaveLength(5);
	})
});