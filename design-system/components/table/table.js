import './table.css';
import '../card/card.css';
import '../button/button.css';
import { Button } from '../button/button.js';

const STATUS = { ok: 'Ready', run: 'Processing', fail: 'Failed', wait: 'Queued' };
const cell = (r) => `<td><div class="dname"><span class="ext">${r.ext}</span><span>${r.name}</span></div></td>`;

/** Data table: the prototype's .dtable inside a card */
export function Table({ rows = [], actions = true, openRow = -1, empty = 'No sources yet' } = {}) {
  const head = `<thead><tr><th>Name</th><th>Status</th><th class="num">Answers</th>${actions ? '<th class="tacts"></th>' : ''}</tr></thead>`;
  const body = rows.length
    ? rows.map((r, i) => `<tr class="is-row${i === openRow ? ' is-open' : ''}">${cell(r)}<td><span class="dst ${r.status}">${STATUS[r.status]}</span></td><td class="num">${r.answers}</td>${actions ? `<td class="tacts">${Button({ label: 'Open', variant: 'secondary', size: 'sm' })}${Button({ label: 'Remove', variant: 'ghost', size: 'sm' })}</td>` : ''}</tr>`).join('')
    : `<tr><td class="table-empty" colspan="${actions ? 4 : 3}">${empty}</td></tr>`;
  return `<div class="card table-card"><div class="dscroll"><table class="dtable">${head}<tbody>${body}</tbody></table></div></div>`;
}
