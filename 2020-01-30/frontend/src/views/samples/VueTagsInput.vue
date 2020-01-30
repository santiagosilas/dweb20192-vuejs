<template>
  <SimpleLayoutPage>
    <div class="container">
        <h6>Vue Tags Input</h6>

        <vue-tags-input
        v-model="tag"
        :tags="tags"
        :autocomplete-items="filteredItems"
        @tags-changed="newTags => tags = newTags"
        />

    </div>
  </SimpleLayoutPage>
</template>

<script>
import SimpleLayoutPage from "@/components/layouts/SimpleLayout";
import VueTagsInput from '@johmun/vue-tags-input';

export default {
  components: {
    SimpleLayoutPage, VueTagsInput
  },
  data() {
    return {
      tag: '',
      tags: [],
      autocompleteItems: [{
        text: 'Spain',
      }, {
        text: 'France',
      }, {
        text: 'USA',
      }, {
        text: 'Germany',
      }, {
        text: 'China',
      }],
    };
  },
  methods: {
    AboutMe: function() {
      this.$router.push("/about");
    }
  }
};
</script>

<style scoped>
div.background-image {
  height: 200px;
  background-repeat: no-repeat;
}
</style>