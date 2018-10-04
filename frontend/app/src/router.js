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
            // route level code-splitting
            // this generates a separate chunk (about.[hash].js) for this route
            // which is lazy-loaded when the route is visited.
            component: () =>
                import ( /* webpackChunkName: "about" */ './views/AboutUs.vue')
        },
        {
            path: '/wall',
            name: 'wall',
            component: () =>
                import ( /* webpackChunkName: "wall" */ './views/PersonalWall.vue')
        }
    ]
})