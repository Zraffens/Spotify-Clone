<!-- @format -->

<template>
  <div>
    <PlaylistComponent @playAudio="emitApp" />
  </div>
</template>

<script>
import PlaylistComponent from "../components/PlaylistComponent.vue";

export default {
  name: "Playlist",
  components: {
    PlaylistComponent,
  },
  methods: {
    emitApp(id, type, songID) {
      this.$emit("playAudio", id, type, songID);
    },
  },
};
</script>
