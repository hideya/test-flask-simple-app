
const loginForm = document.querySelector('form');
const loginButton = document.getElementById('login-button');
const loginSpinner = document.getElementById('login-spinner');
const loginText = document.querySelector('.login-text');

loginForm.addEventListener('submit', (e) => {
    loginButton.disabled = true;
    loginSpinner.classList.remove('d-none');
    loginText.textContent = 'Logging in...';
});
