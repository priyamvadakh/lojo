import { Card, Section, Stat } from './card.js';
import { Button } from '../button/button.js';
const P = '<p style="margin:0">Answers drafted from your sources wait here until someone on the team approves them.</p>';
export default {
  title: 'Components/Card',
  render: (args) => `<div style="max-width:560px">${Card(args)}</div>`,
  args: { title: 'Review queue', sub: '20 drafts due Friday', actions: '', body: P },
};
export const Playground = {};
export const WithActions = { args: { actions: Button({ label: 'Open queue', variant: 'secondary', size: 'sm' }) } };
export const BodyOnly = { args: { title: '' } };
export const SectionPanel = {
  render: () => `<div style="max-width:640px">${Section({ title: 'This week', meta: 'Week 2 of 4', link: 'See all', body: P })}</div>`,
};
export const Stats = {
  render: () => `<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:var(--space-14);max-width:640px">${Stat({ value: '128', label: 'Sources connected' })}${Stat({ value: '42', label: 'Answers approved', key: true })}${Stat({ value: '7', label: 'Waiting on you' })}</div>`,
};

import { Guidelines } from '../../guidelines.js';
const w = (h) => '<div style="width:100%;max-width:340px">' + h + '</div>';
export const Guideline = {
  name: 'Do and don’t',
  parameters: { controls: { disable: true }, actions: { disable: true }, interactions: { disable: true } },
  render: () => Guidelines({
    intro: 'Cards group one topic. The title says what it is, actions sit on the right of the head.',
    rules: [
      {
        do: { example: w(Card({ title: 'Review queue', actions: Button({ label: 'Open', variant: 'secondary', size: 'sm' }), body: '<p class="sub">20 drafts due Friday</p>' })), text: 'Give each card one clear title and at most one or two actions in the head.' },
        dont: { example: w(Card({ title: 'Review queue', actions: Button({ label: 'Open', size: 'sm' }) + Button({ label: 'Edit', size: 'sm' }) + Button({ label: 'Share', size: 'sm' }), body: '<p class="sub">20 drafts due Friday</p>' })), text: 'Don’t crowd the head with buttons.' },
      },
      {
        do: { example: w(Card({ title: 'Sources', body: '<p class="sub">128 connected · 4 need attention</p>' })), text: 'Keep cards flat: one level, content inside.' },
        dont: { example: w(Card({ title: 'Sources', body: Card({ title: 'Drive', body: Card({ body: '<p class="sub">128 files</p>' }) }) })), text: 'Don’t nest cards inside cards.' },
      },
      {
        do: { example: '<div style="display:grid;grid-template-columns:1fr 1fr;gap:var(--space-12);width:100%">' + Stat({ value: '42', label: 'Answers approved', key: true }) + Stat({ value: '7', label: 'Waiting on you' }) + '</div>', text: 'Highlight the one number that matters most with the key stat.' },
        dont: { example: '<div style="display:grid;grid-template-columns:1fr 1fr;gap:var(--space-12);width:100%">' + Stat({ value: '42', label: 'Approved', key: true }) + Stat({ value: '7', label: 'Waiting', key: true }) + '</div>', text: 'Don’t highlight every stat.' },
      },
    ],
  }),
};
