<template>
  <SimpleLayoutPage>
    <div class="container">
        <h6>Vue Tags Input</h6>

        <vue-tags-input
        v-model="tag"
        :tags="tags"
        :autocomplete-items="filteredItems"
        @tags-changed="newTags => {tags = newTags; }"
        />
        
        <ul>
          <li  v-for="tag in tags" :key="tag.id">
            {{tag.text}}
          </li>
        </ul>


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
      autocompleteItems: [
          { id: 1, text: 'Futebol' },
          { id: 2, text: 'Filosofia' },
          { id: 3, text: 'Finanças' },
          { id: 4, text: 'Esporte' },
          { id: 5, text: 'Praia' },
          { id: 6, text: 'Canoa Quebrada' },
          { id: 7, text: 'Aracati' },
        ],
    };
  },
  computed: {
    filteredItems() {
      return this.autocompleteItems.filter(item => {
        // texto em minúsculas
        let text = item.text.toLowerCase();
        let tag_name = this.tag.toLowerCase();
        return text.indexOf(tag_name) !== -1; // -1 quando não há a substring na string
      });
    },
  },
  methods: {
    save(){
      this.$toast("Alterações salvas com sucesso!");
    },
    AboutMe: function() {
      this.$router.push("/about");
    }
  },
  mounted(){
    this.tags.push( { id: 1, text: 'Futebol' });
  }
};
</script>

<style scoped>
div.background-image {
  height: 200px;
  background-repeat: no-repeat;
}
</style>