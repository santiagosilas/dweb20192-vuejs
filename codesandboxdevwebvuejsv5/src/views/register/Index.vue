<template>
  <SimpleLayoutPage>
    <div class="register">
        <div class="container py-5"><FormRegister /></div>
        <div class="container"><AlertRegister /></div>
        <div class="container"><TableRegister /></div>

    </div>
  </SimpleLayoutPage>
</template>

<script>
/*eslint-disable */
import SimpleLayoutPage from "@/layouts/SimpleLayout";
import FormRegister from "@/views/register/components/Form";
import TableRegister from "@/views/register/components/Table";
import AlertRegister from "@/views/register/components/Alert";
export default {
  components: {
    SimpleLayoutPage, FormRegister, TableRegister, AlertRegister
  },
  data() {
    return {

    };
  },
  methods: {

  },
  computed: {

  },
  watch: {

  }
};
</script>

<style scoped>

</style>