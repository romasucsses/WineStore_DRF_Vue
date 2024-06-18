<script setup>
    import { onMounted } from 'vue';
    import { getShippingInfo, shippingData, AccessToken } from './MyShipingAddress.vue';
    import { DOMAIN_NAME } from '../../utils/api_links.js';
    import axios from 'axios';
    import { useRouter } from 'vue-router';
    

    const router = useRouter();
    onMounted( () => {
        getShippingInfo();
    })

    function saveShippingData(){
        console.log('Bearer ' + AccessToken.value);
        const FinalEndPoint = DOMAIN_NAME + 'users/my-account-details/view-my-shipping-info/'
        axios.patch(FinalEndPoint, shippingData.value, {
            headers:{
                Authorization: 'Bearer ' + AccessToken.value
            }
        }).then(
            (response) => {
                console.log(response);
            },
            router.push({name: 'acccount_address'})
            
        ).catch((error) => {
            console.log(error);
        })
    }
</script>

<template>
    <div>
        <h1 class="header-title">View and Edit your Address</h1>


        <div class="main-block">
            <div class="form">
                <div class="client-info">
                    <div class="part1-of">
                        <label for="first_name">First Name:</label>
                        <input type="text" id="first_name" name="first_name" v-model="shippingData.first_name "/>
                        <label for="last_name">Last Name:</label>
                        <input type="text" id="last_name" name="last_name" v-model="shippingData.last_name "/>
                        <label for="country">Country:</label>
                        <input type="text" id="country" name="country" required v-model="shippingData.country"/>
                        <label for="street_address_1">Street Address 1:</label>
                        <textarea id="street_address_1" name="street_address_1" required v-model="shippingData.street_address_1"></textarea>
                        <label for="street_address_2">Street Address 2:</label>
                        <textarea id="street_address_2" name="street_address_2" v-model="shippingData.street_address_2"></textarea>
                    </div>
                    <div class="part2-of">
                        <label for="city">City:</label>
                        <input type="text" id="city" name="city" required v-model="shippingData.city"/>
                        <label for="state">State:</label>
                        <input type="text" id="state" name="state" required v-model="shippingData.state"/>
                        <label for="zip_code">Zip Code:</label>
                        <input type="text" id="zip_code" name="zip_code" required v-model="shippingData.zip_code"/>
                        <label for="phone">Phone:</label>
                        <input type="text" id="phone" name="phone" required v-model="shippingData.phone"/>
                        <label for="email">Email:</label>
                        <input type="email" id="email" name="email" required v-model="shippingData.email"/>

                    </div>
                </div>

                <button class="btn-add-address" @click="saveShippingData()">Save</button>

            </div>
        </div>
    </div>
</template>

<style scoped>
    .header-title {
        font-weight: 700;
        color: #54595f;
        font-size: 30px;
        text-align: center;
    }

    .main-block {
        width: 500px;
        margin: 0 auto;
        margin-top: 20px;
        margin-bottom: 30px;
        background-color: #f9f9f9;
        padding: 20px;
        border-radius: 8px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    }

 

    .client-info{
        display: flex;
        justify-content: space-around;
        padding: 10px;
    }

    label {
        display: block;
        margin-top: 10px;
        font-weight: 600;
        color: #555;
    }

    input,
    textarea {
        width: 100%;
        padding: 10px;
        margin-top: 5px;
        border: 1px solid #ccc;
        border-radius: 4px;
        font-size: 16px;
    }

    input:focus,
    textarea:focus {
        outline: none;
        border: 1px solid #007bff;
    }

    .btn-add-address {
        background-color: #000000;
        color: #fff;
        border: none;
        border-radius: 4px;
        font-size: 15px;
        width: 200px;
        height: 40px;
        margin: 15px;
    }

    .btn-add-address:hover {
        width: 205px;
        height: 45px;
    }
</style>