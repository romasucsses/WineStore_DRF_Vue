<script setup>
    import { onMounted, ref, watch } from 'vue';
    import { DOMAIN_FOR_IMG, DOMAIN_NAME } from '@/utils/api_links';
    import { DeleteItemFromCart, SaveLocalData } from '@/utils/cart_logic/cart.js';
    import axios from 'axios';
    import { RouterLink, useRouter } from 'vue-router';

    const final_cart = ref([]);
    let total = 0;
    const router = useRouter();

    function calculateTotal(){
        console.log(final_cart.value);
        console.log('cart is', final_cart.value);
        total = 0;
        if (final_cart.value !== null){
            final_cart.value.forEach(element =>{
                total += element.price * element.quantity;
            })
            console.log(total);
        }
        

    };
    onMounted(() => {
        final_cart.value = JSON.parse(localStorage.getItem('cart_storage')) || [];
        
        calculateTotal();
        
    })

    watch(final_cart, () => {
            calculateTotal();
            SaveLocalData(final_cart.value);
        }, 
        {deep:true}, { immediate: true }
    );

    function CreateOrder(){
        const AccessToken = ref(localStorage.getItem('AccessToken'))
        SaveLocalData(final_cart.value);
        final_cart.value = JSON.parse(localStorage.getItem('cart_storage'));
        const orderData = {
            
            'cart_data': final_cart.value,
            'is_paid': false,
            'payment_method': 'card',
            'total_sum' : total
            
        }
        const finalEndPoint = DOMAIN_NAME + 'orders/create-new-order/';
        axios.post(finalEndPoint, orderData, {
            headers: { 
                Authorization: 'Bearer ' + AccessToken.value
                
            }
        })
        .then((response) => {
            console.log(response);
        })
        .catch((error) => {
            console.log(error);
        });
        const stripe_endpoint = DOMAIN_NAME + 'stripe-api/create-order/';
        const stripeData = {
            'amount' : total
        }
        axios.post(stripe_endpoint, stripeData)
        .then((response) => {
            console.log(response);
            
            router.push({name: 'successfull-order'});
        })

        
    }

    function redirectToLogin(){
        const isAuthenticated = ref(localStorage.getItem('isAuthenticated')=== 'true');
        if (!isAuthenticated.value){
            router.push({ name: 'login'});
        }else{
            CreateOrder();
        }
        
    }
    
</script>

<template>
    <div>
        <div class="main-block" v-if="final_cart.value && final_cart.value.length > 0">
            <h1 class="cart-header">Cart</h1>
            <table class="products-table">
                <tr>
                    <th colspan="2">
                        <RouterLink :to="{name: 'shop'}"><a><button>Add Others Products</button></a></RouterLink>
                    </th>
                    <th>Product</th>
                    <th>Price</th>
                    <th>Quantity</th>
                    <th>Subtotal</th>
                </tr>
                <tr v-for="eachitem in final_cart" :key="eachitem.id">
                    <td class="cancel-prod">
                        <div>
                            <button class="delete-item" @click="DeleteItemFromCart(eachitem.id)">
                                <img src="../../public/shop/images/site-img/cancel-circle.svg">
                            </button>
                        </div>
                    </td>
                    <td class="image-prod"><img :src="DOMAIN_FOR_IMG + eachitem.image"></td>
                    <td>{{ eachitem.name }} </td>
                    <td>$ {{ eachitem.price }}.00</td>
                    <td><input type="number" v-model="eachitem.quantity"></td>
                    <td>$ {{ eachitem.price * eachitem.quantity }}.00</td>
                </tr>
            </table>
            <div class="total">
                <form class="coupons-add">
                    <div class="coupons">
                        <input type="text" placeholder="Your coupon..">
                        <button>Apply Coupon</button>
                    </div>
                </form>
                <table class="checkout-table">
                    <tr>
                        <th colspan="2">Cart Totals</th>
                    </tr>
                    <tr>
                        <td>Total</td>
                        <td class="total-sum">${{ total }}.00</td>
                    </tr>
                    <tr>
                        <td colspan="1" class="guest"><button @click="CreateOrder()">Checkout As Guest</button></td>
                        <td colspan="1" class="user"><button @click="redirectToLogin()">Continue with Login</button>
                        </td>
                    </tr>


                </table>
            </div>
        </div>
        <div v-else class="to-center">
            <h1 class="cart-header">Your Cart is Empty Now</h1>
            <RouterLink :to="{name: 'shop'}">
                <a class="return-to-shop">
                    <button>Return to Shop</button>
                </a>
            </RouterLink>
        </div>

    </div>

