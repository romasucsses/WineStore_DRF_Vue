<script setup>
    import { DOMAIN_NAME } from '../utils/api_links.js';
    import { AddToCart } from '../utils/cart_logic/cart.js';
    import axios from 'axios';
    import { onMounted, ref} from 'vue';
    import {  useRoute } from 'vue-router';
   
    const productDetail = ref({});
    const route = useRoute();
    const slug = route.params.slug;
    let product_category = '';
    const all_reviews = ref(null);

    function getProductDetail(slug){
        const finalEndPoint = DOMAIN_NAME + 'products/product-detail/' + slug;
        axios.get(finalEndPoint)
        .then((response) => {
            productDetail.value = response.data;
            product_category= (productDetail.value.category == 1)?'Wine': 'Sparkling'
            console.log(productDetail.value.id);
            all_reviews.value = new Reviews(productDetail.value.id);
            all_reviews.value.getReviews();
        }).catch((error) => {
            console.log(error);
        });
    };

    class Reviews{
        constructor(id) {
            this.id = id;
            this.finalEndPoint = DOMAIN_NAME + 'products/product-reviews/' + this.id;
            this.reviews = [];
            this.reviews_next = '';
            this.reviews_previous = '';
            this.senderReviewText = '';
            this.senderReviewName = '';
            this.count = '';
        }

        getReviews(){
            axios.get(this.finalEndPoint)
            .then((response) => {
                this.reviews = response.data.results;
                this.reviews_next = response.data.next;
                this.reviews_previous = response.data.previous;
                this.count = response.data.count;
                console.log('reviews', this.reviews);
            })
            .catch((error) => {
                console.log(error);
            });
        }

        sendReview(stars){
            console.log('review data: ', this.senderReviewName, this.senderReviewText)
            axios.post(this.finalEndPoint, {
                name : this.senderReviewName,
                stars_count: parseInt(stars),
                review: this.senderReviewText,
                product: this.id
            })
            .then(() => {
                // After sending the review, refresh the reviews list
                this.getReviews();
            })
            .catch((error) => {
                console.log(error);
            });
        }

        loadNextPage() {
            axios.get(this.reviews_next)
            .then(response => {
                this.reviews = response.data.results;
                this.reviews_next = response.data.next;
                this.reviews_previous = response.data.previous;
            })
            .catch(error => {
                console.log(error);
            });
        }
        loadPreviousPage() {
            axios.get(this.reviews_previous)
            .then(response => {
                this.reviews = response.data.results;
                this.reviews_next = response.data.next;
                this.reviews_previous = response.data.previous;
            })
            .catch(error => {
                console.log(error);
            });
        }
    }

    onMounted(() => {
        getProductDetail(slug);

        
    });
  


</script>

