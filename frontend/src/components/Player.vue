<!-- @format -->

<template>
  <div id="parent" class="flex">
    <div class="song-details flex-1 flex">
      <img :src="albumLogo" class="img-container flex-2" />
      <div class="titles flex-5">
        <h5>{{ currentSong.title }}</h5>
        <p>{{ currentSong.artistn }}</p>
      </div>
      <div class="flex other-btns flex-3 align-left">
        <button @click="like" class="love">
          <i
            :class="currentSong.liked ? `fas fa-heart liked` : `fas fa-heart`"
          ></i>
        </button>
      </div>
    </div>

    <div id="player" class="flex-2">
      <audio
        id="music-player"
        :src="currentSong.file"
        @timeupdate="increaseSeek"
        @ended="repeat ? loop : next"
      >
        <!--http://localhost:8000/media/musics/Sushant_KC_-_Gulabi_Official_Lyric_Video.mp3 -->
      </audio>
      <div class="flex control-btns align-center">
        <div class="control flex-5 align-right">
          <button
            id="shuffle"
            @click="shuffle = !shuffle"
            :class="shuffle ? 'side-btn focus' : 'side-btn'"
          >
            <i class="fas fa-random"></i>
          </button>
          <button class="next-previous" @click="prev" id="previous">
            <i class="fas fa-step-backward"></i>
          </button>
        </div>
        <div class="control flex-1">
          <button @click="playOrPause" id="play-or-pause">
            <i
              :class="
                played ? `fas fa-pause play-pause` : `fas fa-play play-pause`
              "
            ></i>
          </button>
        </div>
        <div class="control flex-5 align-left">
          <button class="next-previous" @click="next" id="next">
            <i class="fas fa-step-forward"></i>
          </button>
          <button
            id="repeat"
            @click="repeat = !repeat"
            :class="repeat ? 'side-btn focus' : 'side-btn'"
          >
            <i class="fas fa-redo"></i>
          </button>
        </div>
      </div>
      {{ currentTime }}
      <input
        type="range"
        id="change-time"
        @change="changeTime"
        step="0.1"
        min="0"
        max="100"
        value="0"
        style="width: 80%;"
      />
      {{ duration }}
    </div>

    <div class="volume-and-stuffs flex flex-1">
      <i class="fas fa-volume-up flex-2 align-right"></i>
      <input
        class="flex-1"
        type="range"
        id="change-vol"
        @change="changeVol"
        step="0.005"
        min="0"
        max="1"
        value="1"
      />
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "Player",
  data() {
    return {
      player: document.getElementById("music-player"),
      played: true,
      duration: "0:00",
      currentTime: "0:00",
      changingTime: false,
      playlist: {},
      index: 0,
      currentSong: {},
      shuffle: false,
      repeat: false,
      albumLogo: "",
    };
  },
  props: ["type", "id", "songID"],
  async created() {
    this.starter();
    document.getElementById("change-time").value = 0;
  },
  mounted() {
    // just the first and basic things
    let player = document.getElementById("music-player");
    player.addEventListener("timeupdate", this.increaseSeek);
    player.controls = false;
    document.getElementById("change-time").value = 0;
    this.player = player;
    this.player.addEventListener("playing", this.increaseSeek);
    this.player.play();
  },
  methods: {
    // this gets the required song played
    async starter() {
      if (this.type === "liked") {
        await axios.get("http://localhost:8000/liked/").get(async (data) => {
          const songId = this.songID ? this.songID : data.data[this.index];
          let playlist = {
            title: "Liked Songs",
            songs: data.data,
            artistn: [],
          };
          data.data.forEach((song) => {
            playlist.artistn.push(song.artistn);
          });
          await axios
            .get(`http://localhost:8000/songs/${songId}`)
            .then((res) => {
              let song = res.data;
              this.duration = this.intoMinutes(song.length);
              this.currentSong = song;
              this.albumLogo = song.logo;
            });
        });
      } else {
        await axios
          .get(`http://localhost:8000/albums/${this.type}/${this.id}`) // getting the details of the playlist
          .then(async (res) => {
            this.playlist = res.data; // putting all the data into this variable
            const songId = this.songID
              ? this.songID
              : res.data.songs[this.index]; // this.index keeps track of the index and will help to get the proper id of the song
            console.log(res.data.songs);
            await axios
              .get(`http://localhost:8000/songs/${songId}`)
              .then((res1) => {
                let song = res1.data; // putting the details of the song in this variable
                this.duration = this.intoMinutes(song.length);
                this.currentSong = song;
                const albumID = res1.data.album;
                this.albumLogo = song.logo; // storing the url of the logo to display it in the player
              });
          });
      }
      setTimeout(() => {
        // this.player.pause()
        this.player.play(); // I have to do this because the audio tag won't load by the time this plays
      }, 1000);
    },

    async getSong(id) {
      if (this.type === "liked") {
        await axios.get("http://localhost:8000/liked/").get((data) => {
          const songId = this.songID ? this.songID : data.data[this.index];
          axios.get(`http://localhost:8000/songs/${songId}`).then((res) => {
            let song = res.data;
            this.duration = this.intoMinutes(song.length);
            this.currentSong = song;
            this.albumLogo = song.logo;
          });
        });
      } else {
        const songId = this.songID
          ? this.songID
          : this.playlist.songs[this.index];
        await axios
          .get(`http://localhost:8000/songs/${songId}`)
          .then(async (res1) => {
            let song = res1.data;
            await axios
              .get(`http://localhost:8000/artists/${song.artist}`)
              .then((res2) => {
                song.artist = res2.data.title;
              });
            this.currentSong = song;
            this.duration = this.intoMinutes(song.length);
            console.log("went through");
            const albumID = res1.data.album;
            await axios
              .get(`http://localhost:8000/albums/albums/${albumID}`)
              .then((res3) => {
                this.albumLogo = res3.data.logo;
              });
          });
      }
    },
    checkNavigator() {
      console.log("checked");
      console.log(Navigator);
      if ("mediaSession" in Navigator) {
        Navigator.mediaSession.metadata = new MediaMetadata({
          title: this.song.title,
          artist: this.song.artistn,
          album: this.song.album,
          artwork: this.albumLogo,
        });
      }
    },
    // this function converts the given secs into mins and secs

    intoMinutes(time) {
      let duration = Math.round(time); // rounding off the secs to the nearest value
      let minutes = duration > 60 ? Math.floor(duration / 60) : 0; // basic things to do to convert it into minutes and seconds
      let seconds = Math.round(duration % 60);
      return seconds > 9 ? `${minutes}:${seconds}` : `${minutes}:0${seconds}`; // just to make it look better e.g.: 1:05
    },
    playOrPause() {
      // this.player.load(); // this loads the element first in order to avoid the previous music to play
      const btn = document.getElementById("play-or-pause");
      const child = btn.firstChild;
      if (this.played) {
        this.player.pause();
      } else {
        this.player.play();
      }
      this.played = !this.played;
      this.checkNavigator();
    },
    changeVol() {
      this.player.volume = document.getElementById("change-vol").value;
    },
    changeTime() {
      this.player.removeEventListener("timeupdate", this.increaseSeek); // this removes the event listener because nothing worked
      this.changingTime = true;
      this.player.pause();
      let duration = document.getElementById("change-time").value;
      console.log(`${this.player.currentTime} before multiplying`);
      this.player.currentTime = (duration / 100) * this.player.duration; // updating the time by converting it into percentage
      // this.player.currentTime = duration * this.player.duration;
      console.log(`${this.player.currentTime} after multiplying`);
      this.currentTime = this.intoMinutes(this.player.currentTime); // converting the currenttime into minutes
      if (this.played) {
        this.player.play(); // maintaining the status quo
      }
      this.player.addEventListener("timeupdate", this.increaseSeek);
      this.changingTime = false;

      // music.currentTime = duration *
      // music.currentTime = duration * clickPercent(event)
    },
    increaseSeek() {
      if (!this.changingTime) {
        let currentTime = this.player.currentTime;
        let seeker = document.getElementById("change-time");
        seeker.value = (currentTime / this.currentSong.length) * 100; // basic math to make the seek go ahead
        this.currentTime = this.intoMinutes(this.player.currentTime);
      }
    },

    like() {
      console.log(this.id);
      this.currentSong.liked = !this.currentSong.liked;
      console.log(this.currentSong);
      axios.patch(`http://localhost:8000/songs/${this.currentSong.id}/`, {
        liked: this.currentSong.liked,
      });
    },

    async next() {
      this.player.pause();
      let songs = this.playlist.songs;
      // resetting everything
      document.getElementById("change-time").value = 0;
      this.player.currentTime = 0;

      // conditional to check if it is in shuffle or if it is the last song in the list

      if ((this.index + 1 === songs.length) & !this.shuffle) {
        this.index = 0;
      } else if (this.shuffle) {
        let index = this.index;
        while (this.index === index) {
          this.index = Math.floor(Math.random() * this.playlist.songs.length);
        }
      } else {
        this.index = this.index + 1;
      }

      // getting the song

      this.getSong(this.playlist.songs[this.index]);
      this.player.load();
      if (this.played) {
        setTimeout(() => {
          // this.player.pause()
          this.player.play(); // I have to do this because the audio tag won't load by the time this plays
        }, 2000);
      }
      navigator;
    },
    prev() {
      this.index =
        this.index === 0 ? this.playlist.songs.length - 1 : this.index - 1;
      this.getSong(this.playlist.songs[this.index]);
      this.player.load();
      if (this.played) {
        setTimeout(() => {
          // this.player.pause()
          this.player.play(); // I have to do this because the audio tag won't load by the time this plays
        }, 1000);
      }
    },
    loop: () => {
      this.player.loop = true;
      this.player.play();
    },
  },
  watch: {
    id: function(value) {
      console.log("changed");
      console.log(this.id);
      console.log(this);
      this.starter();
      setTimeout(() => {
        this.player.play();
      }, 1000);
      this.played = true;
    },
    songID: function(value) {
      console.log("changed");
      console.log(this.id);
      console.log(this);
      this.starter();
      setTimeout(() => {
        this.player.play();
      }, 1000);
      this.played = true;
    },
    type: function(value) {
      console.log("changed");
      console.log(this.id);
      console.log(this);
      this.starter();
      setTimeout(() => {
        this.player.play();
      }, 1000);
      this.played = true;
    },
  },
};
</script>

