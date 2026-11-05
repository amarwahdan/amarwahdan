const root = document.documentElement;
const reducedQuery = window.matchMedia('(prefers-reduced-motion: reduce)');
let motionReduced = reducedQuery.matches;
try { motionReduced = motionReduced || localStorage.getItem('amar-motion') === 'reduced'; } catch (_) { /* Storage can be disabled. */ }
root.dataset.reducedMotion = String(motionReduced);

const motionButton = document.querySelector('.motion-control');
function syncMotionButton() {
  if (!motionButton) return;
  motionButton.setAttribute('aria-pressed', String(motionReduced));
  motionButton.textContent = motionReduced ? 'MOTION REDUCED' : 'REDUCE MOTION';
}
syncMotionButton();
motionButton?.addEventListener('click', () => {
  motionReduced = !motionReduced;
  root.dataset.reducedMotion = String(motionReduced);
  try { localStorage.setItem('amar-motion', motionReduced ? 'reduced' : 'full'); } catch (_) { /* Optional preference. */ }
  syncMotionButton();
});

const canHover = window.matchMedia('(hover: hover)').matches;
const heroArt = document.querySelector('.hero-art');
let pointerFrame = 0;
if (canHover) {
  window.addEventListener('pointermove', event => {
    if (motionReduced || pointerFrame) return;
    const { clientX, clientY } = event;
    pointerFrame = requestAnimationFrame(() => {
      root.style.setProperty('--px', `${clientX}px`);
      root.style.setProperty('--py', `${clientY}px`);
      if (heroArt) {
        heroArt.style.setProperty('--hx', `${(clientX / innerWidth - .5) * 20}px`);
        heroArt.style.setProperty('--hy', `${(clientY / innerHeight - .5) * 14}px`);
      }
      pointerFrame = 0;
    });
  }, { passive: true });
  document.querySelectorAll('.magnetic').forEach(element => {
    element.addEventListener('pointermove', event => {
      if (motionReduced) return;
      const box = element.getBoundingClientRect();
      const x = (event.clientX - box.left - box.width / 2) * .08;
      const y = (event.clientY - box.top - box.height / 2) * .15;
      element.style.transform = `translate(${x}px, ${y}px)`;
    });
    element.addEventListener('pointerleave', () => { element.style.transform = ''; });
  });
}

const cards = [...document.querySelectorAll('.project-card')];
let keyboardMode = false;
window.addEventListener('keydown', () => { keyboardMode = true; });
window.addEventListener('pointerdown', () => { keyboardMode = false; }, { passive: true });
cards.forEach(card => {
  const reveal = card.querySelector('.card-reveal');
  const overlay = card.querySelector('.stack-overlay');
  let hovered = false;
  let focused = false;
  let manuallyOpen = false;
  let manuallyHidden = false;
  function syncCard() {
    const shown = !manuallyHidden && (manuallyOpen || hovered || focused);
    card.classList.toggle('is-stack-open', shown);
    card.classList.toggle('is-revealed', manuallyOpen);
    overlay?.setAttribute('aria-hidden', String(!shown));
    reveal?.setAttribute('aria-expanded', String(shown));
    if (reveal) {
      reveal.querySelector('.reveal-label').textContent = shown ? 'Hide stack' : 'Reveal stack';
      reveal.querySelector('.reveal-symbol').textContent = shown ? '−' : '+';
    }
  }
  reveal?.addEventListener('click', () => {
    manuallyOpen = !card.classList.contains('is-stack-open');
    manuallyHidden = !manuallyOpen;
    syncCard();
  });
  card.addEventListener('focusin', event => {
    if (keyboardMode && !card.contains(event.relatedTarget)) {
      focused = true;
      manuallyHidden = false;
      syncCard();
    }
  });
  card.addEventListener('focusout', () => {
    requestAnimationFrame(() => {
      focused = keyboardMode && card.contains(document.activeElement);
      if (!focused && !hovered) manuallyHidden = false;
      syncCard();
    });
  });
  card.addEventListener('keydown', event => {
    if (event.key === 'Escape') {
      manuallyOpen = false;
      manuallyHidden = true;
      syncCard();
    }
  });
  if (canHover) {
    card.addEventListener('pointerenter', event => {
      if (event.pointerType === 'touch') return;
      hovered = true;
      manuallyHidden = false;
      syncCard();
    });
    card.addEventListener('pointermove', event => {
      if (event.pointerType === 'touch') return;
      const box = card.getBoundingClientRect();
      const x = (event.clientX - box.left) / box.width;
      const y = (event.clientY - box.top) / box.height;
      card.style.setProperty('--cx', `${x * 100}%`);
      card.style.setProperty('--cy', `${y * 100}%`);
      if (!motionReduced) {
        card.style.setProperty('--rx', `${(y - .5) * -5}deg`);
        card.style.setProperty('--ry', `${(x - .5) * 6}deg`);
      }
    });
    card.addEventListener('pointerleave', () => {
      hovered = false;
      if (!focused) manuallyHidden = false;
      syncCard();
      card.style.setProperty('--rx', '0deg');
      card.style.setProperty('--ry', '0deg');
    });
  }
  syncCard();
});

