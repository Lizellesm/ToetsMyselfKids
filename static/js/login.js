
// Function to get the ID token from Firebase
async function getIdToken() {
    const user = firebase.auth().currentUser;
    if (user) {
        return await user.getIdToken();
    }
    return null;
}

document.getElementById('login-form').addEventListener('submit', async function(event) {
    event.preventDefault();

    const submitButton = document.querySelector('button[type="submit"]');
    const loadingSpinner = document.getElementById('loading-spinner');

    submitButton.disabled = true;
    loadingSpinner.style.display = 'block';

    try {
        const email = document.getElementById('floatingInput').value;
        const password = document.getElementById('floatingPassword').value;

        // Sign in with Firebase Authentication
        await firebase.auth().signInWithEmailAndPassword(email, password);

        // Get the ID token
        const idToken = await getIdToken();
        if (idToken) {
            document.getElementById('id_token').value = idToken;
            this.submit();
        } else {
            alert('Failed to get ID token. Ensure you are logged into Firebase and try again.');
        }
    } catch (error) {
        console.error('An error occurred during login:', error);
        alert('An error occurred during login. Please try again.');
    } finally {
        submitButton.disabled = false;
        loadingSpinner.style.display = 'none';
    }
});