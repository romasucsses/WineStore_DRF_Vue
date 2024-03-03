import MyAccountInfo from '../components/Accounts/MyAccountInfo.vue';
import MyDetailOrder from '../components/Accounts/MyDetailOrder.vue';
import MyOrders from '../components/Accounts/MyOrders.vue';
import MyShipingAddress from '../components/Accounts/MyShipingAddress.vue';
import LoginView from '../views/Accounts/LoginView.vue';
import SingUpView from '../views/Accounts/SingUpView.vue';
import BaseAccountView from '../views/Accounts/BaseAccountView.vue';
import { DOMAIN_NAME } from '@/api_links';

export default [
    {
        path: '/login',
        name: 'login',
        component: LoginView,
        meta: {
            title: 'Login'
        },
        beforEnter: beforEntaring
    },
    {
        path: '/sing-up',
        name: 'sing_up',
        component: SingUpView,
        meta: {
            title: 'Sing Up'
        }
    },
    
    {
        path: '/my-account/',
        name: 'my_account',
        component: BaseAccountView,
        redirect: to => {
            return {name: 'account_details'}
        },
        children : [
            {
                path: 'details',
                name: 'account_details',
                component: MyAccountInfo,
                mata: {
                    title: 'Account Details'
                }
            },
            {
                path: 'order-view',
                name: 'account_order_view',
                component: MyDetailOrder,
                
            },
            {
                path: 'all-orders',
                name: 'account_all_orders',
                component:MyOrders,
            },
            {
                path: 'shiping-address',
                name: 'acccount_address',
                component: MyShipingAddress,
            },
        ],
        meta: {
            title: 'My Acccount',
            requiresAuth: true
        },
        beforEnter: beforEntaring,
    }
]

function beforEntaring(to, next){
    const isAuthenticated  = localStorage.getItem('isAuthenticated');

    if (to.meta.requiresAuth) {
        if (!isAuthenticated) {
            next('/login'); 
        }else if (isAuthenticated === true){
            next({name: 'account_details'});
        }

    // Continue to the requested route
    
    } else{
        if(isAuthenticated === true){
            window.location.href = DOMAIN_NAME + 'users/my-account/details/';
        }
    }
};
