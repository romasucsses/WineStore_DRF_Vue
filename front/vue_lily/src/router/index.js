import { createRouter, createWebHistory } from 'vue-router';
import HomeView from '@/views/HomeView.vue';
import AboutUsView from '@/views/AboutUsView.vue';
import ShopView from '@/views/ShopView.vue';
import ContactUsView from '@/views/ContactUsView.vue';
import WineView from '@/views/WineView.vue';
import SparklingView from '@/views/SparklingView.vue';
import FindNearMeView from '@/views/FindNearMeView.vue';
import my_accounts_router from './my_accounts_router.js';
import CartView from '@/views/CartView.vue';
import ProductDetailView from '@/views/ProductDetailView.vue';
import SuccessfulOrder from '@/views/SuccessfulOrder.vue';
import ShippingAddressCartView from '@/views/ShippingAddressCartView.vue';


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    ...my_accounts_router,
    {
      path: '/',
      name: 'home',
      component: HomeView,
      meta: {
        title: 'Home Page'
      }
    },
    {
      path: '/about-us',
      name: 'about_us',
      component: AboutUsView,
      meta: {
        title: 'About Us'
      }
    },
    {
      path: '/shop',
      name: 'shop',
      component: ShopView,
      meta: {
        title: 'Shop'
      }
    },
    {
      path: '/contact-us',
      name: 'contact_us',
      component: ContactUsView,
      meta: {
        title: 'Contact US'
      }
    },
    {
      path: '/shop/wine',
      name: 'wine',
      component: WineView,
      meta: {
        title: 'Our Wine'
      }
    },
    {
      path: '/shop/sparkling',
      name: 'sparkling',
      component: SparklingView,
      meta: {
        title: 'Our Sparkling'
      }
    },
    {
      path: '/shop/product-detail/:slug',
      name: 'product_detail',
      component: ProductDetailView,
      meta: {
        title: 'Product'
      }
    },
    {
      path: '/find-near-me',
      name: 'find_near_me',
      component: FindNearMeView,
      meta: {
        title: 'Find Near Me'
      }
    },
    {
      path: '/cart',
      name: 'cart',
      component: CartView,
      meta: {
        title: 'Cart'
      }
    },
    {
      path: '/successfull-order',
      name: 'successfull-order',
      component: SuccessfulOrder,
      meta: {
        title: 'Successful Order'
      }
    },
    {
      path: '/client-shipping-address',
      name: 'client_shipping_address',
      component: ShippingAddressCartView,
      meta: {
        title: 'Your Address'
      }
    },
    
  ]
});

export default router;