</template>

<style scoped>
    .main-block{
        margin: 15px;
        margin-bottom: 90px;
        
    }

    .guest button {
        width: 300px;
        height: 60px;
        background-color: #007bff;
        font-size: 20px;
        color:#FFFFFF;
        border: 0;
        border-radius: 10px;
        margin-bottom: 3%;
    }

    .guest button:hover{
        background-color: #0084d6;
        width: 308px;
        height: 63px;
    }


    .user button{
        width: 300px;
        height: 60px;
        background-color: #0084d6;
        font-size: 20px;
        color:#FFFFFF;
        border: 0;
        border-radius: 10px;
    }

    .user button:hover{
        background-color: #007bff;
        width: 308px;
        height: 63px;
    }

    .cart-header{
        font-weight: 700;
        color: #54595f;
        font-size: 60px;
        text-align: center;

    }

    .products-table {
        margin: 0 auto; 
        margin-top: 90px;
        font-family: Arial, sans-serif; 

        border: 1px solid #444; 
        border-collapse: collapse; 
        width: 80%; 
    }

    .products-table tr{
        border: 1.5px solid  #ccc;
    }

    .products-table th {
        background-color: #FFFFFF;
        padding: 20px; 
        text-align: center; 
        font-weight: 600;
        font-family: 'Lato', sans-serif;
    }

    .products-table th button{
        width: 150px;
        height: 45px;
        background-color: #007bff;
        color: #FFFFFF;
        border: 0;
        font-size: 17px;
        border-radius: 5px;
        font-weight: 600;
    }

    .products-table td{
        background-color: #f5f7f9;
        padding: 15px; 
        text-align: center;
        font-size: 17px;
    }


    .products-table a {
        text-decoration: none; 
        color: #007bff; 
    }

    .image-prod img {
        max-width: 70px;
        max-height: 70px;
    }

    .cancel-prod img{
        max-width: 20px;
        max-height: 20px;
    }

    .cancel-prod img:hover{
        max-width: 28px;
        max-height: 28px;
    }


    input[type="number"] {
        width: 70px;
        text-align: center;
        padding: 10px;

    }

    .total{
        display: flex;
        justify-content: center;
    }

    .coupons-add{
        margin: 0 auto;
        margin-top: 60px;
        
        max-width: 40%;
        padding: 25px;
        border-radius: 10px;
    }

    .coupons input{
        width: 190px;
        height: 35px;
    }



    .coupons-add button{
        width: 170px;
        height: 45px;
        background-color: #007bff;
        color: #FFFFFF;
        border: 0;
        font-size: 17px;
        margin-top: 30px;
        border-radius: 5px;
    }


    .checkout-table {
        margin: 0 auto; 
        margin-top: 90px;
        font-family: Arial, sans-serif; 

        border: 1px solid #444; 
        border-collapse: collapse; 
        width: 50%; 
    }

    .checkout-table tr{
        border: 1px solid  #ccc;
    }

    .checkout-table th {
        background-color: #FFFFFF;
        padding: 20px; 
        text-align: left; 
        font-weight: 600;
        font-family: 'Lato', sans-serif;
        font-size: 20px;
    }

    .checkout-table td{
        background-color: #f5f7f9;
        padding: 15px; 
        text-align: center;
        font-size: 19px;
    }


    .to-center{
        text-align: center;
    }
    .return-to-shop{
        margin-top: 200px;
        text-align: center;

    }


    .return-to-shop button{
        background-color: #007bff;
        color: #fff;
        padding: 10px 20px;
        border: none;
        border-radius: 4px;
        cursor: pointer;
        font-size: 18px;
        margin-top: 50px;
    }

</style>