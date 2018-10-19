import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

export default new Router({
    mode: 'history',
    routes: [
        {
            path: '/',
            name: 'homepage',
            component: () => 
                import ( /* webpackChunkName: "homepage" */ './views/HomePage.vue')
        },
        {
            path: '/about',
            name: 'about',
            component: () =>
                import ( /* webpackChunkName: "about" */ './views/AboutUs.vue')
        },
        {
            path: '/wall',
            name: 'wall',
            component: () =>
                import ( /* webpackChunkName: "wall" */ './views/PersonalWall.vue')
        },
        {
            path: '/search',
            name: 'search',
            component: () =>
                import ( /* webpackChunkName: "search" */ './views/SearchResults.vue')
        },
    ]
})