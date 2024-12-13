
const loginForm = document.querySelector('form');
const loginButton = document.getElementById('login-button');
const loginSpinner = document.getElementById('login-spinner');

loginForm.addEventListener('submit', (e) => {
    loginButton.disabled = true;
    loginSpinner.classList.remove('d-none');
});
