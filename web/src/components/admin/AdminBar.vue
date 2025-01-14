<template lang="pug">
v-navigation-drawer(:width='193')
  v-list-item(style='color: blue; height:150px') OTANI ADMIN
  v-divider
  v-list-item(link='' to='/admin' title='Product' style='color: blue; ' :style="{ color: selectedItem === 'Product' ? 'blue' : '' }" @click="selectItem('Product')")
  v-divider
  v-list-item(link='' to='/admins/orders' title='Order' :style="{ color: selectedItem === 'Order' ? 'blue' : '' }" @click="selectItem('Order')")
  v-divider
</template>

<script setup>
import { ref } from 'vue'

const selectedItem = ref('None')


function selectItem(item) {
  selectedItem.value = item
}
</script>