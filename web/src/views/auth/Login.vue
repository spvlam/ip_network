<template lang="pug">
v-container(
  class="d-flex flex-column custom-container align-center bg-white mt-10 mb-10"
  gap="10"
)
  v-col(cols="12" class="text-center")
    h1.text-h4.text-black LOG IN
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
        class="mb-4"
      )
      v-text-field(
        v-model="formData.password"
        :rules="passwordRules"
        id="password"
        label="Password"
        type="password"
        placeholder="*************"
        outlined
        class="mb-6"
      )
      v-checkbox(v-model="isAdmin" label="Is Admin")
      v-btn(
        class="mt-6 mb-6"
        color="zinc-800"
        dark
        block
        @click="onSubmit"
      )
        | LOG IN
      v-divider(class="my-6 mb-6")
        | -----------------------Or------------------------
      v-row
        v-col(cols="12" class="text-center mt-6")
          p
            | New to Otani shop ?
            v-btn(
              :href="'/register'"
              class="text-indigo-700"
            )
              | create an account here
   
</template>

<script setup>
import { login } from '../../utils/api';
import { ref } from 'vue';
import { StoreEnum } from '../../utils/enum';
import { useRouter } from 'vue-router';
import { toast } from 'vue3-toastify';

const router = useRouter()
const formData = ref({
  email: '',
  password:'',
});
const isAdmin = ref(false)
const onSubmit =async ()=>{
    
    let res =await login(formData.value.email,formData.value.password,isAdmin.value)
    if(res.isError){
      toast.error(res.error)
    }else{
      localStorage.setItem(StoreEnum.accessToken, res.data.access_token)
      localStorage.setItem(StoreEnum.refreshToken,res.data.refresh_token)
      localStorage.setItem(StoreEnum.user_id,res.data.id)
      localStorage.setItem(StoreEnum.user_name,res.data.name)
      localStorage.setItem(StoreEnum.role,isAdmin)
      if(isAdmin.value){
        window.location.href ='/admin'
      }else{
        window.location.href ='/'
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