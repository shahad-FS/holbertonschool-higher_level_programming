const header = document.body.querySelector('header');

const click = document.body.querySelector('#red_header');

click.addEventListener('click', () => {
    header.style.color = "#FF0000";
});
