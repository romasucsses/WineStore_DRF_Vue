<template>
  <div class="navigation-menu">
    <nav>
      <div class="menu">
        <img class="logo-img" src="/public/shop/images/site-img/logo.png" />
        <ul :class="{ 'menu-open': isMenuOpen }">
          <li @click="closeMenu">
            <RouterLink :to="{ name: 'home' }">HOME</RouterLink>
          </li>
          <li @click="closeMenu">
            <RouterLink :to="{ name: 'shop' }">SHOP</RouterLink>
          </li>
          <li @click="closeMenu">
            <RouterLink :to="{ name: 'wine' }">WINE</RouterLink>
          </li>
          <li @click="closeMenu">
            <RouterLink :to="{ name: 'sparkling' }">SPARKLING</RouterLink>
          </li>
          <li @click="closeMenu">
            <RouterLink :to="{ name: 'login' }">MY ACCOUNT</RouterLink>
          </li>
          <li @click="closeMenu">
            <RouterLink :to="{ name: 'about_us' }">OUR STORY</RouterLink>
          </li>
          <li @click="closeMenu">
            <RouterLink :to="{ name: 'find_near_me' }">FIND NEAR ME</RouterLink>
          </li>
          <li @click="closeMenu">
            <RouterLink :to="{ name: 'contact_us' }">CONTACT US</RouterLink>
          </li>
        </ul>
        <div class="cart-acc-img">
          <RouterLink :to="{ name: 'cart' }"><a><img src="/public/shop/images/site-img/cart_.svg.png" /></a></RouterLink>
          <RouterLink :to="{ name: 'my_account' }"><a><img src="/public/shop/images/site-img/my-account.png" /></a>
          </RouterLink>
        </div>
        <button class="menu-toggle" @click="toggleMenu">☰</button>
      </div>
    </nav>
  </div>
</template>

<script>
export default {
  data() {
    return {
      isMenuOpen: false,
    };
  },
  methods: {
    toggleMenu() {
      this.isMenuOpen = !this.isMenuOpen;
    },
    closeMenu() {
      this.isMenuOpen = false;
    },
  },
};
</script>

<style scoped>

.navigation-menu nav .menu {
  display: flex;
  justify-content: space-between;
  align-items: center;
  height: 100px;
  padding: 0 20px;
  background-color: rgba(255, 255, 255, 0.9);
}

.navigation-menu nav ul {
  display: flex;
  list-style: none;
  margin: 0;
  padding: 0;
}

.navigation-menu nav li {
  margin: 0 15px;
}

.navigation-menu nav a {
  color: #483e3e;
  text-decoration: none;
  font-size: 16px;
  padding: 5px;
  border-radius: 4px;
}

.navigation-menu li a:hover {
  background-color: #483e3e;
  color: #FFFFFF;
}

.navigation-menu .logo-img {
  height: 80px;
  margin-right: 20px;
}

.navigation-menu .cart-acc-img {
  display: flex;
  align-items: center;
}

.navigation-menu .cart-acc-img a {
  margin-left: 15px;
}

.navigation-menu .cart-acc-img img {
  width: 30px;
  height: 30px;
  transition: transform 0.3s ease;
}

.navigation-menu .cart-acc-img img:hover {
  transform: scale(1.2);
}

.menu-toggle {
  display: none;
  background: none;
  border: none;
  font-size: 30px;
  cursor: pointer;
}

/* Responsive Design */
@media (max-width: 768px) {
  .navigation-menu{
    width: 100%;
  }
  .navigation-menu nav .menu {
    flex-direction: column;
    align-items: flex-start;
    
  }

  .navigation-menu nav ul {
    display: none;
    flex-direction: column;
    align-items: flex-start;
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(255, 255, 255, 0.9);
    padding: 20px;
    overflow-y: auto;
    z-index: 1000;
  }

  .navigation-menu nav ul.menu-open {
    display: flex;
  }

  .navigation-menu nav li {
    margin: 10px 0;
  }

  .navigation-menu .cart-acc-img {
    position: absolute;
    top: 10px;
    right: 20px;
    
  }

  .navigation-menu .cart-acc-img a {
    margin-left: 0;
    margin-bottom: 10px;
  }

  .menu-toggle {
    display: block;
    margin-left: auto;
    margin-top: -4%;
  }
}
</style>
