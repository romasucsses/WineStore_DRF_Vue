<script setup>

</script>

<template>
    <div class="to-center">
        <h1 class="cart-header">Your Order have been place Successfuly</h1>
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