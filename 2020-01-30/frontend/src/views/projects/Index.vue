<template>
<SimpleLayoutPage>  
  <div class="container">
    <h1>{{welcome}}</h1>
    <ProjectsGrid :projects="projects" />
  </div>
</SimpleLayoutPage>  
</template>

<script>
import SimpleLayoutPage from "@/components/layouts/SimpleLayout";
import ProjectsGrid from "@/views/projects/components/ProjectsGrid";
export default {
  components: {
    SimpleLayoutPage, ProjectsGrid
  },  
  
  data() {
    return {
      welcome: "Projects Page",
      type: "A",
      projects: []
    };
  },

  methods: {
    async loadProjects(){
      let new_project = {
        "name": "stuff 92",
        "image": "/static/profile.jpg"
      };

      let response_post = await this.$services.projects.post(new_project);
      console.log(response_post.data);

      let response_put = await this.$services.projects.put(response_post.data.id, {name: 'XXXX', image: "/static/profile.jpg"});
      
      let response_patch = await this.$services.projects.patch(response_post.data.id, {name: 'User Admin 37'});

      response_post = await this.$services.projects.post(new_project);
      console.log(response_post.data);

      let response_delete = await this.$services.projects.delete(response_post.data.id);


      let response_get = await this.$services.projects.getAll(`http://localhost:3000/projects`);
      this.projects = response_get.data;

      console.log(response_get);

    },
    doSomething() {
      console.log("do something..");
    },
    stuffDetails(index) {
      const id = this.projects[index].id;
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
  watch: {

  },
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
    this.loadProjects();
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