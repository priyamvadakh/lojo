import { Nav, NavItem } from './nav.js';
const ITEMS = [
  { icon: 'overview', label: 'Dashboard', active: true },
  { icon: 'documents', label: 'Sources' },
  { icon: 'review', label: 'Build', count: 20, hot: true },
  { icon: 'questions', label: 'Insights', count: 6 },
  { icon: 'approved', label: 'Distribute' },
  { icon: 'readout', label: 'Knowledge' },
  { icon: 'activity', label: 'Activity' },
];
export default {
  title: 'Components/Nav',
  render: (args) => Nav(args),
  args: { items: ITEMS, collapsed: false },
};
export const Sidebar = {};
export const Collapsed = { args: { collapsed: true } };
export const ItemStates = {
  render: () => `<div class="side"><nav>${[
    NavItem({ label: 'Default' }),
    NavItem({ label: 'Hover', state: 'hover' }),
    NavItem({ label: 'Active', active: true }),
    NavItem({ icon: 'review', label: 'With count', count: 6 }),
    NavItem({ icon: 'review', label: 'Hot count', count: 20, hot: true }),
  ].join('')}</nav></div>`,
};

import { Guidelines } from '../../guidelines.js';
const side = (items) => '<div class="side" style="width:220px"><nav>' + items.join('') + '</nav></div>';
export const Guideline = {
  name: 'Do and don’t',
  parameters: { controls: { disable: true }, actions: { disable: true }, interactions: { disable: true } },
  render: () => Guidelines({
    intro: 'The sidebar shows where you are. Exactly one item is active.',
    rules: [
      {
        do: { example: side([NavItem({ label: 'Dashboard', active: true }), NavItem({ icon: 'documents', label: 'Sources' })]), text: 'Mark only the current page as active.' },
        dont: { example: side([NavItem({ label: 'Dashboard', active: true }), NavItem({ icon: 'documents', label: 'Sources', active: true })]), text: 'Don’t highlight two items at once.' },
      },
      {
        do: { example: side([NavItem({ icon: 'review', label: 'Build', count: 20, hot: true }), NavItem({ icon: 'questions', label: 'Insights', count: 6 })]), text: 'Use the hot (rose) count only where someone needs to act now.' },
        dont: { example: side([NavItem({ icon: 'review', label: 'Build', count: 20, hot: true }), NavItem({ icon: 'questions', label: 'Insights', count: 6, hot: true }), NavItem({ icon: 'approved', label: 'Distribute', count: 3, hot: true })]), text: 'Don’t make every count hot: it stops meaning urgent.' },
      },
      {
        do: { example: side([NavItem({ icon: 'documents', label: 'Sources' })]), text: 'One or two word labels, with an icon.' },
        dont: { example: side([NavItem({ icon: 'documents', label: 'All your connected sources and files' })]), text: 'Don’t write long labels: they get cut off and hide in collapsed mode.' },
      },
    ],
  }),
};
