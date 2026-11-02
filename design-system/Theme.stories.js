// Light and dark themes side by side. Every colour comes from tokens.css.
import './components/button/button.css';
import './components/badge/badge.css';
import './components/card/card.css';
import './components/input/input.css';
import { Guidelines } from './guidelines.js';
import { Button } from './components/button/button.js';
import { Badge } from './components/badge/badge.js';

const sample = (mode) => `
  <div data-theme="${mode}" style="color-scheme:${mode};padding:var(--space-22);border-radius:var(--radius-3xl);border:var(--border-width) solid var(--line);background:var(--canvas);color:var(--ink);font-family:var(--body)">
    <p style="margin:0 0 var(--space-12);font-size:var(--text-70);font-weight:var(--weight-bold);letter-spacing:var(--tracking-overline);text-transform:uppercase;color:var(--rose)">${mode} theme</p>
    <div class="card"><div class="card__head"><div><h2>Review queue</h2><p class="sub">20 drafts due Friday</p></div><span class="spacer"></span>${Badge({ tone: 'amber', label: 'Needs review' })}</div>
    <div class="card__body" style="display:grid;gap:var(--space-14)"><input class="text" placeholder="Search answers"><div style="display:flex;gap:var(--space-8);flex-wrap:wrap">${Button({ label: 'Approve' })}${Button({ label: 'Edit', variant: 'secondary' })}${Button({ label: 'Reject', variant: 'danger' })}</div>
    <div style="display:flex;gap:var(--space-6);flex-wrap:wrap">${Badge({ tone: 'ok', label: 'Approved' })}${Badge({ tone: 'info', label: 'Processing' })}${Badge({ tone: 'err', label: 'Failed' })}${Badge({ tone: 'muted', label: 'Draft' })}</div></div></div>
  </div>`;

// The dark block re-declares the dark token values on its own element, so both show at once
const scopeDark = () => {
  if (document.getElementById('theme-scope')) return;
  const css = [...document.styleSheets].flatMap((s) => { try { return [...s.cssRules]; } catch { return []; } })
    .filter((r) => r.selectorText === ':root[data-theme="dark"]').map((r) => r.cssText.replace(':root[data-theme="dark"]', '[data-theme="dark"]')).join('\n');
  const el = document.createElement('style'); el.id = 'theme-scope'; el.textContent = css + '\n[data-theme="light"]{' + lightVars() + '}'; document.head.appendChild(el);
};
const lightVars = () => [...document.styleSheets].flatMap((s) => { try { return [...s.cssRules]; } catch { return []; } })
  .filter((r) => r.selectorText === ':root').map((r) => r.style.cssText).join('');

export default { title: 'Foundations/Theme' };

export const LightAndDark = {
  render: () => { scopeDark(); return `<p class="sub" style="margin:0 0 var(--space-16)">The whole product switches with <code>data-theme="dark"</code> on &lt;html&gt;. Use the toolbar Theme switch to flip every story.</p><div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(340px,1fr));gap:var(--space-16);max-width:980px">${sample('light')}${sample('dark')}</div>`; },
};

export const Guideline = {
  name: 'Do and don’t',
  parameters: { controls: { disable: true }, actions: { disable: true }, interactions: { disable: true } },
  render: () => Guidelines({
    intro: 'Colour comes from tokens so light and dark stay in step. Rose is the accent, ink is the action.',
    rules: [
      {
        do: { example: `<span style="color:var(--ink);font-weight:var(--weight-semibold)">var(--ink)</span><span style="color:var(--muted)">var(--muted)</span>`, text: 'Use token names (var(--ink), var(--panel)) so dark mode works for free.' },
        dont: { example: `<span style="color:#241A14;font-weight:var(--weight-semibold)">#241A14</span>`, text: 'Don’t hard-code hex values in components: they stay light in dark mode.' },
      },
      {
        do: { example: Button({ label: 'Save' }) + Button({ label: 'Cancel', variant: 'secondary' }), text: 'Ink for the main action, rose for small accents (active tab, counts, focus).' },
        dont: { example: `<button class="btn" style="background:var(--rose);color:var(--on-brand)">Save</button><button class="btn" style="background:var(--peach)">Cancel</button>`, text: 'Don’t fill buttons with flat rose or peach.' },
      },
      {
        do: { example: Badge({ tone: 'ok', label: 'Approved' }) + Badge({ tone: 'err', label: 'Failed' }), text: 'Use status colours only for status: green done, red failed, amber waiting, blue running.' },
        dont: { example: `<span style="color:var(--success);font-weight:var(--weight-bold)">Welcome back</span>`, text: 'Don’t use status colours for decoration or headings.' },
      },
    ],
  }),
};
