import './chip.css';
/** Filter chip: the prototype's .chip toggle */
export const Chip = ({ label = 'Chip', pressed = false, state = '', disabled = false } = {}) =>
  `<button class="chip${state === 'hover' ? ' is-hover' : ''}" type="button" aria-pressed="${pressed}"${disabled ? ' disabled' : ''}>${label}</button>`;
export const Chips = ({ chips = [] } = {}) => `<div class="chips">${chips.map(Chip).join('')}</div>`;
