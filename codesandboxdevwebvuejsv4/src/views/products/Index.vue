<template>
  <SimpleLayoutPage>
    <div class="container">
      <h1>{{welcome}}</h1>
      <p v-on:click="doSomething">Do something</p>
      <p @click="doSomething">Do something</p>

      <div v-if="type === 'A'">it's A</div>
      <div v-else-if="type === 'B'">it's B</div>
      <div v-else-if="type === 'C'">it's C</div>
      <div v-else>it's neither one</div>

      <div>{{ type === 'A' ? 'yes' : 'no' }}</div>

      <ProductsGrid :products="stuffs"/>
    </div>
  </SimpleLayoutPage>
</template>

<script>
import SimpleLayoutPage from "@/layouts/SimpleLayout";
import ProductsGrid from "@/views/products/components/ProductsGrid";

export default {
  components: {
    SimpleLayoutPage,
    ProductsGrid
  },
  data() {
    return {
      welcome: "Products Page",
      type: "A",
      stuffs: [
        {
          id: 41,
          name: "stuff 41",
          image: "/static/profile.jpg"
        },
        {
          id: 42,
          name: "stuff 42",
          image: "/static/profile.jpg"
        },
        {
          id: 43,
          name: "stuff 43",
          image: "/static/profile.jpg"
        }
      ]
    };
  },
  methods: {
    doSomething() {
      console.log("do something..");
    },
    stuffDetails(index) {
      const id = this.stuffs[index].id;

      this.$router.push({
        name: "ProductDetails",
        params: { id: id }
      });
    }
  },
  computed: {
    reversedMessage: function() {
      return this.message
        .split("")
        .reverse()
        .join("");
    }
  },
  watch: {},

  /********************
   ** Lifecycle Hooks **
   *********************/
  beforeCreate() {
    // called before the app is created
  },
  created() {
    // called after the app is created
  },
  beforeMount() {
    // called before the app is mounted on the DOM
  },
  mounted() {
    // called after the app is mounted on the DOM
  },
  beforeUpdate() {
    // called before a property is updated
  },
  updated() {
    // called after a property is updated
  }
};
</script>

<style>
.stuff-img {
  width: 50px;
  height: 50px;
}
</style>