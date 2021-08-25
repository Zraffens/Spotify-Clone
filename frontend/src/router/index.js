/** @format */

import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/playlists/:id",
    name: "Playlist",
    component: () =>
      import(/* webpackChunkName: "Playlist" */ "../views/Playlist.vue"),
  },
  {
    path: "/albums/:id",
    name: "Album",
    component: () =>
      import(/* webpackChunkName: "Playlist" */ "../views/Playlist.vue"),
  },
  {
    path: "/search",
    name: "Search",
    component: () =>
      import(/* webpackChunkName: "Search" */ "../views/Search.vue"),
  },
  {
    path: "/search/:keyword",
    name: "SearchWithKeyword",
    component: () =>
      import(/* webpackChunkName: "Search" */ "../views/Search.vue"),
  },
  {
    path: "/liked",
    name: "Liked",
    component: () =>
      import(/* webpackChunkName: "LikedSongs" */ "../views/LikedSongs.vue"),
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
