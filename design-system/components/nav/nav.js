import './nav.css';
import { icons } from '../../icons.js';

/** One sidebar link: the prototype's .nav-item */
export function NavItem({ icon = 'overview', label = 'Dashboard', active = false, count = null, hot = false, state = '' } = {}) {
  const cls = ['nav-item', active ? 'is-active' : '', state === 'hover' ? 'is-hover' : ''].filter(Boolean).join(' ');
  const cnt = count != null ? `<span class="count${hot ? ' count--hot' : ''}">${count}</span>` : '';
  return `<a class="${cls}" href="#"${active ? ' aria-current="page"' : ''} title="${label}">${icons[icon] || ''}<span class="lbl">${label}</span>${cnt}</a>`;
}

/** Sidebar nav: the floating .side panel with a list of items */
export function Nav({ items = [], collapsed = false } = {}) {
  return `<aside class="side${collapsed ? ' is-collapsed' : ''}" aria-label="Main navigation"><nav>${items.map(NavItem).join('')}</nav></aside>`;
}
