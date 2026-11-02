import { Table } from './table.js';
const ROWS = [
  { ext: 'pdf', name: 'Policy wording.pdf', status: 'ok', answers: 34 },
  { ext: 'doc', name: 'Claims how-to.docx', status: 'run', answers: 12 },
  { ext: 'xls', name: 'Vet clinics UAE.xlsx', status: 'wait', answers: 0 },
  { ext: 'pdf', name: 'Old pricing 2023.pdf', status: 'fail', answers: 0 },
];
export default {
  title: 'Components/Table',
  render: (args) => Table(args),
  args: { rows: ROWS, actions: true, openRow: -1 },
};
export const Default = {};
export const SelectedRow = { args: { openRow: 1 } };
export const WithoutActions = { args: { actions: false } };
export const Empty = { args: { rows: [] } };

import { Guidelines } from '../../guidelines.js';
const mini = (cells) => '<div class="card table-card" style="width:100%"><table class="dtable"><thead><tr><th>Name</th><th class="num">Answers</th></tr></thead><tbody>' + cells + '</tbody></table></div>';
export const Guideline = {
  name: 'Do and don’t',
  parameters: { controls: { disable: true }, actions: { disable: true }, interactions: { disable: true } },
  render: () => Guidelines({
    intro: 'Tables are for comparing many rows of the same thing.',
    rules: [
      {
        do: { example: mini('<tr><td>Policy wording</td><td class="num">34</td></tr><tr><td>Claims how-to</td><td class="num">1,204</td></tr>'), text: 'Right-align numbers so the digits line up.' },
        dont: { example: mini('<tr><td>Policy wording</td><td>34</td></tr><tr><td>Claims how-to</td><td>1,204</td></tr>'), text: 'Don’t left-align number columns.' },
      },
      {
        do: { example: Table({ rows: [{ ext: 'pdf', name: 'Policy wording.pdf', status: 'ok', answers: 34 }] }), text: 'Put row actions in the last column: one main action and one quiet one.' },
        dont: { example: '<div class="card table-card" style="width:100%"><table class="dtable"><tbody><tr><td>Policy.pdf</td><td class="tacts">' + ['Open', 'Edit', 'Share', 'Delete'].map((l) => '<button class="btn btn--primary btn--sm">' + l + '</button>').join('') + '</td></tr></tbody></table></div>', text: 'Don’t fill each row with primary buttons.' },
      },
      {
        do: { example: Table({ rows: [], actions: false, empty: 'No sources yet. Connect Google Drive or upload files to start.' }), text: 'When there are no rows, say why and what to do next.' },
        dont: { example: Table({ rows: [], actions: false, empty: '—' }), text: 'Don’t leave an empty table with no explanation.' },
      },
    ],
  }),
};
