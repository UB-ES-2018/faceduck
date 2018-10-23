import Vue from 'vue';
import App from './App.vue';
import router from './router';

Vue.config.productionTip = false;

router.beforeEach((to, from, next) => {
    var loggedIn = localStorage.getItem("access-token");
    if (to.matched.some(record => record.meta.requiresAuth)) {
        // this route requires auth, check if logged in
        // if not, redirect to login page.
        if (!loggedIn) {
            localStorage.removeItem("user");
            next({
                path: "/",
                query: { redirect: to.fullPath }
            })
        } else {
            next()
        }
    } else {
        next() // make sure to always call next()!
    }
});

new Vue({
    router,
    render: h => h(App)
}).$mount('#app');