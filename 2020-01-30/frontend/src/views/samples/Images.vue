<template>
  <SimpleLayoutPage>
    <div class="container">
      <!-- Static path im img tag -->
      <img src="../../assets/logo.png">
      <img src="/static/profile.jpg">

      <!-- Binded path im img tag -->
      <img :src="logo">
      <img :src="profile">
      <img :src="fromweb">

      <!-- Binded path im div tag in css style -->
      <div 
        class="background-image" 
        v-bind:style="{ 'background-image': 'url(' + logo + ')' }">
        <h1>Texto</h1>
      </div>

      <div 
        class="background-image" 
        v-bind:style="{ 'background-image': 'url(' + profile + ')' }">
        <h1>Texto</h1>
      </div>

      <div 
        class="background-image" 
        v-bind:style="{ 'background-image': 'url(' + fromweb + ')' }">
        <h1>Texto</h1>
      </div>

      <br>
    </div>
  </SimpleLayoutPage>
</template>

<script>
import SimpleLayoutPage from "@/components/layouts/SimpleLayout";
export default {
  components: {
    SimpleLayoutPage
  },
  data() {
    return {
        logo: require("../../assets/logo.png"),
        profile: "/static/profile.jpg",
        fromweb: 'https://api.adorable.io/avatars/100/abott.png'
    };
  },
  methods: {
    AboutMe: function() {
      this.$router.push("/about");
    }
  }
};
</script>

<style scoped>
div.background-image {
  height: 200px;
  background-repeat: no-repeat;
}
</style>