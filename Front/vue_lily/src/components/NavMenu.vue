<script setup>


</script>

<template>
  <div class="navigation-menu">
    <nav>
      <div class="menu">
        <ul>
          <img class="logo-img" src="/public/shop/images/site-img/logo.png" />
          <li><RouterLink :to="{name: 'home'}"><a>HOME</a></RouterLink></li>
          <li><RouterLink :to="{name: 'shop'}"><a>SHOP</a></RouterLink></li>
          <li><RouterLink :to="{name: 'wine'}"><a>WINE</a></RouterLink></li>
          <li><RouterLink :to="{name: 'sparkling'}"><a>SPARKLING</a></RouterLink></li>
          <li><RouterLink :to="{name: 'login'}"><a>MY ACCOUNT</a></RouterLink></li>
          <li><RouterLink :to="{name: 'about_us'}"><a>OUR STORY</a></RouterLink></li>
          <li><RouterLink :to="{name: 'find_near_me'}"><a>FIND NEAR ME</a></RouterLink></li>
          <li><RouterLink :to="{name: 'contact_us'}"><a>CONTACT US</a></RouterLink></li>
        </ul>
        <div class="cart-acc-img">
          <a href="{% url 'cart' %}"><img src="/public/shop/images/site-img/cart_.svg.png" /></a>
          <a href="{% url 'my_account' %}"><img src="/public/shop/images/site-img/my-account.png"/></a>
        </div>
      </div>
    </nav>
  </div>
</template>

<style scoped>
.navigation-menu nav .menu {
  display: flex;
  justify-content: space-between;
}

.navigation-menu nav ul {
  display: flex;
  list-style: none;
  margin: 0;
  padding: 0;
}

.navigation-menu nav li {
  margin-top: 35px;
  margin-right: 30px;
}

.navigation-menu nav a {
  color: #483e3e;
  text-decoration: none;
  font-size: 16px;
  /* background-color: #FFFFFF; */
  border-radius: 4px;
}

.navigation-menu li a:hover {
  background-color: #483e3e; 
  color: #ffffff;
  padding: 5px;
  border-radius: 8px;
}

.navigation-menu nav .logo-img {
  width: auto;
  height: 100px;
  margin-right: 20px;
}

.navigation-menu .cart-acc-img {
  margin-top: 23px;
  margin-right: 60px;
}

.navigation-menu .cart-acc-img img {
  width: 30px;
  height: 30px;
  padding: 10px;
}

.navigation-menu .cart-acc-img img:hover {
  width: 35px;
  height: 35px;
}
</style>
