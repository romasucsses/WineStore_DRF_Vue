<script setup>

import { RouterLink } from 'vue-router'


 const items = [
    {
        image: "../../public/pages/images/block3_first_img.jpg",
        p_text: "To provide you with the best wine and service is our primary goal.",
        a_text: "OUR WINES",
        link: "/shop/wine"
    },
    {
        image: "../../public/pages/images/block3_second_img.jpg",
        p_text: "La Fleur Lily is love in a glass.",
        a_text: "OUR SPARKLING",
        link: "/shop/sparkling"
    },
    {
        image: "../../public/pages/images/block3_three_img.jpg",
        p_text: "La Fleur Lily - wine born with love and passion.",
        a_text: "OUR STORY",
        link: "/about-us"
    }

]



</script>

<template>
  <div style="margin: 0; padding: 0;" class="max-width">
    <div class="first-block">

      <div class="buttons">
        <button class="block1-btn1">
          <RouterLink to="/shop"><a class="block1-a1">SHOP NOW</a></RouterLink>
        </button>
        <button class="block1-btn2">
          <RouterLink to="/about-us"><a class="block1-a2">ABOUT US</a></RouterLink>
        </button>
      </div>
    </div>
    <div class="two-block">
      <video src="../../public/pages/videos/first_video_two-block.mp4" width="580" height="300" autoplay muted loop
        controls="false">
        Your browser does not support the video
      </video>
      <p>
        Welcome to La Fleur Lily, where organic wines<br>
        are crafted with soul.Our vineyards thrive<br>
        under the nurturing touch of nature, yielding<br>
        grapes bursting with vibrant flavors.<br>
        Experience the essence of our handcrafted<br>
        wines, made with love and care, and embark<br>
        on a journey of pure delight for your senses.
      </p>
    </div>
    <div class="three-block">
      <div class="card" v-for="item in items" :key="item.image">
        <img :src="item.image" class="block3-first-img" />
        <div class="act-on-content">
          <p class="block3-p1">{{ item.p_text }}</p>
          <button class="block3-btn1">
            <RouterLink :to="item.link"><a>{{ item.a_text }}</a></RouterLink>
          </button>
        </div>
      </div>
    </div>
    <div class="home-products">
      <h2 class="featured-prod">Featured Products</h2>
      <div class="products">
        <!-- <div class="product-card">
              <a href="{% url 'each_wine' wine_slug=product.slug %}">
                  <img src="{{ product.image.url }}" alt="Wait please"/>
              </a>
              <div class="info-product-shop">
            <h2 class="product-name">{{ product.name }} </h2>
            <p class="product-category">{{ product.category }}</p>
            <p class="product-price">${{ product.price }}0</p>
            <div class="review">
              <p>stars</p>
              <div class="stars-img">
    
                <img src="{% static 'shop/images/site-img/star-photo-review.svg' %}"/>
    
              </div>
            </div>
          </div> -->
      </div>
      <button class="products-btn">
        <a href="#">VIEW ALL PRODUCTS</a>
      </button>
    </div>
  </div>


</template>

<style scoped>

.first-block {
  position: relative;
  height: 470px;
  background-image: url(../../public/pages/images/first-background-img.jpg);
  background-size: cover;
  background-attachment: fixed;
}
.first-block button {
  margin-top: 15%;
  font-size: larger;
  margin-left: 45px;
}


button a {
  text-decoration: none;
}

.block1-btn1 {
  width: 180px;
  height: 50px;
  background-color: white;
  border: 0;
}

.block1-btn1 a {
  color: black;
}

.block1-btn1:hover {
  background-color: black;
  border: 0;
}

.block1-btn1:hover a {
  color: white;
}

.block1-btn2 {
  width: 165px;
  height: 50px;
  border: 6%;
  border-color: white;
  background-color: rgba(0, 0, 0, 0);
}

.block1-btn2 a {
  color: white;
}

.block1-btn2:hover {
  background-color: white;
  border: 0;
}

.block1-btn2:hover a {
  color: black;
}

.block1-p1 {
  font-size: xxx-large;
  color: #ffffff;
  /* margin-top: 50px; */
  margin-left: 5%;
  border: 10px;
  border-color: #000000;
}


.two-block {
  display: flex;
  justify-content: space-between;
  width: 1100px;
}


.two-block video::-webkit-media-controls-panel {
  display: none;
}

.two-block video::-webkit-media-controls {
  display: none;
}

