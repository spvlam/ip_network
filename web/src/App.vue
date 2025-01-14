<script setup lang="ts">
import { computed } from 'vue';
import { useRoute } from 'vue-router';
import Footer from './components/footer/Footer.vue';
import FixHeader from './components/header/FixHeader.vue';
import Header from './components/header/Header.vue';

const route = useRoute();
const showLayout = computed(() => {
  return route.name == 'Admin' || route.name =='AdminOrder';
});
</script>


<template>
  <v-app>
    <div v-if="!showLayout" >
      <FixHeader />
      <Header />
      <main class="flex-grow-1 w-full">
        <router-view v-slot="{ Component }">
          <transition name="scale" mode="out-in">
            <component :is="Component" />
          </transition>
        </router-view>
      </main>
      <Footer />
    </div>
    <div v-else>
      <router-view />
    </div>
  </v-app>
</template>


<style scoped></style>
