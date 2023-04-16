<template>
  <div>
    <Navbar />
    <HomePage />
    <Footer />
    <!-- Your app content goes here -->
    <router-view></router-view>
  </div>
</template>

<script>
import Navbar from './components/Navbar.vue'
import Footer from './components/Footer.vue'
import HomePage from './pages/HomePage.vue'

export default {
  name: 'App',
  components: {
    Navbar,
    HomePage,Footer
  },
  // Other options and methods
}
</script>

