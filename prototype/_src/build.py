import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from shell import page

OUT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))



# ============================================================ OVERVIEW
OVERVIEW = dict(
  active='overview', title='Dashboard',
  desc='<!-- ASSUMPTION: a light home for the four weeks, not the analytics dashboards the proposal leaves out. Weekly review target (~20 drafts, due Friday) comes from the plan. check with Eric -->',
  css=r"""
  .hello{display:flex;align-items:center;gap:14px}
  .hello img{width:40px;height:40px;border-radius:22%}
  .hello h1{font-family:var(--display);font-weight:700;font-size:1.55rem;letter-spacing:-.02em;margin:0;color:#8E2F45}
  .hello p{margin:2px 0 0;font-size:.74rem;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:var(--muted)}
  /* loop status (header): ring with stats */
  .mini{display:flex;align-items:center;gap:14px;padding:8px 18px 8px 8px;border:1px solid var(--line-2);border-radius:14px;background:var(--panel);cursor:pointer;text-align:left;transition:border-color .15s ease,box-shadow .15s ease}
  .mini:hover{border-color:rgba(36,26,20,.28);box-shadow:0 10px 24px -18px rgba(36,26,20,.5)}
  .mini svg{width:52px;height:52px;flex:none}
  .mini .m-track{fill:none;stroke:rgba(36,26,20,.08);stroke-width:5}
  .mini .m-arc{fill:none;stroke:url(#miniGrad);stroke-width:5;stroke-linecap:round;transition:stroke-dasharray .4s ease}
  .mini text{font:800 13px "Outfit",sans-serif;fill:var(--ink)}
  .mini small{display:block;font-size:.62rem;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--muted)}
  .mini b{display:block;font-size:.92rem;font-weight:700;line-height:1.3}
  .mini em{display:block;font-style:normal;font-size:.76rem;color:var(--muted)}
  .mini .sep{width:1px;align-self:stretch;background:var(--line);margin:4px 2px}
  .mini .k{text-align:center}
  .mini .k b{font-family:var(--display);font-size:1.15rem;color:var(--rose)}
  /* next step */
  .next{display:grid;grid-template-columns:minmax(0,1.5fr) minmax(0,1fr);gap:0;padding:0;overflow:hidden}
  .next__main{padding:24px 26px;background:linear-gradient(135deg,#FFF6F2,#FFFDFB 60%);border-right:1px solid var(--line)}
  .next__main h2{font-family:var(--display);font-weight:700;font-size:1.5rem;letter-spacing:-.01em;margin:8px 0 4px}
  .next__main p{margin:0;color:var(--muted)}
  .target{margin:18px 0 20px}
  .target__row{display:flex;justify-content:space-between;font-size:.82rem;margin-bottom:6px}
  .target__row b{font-weight:700}
  .target__row span{color:var(--muted)}
  .target__bar{height:8px;border-radius:8px;background:rgba(36,26,20,.07);overflow:hidden;position:relative}
  .target__bar i{position:absolute;inset:0 auto 0 0;background:var(--brand-gradient);border-radius:8px}
  .target__bar u{position:absolute;top:-3px;bottom:-3px;width:2px;background:var(--ink);opacity:.35}
  .target small{display:block;margin-top:6px;font-size:.76rem;font-weight:600}
  .next__side{padding:18px 20px;display:grid;gap:8px;align-content:start}
  .next__side h3{margin:0 0 4px;font-size:.72rem;font-weight:800;letter-spacing:.12em;text-transform:uppercase;color:var(--muted)}
  .also{display:grid;grid-template-columns:34px 1fr auto;gap:12px;align-items:center;padding:10px;border-radius:12px;text-decoration:none;color:inherit}
  .also:hover{background:var(--bg-soft);text-decoration:none}
  .also .ic{width:34px;height:34px;border-radius:10px;display:grid;place-items:center;background:var(--bg-soft)}
  .also b{display:block;font-size:.88rem;font-weight:600}
  .also span{color:var(--muted);font-size:.78rem}
  .also em{font-style:normal;color:var(--muted)}
  /* worth knowing + feed */
  .duo{display:grid;grid-template-columns:minmax(0,1.2fr) minmax(0,1fr);gap:22px;margin-bottom:22px}
  .duo .sec{margin:0}
  .finding{display:grid;gap:12px}
  .finding h3{font-family:var(--display);font-weight:700;font-size:1.15rem;margin:0;line-height:1.3}
  .finding p{margin:0;color:var(--muted);font-size:.86rem}
  .vs{display:grid;grid-template-columns:1fr auto 1fr;gap:10px;align-items:stretch}
  .vs blockquote{margin:0;padding:10px 12px;border-radius:10px;font-size:.82rem;background:var(--bg-soft)}
  .vs blockquote.warn{background:#FBF1E4}
  .vs blockquote em{display:block;font-style:normal;font-size:.7rem;font-weight:700;color:var(--muted);margin-bottom:3px}
  .vs .x{align-self:center;font-size:.7rem;font-weight:800;color:var(--muted)}
  .feed{list-style:none;margin:0;padding:0;display:grid}
  .feed li{display:grid;grid-template-columns:30px 1fr;gap:12px;padding:10px 0;border-top:1px solid var(--line)}
  .feed li:first-child{border-top:0;padding-top:0}
  .feed .dot{width:30px;height:30px;border-radius:9px;display:grid;place-items:center;background:var(--bg-soft);color:var(--muted)}
  .feed .dot svg{width:15px;height:15px}
  .feed b{display:block;font-size:.86rem;font-weight:600}
  .feed span{color:var(--muted);font-size:.76rem}
  /* tiles */
  .tiles{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:16px}
  .tile{position:relative;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;gap:6px;min-height:188px;padding:22px 18px;border:1px solid var(--line-2);border-radius:14px;background:var(--panel);color:inherit;text-decoration:none;transition:box-shadow .2s ease,transform .2s ease}
  a.tile:hover{box-shadow:0 16px 30px -24px rgba(36,26,20,.5);transform:translateY(-2px);text-decoration:none}
  .tile__lbl{display:inline-flex;align-items:center;gap:6px;font-size:.72rem;font-weight:800;letter-spacing:.1em;text-transform:uppercase;color:var(--ink)}
  .tip{position:relative;width:16px;height:16px;border-radius:50%;background:#8E2F45;color:#fff;font-style:normal;font-size:.62rem;font-weight:800;display:grid;place-items:center;letter-spacing:0;cursor:help}
  .tip::after{content:attr(data-tip);position:absolute;bottom:calc(100% + 8px);left:50%;transform:translate(-50%,4px);width:220px;padding:9px 11px;border-radius:10px;background:var(--ink);color:#fff;font-size:.74rem;font-weight:500;line-height:1.4;letter-spacing:0;text-transform:none;text-align:left;opacity:0;pointer-events:none;transition:opacity .15s ease,transform .15s ease;z-index:5}
  .tip:hover::after,.tip:focus::after{opacity:1;transform:translate(-50%,0)}
  .tile__val{font-family:var(--display);font-weight:800;font-size:2.1rem;letter-spacing:-.02em;line-height:1.05}
  .tile__sub{color:var(--muted);font-size:.84rem;line-height:1.45}
  .tile__tag{position:absolute;top:12px;right:12px;height:22px;padding:0 9px;border-radius:999px;font-size:.68rem;font-weight:700;display:inline-flex;align-items:center;color:#fff}
  .tile__go{position:absolute;right:14px;bottom:12px;color:var(--ink)}
  .tile--soft{background:var(--bg-soft)}
  .tile--ok{background:#F2F7EC;border-color:#DCE8CE}
  .tile--ok .tile__tag{background:var(--success)}
  .tile--ok .tile__val{color:#2F6B47}
  .tile--warn{background:#FBF1E4;border-color:#F0DCC0}
  .tile--warn .tile__tag{background:#C98A2E}
  .tile--warn .tile__val{color:#8A5A12}
  .gauge{position:relative;width:128px;height:72px}
  .gauge svg{width:128px;height:72px;overflow:visible}
  .gauge .g-bg{fill:none;stroke:rgba(36,26,20,.08);stroke-width:10;stroke-linecap:round}
  .gauge .g-fg{fill:none;stroke-width:10;stroke-linecap:round}
  .gauge b{position:absolute;left:0;right:0;bottom:2px;font-family:var(--display);font-weight:800;font-size:1.2rem}
  .checks{display:flex;flex-wrap:wrap;gap:8px 18px;align-items:center;margin-top:16px;padding-top:14px;border-top:1px solid var(--line);font-size:.84rem}
  .checks span{display:inline-flex;align-items:center;gap:6px}
  .checks .ok{color:var(--success);font-weight:700}
  .checks .muted{color:var(--muted)}
  .checks a{margin-left:auto;color:var(--ink);font-size:.82rem}
  /* strips */
  .strip{display:flex;align-items:center;gap:14px;flex-wrap:wrap;padding:14px 18px;border-radius:14px;border:1px dashed var(--line-2);background:rgba(255,255,255,.7);margin-bottom:22px;font-size:.88rem}
  .strip img{width:30px;height:30px;border-radius:22%;opacity:.55}
  .strip b{font-weight:700}
  .strip .spacer{flex:1}
  .scope{display:flex;align-items:center;gap:12px;flex-wrap:wrap;padding:12px 18px;border-radius:14px;background:#F2F7EC;border:1px solid #DCE8CE;font-size:.86rem}
  .scope .ok{width:24px;height:24px;border-radius:50%;background:var(--panel);color:var(--success);display:grid;place-items:center;font-weight:800;font-size:.75rem}
  .scope .spacer{flex:1}
  .scope-more{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-top:12px;font-size:.84rem}
  .scope-more div{padding:14px 16px;border-radius:12px;background:var(--panel);border:1px solid var(--line)}
  .scope-more h4{margin:0 0 6px;font-size:.7rem;letter-spacing:.1em;text-transform:uppercase;color:var(--muted)}
  .scope-more ul{margin:0;padding-left:18px;display:grid;gap:4px;color:var(--muted)}
  @media (max-width:1320px){.tiles{grid-template-columns:repeat(2,minmax(0,1fr))}.tile{min-height:160px}}
  @media (max-width:1180px){.next,.duo{grid-template-columns:1fr}.next__main{border-right:0;border-bottom:1px solid var(--line)}.scope-more{grid-template-columns:1fr}}
  .loopdlg{border:0;padding:0;border-radius:20px;width:min(760px,calc(100vw - 32px));box-shadow:0 40px 90px -30px rgba(36,26,20,.5);color:var(--ink)}
  .loopdlg::backdrop{background:rgba(36,26,20,.35);backdrop-filter:blur(2px)}
  .loopdlg[open]{animation:dlgIn .35s cubic-bezier(.2,.8,.2,1)}
  @keyframes dlgIn{from{opacity:0;transform:translateY(12px) scale(.98)}}
  .loopdlg__head{position:relative;text-align:center;padding:22px 24px 0}
  .loopdlg[open]{padding-bottom:18px}
  .loopdlg__head h2{font-family:var(--display);font-weight:700;font-size:1.25rem;margin:6px 0 0}
  .loopdlg__x{position:absolute;right:20px;top:20px;width:36px;height:36px;border-radius:50%;border:1px solid var(--line-2);background:var(--panel);font-size:1.2rem;cursor:pointer;color:var(--muted)}
  .loopdlg__x:hover{background:var(--bg-soft);color:var(--ink)}
  .loopdlg__foot{margin:0;padding:0 24px 22px;text-align:center;color:var(--muted);font-size:.8rem}
  .lp{position:relative;width:560px;height:470px;margin:0 auto;max-width:100%}
  .lp > svg{position:absolute;inset:0;width:100%;height:100%;overflow:visible}
  .lp__track{fill:none;stroke:rgba(232,93,117,.4);stroke-width:1.8;stroke-dasharray:4 7;stroke-linecap:round;animation:drift 2.2s linear infinite}
  @keyframes drift{to{stroke-dashoffset:-22}}
  .lp__prog{fill:none;stroke:url(#lpGrad);stroke-width:3;stroke-linecap:round}
  .lp__tri{fill:var(--rose)}
  .lp__nodes{list-style:none;margin:0;padding:0}
  .lp__nodes li{position:absolute;width:0;height:0}
  .lp__nodes a{position:absolute;left:0;top:0;transform:translate(-50%,-50%);display:block;text-decoration:none;color:inherit}
  .lp__n{width:62px;height:62px;border-radius:50%;display:grid;place-items:center;background:var(--panel);border:2px solid rgba(232,93,117,.25);color:var(--muted);transition:transform .2s ease,box-shadow .2s ease}
  .lp__n svg{width:20px;height:20px;fill:none;stroke:currentColor;stroke-width:1.8;stroke-linecap:round;stroke-linejoin:round}
  .lp__nodes a:hover .lp__n{transform:scale(1.07)}
  .lp__nodes li.gate .lp__n{width:42px;height:42px;border-color:var(--rose);color:var(--rose)}
  .lp__nodes li.is-done .lp__n{background:var(--rose);border-color:var(--rose);color:#fff;box-shadow:0 12px 24px -14px rgba(232,93,117,.8)}
  .lp__nodes li.is-now .lp__n{background:var(--amber);border-color:var(--amber);color:#fff;box-shadow:0 0 0 7px var(--amber-soft)}
  .lp__t{position:absolute;width:170px}
  .lp__t small{display:none;width:max-content;margin-bottom:4px;padding:2px 8px;border-radius:999px;font-size:.58rem;font-weight:700;letter-spacing:.12em;text-transform:uppercase;background:var(--amber-soft);color:#8A6212}
  .lp__nodes li.is-now .lp__t small{display:block}
  .lp__t b{display:block;font-family:var(--display);font-weight:700;font-size:.95rem;white-space:nowrap}
  .lp__t span{display:block;color:var(--muted);font-size:.74rem;line-height:1.35;margin-top:2px}
  .lp__nodes a:hover .lp__t b{color:#B73C54}
  [data-side="top"] .lp__t{left:50%;bottom:calc(100% + 10px);transform:translateX(-50%);text-align:center}
  [data-side="top"] .lp__t small{margin-inline:auto}
  [data-side="bottom"] .lp__t{left:50%;top:calc(100% + 10px);transform:translateX(-50%);text-align:center}
  [data-side="bottom"] .lp__t small{margin-inline:auto}
  [data-side="right"] .lp__t{left:calc(100% + 14px);top:50%;transform:translateY(-50%)}
  [data-side="left"] .lp__t{right:calc(100% + 14px);top:50%;transform:translateY(-50%);text-align:right}
  [data-side="left"] .lp__t small{margin-left:auto}
  .lp__center{position:absolute;left:280px;top:235px;transform:translate(-50%,-50%);width:200px;text-align:center;pointer-events:none}
  .lp__center small{display:block;font-size:.62rem;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:var(--rose)}
  .lp__center b{display:block;font-family:var(--display);font-weight:700;font-size:1.15rem;margin:4px 0 6px}
  .lp__center span{display:block;color:var(--muted);font-size:.74rem;line-height:1.4}
""",
  body=r"""
    <div class="head">
      <div class="hello">
        <img src="assets/lojo-icon.png" alt="" width="40" height="40">
        <div><h1 id="ovTitle">Good evening, Sara</h1><p id="ovDate"></p></div>
      </div>
      <span class="spacer"></span>
      <button class="mini" id="loopBtn" type="button" aria-label="Open the loop">
        <svg viewBox="0 0 52 52" aria-hidden="true"><defs><linearGradient id="miniGrad" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#E85D75"/><stop offset="1" stop-color="#FFB199"/></linearGradient></defs>
          <circle class="m-track" cx="26" cy="26" r="21"/><circle class="m-arc" id="miniArc" cx="26" cy="26" r="21" transform="rotate(-90 26 26)"/><text id="miniFrac" x="26" y="30.5" text-anchor="middle">4/5</text></svg>
        <span><small>Your loop</small><b id="miniNow">Validation</b><em id="miniWhy">10 drafts waiting</em></span>
        <span class="sep"></span>
        <span class="k"><small>Approved</small><b id="miniK">6</b></span>
      </button>
    </div>

    <dialog class="loopdlg" id="loopDlg" aria-labelledby="loopDlgH">
      <div class="loopdlg__head">
        <div><p class="label">Your loop</p><h2 id="loopDlgH">Where you are in the loop</h2></div>
        <button class="loopdlg__x" id="loopX" type="button" aria-label="Close">×</button>
      </div>
      <div class="lp" id="lp">
        <svg viewBox="0 0 560 470" aria-hidden="true">
          <defs><linearGradient id="lpGrad" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#E85D75"/><stop offset="1" stop-color="#FFB199"/></linearGradient></defs>
          <circle cx="280" cy="235" r="128" fill="#FBF1F2"/>
          <circle class="lp__track" cx="280" cy="235" r="150"/>
          <circle class="lp__prog" id="lpProg" cx="280" cy="235" r="150" transform="rotate(-90 280 235)"/>
          <g id="lpTris"></g>
        </svg>
        <ol class="lp__nodes" id="lpNodes"></ol>
        <div class="lp__center"><small id="lpWeek">Week 3 of 4</small><b id="lpNow">Validation</b><span>The loop keeps running: new drafts land in review as your documents change.</span></div>
      </div>
    </dialog>

    <section class="sec next" aria-labelledby="nextH">
      <div class="next__main">
        <p class="label">Up next</p>
        <h2 id="nextH">Review 10 drafts</h2>
        <p id="nextSub"></p>
        <div class="target">
          <div class="target__row"><b id="tgtTxt"></b><span id="tgtDue"></span></div>
          <div class="target__bar"><i id="tgtBar"></i><u id="tgtMark"></u></div>
          <small id="tgtPace"></small>
        </div>
        <a class="btn btn--grad" href="review.html" id="nextCta">Start reviewing →</a>
      </div>
      <div class="next__side">
        <h3>Also waiting on you</h3>
        <div id="also"></div>
      </div>
    </section>

    <div class="duo">
      <section class="sec" aria-labelledby="fH">
        <div class="sec__head"><h2 id="fH">Worth knowing</h2><span>· Found in your documents</span></div>
        <div class="finding">
          <h3>Your help page and your pricing disagree about SSO</h3>
          <div class="vs">
            <blockquote class="warn"><em>Help Center · 9 months old</em>“SSO is an Enterprise-only feature.”</blockquote>
            <span class="x">VS</span>
            <blockquote><em>Pricing &amp; plans 2026 · p. 4</em>“SAML single sign-on is available to Growth and Scale workspaces.”</blockquote>
          </div>
          <p>Sales calls back the 2026 pricing. Customers reading the help page are being told the wrong thing.</p>
          <div><a class="btn btn--secondary btn--sm" href="review.html">See the draft answer →</a></div>
        </div>
      </section>
      <section class="sec" aria-labelledby="feedH">
        <div class="sec__head"><h2 id="feedH">Since you last looked</h2></div>
        <ul class="feed" id="feed"></ul>
      </section>
    </div>

    <section class="sec" aria-labelledby="s1">
      <div class="sec__head"><h2 id="s1">Your knowledge today</h2><span>· What Nimbus Pay has in lojo right now</span></div>
      <div class="tiles" id="today"></div>
      <div class="checks" id="checks"></div>
    </section>

    <div class="strip">
      <img src="assets/lojo-icon.png" alt="">
      <span><b>Coming in week 4:</b> the chat opens for your team, and the readout lands.</span>
      <span class="spacer"></span>
      <a class="btn btn--secondary btn--sm" href="chat.html">Preview the chat →</a>
    </div>

    <!-- ASSUMPTION: server location wording is a placeholder until the week-1 sign-off is written up. check with Eric -->
    <div class="scope">
      <span class="ok">✓</span>
      <span id="scopeBy"></span>
      <span class="spacer"></span>
      <button class="btn btn--ghost btn--sm" id="scopeToggle" aria-expanded="false">Details</button>
    </div>
    <div class="scope-more" id="scopeMore" hidden>
      <div><h4>In scope</h4><ul><li>10 documents you sent us, on one lojo-run server</li><li>One fixed model, called through our proxy</li><li>Personal details are not removed automatically</li></ul></div>
      <div><h4>Not in this phase</h4><ul><li>Roles and permissions</li><li>Publishing to a help centre or widget</li><li>Live sources such as mail and calls</li><li>Dashboards, billing and uptime guarantees</li></ul></div>
    </div>
""",
  js=r"""
const LOOP_ICON = {
  src: '<svg viewBox="0 0 24 24"><ellipse cx="12" cy="6" rx="7" ry="3"/><path d="M5 6v6c0 1.7 3.1 3 7 3s7-1.3 7-3V6M5 12v6c0 1.7 3.1 3 7 3s7-1.3 7-3v-6"/></svg>',
  ins: '<svg viewBox="0 0 24 24"><path d="M3 17l6-6 4 4 8-8"/><path d="M15 7h6v6"/></svg>',
  bld: '<svg viewBox="0 0 24 24"><path d="M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8z"/><path d="M14 3v5h5M9 13h6M9 17h4"/></svg>',
  val: '<svg viewBox="0 0 24 24"><path d="M5 12.5l4.5 4.5L19 7.5"/></svg>',
  dis: '<svg viewBox="0 0 24 24"><path d="M21 3 10 14M21 3l-7 18-4-7-7-4z"/></svg>',
};
function renderLoop() {
  const c = counts(), CX = 280, CY = 235, R = 150, rad = (d) => d * Math.PI / 180;
  const valNow = c.pending > 0;
  const stages = [
    { a: -90, side: 'top', ic: 'src', t: '01 Source', s: c.docs + ' documents · ' + c.passages + ' passages', href: 'documents.html', st: 'is-done' },
    { a: 0, side: 'right', ic: 'ins', t: '02 Insights', s: c.questions + ' questions · ' + c.gaps + ' gaps', href: 'questions.html', st: 'is-done' },
    { a: 90, side: 'bottom', ic: 'bld', t: '03 Build', s: c.drafts + ' drafts with sources', href: 'review.html', st: 'is-done' },
    { a: 135, side: 'left', ic: 'val', t: 'Validation', s: valNow ? c.pending + ' drafts waiting on you' : 'First batch reviewed', href: 'review.html', st: valNow ? 'is-now' : 'is-done', gate: 1 },
    { a: 180, side: 'left', ic: 'dis', t: '04 Distribute', s: c.approved + ' approved · chat to try', href: 'chat.html', st: valNow ? '' : 'is-now' },
  ];
  $('lpNodes').innerHTML = stages.map(s => '<li class="' + s.st + (s.gate ? ' gate' : '') + '" data-side="' + s.side + '" style="left:' + (CX + R * Math.cos(rad(s.a))).toFixed(1) + 'px;top:' + (CY + R * Math.sin(rad(s.a))).toFixed(1) + 'px">' +
    '<a href="' + s.href + '"><span class="lp__n">' + LOOP_ICON[s.ic] + '</span><span class="lp__t"><small>You’re here</small><b>' + s.t + '</b><span>' + esc(s.s) + '</span></span></a></li>').join('');
  $('lpTris').innerHTML = [-45, 45, 160, 225].map(a => '<path class="lp__tri" d="M-5 -5 L5 0 L-5 5 Z" transform="translate(' + (CX + R * Math.cos(rad(a))).toFixed(1) + ' ' + (CY + R * Math.sin(rad(a))).toFixed(1) + ') rotate(' + (a + 90) + ')"/>').join('');
  const now = stages.find(s => s.st === 'is-now'), C = 2 * Math.PI * R, frac = (now.a + 90) / 360;
  const prog = $('lpProg'); prog.setAttribute('stroke-dasharray', C.toFixed(1)); prog.setAttribute('stroke-dashoffset', (C * (1 - frac)).toFixed(1));
  $('lpWeek').textContent = 'Week ' + POC_WEEK + ' of 4';
  $('lpNow').textContent = now.t;
}
$('loopBtn').addEventListener('click', () => { renderLoop(); $('loopDlg').showModal(); });
$('loopX').addEventListener('click', () => $('loopDlg').close());
$('loopDlg').addEventListener('click', (e) => { if (e.target === $('loopDlg')) $('loopDlg').close(); });
function gauge(pct, color) {
  const L = Math.PI * 50, v = Math.max(0, Math.min(1, pct));
  return '<div class="gauge"><svg viewBox="0 0 128 72" aria-hidden="true"><path class="g-bg" d="M14 66 A50 50 0 0 1 114 66"/>' +
    '<path class="g-fg" d="M14 66 A50 50 0 0 1 114 66" stroke="' + color + '" stroke-dasharray="' + (L * v).toFixed(1) + ' ' + L.toFixed(1) + '"/></svg><b style="color:' + color + '">' + Math.round(v * 100) + '%</b></div>';
}
const tip = (t) => '<i class="tip" tabindex="0" data-tip="' + esc(t) + '">i</i>';
const ICON = {
  q: '<svg class="i" viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/><path d="M9.5 9.5a2.5 2.5 0 1 1 3.5 2.3c-.6.3-1 .8-1 1.5V14M12 17h.01"/></svg>',
  gap: '<svg class="i" viewBox="0 0 24 24"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></svg>',
  hand: '<svg class="i" viewBox="0 0 24 24"><path d="M12 9v4M12 17h.01"/><path d="M10.3 3.9 1.8 18a2 2 0 0 0 1.7 3h17a2 2 0 0 0 1.7-3L13.7 3.9a2 2 0 0 0-3.4 0z"/></svg>',
  sync: '<svg class="i" viewBox="0 0 24 24"><path d="M3 12a9 9 0 0 1 15.5-6.2L21 8M21 3v5h-5M21 12a9 9 0 0 1-15.5 6.2L3 16M3 21v-5h5"/></svg>',
  check: '<svg class="i" viewBox="0 0 24 24"><path d="M5 12l5 5 9-10"/></svg>',
  doc: '<svg class="i" viewBox="0 0 24 24"><path d="M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8z"/><path d="M14 3v5h5"/></svg>',
};
const TARGET = 20, DUE = 'Fri 2 Oct';
function miniLoop(c) {
  const valNow = c.pending > 0, idx = valNow ? 4 : 5, L = 2 * Math.PI * 21;
  $('miniArc').setAttribute('stroke-dasharray', (L * idx / 5).toFixed(1) + ' ' + L.toFixed(1));
  $('miniFrac').textContent = idx + '/5';
  $('miniNow').textContent = valNow ? 'Validation' : '04 Distribute';
  $('miniWhy').textContent = valNow ? c.pending + ' draft' + (c.pending === 1 ? '' : 's') + ' waiting' : 'Chat ready to try';
  $('miniK').textContent = c.approved;
}
function render() {
  const c = counts();
  let first = 'Sara';
  try { const u = JSON.parse(sessionStorage.getItem('lojo-user')); if (u && u.name) first = u.name.trim().split(' ')[0]; } catch (e) {}
  const hr = new Date().getHours();
  $('ovTitle').textContent = (hr < 12 ? 'Good morning' : hr < 18 ? 'Good afternoon' : 'Good evening') + ', ' + first;
  $('ovDate').textContent = new Date().toLocaleDateString('en-GB', { weekday: 'long', day: 'numeric', month: 'long' }) + ' · week ' + POC_WEEK + ' of 4';
  miniLoop(c);

  // up next + weekly target
  const decided = c.approved + c.final, mins = Math.max(1, Math.round(c.pending * 1.2));
  if (c.pending) {
    $('nextH').textContent = 'Review ' + c.pending + ' draft' + (c.pending > 1 ? 's' : '');
    $('nextSub').textContent = 'About ' + mins + ' minutes. Approve, edit, or reject with a reason; a rejected draft is written again once.';
    $('nextCta').textContent = 'Start reviewing →'; $('nextCta').href = 'review.html';
  } else {
    $('nextH').textContent = 'Try the chat';
    $('nextSub').textContent = 'The first batch is reviewed. Ask it questions: it answers only from what you approved.';
    $('nextCta').textContent = 'Open the chat →'; $('nextCta').href = 'chat.html';
  }
  // expected pace: Monday → Friday, today is Wednesday
  const expected = Math.round(TARGET * 0.6);
  $('tgtTxt').textContent = decided + ' of about ' + TARGET + ' drafts reviewed this week';
  $('tgtDue').textContent = 'Due ' + DUE;
  $('tgtBar').style.width = Math.min(100, decided / TARGET * 100) + '%';
  $('tgtMark').style.left = (expected / TARGET * 100) + '%';
  const ahead = decided >= expected;
  $('tgtPace').textContent = ahead ? '✓ On pace for Friday' : '⚠ ' + (expected - decided) + ' behind the pace for Friday';
  $('tgtPace').style.color = ahead ? 'var(--success)' : '#A5561A';

  const also = [];
  if (c.final) also.push({ ic: 'hand', t: c.final + ' draft' + (c.final > 1 ? 's need' : ' needs') + ' a human answer', s: 'Rejected twice', href: 'review.html' });
  if (c.needCall) also.push({ ic: 'q', t: 'Say whether ' + c.needCall + ' question' + (c.needCall > 1 ? 's matter' : ' matters'), s: 'Only those get drafted', href: 'questions.html' });
  if (c.gaps) also.push({ ic: 'gap', t: c.gaps + ' gaps need a source', s: 'Send a document or add them as questions', href: 'questions.html#gaps' });
  $('also').innerHTML = also.length ? also.map(i => '<a class="also" href="' + i.href + '"><span class="ic">' + ICON[i.ic] + '</span><div><b>' + esc(i.t) + '</b><span>' + esc(i.s) + '</span></div><em>→</em></a>').join('') : '<p class="sub">Nothing else right now.</p>';

  // since you last looked
  const rewrites = DRAFTS.filter(r => decision(r).redrafted).length;
  const feed = [
    { ic: 'sync', t: rewrites + ' rejected draft' + (rewrites === 1 ? ' was' : 's were') + ' written again', s: 'Using your reasons · overnight' },
    { ic: 'q', t: '4 new questions found', s: 'In Sales call notes, Billing FAQ and your help pages · yesterday' },
    { ic: 'doc', t: 'Security overview indexed', s: '51 passages, searchable by meaning · yesterday' },
    { ic: 'check', t: 'You approved ' + c.approved + ' answers', s: 'They’re in the store, ready for the chat · Tue 29 Sep' },
  ];
  $('feed').innerHTML = feed.map(f => '<li><span class="dot">' + ICON[f.ic] + '</span><div><b>' + esc(f.t) + '</b><span>' + esc(f.s) + '</span></div></li>').join('');

  // merged tiles
  const yours = allQuestions().filter(q => q.origin === 'you').length;
  $('today').innerHTML = [
    '<a class="tile tile--soft" href="review.html">' + gauge(decided / c.drafts, '#4F7A2F') + '<span class="tile__lbl">Review progress ' + tip('Drafts in the first batch that you have approved, edited or left for a human answer.') + '</span><span class="tile__sub">' + decided + ' of ' + c.drafts + ' decided · ' + c.approved + ' approved</span><span class="tile__go">→</span></a>',
    '<a class="tile tile--ok" href="documents.html"><span class="tile__tag">Indexed</span><span class="tile__lbl">Documents ' + tip('Documents you sent us. Their text is pulled out, split into passages and indexed by meaning.') + '</span><span class="tile__val">' + c.docs + '</span><span class="tile__sub">' + c.pages + ' pages · ' + c.passages + ' passages</span></a>',
    '<a class="tile' + (c.needCall ? ' tile--warn' : '') + '" href="questions.html">' + (c.needCall ? '<span class="tile__tag">' + c.needCall + ' need your call</span>' : '') + '<span class="tile__lbl">Questions ' + tip('Questions your documents answer, found by the agent, plus the ones you added.') + '</span><span class="tile__val">' + c.questions + '</span><span class="tile__sub">' + (c.questions - yours) + ' found · ' + yours + ' from you</span></a>',
    '<a class="tile' + (c.gaps ? ' tile--warn' : ' tile--ok') + '" href="questions.html#gaps">' + (c.gaps ? '<span class="tile__tag">Needs input</span>' : '') + '<span class="tile__lbl">Gaps ' + tip('Things your documents refer to but never explain. Expected at this stage: send a document or answer them yourself.') + '</span><span class="tile__val">' + c.gaps + '</span><span class="tile__sub">Referred to, never explained</span></a>',
  ].join('');

  // outcome checks; approval rate stays neutral until there are enough decisions
  const rate = decided ? Math.round(c.approved / decided * 100) : 0, early = decided < 10;
  $('checks').innerHTML = '<span><span class="ok">✓</span>Every draft shows its sources</span>' +
    '<span><span class="ok">✓</span>' + rewrites + ' rejected draft' + (rewrites === 1 ? '' : 's') + ' rewritten once</span>' +
    '<span class="' + (early ? 'muted' : '') + '">Approval rate ' + rate + '% · ' + decided + ' decided' + (early ? ' (too early to judge)' : '') + '</span>' +
    '<span class="muted">Processing $18.40 · $1.84 per document</span>' +
    '<a href="readout.html">See readout →</a>';

  $('scopeBy').innerHTML = '<b>Scope signed off</b> by ' + esc(ST.scope.by) + ' on ' + esc(ST.scope.at) + ' · personal details are not removed automatically';
}
$('scopeToggle').addEventListener('click', () => {
  const m = $('scopeMore'); m.hidden = !m.hidden;
  $('scopeToggle').setAttribute('aria-expanded', !m.hidden); $('scopeToggle').textContent = m.hidden ? 'Details' : 'Hide';
});
render();
""")

