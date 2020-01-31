<template>
        <form>
        <div class="form-row">
            <div class="form-group col-md-6">
            <label for="inputEmail4">Nome</label>
            <input type="text" class="form-control" id="name" v-model="name">
            </div>          
            <div class="form-group col-md-6">
            <label for="inputEmail4">Email</label>
            <input type="email" class="form-control" id="email" v-model="email">
            </div>
        </div>
        <div class="d-flex justify-content-between">
          <span />
          <button type="submit" class="btn btn-primary" @click="Add">Add</button>
        </div>
        </form>
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
      email: 'fulano@hotmail.com',
      name: 'Fulano de Tal'
    };
  },
  methods: {
    Add: function(){
      console.log('button click event Add');
      this.$eventHub.$emit('emitAlert', this.name);
    }
  },
  computed: {

  },
  watch: {
    name() {
      //console.log(this.name);
      // Emite um evento baseado no eventBus (submit)
      
    
    }
  },
  created() {

  },
  mounted(){

  },
  updated(){

  }  
};
</script>

<style scoped>

</style>