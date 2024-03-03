<script setup>
  import NavMneu from './components/NavMenu.vue'
  import FooterMenu from './components/FooterMenu.vue'

  import { RouterView } from 'vue-router'
  import { useRoute } from 'vue-router'
  import { watch } from 'vue'

  const route = useRoute()
  console.log(route);
  watch(
    route, (to) => {
      document.title = to.meta.title
    },
    { immediate: true } // Trigger the watch immediately
  )

</script>

<template>
  <div>
      <NavMneu />
      <RouterView />
      <FooterMenu />
  </div>
  
</template>