<style scoped>
.flex {
  align-items: center;
}

#parent {
  height: 9rem;
  width: 98vw;
  z-index: 10000;
  background: rgb(24, 24, 24);
}

button {
  cursor: auto;
  color: rgb(181, 181, 181);
}

button:hover {
  color: white;
}

.focus {
  color: #1db954;
}

.focus:hover {
  color: #21e666;
}

.fa,
.fas {
  -webkit-text-stroke: 0.7px black;
}

.fas:hover {
  -wekit-text-stroke: none;
}

#player {
  padding: 5px;
  box-sizing: border-box;
  text-align: center;
}

#shuffle i,
#repeat i {
  -webkit-text-stroke: 1px black;
  font-size: 1.3rem;
}

.songs {
  align-items: center;
}

h5,
p {
  margin-bottom: 0;
}

button {
  border: none;
}

.img-container {
  width: 65px;
  height: 65px;
  background: white;
}

.titles {
  margin-left: 1rem;
}

#play-or-pause {
  border-radius: 50%;
  padding: 0.6rem 1.1rem;
  background: white;
  transition: 0.02s;
  color: black;
}

#play-or-pause:hover {
  transform: scale(1.03);
}

.fa-play,
.fa-pause {
  -webkit-text-stroke: 0.8px white;
}

