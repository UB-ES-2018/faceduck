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
            path: '/profile/:userid',
            name: 'profile_userid',
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
            path: '/login_logs',
            name: 'All account\'s logins',
            component: () =>
                import ( /* webpackChunkName: "search" */ './views/Login_logs.vue'),
            meta: { requiresAuth: true }
        },
        {
            path: '/post/:idpost',
            name: 'post_page',
            component: () =>
                import ( /* webpackChunkName: "post_page" */ './views/PostPage.vue'),
        },
        {
            path: '/group',
            name: 'create_group',
            component: () =>
                import ( /* webpackChunkName: "create_group" */ './views/CreateGroup.vue'),
        },
        {
            path: '/group/:idgroup',
            name: 'group',
            component: () =>
                import ( /* webpackChunkName: "group" */ './views/GroupPage.vue'),
        },
    ]
})