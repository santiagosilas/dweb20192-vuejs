# vuejs-todo

## Instalação, criação e execução do projeto Vue.js

### verificar a instalação
~~~console
$ node -v
~~~
 
### atualizar o node
~~~console
$ sudo npm cache clean -f
$ sudo npm install -g n
$ sudo n stable
~~~

### resolver problemas na instalação do nodejs no ubuntu:
~~~console
$ sudo apt-get remove nodejs
$ sudo apt-get remove npm
$ sudo rm -rf ~/.npm
$ sudo rm -rf /usr/local/lib/node_modules
$ curl -0 -L https://npmjs.org/install.sh | sudo sh
~~~

# Atualizar todos os pacotes
~~~console
$ npm --depth=9999 upgrade
~~~

### instalar o CLI
~~~console
$ sudo npm install --global vue-cli ou
$ sudo npm install -g @vue/cli
~~~

 
### templates oficiais
~~~console
$ vue list
~~~
 
### Criar um projeto webpack
~~~console
$ vue init webpack todolist
~~~
 
### Para desenvolvimento 
~~~console
$ npm run dev
~~~
 
### Para produção
~~~console
$ npm run build
~~~
 
### Instalar as dependências do projeto
~~~console
$ npm install
~~~

### Instalar o vue-router
~~~console
npm install vue-router
~~~

### Instalar o Json-Server
~~~console
$ npm install -g json-server
~~~

