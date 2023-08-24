const navbar = document.querySelector('.navbar');
const initialGradient = 'linear-gradient(to right, #91fffb, #fcffff)';
const scrolledColor = 'white'; // Change to your desired color
const scrollThreshold = 100; // Adjust the scroll threshold as needed

window.addEventListener('scroll', () => {
    if (window.scrollY > scrollThreshold) {
        navbar.style.background = scrolledColor;
    } else {
        navbar.style.background = initialGradient;
    }
});