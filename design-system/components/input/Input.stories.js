import { Input } from './input.js';
const OPTS = ['All sources', 'Google Drive', 'Notion', 'Uploads'];
const grid = (items) => `<div style="display:grid;gap:var(--space-20);max-width:420px">${items.join('')}</div>`;
export default {
  title: 'Components/Input',
  render: (args) => `<div style="max-width:420px">${Input(args)}</div>`,
  args: { type: 'text', label: 'Workspace name', placeholder: 'e.g. Support', value: '', hint: '', state: '', disabled: false, options: OPTS },
  argTypes: {
    type: { control: 'select', options: ['text', 'email', 'password', 'textarea', 'select'] },
    state: { control: 'inline-radio', options: ['', 'focus', 'error'] },
  },
};
export const Playground = {};
export const Text = { args: { label: '', hint: '' } };
export const Textarea = { args: { type: 'textarea', label: 'Why are you rejecting this answer?', placeholder: 'Add a note for the reviewer' } };
export const Select = { args: { type: 'select', label: 'Source', value: 'Notion' } };
export const AllStates = {
  render: () => grid([
    Input({ label: 'Default', placeholder: 'Placeholder text' }),
    Input({ label: 'Filled', value: 'Oslo support' }),
    Input({ label: 'Focus', value: 'Oslo support', state: 'focus' }),
    Input({ label: 'Error', value: 'oslo@', state: 'error', hint: 'Enter a full email address.' }),
    Input({ label: 'Disabled', value: 'Locked', disabled: true }),
    Input({ label: 'With hint', placeholder: 'name@company.com', type: 'email', hint: 'We send the invite here.' }),
    Input({ type: 'textarea', label: 'Textarea', placeholder: 'Write a note' }),
    Input({ type: 'select', label: 'Select', options: OPTS, value: 'Google Drive' }),
    Input({ type: 'select', label: 'Select, disabled', options: OPTS, disabled: true }),
  ]),
};

import { Guidelines } from '../../guidelines.js';
const w = (h) => '<div style="width:100%;max-width:300px">' + h + '</div>';
export const Guideline = {
  name: 'Do and don’t',
  parameters: { controls: { disable: true }, actions: { disable: true }, interactions: { disable: true } },
  render: () => Guidelines({
    intro: 'Every field needs a visible label. Placeholder text is only an example.',
    rules: [
      {
        do: { example: w(Input({ label: 'Work email', placeholder: 'name@company.com' })), text: 'Put a label above the field and an example in the placeholder.' },
        dont: { example: w(Input({ placeholder: 'Work email' })), text: 'Don’t use the placeholder as the label: it disappears once someone types.' },
      },
      {
        do: { example: w(Input({ label: 'Work email', value: 'eric@', state: 'error', hint: 'Enter a full email address, like eric@oslo.com.' })), text: 'Say what’s wrong and how to fix it, right under the field.' },
        dont: { example: w(Input({ label: 'Work email', value: 'eric@', state: 'error', hint: 'Invalid input.' })), text: 'Don’t show vague errors like “Invalid input”.' },
      },
      {
        do: { example: w(Input({ type: 'select', label: 'Source', options: ['Google Drive', 'Notion', 'Uploads'] })), text: 'Use a select for a short, fixed list of choices.' },
        dont: { example: w(Input({ label: 'Source', placeholder: 'Type Google Drive, Notion or Uploads' })), text: 'Don’t make people type an option they could pick.' },
      },
    ],
  }),
};
