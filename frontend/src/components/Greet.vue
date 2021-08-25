<!-- @format -->

<template>
  <div id="parent-greet">
    <main>
      <h2 id="greeting">Good Evening</h2>
      <div class="grid grid-three">
        <router-link
          v-for="playlist in playlists"
          :key="playlist.id"
          :to="`/playlists/${playlist.id}`"
          class="playlist"
        >
          <div
            class="flex"
            :id="`q${playlist.id}`"
            @mouseover="onHoverG(`q${playlist.id}`)"
            @mouseleave="onLeaveG(`q${playlist.id}`)"
          >
            <img class="flex-1" :src="playlist.logo" alt="img" />
            <div class="flex-5">
              <h5 class="radio">{{ playlist.title }}</h5>
            </div>
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
        </router-link>
      </div>
    </main>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Greet",
  data() {
    return {
      playlists: {},
    };
  },
  methods: {
    onHoverG(index) {
      const button = document.querySelector(`#${index} button`);
      button.style.display = "inline-block";
    },

    onLeaveG(index) {
      const button = document.querySelector(`#${index} button`);
      button.style.display = "none";
    },
    playAudio(e) {
      e.preventDefault();
    },

    // play: (e, id) => {
    //   var vm = this.self;
    //   e.preventDefault();
    //   vm.$emit("play", id, "p");
    // },
  },
  created() {
    axios
      .get("http://localhost:8000/albums/playlists")
      .then((data) => (this.playlists = data.data));
    console.log(this.playlists);
  },
};
</script>

<style scoped>
#greeting {
  font-family: "montserrat";
}

img {
  width: 25%;
}

.playlist .flex {
  align-items: center;
  background: rgb(39, 39, 39);
  border-radius: 5px;
  padding-right: 0.6em;
  min-height: 60px;
}

.playlist img {
  height: 100%;
}

main .grid {
  gap: 1em;
}

h5.radio {
  margin: 0.5em;
}

.playlist div {
  transition: 0.2s;
}

.playlist div:hover {
  background: rgb(29, 29, 29);
}
</style>
