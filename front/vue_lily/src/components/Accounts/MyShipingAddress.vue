<script setup>
    import axios from 'axios';
    import ImageAdding from '../../../public/accounts/adding-image.png';
    import { DOMAIN_NAME } from '../../utils/api_links.js';
    import { onMounted, ref } from 'vue';
    import { RouterLink } from 'vue-router';

    

    onMounted(
        () => {
            getShippingInfo();
        }
    )
    
    

</script>

<script>


    export const AccessToken = ref(localStorage.getItem('AccessToken'));
    export const shippingData= ref({});
  

    export function getShippingInfo(){
        const FinalEndPoint = DOMAIN_NAME + 'users/my-account-details/view-my-shipping-info/';
        axios.get(FinalEndPoint,{ 
            headers : {
                Authorization: 'Bearer ' + AccessToken.value
            }
            
        }    
        ).then(
            (response) =>{
                shippingData.value = response.data;
                console.log(shippingData.value);
            }
        ).catch(
            (error) => {
                console.log(error);
            }
        )
    }
    
</script>


<template>
    <div>
        <div v-if="shippingData && shippingData.length > 0">
            <div class="billing">
                <div class="head">
                    <h3>Shipping address</h3>
                    <RouterLink :to="{name: 'add_new_address'}"><a>Edit</a></RouterLink>
                </div>
                <div class="body">
              
                    <p>{{ shippingData.first_name }} {{ shippingData.last_name }}</p>
                    <p>{{ shippingData.street_address_1 }}</p>
                    <p>{{ shippingData.city }}</p>
                    <p>{{ shippingData.phone }}</p>
                    <p>{{ shippingData.country }}</p>
                </div>
            </div>
        </div>

        <div v-else>
            <p class="dont-have">Yor Don't Have Yet</p>
            
            <div class="add-address">
                <h3>Add new address</h3>
                <RouterLink :to="{name: 'add_new_address'}"><a><img :src="ImageAdding"></a></RouterLink>
            </div>
        </div>
    </div>
</template>

<style scoped>

  

    .billing {
        min-width: 100%;
        height: 400px; 
        border: 1px solid #e0e0e0;
        border-radius: 5px;
        
        
        
    
    }
    
    
    .head {
        display: flex;
        justify-content: space-between;
        padding: 20px;
        background-color: #f5f3f3;
    }
    
    .head h3 {
        font-size: 20px;
        
    }
    
    .head a {
        text-decoration: none;
        color: #007BFF;
        font-weight: bold;
    }

    .body {
        padding: 10px;
        
    }
    
    .body p {
        font-size: 20px;
        text-align: center;
    }

    .add-address {
        display: flex;
        justify-content: center;
        align-items: center;
    }


    .add-address img{
        width: 50px;
        height: auto;

    }

    .add-address img:hover{
        width: 55px;
    }

    .add-address h3{
        font-weight: 700;
        color: #54595f;
        font-size: 20px;
        text-align: center;
    }

    .dont-have{
        font-size: 25px;
        color: black;
        font-weight: bold;
    }

</style>