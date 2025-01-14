import { createApp } from 'vue'
import './style.css'
import vuetify from './plugins/vuetify'
import router from './routes'
import { createPinia } from 'pinia'
import App from './App.vue'
import '@mdi/font/css/materialdesignicons.css'
import 'vue3-toastify/dist/index.css';
createApp(App)
    .use(createPinia())
    .use(vuetify)
    .use(router)
    .mount('#app')
