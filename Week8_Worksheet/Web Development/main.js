// main.js — small helpers: menu toggle, contact form validation, year insert
document.addEventListener('DOMContentLoaded', () => {
  // year
  const yearEl = document.getElementById('year');
  if (yearEl) yearEl.textContent = new Date().getFullYear();

  // mobile nav toggle
  const navToggle = document.getElementById('navToggle');
  const primaryNav = document.getElementById('primaryNav');
  if (navToggle && primaryNav) {
    navToggle.addEventListener('click', () => {
      const expanded = navToggle.getAttribute('aria-expanded') === 'true';
      navToggle.setAttribute('aria-expanded', String(!expanded));
      if (primaryNav.classList.contains('open')) {
        primaryNav.classList.remove('open');
      } else {
        primaryNav.classList.add('open');
      }
    });
  }

  // contact form validation
  const form = document.getElementById('contactForm');
  if (form) {
    form.addEventListener('submit', (ev) => {
      ev.preventDefault();
      // simple validation
      const name = document.getElementById('name');
      const email = document.getElementById('email');
      const message = document.getElementById('message');
      let ok = true;
      document.getElementById('errName').textContent = '';
      document.getElementById('errEmail').textContent = '';
      document.getElementById('errMessage').textContent = '';
      if (!name.value.trim()) { document.getElementById('errName').textContent = 'Please enter your name'; ok = false; }
      if (!email.value.trim() || !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email.value)) { document.getElementById('errEmail').textContent = 'Please enter a valid email'; ok = false; }
      if (!message.value.trim() || message.value.trim().length < 10) { document.getElementById('errMessage').textContent = 'Message must be at least 10 characters'; ok = false; }
      const result = document.getElementById('formResult');
      if (!ok) { if (result) result.textContent = 'Please fix errors above.'; return; }
      // success (no backend) — show friendly message
      if (result) {
        result.style.color = 'green';
        result.textContent = 'Thanks — your message is ready to send (demo).';
      }
      form.reset();
    });
  }
});
