<script setup>

</script>

<template>
    <div>
        <div class="billing">
          <div class="head">
            <h3>Shipping address</h3>
            <a href="#">Edit</a>
          </div>
          <div class="body">
          <!-- {% if user.user_shipping_address %} -->
            <p>user.user_shipping_address.first_name  user.user_shipping_address.last_name </p>
            <p>user.user_shipping_address.street_address_1 </p>
            <p>user.user_shipping_address.city</p>
            <p> user.user_shipping_address.phone</p>
            <p> user.user_shipping_address.country</p>

          <!-- {% else %}
            <p>Yor Don't Have Yet</p>
          {% endif %} -->
          </div>

        </div>

        <div class="add-address">
          <h3>Add new address</h3>
          <a href="#">
            <img src="#">
          </a>
        </div>
    </div>
</template>

<style scoped>
    .right-info{
        width: 600px;
        margin: 20px;
        
        
    }

    /* Styles for the .right-info container */
    .right-info {
        display: flex;
        justify-content: center;
    }
    
    /* Styles for the .billing and .shipping sections */
    .billing, .shipping {
        width: 50%; 
        border: 1px solid #e0e0e0;
        border-radius: 5px;
        margin: 10px;
    
    }
    
    
    .head {
        display: flex;
        justify-content: space-between;
        margin-bottom: 10px;
        padding: 30px;
        background-color: #f5f3f3;
    }
    
    .head h3 {
        font-size: 20px;
        margin: 0;
    }
    
    .head a {
        text-decoration: none;
        color: #007BFF;
        font-weight: bold;
    }

    .body {
        margin: 10px;
        padding: 20px
    }
    
    .body p {
        
        font-size: 16px;
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

</style>