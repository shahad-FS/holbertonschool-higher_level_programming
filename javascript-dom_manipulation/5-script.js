#!/usr/bin/node

const headerText = document.querySelector('header');

const updateHeader = document.querySelector('#update_header');

updateHeader.addEventListener('click', () => {
  updateHeader.textContent = 'New Header!!!';
});
