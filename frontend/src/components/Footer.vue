<template>
  <footer class="bg-gray-800 py-8">
    <div class="container mx-auto">
      <div class="flex flex-wrap">
        <!-- First row -->
        <div class="w-full md:w-1/3 px-4 mb-4 md:mb-0">
          <h3 class="text-lg font-bold text-white mb-2">Column 1</h3>
          <p class="text-gray-400">
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed blandit
            nulla tellus.
          </p>
        </div>
        <div class="w-full md:w-1/3 px-4 mb-4 md:mb-0">
          <h3 class="text-lg font-bold text-white mb-2">Column 2</h3>
          <p class="text-gray-400">
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed blandit
            nulla tellus.
          </p>
        </div>
        <div class="w-full md:w-1/3 px-4 mb-4 md:mb-0">
          <h3 class="text-lg font-bold text-white mb-2">Column 3</h3>
          <p class="text-gray-400">
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed blandit
            nulla tellus.
          </p>
        </div>
      </div>

      <!-- Second row -->
      <div
        class="bg-gray-700 w-full flex items-center justify-between flex-wrap h-20 -mb-[1rem]"
      >
        <div class="w-full md:w-1/3 px-4">
          <p class="text-gray-400">&copy; {{ currentYear }} My Website Name</p>
        </div>
        <div class="w-full md:w-1/3 px-4">
          <p class="text-gray-400 text-center md:text-right">
            All rights reserved
          </p>
        </div>
        <div class="w-full md:w-1/3 px-4">
          <p class="text-gray-400 text-center md:text-right">Privacy Policy</p>
        </div>
      </div>
    </div>
  </footer>
</template>

<script>
export default {
  data() {
    return {
      currentYear: new Date().getFullYear(),
    };
  },
};
</script>

<style>
/* Styles for the footer */
</style>
