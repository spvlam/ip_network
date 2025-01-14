<script setup>
import ProductCard from '../../components/product/ProductCard.vue';

import { ref } from 'vue';
const model = ref(null);
defineProps({
  title: String,
  headerOption: String,
  items: {
    type: Array,
    required: true,
  },
});
</script>

<template lang="pug">
v-container.w-100.mt-10
  v-row
    v-col
      v-row.align-start
        v-col(cols="auto")
          v-sheet(width="25px" height="40px" color="red" rounded)
        v-col
          v-text(variant="h8" :style="{ color: 'red' }" )
            | {{ headerOption }}
      v-text.mt-3(variant="h1" style="font-weight: 600; font-size: 2rem;")
        | {{ title }}

  v-row
    v-sheet(elevation="3" width="100%")
          v-slide-group.w-full.d-flex.justify-between
            v-slide-item(v-for="item in items" :key="item.name" class="ma-4")
              ProductCard(:id="item.id" :discount="item.discount" :price="item.price"
                :quantity="item.quantity" :img_link="item.img_link" :name="item.name" :description="item.description")

</template>