<template>
    <div>
        <div class="product">
            <img :src="productDetail.img_url" class="prod-img" />

            <div class="prod-info">
                <p class="situated">Home/{{ product_category }}/{{ productDetail.name }}</p>
                <p class="categ1">{{ product_category }}</p>

                <h2 class="name">{{ productDetail.name }}</h2>
                <div class="price_shipping_stars">
                    <h4 class="price">${{ productDetail.price }}.00</h4>
                    <div style="margin-top: 20px; margin-left: 10px;">
                        <p class="shiping">+ Free Shipping</p>
                        <div class="review">

                            <div class="stars-img">
                                <img v-for="item in 5" :key="item"
                                    src="../../public/shop/images/site-img/star-photo-review.svg" />
                            </div>
                        </div>
                    </div>

                </div>

                <div class="form">
                    <input id="quality" value="1" type="number">
                    <button class="btn1" @click="AddToCart(productDetail)">ADD TO CART</button>
                </div>

            </div>
        </div>

        <div class="two-block">
            <div class="reviews" v-if="all_reviews !== null">
                <p class="reviws">Reviews ({{ all_reviews.count}})</p>
                <div class="all-reviews">


                    <div class="each-review" v-for="review in all_reviews.reviews" :key="review.id">
                        <img src="../../public/shop/images/site-img/avatar-review.png">
                        <div class="right-colum">
                            <p> {{ review.name }} </p>
                            <p>{{ review.date }} </p>
                            <p>
                                {{ review.review }}
                            </p>
                        </div>

                    </div>
                    <button v-if="all_reviews.reviews_previous" @click="all_reviews.loadPreviousPage"
                        class="pagination-button">Previous Reviews </button>
                    <button v-if="all_reviews.reviews_next" @click="all_reviews.loadNextPage"
                        class="pagination-button">Next Reviews</button>

                </div>


                <div class="write-review">
                    <p>Add a review to La Fleur Lily</p>
                    <div id="review-from" v-if="all_reviews">

                        <input id="name" name="name" type="text" placeholder="Write your name"
                            v-model="all_reviews.senderReviewName">
                        <input id="review" name="review" type="text" placeholder="Write your Review"
                            v-model="all_reviews.senderReviewText">
                        <button id="submit-review" @click="all_reviews.sendReview(5)">Submit my review</button>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<style scoped>
    .pagination-button {
        background-color: #007bff; 
        border: none; 
        color: white; 
        padding: 5px 10px; 
        text-align: center; 
        text-decoration: none; 
        display: inline-block; 
        font-size: 16px; 
        cursor: pointer; 
        border-radius: 5px; 
        margin: 10px; 
    }

    .pagination-button:hover {
        background-color: #54a1f3 
    }
    .product{
    display: flex;
    margin-top:50px;
    width: 1100px;
    margin: 20px;
    padding: 20px;
    }
    .prod-info{
        text-align: left;
        margin-left: 100px;
    }
    .form{
        display: flex;
        justify-content: space-between;
        
    }

    #quality {
    padding: 5px;
    margin-right: 10px;
    font-size: 16px;
    border: 1px solid #ccc;
    border-radius: 4px;
    width: 50px;
    height: 35px;

    }
    .btn1{
    width: 240px;
    height: 40px;

    background-color:blue;
    border: 0;
    }

    .btn1{
    text-decoration: none;
    color: white;
    font-size: larger;
    }

    .prod-img{

    width: 460px;
    height: 460px;
    }

    .categ1{
        color: rgba(0, 0, 0, 0.5);
    }
    .situated{
        color:rgba(0, 0, 0, 0.5);
    }
    

    .price_shipping_stars{
        display: flex;
    }

    

    .price{

    font-size: 30px;
    }

    .two-blcok{
        margin-top: 70px;
    }

    .reviews {
        border: 1px solid #ccc;
        padding: 30px;
        max-width: 1150px;
        margin: 0 auto;
        background-color:#FFFFFF;
        border-radius: 25px;
        display: flex;
        justify-content: space-between;
        margin-top: 90px;
    }

    .reviews p.reviws {
        font-size: 18px;
        font-weight: bold;
        color: #333;
        margin: 0;
    }

    .all-reviews{
        display: inline-block;
        justify-content: left;
        margin-top: 80px;
        margin-right: 250px;
        padding-bottom: 20px;

    }

    .each-review {
        display: flex;
        justify-content: center;
        margin-bottom: 15px;

    }
    
    .each-review img {
        width: 50px;
        height: 50px;
        border-radius: 50%;
        margin-right: 10px;
    }
    
    .right-colum {
        flex-grow: 1;
    }

    .right-colum p:first-child {
        font-size: 16px;
        font-weight: bold;
        margin: 0;
    }

    .right-colum p:nth-child(2) {
        color: #888;
        margin: 5px 0;
    }

    .right-colum p:last-child {
        margin: 10px 0;
    }
    .write-review {
        margin-top: 40px;;
    }
    
    .write-review p {
        font-size: 16px;
        font-weight: bold;
        color: #333;
        margin: 0;
    }
    
    #review-from {
        display: flex;
        flex-direction: column;

    }
    
    #name,
    #review {
        padding: 10px;
        margin: 10px 0;
        border: 1px solid black;
        border-radius: 5px;
    }

    #name{
        margin-top: 35px;
        width: 130px;
        height: 35px;
    }

    #review{
        width: 260px;
        height: 70px;
    }
    
    #submit-review {
        background-color: #007bff;
        color: #fff;
        border: none;
        padding: 10px;
        border-radius: 5px;

    }
    
    #submit-review:hover {
        background-color: #0056b3;
    }
    

    

    .stars-img{
        display: flex;
        justify-content: space-between;
        
    }

    .stars-img img{
        width: 15px;
        height: 15px;
        margin-top: -15px;
        
    }
   @media (max-width: 768px) {
       .product {
           flex-direction: column; 
           align-items: center;
           margin-top: 20px;
           margin-bottom: 50px;
           width: 80%;
       }

       .prod-img {
           width: 100%;
           max-width: 300px;
           height: auto;
           
       }

        .prod-info {
            text-align: center;
            margin-left: 0;
        }
    

       .btn1 {
           width: 100%;
           width: 200px;
       }

       .reviews {
           flex-direction: column;
           padding: 15px;
       }

       .all-reviews {
           margin-right: 0;
       }

       .each-review {
           flex-direction: column;
           align-items: center;
           text-align: center;
       }

       .each-review img {
           margin: 0 0 10px 0;
       }

       .right-colum {
           text-align: center;
       }

       #name,
       #review {
           width: 100%;
           max-width: 100%;
       }
   }
</style>