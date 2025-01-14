<template lang="pug">
v-container(fluid='' style='width: 80%;')
  v-row.mt-3
    v-form.d-flex.flex-column.text-base(style='width: 655px; min-width: 240px;')
      v-text-field.w-100(v-model='search' placeholder='Search')
        template(#prepend-inner='')
          v-img.object-contain(src='https://cdn.builder.io/api/v1/image/assets/TEMP/11409849ac006ed6f9e5b1c2f8f7e4774aac40768f61b429a0785a7d42b8aa70?placeholderIfAbsent=true&apiKey=d8afa7d77be34c1fa1a04b67e7e290a3' alt='Search Icon' width='24' height='24' contain='')
    v-row.d-flex.align-center.justify-end
      v-col(cols='auto')
        v-img.object-contain(src='https://cdn.builder.io/api/v1/image/assets/TEMP/b334a24ea7c547b0237cd82a262a777eb7bf4e693753f924437d153d307ae6f8?placeholderIfAbsent=true&apiKey=d8afa7d77be34c1fa1a04b67e7e290a3' alt='Navigation icon' width='52' height='52' contain='')
      v-col(cols='auto')
        v-img.object-contain.rounded-xl(src='https://cdn.builder.io/api/v1/image/assets/TEMP/1a02742d5397f950c7057b677944345b4de579bfb64b114f242272b9b61fb0c3?placeholderIfAbsent=true&apiKey=d8afa7d77be34c1fa1a04b67e7e290a3' alt='User profile' width='52' height='52' contain='' @click="logout()")
  v-row.d-flex.flex-wrap.justify-space-between.align-center.mt-11.mb-8
    h1.text-2xl.font-weight-medium {{ title }}
    v-container(v-if='showDashboard')
      v-btn.text-base.text-neutral-50(color='red' @click='addProduct')
        | Add new product
      v-main.mt-4(v-if='showForm')
        ProductAdd  
v-divider.border-opacity-25(:thickness='2' color='success')
v-container
  v-row(v-if='showDashboard').ml-15
    template(v-slot:default='')
      v-slide-item.ma-4(v-for='item in items' :key='item.name')
        ProductCard(:discount='item.discount' :price='item.price' :quantity='item.quantity' :img_link='item.img_link' :name='item.name')
v-container(v-if='!showDashboard' fluid='')
  v-table(density='compact')
    thead
      tr
        th.text-left
          | Order Id
        th.text-left
          | Order date
        th.text-left
          | Customer
        th.text-left
          | Amount
        th.text-left
          | Result
        th.text-left
          | Phone
    tbody
      tr(v-for='item in items' :key='item.name')
        td {{ item.id }}
        td {{ item.created_at }}
        td {{ item.name }}
        td {{ item.total_amount }}
        td {{ item.result }}
        td {{ item.receiver_phone }}

</template>

<script setup  >
import { ref } from 'vue';
import ProductCard from '../product/ProductCard.vue';
import ProductAdd from '../product/ProductAdd.vue';
const search = ref('');
const showForm = ref(false)
const addProduct = () => {
    showForm.value = !showForm.value
};
const logout = ()=>{
  localStorage.clear()
  window.location.href='/login'
}
defineProps({
    title: String,
    showDashboard: Boolean,
    headerOption: String,
    items: {
        type: Array,
        required: true,
    },
});
</script>