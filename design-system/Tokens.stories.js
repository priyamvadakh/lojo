// Lists every custom property in tokens.css, with a swatch for colours
import "./components/table/table.css";
import tokensCss from './tokens.css?raw';

const tokens = [...tokensCss.replace(/\/\*[\s\S]*?\*\//g, '').split(':root[data-theme="dark"]')[0].matchAll(/(--[\w-]+)\s*:\s*([^;]+);/g)].map((m) => ({ name: m[1], value: m[2].trim() }));
const group = (prefix) => tokens.filter((t) => prefix.some((p) => t.name.startsWith(p)));
const isColour = (v) => /^(#|rgba?\(|linear-gradient|var\()/.test(v) && !v.startsWith('url');
const swatch = (t) => `<div style="display:flex;align-items:center;gap:var(--space-12);padding:var(--space-6) 0"><span style="width:40px;height:40px;border-radius:var(--radius-md);border:var(--border-width) solid var(--line);background:var(${t.name})"></span><code>${t.name}</code></div>`;
const rowOf = (t, demo) => `<tr><td><code>${t.name}</code></td><td style="color:var(--muted)">${t.value}</td><td>${demo(t)}</td></tr>`;
const table = (list, demo) => `<table class="dtable" style="max-width:820px"><tbody>${list.map((t) => rowOf(t, demo)).join('')}</tbody></table>`;

export default { title: 'Foundations/Tokens', parameters: { layout: 'padded' } };

export const Colours = {
  render: () => `<p class="sub">Use the toolbar Theme switch to see dark values.</p><div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:var(--space-4) var(--space-20);margin-top:var(--space-12)">${tokens.filter((t) => isColour(t.value) && !/^--(shadow|focus)/.test(t.name)).map(swatch).join('')}</div>`,
};
export const Typography = {
  render: () => table(group(['--text-', '--weight-', '--display', '--body']), (t) => t.name.startsWith('--text-') ? `<span style="font-size:var(${t.name})">The company brain</span>` : t.name.startsWith('--weight') ? `<span style="font-weight:var(${t.name})">The company brain</span>` : `<span style="font-family:var(${t.name})">The company brain</span>`),
};
export const Spacing = {
  render: () => table(group(['--space-']), (t) => `<span style="display:block;height:12px;width:var(${t.name});background:var(--rose);border-radius:2px"></span>`),
};
export const Radius = {
  render: () => table(group(['--radius-']), (t) => `<span style="display:block;width:64px;height:40px;border:var(--border-width) solid var(--line-2);background:var(--bg-soft);border-radius:var(${t.name})"></span>`),
};
export const Shadows = {
  render: () => table(group(['--shadow-', '--focus-']), (t) => `<span style="display:block;width:120px;height:56px;margin:var(--space-12) 0;border-radius:var(--radius-md);background:var(--panel);box-shadow:var(${t.name})"></span>`),
};
