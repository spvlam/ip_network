<template lang="pug">
v-table(height='300px' fixed-header='')
  thead
    tr
      th.text-center
        | Image
      th.text-left
        | Name
      th.text-left
        | Price
      th.text-left
        | Quantity
      th.text-left
        | Total price
  tbody
    tr(v-for='item in items' :key='item.name')
      td
        v-img(:src='item.img_link' alt='Header Image' max-height='40' )
      td {{ item.name }}
      td {{ item.price }}
      td {{ item.quantity }}
      td {{ item.price * item.quantity }}
</template>
<script lang="ts">
export default {
    props:{
      items:{
        type:Array
      }
    }
}
</script>