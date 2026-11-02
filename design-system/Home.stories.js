import './cover.css';
import { Button } from './components/button/button.js';
import { Badge } from './components/badge/badge.js';
import { Input } from './components/input/input.js';
import { Avatar, AgentAvatar } from './components/avatar/avatar.js';
import { Tabs } from './components/tabs/tabs.js';
import { Chips } from './components/chip/chip.js';
import { NavItem } from './components/nav/nav.js';
import { Segmented } from './components/filters/filters.js';
import { Stat } from './components/card/card.js';
import './components/table/table.css';
import './components/nav/nav.css';
import { LogoLockup } from './brand/logo.js';

// demos sit inside a link, so any link inside them becomes a span (links can't nest)
const noLinks = (h) => h.replace(/<a\b/g, '<span').replace(/<\/a>/g, '</span>');
const go = (id) => `./?path=/story/${id}`;
const tile = (id, title, sub, demo) => `<a class="cover__tile" href="${go(id)}" target="_top"><div class="cover__demo">${noLinks(demo)}</div><div class="cover__txt"><b>${title}</b><span>${sub}</span></div></a>`;
const sw = (v) => `<i style="width:28px;height:28px;border-radius:var(--radius-3xs);background:var(${v});border:var(--border-width) solid var(--line)"></i>`;

export default { title: 'Home', parameters: { layout: 'fullscreen', controls: { disable: true }, actions: { disable: true }, interactions: { disable: true } } };

export const Cover = {
  render: () => `<div class="cover">
    <header class="cover__hero">
      <img src="brand/prototype/lojo-cloud.png" alt="" width="96" height="96">
      <div>
        <p class="cover__eyebrow">lojo.ai</p>
        <h1>Design System</h1>
        <p class="cover__lede">The tokens, components and rules behind lojo, the company brain that never stops learning. Everything here is built from one tokens file, so it matches the product in light and dark.</p>
        <div class="cover__meta"><span>HTML + CSS</span><span>Light and dark</span><span>Do and don’t for every component</span></div>
      </div>
    </header>

    <h2 class="cover__h">Foundations</h2>
    <div class="cover__grid">
      ${tile('foundations-tokens--colours', 'Tokens', 'Colour, type, spacing, radius, shadow', ['--rose', '--peach', '--ink', '--bg-soft', '--success', '--info'].map(sw).join(''))}
      ${tile('foundations-theme--light-and-dark', 'Theme', 'Light and dark, side by side', sw('--panel') + `<i style="width:28px;height:28px;border-radius:var(--radius-3xs);background:var(--surface-dark)"></i>`)}
      ${tile('foundations-logo--logo', 'Logo', 'Marks, sizes, clear space', LogoLockup())}
    </div>

    <h2 class="cover__h">Components</h2>
    <div class="cover__grid">
      ${tile('components-button--all-variants-and-states', 'Button', 'Primary, gradient, secondary, ghost, danger', Button({ label: 'Approve', size: 'sm' }) + Button({ label: 'Edit', variant: 'secondary', size: 'sm' }))}
      ${tile('components-badge--all-tones', 'Badge', 'Status labels', Badge({ tone: 'ok', label: 'Approved' }) + Badge({ tone: 'amber', label: 'Review' }) + Badge({ tone: 'err', label: 'Failed' }))}
      ${tile('components-input--all-states', 'Input', 'Text, textarea, select, states', `<div style="width:100%">${Input({ placeholder: 'Search answers' })}</div>`)}
      ${tile('components-avatar--people', 'Avatar', 'People, companies, agents', Avatar({ name: 'Eric Ouisse' }) + Avatar({ name: 'Lina Odeh' }) + Avatar({ name: 'Oslo', kind: 'org' }) + AgentAvatar({ agent: 'Drafting agent' }))}
      ${tile('components-card--stats', 'Card', 'Cards, sections, stats', `<div style="width:100%">${Stat({ value: '42', label: 'Answers approved', key: true })}</div>`)}
      ${tile('components-table--default', 'Table', 'Data rows, status, actions', `<div class="card table-card" style="width:100%"><table class="dtable"><tbody><tr><td>Policy.pdf</td><td><span class="dst ok">Ready</span></td></tr></tbody></table></div>`)}
      ${tile('components-nav--sidebar', 'Nav', 'Sidebar items, counts, collapsed', `<div style="width:100%">${NavItem({ label: 'Dashboard', active: true })}</div>`)}
      ${tile('components-tabs--default', 'Tabs', 'Underline tabs with counts', `<div style="width:100%">${Tabs({ tabs: [{ label: 'To review', count: 20 }, { label: 'Approved' }] })}</div>`)}
      ${tile('components-chip--filter-group', 'Chip', 'Filter chips', Chips({ chips: [{ label: 'All', pressed: true }, { label: 'Drive' }, { label: 'Notion' }] }))}
      ${tile('components-filters--filters-applied', 'Filters', 'Search, filter menu, toggles', Segmented({ options: ['Cards', 'List'], selected: 0, size: 'sm' }))}
    </div>

    <p class="cover__foot">Use the toolbar Theme switch to see any page in dark. Source: <code>design-system/</code> in the lojo repo.</p>
  </div>`,
};
