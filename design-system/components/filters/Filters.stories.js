import { FilterBar, FilterMenu, ActiveFilters, Search, Segmented, CountChips } from './filters.js';
import { Guidelines } from '../../guidelines.js';

const OPTS = [{ label: 'Claims', count: 14 }, { label: 'Billing', count: 9 }, { label: 'Coverage', count: 22 }, { label: 'Onboarding', count: 5 }];
const wrap = (h, w = 560) => `<div style="max-width:${w}px;min-height:var(--space-38)">${h}</div>`;
const label = (t) => `<p style="margin:var(--space-20) 0 var(--space-10);font-size:var(--text-70);font-weight:var(--weight-bold);letter-spacing:var(--tracking-overline);text-transform:uppercase;color:var(--muted)">${t}</p>`;

export default {
  title: 'Components/Filters',
  render: (args) => wrap(FilterBar(args) + (args.open ? '<div style="height:200px"></div>' : '')),
  args: { placeholder: 'Search drafts', query: '', options: OPTS, selected: [], open: false },
  argTypes: { selected: { control: 'check', options: OPTS.map((o) => o.label) } },
};

export const Playground = {};
export const Default = {};
export const MenuOpen = { args: { open: true, selected: ['Claims'] } };
export const FiltersApplied = { args: { selected: ['Claims', 'Coverage'], query: 'refund' } };

export const Parts = {
  render: () => label('Search') + wrap(Search({ placeholder: 'Search sources' }), 360) +
    label('Filter menu') + FilterMenu({ options: OPTS, selected: ['Billing'], staticMenu: true }) +
    label('Active filters') + ActiveFilters({ selected: ['Claims', 'Coverage', 'Last 7 days'] }),
};

export const SegmentedToggle = {
  render: () => label('Large: switch the whole view') + Segmented({ options: ['Cards', 'List', 'Board'], selected: 0 }) +
    label('Small: inside a card or row') + Segmented({ options: ['Day', 'Week', 'Month'], selected: 1, size: 'sm' }) +
    label('Small, with a disabled option') + Segmented({ options: ['Day', 'Week', 'Month'], selected: 0, size: 'sm', disabled: [2] }),
};

export const CountChipGroup = {
  render: () => wrap(CountChips({ items: [
    { label: 'All', count: 128, pressed: true }, { label: 'Running', count: 2, dot: 'live' }, { label: 'Waiting on you', count: 7, dot: 'wait' },
    { label: 'Sync agent', count: 41 }, { label: 'Drafting agent', count: 36 }, { label: 'Publisher', count: 12 },
  ] }), 700),
  parameters: { chromatic: { pauseAnimationAtEnd: true } },
};

export const Guideline = {
  name: 'Do and don’t',
  parameters: { controls: { disable: true }, actions: { disable: true }, interactions: { disable: true } },
  render: () => Guidelines({
    intro: 'Filters narrow a list. Always show what’s on and give a one-click way back.',
    rules: [
      {
        do: { example: wrap(FilterBar({ selected: ['Claims', 'Coverage'], options: OPTS }), 400), text: 'Show every active filter as a chip under the bar, with Reset.' },
        dont: { example: wrap(FilterBar({ options: OPTS }).replace('lfbtn', 'lfbtn is-on'), 400), text: 'Don’t hide which filters are on inside the menu.' },
      },
      {
        do: { example: FilterMenu({ options: OPTS, selected: ['Claims'], staticMenu: true }), text: 'Show a count next to each option so people know what they’ll get.' },
        dont: { example: FilterMenu({ options: [{ label: 'Claims', count: 0 }, { label: 'Billing', count: 0 }, { label: 'Coverage', count: 0 }], staticMenu: true }), text: 'Don’t offer options that return nothing. Hide zero-count options.' },
      },
      {
        do: { example: Segmented({ options: ['Cards', 'List'], selected: 0 }), text: 'Use a segmented toggle to switch how the same list is shown.' },
        dont: { example: Segmented({ options: ['Claims', 'Billing', 'Coverage', 'Onboarding', 'Pricing'], selected: 0, size: 'sm' }), text: 'Don’t use it for many filter values. Use the Filter menu or chips.' },
      },
      {
        do: { example: wrap(Search({ placeholder: 'Search drafts' }), 300), text: 'Say what is being searched in the placeholder.' },
        dont: { example: wrap(Search({ placeholder: 'Type here…' }), 300), text: 'Don’t use a vague placeholder.' },
      },
    ],
  }),
};
