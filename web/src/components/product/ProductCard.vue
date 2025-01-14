<template lang="pug">
v-card.border-box.border-2.border-gray-300.mb-5(class='min-w-[240px] w-[270px]  cursor: pointer;' @click="goToProductDetail")
  v-card-text.flex.overflow-hidden.gap-5.justify-between.items-start.px-3.pt-3.pb-9.w-full.rounded.bg-neutral-100(class='max-w-[270px]')
    .flex.items-start.text-xs.whitespace-nowrap.text-neutral-50(class='gap-3.5')
      v-chip.px-3.py-1.rounded(color='red' label='')
        | -{{ discount }}%
      v-img.object-contain.shrink-0.self-end.mt-6.max-w-full(:src='img_link' style='width: 208px; height: 148px; object-fit: cover;'  alt='S-Series Comfort Chair')
  v-divider(style='height: 4px; background-color: #000;') 
  v-card-subtitle.flex.flex-col.self-start.mt-4.text-base.font-medium.mb-5
    h3.text-black {{ name }}
    .flex(style=' display: flex; justify-content: space-between;')
      span(style='color: #c53030;') ${{ price }}
      span Quantity: {{ quantity }}
</template>

<script >
import { useRouter } from 'vue-router';
export default {
    props: {
        id: {
            type: Number,
            required: true
        },
        discount: {
            type: Number,
            required: true
        },
        name: {
            type: String,
            required: true
        },
        price: {
            type: Number,
            required: true
        },
        quantity:{
            type: Number,
            required: true
        },
        img_link: {
            type: String,
            required: true
        },
        description:{
            type: Number,
            required: true
        }
    },
    methods: {
    goToProductDetail() {
    const router = useRouter();
    this.$router.push({ name: 'ProductDetail',
    query: { 
        name: this.name,
        price:this.price, 
        description:this.description,
        img_link:this.img_link,
        id:this.id
    }});
    },
  },
}
</script>
