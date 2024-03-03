<script setup>
  
    import axios from 'axios'
    import {ref, onMounted, watch, watchEffect} from 'vue'


    const products = ref()

    onMounted(() => {
        axios.get('http://127.0.0.1:8000/api/v1/products/wine/')
        .then(
            (responese) => {
                products.value = responese.data;
                console.log("products list : ", products.value);
            }
        )
        .catch((error) =>{
            console.log(error);
        })

        
    })

    //Sorting

    const SelectedSort = ref('default')

    function CallSorting(){
        axios.get('http://127.0.0.1:8000/api/v1/products/wine/', {
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

    // watch(SelectedSort, CallSorting());
    // watchEffect(() => {
    //     CallSorting();
    // })

    //Searching
    
    const searchQuary = ref('');


    function Searching(){
        const quary = searchQuary.value.toLocaleLowerCase();
        if (products.value){
            const initial_products = products.value
            if (searchQuary == ''){
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
                    <input v-model="searchQuary" @keypress="Searching()" @keyup.enter="Searching()" type="text" id="search-prod" name="query" placeholder="Search products..">
                </form>
        
                <div class="categories">
                    <p class="title">Categories</p>
                    <p class="sparkling-cat">Sparkling  (4)</p>
                    <p class="wine-cat">Wine    (8)</p>
                </div>
        
                <div class="best-sellers">
                    <p class="title">Our Best Sellers</p>
        
                    <div class="products-list">
        
        
                        <div v-for="best_seller in 5" :key="best_seller" class="best_seller_card">
                            <a href="#">
                                <div class="card">
                                    <img class="product-img" src="../../public/shop/images/best-sellers/1.png"/>
                                    <div class="info-product-shop">
                                        <span class="name-prod">La Fleur Lily semi-sweet white</span>
                                        <div class="stars">
                                            <img v-for="item in 5" :key="item" src="../../public/shop/images/site-img/star-photo-review.svg"/>
                                        </div>
                                        <span class="price">$15.00</span>
                                    </div>
                                </div>
                            </a>
                            <hr class="horizontal-line-menu"/>
                        </div>
        
                    </div>
                </div>
            </div>
        
            <div class="right-block">
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
        
                    <p class="results">Showing all 12 results</p>
        
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
        
                    <div v-for="product in products" :key="product.id" class="product-card">
                        <a href="#">
                            <img :src= " `http://127.0.0.1:8000${product.image}`" alt="Wait please"/>
                        </a>
                        <div class="info-product-shop">
                            <h2 class="product-name">{{ product.name }} </h2>
                            <p class="product-category" >
                                <span v-if="product.category == 1 ">Wine</span>
                                <span v-else>Sparkling</span>
                            </p>
                            <p class="product-price">${{ product.price }}.00</p>
                            <div class="review">

                                <div class="stars-img">
                                    <img v-for="item in 5" :key="item" src="../../public/shop/images/site-img/star-photo-review.svg"/>
                                </div>
                            </div>
                        </div>
                    </div>

                </div>
            </div>
        </div>
        
       
    </div>
</template>

<style scoped>
    /* editing main-content-block */

.main-content{
    display: flex;
    justify-content: space-between;
    max-width: 1200px;
}

/*editing left-block */

.left-block{
    margin-left: 16px;
    max-width: 300px;
}

.search-prod-form input{
    height: 40px;
    border: none;
    width: 200px;
    font-size: 17px;
}

.search-prod-form button{
    height: 40px;
    width: 36px;
    color: #FFFFFF;
    background-color: #0075be;
    border: none;
    font-size: 20px;
}


.categories{
    margin-top: 70px;
    padding-bottom: 9px;
}
.categories .title{
    font-size: 28px;
}

.categories .wine-cat,
.categories .sparkling-cat{
    font-size: 18px;
}

.best-sellers{
    margin-top: 40px;
}


.best-sellers .title{
    font-size: 26px;
    padding-bottom: 20px;
}

.card{
    display: flex;
    justify-content: space-between;
    max-width: 245px;
    max-height: 115px;
}

.info-product{
    text-align: left;
    margin-right: 35px;
}

.price{
    font-size: 18px;
    font-weight: 200;
}

.product-img{
    width: 64px;
    height: 64px;
}

.stars{
    display: flex;
    justify-content: space-between;
    max-width: 60px;
    
}

.stars img{
    width: 15px;
    height: 15px;
    bottom: 0;
    padding: 1px;
    margin: 1px;
    margin-top: 13px;
}   




/*editing right-block */


.right-block{
    background-color: #FFFFFF;
    max-width: 910px;
}

.head-category{
    margin: 30px;
    padding: 30px;
}

.head-category h1{
    font-weight: 300;
    font-size: 60px;
}

.head-category p{
    font-size: 19px;
    line-height: 1.7;
}

.head-rightcolum{
    display: flex;
    justify-content: space-between;
    margin: 50px;

}

.head-rightcolum p{
    font-size: 18px;
    color: #666;
}

.head-rightcolum select{
    background-color: transparent;
    border: transparent;
    border-radius: 2px;
    color: #666;
    width: 210px;
    height: 50px;
    font-size: 16px;
    border-color: #666;
    box-shadow: #666;
    
}

.head-rightcolum button{
    height: 35px;
    width: 55px;
    color: #FFFFFF;
    background-color: #0075be;
    border: none;
    font-size: 20px;
    border-radius: 8px;
}

.proucts-shop{
    display: flex;
    justify-content: center;
    flex-wrap: wrap;
    max-width: 100%;
    margin-top: 60px;
    padding: 15px;
    width: 100%;
    max-width: 900px;
}

.product-card{
    text-align: left;
    padding: 8px;
}

.product-card img{
    width: 219px;
    height: 219px;
    margin: 9px;
}

.product-category{
    font-weight: 100;
    letter-spacing: 1px;
    color: #6f6f6f;
}

.info-product-shop{
    margin: 10px 0;
}

.product-name,
.product-category,
.product-price,
.review {
    margin: 5px 0;
}

.info-product-shop h2{
    font-size: 16px;
    font-weight: 550;
}

.product-price{
    font-size: 27px;
    font-weight: 500;
}

.review{
    display: flex;
    position: relative;
    color: #8e7e4d;
}

.stars-img{
    display: flex;
    justify-content: space-between;
    
}

.stars-img img{
    width: 15px;
    height: 15px;
    bottom: 0;
    padding: 1px;
    margin: 1px;
    margin-top: 13px;
}  
</style>