 
<template>
  <SimpleLayoutPage>
    <div class="container">
      <h1>{{ info }}</h1>
      <img src="../../assets/logo.png">
      <img src="/static/profile.jpg">
      <br>
      <router-link to="/about">
        <span>About me</span>
      </router-link>
      <br>
      <router-link :to="{name: 'About'}">
        <span>About me</span>
      </router-link>
      <br>
      <a href="#" @click="AboutMe">About me</a>
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
      info: "Home",
      ages: [1, 2, 3]
    };
  },
  methods: {
    AboutMe: function() {
      this.$router.push("/about");
    }
  },
  mounted(){
    this.$toast("Default toast");
    this.$toast.info("Info toast");
    this.$toast.success("Success toast");
    this.$toast.error("Error toast");
    this.$toast.warning("Warning toast");
  }
};
</script>

<style scoped>
</style>