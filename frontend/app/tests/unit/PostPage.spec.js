import { mount } from "@vue/test-utils";
import { shallowMount } from '@vue/test-utils';
import PostPage from "@/views/PostPage.vue";

const factory = (values = {}) => {
    return shallowMount(PostPage, {
        data: {...values }
    })
};
it('renders $route.params.idpost', () => {
    const $route = {
        params: {
            idpost: "453"
        }
    }
    const wrapper = shallowMount(PostPage, {
        mocks: {
            $route
        }
    })
    expect(wrapper.vm.setIdpost()).toBe($route.params.idpost)
        //expect(PostPage.idpost).toBe($route.params.idpost)
})