# ============================================================ DOCUMENTS
DOCUMENTS = dict(
  active='documents', title='Documents',
  css=r"""
  .scope{display:grid;grid-template-columns:36px 1fr auto;gap:14px;align-items:center;padding:14px 18px;border-radius:14px;background:rgba(63,143,95,.06);border:1px solid rgba(63,143,95,.22);margin-bottom:20px}
  .scope .ok{width:36px;height:36px;border-radius:50%;display:grid;place-items:center;background:rgba(63,143,95,.14);color:var(--success);font-weight:700}
  .scope b{display:block;font-size:.9rem}
  .scope-detail{grid-column:1/-1;display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:16px;padding-top:12px;border-top:1px solid rgba(63,143,95,.2);font-size:.82rem}
  .scope-detail h4{margin:0 0 6px;font-size:.72rem;letter-spacing:.1em;text-transform:uppercase;color:var(--muted)}
  .scope-detail ul{margin:0;padding-left:16px;display:grid;gap:4px}
  .cols{display:grid;grid-template-columns:1fr;gap:20px;align-items:start}
  table{width:100%;border-collapse:collapse;font-size:.84rem}
  th{text-align:left;font-size:.68rem;letter-spacing:.1em;text-transform:uppercase;color:var(--muted);font-weight:700;padding:10px 12px;border-bottom:1px solid var(--line)}
  td{padding:12px;border-bottom:1px solid var(--line);vertical-align:middle}
  tr.row{cursor:pointer}
  tr.row:hover td{background:var(--bg-soft)}
  tr.row.is-open td{background:var(--bg-soft)}
  td.num{text-align:right;font-variant-numeric:tabular-nums}
  th.num{text-align:right}
  .dname{display:flex;align-items:center;gap:10px;font-weight:600}
  .ext{width:30px;height:30px;border-radius:8px;background:var(--bg-soft);display:grid;place-items:center;font-size:.58rem;font-weight:700;color:var(--muted);text-transform:uppercase;flex:none}
  .stage{display:inline-flex;align-items:center;gap:6px;font-size:.76rem;font-weight:600;color:var(--success)}
  .stage.is-run{color:var(--info)}
  tr.detail td{padding:0 12px 16px 52px;background:var(--bg-soft)}
  .passage{border-left:3px solid var(--line-2);padding:6px 12px;margin:8px 0;font-size:.82rem;color:var(--ink)}
  .passage em{display:block;font-style:normal;color:var(--muted);font-size:.72rem;margin-bottom:2px}
  .search{display:flex;gap:8px}
  .hits{display:grid;gap:10px;margin-top:14px}
  .hit{background:var(--panel);border:1px solid var(--line);border-radius:12px;padding:12px 14px}
  .hit__top{display:flex;gap:8px;align-items:center;margin-bottom:4px;flex-wrap:wrap}
  .hit__top b{font-size:.8rem}
  .hit__top em{font-style:normal;color:var(--muted);font-size:.74rem}
  .hit__top .sc{margin-left:auto;font-family:var(--display);font-weight:700;color:var(--rose)}
  .hit p{margin:0;font-size:.84rem}
  .folder{display:flex;gap:8px;margin-top:12px}
""",
  body=r"""
    <div class="head">
      <div>
        <p class="label">01 Source</p>
        <h1>Documents</h1>
        <p>One source: documents you upload, or a folder you send us. We pull the text out, split it into passages and index it by meaning, so answers are found even when the wording differs. Ten documents is enough to start.</p>
      </div>
      <span class="spacer"></span>
      <button class="btn btn--secondary" id="folderBtn">Send a folder</button>
      <label class="btn btn--primary" style="cursor:pointer">Upload documents<input type="file" id="fileInput" multiple accept=".pdf,.docx,.doc,.md,.txt" hidden></label>
    </div>

    <section class="scope" id="scope">
      <span class="ok">✓</span>
      <div><b id="scopeTitle">Data in scope, signed off</b><span class="sub" id="scopeSub"></span></div>
      <button class="btn btn--ghost btn--sm" id="scopeToggle" aria-expanded="false">What’s in scope</button>
      <div class="scope-detail" id="scopeDetail" hidden>
        <div><h4>In scope</h4><ul><li>The documents on this page</li><li>Your current help pages</li><li>Questions you add</li></ul></div>
        <div><h4>Out of scope</h4><ul><li>Customer records and tickets</li><li>Mail and call recordings</li><li>Anything not listed here</li></ul></div>
        <!-- ASSUMPTION: scope wording mirrors the week-1 agreement; final text comes from that sign-off. check with Eric -->
        <div><h4>Good to know</h4><ul><li>Personal details are not removed automatically</li><li>Everyone who signs in can see everything</li><li>Data sits on one lojo-run server</li></ul></div>
      </div>
    </section>

    <div class="cols">
      <section class="card" aria-labelledby="docH">
        <div class="card__head"><h2 id="docH">Your documents</h2><span class="sub" id="docMeta"></span></div>
        <div class="folder" id="folderRow" hidden style="padding:14px 20px 0">
          <input class="text" id="folderLink" placeholder="Paste a Google Drive, SharePoint or Dropbox folder link">
          <button class="btn btn--primary btn--sm" id="folderSend" style="height:40px">Send</button>
        </div>
        <table>
          <thead><tr><th>Document</th><th class="num">Pages</th><th class="num">Passages</th><th class="num">Questions</th><th>Status</th></tr></thead>
          <tbody id="docRows"></tbody>
        </table>
      </section>
    </div>
""",
  js=r"""
let open = null;
const extra = [];
function passagesFor(id) {
  const out = [];
  DRAFTS.forEach(r => r.src.forEach(([d, loc, text]) => { if (d === id && !out.some(p => p.text === text)) out.push({ loc, text }); }));
  GAPS.forEach(g => g.where.forEach(([d, loc, text]) => { if (d === id && !out.some(p => p.text === text)) out.push({ loc, text }); }));
  return out;
}
const qsFor = (id) => allQuestions().filter(q => (q.docs || []).includes(id));
function render() {
  const c = counts();
  $('scopeSub').textContent = 'By ' + ST.scope.by + ' on ' + ST.scope.at + ' · personal details are not removed automatically';
  $('docMeta').textContent = (c.docs + extra.length) + ' documents · ' + c.pages + ' pages · ' + c.passages + ' passages';
  const rows = DOCS.map(d => {
    const ext = d.name.split('.').pop(), n = Math.round(d.pages * 4.6), qs = qsFor(d.id);
    let html = '<tr class="row' + (open === d.id ? ' is-open' : '') + '" data-id="' + d.id + '"><td><span class="dname"><span class="ext">' + ext + '</span>' + esc(d.name) +
      (d.faq ? ' <span class="badge badge--info">Your help pages</span>' : '') + '</span></td><td class="num">' + d.pages + '</td><td class="num">' + n + '</td><td class="num">' + qs.length + '</td>' +
      '<td><span class="stage">✓ Indexed</span></td></tr>';
    if (open === d.id) {
      const ps = passagesFor(d.id).slice(0, 3);
      html += '<tr class="detail"><td colspan="5"><p class="sub" style="margin:10px 0 4px">Sample passages</p>' +
        (ps.length ? ps.map(p => '<div class="passage"><em>' + esc(p.loc) + '</em>' + esc(p.text) + '</div>').join('') : '<p class="sub">No passages sampled yet.</p>') +
        (qs.length ? '<p class="sub" style="margin:10px 0 6px">Questions found here</p><div class="chips">' + qs.map(q => '<a class="chip" href="questions.html">' + esc(q.q) + '</a>').join('') + '</div>' : '') + '</td></tr>';
    }
    return html;
  });
  extra.forEach(f => rows.push('<tr><td><span class="dname"><span class="ext">' + esc(f.ext) + '</span>' + esc(f.name) + '</span></td><td class="num">' + (f.pages || '–') + '</td><td class="num">' + (f.passages || '–') + '</td><td class="num">–</td><td><span class="stage ' + (f.done ? '' : 'is-run') + '">' + (f.done ? '✓ Indexed' : '<span class="spin" style="width:11px;height:11px"></span> ' + esc(f.stage)) + '</span></td></tr>'));
  $('docRows').innerHTML = rows.join('');
}
$('docRows').addEventListener('click', (e) => { const tr = e.target.closest('tr.row'); if (!tr || e.target.closest('a')) return; open = open === tr.dataset.id ? null : tr.dataset.id; render(); });
$('scopeToggle').addEventListener('click', () => { const d = $('scopeDetail'); d.hidden = !d.hidden; $('scopeToggle').setAttribute('aria-expanded', !d.hidden); $('scopeToggle').textContent = d.hidden ? 'What’s in scope' : 'Hide'; });
$('fileInput').addEventListener('change', (e) => {
  [...e.target.files].forEach(f => {
    const item = { name: f.name, ext: (f.name.split('.').pop() || '').slice(0, 4), stage: 'Extracting text', done: false, pages: Math.max(1, Math.round(f.size / 40000)) };
    extra.push(item);
    setTimeout(() => { item.stage = 'Splitting into passages'; render(); }, 900);
    setTimeout(() => { item.stage = 'Indexing by meaning'; render(); }, 1800);
    setTimeout(() => { item.done = true; item.passages = Math.round(item.pages * 4.6); render(); toast(item.name + ' indexed'); }, 2800);
  });
  e.target.value = ''; render();
});
$('folderBtn').addEventListener('click', () => { $('folderRow').hidden = !$('folderRow').hidden; if (!$('folderRow').hidden) $('folderLink').focus(); });
$('folderSend').addEventListener('click', () => {
  const v = $('folderLink').value.trim();
  if (!/^https?:\/\/\S+\.\S+/.test(v)) { $('folderLink').focus(); toast('Paste a full folder link'); return; }
  extra.push({ name: 'Shared folder · ' + v.replace(/^https?:\/\//, '').slice(0, 32) + '…', ext: 'dir', stage: 'Waiting for access', done: false });
  $('folderLink').value = ''; $('folderRow').hidden = true; render();
  toast('We’ll pull the documents once ingest@lojo.ai has view access');
});

render();
""")

