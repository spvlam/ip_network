<script setup lang="js">
import { ref, onMounted } from 'vue'
import Banner from '../../components/product/Banner.vue';
import ProductList from '../../components/product/ProductList.vue'
import { getAllProduct } from '../../utils/api';
const items = ref([])
onMounted(() => {
    getAllProduct()
        .then(res => {
            items.value = res.data
        })
})
</script>

<template lang="pug">
v-container
    Banner 
    ProductList(title="THE NEW PRODUCTS" headerOption="Today's" :items="items")
    ProductList(title="THE OLDEST PRODUCTS" headerOption="Last Month" :items="items")
</template>