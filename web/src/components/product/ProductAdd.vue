<template lang="pug">
form()
    v-text-field(v-model='name.value.value' :counter='10'  label='name')
    v-text-field(v-model='quantity.value.value' :counter='7' :error-messages='quantity.errorMessage.value' label='quantity')
    v-text-field(v-model='price.value.value' :counter='7' :error-messages='quantity.errorMessage.value' label='price')
    v-file-input( v-model='file', clearable='' label='File input' variant='solo-inverted')
    v-text-field(v-model='description.value.value' label='description')
    v-text-field(v-model='discount.value.value' label='discount')
    v-btn.me-4(@click='submitButton')
        | submit
    v-btn(@click='handleReset')
        | clear
</template>
<script setup  >
import { ref } from 'vue'
import { useField, useForm } from 'vee-validate'
import { uploadProduct } from '../../utils/api';
import { toast } from 'vue3-toastify';
const { handleReset } = useForm({
    validationSchema: {
        quantity(value) {
            if (/[0-9-]+/.test(value)) return true
            return 'Must be the number'
        },
        select(value) {
            if (value) return true
            return 'Select an item.'
        },
    },
})
const name = useField('name')
const quantity = useField('quantity')
const description = useField('description')
const price = useField('price')
const discount = useField('discount')
const file = ref(null)
const submitButton = async () => {
    try {
    const formData = new FormData()
    formData.append('product_data', JSON.stringify({
        "name": name.value.value,
        "quantity": quantity.value.value,
        "price": price.value.value,
        "description": description.value.value,
        "discount": discount.value.value,
    }));
    formData.append('image', file.value)
    let res = await uploadProduct(formData)
    if(res.ok){
        window.location.href='/admin'
    }
    } catch (error) {
        toast.error(error)
    }
   
}
</script>