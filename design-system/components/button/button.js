import './button.css';
import { icons } from '../../icons.js';

/** Button: same markup as the prototype's .btn */
export function Button({ label = 'Button', variant = 'primary', size = 'md', disabled = false, loading = false, icon = '', state = '' } = {}) {
  const cls = ['btn', `btn--${variant}`, size === 'sm' ? 'btn--sm' : '', state === 'hover' ? 'is-hover' : ''].filter(Boolean).join(' ');
  const lead = loading ? '<span class="spin" aria-hidden="true"></span>' : (icon ? icons[icon] || '' : '');
  return `<button class="${cls}" type="button"${disabled ? ' disabled' : ''}${loading ? ' aria-busy="true"' : ''}>${lead}${label}</button>`;
}
