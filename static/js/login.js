
const loginForm = document.querySelector('form');
const loginButton = document.getElementById('login-button');
const loginSpinner = document.getElementById('login-spinner');
const loginText = document.querySelector('.login-text');

loginForm.addEventListener('submit', (e) => {
    loginButton.disabled = true;
    loginButton.classList.add('processing');
    loginSpinner.classList.remove('d-none');
    loginText.textContent = 'Logging in...';
});

// Reset form state if there's an error
window.addEventListener('load', () => {
    loginButton.disabled = false;
    loginButton.classList.remove('processing');
    loginSpinner.classList.add('d-none');
    loginText.textContent = 'Login';
});
