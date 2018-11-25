import { mount } from "@vue/test-utils";
import SearchUsers from "@/components/SearchUsers.vue";

describe('SearchUsers', () => {
    it('has a created hook', () => {
        expect(typeof SearchUsers.created).toBe('function');
    });
})