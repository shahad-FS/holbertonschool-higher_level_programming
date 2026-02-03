#!/usr/bin/node

const charName = document.querySelector('#character');

fetch('https://swapi-api.alx-tools.com/api/people/5/?format=json')
  .then((response) => response.json())
  .then((data) => { charName.textContent = data.name; });