# ============================================================ QUESTIONS & GAPS
QUESTIONS_PAGE = dict(
  active='questions', title='Questions & gaps',
  css=r"""
  .bar{display:flex;gap:12px;align-items:center;flex-wrap:wrap;margin-bottom:14px}
  .bar .spacer{flex:1}
  .add{display:flex;gap:8px;flex:1;max-width:520px}
  .qlist{list-style:none;margin:0;padding:0}
  .qrow{display:grid;grid-template-columns:minmax(0,1fr) auto auto;gap:18px;align-items:center;padding:14px 20px;border-top:1px solid var(--line)}
  .qrow:first-child{border-top:0}
  .qrow:hover{background:#FCFBFA}
  .qrow b{display:block;font-size:.92rem;font-weight:600;margin-bottom:6px}
  .qmeta{display:flex;flex-wrap:wrap;gap:6px;align-items:center}
  .qrow.is-out b{color:var(--muted);text-decoration:line-through;text-decoration-color:rgba(36,26,20,.25)}
  .status{font-size:.76rem;font-weight:600;white-space:nowrap}
  .st-ok{color:var(--success)} .st-rev{color:#8A6212} .st-q{color:var(--info)} .st-no{color:var(--error)} .st-mute{color:var(--muted)}
  .seg{display:inline-flex;border:1px solid var(--line-2);border-radius:999px;padding:2px;background:var(--panel)}
  .seg button{border:0;background:none;height:28px;padding:0 12px;border-radius:999px;font-size:.76rem;font-weight:600;color:var(--muted);cursor:pointer}
  .seg button:hover{color:var(--ink)}
  .seg button[aria-pressed="true"].yes{background:rgba(63,143,95,.12);color:var(--success)}
  .seg button[aria-pressed="true"].no{background:rgba(36,26,20,.07);color:var(--ink)}
  .qrow.is-call{box-shadow:inset 3px 0 0 var(--amber)}
  .gaps{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:16px}
  .gap{background:var(--panel);border:1px solid var(--line);border-radius:16px;padding:18px 20px;display:flex;flex-direction:column;gap:10px}
  .gap h3{font-family:var(--display);font-weight:700;font-size:1.02rem;margin:0}
  .gap .why{margin:0;color:var(--muted);font-size:.84rem}
  .gap blockquote{margin:0;border-left:3px solid var(--line-2);padding:4px 12px;font-size:.82rem}
  .gap blockquote em{display:block;font-style:normal;color:var(--muted);font-size:.72rem}
  .gap .acts{display:flex;gap:8px;flex-wrap:wrap;margin-top:auto;padding-top:6px}
  .gap.is-done{opacity:.6}
  @media (max-width:1000px){.gaps{grid-template-columns:1fr}.qrow{grid-template-columns:1fr}}
""",
  body=r"""
    <div class="head">
      <div>
        <p class="label">02 Insights</p>
        <h1>Questions &amp; gaps</h1>
        <p>Questions your documents answer, drawn from the documents themselves, plus the ones you give us. Tell us which matter; only those get drafted. Gaps are things your documents refer to but never explain.</p>
      </div>
    </div>
    <div class="tabs" role="tablist">
      <button class="tab" role="tab" data-tab="q" aria-selected="true">Questions <span class="n" id="nQ">0</span></button>
      <button class="tab" role="tab" data-tab="g" aria-selected="false">Gaps <span class="n" id="nG">0</span></button>
    </div>

    <section id="tabQ">
      <div class="bar">
        <div class="chips" id="filters">
          <button class="chip" data-f="all" aria-pressed="true">All</button>
          <button class="chip" data-f="call" aria-pressed="false">Needs your call</button>
          <button class="chip" data-f="yes" aria-pressed="false">Matters</button>
          <button class="chip" data-f="no" aria-pressed="false">Not relevant</button>
          <button class="chip" data-f="you" aria-pressed="false">From you</button>
        </div>
        <span class="spacer"></span>
        <form class="add" id="addForm"><input class="text" id="addQ" placeholder="Add a question we missed" aria-label="Add a question"><button class="btn btn--primary">Add</button></form>
      </div>
      <section class="card"><ul class="qlist" id="qlist"></ul></section>
    </section>

    <section id="tabG" hidden>
      <div class="gaps" id="gapList"></div>
    </section>
""",
  js=r"""
let filter = 'all';
const ORIGIN = { found: ['Found in documents', 'badge--muted'], faq: ['From your help pages', 'badge--info'], you: ['From you', 'badge--rose'], gap: ['From a gap', 'badge--amber'] };
function statusOf(q) {
  const r = draftByQ(q.id);
  if (matters(q) === false) return ['Not drafted', 'st-mute'];
  if (r) {
    const s = decision(r).status;
    if (s === 'approved') return ['Approved', 'st-ok'];
    if (s === 'final') return ['Needs a human answer', 'st-no'];
    return ['Draft in review', 'st-rev'];
  }
  if (!q.docs || !q.docs.length) return ['No source yet', 'st-no'];
  if (matters(q) === null) return ['Waiting for your call', 'st-rev'];
  return ['Queued for drafting', 'st-q'];
}
function renderQ() {
  const qs = allQuestions().filter(q => filter === 'all' || (filter === 'call' && matters(q) === null) || (filter === 'yes' && matters(q) === true) || (filter === 'no' && matters(q) === false) || (filter === 'you' && q.origin === 'you'));
  $('qlist').innerHTML = qs.length ? qs.map(q => {
    const m = matters(q), [st, cls] = statusOf(q), [ol, oc] = ORIGIN[q.origin];
    return '<li class="qrow' + (m === false ? ' is-out' : '') + (m === null ? ' is-call' : '') + '"><div><b>' + esc(q.q) + '</b><div class="qmeta"><span class="badge ' + oc + '">' + ol + '</span>' +
      (q.docs || []).map(d => '<span class="src">' + esc(docShort(d)) + '</span>').join('') + '</div></div>' +
      '<span class="status ' + cls + '">' + st + '</span>' +
      '<span class="seg" role="group" aria-label="Does this matter?"><button class="yes" data-q="' + q.id + '" data-v="1" aria-pressed="' + (m === true) + '">Matters</button><button class="no" data-q="' + q.id + '" data-v="0" aria-pressed="' + (m === false) + '">Not relevant</button></span></li>';
  }).join('') : '<li class="empty"><b>Nothing here</b>Try another filter.</li>';
  const c = counts();
  $('nQ').textContent = c.questions; $('nG').textContent = c.gaps;
}
$('qlist').addEventListener('click', (e) => {
  const b = e.target.closest('[data-q]'); if (!b) return;
  ST.matters[b.dataset.q] = b.dataset.v === '1'; save(); renderQ();
});
$('filters').addEventListener('click', (e) => {
  const b = e.target.closest('[data-f]'); if (!b) return;
  filter = b.dataset.f; document.querySelectorAll('#filters .chip').forEach(x => x.setAttribute('aria-pressed', x === b)); renderQ();
});
$('addForm').addEventListener('submit', (e) => {
  e.preventDefault();
  let v = $('addQ').value.trim(); if (!v) return;
  if (!v.endsWith('?')) v += '?';
  ST.extra.push({ id: 'x' + Date.now(), q: v, origin: 'you', docs: [] });
  save(); $('addQ').value = ''; renderQ(); toast('Added. It joins the same drafting queue.');
});

function renderG() {
  $('gapList').innerHTML = GAPS.map(g => {
    const done = ST.gaps[g.id];
    return '<article class="gap' + (done ? ' is-done' : '') + '"><div style="display:flex;gap:8px;align-items:center"><h3>' + esc(g.term) + '</h3>' +
      (done ? '<span class="badge ' + (done === 'question' ? 'badge--info' : 'badge--muted') + '">' + (done === 'question' ? 'Added as a question' : 'Not needed') + '</span>' : '') + '</div>' +
      '<p class="why">' + esc(g.why) + '</p>' +
      g.where.map(([d, loc, text]) => '<blockquote><em>' + esc(docShort(d)) + ' · ' + esc(loc) + '</em>“' + esc(text) + '”</blockquote>').join('') +
      '<div class="acts">' + (done ? '<button class="btn btn--ghost btn--sm" data-undo="' + g.id + '">Undo</button>' :
        '<a class="btn btn--secondary btn--sm" href="documents.html">Send a document that explains it</a><button class="btn btn--secondary btn--sm" data-ask="' + g.id + '">Add as a question</button><button class="btn btn--ghost btn--sm" data-skip="' + g.id + '">Not needed</button>') + '</div></article>';
  }).join('');
}
$('gapList').addEventListener('click', (e) => {
  const t = e.target.closest('button'); if (!t) return;
  if (t.dataset.ask) {
    const g = GAPS.find(x => x.id === t.dataset.ask);
    if (!allQuestions().some(q => q.gap === g.id)) ST.extra.push({ id: 'x' + g.id, q: 'What is our ' + g.term.toLowerCase().replace(/^the /, '') + '?', origin: 'gap', docs: [], gap: g.id });
    ST.gaps[g.id] = 'question'; toast('Added to your questions');
  }
  if (t.dataset.skip) ST.gaps[t.dataset.skip] = 'skip';
  if (t.dataset.undo) delete ST.gaps[t.dataset.undo];
  save(); renderG(); renderQ();
});

function show(tab) {
  document.querySelectorAll('.tab').forEach(t => t.setAttribute('aria-selected', t.dataset.tab === tab));
  $('tabQ').hidden = tab !== 'q'; $('tabG').hidden = tab !== 'g';
}
document.querySelectorAll('.tab').forEach(t => t.addEventListener('click', () => { show(t.dataset.tab); history.replaceState(null, '', t.dataset.tab === 'g' ? '#gaps' : '#'); }));
renderQ(); renderG(); show(location.hash === '#gaps' ? 'g' : 'q');
""")

