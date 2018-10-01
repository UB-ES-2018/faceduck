<template>
  <div id="HomePage">
    <div class="container">
      <div class="row">
        <div class="title col">
          <h1>Faceduck</h1>
        </div>
      </div>
      <div class="row" id="buttons">
          <div class="col"> 
            <button class="but_sign" href="/register">Register</button> 
            <button class="but_sign" href="/login">Log in</button>
          </div>
      </div>
    </div>
  </div>
</template>

<style lang="scss" scoped> 
#HomePage {
  background-color: #aaa;
  width: 50%;
  transform: translate(-50%, -50%);
  position: absolute;
  top: 50%;
  left: 50%;
  padding: 40px 0;
  border-radius: 10px;
}

.title {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #ffb511;
  text-shadow: 3px 3px #555;

  &>h1 {
    font-size: 450%;
    height: 150px;
    line-height: 150px;
  }
}

.but_sign {
  font-size: 100%;
 
  display: inline-block;
  padding: .4em 1.2em;
  border: .094em solid #ffb451;
  border-radius: .625em;
  background-color: #ffb511;
  box-shadow: 0 0.375em 0.313em -0.313em rgba(0, 0, 0, 0.8), inset 0 0.063em rgba(255, 255, 255, 0.4), inset 0 -0.15em rgba(0, 0, 0, 0.15);
  color: #FFF;
  text-decoration: none;
  text-transform: uppercase;
  text-shadow: 0 .063em #000;
  cursor: pointer;
  font: bold 1.8rem 'Avenir';

  &:not(last-child) {
    margin-right: 10px;
  }

  &:hover {
    background-color: #ffb516;
    box-shadow: 0 0.125em 0.05em -0.05em rgba(255, 255, 255, 0.4), inset 0 0.063em rgba(255, 255, 255, 0.4), inset 0 -0.15em rgba(0, 0, 0, 0.15);
  }
  &:active {
      box-shadow: inset 0 0 1.094em #ffb451, inset 0 0.063em #ffb351, inset 0 -0.188em #ffe451, 0 0.063em rgba(255, 255, 255, 0.4);
  }
}
</style>

