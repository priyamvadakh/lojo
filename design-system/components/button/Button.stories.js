import { Button } from './button.js';

const VARIANTS = ['primary', 'grad', 'secondary', 'ghost', 'danger'];
const row = (items) => `<div style="display:flex;gap:var(--space-12);align-items:center;flex-wrap:wrap">${items.join('')}</div>`;
const label = (t) => `<p style="margin:var(--space-16) 0 var(--space-8);font-size:var(--text-70);font-weight:var(--weight-bold);letter-spacing:var(--tracking-overline);text-transform:uppercase;color:var(--muted)">${t}</p>`;

export default {
  title: 'Components/Button',
  render: (args) => Button(args),
  args: { label: 'Approve', variant: 'primary', size: 'md', disabled: false, loading: false, icon: '', state: '' },
  argTypes: {
    variant: { control: 'select', options: VARIANTS },
    size: { control: 'inline-radio', options: ['md', 'sm'] },
    icon: { control: 'select', options: ['', 'plus', 'download', 'review'] },
    state: { control: 'inline-radio', options: ['', 'hover'] },
  },
};

export const Playground = {};
export const Primary = { args: { variant: 'primary' } };
export const Gradient = { args: { variant: 'grad', label: 'Start the loop' } };
export const Secondary = { args: { variant: 'secondary', label: 'Cancel' } };
export const Ghost = { args: { variant: 'ghost', label: 'Skip' } };
export const Danger = { args: { variant: 'danger', label: 'Delete' } };

export const AllVariantsAndStates = {
  render: () => [
    ['Default', {}], ['Hover', { state: 'hover' }], ['Small', { size: 'sm' }], ['With icon', { icon: 'plus' }],
    ['Loading', { loading: true }], ['Disabled', { disabled: true }],
  ].map(([t, extra]) => label(t) + row(VARIANTS.map((v) => Button({ label: v[0].toUpperCase() + v.slice(1), variant: v, ...extra })))).join(''),
};

import { Guidelines } from '../../guidelines.js';
export const Guideline = {
  name: 'Do and don’t',
  parameters: { controls: { disable: true }, actions: { disable: true }, interactions: { disable: true } },
  render: () => Guidelines({
    intro: 'Buttons start actions. Label them with a short verb in sentence case.',
    rules: [
      {
        do: { example: Button({ label: 'Approve' }) + Button({ label: 'Edit', variant: 'secondary' }) + Button({ label: 'Skip', variant: 'ghost' }), text: 'Use one primary button per area, with secondary or ghost buttons beside it.' },
        dont: { example: Button({ label: 'Approve' }) + Button({ label: 'Edit' }) + Button({ label: 'Skip' }), text: 'Don’t line up several primary buttons: nothing stands out.' },
      },
      {
        do: { example: Button({ label: 'Start the loop', variant: 'grad' }), text: 'Keep the gradient button for the one big moment on a page (start, connect, launch).' },
        dont: { example: Button({ label: 'Save', variant: 'grad' }) + Button({ label: 'Cancel', variant: 'grad' }), text: 'Don’t use the gradient for routine actions or more than once per view.' },
      },
      {
        do: { example: Button({ label: 'Delete source', variant: 'danger' }), text: 'Use danger for actions that remove or can’t be undone, and say what goes.' },
        dont: { example: Button({ label: 'OK', variant: 'danger' }), text: 'Don’t use danger to draw attention, or vague labels like “OK”.' },
      },
      {
        do: { example: Button({ label: 'Upload files', icon: 'plus' }) + Button({ label: 'Saving', loading: true }), text: 'Sentence case, verb first. Show a spinner while it works.' },
        dont: { example: Button({ label: 'UPLOAD FILES NOW', icon: 'plus' }) + Button({ label: 'Click here' }), text: 'Don’t shout in capitals or write “Click here”.' },
      },
    ],
  }),
};
