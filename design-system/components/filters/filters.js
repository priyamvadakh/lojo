import './filters.css';
import '../input/input.css';
import '../button/button.css';
import '../chip/chip.css';

const SEARCH = '<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></svg>';
const FUNNEL = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 5h16l-6 8v5l-4 2v-7z"/></svg>';

/** Search field with an icon */
export const Search = ({ placeholder = 'Search', value = '', glow = false } = {}) =>
  `<label class="lfsearch${glow ? ' is-glow' : ''}">${SEARCH}<input class="text" type="search" placeholder="${placeholder}" aria-label="${placeholder}" value="${value}" autocomplete="off"></label>`;

/** The Filter menu: checkboxes with counts, and Clear */
export const FilterMenu = ({ options = [], selected = [], staticMenu = false } = {}) =>
  `<div class="lfmenu${staticMenu ? ' is-static' : ''}" role="menu">${options.map((o) => `<label class="lfitem"><input type="checkbox"${selected.includes(o.label) ? ' checked' : ''}><span>${o.label}</span><em>${o.count}</em></label>`).join('')}${selected.length ? '<button class="lfclear" type="button">Clear filters</button>' : ''}</div>`;

/** Chips for the filters that are on, with Reset */
export const ActiveFilters = ({ selected = [] } = {}) =>
  selected.length ? `<div class="lfactive">${selected.map((s) => `<span class="lfchip">${s}<button type="button" aria-label="Remove ${s}">×</button></span>`).join('')}<button class="lfreset" type="button">Reset</button></div>` : '';

/** Filter bar: search + Filter button (+ open menu) + active filters */
export function FilterBar({ placeholder = 'Search drafts', query = '', options = [], selected = [], open = false } = {}) {
  const n = selected.length;
  return `<div class="lfind"><div class="lfrow">${Search({ placeholder, value: query })}<div class="lfdrop"><button class="btn btn--secondary lfbtn${n ? ' is-on' : ''}" type="button" aria-haspopup="true" aria-expanded="${open}">${FUNNEL}<span>Filter</span>${n ? `<span class="n">${n}</span>` : ''}</button>${open ? FilterMenu({ options, selected }) : ''}</div></div>${ActiveFilters({ selected })}</div>`;
}

/** Segmented toggle. size: lg (.segp) | sm (.rseg) */
export const Segmented = ({ options = [], selected = 0, size = 'lg', disabled = [] } = {}) =>
  `<div class="${size === 'sm' ? 'rseg' : 'segp'}" role="group">${options.map((o, i) => `<button type="button" aria-pressed="${i === selected}"${disabled.includes(i) ? ' disabled' : ''}>${o}</button>`).join('')}</div>`;

/** Count chips. Each item: { label, count, pressed, dot: 'live' | 'wait' } */
export const CountChips = ({ items = [] } = {}) =>
  `<div class="agf">${items.map((c) => `<button class="chip" type="button" aria-pressed="${!!c.pressed}">${c.dot === 'live' ? '<span class="live" aria-hidden="true"></span>' : c.dot === 'wait' ? '<span class="w" aria-hidden="true"></span>' : ''}${c.label}${c.count != null ? `<em>${c.count}</em>` : ''}</button>`).join('')}</div>`;
