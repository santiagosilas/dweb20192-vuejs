<template>
  <Layout>
      <div class="about">
        <h1>{{ info }}</h1>
          <router-link to="/">
            <span class="btn btn-primary">Home</span>
          </router-link>    
      </div> 
  </Layout>
</template>

<script>
import Layout from "@/layouts/SimpleLayout";
export default {
  components: {
    Layout
  },
  data() {
    return {
      info: "About Page",
      ages: [1, 2, 3]
    };
  }
};
</script>

<style scoped>
.about {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>