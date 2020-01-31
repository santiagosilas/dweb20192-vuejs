<template>
  <SimpleLayoutPage>
    <div class="home">

    <div class="container py-5">
      <div class="row">
          <div class="offset-4 col-4">
              <form>
                <div class="form-group">
                  <label for="exampleInputEmail1">Email address</label>
                  <input 
                    type="email" 
                    value="Digite seu e-mail"
                    class="form-control" 
                    id="exampleInputEmail1" 
                    aria-describedby="emailHelp">
                  <small id="emailHelp" class="form-text text-muted">We'll never share your email with anyone else.</small>
                </div>
                <div class="form-group">
                  <label for="exampleInputPassword1">Password</label>
                  <input type="password" class="form-control" id="exampleInputPassword1">
                </div>
                <div class="form-group form-check">
                  <input type="checkbox" class="form-check-input" id="exampleCheck1">
                  <label class="form-check-label" for="exampleCheck1">Check me out</label>
                </div>
                <button type="submit" class="btn btn-primary">Submit</button>
              </form>
          </div>
      </div>
    </div>


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

.home img {
  height: 100px;
}
</style>