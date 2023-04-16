<template>
  <nav class="flex items-center justify-between flex-wrap bg-purple-500 z-50 p-6 w-full fixed top-0">
    <!-- Logo and Brand Name -->
    <div class="flex items-center flex-shrink-0 text-white mr-6">
      <svg class="h-8 w-8 text-gold fill-current mr-2" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
        <path d="M10 12a2 2 0 100-4 2 2 0 000 4z"/>
        <path fill-rule="evenodd" clip-rule="evenodd" d="M4 0C1.79 0 0 1.79 0 4v12c0 2.21 1.79 4 4 4h12c2.21 0 4-1.79 4-4V4c0-2.21-1.79-4-4-4H4zm6 16a4 4 0 100-8 4 4 0 000 8z"/>
      </svg>
      <span class="font-semibold text-xl tracking-tight">Photography</span>
    </div>

    <!-- Search Button -->
    <div class="flex items-center flex-grow">
      <div class="w-full">
        <div class="relative text-gray-600">
          <input type="search" name="search" placeholder="Search" class="bg-white h-10 px-5 pr-10 rounded-full text-sm focus:outline-none">
          <button type="submit" class="absolute right-0 top-0 mt-3 mr-4">
            <svg class="h-4 w-4 fill-current" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20"><path d="M18.707 17.293l-5.42-5.42a7.5 7.5 0 10-1.414 1.414l5.42 5.42a1 1 0 001.414-1.414z"/></svg>
          </button>
        </div>
      </div>
    </div>

    <!-- Login Button -->
    <div class="text-lg">
   <router-link to="/login">Login</router-link>
<router-link to="/register">Register</router-link>

    </div>
  </nav>
      <nav class="flex items-center justify-between flex-wrap bg-purple-600 p-2 z-10 w-full fixed top-20">
      <div class="flex items-center flex-shrink-0 text-white mr-6">
        <span class="font-semibold text-xl tracking-tight">Categories:</span>
      </div>
      <div class="flex-grow">
        <div class="flex justify-center">
          <a href="#" class="block mt-4 lg:inline-block lg:mt-0 text-white hover:text-gold mr-4">Landscape</a>
          <a href="#" class="block mt-4 lg:inline-block lg:mt-0 text-white hover:text-gold mr-4">Portrait</a>
          <a href="#" class="block mt-4 lg:inline-block lg:mt-0 text-white hover:text-gold mr-4">Architecture</a>
          <a href="#" class="block mt-4 lg:inline-block lg:mt-0 text-white hover:text-gold">Travel</a>
        </div>
      </div>
    </nav>
</template>
