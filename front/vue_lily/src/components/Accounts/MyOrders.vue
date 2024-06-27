<script setup>
    import { onBeforeMount, ref } from 'vue';
    import { DOMAIN_NAME } from '../../utils/api_links.js';
    import axios from 'axios';
   

    const AccessToken = ref(localStorage.getItem('AccessToken'));
    const orderData = ref();

    function getOrdersData(){
        const final_end_point = DOMAIN_NAME + 'users/my-account-details/my-orders/';
        axios.get(final_end_point, {
            headers:{
                Authorization: 'Bearer ' + AccessToken.value
            }
        }).then((response) => {
            orderData.value = response.data;
        })
    }

    onBeforeMount(() => {
        getOrdersData();
    })
</script>

<template>
    <div v-if="orderData && orderData.length > 0">
    
        <table>
            <tr>
              <th>Order</th>	
              <th>Date</th>
              <th>Status</th>	
              <th>Total</th>	
              <th>Actions</th>
            </tr>

        
            <tr v-for="each_order in orderData" v-bind:key="each_order.pk">
              <td>#{{ each_order.id }}</td>
              <td>{{ each_order.date_created }} </td>
              <td>{{ each_order.status }}</td>
              <td>${{ each_order.total_sum}}</td>
              <td><RouterLink :to="{name: 'account_order_view', params:{pk: parseInt(each_order.id)}}"><button>View</button></RouterLink></td>
            </tr>
        


        </table>
    
    
    
    </div>
    <h2 v-else>You don't have orders yet</h2>

    
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
        background-color:#f5f3f3;

        color: black;
    }


    table button {
        width: 80px;
        height: 30px;
        border: 2px;
        border-radius: 5px;
        background-color: #0084d6;
        color: white;
        font-size: 17px;

    }
</style>