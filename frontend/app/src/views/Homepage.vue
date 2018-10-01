<template>
  <div id="HomePage">
    <div class='title'>
        <h1>FACEDUCK</h1>
    </div>

    <div id='buttons'>
        <button class='but_sign' href="/register">Register</button> 
        <button class='but_sign' href="/login">Log in</button>
    </div>
  </div>
</template>


<style lang="sass"> 
.title
  font-family: 'Avenir', Helvetica, Arial, sans-serif
  -webkit-font-smoothing: antialiased
  -moz-osx-font-smoothing: grayscale
  text-align: center
  background-color: #434547
  color: #ffb511
  font-size: 450%



.but_sign 
  
 
  font-size: 100%
   
  display: inline-block
  padding: .938em 1.875em
  border: .094em solid #ffb451
  border-radius: .625em
  background-color: #ffb511
  box-shadow: 0 0.375em 0.313em -0.313em rgba(0, 0, 0, 0.8), inset 0 0.063em rgba(255, 255, 255, 0.4), inset 0 -0.188em rgba(0, 0, 0, 0.15)
  color: #FFF
  text-decoration: none
  text-transform: uppercase
  text-shadow: 0 .063em #000
  cursor: pointer
  font: bold 1.8rem 'Avenir'
  &:hover
    background-color: #ffb516
    box-shadow: 0 0.125em rgba(255, 255, 255, 0.4), inset 0 0.063em rgba(255, 255, 255, 0.4), inset 0 -0.188em #ffb451
  &:active
    box-shadow: inset 0 0 1.094em #ffb451, inset 0 0.063em #ffb351, inset 0 -0.188em #ffe451, 0 0.063em rgba(255, 255, 255, 0.4)
</style>