# ============================================================ REVIEW
REVIEW = dict(
  active='review', title='Review',
  css=r"""
  .meter{min-width:260px}
  .meter b{font-family:var(--display);font-size:1rem}
  .meter span{color:var(--muted);font-size:.8rem;margin-left:6px}
  .meter .bar{height:6px;border-radius:6px;background:var(--bg-soft);margin-top:8px;overflow:hidden}
  .meter .bar i{display:block;height:100%;background:var(--brand-gradient);transition:width .4s ease}
  .rv{display:grid;grid-template-columns:340px minmax(0,1fr);gap:20px;align-items:start}
  .list{position:sticky;top:84px;max-height:calc(100vh - 110px);display:flex;flex-direction:column;overflow:hidden}
  .list .tabs{padding:0 10px;margin:0}
  .list .tab{padding:12px 8px;font-size:.8rem;white-space:nowrap}
  .items{list-style:none;margin:0;padding:6px;overflow:auto}
  .item{padding:11px 12px;border-radius:10px;cursor:pointer;display:grid;grid-template-columns:auto 1fr;column-gap:10px;row-gap:5px;align-items:start}
  .item > b,.item > .meta{grid-column:2}
  .item .pick{grid-row:1/span 2;margin-top:2px}
  .pick{width:17px;height:17px;margin:0;accent-color:var(--rose);cursor:pointer}
  .item.is-picked{background:rgba(232,93,117,.06)}
  .bulk{display:flex;align-items:center;gap:8px;flex-wrap:wrap;padding:10px 14px;border-bottom:1px solid var(--line);background:var(--panel)}
  .bulk label{display:flex;align-items:center;gap:8px;font-size:.8rem;font-weight:600;cursor:pointer;margin-right:auto}
  .bulk.is-on{background:#FFF6F3}
  .bulk .btn{height:30px;padding:0 12px;font-size:.76rem}
  .bulkrej{display:grid;gap:8px;padding:12px 14px;border-bottom:1px solid var(--line);background:var(--bg-soft)}
  .bulkrej .row{display:flex;gap:8px}
  .item:hover{background:var(--bg-soft)}
  .item.is-sel{background:var(--bg-soft);box-shadow:inset 3px 0 0 var(--rose)}
  .item b{font-size:.84rem;font-weight:600;line-height:1.35}
  .item .meta{display:flex;gap:6px;flex-wrap:wrap}
  .detail{padding:24px 26px}
  .detail h2{font-family:var(--display);font-weight:700;font-size:1.3rem;letter-spacing:-.01em;margin:10px 0 16px;line-height:1.25}
  .seclbl{font-size:.68rem;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--muted);margin:0 0 8px}
  .answer{font-size:.98rem;line-height:1.6;margin:0 0 22px;padding:16px 18px;border-radius:12px;background:var(--bg-soft)}
  .quotes{display:grid;gap:10px;margin-bottom:22px}
  .quote{background:var(--panel);border:1px solid var(--line);border-radius:12px;padding:12px 14px}
  .quote.is-warn{border-color:rgba(217,154,43,.5);background:rgba(217,154,43,.05)}
  .quote .qtop{display:flex;gap:8px;align-items:center;margin-bottom:4px}
  .quote .qtop b{font-size:.8rem}
  .quote .qtop em{font-style:normal;color:var(--muted);font-size:.74rem}
  .quote p{margin:0;font-size:.86rem}
  .prev{margin:0 0 22px;padding:12px 14px;border-left:3px solid var(--line-2);color:var(--muted);font-size:.84rem}
  .prev b{color:var(--ink)}
  .acts{display:flex;gap:10px;align-items:center;flex-wrap:wrap;padding-top:18px;border-top:1px solid var(--line)}
  .acts .spacer{flex:1}
  kbd{font-family:var(--body);font-size:.66rem;font-weight:700;border:1px solid var(--line-2);border-radius:5px;padding:1px 5px;color:var(--muted);background:var(--panel)}
  .btn--primary kbd{background:rgba(255,255,255,.12);border-color:rgba(255,255,255,.3);color:#fff}
  .reject{display:grid;gap:10px;margin-bottom:18px;padding:16px;border-radius:12px;background:var(--bg-soft)}
  .done-note{display:flex;gap:10px;align-items:center;padding:12px 14px;border-radius:12px;margin-bottom:18px;font-size:.86rem}
  .done-note.ok{background:rgba(63,143,95,.08);color:var(--success)}
  .done-note.no{background:rgba(198,69,69,.07);color:var(--error)}
  @media (max-width:1000px){.rv{grid-template-columns:1fr}.list{position:static;max-height:none}}
""",
  body=r"""
    <div class="head">
      <div>
        <p class="label">03 Build · Validation</p>
        <h1>Review</h1>
        <p>First batch of drafts. Approve, edit, or reject with a reason. A rejected draft is written again once; if it’s still wrong, it waits for a human answer.</p>
      </div>
      <span class="spacer"></span>
      <div class="meter"><b id="mCount">0 of 0</b><span>reviewed</span><div class="bar"><i id="mBar"></i></div></div>
    </div>
    <div class="rv">
      <section class="card list" aria-label="Drafts">
        <div class="tabs" role="tablist" id="rtabs">
          <button class="tab" data-f="pending" aria-selected="true">To review <span class="n" id="nP">0</span></button>
          <button class="tab" data-f="approved" aria-selected="false">Approved <span class="n" id="nA">0</span></button>
          <button class="tab" data-f="final" aria-selected="false">Human <span class="n" id="nF">0</span></button>
        </div>
        <div class="bulk" id="bulk" hidden>
          <label><input type="checkbox" class="pick" id="pickAll"> <span id="pickTxt">Select all</span></label>
          <button class="btn btn--primary" id="bulkApprove" type="button" disabled>Approve</button>
          <button class="btn btn--danger" id="bulkReject" type="button" disabled>Reject</button>
        </div>
        <div class="bulkrej" id="bulkRej" hidden>
          <span class="sub" id="bulkRejTxt"></span>
          <select class="text" id="bulkWhy"></select>
          <input class="text" id="bulkNote" placeholder="What should change? (optional)">
          <div class="row"><button class="btn btn--danger btn--sm" id="bulkRejGo" type="button">Reject selected</button><button class="btn btn--ghost btn--sm" id="bulkRejCancel" type="button">Cancel</button></div>
        </div>
        <ul class="items" id="items"></ul>
      </section>
      <section class="card detail" id="detail" aria-live="polite"></section>
    </div>
""",
  js=r"""
let tab = 'pending', sel = null, mode = 'view';
const picked = new Set();
const REASONS = ['Wrong answer', 'Outdated source', 'Missing detail', 'Not a question we answer'];
const Q = (r) => QUESTIONS.find(q => q.id === r.qid).q;
const inTab = (r) => { const s = decision(r).status; return tab === 'pending' ? (s === 'pending' || s === 'redrafting') : s === tab; };
function badges(r) {
  const d = decision(r); let b = '';
  if (r.conflict) b += '<span class="badge badge--amber">Sources disagree</span>';
  if (r.src.length > 1 && !r.conflict) b += '<span class="badge badge--muted">' + r.src.length + ' sources</span>';
  if (d.redrafted) b += '<span class="badge badge--info">Redrafted</span>';
  if (d.edited) b += '<span class="badge badge--muted">Edited</span>';
  return b;
}
function renderList() {
  const c = counts();
  $('nP').textContent = c.pending; $('nA').textContent = c.approved; $('nF').textContent = c.final;
  const done = c.approved + c.final;
  $('mCount').textContent = done + ' of ' + c.drafts; $('mBar').style.width = (done / c.drafts * 100) + '%';
  const list = DRAFTS.filter(inTab);
  if (!list.some(r => r.id === sel)) { sel = list.length ? list[0].id : null; mode = 'view'; }
  const pickable = tab === 'pending';
  [...picked].forEach(id => { if (!list.some(r => r.id === id && decision(r).status === 'pending')) picked.delete(id); });
  $('items').innerHTML = list.length ? list.map(r => '<li class="item' + (r.id === sel ? ' is-sel' : '') + (picked.has(r.id) ? ' is-picked' : '') + '" data-id="' + r.id + '">' +
    (pickable ? '<input type="checkbox" class="pick" data-pick="' + r.id + '" aria-label="Select: ' + esc(Q(r)) + '"' + (picked.has(r.id) ? ' checked' : '') + (decision(r).status !== 'pending' ? ' disabled' : '') + '>' : '<span></span>') +
    '<b>' + esc(Q(r)) + '</b><span class="meta">' + (badges(r) || '<span class="badge badge--muted">1 source</span>') + '</span></li>').join('')
    : '<li class="empty"><b>' + (tab === 'pending' ? 'Nothing to review.' : 'Nothing here yet.') + '</b>' + (tab === 'pending' ? 'The first batch is done.' : '') + '</li>';
  renderBulk(list.filter(r => decision(r).status === 'pending'));
}
function renderBulk(open) {
  const on = tab === 'pending' && open.length > 0, n = picked.size;
  $('bulk').hidden = !on;
  if (!on) { $('bulkRej').hidden = true; return; }
  $('bulk').classList.toggle('is-on', n > 0);
  $('pickAll').checked = n > 0 && n === open.length;
  $('pickAll').indeterminate = n > 0 && n < open.length;
  $('pickTxt').textContent = n ? n + ' selected' : 'Select all (' + open.length + ')';
  $('bulkApprove').disabled = $('bulkReject').disabled = !n;
  $('bulkApprove').textContent = n ? 'Approve ' + n : 'Approve';
  $('bulkReject').textContent = n ? 'Reject ' + n : 'Reject';
  if (!n) $('bulkRej').hidden = true;
}
function renderDetail() {
  const r = DRAFTS.find(x => x.id === sel);
  if (!r) { $('detail').innerHTML = '<div class="empty"><b>Nothing to review. The loop is running.</b>Approved answers are in the store; try them in the chat.</div>'; return; }
  const d = decision(r), ans = answerOf(r);
  let h = '<div class="meta" style="display:flex;gap:6px;flex-wrap:wrap">' + badges(r) + '</div><h2>' + esc(Q(r)) + '</h2>';
  if (d.status === 'approved') h += '<div class="done-note ok">✓ Approved' + (d.at ? ' · ' + esc(d.at) : '') + '. It’s in the store and the chat can use it.</div>';
  if (d.status === 'final') h += '<div class="done-note no">Rejected twice (' + esc(d.reason) + '). Write the answer yourself with Edit, or leave it out.</div>';
  if (d.status === 'redrafting') {
    h += '<div class="answer" style="display:flex;gap:10px;align-items:center;color:var(--muted)"><span class="spin"></span>Writing it again with your reason: “' + esc(d.reason) + '”</div>';
  } else if (mode === 'edit') {
    h += '<p class="seclbl">Your answer</p><textarea class="text" id="editBox" style="min-height:120px;margin-bottom:22px">' + esc(ans) + '</textarea>';
  } else {
    h += '<p class="seclbl">' + (d.redrafted ? 'Rewritten draft' : 'Draft answer') + '</p><p class="answer">' + esc(ans) + '</p>';
  }
  if (d.redrafted && d.prev) h += '<p class="prev"><b>First draft, rejected</b> (' + esc(d.reason) + '): ' + esc(d.prev) + '</p>';
  h += '<p class="seclbl">Where it came from</p><div class="quotes">' + r.src.map(([doc, loc, text]) => {
    const warn = r.conflict === doc;
    return '<div class="quote' + (warn ? ' is-warn' : '') + '"><div class="qtop"><b>' + esc(docShort(doc)) + '</b><em>' + esc(loc) + '</em>' + (warn ? '<span class="badge badge--amber">Conflicts</span>' : '') + '</div><p>“' + esc(text) + '”</p></div>';
  }).join('') + '</div>';
  if (mode === 'reject') {
    h += '<div class="reject"><label class="seclbl" for="why" style="margin:0">Reason</label><select class="text" id="why">' + REASONS.map(x => '<option>' + x + '</option>').join('') + '</select>' +
      '<textarea class="text" id="note" placeholder="What should change? (optional)" style="min-height:70px"></textarea>' +
      '<p class="sub">' + (d.redrafted ? 'This draft was already rewritten once. Rejecting it again leaves it for a human answer.' : 'The agent writes it again once, using your reason.') + '</p></div>';
  }
  let acts = '';
  if (d.status === 'redrafting') acts = '';
  else if (mode === 'edit') acts = '<button class="btn btn--primary" data-a="save">Save &amp; approve</button><button class="btn btn--ghost" data-a="cancel">Cancel</button>';
  else if (mode === 'reject') acts = '<button class="btn btn--danger" data-a="confirm">' + (d.redrafted ? 'Reject' : 'Reject &amp; rewrite') + '</button><button class="btn btn--ghost" data-a="cancel">Cancel</button>';
  else if (d.status === 'pending') acts = '<button class="btn btn--primary" data-a="approve">Approve <kbd>A</kbd></button><button class="btn btn--secondary" data-a="edit">Edit &amp; approve <kbd>E</kbd></button><button class="btn btn--danger" data-a="reject">Reject <kbd>R</kbd></button><span class="spacer"></span><span class="sub"><kbd>J</kbd> <kbd>K</kbd> to move</span>';
  else if (d.status === 'final') acts = '<button class="btn btn--primary" data-a="edit">Write the answer</button><button class="btn btn--ghost" data-a="undo">Back to review</button>';
  else acts = '<button class="btn btn--ghost" data-a="undo">Undo approval</button>';
  if (acts) h += '<div class="acts">' + acts + '</div>';
  $('detail').innerHTML = h;
  if (mode === 'edit') { const t = $('editBox'); t.focus(); t.setSelectionRange(t.value.length, t.value.length); }
}
function render() { renderList(); renderDetail(); }
function next() {
  const list = DRAFTS.filter(inTab);
  if (!list.length) { sel = null; return; }
  const i = DRAFTS.findIndex(x => x.id === sel);
  const after = DRAFTS.slice(i + 1).find(inTab) || list[0];
  sel = after.id;
}
function act(a) {
  const r = DRAFTS.find(x => x.id === sel); if (!r) return;
  const d = ST.decisions[r.id] = ST.decisions[r.id] || { status: 'pending' };
  const today = new Date().toLocaleDateString('en-GB', { weekday: 'short', day: 'numeric', month: 'short' }).replace(',', '');
  if (a === 'approve') { d.status = 'approved'; d.at = today; toast('Approved'); mode = 'view'; save(); next(); }
  if (a === 'edit') mode = 'edit';
  if (a === 'reject') mode = 'reject';
  if (a === 'cancel') mode = 'view';
  if (a === 'undo') { d.status = 'pending'; mode = 'view'; save(); }
  if (a === 'save') {
    const v = $('editBox').value.trim(); if (!v) return;
    d.edited = v !== answerOf(r) || d.edited; d.answer = v; d.status = 'approved'; d.at = today; mode = 'view';
    toast('Edited and approved'); save(); next();
  }
  if (a === 'confirm') {
    const reason = $('why').value + ($('note').value.trim() ? ': ' + $('note').value.trim() : '');
    mode = 'view';
    if (d.redrafted) { d.status = 'final'; d.reason = reason; toast('Left for a human answer'); save(); next(); }
    else {
      d.status = 'redrafting'; d.reason = reason; d.prev = answerOf(r); save();
      const id = r.id;
      setTimeout(() => { const x = ST.decisions[id]; x.status = 'pending'; x.redrafted = true; save(); if (sel === id || tab === 'pending') render(); toast('Rewritten once. Have another look.'); }, 1500);
    }
  }
  render();
}
$('detail').addEventListener('click', (e) => { const b = e.target.closest('[data-a]'); if (b) act(b.dataset.a); });
$('items').addEventListener('click', (e) => {
  const cb = e.target.closest('[data-pick]');
  if (cb) { cb.checked ? picked.add(cb.dataset.pick) : picked.delete(cb.dataset.pick); renderList(); return; }
  const li = e.target.closest('[data-id]'); if (li) { sel = li.dataset.id; mode = 'view'; render(); }
});
$('pickAll').addEventListener('change', () => {
  const open = DRAFTS.filter(r => inTab(r) && decision(r).status === 'pending');
  if ($('pickAll').checked) open.forEach(r => picked.add(r.id)); else picked.clear();
  renderList();
});
const todayStr = () => new Date().toLocaleDateString('en-GB', { weekday: 'short', day: 'numeric', month: 'short' }).replace(',', '');
$('bulkApprove').addEventListener('click', () => {
  const n = picked.size, at = todayStr();
  picked.forEach(id => { const d = ST.decisions[id] = ST.decisions[id] || { status: 'pending' }; d.status = 'approved'; d.at = at; });
  picked.clear(); $('bulkRej').hidden = true; save(); sel = null; render();
  toast(n + ' draft' + (n === 1 ? '' : 's') + ' approved');
});
$('bulkReject').addEventListener('click', () => {
  const ids = [...picked], again = ids.filter(id => (ST.decisions[id] || {}).redrafted).length;
  $('bulkWhy').innerHTML = REASONS.map(x => '<option>' + x + '</option>').join('');
  $('bulkRejTxt').textContent = 'One reason for all ' + ids.length + '. Each is written again once' + (again ? '; ' + again + ' already rewritten will be left for a human answer.' : '.');
  $('bulkRej').hidden = false; $('bulkWhy').focus();
});
$('bulkRejCancel').addEventListener('click', () => { $('bulkRej').hidden = true; });
$('bulkRejGo').addEventListener('click', () => {
  const reason = $('bulkWhy').value + ($('bulkNote').value.trim() ? ': ' + $('bulkNote').value.trim() : '');
  const ids = [...picked]; let rewrite = 0, human = 0;
  ids.forEach(id => {
    const r = DRAFTS.find(x => x.id === id), d = ST.decisions[id] = ST.decisions[id] || { status: 'pending' };
    if (d.redrafted) { d.status = 'final'; d.reason = reason; human++; return; }
    d.status = 'redrafting'; d.reason = reason; d.prev = answerOf(r); rewrite++;
  });
  picked.clear(); $('bulkRej').hidden = true; $('bulkNote').value = ''; save(); render();
  toast(rewrite + ' sent back to be rewritten' + (human ? ' · ' + human + ' left for a human' : ''));
  if (rewrite) setTimeout(() => {
    ids.forEach(id => { const x = ST.decisions[id]; if (x && x.status === 'redrafting') { x.status = 'pending'; x.redrafted = true; } });
    save(); render(); toast('Rewritten once. Have another look.');
  }, 1600);
});
document.querySelectorAll('#rtabs .tab').forEach(t => t.addEventListener('click', () => {
  tab = t.dataset.f; document.querySelectorAll('#rtabs .tab').forEach(x => x.setAttribute('aria-selected', x === t)); sel = null; mode = 'view'; picked.clear(); render();
}));
document.addEventListener('keydown', (e) => {
  if (e.target.closest('input,textarea,select') || e.metaKey || e.ctrlKey) return;
  const k = e.key.toLowerCase(), r = DRAFTS.find(x => x.id === sel);
  if (k === 'j' || k === 'k') {
    const list = DRAFTS.filter(inTab), i = list.findIndex(x => x.id === sel);
    const n = list[Math.max(0, Math.min(list.length - 1, i + (k === 'j' ? 1 : -1)))]; if (n) { sel = n.id; mode = 'view'; render(); }
  }
  if (r && decision(r).status === 'pending' && mode === 'view') {
    if (k === 'a') act('approve'); if (k === 'e') act('edit'); if (k === 'r') act('reject');
  }
  if (k === 'escape' && mode !== 'view') act('cancel');
});
render();
""")

