import Router from "vue-router";
import Home from "@/views/home/Index";
import About from "@/views/about/Index";
import Products from "@/views/products/Index";
import ProductDetails from "@/views/products/Details";

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
      path: "/products",
      name: "Products",
      component: Products
    },
    {
      path: "/products/details/:id",
      name: "ProductDetails",
      component: ProductDetails
    }
  ]
});
