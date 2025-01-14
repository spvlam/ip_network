<template lang="pug">
v-container.pa-0
  v-row.mt-5(justify='space-between')
    v-col
      v-breadcrumbs.text-sm(divider='/')
        v-breadcrumbs-item Products /
        v-breadcrumbs-item(:active='true') {{ name }}
      v-divider.mb-5.mt-5
      v-row.mt-20(justify='space-between' align='stretch')
        v-col(:cols='8' ).h-100
          v-row.h-200
            v-col(:cols="3").d-flex.flex-column.align-stretch.h-100
              v-responsive(style="height: 25%; border: 1px solid black; max-height:200px")
                v-img(:src='img_link' contain)
              v-responsive(style="height: 25%; border: 1px solid black; max-height:200px")
                v-img(:src='img_link' contain)
              v-responsive(style="height: 25%; border: 1px solid black; max-height:200px")
                v-img(:src='img_link' contain)
              v-responsive(style="height: 25%; border: 1px solid black; max-height:200px")
                v-img(:src='img_link' contain)
            v-col(:cols="9").h-100
              v-img(:src='img_link' style="padding-bottom: 21.2257% ; width: 100%; height: 100%; border: 1px solid black; max-height:800px" cover )
        v-col(:col='3' )
          v-card.h-100.d-flex.flex-column.align-center
            v-card-title {{ name }}
            v-card-subtitle.mt-4 ${{ price }}
            v-card-text.mt-3.mb-5 {{ description }}
            v-divider.mb-5
            v-row.w-50.align-center(justify='space-around')
              v-btn(icon='' @click="decrease")
                | -
              span {{ productCount }}
              v-btn(icon=''  @click="increase")
                | +
            v-btn.mt-10.w-50.mb-10.self-center(color='red' large='' @click="addTocart")
              | Add to Cart
          

</template>

<script >
import { addProductToCart } from '../../utils/api';
import { StoreEnum } from '../../utils/enum';
import { useAuthStorage } from '../../utils/authStore';
import { toast } from 'vue3-toastify';
export default {
  name: "ProductDetail",
  props: {
    name: {
      type: String,
      required: true
    },
    price: {
      type: Number,
      required: true
    },
    description: {
      type: String,
      required: true
    },
    img_link: {
      type: String,
      required: true
    },
    id: { type: Number },
    productCount: Number
  },
  methods: {
    decrease() {
      this.productCount--
    },
    increase() {
      this.productCount++
    },
    async addTocart() {
      let store = useAuthStorage()
      if (!store.isAuth) this.$router.push({ name: 'Login' })
      else {
        let res = await addProductToCart(Number(this.id), Number(localStorage.getItem(StoreEnum.user_id)), !Boolean(localStorage.getItem(StoreEnum.cart_id)), this.productCount)
        if (res.isError) {
          toast.error("some thing when wrong, try again")
        } else {
          toast.success("Product has been added to cart")
          localStorage.setItem(StoreEnum.cart_id,res.data)
        }
      }
    }
  },
  data() {
    return {
      productCount: 1
    };
  },
};
</script>

<style scoped></style>