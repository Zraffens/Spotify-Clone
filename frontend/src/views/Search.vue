<!-- @format -->

<template>
  <div>
    <div id="top-div">
      <NormalPlaylists v-if="!$route.query.kw" title="Recently Searched" />
      <div
        @mouseover="onHoverTop(``)"
        @mouseleave="onLeaveTop(``)"
        v-if="topResult.id"
        class="top-result"
      >
        <div class="img-container">
          <img :src="`${topResult.logo}`" alt="" />
        </div>
        <h3 class="title">{{ topResult.title }}</h3>
        <span class="artist" v-if="topResult.artist">{{
          topResult.artistn
        }}</span>
        <span class="type" v-if="topResult.artist">Song</span>
        <span class="type" v-else-if="topResult.artists">Album</span>
        <span class="type" v-else-if="topResult.artistSongs">Artist</span>
        <button
          v-if="topResult.type === 'album'"
          class="button play flex-1"
          @click="$emit('playAudio', `${topResult.id}`, 'albums')"
          style="display: none;"
        >
          <i class="fas fa-play"></i>
        </button>
        <button
          v-else
          class="button play flex-1"
          @click="
            $emit(
              'playAudio',
              `${topResult.album}`,
              'albums',
              `${topResult.id}`
            )
          "
          style="display: none;"
        >
          <i class="fas fa-play"></i>
        </button>
      </div>
      <div v-if="data.songs.length > 0" class="songs">
        <h4>Songs</h4>
        <div
          class="song flex"
          v-for="song in data.songs"
          :key="song.id"
          :id="`a${song.id}`"
          @mouseover="onHover(`${song.id}`)"
          @mouseleave="onLeave(`${song.id}`)"
        >
          <div class="info flex-1 flex align-left">
            <img
              :src="song.logo"
              alt=""
              style="width: 100%;"
              class="song-img flex-1"
            />
            <button
              class="play-song"
              :id="`song${song.id}`"
              style="display: none;"
            >
              <i class="fas fa-play"></i>
            </button>
            <div class="flex titles">
              <div class="title flex-1">
                <h6>{{ song.title }}</h6>
                <p>{{ song.artistn }}</p>
              </div>
            </div>
          </div>
          <div class="other-btns flex flex-1 align-right">
            <div class="flex-1">
              <button
                @click="
                  song.liked
                    ? likeSong(song.id, true)
                    : likeSong(song.id, false)
                "
                class="love"
              >
                <i
                  :class="song.liked ? `fa liked fa-heart` : `fa fa-heart`"
                ></i>
              </button>
            </div>
            <div class="flex-2 duration">
              {{ intoMinutes(song.length) }}
            </div>
          </div>
        </div>
      </div>
      <div class="albums" v-if="data.albums.length > 0">
        <h3>Albums</h3>
        <div class="grid playlist-container" v-if="data.albums.length > 0">
          <router-link
            v-for="playlist in data.albums"
            :key="playlist.id"
            class="playlist-item"
            :to="`/albums/playlists/${id}`"
          >
            <div
              :id="`b${playlist.id}`"
              @mouseover="onHoverP(`${playlist.id}`)"
              @mouseleave="onLeaveP(`${playlist.id}`)"
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
              <h4 class="align-center">{{ playlist.title }}</h4>
              <p class="align-center">
                <span v-for="(artist, i) in playlist.artistn" :key="i">{{
                  artist
                }}</span>
              </p>
            </div>
          </router-link>
        </div>
      </div>
      <div class="artists" v-if="data.artists.length > 0">
        <h3>Artists</h3>
        <div class="grid playlist-container">
          <router-link
            v-for="playlist in data.artists"
            :key="playlist.id"
            class="playlist-item"
            :to="`/artists/${id}`"
          >
            <div
              :id="`a${playlist.id}`"
              @mouseover="onHoverA(`${playlist.id}`)"
              @mouseleave="onLeaveA(`${playlist.id}`)"
            >
              <div class="img-container">
                <img :src="playlist.logo" height="156px" alt="" />
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
              <h4 class="align-center">{{ playlist.title }}</h4>
            </div>
          </router-link>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import NormalPlaylists from "../components/NormalPlaylists.vue";
import axios from "axios";

