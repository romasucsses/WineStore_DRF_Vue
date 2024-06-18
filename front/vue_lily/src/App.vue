<script setup>
  import NavMenu from './components/NavMenu.vue'
  import FooterMenu from './components/FooterMenu.vue'
  import { RouterView } from 'vue-router'
</script>

<template>
  <NavMenu />
  <RouterView />
  <FooterMenu />
</template>

<!-- <style>
@media (max-width: 768px) {
  .max-width{
    max-width: 768px;
  }
}
</style> -->