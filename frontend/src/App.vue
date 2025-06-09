<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
import {useAuthStore} from "@/stores/AuthStore";

const authStore = useAuthStore()
const logout = async () => {
  await authStore.logout()
  window.location.reload();
}
</script>

<template>
  <header>

    <div class="wrapper">

      <nav>
        <RouterLink to="/">Home</RouterLink>
        <RouterLink to="/about">About</RouterLink>
        <button @click="logout" v-if="authStore.is_logged_in">Logout</button>
      </nav>
    </div>
  </header>

  <RouterView />
</template>
