import { Tabs } from './tabs.js';
const TABS = [{ label: 'To review', count: 20 }, { label: 'Approved', count: 42 }, { label: 'Rejected', count: 3 }, { label: 'All' }];
export default {
  title: 'Components/Tabs',
  render: (args) => Tabs(args),
  args: { tabs: TABS, selected: 0, hover: -1 },
  argTypes: { selected: { control: { type: 'range', min: 0, max: 3 } } },
};
export const Default = {};
export const SecondSelected = { args: { selected: 1 } };
export const HoverOnUnselected = { args: { hover: 2 } };
export const WithoutCounts = { args: { tabs: TABS.map(({ label }) => ({ label })) } };

import { Guidelines } from '../../guidelines.js';
const w = (h) => '<div style="width:100%">' + h + '</div>';
export const Guideline = {
  name: 'Do and don’t',
  parameters: { controls: { disable: true }, actions: { disable: true }, interactions: { disable: true } },
  render: () => Guidelines({
    intro: 'Tabs switch between views of the same content. They don’t start actions.',
    rules: [
      {
        do: { example: w(Tabs({ tabs: [{ label: 'To review', count: 20 }, { label: 'Approved', count: 42 }, { label: 'Rejected', count: 3 }] })), text: 'Use tabs to filter one list, with a count on each.' },
        dont: { example: w(Tabs({ tabs: [{ label: 'Approve all' }, { label: 'Export' }, { label: 'Delete' }] })), text: 'Don’t use tabs as buttons for actions.' },
      },
      {
        do: { example: w(Tabs({ tabs: [{ label: 'To review' }, { label: 'Approved' }, { label: 'All' }] })), text: 'Keep it to two to five short tabs.' },
        dont: { example: w(Tabs({ tabs: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun', 'Last week'].map((label) => ({ label })) })), text: 'Don’t use tabs for long lists of options. Use a select instead.' },
      },
    ],
  }),
};
