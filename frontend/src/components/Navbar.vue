<!-- @format -->

<template>
  <div class="navbar">
    <div class="logo">
      <h2>Spotify</h2>
    </div>
    <ul class="nav-links-basics">
      <li id="home-link" class="focus">
        <router-link to="/" class="nav-link">Home</router-link>
      </li>
      <li id="search-link">
        <router-link to="/search" class="nav-link">Search</router-link>
      </li>
      <li id="library-link">
        <router-link to="/" class="nav-link">Your Library</router-link>
      </li>
    </ul>
    <ul class="nav-links-extra">
      <li id="liked-link">
        <router-link to="/liked" class="nav-link">Liked Songs</router-link>
      </li>
      <hr />
    </ul>
  </div>
</template>

<script>
export default {
  name: "Navbar",
  // Applyiing the focus rule
  mounted() {
    if (this.$router.currentRoute == "/search") {
      console.log(document.querySelector("#search-link"));
      document.querySelector("#search-link").classList.add("focus");
      document.querySelector("#home-link").classList.remove("focus");
    } else {
      document.querySelector("#home-link").classList.add("focus");
      document.querySelector("#search-link").classList.remove("focus");
    }
  },
  watch: {
    $route(to, from) {
      if (to.path === "/search") {
        document.querySelectorAll("li").forEach((item) => {
          item.classList.remove("focus");
        });
        document.querySelector("#search-link").classList.add("focus");
      } else if (to.path === "/liked") {
        document.querySelectorAll("li").forEach((item) => {
          item.classList.remove("focus");
        });
        document.querySelector("#liked-link").classList.add("focus");
      } else {
        document.querySelectorAll("li").forEach((item) => {
          item.classList.remove("focus");
        });
        document.querySelector("#home-link").classList.add("focus");
      }
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
}

.logo h2 {
  margin: 0.5em;
}

li {
  display: block;
  line-height: 16px;
  padding: 0.7em;
  letter-spacing: 0.07em;
  transition: 0.3s;
  margin-right: 1em;
}

li a {
  color: rgb(202, 202, 202);
  transition: 0.2s;
}

li a:hover {
  color: #fff;
}

.focus {
  color: #fff;
  font-weight: 700;
  background: rgb(255, 255, 255, 0.2);
}
</style>
