<template>
  <SimpleLayoutPage>
    <div class="home">
    <div class="home-banner">

    </div>



      <h1>{{ info }}</h1>
      <div>
        teste <font-awesome-icon icon="user-secret" />
      </div>
      <img src="../../assets/logo.png">
      <img src="/static/profile.jpg">
      <div class="d-flex justify-content-around">
        <router-link class="btn btn-dark" to="/about">
          <span>About me</span>
        </router-link>
        
        <router-link class="btn btn-dark" :to="{name: 'About'}">
          <span>About me</span>
        </router-link>
        
        <a class="btn btn-dark" href="#" @click="AboutMe">About me</a>
      </div>
      <br>

    </div>
  </SimpleLayoutPage>
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
      info: "Home",
      ages: [1, 2, 3]
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
.home {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

.home .home-banner {
  background-image: url("../../assets/banner.jpg");
  background-color: #cccccc;
  height:200px;
  width: 100%;
}

.home img {
  height: 100px;
}
</style>