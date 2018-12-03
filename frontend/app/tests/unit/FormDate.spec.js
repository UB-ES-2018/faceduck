import { shallowMount, mount } from "@vue/test-utils";
import FormDate from "@/components/FormDate.vue";


it("sets initialy day", () => {
    const wrapper = shallowMount(FormDate, {
        props: {
            value: 696988800
        }
    })
    wrapper.setData({ day: 2 })
    wrapper.vm.updateDay()
    expect(wrapper.vm.day).toBe(2)
})
it("sets initialy month", () => {
    const wrapper = shallowMount(FormDate, {
        props: {
            value: 696988800
        }
    })
    wrapper.setData({ month: 2 })
    wrapper.vm.updateMonth()
    expect(wrapper.vm.month).toBe(2)
})
it("sets initialy year", () => {
    const wrapper = shallowMount(FormDate, {
        props: {
            value: 696988800
        }
    })
    wrapper.setData({ year: 1992 })
    wrapper.vm.updateValue()
    expect(wrapper.vm.year).toBe(1992)
})
it("test overflow day", () => {
    const wrapper = shallowMount(FormDate, {
        props: {
            value: 696988800
        }
    })
    wrapper.setData({ day: '-1' })
    wrapper.vm.updateDay()
    wrapper.vm.updateValue()
    expect(wrapper.vm.day).toBe(1)
})
it("test overflow month", () => {
    const wrapper = shallowMount(FormDate, {
        props: {
            value: 696988800
        }
    })
    wrapper.setData({ month: '-1' })
    wrapper.vm.updateMonth()
    wrapper.vm.updateValue()
    expect(wrapper.vm.month).toBe(1)
})