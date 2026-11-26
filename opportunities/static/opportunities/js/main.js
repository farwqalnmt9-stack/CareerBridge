document.querySelectorAll('.save-button').forEach((button) => {
  button.addEventListener('click', () => {
    const saved = button.getAttribute('aria-pressed') === 'true';
    button.setAttribute('aria-pressed', String(!saved));
    button.textContent = saved ? '♡' : '♥';
  });
});

if (!window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
  const observer = new IntersectionObserver((entries, currentObserver) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) { entry.target.style.transition = 'opacity .35s ease, transform .35s ease'; entry.target.style.opacity = '1'; entry.target.style.transform = 'none'; currentObserver.unobserve(entry.target); }
    });
  }, { threshold: .15 });
  document.querySelectorAll('.reveal').forEach((card) => { card.style.opacity = '0'; card.style.transform = 'translateY(16px)'; observer.observe(card); });
}
