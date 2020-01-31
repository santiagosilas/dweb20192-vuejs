<template>
    <table class="table">
    <thead class="thead-dark">
        <tr>
        <th scope="col">#</th>
        <th scope="col">Nome</th>
        <th scope="col">Email</th>
        </tr>
    </thead>
    <tbody>
        <tr>
        <th scope="row">1</th>
        <td>Mark</td>
        <td>otto@hotmail.com</td>
        </tr>
        <tr>
        <th scope="row">2</th>
        <td>Jacob@gmail.com</td>
        <td>thornton@gmail.com</td>
        </tr>
        <tr>
        <th scope="row">3</th>
        <td>Larry</td>
        <td>thebird@gmail.com</td>
        </tr>
    </tbody>
    </table>
</template>

<script>
/*eslint-disable */
import SimpleLayoutPage from "@/layouts/SimpleLayout";
export default {
  components: {
    SimpleLayoutPage
  },
  data() {
    return {
      profile: {
        email: 'fulano@gmail.com',
        password: '1234'
      }
    };
  },
  methods: {

  }
};
</script>

<style scoped>

</style>