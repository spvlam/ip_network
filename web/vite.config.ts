import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import vuetify from 'vite-plugin-vuetify'
import * as path from "path";
// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    vue(),
    vuetify({ autoImport: true }), // Enabled by default
  ],
  resolve: {
    alias: {
      "@": path.resolve(__dirname, "src"),
    },
  },
 // accpect all network interface
 // vite only accept the connection inside the container or in the machine it's running
 // we need to binds all the network interface
  server: {
    host: '0.0.0.0',
    port: 3000,
  }
})
