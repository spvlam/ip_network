<template lang="pug">
v-container.pa-0(fluid)
  v-row.custom-container.mt-5
    v-col.d-flex(cols="11").justify-space-between
      v-tab(to="/" class="text-h5 font-weight-bold" ) Otani Shop
      v-tab(to="/" class="text-body-1") Home
      v-tab(to="#" class="text-body-1") Contact
      v-tab(to="#" class="text-body-1") About
      v-tab.mr-15(to="/register" class="text-body-1") Sign Up
      v-row
        v-text-field(
          v-model="searchQuery"
          placeholder="What are you looking for?"
          class="mr-4 mb-30"
        )
    v-col(cols="1")
        v-btn.ml-7(
          v-if="!isLoggedIn"
          color="primary"
          href="/login"
        ) Login
        v-row(v-else class="align-custom")
          v-img(
            src="https://cdn.builder.io/api/v1/image/assets/TEMP/672599e150869a16f594af60644cc3ee3e7f64cf7ba2184498cb6a8008983e09?apiKey=d8afa7d77be34c1fa1a04b67e7e290a3",
            alt="cart-icon",
            max-width="32"
            class="mr-5 cursor-pointer"
            @click="navigateTo()"
          )
          v-avatar(
            image="https://gravatar.com/avatar/HASH",
            size="40"
              @click="logout()"
          )
  v-divider.mt-4
</template>
<script setup lang="ts">
import { ref, onMounted } from 'vue';
import { StoreEnum } from '../../utils/enum';
const searchQuery = ref('');
const isLoggedIn = ref(false);
import { useRouter } from 'vue-router';
const router = useRouter();
onMounted(() => {
  checkLoginStatus();
});

function checkLoginStatus() {
  isLoggedIn.value = Boolean(localStorage.getItem(StoreEnum.refreshToken));
}
function navigateTo() {
  router.push("/cartOrder");
}
const logout = () => {
  localStorage.clear()
  window.location.href = '/login'
}
</script>
<style scoped>
.custom-container {
  max-width: 80%;
  margin: 0 auto;
}

.align-custom {
  justify-content: end;
  align-items: center;
  margin-left: 13px;
  margin-bottom: 10px;

}
</style>