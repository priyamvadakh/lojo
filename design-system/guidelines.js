import './guidelines.css';

const card = (kind, { example, text }) =>
  `<figure class="gl__card gl__card--${kind}" style="margin:0"><div class="gl__stage">${example}</div><figcaption class="gl__note"><span class="gl__tag">${kind === 'do' ? '✓ Do' : '✕ Don’t'}</span><p>${text}</p></figcaption></figure>`;

/**
 * Do / Don't guidelines.
 * rules: [{ do: { example, text }, dont: { example, text } }]  — each rule renders as a side-by-side pair
 */
export function Guidelines({ intro = '', rules = [] } = {}) {
  return `<div class="gl">${intro ? `<p class="gl__intro">${intro}</p>` : ''}${rules.map((r) => `<div class="gl__pair">${r.do ? card('do', r.do) : ''}${r.dont ? card('dont', r.dont) : ''}</div>`).join('')}</div>`;
}
