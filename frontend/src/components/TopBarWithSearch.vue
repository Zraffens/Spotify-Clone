<!-- @format -->

<template>
  <div class="grid topbar">
    <div id="left-right" class="flex">
      <button class="button"><i class="fas fa-chevron-left"></i></button>
      <button class="button"><i class="fas fa-chevron-right"></i></button>
    </div>
    <div id="search-form" class="grid other-btns">
      <input
        type="text"
        name="keyword"
        id="search-keyword"
        @input="search"
        v-model="keyword"
        placeholder="Artists, songs, or podcasts"
      />
      <div class="align-right">
        <button id="user" class="button flex-1">User</button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "TopBarWithSearch",
  data() {
    return {
      keyword: this.$route.query.kw || "",
    };
  },
  methods: {
    search() {
      this.$emit("search", this.keyword);
      console.log("I'm trying");
      console.log("Hope it works");
    },
  },
};
</script>

<style scoped>
.topbar {
  grid-template-columns: 1fr 4fr;
}

#left-right button {
  font-size: 2rem;
  margin: 0.2em;
}

.other-btns button {
  background: black !important;
}

.other-btns {
  grid-template-columns: 1fr 1fr;
}

#user {
  padding: 0.4em;
  font-size: 1.3rem;
}

#user:hover {
  background: rgb(46, 46, 46);
}

#user {
  background: rgb(255, 255, 255, 0.2);
}

#search-keyword {
  background: white;
  border-radius: 50px;
  font-size: 1.7rem;
  color: rgb(1, 1, 1);
  padding: 0.7em;
  width: 80%;
}
</style>
