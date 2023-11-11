const darkModeToggle = document.getElementById('darkModeToggle');
const body = document.body;


darkModeToggle.addEventListener('change', function() {
  body.classList.toggle('dark-mode');
  localStorage.setItem('darkModeEnabled', body.classList.contains('dark-mode'));
  
});

// Check if dark mode was enabled previously
if (localStorage.getItem('darkModeEnabled') === 'true') {
  body.classList.add('dark-mode');
  darkModeToggle.checked = true;

}

// Check if user prefers dark or light color scheme and apply styles accordingly
const prefersDarkScheme = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;
const prefersLightScheme = window.matchMedia && window.matchMedia('(prefers-color-scheme: light)').matches;

if (prefersDarkScheme) {
  body.classList.add('dark-mode');
  darkModeToggle.checked = true;
  
} else if (prefersLightScheme) {
  body.classList.remove('dark-mode');
  darkModeToggle.checked = false;
  
}
