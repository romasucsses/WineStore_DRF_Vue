<script setup>
    
    import { onBeforeMount } from 'vue';
import { RouterView, RouterLink } from 'vue-router';
    import { useRouter } from 'vue-router';

    const router = useRouter();

    function logOutFromAccount(){
        localStorage.removeItem('AccsessToken');
        localStorage.removeItem('RefreshToken');
        localStorage.removeItem('isAuthenticated');
        router.push({name: 'login'});
        
        
    };

    onBeforeMount(() => {
        const isAuthenticated = localStorage.getItem('isAuthenticated') === 'true';
        if (isAuthenticated === false){
            router.push({name: 'login'});
        }
    })
    
    
</script>

<template>

    <div>
       

        <h2 class="greetings">Hey  user.name , we really happy to see you again on our store</h2>
        
        <div class="main-block">
        
            <div class="left-menu">
                <nav>
                    <ul>
                        <li><RouterLink :to="{name: 'account_details'}">Account details</RouterLink></li>
                        <li><RouterLink :to="{name: 'account_all_orders'}">My Orders</RouterLink></li>
                        <li><RouterLink :to="{name: 'acccount_address'}">My Address</RouterLink></li>
                        <li @click="logOutFromAccount()"><a>LogOut</a></li>
                    </ul>
                </nav>
            
            </div>
        
            <div class="right-info">
                <RouterView/>
            </div>
        
        </div>

        
    </div>

</template>

<style scoped>

    .greetings{
        text-align: center;
        font-size: 24px;
        color: #483e3e;
        font-weight: bold;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    .main-block{

        margin-top: 80px;
        display: flex;
        justify-content: center;
        width: 90%;
    }

    .left-menu li{
        list-style: none;
        width: 350px;
        height: 45px;
        border: solid 0.5px;
        border-radius: 5px;
        margin: 7px;

    }

    .left-menu li:hover{
        width: 370px;
        height: 55px;
    }

    .left-menu a{
        display: block;
        line-height: 1.8;
        padding: 0.5em 1em;
        font-size: 17px;
        color:#333333;

    }

    .left-menu a:hover{
        color:#0084d6;
        font-size: 19px;
    }

    .right-info{
        width: 600px;
        margin: 20px;
        
        
    }

    .right-info {
        display: flex;
        justify-content: center;
    }

</style>