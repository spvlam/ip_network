<script setup lang="js">
    import AdminBar from '../../components/admin/AdminBar.vue';
    import AdminBody from '../../components/admin/AdminBody.vue';
    import {ref, onMounted } from 'vue';
    import { getAllOrder } from '../../utils/api';
    const items = ref([])
    onMounted(async()=>{
        let res = await getAllOrder()
        items.value = res.data
    })
</script>
<template lang="pug">
v-main
    AdminBar
    AdminBody(:showDashboard=false title="Order Dashboard " :items="items")
</template>