# ============================================================ APPROVED
APPROVED = dict(
  active='approved', title='Approved answers',
  css=r"""
  .bar{display:flex;gap:12px;align-items:center;margin-bottom:14px}
  .bar .text{max-width:420px}
  .alist{display:grid;gap:12px}
  .ans{background:var(--panel);border:1px solid var(--line);border-radius:14px;padding:16px 20px}
  .ans h3{font-family:var(--display);font-weight:700;font-size:1rem;margin:0 0 6px}
  .ans p{margin:0 0 10px;font-size:.9rem}
  .ans .meta{display:flex;gap:6px;flex-wrap:wrap;align-items:center}
  .ans .by{margin-left:auto;color:var(--muted);font-size:.76rem}
""",
  body=r"""
    <div class="head">
      <div>
        <p class="label">04 Distribute</p>
        <h1>Approved answers</h1>
        <p>The approved store. The chat reads only from these answers. It isn’t published anywhere in this phase, and you keep everything as an export.</p>
      </div>
      <span class="spacer"></span>
      <button class="btn btn--secondary" id="csv">Export CSV</button>
      <button class="btn btn--primary" id="json">Export JSON</button>
    </div>
    <div class="bar"><input class="text" id="filter" placeholder="Filter approved answers" aria-label="Filter"><span class="sub" id="meta"></span></div>
    <div class="alist" id="alist"></div>
""",
  js=r"""
const approved = () => DRAFTS.filter(r => decision(r).status === 'approved').map(r => ({ r, q: QUESTIONS.find(q => q.id === r.qid).q, a: answerOf(r), d: decision(r) }));
function render() {
  const f = $('filter').value.trim().toLowerCase(), all = approved();
  const list = all.filter(x => !f || (x.q + ' ' + x.a).toLowerCase().includes(f));
  $('meta').textContent = all.length + ' approved of ' + DRAFTS.length + ' drafts';
  $('alist').innerHTML = list.length ? list.map(x => '<article class="ans"><h3>' + esc(x.q) + '</h3><p>' + esc(x.a) + '</p><div class="meta">' +
    x.r.src.map(([d, loc]) => srcChip(d, loc)).join('') + (x.d.edited ? '<span class="badge badge--muted">Edited</span>' : '') + (x.d.redrafted ? '<span class="badge badge--info">Redrafted</span>' : '') +
    '<span class="by">Approved' + (x.d.at ? ' · ' + esc(x.d.at) : '') + '</span></div></article>').join('')
    : '<div class="card empty"><b>' + (all.length ? 'No matches' : 'Nothing approved yet') + '</b>' + (all.length ? 'Try another word.' : '<a href="review.html">Review the first batch</a> to fill the store.') + '</div>';
}
function download(name, text, type) {
  const a = document.createElement('a');
  a.href = URL.createObjectURL(new Blob([text], { type }));
  a.download = name; a.click(); setTimeout(() => URL.revokeObjectURL(a.href), 1000);
}
const rows = () => approved().map(x => ({ question: x.q, answer: x.a, sources: x.r.src.map(([d, loc]) => docById(d).name + ' (' + loc + ')'), edited: !!x.d.edited, approved: x.d.at || '' }));
$('json').addEventListener('click', () => { download('nimbus-pay-approved-answers.json', JSON.stringify(rows(), null, 2), 'application/json'); toast('Exported ' + rows().length + ' answers'); });
$('csv').addEventListener('click', () => {
  const q = (s) => '"' + String(s).replace(/"/g, '""') + '"';
  const csv = ['question,answer,sources,edited,approved'].concat(rows().map(r => [r.question, r.answer, r.sources.join('; '), r.edited, r.approved].map(q).join(','))).join('\n');
  download('nimbus-pay-approved-answers.csv', csv, 'text/csv'); toast('Exported ' + rows().length + ' answers');
});
$('filter').addEventListener('input', render);
render();
""")

