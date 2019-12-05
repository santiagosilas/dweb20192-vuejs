<template>
  <div id="app">
    <!-- The router uses this tag as a 
      container for rendering the different 
    components.
    It is the view where the components 
    are rendered-->
    <router-view/>
  </div>
</template>

<script>
// App.vue is the root component.
// All components in vue files,
// which allows us to save the template,
// javascript and styling into a single file.

// The Vue component object
export default {
  name: "App",
  components: {}
};
</script>

<style>
</style>
