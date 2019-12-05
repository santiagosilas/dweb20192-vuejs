<template>
  <div class="">
    <NavbarSimple></NavbarSimple>
    <article>
      <slot />
    </article>
    <footer class="text-center">&copy; Stuffs</footer>
  </div>
</template>

<script>
import NavbarSimple from '@/components/common/NavbarSimple';
export default {
  components: {
    NavbarSimple
  }
}
</script>

<style>

</style>