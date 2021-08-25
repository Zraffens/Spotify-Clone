<!-- @format -->

<template>
  <div class="grid grid-3-1 topbar">
    <div id="left-right" class="flex">
      <button
        class="button"
        @click="hasHistory() ? $router.go(-1) : $router.push('/')"
      >
        <i class="fas fa-chevron-left"></i>
      </button>
      <button
        class="button"
        @click="hasHistory() ? $router.go(1) : $router.push('/')"
      >
        <i class="fas fa-chevron-right"></i>
      </button>
    </div>
    <div class="grid other-btns">
      <div>
        <button id="upgrade" class="button flex-1">UPgrade</button>
      </div>
      <div class="align-right">
        <button id="user" class="button flex-1">User</button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "TopBar",
  methods: {
    hasHistory() {
      return window.history.length > 2;
    },
  },
};
</script>

<style>
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

#upgrade {
  font-size: 1.1rem;
  padding: 0.8em 2.5em;
  border-radius: 1.7em;
}

#upgrade:hover {
  transform: scale(1.04);
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
</style>
