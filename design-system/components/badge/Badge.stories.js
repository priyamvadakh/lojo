import { Badge } from './badge.js';
const TONES = { rose: 'New', amber: 'Needs review', ok: 'Approved', err: 'Failed', info: 'Processing', muted: 'Draft' };
export default {
  title: 'Components/Badge',
  render: (args) => Badge(args),
  args: { label: 'New', tone: 'rose' },
  argTypes: { tone: { control: 'select', options: Object.keys(TONES) } },
};
export const Playground = {};
export const AllTones = {
  render: () => `<div style="display:flex;gap:var(--space-8);flex-wrap:wrap">${Object.entries(TONES).map(([tone, label]) => Badge({ tone, label })).join('')}</div>`,
};

import { Guidelines } from '../../guidelines.js';
export const Guideline = {
  name: 'Do and don’t',
  parameters: { controls: { disable: true }, actions: { disable: true }, interactions: { disable: true } },
  render: () => Guidelines({
    intro: 'Badges label a status. They are not buttons and are not clickable.',
    rules: [
      {
        do: { example: Badge({ tone: 'ok', label: 'Approved' }) + Badge({ tone: 'err', label: 'Failed' }) + Badge({ tone: 'amber', label: 'Needs review' }), text: 'Match the tone to the meaning: ok for done, err for failed, amber for waiting.' },
        dont: { example: Badge({ tone: 'err', label: 'Approved' }) + Badge({ tone: 'ok', label: 'Failed' }), text: 'Don’t pick a tone for its colour. Red “Approved” reads as a problem.' },
      },
      {
        do: { example: Badge({ tone: 'rose', label: 'New' }) + Badge({ tone: 'muted', label: 'Draft' }), text: 'Keep it to one or two words.' },
        dont: { example: Badge({ tone: 'info', label: 'This answer is being processed by the agent' }), text: 'Don’t write sentences in a badge. Put detail in the text beside it.' },
      },
      {
        do: { example: '<span style="display:flex;gap:var(--space-8);align-items:center"><b>Claims how-to</b>' + Badge({ tone: 'amber', label: 'Needs review' }) + '</span>', text: 'Use one badge per item, next to its name.' },
        dont: { example: Badge({ tone: 'rose', label: 'New' }) + Badge({ tone: 'amber', label: 'Review' }) + Badge({ tone: 'info', label: 'Synced' }) + Badge({ tone: 'muted', label: 'Draft' }), text: 'Don’t stack several badges on one item.' },
      },
    ],
  }),
};
