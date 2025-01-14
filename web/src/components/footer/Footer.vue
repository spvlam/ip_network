<template lang="pug">
v-footer.bg-black.text-neutral-50.py-20.mt-36
  v-row.justify-between.custom-container
    v-col(cols='12' md='3')
      h2.text-2xl.font-weight-bold.mb-6 Otani shop
      h3.text-xl.font-weight-medium.mb-6 Subscribe
      p.mb-6 Get 10% off your first order
      v-form
        v-text-field.bg-transparent(label='Enter your email' type='email' placeholder='Enter your email')
    v-col(cols='12' md='2')
      h3.text-xl.font-weight-medium.mb-6 Support
      ul.list-unstyled
        ol Flat 10, Prime building, Nguyen Du Street, Ha noi, VietNam
        ol otani@gmail.com
        ol 11111-88888-9999
    v-col(cols='12' md='2')
      h3.text-xl.font-weight-medium.mb-6 Account
      ul.list-unstyled
        ol My Account
        ol Login / Register
        ol Cart
        ol Wisholst
        ol Shop
    v-col(cols='12' md='2')
      h3.text-xl.font-weight-medium.mb-6 Quick Link
      ul.list-unstyled
        ol Privacy Poolcy
        ol Terms Of Use
        ol FAQ
        ol Contact
    v-col(cols='12' md='3')
      h3.text-xl.font-weight-medium.mb-6 Download App
      p.text-xs.mb-2 Save $3 with App New User Only
      v-row.align-center.justify-center.h-50
        v-img(
          src='web/src/assets/QR.png'
          alt='QR Code'
          cover
          :width="119"
          :height="119"
        )
        v-img(
          src='web/src/assets/google.png'
          alt='Google Play Store'
          max-width='150'
          class='mb-1'
        )
        v-img(
          src='web/src/assets/appStore.png'
          alt='Apple App Store'
          max-width='150'
        )
      v-row.mt-6
        v-col(cols='auto')
          v-img(src='web/src/assets/Face.svg' max-width='24' alt='Facebook')
        v-col(cols='auto')
          v-img(src='web/src/assets/twister.svg' max-width='24' alt='Twitter')
        v-col(cols='auto')
          v-img(src='web/src/assets/Insta.svg' max-width='24' alt='Instagram')
        v-col(cols='auto')
          v-img(src='web/src/assets/linkIn.svg' max-width='24' alt='LinkedIn')

</template>

<style scoped>
.custom-container {
  max-width: 80%;
  margin: 0 auto;
}
</style>

<script setup>
import qrImage from '@/assets/QR.png'
import googleImage from '@/assets/google.png'
import appStoreImage from '@/assets/appStore.png'
</script>