import './card.css';
/** Card: .card with an optional head (title + actions) and body */
export function Card({ title = '', sub = '', actions = '', body = '' } = {}) {
  const head = title ? `<div class="card__head"><div><h2>${title}</h2>${sub ? `<p class="sub">${sub}</p>` : ''}</div><span class="spacer"></span>${actions}</div>` : '';
  return `<div class="card">${head}<div class="card__body">${body}</div></div>`;
}
/** Section: the larger .sec panel with an overline heading */
export function Section({ title = '', meta = '', link = '', body = '' } = {}) {
  return `<section class="sec"><div class="sec__head"><h2>${title}</h2>${meta ? `<span>${meta}</span>` : ''}${link ? `<a href="#">${link}</a>` : ''}</div>${body}</section>`;
}
/** Stat: a number tile */
export const Stat = ({ value = '0', label = '', key = false } = {}) => `<div class="stat${key ? ' is-key' : ''}"><b>${value}</b><span>${label}</span></div>`;
