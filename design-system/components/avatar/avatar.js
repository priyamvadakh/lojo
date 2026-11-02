import './avatar.css';

/** Initials, as the prototype does it: first letter of the first two words */
export const initials = (name = '') => name.split(/\s+/).filter(Boolean).map((w) => w[0]).join('').slice(0, 2).toUpperCase();
/** Colour from the name, same formula as the prototype's tone(): the same name always gets the same colour */
export const tone = (name = '') => 'avt' + ([...String(name)].reduce((a, c) => a + c.charCodeAt(0), 0) % 4 + 1);

/**
 * Initials avatar.
 * kind: person (circle) | org (rounded square)   size: xs | sm | me | md | lg
 * pending: invited, not joined yet   ink: dark tile (lojo back office)
 */
export function Avatar({ name = 'Eric Ouisse', kind = 'person', size = 'md', pending = false, ink = false, icon = '' } = {}) {
  const cls = ['av', kind === 'org' ? 'av--org' : 'av--p', size !== 'md' ? `av--${size}` : '', pending ? 'is-pending' : ink ? 'av--ink' : tone(name)].filter(Boolean).join(' ');
  return `<span class="${cls}" role="img" aria-label="${name}${pending ? ' (invited)' : ''}">${icon || initials(name)}</span>`;
}

/** Avatar with a name and a line of detail */
export const Who = ({ name = 'Eric Ouisse', sub = '', badge = '', ...av } = {}) =>
  `<div class="who">${Avatar({ name, ...av })}<div><b>${name}${badge}</b>${sub ? `<span class="who__sub">${sub}</span>` : ''}</div></div>`;

/* ---------- agents ---------- */
export const AGENTS = {
  'Sync agent': { key: 'sync', job: '<path d="M3 12a9 9 0 0 1 15.5-6.2L21 8M21 3v5h-5M21 12a9 9 0 0 1-15.5 6.2L3 16M3 21v-5h5"/>' },
  'Indexer': { key: 'indexer', job: '<path d="M12 3 2 8l10 5 10-5z"/><path d="m2 13 10 5 10-5M2 18l10 5 10-5"/>' },
  'Question finder': { key: 'questions', job: '<circle cx="12" cy="12" r="9"/><path d="M9.5 9.5a2.5 2.5 0 1 1 3.5 2.3c-.6.3-1 .8-1 1.5V14M12 17h.01"/>' },
  'Gap finder': { key: 'gaps', job: '<circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/>' },
  'Drafting agent': { key: 'drafting', job: '<path d="M12 20h9"/><path d="M16.5 3.5a2.1 2.1 0 0 1 3 3L7 19l-4 1 1-4z"/>' },
  'Rewrite agent': { key: 'rewrite', job: '<path d="M3 12a9 9 0 1 0 3-6.7L3 8"/><path d="M3 3v5h5"/>' },
  'Chat agent': { key: 'chat', job: '<path d="M21 12a8 8 0 0 1-11.6 7.1L4 20l1-4.6A8 8 0 1 1 21 12z"/>' },
  'Publisher': { key: 'publisher', job: '<path d="M21 3 10 14M21 3l-7 18-4-7-7-4z"/>' },
};

/** Agent avatar. state: idle | run | off */
export function AgentAvatar({ agent = 'Sync agent', state = 'idle' } = {}) {
  const a = AGENTS[agent] || AGENTS['Chat agent'];
  const id = 'ag-' + a.key + '-' + Math.random().toString(36).slice(2, 7);
  const st = state === 'run' ? ' is-run' : state === 'off' ? ' is-off' : '';
  return `<span class="ava3d${st}" role="img" aria-label="${agent}${state === 'run' ? ', running' : state === 'off' ? ', off' : ''}"><svg viewBox="0 0 44 44"><defs><linearGradient id="${id}" x1="0" y1="0" x2="1" y2="1"><stop offset="0" style="stop-color:var(--agent-${a.key}-deep)"/><stop offset="1" style="stop-color:var(--agent-${a.key}-light)"/></linearGradient></defs><rect width="44" height="44" rx="11" fill="url(#${id})"/><image href="brand/prototype/lojo-cloud.png" x="9.5" y="9.5" width="25" height="25"/></svg><i class="ava3d__job" style="color:var(--agent-${a.key}-deep)"><svg viewBox="0 0 24 24">${a.job}</svg></i></span>`;
}
