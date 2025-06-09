import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import {useAuthStore} from "@/stores/AuthStore";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
    {
      path: '/about',
      name: 'about',
      component: () => import('../views/AboutView.vue'),
    },
        {
            path: '/auth',
            name: 'auth',
            children: [
                {
                    path: 'login',
                    name: 'login',
                    component: () => import('../views/auth/login.vue')
                },
            ]
        },
  ],
})

router.beforeEach(async (to) => {
    // redirect to login page if not logged in and trying to access a restricted page
    const publicPages = ['/auth/login'];
    const authRequired = !publicPages.includes(to.path);
    const auth = useAuthStore();
    if (authRequired && !(await auth.get_valid_token())) {
        auth.returnUrl = to.fullPath;
        return '/auth/login';
    }
});
export default router
