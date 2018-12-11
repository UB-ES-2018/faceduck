import { shallowMount } from '@vue/test-utils';
import CreateGroup from "@/views/CreateGroup.vue";

describe("CreateGroup", () => {
	it('Visibility Create Group Components', () => {
	    const wrapper = shallowMount(CreateGroup, {
	        stubs: ['router-link', 'router-view'],
	        
	    })
	    expect(wrapper.find('#CreateGroup').isVisible()).toBeTruthy()
	});
});