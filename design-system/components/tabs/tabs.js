import './tabs.css';
/** Tabs: the prototype's .tabs / .tab underline tabs */
export function Tabs({ tabs = [], selected = 0, hover = -1 } = {}) {
  return `<div class="tabs" role="tablist">${tabs.map((t, i) => `<button class="tab${i === hover ? ' is-hover' : ''}" role="tab" type="button" aria-selected="${i === selected}">${t.label}${t.count != null ? `<span class="n">${t.count}</span>` : ''}</button>`).join('')}</div>`;
}
