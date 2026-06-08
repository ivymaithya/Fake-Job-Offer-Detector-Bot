document.addEventListener('DOMContentLoaded', () => {
    
    // Mobile sidebar toggle functionality
    const mobileMenuBtn = document.getElementById('mobile-menu-btn');
    const sidebar = document.querySelector('.sidebar');
    
    if (mobileMenuBtn && sidebar) {
        mobileMenuBtn.addEventListener('click', () => {
            sidebar.classList.toggle('open');
        });
        
        // Close sidebar when clicking outside on mobile
        document.addEventListener('click', (event) => {
            if (window.innerWidth <= 768) {
                if (!sidebar.contains(event.target) && event.target !== mobileMenuBtn) {
                    sidebar.classList.remove('open');
                }
            }
        });
    }

    // Animate the progress circle in the analyze page if present
    const circle = document.querySelector('.circle');
    if (circle) {
        // Force reflow to ensure animation triggers when re-rendering
        void circle.offsetWidth;
    }
});
