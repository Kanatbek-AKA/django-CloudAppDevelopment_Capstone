"use strict";

const warn = document.getElementById("warnings");
const txt = document.querySelector("#warnText");
warn.addEventListener('click', (elem) => {
  elem.preventDefault();

  txt.innerText= "Hey, I am currently not yet finished this Bootstrap data-...";
  txt.style.color = "red";
  txt.style.fontWeight = "bold";


})
