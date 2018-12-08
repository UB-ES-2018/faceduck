<template>
<nav class="navbar">
  <div class="navbar-content">
    <router-link class="title" to="/wall">
      <h1>Faceduck</h1>
    </router-link>
    <SearchBar class="search-bar" v-bind:redirect="!searchPage" />
    
    <div class="mobile-menu dropdown">
      <button class="fas fa-bars"></button>
      <div>
        <ul class="main-menu">
          <router-link tag="li" to="/wall"><a>Wall</a></router-link>
          <router-link tag="li" to="/profile"><a><!--{{user.username}}-->My personal page</a></router-link>
        </ul>
        <div class="desktop-menu dropdown">
          <button class="desktop-button fas fa-bars"></button>
          <ul class="dropdown-content">
            <router-link tag="li" to="/login_logs"><a>Logs</a></router-link>
            <li><a v-on:click="logout">Log Out</a></li>
          </ul>
        </div>
      </div>
    </div>
    
  </div>
</nav>
</template>

<script>
import SearchBar from "./SearchBar.vue";

export default {
    name: "NavBar",
    data() {
        return {
            user: JSON.parse(localStorage.getItem("user")),
                searchPage: (this.$route.name === "search")
            }
        },
        methods: {
            logout: function() {
                localStorage.removeItem("access-token");
                localStorage.removeItem("user");
                this.$router.push("/");
            },
        },
        components: {
            SearchBar
        }
    }
</script>

<style lang="sass" scoped>
@import '../assets/global.sass';

// Navbar specific defaults
  
.navbar ul
  list-style-type: none
  margin: 0;
  padding: 0;
  
.navbar h1
  color: $accent3
  margin: 0
  
.navbar a, .navbar a:hover
  text-decoration: none
  
// Navbar layout
  
.navbar
  position: relative;
  width: 100%
  padding: 1rem 1rem;
  background-color: $accent2
  box-shadow: 0px 0px 8px 2px #00000099;
  
.navbar-content
  width: 100%
  margin: auto;
  display: flex;
  align-items: center;
  justify-content: flex-start;
  @media screen and (min-width: $break-large)
    width: 80%
    min-width: $break-large
  @media screen and (max-width: $break-small)
    justify-content: center
    flex-wrap: wrap
    align-items:center
    align-content: space-between
    min-height: 105px
   
// Title

.title
  font-family: "Avenir", Helvetica, Arial, sans-serif
  text-align: center
  color: #ffb511
  text-shadow: 3px 3px #555
  font-size: 25px
  
.title
  margin: 0
  margin-right: 2rem
  font-family: inherit;
  font-weight: 500;
  padding-top: 5px
  color: inherit
  @media screen and (max-width: $break-small)
    margin-right: auto
  
// Search bar
  
.search-bar
  min-width: 300px
  width: 30%
  margin-right: auto
  @media screen and (max-width: $break-small)
    margin-right: 0
    order: 10
    
// Menu
  
.main-menu
  display: flex
  flex-flow: row wrap
  align-items: center
  list-style-type: none
  margin: 0
  padding: 0
  @media screen and (max-width: $break-mid)
    display: flex
    flex-direction: column
    display: none
    
.main-menu a
  @media screen and (max-width: $break-mid)
    color: black;
    padding: 12px 16px;
    text-decoration: none;
    display: block;
    white-space: nowrap;
    
.main-menu a:hover
  @media screen and (max-width: $break-mid)
    background-color: #ddd;
    
.mobile-menu:hover .main-menu
  @media screen and (max-width: $break-mid)
    display: block;
    
.mobile-menu:hover > div
  @media screen and (max-width: $break-mid)
    display: block;
    
.main-menu li.router-link-exact-active
  @media screen and (min-width: $break-mid)
    color: inherit
    border-bottom: 2px solid $accent3;

.main-menu > li
  @media screen and (min-width: $break-mid)
    margin-right: 1em
    padding-left: 2px
    padding-right: 2px
    border-top: 2px solid transparent;
    border-bottom: 2px solid transparent;
    &:last-child
      margin-right: 0

.main-menu > li > a:hover
  color: black

.dropdown-content > li > a:hover
  color: black

.dropdown
  position: relative;
  display: inline-block;

.dropdown > button
  color: $accent3;
  padding: 8px;
  font-size: 20px;
  border: none;
  background-color: inherit
  border-radius: 0.2rem 0.2rem 0 0

.desktop-menu:hover > button
  @media screen and (min-width: $break-mid)
    background-color: $accent3;
    color: $accent2

.mobile-menu
  &:hover > button, &:active > button
    @media screen and (max-width: $break-mid)
      background-color: $accent3;
      color: $accent2

.desktop-menu
  &:hover .dropdown-content, &:active .dropdown-content
    @media screen and (min-width: $break-mid)
      display: block;
    
.mobile-menu
  &:hover .dropdown-content, &:active .dropdown-content
    @media screen and (max-width: $break-mid)
      display: block;

.mobile-menu a:hover
  @media screen and (max-width: $break-mid)
    background-color: #ddd;

.desktop-menu a:hover
  background-color: #ddd;

.mobile-menu
  display: flex
  flex-direction: row
  @media screen and (max-width: $break-mid)
    display: flex
    flex-direction: column

.mobile-menu > button
  display: none
  @media screen and (max-width: $break-mid)
    display: inline-block

.desktop-menu > button
  display: inline-block;
  @media screen and (min-width: $break-mid)
    margin-left: .5rem
  @media screen and (max-width: $break-mid)
    display: none

.desktop-menu
  @media screen and (max-width: $break-mid)
    position: relative
    width: 100%

.dropdown-content
  display: none;
  position: absolute;
  right: 0
  background-color: #f1f1f1;
  //min-width: 100px;
  box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
  z-index: 1;
  @media screen and (min-width: $break-mid)
    border-radius: .3rem 0 .3rem .3rem
    overflow: hidden
  @media screen and (max-width: $break-mid)
    position: relative
    width: 100%
  
.dropdown-content a
  color: black;
  padding: 12px 16px;
  display: block;
  white-space: nowrap;

.mobile-menu
  position: relative;
  display: inline-block;
  @media screen and (max-width: $break-small)
    margin-left: 2rem
  

.mobile-menu > div
  display: flex
  flex-direction: row
  @media screen and (max-width: $break-mid)
    display: none;
    position: absolute;
    right: 0
    background-color: #f1f1f1;
    //min-width: 100px;
    box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
    z-index: 1;
    border-radius: .4rem 0 .4rem .4rem
    overflow: hidden

.mobile-menu li
  @media screen and (max-width: $break-mid)
    position: relative
    width: 100%

</style>
