<template>
  <header>
    <nav class="navbar navbar-dark bg-dark">
          <router-link class="navbar-brand" to="/">
            <span>Home</span>
          </router-link>      
      <button
        class="navbar-toggler"
        type="button"
        data-toggle="collapse"
        data-target="#navbarNavAltMarkup"
        aria-controls="navbarNavAltMarkup"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
        <div class="navbar-nav">
          <router-link class="nav-item nav-link" to="/">
            <span>Home</span>
          </router-link>
         <router-link class="nav-item nav-link" to="/about">
            <span>About</span>
          </router-link>
         <router-link class="nav-item nav-link" to="/projects">
            <span>Projects</span>
          </router-link>   
        </div>
      </div>
    </nav>
  </header>
</template>

<script>
</script>

<style scoped>
</style>