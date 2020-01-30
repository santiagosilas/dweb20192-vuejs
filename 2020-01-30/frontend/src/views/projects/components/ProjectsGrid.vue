<template>
  <div class="container">
    <div class="row">
      <div class="col-3 py-1" v-for="(project, index) in this.projects" :key="project.id">
        <div class="card" >
          <div class="card-body">
            <a @click="projectDetails(index)">
              <div class="d-flex justify-content-between align-self-center align-content-center">
                <div><span>{{project.name}}</span></div>
                <img class="stuff-img" :src="project.image">                
              </div>
            </a>            
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: [
    'projects'
  ],
  data() {
    return {};
  },
  methods: {
    projectDetails(index) {
      const id = this.projects[index].id;
      this.$router.push({
        name: "ProjectDetails",
        params: { id: id }
      });
    }
  },
};
</script>