import { Avatar, Who, AgentAvatar, AGENTS } from './avatar.js';
import { Guidelines } from '../../guidelines.js';
import '../badge/badge.css';

const row = (items) => `<div style="display:flex;gap:var(--space-16);align-items:center;flex-wrap:wrap">${items.join('')}</div>`;
const cap = (inner, t) => `<figure style="margin:0;display:grid;justify-items:center;gap:var(--space-8)">${inner}<figcaption class="sub" style="font-size:var(--text-76);color:var(--muted)">${t}</figcaption></figure>`;
const label = (t) => `<p style="margin:var(--space-20) 0 var(--space-10);font-size:var(--text-70);font-weight:var(--weight-bold);letter-spacing:var(--tracking-overline);text-transform:uppercase;color:var(--muted)">${t}</p>`;
const NAMES = ['Eric Ouisse', 'Lina Odeh', 'Jamal Latif', 'Sadaf Farman', 'Maya Chen', 'Omar Haddad'];
const SIZES = ['xs', 'sm', 'me', 'md', 'lg'];
const PX = { xs: 26, sm: 30, me: 34, md: 40, lg: 44 };

export default {
  title: 'Components/Avatar',
  render: (args) => Avatar(args),
  args: { name: 'Eric Ouisse', kind: 'person', size: 'md', pending: false, ink: false },
  argTypes: {
    kind: { control: 'inline-radio', options: ['person', 'org'] },
    size: { control: 'inline-radio', options: SIZES },
  },
};

export const Playground = {};

export const People = {
  render: () => label('Colour comes from the name') + row(NAMES.map((n) => cap(Avatar({ name: n }), n))) +
    label('Sizes') + row(SIZES.map((s) => cap(Avatar({ name: 'Eric Ouisse', size: s }), `${s} · ${PX[s]}px`))) +
    label('States') + row([cap(Avatar({ name: 'Eric Ouisse' }), 'Joined'), cap(Avatar({ name: 'Lina Odeh', pending: true }), 'Invited, pending')]),
};

export const Companies = {
  render: () => label('Companies and workspaces') + row(['Oslo', 'Acme Health', 'Northwind', 'Blue Bay'].map((n) => cap(Avatar({ name: n, kind: 'org' }), n))) +
    label('Sizes') + row(SIZES.map((s) => cap(Avatar({ name: 'Oslo', kind: 'org', size: s }), `${s} · ${PX[s]}px`))) +
    label('Ink tile') + row([cap(Avatar({ name: 'Oslo', kind: 'org', ink: true }), 'Current company (sidebar)')]),
};

export const WithName = {
  render: () => `<div style="display:grid;gap:var(--space-16);max-width:360px">${[
    Who({ name: 'Eric Ouisse', sub: 'eric@oslo.com', badge: ' <span class="badge badge--rose">Admin</span>' }),
    Who({ name: 'Lina Odeh', sub: 'Editor · Support' }),
    Who({ name: 'Jamal Latif', sub: 'Invited 2 days ago', pending: true }),
    Who({ name: 'Oslo', sub: 'oslo.com · 2 workspaces', kind: 'org' }),
    Who({ name: 'Maya Chen', sub: 'Viewer', size: 'sm' }),
  ].join('')}</div>`,
};

export const Agents = {
  render: () => label('Each agent has its own colour and job badge') + row(Object.keys(AGENTS).map((a) => cap(AgentAvatar({ agent: a }), a))) +
    label('States') + row([cap(AgentAvatar({ agent: 'Drafting agent' }), 'Idle'), cap(AgentAvatar({ agent: 'Drafting agent', state: 'run' }), 'Running'), cap(AgentAvatar({ agent: 'Drafting agent', state: 'off' }), 'Off')]),
  parameters: { chromatic: { pauseAnimationAtEnd: true } },
};

export const Guideline = {
  name: 'Do and don’t',
  parameters: { controls: { disable: true }, actions: { disable: true }, interactions: { disable: true } },
  render: () => Guidelines({
    intro: 'People are circles, companies are rounded squares, agents are the lojo cloud. The shape tells you what it is.',
    rules: [
      {
        do: { example: Avatar({ name: 'Eric Ouisse' }) + Avatar({ name: 'Oslo', kind: 'org' }), text: 'Use a circle for a person and a rounded square for a company or workspace.' },
        dont: { example: Avatar({ name: 'Eric Ouisse', kind: 'org' }) + Avatar({ name: 'Oslo' }), text: 'Don’t swap the shapes: a square person reads as a company.' },
      },
      {
        do: { example: Avatar({ name: 'Lina Odeh' }) + Avatar({ name: 'Lina Odeh', size: 'sm' }), text: 'Let the colour come from the name, so the same person always looks the same.' },
        dont: { example: Avatar({ name: 'Lina Odeh' }).replace(/avt\d/, 'avt1') + Avatar({ name: 'Lina Odeh' }).replace(/avt\d/, 'avt4'), text: 'Don’t pick colours by hand or change them between screens.' },
      },
      {
        do: { example: Who({ name: 'Jamal Latif', sub: 'Invited 2 days ago', pending: true }), text: 'Show people who haven’t joined yet with the dashed pending avatar.' },
        dont: { example: Who({ name: 'Jamal Latif', sub: 'Invited 2 days ago' }), text: 'Don’t give invited people a full avatar: it looks like they’ve joined.' },
      },
      {
        do: { example: AgentAvatar({ agent: 'Drafting agent', state: 'run' }) + Avatar({ name: 'Maya Chen' }), text: 'Agents get the cloud avatar. People keep initials, so you can tell who did what.' },
        dont: { example: Avatar({ name: 'Drafting agent' }) + `<span class="av av--p" style="background:var(--avatar-4)">${'<svg viewBox="0 0 24 24"><path d="M12 20h9"/><path d="M16.5 3.5a2.1 2.1 0 0 1 3 3L7 19l-4 1 1-4z"/></svg>'}</span>`, text: 'Don’t give agents initials or a person-style circle.' },
      },
    ],
  }),
};