.two-block video {
  margin-top: 30px;
  margin-right: 5px;
  padding-left: 0%;
  padding-right: 0%;
}

.two-block p {
  text-align: left;
  width: 350px;
  margin-top: 75px;
  margin-left: 40px;
  font-style: normal;
  font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva,
    Verdana, sans-serif;
  font-size: medium;
  line-height: 32px;
}

.three-block {
  display: flex;
  margin-top: 75px;
  justify-content: space-between;
}

.three-block img {
  width: 380px;
  height: 480px;
  position: relative;
  object-fit: cover;
}

.card{
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  padding: 20px;
  position: relative;
  height: 480px;
}

.act-on-content {
  position: absolute;
  bottom: 0;
  left: 0;
  margin-bottom: 90px;
  margin-left: 40px;
}

.three-block button {
  width: 180px;
  height: 50px;
  background-color: white;
  border: 0;
}
.three-block button a {
  color: black;
  font-size: large;
}

.three-block button:hover {
  background-color: black;
}

.three-block button:hover a {
  color: white;
}

.three-block p {
  font-size: xx-large;
  width: 240px;
  color: white;
  background-color: rgb(181, 170, 170);
}

.home-products {
  text-align: center;
}

.featured-prod {
  align-content: center;
  font-size: 40px;
  color: #000000;
}

.products {
  display: flex;
  justify-content: center;
  flex-wrap: wrap;
  max-width: 100%;
  margin-top: 50px;
  padding: 15px;
}

.product-card {
  text-align: left;
  padding: 8px;
}

.product-card img {
  width: 219px;
  height: 219px;
  margin: 9px;
}

.product-category {
  font-weight: 100;
  letter-spacing: 1px;
  color: #6f6f6f;
}

.info-product-shop {
  margin: 10px 0;
}

.product-name,
.product-category,
.product-price,
.review {
  margin: 5px 0;
}

.info-product-shop h2 {
  font-size: 16px;
  font-weight: 550;
}

.product-price {
  font-size: 27px;
  font-weight: 500;
}

.review {
  display: flex;
  position: relative;
  color: #8e7e4d;
}

.stars-img {
  display: flex;
  justify-content: space-between;
}

.stars-img img {
  width: 15px;
  height: 15px;
  bottom: 0;
  padding: 1px;
  margin: 1px;
  margin-top: 13px;
}

.products-btn {
  margin-top: 90px;
  width: 820px;
  height: 50px;
  margin-left: 20px;
  background-color: rgba(0, 0, 0, 0);
  border: 10%;
  border-color: black;
}

.products-btn a {
  color: black;
  font-size: larger;
}

.products-btn:hover {
  background-color: black;
}

.products-btn:hover a {
  color: white;
}


@media (max-width: 768px) {
  .max-width{
    max-width: 100%;
  }

  .first-block {
    height: 300px;
    background-attachment: scroll;
    width: 100%;
  }

  .first-block button {
    margin-top: 60%;
    font-size: medium;
    margin-left: 10%;
  }

  .block1-btn1,
  .block1-btn2 {
    width: 140px;
    height: 40px;
  }

  .two-block {
    display: block;
    width: 100%;
  }

  .two-block video {
    width: 80%;
    height: auto;
    margin: 0 auto;
    display: block;
    margin-top: 10%;
  }

  .two-block p {
    text-align: center;
    width: auto;
    margin: 5px;
    font-size: small;
  }

  .three-block {
    display: block;
    margin: 20px auto;
    justify-content: center;
    text-align: center;
  }

  .three-block img {
    width: 100%;
    height: 350px;
  }

  .card {
    width: 90%;
    height: auto;
  }

  .act-on-content {
    margin: 0 auto;
    bottom: 10px;
    left: 50%;
    transform: translateX(-50%);
   
  }

  .three-block button {
    width: 100%;
    height: 40px;
    font-size: medium;
    margin-bottom: 30px;
  }

  .three-block p {
    font-size: large;
    width: 90%;
    margin: 0 auto;
    margin-bottom: 50px;
  }

  .products {
    display: block;
    margin: 5px auto;
  }

  .product-card {
    width: 100%;
  }

  .product-card img {
    width: 100%;
    height: auto;
  }

  .products-btn {
    width: 80%;
    height: 40px;
    margin: 20px auto;
    font-size: medium;
  }

  .products-btn a {
    font-size: medium;
  }
}
</style>
