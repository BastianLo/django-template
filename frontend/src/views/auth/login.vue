<template>
  <h1>
    Melde dich mit deinem Account an
  </h1>
  <label for="email" class="block mb-2 text-sm font-medium text-white">
    Benutzername</label>
  <input type="text" v-model="username" name="username"/>

  <label for="password" >Passwort</label>
  <input type="password" v-model="password" name="password"/>
  <button type="submit"  @click="login">Anmelden</button>
</template>

<script setup lang="ts">

import {ref} from "vue";
import {useAuthStore} from "@/stores/AuthStore";
import {storeToRefs} from "pinia";
import router from "@/router";

let errorMessage = ref("");
let username = ref("")
let password = ref("")

let authStore = useAuthStore()
let {user} = storeToRefs(authStore)
authStore.get_valid_token()

let login = async () => {
  const response = await authStore.login(username.value, password.value)
  errorMessage.value = response.message;
  if (response.response.ok) {
    await router.push(authStore.returnUrl)
  }
}
</script>