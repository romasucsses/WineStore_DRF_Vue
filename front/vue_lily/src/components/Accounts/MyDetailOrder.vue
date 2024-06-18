<script setup>
    import { onMounted, ref } from 'vue';
    import { DOMAIN_NAME } from '../../utils/api_links.js';
    import axios from 'axios';
    import {useRoute} from 'vue-router'
    import { RouterLink } from 'vue-router';
   

    const AccessToken = ref(localStorage.getItem('AccessToken'));
    const orderData = ref();
    const orderCartData = ref();

    function getOrdersData(){
        const route = useRoute();
        const pk = parseInt(route.params.pk);
        const final_end_point = DOMAIN_NAME + `users/my-account-details/my-detail-order/${pk}`;
        axios.get(final_end_point, {
            headers:{
                Authorization: 'Bearer ' + AccessToken.value
            }
        }).then((response) => {
            orderData.value = response.data;
            console.log(orderData.value)
            // orderCartData.value = JSON.stringify(orderData.value.cart_data);
        })
    }

    onMounted(() => {

        getOrdersData();
    })
</script>

<template>
    <div v-if="orderData">
        <h3>Order Nr. # {{ orderData.id }} Information</h3>
        <table class="data-table">

            <thead>
                <tr>
                    <th>Product</th>
                    <th>Sub Total</th>
                </tr>
            </thead>

            <tbody>
            
                <tr v-for="each_product in orderData.cart_data" :key="each_product.id">
                    <td><RouterLink :to="{name:'product_detail', params:{slug: each_product.slug_url}}">{{ each_product.name }}</RouterLink></td>
                    <td><span>${{ each_product.price  *  each_product.quantity }} </span></td>
                </tr>
            

            </tbody>

            <tfoot>

                <tr>
                    <th scope="row">Payment method</th>
                    <td> {{ orderData.payment_method }} </td>
                </tr>

                <tr>
                    <th scope="row">Date:</th>
                    <td><span> {{ orderData.date_created }} </span></td>
                </tr>

                <tr>
                    <th scope="row">Total:</th>
                    <td><span>$ {{ orderData.total_sum }} </span></td>
                </tr>

            </tfoot>

        </table>

    </div>
</template>

<style scoped>
    .right-info{
        width: 600px;
        margin: 20px;
        
        
    }



    table {
        margin-left: 10px;
        font-family: Arial, sans-serif;
        border-collapse: collapse;
        width: 100%;
        background-color: #FFFFFF;
    }

    th, td {
        border: 1px solid #483e3e;
        text-align: left;
        padding: 10px;

    }

    th {
        background-color: #007bff;
        color: white;
    }
</style>