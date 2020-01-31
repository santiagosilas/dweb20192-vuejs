<template>
  <div class="container">
    <div class="row">
      <div class="col-3" v-for="stuff in this.products" :key="stuff.id">
        <ProductCard 
          @emit-click="productDetails"
          :item="stuff"/>
      </div>
    </div>
  </div>
</template>

<script>
import ProductCard from "@/views/products/components/ProductCard";
export default {
  props: ["products"],
  components: {
    ProductCard
  },
  data() {
    return {};
  },
  methods: {
    productDetails(id){

      this.$router.push({
        name: "ProductDetails",
        params: { id: id }
      });

    }
  }
};
</script>