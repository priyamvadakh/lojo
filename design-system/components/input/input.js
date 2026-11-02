import './input.css';
/** Text field: the prototype's .text on input, textarea or select, with an optional label and hint */
export function Input({ type = 'text', label = '', placeholder = '', value = '', hint = '', state = '', disabled = false, options = [] } = {}) {
  const cls = 'text' + (state === 'focus' ? ' is-focus' : '');
  const dis = disabled ? ' disabled' : '';
  let control;
  if (type === 'textarea') control = `<textarea class="${cls}" placeholder="${placeholder}"${dis}>${value}</textarea>`;
  else if (type === 'select') control = `<select class="${cls}"${dis}>${options.map((o) => `<option${o === value ? ' selected' : ''}>${o}</option>`).join('')}</select>`;
  else control = `<input class="${cls}" type="${type}" placeholder="${placeholder}" value="${value}"${dis}>`;
  if (!label && !hint) return control;
  return `<label class="field${state === 'error' ? ' is-error' : ''}">${label ? `<span class="field__label">${label}</span>` : ''}${control}${hint ? `<p class="field__hint">${hint}</p>` : ''}</label>`;
}
