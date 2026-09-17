const header = document.querySelector('[data-header]');
const menu = document.querySelector('[data-menu]');
const menuButton = document.querySelector('[data-menu-button]');

const closeMenu = () => {
  menu?.classList.remove('open');
  menuButton?.setAttribute('aria-expanded', 'false');
};

menuButton?.addEventListener('click', () => {
  const isOpen = menu?.classList.toggle('open');
  menuButton.setAttribute('aria-expanded', String(Boolean(isOpen)));
});

menu?.querySelectorAll('a').forEach((link) => link.addEventListener('click', closeMenu));

const updateHeader = () => header?.classList.toggle('scrolled', window.scrollY > 16);
updateHeader();
window.addEventListener('scroll', updateHeader, { passive: true });

document.querySelectorAll('[data-year]').forEach((node) => {
  node.textContent = new Date().getFullYear();
});

const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
if (reduceMotion || !('IntersectionObserver' in window)) {
  document.querySelectorAll('.reveal').forEach((node) => node.classList.add('visible'));
} else {
  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.12 });

  document.querySelectorAll('.reveal').forEach((node) => observer.observe(node));
}
