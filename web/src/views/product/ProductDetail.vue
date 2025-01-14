<script setup >
import { useRoute } from 'vue-router'
import ProductDetail from '../../components/product/ProductDetail.vue';
import ProductList from '../../components/product/ProductList.vue';
import {ref,onMounted} from 'vue'
import { getAllProduct } from '../../utils/api';
const items = ref([])
const namePro =ref('') 
const price = ref('')
const description = ref('')
const img_link = ref('')
const id = ref(0)
const route = useRoute()
onMounted(() => {
    getAllProduct()
        .then(res => {
            items.value = res.data
        })
    namePro.value = route.query.name 
    price.value = route.query.price 
    description.value = route.query.description 
    img_link.value = route.query.img_link 
    id.value = route.query.id 
})
</script>


<template lang="pug">
v-container.pa-0(fluid='')
  v-row(justify='center')
    v-col.d-flex.flex-column.align-center(cols='12')
    ProductDetail(:name="namePro" :price="price" :description="description" :img_link="img_link" :id="id")
    v-divider.my-4
    ProductList.mb-5(title="RELATIVE PRODUCT" headerOption="Reletive product" :items="items")
</template>
