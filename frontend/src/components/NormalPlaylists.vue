<!-- @format -->

<template>
  <div class="playlist-component">
    <router-link v-if="to" :to="to" class="title-link"
      ><h2 id="page-title" class="montserrat">{{ title }}</h2></router-link
    >
    <h2 v-else id="page-title">{{ title }}</h2>
    <p class="subtext">{{ subText }}</p>
    <div class="grid playlist-container">
      <router-link
        v-for="playlist in playlists"
        :to="`/playlists/${playlist.id}`"
        :key="playlist.id"
        class="playlist-item"
      >
        <div
          :id="`${title.slice(0, 3)}${playlist.id}`"
          @mouseover="onHoverP(`${title.slice(0, 3)}${playlist.id}`)"
          @mouseleave="onLeaveP(`${title.slice(0, 3)}${playlist.id}`)"
        >
          <div class="img-container">
            <img :src="playlist.logo" alt="" />
            <button
              class="button play flex-1"
              @click="
                playAudio($event);
                $emit('playAudio', `${playlist.id}`, 'playlists');
              "
              style="display: none;"
            >
              <i class="fas fa-play"></i>
            </button>
          </div>
          <h3>{{ playlist.title }}</h3>
          <p>
            <span
              v-for="(artist, i) in artists[playlist.id].slice(0, 2)"
              :key="i"
              >{{ artist }}, </span
            >...
          </p>
        </div>
      </router-link>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "NormalPlaylists",
  props: ["title", "subText", "to"],
  data() {
    return {
      playlists: [],
      artists: {},
    };
  },
  created() {
    axios.get("http://localhost:8000/albums/playlists").then((data) => {
      let randomPlaylists = data.data
        .map((value) => ({ value, sort: Math.random() }))
        .sort((a, b) => a.sort - b.sort)
        .map(({ value }) => value)
        .slice(0, 5);
      console.log(randomPlaylists);
      console.log(data.data);
      data.data.forEach((playlist) => {
        let id = playlist.id;
        console.log(id);
        this.artists[`${id}`] = playlist.artistn;
        console.log(playlist.artistn);
      });
      this.playlists = randomPlaylists;
      console.log(this.playlists);
    });
  },
  methods: {
    // the following two functions integrate to make the play button appear when hovered over a playlist
    onHoverP(index) {
      const button = document.querySelector(`#${index} button`);
      button.style.display = "inline-block";
    },

    onLeaveP(index) {
      const button = document.querySelector(`#${index} button`);
      button.style.display = "none";
    },

    playAudio: (e) => e.preventDefault(),
  },
};
</script>

<style scoped>
.playlist-component {
  margin: 1rem 0;
}

.title-link:hover {
  text-decoration: underline;
}

p {
  margin: 0 !important;
}

#page-title {
  margin: 1em 0 0.1em 0;
}

img {
  width: 95%;
  border-radius: 6px;
}

.playlist-container {
  grid-template-columns: 1fr 1fr 1fr 1fr 1fr;
  gap: 1.5em;
}

.playlist-item {
  padding: 1em;
  border-radius: 5px;
  background: rgb(21, 21, 21);
  transition: 0.2s;
  text-align: center;
}

.playlist-item:hover {
  background: rgb(28, 28, 28);
}

.img-container {
  position: relative;
}

.play {
  position: absolute;
  z-index: 2;
  bottom: 8%;
  right: 5%;
}
</style>
