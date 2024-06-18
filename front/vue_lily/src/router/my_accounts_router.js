import MyAccountInfo from '@/components/Accounts/MyAccountInfo.vue';
import MyDetailOrder from '@/components/Accounts/MyDetailOrder.vue';
import MyOrders from '@/components/Accounts/MyOrders.vue';
import MyShipingAddress from '@/components/Accounts/MyShipingAddress.vue';
import LoginView from '@/views/Accounts/LoginView.vue';
import SingUpView from '@/views/Accounts/SingUpView.vue';
import BaseAccountView from '@/views/Accounts/BaseAccountView.vue';
import { DOMAIN_NAME } from '@/utils/api_links';
import EditMyShippingAddress from '@/components/Accounts/EditMyShippingAddress.vue';
import { pushScopeId } from 'vue';

export default [
    {
        path: '/login',
        name: 'login',
        component: LoginView,
        meta: {
            title: 'Login'
        },
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
            return {name: 'account_details', reload: true }
        },
        children : [
            {
                path: 'details',
                name: 'account_details',
                component: MyAccountInfo,
                mata: {
                    title: 'Account Details',
                    requiresAuth: true
                },
                
                
            },
            {
                path: 'order-view/:pk',
                name: 'account_order_view',
                component: MyDetailOrder,
                meta: {
                    requiresAuth: true
                },
                
                
            },
            {
                path: 'all-orders',
                name: 'account_all_orders',
                component:MyOrders,
                meta: {
                    requiresAuth: true
                },
                
            },
            {
                path: 'shiping-address',
                name: 'acccount_address',
                component: MyShipingAddress,
                meta: {
                    requiresAuth: true
                },
                
            },
            {
                path: 'edit-address',
                name: 'edit_address',
                component: EditMyShippingAddress,
                meta: {
                    requiresAuth: true
                },
                
            },
            {
                path: 'add-new-address',
                name: 'add_new_address',
                component: EditMyShippingAddress,
                meta: {
                    requiresAuth: true
                },
                
            }
        ],
        meta: {
            title: 'My Acccount',
            requiresAuth: true
        },
        
    }

]


