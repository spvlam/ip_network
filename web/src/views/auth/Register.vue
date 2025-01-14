<template lang="pug">
v-container(
  class="d-flex flex-column custom-container align-center bg-white mt-10 mb-10"
  gap="10"
)
  v-col(cols="12" class="text-center")
    h1.text-h4.text-black CREATE YOUR ACCOUNT
  v-col(cols="12" class="mt-8")
    v-form
      v-text-field(
        v-model="formData.email"
        :rules="emailRules"
        id="email"
        label="Gmail"
        type="email"
        placeholder="example@gmail.com"
        outlined
        required
        class="mb-4"
      )
      v-text-field(
        v-model="formData.name"
        :rules="nameRules"
        id="name"
        label="name"
        type="text"
        placeholder="otani"
        outlined
        class="mb-4"
      )
      v-text-field(
        v-model="formData.password"
        :rules="emailRules"
        id="password"
        label="Password"
        type="password"
        placeholder="*************"
        outlined
        class="mb-6"
      )
      v-text-field(
        v-model="formData.rePass"
        :rules="emailRules"
        id="retypePass"
        label="retypePass"
        type="password"
        placeholder="*************"
        outlined
        class="mb-6"
      )
      v-btn(
        class="mt-6 mb-6 "
        color="zinc-800"
        @click="submitForm"
        dark
        block
      )
        | REGISTER
      v-divider(class="my-6 mb-6")
        | -----------------------Or------------------------
      v-row
        v-col(cols="12" class="text-center mt-6")
          p
            | Already have account ?
            v-btn(
              :href="'/login'"
              class="text-indigo-700"
            )
              | Login here
</template>
<script setup>
import { ref } from 'vue';
import { toast } from "vue3-toastify";
import { RegisterUser } from '../../utils/api';
const formData = ref({
  name: '',
  email: '',
  password:'',
  rePass:''
});
const submitForm = () => {
  if(formData.value.password != formData.value.rePass){
    toast.error("Passwords do not match",{autoClose:3000});
  }else{
    let res = RegisterUser(formData.value.email,formData.value.password,formData.value.name)
    if(!res.isError){
      window.location.href='/login'
    }
   
  }
}
</script>
<style scoped>
.custom-container {
max-width: 70%;
}
@media (max-width: 600px) {
.custom-container {
  max-width: 95%;
}
}
</style>