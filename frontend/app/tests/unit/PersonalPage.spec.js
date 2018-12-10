import { mount } from "@vue/test-utils";
import { shallowMount } from '@vue/test-utils';
import PersonalPage from "@/views/PersonalPage.vue";

const $route = {
    params: {
        path: "/profile"
    }
};
const $router = {
    push(e) {
        return true
    }
}
describe("PersonalPage.vue", () => {
    it("sets expects not image", () => {
        const wrapper = shallowMount(PersonalPage, {
            stubs: ['router-link', 'router-view'],
            mocks: {
                $route,
                $router
            }
        })
        wrapper.setData({ hasImage: false })
        expect(wrapper.find('.photo').isVisible()).toBeFalsy()
    })
    it("sets expects an image", () => {
        const wrapper = shallowMount(PersonalPage, {
            stubs: ['router-link', 'router-view'],
            mocks: {

                $route,
                $router
            }
        })
        wrapper.setData({ hasImage: true })
        expect(wrapper.find('.photo').isVisible()).toBeTruthy()
    })
})