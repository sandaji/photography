<template>
  <form @submit.prevent="submitForm" class="max-w-md mx-auto mt-8">
    <div class="mb-4">
      <label for="username" class="block mb-2 text-sm font-bold text-gray-700">Username</label>
      <div class="relative rounded-md shadow-sm">
        <input 
          type="text" 
          id="username" 
          v-model="username" 
          class="form-input block w-full px-4 py-2 text-gray-700 placeholder-gray-400 border rounded-md focus:outline-none focus:ring-2 focus:ring-indigo-400 focus:border-transparent" 
          placeholder="Enter your username">
      </div>
    </div>
    <div class="mb-4">
      <label for="email" class="block mb-2 text-sm font-bold text-gray-700">Email</label>
      <div class="relative rounded-md shadow-sm">
        <input 
          type="email" 
          id="email" 
          v-model="email" 
          class="form-input block w-full px-4 py-2 text-gray-700 placeholder-gray-400 border rounded-md focus:outline-none focus:ring-2 focus:ring-indigo-400 focus:border-transparent" 
          placeholder="Enter your email">
      </div>
    </div>
        <div>
      <label for="is-admin">Is Admin</label>
      <input type="checkbox" id="is-admin" v-model="isAdmin">
    </div>
    <div class="mb-4">
      <label for="password" class="block mb-2 text-sm font-bold text-gray-700">Password</label>
      <div class="relative rounded-md shadow-sm">
        <input 
          type="password" 
          id="password" 
          v-model="password" 
          class="form-input block w-full px-4 py-2 text-gray-700 placeholder-gray-400 border rounded-md focus:outline-none focus:ring-2 focus:ring-indigo-400 focus:border-transparent" 
          placeholder="Enter your password">
        <div class="absolute inset-y-0 right-0 pr-3 flex items-center text-gray-400">
          <svg class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path 
              stroke-linecap="round" 
              stroke-linejoin="round" 
              stroke-width="2" 
              d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"></path>
            <path 
              stroke-linecap="round" 
              stroke-linejoin="round" 
              stroke-width="2" 
              d="M16 20c-.223-1.419-.776-2.649-1.599-3.602a8.002 8.002 0 01-2.437-5.047C12.15 5.82 10.12 4 8 4c-2.12 0-4.15 1.82-4.964 3.351A8.002 8.002 0 011 16c0 4.411 3.589 8 8 8s8-3.589 8-8z"></path>
          </svg>
        </div>
      </div>
    </div>
    <div class="flex items-center justify-between">
      <button type="submit" class="py-2 px-4 bg-indigo-500 text-white font-semibold rounded-lg shadow-md hover:bg-indigo-700 focus:outline-none">
        <i class=" fas fa-user-plus mr-2"></i> Register
      </button>
    </div>
  </form>
</template>

<script>
import { ref } from 'vue'
import axios from 'axios'

export default {
  setup() {
    const username = ref('')
    const email = ref('')
    const password = ref('')
    const isAdmin = ref(false)

    const submitForm = async () => {
      try {
        const response = await axios.post('http://localhost:8000/api/users/', {
          username: username.value,
          email: email.value,
          password: password.value,
          is_admin: isAdmin.value,
        })
        console.log(response.data)
      } catch (error) {
        console.error(error)
      }
    }

    return {
      username,
      email,
      password,
      isAdmin,
      submitForm,
    }
  },
}
</script>