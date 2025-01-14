<script setup lang="js" >
import AdminBar from '../../components/admin/AdminBar.vue';
import AdminBody from '../../components/admin/AdminBody.vue';
import { getAllProduct } from '../../utils/api';
import { ref, onMounted } from 'vue'
const items = ref([])

onMounted(async() => {
    let res = await getAllProduct()
    items.value = res.data
})
</script>
<template lang="pug">
v-main
    AdminBar
    AdminBody(
      :items="items"
      :showDashboard="true"
      title="Product Dashboard"
    )
</template>
