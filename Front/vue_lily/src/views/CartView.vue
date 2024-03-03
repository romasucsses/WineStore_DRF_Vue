<script setup>
    import NavMneu from '../../components/NavMenu.vue';
    import FooterMenu from '../../components/FooterMenu.vue';

    let product_id = JSON.parse(localStorage.getItem('prod_id_link'))


    export let cart = JSON.parse(localStorage.getItem('cart_storage'));

    if (!cart) {
        cart = [];
    };

    function SaveLocalData() {
        localStorage.setItem('cart_storage', JSON.stringify(cart));
    }

    function ManageCart() {
        
        let existing_record;
    
        cart.forEach((record) => {
            if (record.id === product_id) {
                existing_record = record;
            }
        });

        if (existing_record) {
            existing_record.quantity += 1;
        } else {
            cart.push({
                id: product_id,
                quantity: 1,
                name: products[product_id -1 ].name,
                price: products[product_id -1 ].price,
                category: products[product_id -1 ].category,
                image: products[product_id -1 ].image,
                slug: products[product_id -1 ].slug
            });
        };


        SaveLocalData();
        console.log(cart);


    };

    function RedirectToCart() {
        window.location.href = '/public/orders/cart.html';
    }

    function DeleteItemFromCart(IndexArray) {
        const indexToDelete = cart.findIndex((item) => item.id === IndexArray);
        cart.splice(indexToDelete, 1);
        SaveLocalData();
        location.reload();
    };

    export { ManageCart, RedirectToCart, DeleteItemFromCart };



    const ItemBlock = document.querySelector(".products-table");
    const CartSet = JSON.parse(localStorage.getItem('cart_storage'));
    console.log(CartSet);
    let total_sum = 0;

    CartSet.forEach((eachitem) => {
        ItemBlock.innerHTML +=
        `
            <tr>
                <td class="cancel-prod">
                    <div>
                        <button class="delete-item" data-index="${eachitem.id}">
                            <img src="../../src/orders/assets/images/site-img/cancel-circle.svg">
                        </button>
                    </div>
                </td>
                <td class="image-prod"><a href="#"><img src="${eachitem.image}"></a></td>
                <td> ${eachitem.name} </td>
                <td>$ ${eachitem.price}.00</td>
                <td><input type="number" value="${eachitem.quantity}"></td>
                <td>$${eachitem.price * eachitem.quantity}.00</td>
            </tr>
        `;
        total_sum += eachitem.price * eachitem.quantity;


        
        
    });

    document.querySelector(".total-sum").innerHTML = `$${total_sum}.00`;

    document.querySelectorAll(".delete-item").forEach((deleteButton) => {
        deleteButton.addEventListener('click', () => {
            const data_index = deleteButton.dataset.index;
            console.log(data_index);
            DeleteItemFromCart(parseInt(data_index));
            
        });
    });

    if (CartSet.length === 0){
        
        document.querySelector('body').innerHTML = 
        `
            <div class="to-center">
                <h1 class="cart-header">Your Cart is Empty Now</h1>
                <a href="/public/shop/shop.html" class="return-to-shop">
                    <button>Return to Shop</button>
                </a>
            </div>
        `;
    };
</script>

<template>
    <div>
       

        <div class="main-block">
            <h1 class="cart-header">Cart</h1>
            <table class="products-table">
                <tr>
                    <th colspan="2"><a href="/public/shop/shop.html"><button>Add Others Products</button></a></th>
                    <th>Product</th>
                    <th>Price</th>
                    <th>Quantity</th>
                    <th>Subtotal</th>
                </tr>
            </table>
            <div class="total">
                <form class="coupons-add">
                    <div class="coupons">
                        <input type="text" placeholder="Your coupon..">
                        <button>Apply Coupon</button>
                    </div>
                </form>
                <table class="checkout-table">
                    <tr>
                        <th colspan="2">Cart Totals</th>
                    </tr>
                    <tr>
                        <td>Total</td>
                        <td class="total-sum"></td>
                    </tr>
                    <tr>
                        <td colspan="2"><a href="{% url 'checkout_as_user' %}"><button>Checkout</button></a></td>
                    </tr>
                </table>
            </div>
        </div>

        
    </div>

</template>

<style scoped>
    .main-block{
        margin: 15px;
        margin-bottom: 90px;
        
    }

    .cart-header{
        font-weight: 700;
        color: #54595f;
        font-size: 60px;
        text-align: center;

    }

    .products-table {
        margin: 0 auto; 
        margin-top: 90px;
        font-family: Arial, sans-serif; 

        border: 1px solid #444; 
        border-collapse: collapse; 
        width: 80%; 
    }

    .products-table tr{
        border: 1.5px solid  #ccc;
    }

    .products-table th {
        background-color: #FFFFFF;
        padding: 20px; 
        text-align: center; 
        font-weight: 600;
        font-family: 'Lato', sans-serif;
    }

    .products-table th button{
        width: 150px;
        height: 45px;
        background-color: #007bff;
        color: #FFFFFF;
        border: 0;
        font-size: 17px;
        border-radius: 5px;
        font-weight: 600;
    }

    .products-table td{
        background-color: #f5f7f9;
        padding: 15px; 
        text-align: center;
        font-size: 17px;
    }


    .products-table a {
        text-decoration: none; 
        color: #007bff; 
    }

    .image-prod img {
        max-width: 70px;
        max-height: 70px;
    }

    .cancel-prod img{
        max-width: 20px;
        max-height: 20px;
    }

    .cancel-prod img:hover{
        max-width: 28px;
        max-height: 28px;
    }


    input[type="number"] {
        width: 70px;
        text-align: center;
        padding: 10px;

    }

    .total{
        display: flex;
        justify-content: center;
    }

    .coupons-add{
        margin: 0 auto;
        margin-top: 60px;
        
        max-width: 40%;
        padding: 25px;
        border-radius: 10px;
    }

    .coupons input{
        width: 190px;
        height: 35px;
    }



    .coupons-add button{
        width: 170px;
        height: 45px;
        background-color: #007bff;
        color: #FFFFFF;
        border: 0;
        font-size: 17px;
        margin-top: 30px;
        border-radius: 5px;
    }


    .checkout-table {
        margin: 0 auto; 
        margin-top: 90px;
        font-family: Arial, sans-serif; 

        border: 1px solid #444; 
        border-collapse: collapse; 
        width: 50%; 
    }

    .checkout-table tr{
        border: 1px solid  #ccc;
    }

    .checkout-table th {
        background-color: #FFFFFF;
        padding: 20px; 
        text-align: left; 
        font-weight: 600;
        font-family: 'Lato', sans-serif;
        font-size: 20px;
    }

    .checkout-table td{
        background-color: #f5f7f9;
        padding: 15px; 
        text-align: center;
        font-size: 19px;
    }

    .checkout-table button{
        width: 520px;
        height: 65px;
        background-color: #0084d6;
        color: #FFFFFF;
        border: 0;
        font-size: 20px;
    }

    .to-center{
        text-align: center;
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