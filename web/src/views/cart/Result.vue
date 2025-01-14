<script setup lang="js">
    import InvoiceInfor from '../../components/invoice/InvoiceInfor.vue';
    import { useRoute } from 'vue-router'
    import { ref } from 'vue';
    import { onMounted } from 'vue';
    import { getOrderDetail } from '../../utils/api';
    import { StoreEnum } from '../../utils/enum';
    const route = useRoute()
    const order_id = ref(0)
    const result = ref('')
    const address=ref('')
    const phone=ref('')
    const shipping_fee =ref(0)
    const total_amount =ref(0)
    const user_name = ref('')
    onMounted(async ()=>{
        order_id.value = route.query.order_id
        result.value = route.query.result
        let orderDetail =await getOrderDetail(route.query.order_id)
        phone.value = orderDetail.receiver_phone
        total_amount.value = orderDetail.total_amount
        shipping_fee.value = orderDetail.shipping_fee
        user_name.value = localStorage.getItem(StoreEnum.user_name)
        address.value = orderDetail.order_ship_address
    })
</script>
<template lang="pug">
v-container
    InvoiceInfor(:result ="result" :user_name="user_name" :shipping_fee="shipping_fee" :sub_price = "total_amount-shipping_fee"  :addressResult="address" :phoneResult="phone" invoice_title="PAYMENT RESULT")
</template>