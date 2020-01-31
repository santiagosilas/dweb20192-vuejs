<template>
  <div class="product-card">
    <a @click="stuffDetails()">
      <span>{{item.name}}</span>
      <img class="stuff-img" :src="item.image">
    </a>
  </div>
</template>

<script>
/* eslint-disable */
export default {
  props: ["item"],
  data() {
    return {};
  },
  methods: {
    stuffDetails() {
      this.$emit('emit-click', this.item.id);
    }
  }
};
</script>