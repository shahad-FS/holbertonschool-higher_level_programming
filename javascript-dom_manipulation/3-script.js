#!/usr/bin/node

const headerColor = document.querySelector('header');

const color = document.querySelector('#toggle_header');

color.addEventListener('click', () => {
  if (headerColor.classList.length === 0) {
    headerColor.classList.add('green');
  } else if (headerColor.classList.value.includes('green')) {
    headerColor.classList.replace('green', 'red');
  } else if (headerColor.classList.value.includes('red')) {
    headerColor.classList.replace('red', 'green');
  }
});
