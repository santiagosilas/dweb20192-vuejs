<template>
  <SimpleLayoutPage>  
    <div class="container">
      <h1>Project {{this.project.name}}</h1>
      <img class="stuff-img" :src="this.project.image">
      <router-link to='/projects'>
        <span class="btn btn-primary">return</span>
      </router-link>
    </div>
  </SimpleLayoutPage>  
</template>

<script>
import SimpleLayoutPage from "@/components/layouts/SimpleLayout";
export default {
  components: {
    SimpleLayoutPage
  },    
  data() {
    return {
      project: {},
    };
  },
  async created(){
    let response = await this.$services.projects.getById(this.$route.params.id);
    this.project = response.data;
    console.log(this.project);
  }
};
</script>