<template>
  <div class>
    <NavbarSimple></NavbarSimple>
    <article>
      <slot/>
    </article>
    <footer class="footer text-center bg-dark">
      <div class="py-2">
        &copy; Dev Web 2019.2
      </div>
    </footer>
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
.footer {
  margin-top:800px;
  left: 0;
  bottom: 0;
  width: 100%;
  color: white;
  text-align: center;
}
</style>