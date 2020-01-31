<template>
  <div class="container">
    <h1>{{welcome}}</h1>
    
    <a v-bind:href="url">...</a>
    <a :href="url">...</a>
    
    <a v-on:click="doSomething">Do something</a>
    <a @click="doSomething">Do something</a>

    <div v-if="type === 'A'">
      it's A
    </div>
    <div v-else-if="type === 'B'">
      it's B
    </div>
    <div v-else-if="type === 'C'">
      it's C
    </div>
    <div v-else>
      it's neither one
    </div>
    <div>{{ type === 'A' ? 'yes' : 'no' }}</div>

    <div class="row">
      <div class="col-3" v-for="(stuff, index) in this.stuffs" :key="stuff.id">
        <a @click="stuffDetails(index)">
          <span>{{stuff.name}}</span>
          <img class="stuff-img" :src="stuff.image">
        </a>
      </div>
    </div>
    <router-link to="/about">
      <span class="btn btn-primary">About me.</span>
    </router-link>
  </div>
</template>

<script>
export default {
  data() {
    return {
      welcome: "Stuffs Page",
      url:'http://www.google.com',
      type: 'A',
      stuffs: [
        {
          id: 41,
          name: "stuff 41",
          image: "/stuffs/abott01.png"
        },
        {
          id: 42,
          name: "stuff 42",
          image: "/stuffs/abott02.png"
        },
        {
          id: 43,
          name: "stuff 43",
          image: "/stuffs/abott03.png"
        }
      ]
    };
  },
  methods: {
    doSomething(){
      
    },
    stuffDetails(index) {
      const id = this.stuffs[index].id;
      this.$router.push({
        name: "Stuff",
        params: { id: id }
      });
    }
  },
  computed: {
    reversedMessage: function () {
      return this.message.split('').reverse().join('')
    }
  },
  watch: {
    
  },
  

  beforeCreate() {
  
  },
  created(){
    
  },  
  beforeMount(){

  },
  mounted() {

  },
  beforeUpdate(){

  }, 
  updated(){

  }
};
</script>

<style>
.stuff-img {
  width: 50px;
  height: 50px;
}
</style>