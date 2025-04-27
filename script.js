// Check if the user prefers animations to be enabled
function getUserPreference() {
    const preference = localStorage.getItem('animationPreference');
    return preference ? JSON.parse(preference) : true;  // Default to true if no preference is stored
  }
  
  // Save the user's preference for animations
  function saveUserPreference(preference) {
    localStorage.setItem('animationPreference', JSON.stringify(preference));
  }
  
  // Toggle animation on button click
  function toggleAnimation() {
    const button = document.querySelector('button');
    
    if (getUserPreference()) {
      // If animations are enabled, trigger animation
      button.classList.add('animate');
      
      // Remove animation class after it completes (1 second)
      setTimeout(() => button.classList.remove('animate'), 1000);
    }
  }
  
  // Set or toggle the animation preference (using a checkbox for example)
  function setAnimationPreference(enable) {
    saveUserPreference(enable);
  }
  
  // Example of applying the preference
  document.addEventListener('DOMContentLoaded', () => {
    const button = document.querySelector('button');
    
    // If user prefers animations, show animation on click
    button.addEventListener('click', toggleAnimation);
    
    // Check user's preference and set the checkbox accordingly
    const preference = getUserPreference();
    document.getElementById('enable-animation').checked = preference;
    
    // Listen for changes to the checkbox
    document.getElementById('enable-animation').addEventListener('change', (event) => {
      const enable = event.target.checked;
      setAnimationPreference(enable);
    });
  });
  