.control-btns {
  align-items: center;
}

.next-previous i {
  font-size: 1.7rem;
}

.side-btn {
  margin: 0 0.5em;
}

.fa-volume-up {
  font-size: 1.8rem;
}

.volume-and-stuffs input[type="range"] {
  width: 10%;
}

input[type="range"] {
  -webkit-appearance: none;
  margin: 10px 0;
}

input[type="range"]:focus {
  outline: none;
}

input[type="range"]::-webkit-slider-runnable-track {
  width: 100%;
  height: 5px;
  cursor: auto;
  transition: 0.1s;
  box-shadow: 0px 0px 0px #000000, 0px 0px 0px #0d0d0d;
  background: gray;
  border-radius: 25px;
  border: 0px solid #000101;
}

input[type="range"]::-webkit-slider-thumb {
  box-shadow: 0px 0px 0px #000000, 0px 0px 0px #0d0d0d;
  border: 0px solid #000000;
  height: 12.5px;
  width: 12.5px;
  border-radius: 50%;
  background: white;
  cursor: auto;
  -webkit-appearance: none;
  margin-top: -3.6px;
}

input[type="range"]::-moz-range-track {
  width: 100%;
  height: 12.8px;
  cursor: auto;
  animate: 0.2s;
  box-shadow: 0px 0px 0px #000000, 0px 0px 0px #0d0d0d;
  background: #1db954;
  border-radius: 25px;
  border: 0px solid black;
}
</style>
