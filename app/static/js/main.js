/* ==========================================================
   Transmilenium Logística y Transporte — Main JS
   ========================================================== */

// ---------- Smooth Scroll for Anchor Links ----------
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', function (e) {
    const targetId = this.getAttribute('href');
    const targetEl = document.querySelector(targetId);
    if (targetEl) {
      e.preventDefault();
      window.scrollTo({
        top: targetEl.offsetTop - 70, // offset for navbar height
        behavior: 'smooth'
      });
    }
  });
});

// ---------- Navbar Scroll Effect ----------
const navbar = document.querySelector('.navbar');
window.addEventListener('scroll', () => {
  if (window.scrollY > 80) {
    navbar.classList.add('scrolled');
  } else {
    navbar.classList.remove('scrolled');
  }
});

// ---------- Reveal-on-Scroll ----------
const revealElements = document.querySelectorAll('.reveal');

function revealOnScroll() {
  const windowHeight = window.innerHeight;
  revealElements.forEach(el => {
    const elementTop = el.getBoundingClientRect().top;
    const threshold = 100; // trigger offset
    if (elementTop < windowHeight - threshold) {
      el.classList.add('visible');
    }
  });
}

// Run on scroll and on load
window.addEventListener('scroll', revealOnScroll);
window.addEventListener('load', revealOnScroll);

// ---------- Optional: Add simple fade-in style via CSS ----------
// .reveal { opacity: 0; transform: translateY(20px); transition: all 0.6s ease; }
// .reveal.visible { opacity: 1; transform: translateY(0); }
 
