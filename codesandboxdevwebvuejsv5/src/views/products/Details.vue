<template>
  <div class="container">
    <h1>Product {{this.stuffId}}</h1>
    <router-link to='/'>
      <span class="btn btn-primary">Home.</span>
    </router-link>
  </div>
</template>

<script>
/*eslint-disable */
export default {
  data() {
    return {
      
    };
  },
  created(){
    this.stuffId = this.$route.params.id;
  }
};
</script>