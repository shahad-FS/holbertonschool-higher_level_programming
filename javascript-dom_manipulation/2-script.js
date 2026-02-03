#!/usr/bin/node

const headerColor = document.querySelector('header');

const setClass = document.querySelector('#red_header');

setClass.addEventListener('click', () => {
  headerColor.classList.add('red');
});
