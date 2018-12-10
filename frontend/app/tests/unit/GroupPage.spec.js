import { shallowMount } from '@vue/test-utils';
import GroupPage from "@/views/GroupPage.vue";

it('renders $route.params.idgroup', () => {
    const $route = {
        params: {
            idgroup: "453"
        }
    }
    const wrapper = shallowMount(GroupPage, {
        mocks: {
            $route
        }
    })
    expect(wrapper.vm.id).toBe($route.params.idgroup)
})

it('shows Add Button', () => {
    const $route = {
        params: {
            idgroup: "453"
        }
    }
    const wrapper = shallowMount(GroupPage, {
        stubs: ['router-link', 'router-view'],
        mocks: {
            $route
        }
    })
    wrapper.setData({ added: false })
    expect(wrapper.find('#Add').isVisible()).toBeTruthy()
})

it('shows Cancel Button', () => {
    const $route = {
        params: {
            idgroup: "453"
        }
    }
    const wrapper = shallowMount(GroupPage, {
        stubs: ['router-link', 'router-view'],
        mocks: {
            $route
        }
    })
    wrapper.setData({ added: true })
    expect(wrapper.find('#Cancel').isVisible()).toBeTruthy()
})