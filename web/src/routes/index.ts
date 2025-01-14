import { createRouter, createWebHistory, RouteRecordRaw } from "vue-router";
import Login from "../views/auth/Login.vue";
import Register from "../views/auth/Register.vue";
import ProductDetail from "../views/product/ProductDetail.vue";
import DashBoard from "../views/DashBoard/DashBoard.vue";
import CartOr from "../views/cart/CartOr.vue";
import Result from "../views/cart/Result.vue";
import DashBoardAdmin from "../views/admin/DashBoardAdmin.vue";
import DashBoardOrder from "../views/admin/DashBoardOrder.vue";
import { useAuthStorage } from "../utils/authStore";
import { StoreEnum } from "../utils/enum";
import { toast } from "vue3-toastify";
const routelist: RouteRecordRaw[] = [
  {
    path:'/',
    name:'Home',
    component:DashBoard
  },
    {
      path:'/login',
      name:'Login',
      component:Login,
      beforeEnter:()=>{
        const store = useAuthStorage()
        if(store.isAuth) return {name:'Home'}
      }
    },
    {
      path:'/register',
      name:'Register',
      component:Register,
      beforeEnter:()=>{
        const store = useAuthStorage()
        if(store.isAuth) return {name:'Home'}
      }
    },
    {
      path:'/productDetail/',
      name:'ProductDetail',
      component:ProductDetail,
      props:true
    },
    {
      path:'/cartOrder',
      name:'CartOrder',
      component:CartOr,
      beforeEnter:()=>{
        const store = useAuthStorage()
        if(!store.isAuth) return {name:'Login'}
      }
    },{
      path:'/result',
      name:'Result',
      component:Result
    }
    ,{
      path:'/admin',
      name:'Admin',
      component:DashBoardAdmin,
      beforeEnter:()=>{
        if(!localStorage.getItem(StoreEnum.role)){
            setInterval(()=>{
              toast.error("you are not a admin")
            },3000) 
            window.location.href='/'
        }
      }
    },
    {
      path:'/admins/orders',
      name:'AdminOrder',
      component:DashBoardOrder,
      beforeEnter:()=>{
        if(!localStorage.getItem(StoreEnum.role)){
            window.location.href='/'
        }
      }
    }
]

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: routelist
})
  
  
  export default router;