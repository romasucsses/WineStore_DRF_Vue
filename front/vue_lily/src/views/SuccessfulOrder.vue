<script setup>
    const order_id = localStorage.getItem('order_id');
</script>

<template>
    <div class="to-center">
        <h1 class="cart-header">Your Order have been place Successfuly</h1>
        <h3>Your order id #{{ order_id }} <br>
            also can call and confirm your order +15453432
        </h3>
            <RouterLink :to="{name: 'shop'}">
                <a class="return-to-shop">
                    <button>Return to Shop</button>
                </a>
            </RouterLink>
    </div>
</template>

<style scoped>
    .to-center{
        text-align: center;
    }
    .cart-header{
        color: rgb(11, 183, 11);
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