<script setup>
    import { DOMAIN_NAME } from '../../utils/api_links.js'
    import { onMounted, ref } from 'vue';
    import axios from 'axios';
    
    const  URL_ACCOUNT_INFO = DOMAIN_NAME + 'users/my-account-details/';
    const  AccessToken = ref(null);
    const dataAccount = ref({});
    


    function GetDataAccount(token){
        console.log(`Bearer ${token}`);
        axios.get(URL_ACCOUNT_INFO, {
            headers: {
                Authorization: `Bearer ${token}`
                
            }   
       
    
    }).then( 
        response => {
            
            dataAccount.value = response.data;
            console.log(dataAccount.value.email);
            
        }
    ).catch(
        errors =>{
            console.log(errors)
        }
    )
    }

    function UpdateAccountData(){
        
        console.log(dataAccount.value);
        console.log(`Bearer ${AccessToken.value}`);
        axios.patch(URL_ACCOUNT_INFO, dataAccount.value, {
            headers: {
                Authorization: `Bearer ${AccessToken.value}`
            }
        })
        .then(
            response => {
                console.log(response)
            })
    }

    onMounted(
        () => {
            AccessToken.value = localStorage.getItem('AccessToken');
            if (AccessToken.value){
                GetDataAccount(AccessToken.value);
            }
        }
    )
</script>

<template>
    
    <div>
        
        <p>Editing Your Account Information</p>
        <div class="form">
            <div class="fields">
                <div class="data">
                    <label>username</label>
                    <input id="username" name="username" v-model="dataAccount.username" >
                    <label>email</label>
                    <input id="email"  name="email" v-model="dataAccount.email"> 
                </div>
                <div class="data">
                    <label>first name</label>
                    <input id="name" name="name" v-model="dataAccount.name">
                    <label>last name</label>
                    <input id="last_name" name="last_name"  v-model="dataAccount.last_name">
                </div>
            </div>
            <div class="btns">
                <button name="action" @click="UpdateAccountData()">Save Changes</button>
                <button>Reset Password</button>
            </div>
        </div>
    </div>
</template>

<style scoped>
    .right-info .fields{
        display: flex;
        justify-content: space-between;

    }

    .right-info .data{
        margin: 15px;
    }

    .right-info .form {
        display: flex;
        flex-direction: column;
        max-width: 400px;
        margin: 0 auto;
    }

    .right-info label{
        color: gray;
    }

    .right-info input {
        padding: 10px;
        margin-bottom: 10px;
        border: 1px solid #ccc;
        border-radius: 5px;
        font-size: 16px;
        width: 250px;
    }

    .right-info button {
        padding: 10px 20px;
        margin: 5px;
        border: none;
        border-radius: 5px;
        background-color: #007bff;
        color: #fff;
        font-size: 14px;


    }

    .right-info button:hover {
        background-color: #0056b3;
    }

    .right-info .btns {
        width: 80%;
        display: flex;
        justify-content: space-between;
        margin-left: 140px;
    }

    .right-info .btns button {
        margin-bottom: 10px;
    }
</style>
