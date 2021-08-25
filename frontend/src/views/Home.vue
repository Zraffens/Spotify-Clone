<!-- @format -->

<template>
  <div class="home">
    <Greet @playAudio="emitApp" />
    <NormalPlaylists
      title="Made For You"
      subText="Get better Recommendations the more you listen"
      to="/"
      @playAudio="emitApp"
    />
    <NormalPlaylists title="Recently Played" />
  </div>
</template>

<style scoped>
main {
  background: rgb(14, 14, 14);
  margin-top: -7px;
  padding-top: 10px;
}
</style>

<script>
// @ is an alias to /src
import Navbar from "@/components/Navbar.vue";
import TopBar from "@/components/TopBar.vue";
import Greet from "@/components/Greet.vue";
import NormalPlaylists from "@/components/NormalPlaylists.vue";

export default {
  name: "Home",
  components: {
    Navbar,
    Greet,
    NormalPlaylists,
    TopBar,
  },
  methods: {
    emitApp(id, type) {
      this.$emit("playAudio", id, type);
    },
  },
};
</script>