### Executar o Json-Server
~~~console
$ json-server db.json (running on http://localhost:3000/planets)
~~~

### Instalar o Axios
~~~console
$ npm install axios --save
~~~

### Instalar e configurar o Bootstrap
~~~console
$ npm i bootstrap jquery popper.js 

//Em src/main.js:
import 'bootstrap'; import 'bootstrap/dist/css/bootstrap.min.css';
~~~

## Lifecycle Hooks
* beforeCreate called before the app is created
* created called after the app is created
* beforeMount called before the app is mounted on the DOM
* mounted called after the app is mounted on the DOM
* beforeDestroy called before the app is destroyed
* destroyed called after the app is destroyed
* beforeUpdate called before a property is updated
* updated called after a property is updated
* activated called when a kept-alive component is activated
* deactivated called when a kept-alive component is deactivated


### Hello World Vue.js
~~~html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Vue.JS</title>
</head>
<body>
    <!-- O Vue.JS funcionará dentro desta tag -->
    <div id="app">
        {{ titulo }}
    </div>
 
    <script src="https://cdn.jsdelivr.net/npm/vue"></script>
    
    <script>
    var app = new Vue({
        el: "#app", // Elemento pai da app
        data: {
            titulo: "Aula 01 - Vue.JS"
        }
    });
    </script>
</body>
</html>
~~~

### Estrutura do Projeto Vue.JS
~~~
-build/                              # Arquivos de configuração webpack
-config/                             # Arquivos de configuração do projeto
-node_modules/
-src/
    -assets/
    -components/              #componentes
            - HelloWorld.vue
    -router/
    -App.vue                       # Componente principal da aplicação
    -main.js                       # JS principal
-static/                           # arquivos estáticos
-test/
-.babelrc
-.editorconfig
-.gitignore
-.postcssrc.js
-index.html
-package-lock.json
-package.json               # arquivo de configuração de dependências 
-README.md

~~~

### Arquivos do Projeto: main.js e routes/index.js

**main.js**
~~~javascript
import Vue from 'vue'
import App from './App'
import router from './router'
 
Vue.config.productionTip = false
 
 
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
~~~

**App.vue**
~~~javascript
<template>
  <div id="app">
    <img src="./assets/logo.png">
    <router-view/>
  </div>
</template>
 
<script>
export default {
  name: 'App'
}
</script>
 
<style></style>
~~~

**HelloWorld.vue**
~~~javascript
<template>
  <h1>{{ msg }}</h1>
</template>
 
<script>
export default {
  name: 'HelloWorld',
 
  // data deve ser uma função que 
  // retorna os valores que o  
  // componente precisa
  data () {
    return {
      msg: '...'
    }
  }
}
</script>
 
<style></style>
~~~

**routes/index.js**
~~~javascript
import Vue from 'vue'
import Router from 'vue-router'
 
import HelloWorld from '@/components/HelloWorld'
 
Vue.use(Router)
 
export default new Router({
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    }

~~~

### Expressões
~~~javascript
{{ titulo }}
~~~

### Diretivas v-if, v-else, v-else-if
~~~javascript
<p v-if="status">{{ titulo }}</p>
<p v-else>{{status}}</p>
 
Habilita ou não a propriedade CSS display:none
<p v-show="status">{{ titulo }}</p>
~~~

### Diretiva v-for
~~~html
<tr v-for="pessoa in pessoas">
<td>{{pessoa.id}}</td>
<td>{{pessoa.nome}}</td>
<td>{{pessoa.profissao}}</td>
</tr>
 
<tr v-for="(pessoa, index) in pessoas">
</tr>
 
<tr v-for="(valor, chave) in objeto">
</tr>
 
<tr v-for="pessoa in pessoas": key=”pessoa.id”>
<td>{{pessoa.id}}</td>
<td>{{pessoa.nome}}</td>
<td>{{pessoa.profissao}}</td>
</tr>

~~~

### Binding
~~~javascript
one-way binding
<img v-bind:src="imagem" alt="">
<img :src="imagem" alt=""> 
~~~

### Slot
~~~javascript
// frame.vue
<template>
  <div class="frame">
    <slot></slot>
  </div>
</template>
~~~

~~~javascript
// app.vue
<template>
  <frame><img src="an-image.jpg"></frame>
</template>

~~~

### Página de Layout com Slot
~~~javascript
// Layout.vue
<template>
 <div class="">
   <NavbarSimple></NavbarSimple>
   <article>
     <slot />
   </article>
   <footer class="text-center">&copy; Stuffs</footer>
 </div>
</template>
~~~

~~~javascript
// Home.vue
<template>
 <LayoutPage>
   <div class="container">
     <div class="jumbotron">
       <h1>{{welcome}}</h1>
       <router-link to="/about">
         <span class="btn btn-secondary">About me.</span>
       </router-link>   
     </div>
   </div> 
 </LayoutPage>
</template>

<script>
import LayoutPage from '@/layout/SimpleLayout';
export default {
 components: {
   LayoutPage
 },

~~~


### Eventos
~~~javascript
<button class="btn btn-primary" v-on:click="enviar()">Enviar</button>
<button class="btn btn-primary" @click="enviar()">Enviar</button>
~~~

~~~javascript
methods: {
 enviar() {
   ... 
~~~

### Componentes
~~~javascript
// Em <template>:
<NavbarSimple></NavbarSimple>
~~~

~~~javascript
// Em <script>:
<script>
import NavbarSimple from '@/components/common/NavbarSimple';
export default {
 components: {
   NavbarSimple
 }
}
</script>
~~~

### Rotas com Vue.js
~~~javascript
// Em main.js
// Um sistema de rotas baseado em componentes
import VueRouter from 'vue-router';
Vue.use(VueRouter);
 
// Em App.vue
<div id="App">
    <router-view/>
</div>
~~~

### Router Link: Link de página em Vue.js
~~~html
<router-link to="/login"> <button>Login</button> </router-link>
 
<router-link class="btn btn-dark" :to="{name: 'About'}">
   <span>About me</span>
</router-link>
        
 
<a class="btn btn-dark" href="#" @click="AboutMe">About me</a>
~~~

~~~javascript
  methods: {
    AboutMe: function() {
      this.$router.push("/about");
    }
  }

~~~

### router.push
~~~html
<span @click="redirect('home')"><b>Home</b></span>
<span @click="redirect('sobre')"><b>About</b></span>
~~~

~~~javascript
methods:{
        redirect(path){
            if(path=='home') router.push('/')
            else router.push(`/${path}`)
        }
}
~~~

### Binding com v-model
~~~html
two-way binding for form inputs
<input type="text" class="form-control" id="nome" v-model="nome">
 
sincroniza o input após a mudança em algum evento
<input ... v-model.lazy="nome">
 
remove espaços antes e depois da string 
<input ... v-model.trim="nome">
~~~

### Comunicação entre componentes
* Pai para Filho:  **props**		
* Filho para pai:  **$emit**
~~~javascript
<!-- Componente Filho <menu-bar>-->  
Vue.component('menu-bar', {
    template:"#menu",
    // props: lista de propriedades
    // a propriedade items deve ser carregada com v-bind
    props: [
        // required: obrigatoriamente deve ser declarado items no uso
        // type: String | Array | Object | Boolean
        'items',
      ],
    methods: {
      emitClick(index) {
        this.$emit('emit-click', index)
      }
    }
  })
~~~

~~~javascript
<!-- Componente Pai -->    
Vue.component('navbar', {
    template:'#nav',
    data(){
      return {
        itemsNav: [{'label':'Products'}, {'label':'Categories'}]
      }
    },
    methods: {
      getLink(index) {
        alert(this.itemsNav[index].label)
      }
    }
  })
~~~

~~~html
<!-- Template do Componente Pai -->
<template id="nav">
<menu-bar v-bind:items="itemsNav" @emit-click="getLink"></menu-bar>
~~~


### Métodos
~~~javascript
methods: {
    getLink(index) { … }
}

~~~

### Propriedades Computed e Watch
~~~javascript
var app = new Vue({
    data: {
        nome: 'Fulano de Tal'
    },
    // semelhante a filtros
    computed: {
        toUpperCase() {
            return this.nome.toUpperCase()
        }
    },
    // para observar quando uma variável se altera
    watch: {
        nome(newValue, oldValue) {
            console.log(newValue)
        }
    }
});
~~~

### Mixin
~~~javascript
// componentes/mixins/getatt.js
export default {
  methods: {
    getattr (object, attr) {
      if (object) return object[attr]
      else return ''
    }
  }
}

~~~

~~~javascript
import getattr from '@/components/mixins/getattr';
…
export default {
    data() {
        return {
            ...
            }
        };
    },
    mixins: [getattr],
    ...
~~~

~~~javascript
getattr(dto,'valor')
~~~

### Classe de estilo dinâmicas
~~~javascript
<button class="btn" v-bind:class="btnClassLimpar" :style="btnStyleLimpar">Limpar</button>
~~~

~~~javascript
data: {
   btnClassLimpar: {
     'btn-danger': true,
     'btn-sm': true
   },
~~~

### Lifecycle Hooks
~~~javascript
beforeCreate() {
    console.log('1', this.message)
    console.log('el', this.$el)
  },
  
created() {
    // Neste ponto, tem-se acesso as variáveis
    console.log('2',this.message)
    console.log('el', this.$el) 
  },
  
beforeMount() {
    console.log('3', this.message)
    console.log('el', this.$el)
  },
  
mounted() {
    // Neste ponto, possui acesso ao DOM
    // Ex: neste ponto pode-se usar jQuery para alguma coisa ..
    console.log('4', this.message)
    console.log('el', this.$el)
  },
  
  
beforeUpdate(){
    console.log('5', this.message)
    console.log('el', this.$el)
  },
  
updated(){
    console.log('6', this.message)
    console.log('el', this.$el)
  },

~~~


### Filtros
~~~html
<input v-bind:value="firstPerson | toUpperCase()" />
<input v-bind:value="secondPerson | capitalize " />
~~~

~~~javascript
filters: {
  toUpperCase(str){
     return str.toUpperCase();
  },
  capitalize(){
   if(!value) return ''
   value = value.toString();
   return value.charAt(0).toUpperCase() + value.slice(1);                   
  }
},
~~~

### Integração com axios
~~~javascript
import axios from 'axios'
...

// get
axios.get(url);

// get by id
axios.get(`${url}/${id}`);

// post
axios.post(url, params);

// put
axios.put(`${url}/${id}`, params);

// patch
axios.patch(`${url}/${id}`, params);

// delete
axios.delete(`${url}/${id}`);
~~~


### Vue-Toastification
(Para exibição de feedback ao usuário)
https://www.npmjs.com/package/vue-toastification
npm install --save vue-toastification

Em main.js:
~~~javascript
import Toast from "vue-toastification";
import "vue-toastification/dist/index.css";
Vue.use(Toast, {});
~~~

Para utilizar:
~~~javascript
this.$toast("Default toast");
this.$toast.info("Info toast");
this.$toast.success("Success toast");
this.$toast.error("Error toast");
this.$toast.warning("Warning toast");
~~~


### Vue Tags Input
http://www.vue-tags-input.com/#/
npm install @johmun/vue-tags-input
~~~javascript
import VueTagsInput from '@johmun/vue-tags-input';
...
~~~


### Integração com fetch
~~~javascript

~~~

### Integração com axios
~~~javascript

~~~