const rail = document.querySelector('.project-rail');
const railProgress = document.querySelector('.rail-progress span');
const previous = document.querySelector('[data-scroll="-1"]');
const next = document.querySelector('[data-scroll="1"]');
function syncRail() {
  if (!rail) return;
  const max = rail.scrollWidth - rail.clientWidth;
  const fraction = max > 0 ? rail.scrollLeft / max : 1;
  if (railProgress) railProgress.style.width = `${Math.max(8, fraction * 100)}%`;
  if (previous) previous.disabled = rail.scrollLeft < 5;
  if (next) next.disabled = max < 5 || rail.scrollLeft > max - 5;
}
rail?.addEventListener('scroll', syncRail, { passive: true });
window.addEventListener('resize', syncRail, { passive: true });
document.querySelectorAll('[data-scroll]').forEach(button => {
  button.addEventListener('click', () => {
    if (!rail) return;
    const visible = cards.find(card => !card.hidden);
    const distance = visible ? visible.getBoundingClientRect().width + 20 : 420;
    rail.scrollBy({ left: Number(button.dataset.scroll) * distance, behavior: motionReduced ? 'instant' : 'smooth' });
  });
});
const filters = [...document.querySelectorAll('.filter-button')];
filters.forEach(button => {
  button.addEventListener('click', () => {
    filters.forEach(other => other.setAttribute('aria-pressed', String(other === button)));
    cards.forEach(card => { card.hidden = button.dataset.filter !== 'all' && card.dataset.group !== button.dataset.filter; });
    rail?.scrollTo({ left: 0, behavior: 'instant' });
    requestAnimationFrame(syncRail);
  });
});
syncRail();

const dataNode = document.getElementById('portfolio-data');
const data = dataNode ? JSON.parse(dataNode.textContent) : { tools: [], projects: [] };
const toolButtons = [...document.querySelectorAll('[data-tool]')];
const core = document.querySelector('.tool-core');
const inspector = document.querySelector('.tool-inspector');
const path = document.querySelector('.signal-path');
const signalEnd = document.querySelector('.signal-end');
let burstTimer;
function activateTool(button, clicked = false) {
  const tool = data.tools.find(item => item.id === button.dataset.tool);
  if (!tool || !inspector) return;
  toolButtons.forEach(other => {
    const active = other.dataset.tool === tool.id;
    other.classList.toggle('active', active);
    other.setAttribute('aria-pressed', String(active));
  });
  inspector.querySelector('.selected-name').textContent = tool.name;
  inspector.querySelector('.selected-category').textContent = tool.category;
  inspector.querySelector('.selected-description').textContent = tool.description;
  inspector.querySelector('.selected-action').textContent = tool.signature;
  const iconTarget = inspector.querySelector('.selected-icon');
  iconTarget.replaceChildren();
  const icon = button.querySelector('svg');
  if (icon) iconTarget.append(icon.cloneNode(true));
  const connected = data.projects.filter(project => tool.projects.includes(project.id));
  inspector.querySelector('.connected-count').textContent = String(connected.length).padStart(2, '0');
  const links = inspector.querySelector('.connected-projects');
  links.replaceChildren();
  connected.forEach(project => {
    const link = document.createElement('a');
    link.href = `/projects/${project.id}/`;
    link.textContent = project.name;
    links.append(link);
  });
  if (!connected.length) {
    const note = document.createElement('span');
    note.className = 'unlinked';
    note.textContent = 'Profile capability · explore the notes';
    links.append(note);
  }
  cards.forEach(card => card.classList.toggle('is-connected', tool.projects.includes(card.dataset.project)));
  if (core) {
    core.dataset.action = tool.action;
    if (clicked) {
      core.classList.remove('burst');
      void core.offsetWidth;
      core.classList.add('burst');
      clearTimeout(burstTimer);
      burstTimer = setTimeout(() => core.classList.remove('burst'), 650);
    }
  }
  if (path && signalEnd) {
    const x = Number(button.dataset.x || 330);
    const y = Number(button.dataset.y || 245);
    path.setAttribute('d', `M${x} ${y} Q${(x + 330) / 2 + 20} ${(y + 245) / 2 - 25} 330 245`);
    signalEnd.setAttribute('cx', String(x));
    signalEnd.setAttribute('cy', String(y));
  }
}
toolButtons.forEach(button => {
  if (canHover) button.addEventListener('pointerenter', () => activateTool(button));
  button.addEventListener('focus', () => activateTool(button));
  button.addEventListener('click', () => activateTool(button, true));
});
const firstTool = toolButtons.find(button => button.dataset.tool === 'pytorch');
if (firstTool) activateTool(firstTool);
