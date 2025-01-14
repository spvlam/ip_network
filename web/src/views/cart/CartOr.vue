<script setup lang="js">
    import Cart from '../../components/cart/Cart.vue';
    import InvoiceInfor from '../../components/invoice/InvoiceInfor.vue';
    import { getCartDetail } from '../../utils/api';
    import { ref,onMounted } from 'vue';
    import { StoreEnum } from '../../utils/enum';
    
    const items = ref([])
    const user_name = ref('')
    const totalPrice = ref(0)
    onMounted(() => {
      user_name.value = localStorage.getItem(StoreEnum.user_name)
      getCartDetail(localStorage.getItem(StoreEnum.cart_id))
        .then(res => {
            items.value = res.data
            Array.from(res.data).forEach(item=>{
              totalPrice.value += item.price*item.quantity
            })
        })
    
})
</script>
<template lang="pug">
v-container.w-80
  Cart.mt-10.mb-10(:items="items")
  InvoiceInfor(invoice_title='ORDER INFORMATION' :user_name="user_name" :sub_price="totalPrice" :shipping_fee="totalPrice/10")
</template>