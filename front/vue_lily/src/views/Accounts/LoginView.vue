<script setup>
    import { DOMAIN_NAME } from '../../utils/api_links.js'
    import {ref, watch, onMounted } from 'vue';
    import axios from 'axios';
    import { useRouter } from 'vue-router';

    function sendLoginDataToAPI(){
        axios.post(URL_LOGIN_API, {
            username: UsernameData.value,
            password: PasswordData.value,
        }).then(
            response =>{
                localStorage.setItem('AccessToken', response.data.access);
              
                localStorage.setItem('RefreshToken', response.data.refresh);
               
                
                localStorage.setItem('isAuthenticated', true);
                
                router.push({name: 'my_account'})
            }
        ).catch(error => {
            console.log(error)
        });
    };

    const isAuthenticated = ref(localStorage.getItem('isAuthenticated')=== 'true');
    console.log(isAuthenticated.value);
    const router = useRouter();

    onMounted(() => {
        if (isAuthenticated.value) {
            router.push({ name: 'account_details' });
        }
    });
    
    const URL_LOGIN_API = DOMAIN_NAME + 'users/get-token/';
    const PasswordData = ref();
    const UsernameData = ref();



    function getNewTokens(){
        console.log('getNewTokens() is running')
        const URL_GET_NEW_TOKEN_API = DOMAIN_NAME + 'users/get-refresh-token/';
        const old_refresh_token = localStorage.getItem('RefreshToken');

        axios.post(URL_GET_NEW_TOKEN_API, { 
            refresh: old_refresh_token
        }).then(
            response => {
                localStorage.setItem('AccessToken', response.data.access);
                localStorage.setItem('RefreshToken', response.data.refresh);
            }
        ).catch(error => {
            console.log(error)
        })
    }
    
    watch(isAuthenticated, (newValue) => {
        if (newValue === true){
            setInterval(getNewTokens, 1 * 60 * 1000);
        }
        
    })

</script>



<template>

    <div>
       

        <div class="login-form">
          
            <h1>Login</h1>
            <div>
                <div class="group">
                    <label>Email</label>
                    <input v-model="UsernameData" type="username" id="id_username" name="username">
                </div>
                <div class="group">
                    <label>Password</label>
                    <input v-model="PasswordData" type="password" id="id_password" name="password">
                </div>
                <div class="remember-me">
                    <p>Remember Me</p>
                    <input type="checkbox" name="remember-me">
                </div>
                <button @click="sendLoginDataToAPI()" type="submit">Login</button>
                <RouterLink :to="{name: 'sing_up'}"><a class="create-account" >Create account</a></RouterLink>
            </div>
        </div>

     
    </div>
</template> 

<style scoped>
.login-form {
    margin: 0 auto;
    margin-top: 60px;
    width: 400px;
    padding: 20px;
    background-color: #f9f9f9fb;
    text-align: center;
    border: 1px solid #ccc;
    border-radius: 5px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.login-form h1 {
    color: #333;
    font-size: 24px;
    margin-bottom: 20px;
}

.login-form form {
    width: 90%;
    margin-top: 20px;
}

.group {
    margin-bottom: 20px;
}

.group label {
    display: block;
    text-align: left;
    color: #555;
    font-weight: bold;
    margin-bottom: 5px;
}


.group input{
    width: 90%;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 5px;
    font-size: 16px;
}

.remember-me {
    display: flex;
    justify-content: left;
    color: #555;
    font-size: 14px;
}

.remember-me input[type="checkbox"] {
    margin-right: 5px;
}

button[type="submit"] {
    background-color: #007BFF;
    color: #fff;
    border: none;
    border-radius: 5px;
    padding: 9px 18px;
    font-size: 15px;
    cursor: pointer;
    transition: background-color 0.3s;
}

button[type="submit"]:hover {
    background-color: #0056b3;
}

.create-account {
    margin-top: 10px;
    margin-left: 10px;
}

.create-account a {
    text-decoration: none;
    color: #007BFF;
}

.create-account a:hover {
    text-decoration: underline;
}

@media (max-width: 768px) {
    .login-form {
        width: 70%;
        margin: 20px auto;
        margin-bottom: 40%;
        margin-top: 10%;
    }

    .group input {
        width: 100%;
    }
}
</style>
