<script setup>
import { RouterLink, RouterView } from 'vue-router'
import VuexStore from './store/VuexStore'
import LogoutVue from './views/Logout.vue';
const auth=VuexStore.state.isAuth;
const isAuthenticated = localStorage.getItem('isAuth') === 'true';
</script>

<template>

<head>
  <!-- Basic -->
  <meta charset="utf-8" />
  <meta http-equiv="X-UA-Compatible" content="IE=edge" />
  <!-- Mobile Metas -->
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no" />
  <!-- Site Metas -->
  <link rel="icon" href="./assets/CT/images/fevicon.png" type="image/gif" />
  <meta name="keywords" content="" />
  <meta name="description" content="" />
  <meta name="author" content="" />

  <title>Empalsis</title>


  <!-- fonts style -->
  <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700;900&display=swap" rel="stylesheet">

</head>

<body>

  <div>
    <!-- header section strats -->
    <header class="header_section">
      <div class="container-fluid">
        <nav class="navbar navbar-expand-lg custom_nav-container ">
          <RouterLink class="navbar-brand" to="/">
            <span>Empalsis</span>
          </RouterLink>

          <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
            <span class=""> </span>
          </button>

          <div class="collapse navbar-collapse" id="navbarSupportedContent">
            <ul class="navbar-nav  ml-auto">
              <li class="nav-item active">
                <RouterLink class="nav-link active fa fa-home" to="/"> Home<span class="sr-only">(current)</span></RouterLink>
              </li>
              <li class="nav-item">
                <RouterLink class="nav-link active fa fa-user" to="/about"> About</RouterLink>
              </li>
              <li v-if="!auth" class="nav-item">
                <RouterLink class="nav-link active fa fa-user" to="/register"> Register</RouterLink>
              </li>
              <li v-if="!auth" class="nav-item">
                <RouterLink class="nav-link active fa fa-user" to="/login"> Login</RouterLink>
              </li>
              <li v-if="auth" class="nav-item">
                <RouterLink class="nav-link active fa fa-file" to="/details"> Details</RouterLink>
              </li>
              <li v-if="auth" class="nav-item">
                <RouterLink class="nav-link active fa fa-clone" to="/Upload"> Predict</RouterLink>
              </li>
              <li v-if="auth" class="nav-item">
                <LogoutVue></LogoutVue>
              </li>
            </ul>
            <div v-if="auth" class="quote_btn-container">
              <form class="form-inline">
                <button class="btn   nav_search-btn" type="submit">
                  <i class="fa fa-search" aria-hidden="true"></i>
                </button>
              </form>
              
            </div>
          </div>
        </nav>
      </div>
    </header>
    
  </div>
</body>

  <RouterView />
</template>

<style scoped>
 
 .navbar {
    background-color: #020230; /* Change this to the shade of blue you prefer */
}
.navbar li {
    list-style: none;
    display: inline;
    margin-right: 20px;
}

/* Style the links */
.navbar a {
    text-decoration: none;
    color: #ffffff; /* Default link color */
}

/* Add a hover effect */
.navbar a:hover {
    color: rgb(0, 102, 255); /* Change the color to red on hover */
    text-decoration: none; /* Underline the text on hover */
    background-color: rgb(0, 60, 255); /* Change background color on hover */
}
/* styles.css or within your component */
.custom-dropdown {
  z-index: 9999;
  position: absolute;
  top: 100%; /* Adjust this value as needed to align the dropdown properly */
  color: #020230;
  background-color: rgb(0, 60, 255);
}
</style>
