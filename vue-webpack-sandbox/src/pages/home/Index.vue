<template>
  <LayoutPage>
    <div class="container">
      <div class="jumbotron">
        <h1>{{welcome}}</h1>
        <router-link to="/about">
          <span class="btn btn-secondary">About me.</span>
        </router-link>    
      </div>
    </div>  
  </LayoutPage>
</template>

<script>
import LayoutPage from '@/layout/SimpleLayout';
export default {
  components: {
    LayoutPage
  },
  data() {
    return {
      welcome: "Welcome to the Vue.js Stuffs!",
      stuffs: [
        {
          id: 41,
          name: "stuff 41",
          image: "/stuffs/abott01.png"
        },
        {
          id: 42,
          name: "stuff 42",
          image: "/stuffs/abott02.png"
        },
        {
          id: 43,
          name: "stuff 43",
          image: "/stuffs/abott03.png"
        }
      ]
    };
  },
  methods: {
    stuffDetails(index) {
      const id = this.stuffs[index].id;
      this.$router.push({
        name: "Stuff",
        params: { id: id }
      });
    }
  }
};
</script>

<style>
.stuff-img {
  width: 50px;
  height: 50px;
}
</style>