<template lang="pug">
v-container.pa-0.bg-black(fluid)
  v-row.justify-space-between.custom-container.py-3.text-sm.bg-black.white--text
    v-col.justify-between
      v-row.justify-space-between
        v-col.d-flex.align-center(cols='auto')
          p.ma-0
            | Summer Sale For All Swim Suits And Free Express Delivery - OFF 50%!
          v-tab.font-weight-bold(to='/') ShopNow
        v-col.d-flex.align-center(cols='auto')
          p.ma-0 English
</template>

<style scoped>
.custom-container {
  max-width: 80%;
  margin: 0 auto;
}
</style>