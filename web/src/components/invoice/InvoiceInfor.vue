<template lang="pug">
v-container.mt-16(max-width='80%')
  v-row
    v-col.text-center.mb-5
      v-typography.font-weight-bold.text-black(variant='h2')
        | {{ invoice_title }}
  v-card
    v-card-text
      v-list
        v-list-item.d-flex.flex-row
          v-list-item-content.text-base.text-black.mr-5
            | Receiver:
          v-list-item-content.text-base.text-black.mr-5 {{ user_name }}
        v-divider
        v-text-field(v-if='!result' v-model="formData.address" clearable='' label='Address' variant='outlined' )
        v-list-item.d-flex.flex-row(v-if='result')
          v-list-item-content.text-base.text-black.mr-5
            | Address:
          v-list-item-content.text-base.text-black.mr-5 {{ addressResult }}
        v-divider
        v-text-field(v-if='!result' v-model="formData.phone" clearable='' label='Phone' variant='outlined')
        v-list-item.d-flex.flex-row(v-if='result')
          v-list-item-content.text-base.text-black.mr-5
            | Phone:
          v-list-item-content.text-base.text-black.mr-5 {{ phoneResult }}
        v-divider
        v-list-item.d-flex.flex-row
          v-list-item-content.text-base.text-black.mr-5
            | Total Product Price:
          v-list-item-content.text-base.text-black.mr-5 {{ sub_price }}
        v-divider
        v-list-item.d-flex.flex-row
          v-list-item-content.text-base.text-black.mr-5
            | Shipping fee:
          v-list-item-content.text-base.text-black.mr-5 {{ shipping_fee }}
        v-divider
        v-list-item.d-flex.flex-row
          v-list-item-content.text-base.text-black.mr-5
            | Total Price:
          v-list-item-content.text-base.text-black.mr-5 {{ shipping_fee + sub_price }}
        v-divider
        v-list-item.d-flex.flex-row(v-if='result')
          v-list-item-content.text-base.text-black.mr-5
            | Payment Status:
          v-list-item-content.text-base.text-black.mr-5 {{ result }}
  v-row.mt-14
    v-col.d-flex.justify-center
      v-btn.rounded-lg.text-white(v-if='!result' color='red' large='' @click='payOrder')
        | Pay order
      v-btn.rounded-lg.text-white(v-if='result' color='red' large='' @click='goHome')
        | Back to Home

</template>

<script setup lang="ts">
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import { makePayment } from '../../utils/api';
import { StoreEnum } from '../../utils/enum';
const router = useRouter();
const formData = ref({
  address: '',
  phone: ''
});

const props = defineProps({
  invoice_title: String,
  user_name: String,
  sub_price: Number,
  shipping_fee: Number,
  result: String,
  addressResult:String,
  phoneResult:String,
})

function payOrder() {
  if(props.sub_price &&props.shipping_fee){ 
    makePayment(props.sub_price+props.shipping_fee,Number(localStorage.getItem(StoreEnum.cart_id)),formData.value.address,props.shipping_fee,formData.value.phone)
  }
}
function goHome() {
  router.push('/');
}
</script>
