<template>
    <div class="alert alert-primary">
        
    </div>
</template>

<script>
/*eslint-disable */
export default {
  data() {
    return {

    };
  },
  methods: {

  },
  mounted() {
        
        
        this.$eventHub.$on('emitAlert', function (name) {
          console.log('An alert was emmited! ', this.message );
    });
  },
  watch: {
    message() {
      console.log('texto atualizado:', this.message);

    }
  },
};
</script>

<style scoped>

</style>