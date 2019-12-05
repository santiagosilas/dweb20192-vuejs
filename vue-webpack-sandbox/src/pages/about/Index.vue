<template>
  <div class="container">
    <h1>{{welcome}}</h1>
    <router-link :to="{ name: 'home' }">
      <span class="btn btn-primary">Home.</span>
    </router-link>    
  </div>
</template>

<script>
export default {
  data() {
    return {
      welcome: "About me."
    };
  }
};
</script>