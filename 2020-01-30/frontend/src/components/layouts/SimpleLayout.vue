<template>
  <div class="">
    <NavbarSimple></NavbarSimple>
    <slot />
  </div>
</template>

<script>
import NavbarSimple from '@/components/navbar/NavbarSimple';
export default {
  components: {
    NavbarSimple
  }
}
</script>

<style scoped>
</style>