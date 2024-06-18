<script setup>
    import { DOMAIN_NAME } from '@/utils/api_links';
    import axios from 'axios';
    import { useRouter } from 'vue-router';

    
    const router = useRouter();
    let email;
    let password;

    function createUser(){
        const finalEndPoint = DOMAIN_NAME + 'users/sign-up/';
        axios.post(finalEndPoint, {
            email: email,
            password: password
        }).then((response) => {console.log(response)})
        router.push({name:'login'});
    }
</script>


<template>
    <div>
       

        <div class="login-form">
            <h1>Sing Up</h1>
            <div>
    
                <div class="group">
                    <label>Email</label>
                    <input type="text" name="email" v-model="email">
                </div>
                <div class="group">
                    <label>Password</label>
                    <input type="password" name="password" v-model="password">
                </div>
                <div class="remember-me">
                    <p>Remember Me</p>
                    <input type="checkbox" name="remember-me">
                </div>
    
                <button @click="createUser()" >Create Account</button>
                <RouterLink :to="{name: 'login'}"><a class="create-account">Login</a></RouterLink>
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

.group input {
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

button {
    background-color: #007BFF;
    color: #fff;
    border: none;
    border-radius: 5px;
    padding: 9px 18px;
    font-size: 15px;
    cursor: pointer;
    transition: background-color 0.3s;
}

button:hover {
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