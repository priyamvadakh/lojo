import { Chip, Chips } from './chip.js';
export default {
  title: 'Components/Chip',
  render: (args) => Chip(args),
  args: { label: 'Google Drive', pressed: false, state: '', disabled: false },
  argTypes: { state: { control: 'inline-radio', options: ['', 'hover'] } },
};
export const Playground = {};
export const AllStates = {
  render: () => Chips({ chips: [
    { label: 'Default' }, { label: 'Hover', state: 'hover' }, { label: 'Pressed', pressed: true }, { label: 'Disabled', disabled: true },
  ] }),
};
export const FilterGroup = {
  render: () => Chips({ chips: [{ label: 'All', pressed: true }, { label: 'Google Drive' }, { label: 'Notion' }, { label: 'Uploads' }, { label: 'Calls' }] }),
};

import { Guidelines } from '../../guidelines.js';
export const Guideline = {
  name: 'Do and don’t',
  parameters: { controls: { disable: true }, actions: { disable: true }, interactions: { disable: true } },
  render: () => Guidelines({
    intro: 'Chips filter what’s shown. Pressed chips are the active filters.',
    rules: [
      {
        do: { example: Chips({ chips: [{ label: 'All', pressed: true }, { label: 'Drive' }, { label: 'Notion' }] }), text: 'Start with an “All” chip so people can clear filters in one click.' },
        dont: { example: Chips({ chips: [{ label: 'Drive' }, { label: 'Notion' }, { label: 'Uploads' }] }), text: 'Don’t leave a filter group with no way back to everything.' },
      },
      {
        do: { example: Chips({ chips: [{ label: 'Drive' }, { label: 'Notion' }, { label: 'Calls' }] }), text: 'Short nouns, one or two words.' },
        dont: { example: Chips({ chips: [{ label: 'Show me only the Google Drive files' }] }), text: 'Don’t write long chip labels or sentences.' },
      },
      {
        do: { example: Chips({ chips: [{ label: 'Drive' }, { label: 'Notion' }] }), text: 'Use chips for filters and quick picks.' },
        dont: { example: Chips({ chips: [{ label: 'Save' }, { label: 'Delete' }] }), text: 'Don’t use chips for actions. Use a button.' },
      },
    ],
  }),
};
