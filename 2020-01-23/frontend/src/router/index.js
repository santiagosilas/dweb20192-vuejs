import Vue from 'vue'
import Router from 'vue-router'

import Home from "@/views/home/Index";
import About from "@/views/about/Index";
import Projects from "@/views/projects/Index";
import ProjectDetails from "@/views/projects/Details";

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: "/",
      name: "Home",
      component: Home
    },
    {
      path: "/about",
      name: "About",
      component: About
    },   
    {
      path: "/projects",
      name: "Projects",
      component: Projects
    },
    {
      path: "/projects/details/:id",
      name: "ProjectDetails",
      component: ProjectDetails
    }     
  ]
})
