<template>
  <div class>
    <NavbarSimple></NavbarSimple>
    <article>
      <slot/>
    </article>
    <footer class="text-center">&copy; Dev Web 2019.2</footer>
  </div>
</template>

<script>
import NavbarSimple from "@/components/common/NavbarSimple";
export default {
  components: {
    NavbarSimple
  }
};
</script>

<style scoped>
</style>