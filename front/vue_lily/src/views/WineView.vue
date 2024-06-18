<script setup>
    import { DOMAIN_NAME } from '@/utils/api_links';
    import axios from 'axios'
    import {ref, onMounted, watchEffect} from 'vue'


    const products = ref({})
    const finalEndpoint = DOMAIN_NAME + 'products/wine/';
    onMounted(() => {
        getProducts();
    })

async function getProducts() {
    axios.get(finalEndpoint)
        .then(
            (responese) => {
                products.value = responese.data;
                console.log("products list : ", products.value);
            }
        )
        .catch((error) => {
            console.log(error);
        })
    }

    //Sorting

    const SelectedSort = ref('default')

    function CallSorting(){
        axios.get(finalEndpoint, {
            params : { 'action': 'ordering', 'ordering_by': SelectedSort.value}
        })
        .then( 
            (response) => {
                products.value = response.data;
            }
        )
        .catch(
            (errors) => {
                console.log(errors);
            }
        )
    };

    
    const searchQuary = ref('');


    function Searching(){
        const quary = searchQuary.value.toLocaleLowerCase();
        if (products.value){
            const initial_products = products.value
            if (searchQuary.value == ''){
                products.value = initial_products;
            }else{
                products.value = products.value.filter(record => {
                return record.name.toLocaleLowerCase().includes(quary)})
            }
        } 
    };

    watchEffect(() => {
        Searching();
        CallSorting();
    })
</script>

<template>

    <div>


        <div class="main-content">

            <div class="left-block">
                <form class="search-prod-form">
                    <input v-model="searchQuery" @keypress="Searching()" @keyup.enter="Searching()" type="text"
                        id="search-prod" name="query" placeholder="Search products..">
                </form>

                <div class="categories">
                    <p class="title">Categories</p>
                    <RouterLink :to="{name:'sparkling'}">
                        <p class="sparkling-cat">Sparkling</p>
                    </RouterLink>
                    <RouterLink :to="{name: 'wine'}">
                        <p class="wine-cat">Wine</p>
                    </RouterLink>
                    <RouterLink :to="{name: 'shop'}">
                        <p class="wine-cat">All Products</p>
                    </RouterLink>
                </div>


            </div>

            <div class="right-block-products">
                <div class="head-category">
                    <h1>Wine</h1>
                    <p>
                        Welcome to our exquisite wine collection, where passion and
                        craftsmanship come together to create a delightful journey for your
                        senses. Explore our carefully curated wines, each offering a
                        distinct experience and flavor profile that will captivate both
                        connoisseurs and newcomers alike.
                    </p>
                </div>

                <div class="head-rightcolum">

                    <p class="results">Showing all {{ products.length }} results</p>

                    <form class="ordering-form" method="get" action="#">
                        <select name="ordering-by" class="sorting" v-model="SelectedSort" @change="CallSorting()">
                            <option value="default" selected="selected">Sorting by Default</option>
                            <option value="popularity">By popularity</option>
                            <option value="price-up">By Price Low -> High</option>
                            <option value="price-down">By Price High -> Low</option>
                        </select>

                    </form>
                </div>

                <div class="proucts-shop">

                    <div v-for="product in products" :key="product.id" class="product">
                        <RouterLink :to="{name:'product_detail', params:{slug: product.slug_url}}">
                            <img :src="product.img_url" alt="Wait please" />
                        </RouterLink>
                        <div class="info-product-shop">
                            <h2 class="product-name">{{ product.name }} </h2>
                            <p class="product-category">
                                <span v-if="product.category == 1 ">Wine</span>
                                <span v-else>Sparkling</span>
                            </p>
                            <p class="product-price">${{ product.price }}.00</p>
                            <div class="review">

                                <div class="stars-img">
                                    <img v-for="item in 5" :key="item"
                                        src="../../public/shop/images/site-img/star-photo-review.svg" />
                                </div>
                            </div>
                        </div>
                    </div>

                </div>
            </div>
        </div>


    </div>
</template>
