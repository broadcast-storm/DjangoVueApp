import Vue from "vue";
import VueRouter from "vue-router";
import Main from "@/views/Main";
import LoginForm from "@/views/AuthViews/LoginForm";
import ForgotPassword from "@/views/AuthViews/ForgotPassword";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Main",
    component: Main
  },
  {
    path: "/auth",
    name: "Auth",
    component: () => import("@/views/Auth.vue"),
    children: [
      {
        path: "login",
        components: {
          "auth-router": LoginForm
        }
      },
      {
        path: "forgot-password",
        components: {
          "auth-router": ForgotPassword
        }
      }
    ]
  }
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes
});

export default router;