# ============================================================ CHAT
CHAT = dict(
  active='chat', title='Chat',
  css=r"""
  .chat{display:flex;flex-direction:column;height:calc(100vh - 230px);min-height:460px;max-width:860px}
  .log{flex:1;overflow:auto;padding:22px;display:grid;gap:14px;align-content:start}
  .msg{max-width:78%;padding:12px 15px;border-radius:14px;font-size:.9rem}
  .msg--me{justify-self:end;background:var(--ink);color:#fff;border-bottom-right-radius:4px}
  .msg--bot{justify-self:start;background:var(--bg-soft);border-bottom-left-radius:4px}
  .msg--bot.miss{background:rgba(217,154,43,.1);border:1px solid rgba(217,154,43,.3)}
  .msg--bot .from{display:block;margin-top:10px;font-size:.72rem;font-weight:700;letter-spacing:.06em;text-transform:uppercase;color:var(--muted)}
  .msg--bot .srcs{display:flex;flex-wrap:wrap;gap:6px;margin-top:6px}
  .msg--bot .btn{margin-top:10px}
  .foot{border-top:1px solid var(--line);padding:14px 16px;display:grid;gap:10px}
  .foot form{display:flex;gap:8px}
""",
  body=r"""
    <div class="head">
      <div>
        <p class="label">04 Distribute</p>
        <h1>Chat</h1>
        <p id="chatSub">It answers only from approved answers, shows where each answer came from, and says so when it doesn’t know.</p>
      </div>
      <span class="spacer"></span>
      <span class="badge badge--muted">Not published anywhere in this phase</span>
    </div>
    <section class="card chat">
      <div class="log" id="log" aria-live="polite"></div>
      <div class="foot">
        <div class="chips" id="sugg"></div>
        <form id="form"><input class="text" id="ask" placeholder="Ask a question…" aria-label="Ask a question"><button class="btn btn--primary">Ask</button></form>
      </div>
    </section>
""",
  js=r"""
const store = () => DRAFTS.filter(r => decision(r).status === 'approved').map(r => ({ r, q: QUESTIONS.find(q => q.id === r.qid).q, a: answerOf(r) }));
function bubble(cls, html) {
  const d = document.createElement('div'); d.className = 'msg msg--' + cls; d.innerHTML = html; $('log').appendChild(d); $('log').scrollTop = $('log').scrollHeight; return d;
}
function ask(q) {
  bubble('me', esc(q));
  const typing = bubble('bot', '<span class="spin"></span>');
  setTimeout(() => {
    typing.remove();
    let best = null, bs = 0;
    store().forEach(x => { const s = score(q, x.q + ' ' + x.a); if (s.c > 0 && s.s > bs) { best = x; bs = s.s; } });
    if (best && bs >= 2) {
      bubble('bot', esc(best.a) + '<span class="from">From the approved answer: ' + esc(best.q) + '</span><div class="srcs">' + best.r.src.map(([d, loc]) => srcChip(d, loc)).join('') + '</div>');
    } else {
      const b = bubble('bot miss', 'I don’t know. Nothing approved covers this yet, so I won’t guess.<br><button class="btn btn--secondary btn--sm" type="button">Add it to your questions</button>');
      b.querySelector('button').addEventListener('click', (e) => {
        const v = q.endsWith('?') ? q : q + '?';
        if (!allQuestions().some(x => x.q.toLowerCase() === v.toLowerCase())) { const id = 'x' + Date.now(); ST.extra.push({ id, q: v, origin: 'you', docs: [] }); ST.matters[id] = true; save(); }
        e.target.disabled = true; e.target.textContent = 'Added to your questions'; toast('Added to Questions & gaps');
      });
    }
  }, 600);
}
const n = store().length;
$('chatSub').textContent = 'It answers only from the ' + n + ' approved answer' + (n === 1 ? '' : 's') + ', shows where each answer came from, and says so when it doesn’t know.';
bubble('bot', n ? 'Ask me about Nimbus Pay. I only use the ' + n + ' approved answers.' : 'Nothing is approved yet, so I can’t answer anything. <a href="review.html">Review the first batch</a> to fill the store.');
const SUGG = ['Can Starter teams get more seats?', 'How fast can we call the API?', 'Is our data encrypted?', 'Do you offer a free trial?'];
$('sugg').innerHTML = SUGG.map(s => '<button type="button" class="chip">' + esc(s) + '</button>').join('');
$('sugg').addEventListener('click', (e) => { const c = e.target.closest('.chip'); if (c) ask(c.textContent); });
$('form').addEventListener('submit', (e) => { e.preventDefault(); const v = $('ask').value.trim(); if (!v) return; $('ask').value = ''; ask(v); });
""")

