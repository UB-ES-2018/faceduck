import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

export default new Router({
    mode: 'history',
    routes: [{
            path: '/',
            name: 'homepage',
            component: () =>
                import ( /* webpackChunkName: "homepage" */ './views/HomePage.vue')
        },
        {
            path: '/about',
            name: 'about',
            component: () =>
                import ( /* webpackChunkName: "about" */ './views/AboutUs.vue'),
            meta: { requiresAuth: true }
        },
        {
            path: '/wall',
            name: 'wall',
            component: () =>
                import ( /* webpackChunkName: "wall" */ './views/PersonalWall.vue'),
            meta: { requiresAuth: true }
        },
        {
            path: '/profile',
            name: 'profile',
            component: () =>
                import ( /* webpackCunkName: "profile" */ './views/PersonalPage.vue'),
            meta: { requiresAuth: true }
        },
        {
            path: '/profile/:username',
            name: 'profile_username',
            component: () =>
                import ( /* webpackCunkName: "profile" */ './views/PersonalPage.vue'),
            meta: { requiresAuth: true }
        },
        {
            path: '/search',
            name: 'search',
            component: () =>
                import ( /* webpackChunkName: "search" */ './views/SearchResults.vue'),
            meta: { requiresAuth: true }

        },
        {
            path: '/post/:idpost',
            name: 'post_page',
            component: () =>
                import ( /* webpackChunkName: "post_page" */ './views/PostPage.vue'),
        },
    ]
})