export default {
  name: "Search",
  data() {
    return {
      keyword: this.$route.query.kw || "",
      data: { songs: [], albums: [], artists: [] },
      topResult: {},
    };
  },
  mounted() {
    // this.topResult = this.data.songs[0] || this.data.albums[0] || {};
  },
  methods: {
    async find() {
      const keyword = this.$route.query.kw;
      this.topResult = {};
      this.data = { songs: [], albums: [], artists: [] };
      if (keyword) {
        await axios
          .get(`http://localhost:8000/songs/filter/${keyword}`)
          .then((res) => {
            this.data.songs = res.data.map((i) => {
              return { ...i, type: "song" };
            });
            this.songAlbum = res.data.album;
          });
        await axios
          .get(`http://localhost:8000/albums/filter/${keyword}`)
          .then((res2) => {
            this.data.albums = res2.data.map((i) => {
              return { ...i, type: "album" };
            });
          });
        await axios
          .get(`http://localhost:8000/artists/filter/${keyword}`)
          .then((res2) => {
            this.data.artists = res2.data.map((i) => {
              console.log(i);
              return { ...i, type: "artist" };
            });
          });
      }
      this.topResult =
        this.data.songs[0] || this.data.albums[0] || this.data.artists[0] || {};
    },
    onHoverP(index) {
      const button = document.querySelector(`#b${index} button`);
      button.style.display = "inline-block";
    },

    onLeaveP(index) {
      const button = document.querySelector(`#b${index} button`);
      button.style.display = "none";
    },
    onHoverA(index) {
      const button = document.querySelector(`#a${index} button`);
      button.style.display = "inline-block";
    },

    onLeaveA(index) {
      const button = document.querySelector(`#a${index} button`);
      button.style.display = "none";
    },
    likeSong(id, likedSong) {
      console.log(id);
      let song;
      this.songs.forEach((item) => {
        if (item.id === id) {
          song = item;
        }
      });
      song.liked = !song.liked;
      axios.patch(`http://localhost:8000/songs/${id}/`, {
        liked: song.liked,
      });
    },
    onHoverTop(index) {
      const button = document.querySelector(`.top-result button`);
      button.style.display = "inline-block";
    },

    onLeaveTop(index) {
      const button = document.querySelector(`.top-result button`);
      button.style.display = "none";
    },
    onHover(index) {
      const img = document.querySelector(`#a${index} img`);
      img.style.opacity = 0.3;
      const button = document.querySelector(`#a${index} button`);
      button.style.display = "inline-block";
    },
    onLeave(index) {
      const img = document.querySelector(`#a${index} img`);
      img.style.opacity = 1;
      const button = document.getElementById(`#a${index} button`);
      button.style.display = "none";
    },
    intoMinutes(time) {
      let duration = Math.round(time); // rounding off the secs to the nearest value
      let minutes = duration > 60 ? Math.floor(duration / 60) : 0; // basic things to do to convert it into minutes and seconds
      let seconds = Math.round(duration % 60);
      return seconds > 9 ? `${minutes}:${seconds}` : `${minutes}:0${seconds}`; // just to make it look better e.g.: 1:05
    },
  },
  created() {
    this.$emit("search");
    if (this.$route.query.kw) {
      this.find();
      this.topResult = this.data.songs[0] || this.data.albums[0] || {};
    }
  },
  components: {
    NormalPlaylists,
  },
  watch: {
    $route(to, from) {
      let keyword = this.$route.query.kw;
      if (to.name === "Search") {
        this.find();
        this.topResult = this.data.songs[0] || this.data.albums[0] || {};
        setTimeout(
          () =>
            (this.topResult = this.data.songs[0] || this.data.albums[0] || {}),
          10000
        );
      }
    },
  },
};
</script>

<style>
#top-div {
  margin-top: 3rem;
}

h3,
h5,
h6,
p {
  margin-bottom: 0;
}

.top-result {
  width: 35%;
  background: rgb(30, 30, 30);
  padding: 2rem;
  border-radius: 5px;
  cursor: pointer;
  position: relative;
  transition: 0.2s;
}

.top-result:hover {
  background: rgb(20, 20, 20);
}

.top-result img {
  width: 100%;
}

.type {
  margin: 0 1rem;
}

.top-result .img-container {
  width: 30%;
}

.type {
  background: rgb(10, 10, 10);
  padding: 0.3em;
  border-radius: 10px;
}

.play {
  position: absolute;
  z-index: 2;
  bottom: 8%;
  right: 5%;
}

.songs {
  margin-top: 2rem;
}

.song:hover {
  background: rgb(36, 36, 36);
}

.info {
  width: 33%;
  position: relative;
}

.play-song {
  text-align: center;
  background: transparent;
  position: absolute;
  font-size: 10px;
  border: none;
  left: 0%;
  top: 10%;
  text-align: center;
  color: rgb(255, 255, 255, 0.8);
}

.songs .flex {
  align-items: center;
}

.flex.titles {
  flex: 10;
}

.info img {
  width: 100%;
  max-height: 40px;
  margin-right: 1em;
}

.albums,
.artists {
  margin-top: 5rem;
}

.albums .grid,
.artists .grid {
  grid-template-columns: repeat(5, 1fr);
  gap: 10px;
  align-items: center;
}

.playlist-item {
  padding: 20px;
  background: rgb(30, 30, 30);
}

.playlist-item button {
  position: absolute;
  bottom: 10%;
  right: 1%;
}

.playlist-item .img-container {
  position: relative;
}

.playlist-item:hover {
  background: rgb(20, 20, 20);
}

.albums img {
  width: 100%;
  border-radius: 5px;
}

.artists img {
  width: 100%;
  border-radius: 50%;
}
</style>
