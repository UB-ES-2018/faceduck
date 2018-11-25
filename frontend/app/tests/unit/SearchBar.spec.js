import { mount } from "@vue/test-utils";
import SearchBar from "@/components/SearchBar.vue";

describe('SearchBar', () => {
    it('has a created hook', () => {
        expect(typeof SearchBar.created).toBe('function');
    });
})