/* script.js
   PLP Week 6 — JS Events & Basic Interactivity
   - Event handling examples
   - Two+ interactive features (dark mode toggle, counter game, collapsible FAQ)
   - Custom form validation (no HTML5-only rely)
*/

// ---------- Utility helpers ----------
const $ = (sel) => document.querySelector(sel);
const $$ = (sel) => Array.from(document.querySelectorAll(sel));

// safe text escape
function escapeHtml(s){ return String(s).replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;"); }

// ---------- 1) Theme toggle ----------
const toggleThemeBtn = $('#toggleThemeBtn');
const controlsResult = $('#controlsResult');
toggleThemeBtn.addEventListener('click', () => {
  document.documentElement.classList.toggle('dark');
  const isDark = document.documentElement.classList.contains('dark');
  controlsResult.textContent = isDark ? 'Dark theme enabled' : 'Light theme enabled';
  controlsResult.style.color = isDark ? '#9fe6a0' : '';
});

// demo alert button showing event handling
$('#generateAlertBtn').addEventListener('click', () => {
  controlsResult.textContent = 'You clicked the demo alert button — nice!';
});

// ---------- 2) Counter Game ----------
let score = 0;
let timeLeft = 0;
let gameTimer = null;
const clickBtn = $('#clickBtn');
const startGameBtn = $('#startGameBtn');
const timeLeftSpan = $('#timeLeft');
const scoreSpan = $('#score');
const gameResult = $('#gameResult');

clickBtn.disabled = true; // only allow clicks during game

clickBtn.addEventListener('click', () => {
  // fast clicks increment score only while running
  if (timeLeft > 0) {
    score += 1;
    scoreSpan.textContent = score;
  }
});

startGameBtn.addEventListener('click', () => {
  // initialize
  score = 0; timeLeft = 5;
  scoreSpan.textContent = score; timeLeftSpan.textContent = timeLeft;
  clickBtn.disabled = false; gameResult.textContent = '';
  // countdown
  if (gameTimer) clearInterval(gameTimer);
  gameTimer = setInterval(() => {
    timeLeft -= 1;
    timeLeftSpan.textContent = timeLeft;
    if (timeLeft <= 0) {
      clearInterval(gameTimer);
      clickBtn.disabled = true;
      gameResult.textContent = `Time's up! Your score: ${score}`;
      // small feedback: encourage excellent scores
      if (score >= 30) gameResult.textContent += " — Amazing! Share your score!";
    }
  }, 1000);
});

// ---------- 3) Collapsible FAQ ----------
$$('.faq-question').forEach((btn) => {
  btn.addEventListener('click', () => {
    const answer = btn.nextElementSibling;
    const isOpen = answer.style.display === 'block';
    // close all answers first (accordion feel)
    $$('.faq-answer').forEach(a => a.style.display = 'none');
    if (!isOpen) answer.style.display = 'block';
  });
});

// ---------- 4) Custom Form Validation ----------
const form = $('#signupForm');
const fullName = $('#fullName');
const email = $('#email');
const password = $('#password');
const confirmPassword = $('#confirmPassword');
const ageInput = $('#age');
const terms = $('#terms');

const errName = $('#errName');
const errEmail = $('#errEmail');
const errPassword = $('#errPassword');
const errConfirm = $('#errConfirm');
const errAge = $('#errAge');
const errTerms = $('#errTerms');
const formResult = $('#formResult');
const resetBtn = $('#resetBtn');

// Validation rules
function validateName(name){
  if(!name || name.trim().length < 2) return "Please enter your full name (min 2 chars).";
  if(!/^[A-Za-z\s'-]+$/.test(name.trim())) return "Name may only contain letters, spaces, hyphen and apostrophe.";
  return "";
}
function validateEmail(mail){
  if(!mail) return "Email is required.";
  // simple but effective regex
  if(!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(mail)) return "Please enter a valid email address.";
  return "";
}
function validatePassword(pw){
  if(!pw) return "Password is required.";
  if(pw.length < 8) return "Password must be at least 8 characters.";
  if(!/[A-Z]/.test(pw)) return "Include at least one uppercase letter.";
  if(!/\d/.test(pw)) return "Include at least one number.";
  if(!/[!@#$%^&*(),.?":{}|<>]/.test(pw)) return "Include at least one special character.";
  return "";
}
function validateAge(a){
  if(a === '' || a === null) return "Please enter your age.";
  const n = Number(a);
  if(Number.isNaN(n) || !Number.isInteger(n)) return "Age must be a whole number.";
  if(n < 13) return "You must be at least 13 to sign up.";
  return "";
}

// live validation (on input)
fullName.addEventListener('input', () => { errName.textContent = validateName(fullName.value) });
email.addEventListener('input', () => { errEmail.textContent = validateEmail(email.value) });
password.addEventListener('input', () => { errPassword.textContent = validatePassword(password.value) });
confirmPassword.addEventListener('input', () => { errConfirm.textContent = password.value === confirmPassword.value ? "" : "Passwords do not match."; });
ageInput.addEventListener('input', () => { errAge.textContent = validateAge(ageInput.value) });

// submit handler - prevents default so no page reload
form.addEventListener('submit', (e) => {
  e.preventDefault();
  // reset errors
  errName.textContent = errEmail.textContent = errPassword.textContent = errConfirm.textContent = errAge.textContent = errTerms.textContent = "";
  formResult.textContent = "";
  // validate all
  let hasError = false;
  const vName = validateName(fullName.value);
  if(vName){ errName.textContent = vName; hasError = true; }
  const vEmail = validateEmail(email.value);
  if(vEmail){ errEmail.textContent = vEmail; hasError = true; }
  const vPass = validatePassword(password.value);
  if(vPass){ errPassword.textContent = vPass; hasError = true; }
  if(password.value !== confirmPassword.value){ errConfirm.textContent = "Passwords do not match."; hasError = true; }
  const vAge = validateAge(ageInput.value);
  if(vAge){ errAge.textContent = vAge; hasError = true; }
  if(!terms.checked){ errTerms.textContent = "You must agree to the terms."; hasError = true; }

  if(hasError){
    formResult.style.color = 'var(--danger)';
    formResult.textContent = "Please fix the highlighted errors and resubmit.";
    return;
  }

  // success - simulate submission
  formResult.style.color = 'green';
  formResult.textContent = "Success! Validated client-side. (No server call in this demo.)";
  // show sanitized preview
  const preview = `Name: ${escapeHtml(fullName.value)}, Email: ${escapeHtml(email.value)}, Age: ${escapeHtml(ageInput.value)}`;
  console.log("PLP Form Submission (demo):", preview);

  // optionally clear form after success
  setTimeout(()=> {
    form.reset();
    scoreSpan && (scoreSpan.textContent = scoreSpan.textContent); // no-op, just safe
  }, 800);
});

// reset button
resetBtn.addEventListener('click', () => {
  form.reset();
  [errName,errEmail,errPassword,errConfirm,errAge,errTerms,formResult].forEach(el => el.textContent = '');
});

// Expose small API for graders in console
window.PLPMini = {
  validateName, validateEmail, validatePassword, validateAge,
  runCounterTest: () => { startGameBtn.click() }
};
