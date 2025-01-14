import { defineStore } from 'pinia';
import { StoreEnum } from './enum';

export const useAuthStorage = defineStore('authStorage', {
  state: () => ({
    accessToken: localStorage.getItem(StoreEnum.accessToken) || null,
    refreshToken: localStorage.getItem(StoreEnum.refreshToken) || null
  }),
  getters: {
    isAuth: (state) => Boolean(state.accessToken || state.refreshToken)
  },
  actions: {
    updateToken(newToken: string, tokenType: StoreEnum) {
      if (tokenType === StoreEnum.accessToken) {
        this.accessToken = newToken;
        localStorage.setItem(StoreEnum.accessToken, newToken);
      } else if (tokenType === StoreEnum.refreshToken) {
        this.refreshToken = newToken;
        localStorage.setItem(StoreEnum.refreshToken, newToken);
      }
    },

    removeToken() {
      this.accessToken = null;
      this.refreshToken = null;
      localStorage.removeItem(StoreEnum.accessToken);
      localStorage.removeItem(StoreEnum.refreshToken);
    },
  }
});