# ============================================================ READOUT
READOUT = dict(
  active='readout', title='Readout',
  desc='<!-- ASSUMPTION: processing costs are illustrative placeholders until real usage is metered. check with Eric -->',
  css=r"""
  .doc{max-width:880px;display:grid;gap:20px}
  .draft{display:flex;gap:10px;align-items:center;padding:12px 16px;border-radius:12px;background:var(--amber-soft);color:#7A5710;font-size:.84rem}
  .tiles{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:12px}
  .tile{background:var(--panel);border:1px solid var(--line);border-radius:12px;padding:14px 16px}
  .tile b{display:block;font-family:var(--display);font-weight:800;font-size:1.5rem;line-height:1.1}
  .tile.is-key b{color:var(--rose)}
  .tile span{color:var(--muted);font-size:.78rem}
  .find{margin:16px 0 0;padding-left:18px;display:grid;gap:8px;font-size:.88rem}
  table{width:100%;border-collapse:collapse;font-size:.86rem}
  td{padding:10px 0;border-bottom:1px solid var(--line)}
  td:last-child{text-align:right;font-variant-numeric:tabular-nums;font-weight:600}
  tr.total td{border-bottom:0;font-weight:700}
  tr.total td:last-child{color:var(--rose);font-family:var(--display);font-size:1.1rem}
  .build{display:grid;grid-template-columns:auto 1fr;gap:18px;align-items:start}
  .build .wk{font-family:var(--display);font-weight:800;font-size:2.4rem;line-height:1;color:var(--rose)}
  .build .wk small{display:block;font-family:var(--body);font-size:.74rem;font-weight:600;color:var(--muted);margin-top:4px}
  .adds{margin:0;padding:0;list-style:none;display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:8px}
  .adds li{display:flex;gap:8px;align-items:flex-start;font-size:.86rem;padding:10px 12px;border-radius:10px;background:var(--bg-soft)}
  .adds li::before{content:"+";font-weight:700;color:var(--rose)}
  .decide{display:flex;gap:10px;align-items:center;flex-wrap:wrap}
  .decided{display:flex;gap:10px;align-items:center;padding:12px 16px;border-radius:12px;font-size:.88rem}
  .decided.go{background:rgba(63,143,95,.08);color:var(--success)}
  .decided.stop{background:var(--bg-soft);color:var(--muted)}
  @media print{.side,.top,.no-print{display:none!important}.main{margin:0}}
""",
  body=r"""
    <div class="head">
      <div>
        <p class="label">Decide · Week 4</p>
        <h1>Readout</h1>
        <p>What we found, what it cost to process, and what a full build would take.</p>
      </div>
      <span class="spacer"></span>
      <button class="btn btn--secondary no-print" onclick="window.print()">Print</button>
      <a class="btn btn--primary no-print" href="approved.html">Export approved answers</a>
    </div>
    <div class="doc">
      <p class="draft no-print"><b>Draft.</b> Numbers update as your reviewer works through the batch. The final readout goes out in week 4.</p>

      <section class="card"><div class="card__head"><h2>What we found</h2></div><div class="card__body">
        <div class="tiles">
          <div class="tile is-key"><b id="tQ">0</b><span>questions your documents answer</span></div>
          <div class="tile"><b id="tG">0</b><span>gaps: referred to, never explained</span></div>
          <div class="tile"><b>1</b><span>contradiction between sources</span></div>
          <div class="tile"><b id="tA">0</b><span>answers approved so far</span></div>
        </div>
        <ul class="find">
          <li>Your help pages say SSO is Enterprise-only; the 2026 pricing and recent sales calls say Growth includes it. The help page is 9 months old.</li>
          <li>Two documents say a chargeback fee applies but neither gives the amount. It’s your most-asked unanswered question.</li>
          <li id="fEdit"></li>
          <li>Three of your own questions have no source in the documents: Apple Pay in Germany, the chargeback fee, and call-recording retention.</li>
        </ul>
      </div></section>

      <section class="card"><div class="card__head"><h2>What it cost to process</h2><span class="sub">One fixed model, called through our proxy</span></div><div class="card__body">
        <table>
          <tr><td>Documents processed</td><td id="cDocs"></td></tr>
          <tr><td>Pages read</td><td id="cPages"></td></tr>
          <tr><td>Passages indexed by meaning</td><td id="cPass"></td></tr>
          <tr><td>Model tokens (in / out)</td><td>2.1M / 0.3M</td></tr>
          <tr><td>Indexing and search</td><td>$3.10</td></tr>
          <tr><td>Question finding and drafting, including rewrites</td><td>$15.30</td></tr>
          <tr class="total"><td>Total processing cost</td><td>$18.40 <span class="sub">· $1.84 per document</span></td></tr>
        </table>
      </div></section>

      <section class="card"><div class="card__head"><h2>What a full build would take</h2></div><div class="card__body build">
        <div class="wk">12<small>more weeks</small></div>
        <ul class="adds">
          <li>Roles and permissions</li>
          <li>Live sources such as mail and calls</li>
          <li>Publishing to your own pages</li>
          <li>Personal details removed automatically</li>
          <li>Usage tracking</li>
          <li>Quality measured against a test set</li>
        </ul>
      </div></section>

      <section class="card no-print"><div class="card__head"><h2>Your decision</h2></div><div class="card__body">
        <div id="decision"></div>
      </div></section>
    </div>
""",
  js=r"""
function render() {
  const c = counts();
  const edited = DRAFTS.filter(r => decision(r).status === 'approved' && decision(r).edited).length;
  const rewritten = DRAFTS.filter(r => decision(r).redrafted).length;
  $('tQ').textContent = c.questions; $('tG').textContent = c.gaps; $('tA').textContent = c.approved + ' / ' + c.drafts;
  $('fEdit').textContent = 'Your reviewer approved ' + c.approved + ' drafts, edited ' + edited + ' before approving, and sent ' + rewritten + ' back to be written again.';
  $('cDocs').textContent = c.docs; $('cPages').textContent = c.pages; $('cPass').textContent = c.passages;
  const d = ST.decision;
  $('decision').innerHTML = d ? '<div class="decided ' + (d === 'go' ? 'go' : 'stop') + '">' + (d === 'go' ? '✓ You chose to go on to the full build. We’ll send a plan for the twelve weeks.' : 'You chose not to go on for now. You keep the approved answers as an export.') +
    ' <button class="btn btn--ghost btn--sm" id="undoD">Change</button></div>'
    : '<p class="sub" style="margin-bottom:14px">After trying the chat, decide whether to go on. Either way, you keep the approved answers.</p><div class="decide"><button class="btn btn--grad" id="go">Go on to the full build</button><button class="btn btn--secondary" id="stop">Not now</button></div>';
  if ($('go')) { $('go').onclick = () => { ST.decision = 'go'; save(); render(); }; $('stop').onclick = () => { ST.decision = 'stop'; save(); render(); }; }
  if ($('undoD')) $('undoD').onclick = () => { ST.decision = null; save(); render(); };
}
render();
""")

PAGES = {'dashboard': OVERVIEW, 'documents': DOCUMENTS, 'questions': QUESTIONS_PAGE, 'review': REVIEW, 'approved': APPROVED, 'chat': CHAT, 'readout': READOUT}
for name, p in PAGES.items():
    html = page(p['active'], p['title'], p['css'], p['body'], p['js'], p.get('desc', ''))
    with open(os.path.join(OUT, name + '.html'), 'w') as f:
        f.write(html)
    print('wrote', name + '.html', len(html))
