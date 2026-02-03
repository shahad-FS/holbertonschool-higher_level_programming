#!/usr/bin/node

const listClass = document.querySelector('.my_list');

const setItem = document.querySelector('#add_item');

setItem.addEventListener('click', () => {
  const newItem = document.createElement('li');
  newItem.textContent = 'Item';
  listClass.appendChild(newItem);
});
