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
  .next__main .btn{margin-top:26px}
  /* also waiting: two rows visible, the rest scroll */
  #also{max-height:122px;overflow-y:auto;overscroll-behavior:contain;scroll-snap-type:y mandatory;scrollbar-width:thin;scrollbar-color:var(--line-2) transparent;margin-right:-6px;padding-right:6px}
  #also .also{scroll-snap-align:start}
  .also-more{font-size:.74rem;font-weight:600;color:var(--muted);margin-top:6px}
  .also-more[hidden]{display:none}
  .next__main{display:flex;flex-direction:column;align-items:flex-start;justify-content:center}
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
        <a class="btn btn--primary" href="build.html" id="nextCta">Start reviewing →</a>
      </div>
      <div class="next__side">
        <h3>Also waiting on you</h3>
        <div id="also"></div>
        <p class="also-more" id="alsoMore" hidden></p>
      </div>
    </section>

    <section class="sec" aria-labelledby="feedH">
        <div class="sec__head"><h2 id="feedH">Since you last looked</h2></div>
        <ul class="feed" id="feed"></ul>
      </section>
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
          <div><a class="btn btn--secondary btn--sm" href="build.html">See the draft answer →</a></div>
        </div>
      </section>

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
    { a: -90, side: 'top', ic: 'src', t: '01 Source', s: c.docs + ' documents · ' + c.passages + ' passages', href: 'sources.html', st: 'is-done' },
    { a: 0, side: 'right', ic: 'ins', t: '02 Insights', s: c.questions + ' questions · ' + c.gaps + ' gaps', href: 'insights.html', st: 'is-done' },
    { a: 90, side: 'bottom', ic: 'bld', t: '03 Build', s: c.drafts + ' drafts with sources', href: 'build.html', st: 'is-done' },
    { a: 135, side: 'left', ic: 'val', t: 'Validation', s: valNow ? c.pending + ' drafts waiting on you' : 'First batch reviewed', href: 'build.html', st: valNow ? 'is-now' : 'is-done', gate: 1 },
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
    $('nextSub').textContent = 'Approve, edit, or reject with a reason; a rejected draft is written again up to twice.';
    $('nextCta').textContent = 'Start reviewing →'; $('nextCta').href = 'build.html';
  } else {
    $('nextH').textContent = 'Try the chat';
    $('nextSub').textContent = 'The first batch is reviewed. Ask it questions: it answers only from what you approved.';
    $('nextCta').textContent = 'Open the chat →'; $('nextCta').href = 'chat.html';
  }

  const also = [];
  const noSource = allQuestions().filter(q => (!q.docs || !q.docs.length) && matters(q) !== false).length;
  const human = c.final + noSource, failedDrafts = Object.keys(ST.draftFailed || {}).filter(k => ST.draftFailed[k] && ST.draftFailed[k] !== 'retrying').length;
  if (human) also.push({ ic: 'hand', t: human + ' question' + (human === 1 ? ' needs' : 's need') + ' a human answer', s: 'No source, or rejected three times', href: 'insights.html' });
  if (failedDrafts) also.push({ ic: 'q', t: failedDrafts + ' draft' + (failedDrafts === 1 ? '' : 's') + ' could not be written', s: 'Try ' + (failedDrafts === 1 ? 'it' : 'them') + ' again from Insights', href: 'insights.html?demo=failed' });
  if (c.needCall) also.push({ ic: 'q', t: 'Say whether ' + c.needCall + ' question' + (c.needCall > 1 ? 's matter' : ' matters'), s: 'Only those get drafted', href: 'insights.html' });
  if (c.gaps) also.push({ ic: 'gap', t: c.gaps + ' gaps need a source', s: 'Send a document or add them as questions', href: 'insights.html#gaps' });
  $('alsoMore').hidden = also.length <= 2; $('alsoMore').textContent = '+' + (also.length - 2) + ' more · scroll';
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
    '<a class="tile tile--soft" href="build.html">' + gauge(decided / c.drafts, '#4F7A2F') + '<span class="tile__lbl">Review progress ' + tip('Drafts in the first batch that you have approved, edited or left for a human answer.') + '</span><span class="tile__sub">' + decided + ' of ' + c.drafts + ' decided · ' + c.approved + ' approved</span><span class="tile__go">→</span></a>',
    '<a class="tile tile--ok" href="sources.html"><span class="tile__tag">Indexed</span><span class="tile__lbl">Sources ' + tip('Documents you sent us. Their text is pulled out, split into passages and indexed by meaning.') + '</span><span class="tile__val">' + c.docs + '</span><span class="tile__sub">' + c.pages + ' pages · ' + c.passages + ' passages</span></a>',
    '<a class="tile' + (c.needCall ? ' tile--warn' : '') + '" href="insights.html">' + (c.needCall ? '<span class="tile__tag">' + c.needCall + ' need your call</span>' : '') + '<span class="tile__lbl">Questions ' + tip('Questions your documents answer, found by the agent, plus the ones you added.') + '</span><span class="tile__val">' + c.questions + '</span><span class="tile__sub">' + (c.questions - yours) + ' found · ' + yours + ' from you</span></a>',
    '<a class="tile' + (c.gaps ? ' tile--warn' : ' tile--ok') + '" href="insights.html#gaps">' + (c.gaps ? '<span class="tile__tag">Needs input</span>' : '') + '<span class="tile__lbl">Gaps ' + tip('Things your documents refer to but never explain. Expected at this stage: send a document or answer them yourself.') + '</span><span class="tile__val">' + c.gaps + '</span><span class="tile__sub">Referred to, never explained</span></a>',
  ].join('');

  // outcome checks; approval rate stays neutral until there are enough decisions
  const rate = decided ? Math.round(c.approved / decided * 100) : 0, early = decided < 10;
  $('checks').innerHTML = '<span><span class="ok">✓</span>Every draft shows its sources</span>' +
    '<span><span class="ok">✓</span>' + rewrites + ' rejected draft' + (rewrites === 1 ? '' : 's') + ' rewritten once</span>' +
    '<span class="' + (early ? 'muted' : '') + '">Approval rate ' + rate + '% · ' + decided + ' decided' + (early ? ' (too early to judge)' : '') + '</span>' +
    '<span class="muted">Processing $18.40 · $1.84 per document</span>' +
    '<a href="knowledge.html">See knowledge →</a>';

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
  active='documents', title='Sources',
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
  .up-hint{display:block;font-size:.74rem;color:var(--muted);text-align:right;margin-top:6px}
  .uperr{margin:0 0 16px;padding:14px 16px;border-radius:14px;border:1px solid rgba(198,69,69,.3);background:rgba(198,69,69,.05)}
  .uperr__h{display:flex;align-items:center;gap:10px;font-weight:700;font-size:.9rem;color:var(--error)}
  .uperr__h button{margin-left:auto}
  .uperr ul{list-style:none;margin:10px 0 0;padding:0;display:grid;gap:6px}
  .uperr li{display:grid;grid-template-columns:auto 1fr;gap:10px;font-size:.84rem;align-items:baseline}
  .uperr li b{font-weight:600}
  .uperr li span{color:var(--muted)}
  .stage.is-fail{color:var(--error)}
  .stage.is-wait{color:var(--muted)}
  .stage.is-wait::before{content:"";width:8px;height:8px;border-radius:50%;border:2px solid currentColor}
  .stage.is-ret{color:var(--muted)}
  tr.is-retired td{color:var(--muted)}
  tr.is-retired .dname{opacity:.6;text-decoration:line-through;text-decoration-color:rgba(36,26,20,.3)}
  tr.is-failed td{background:rgba(198,69,69,.03)}
  .why{display:block;font-size:.76rem;color:var(--error);font-weight:500;margin-top:4px;white-space:normal;max-width:420px}
  .why.mute{color:var(--muted)}
  .acts{white-space:nowrap;text-align:right}
  .acts .btn{height:28px;padding:0 10px;font-size:.74rem}
  tr.row .acts .btn--ghost{opacity:0}
  tr.row:hover .acts .btn--ghost,tr.row .acts .btn--ghost:focus-visible{opacity:1}
  .scope.is-pending{grid-template-columns:36px 1fr;background:rgba(217,154,43,.07);border-color:rgba(217,154,43,.35)}
  .scope.is-pending .ok{background:rgba(217,154,43,.16);color:#94660F}
  .scope .confirm{grid-column:2;display:flex;gap:12px;align-items:center;flex-wrap:wrap;margin-top:4px}
  .scope .confirm label{display:flex;gap:8px;align-items:center;font-size:.86rem;font-weight:600;cursor:pointer}
  .scope .confirm input{width:17px;height:17px;accent-color:var(--rose)}
""",
  body=r"""
    <div class="head">
      <div>
        <p class="label">01 Source</p>
        <h1>Sources</h1>
        <p>One source: documents you upload, or a folder you send us. We pull the text out, split it into passages and index it by meaning, so answers are found even when the wording differs. Ten documents is enough to start.</p>
      </div>
      <span class="spacer"></span>
      <button class="btn btn--secondary" id="folderBtn">Send a folder</button>
      <div><label class="btn btn--primary" id="upBtn" style="cursor:pointer">Upload documents<input type="file" id="fileInput" multiple hidden></label><span class="up-hint">PDF, DOCX, MD or TXT · up to 25 MB each</span></div>
    </div>

    <section class="uperr" id="upErr" hidden role="alert"></section>

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
        <div class="card__head"><h2 id="docH">Your sources</h2><span class="sub" id="docMeta"></span></div>
        <div class="folder" id="folderRow" hidden style="padding:14px 20px 0">
          <input class="text" id="folderLink" placeholder="Paste a Google Drive, SharePoint or Dropbox folder link">
          <button class="btn btn--primary btn--sm" id="folderSend" style="height:40px">Send</button>
        </div>
        <table>
          <thead><tr><th>Source</th><th class="num">Pages</th><th class="num">Passages</th><th class="num">Questions</th><th>Status</th><th class="acts"><span class="sr-only" style="position:absolute;left:-9999px">Actions</span></th></tr></thead>
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
const MAX_MB = 25, OK_EXT = ['pdf', 'docx', 'doc', 'md', 'txt'];
const forceScope = new URLSearchParams(location.search).get('scope') === 'unconfirmed';
ST.retired = ST.retired || {};
function renderScope() {
  const pending = forceScope ? !ST.__scopeOk : !ST.scope.signed;
  const el = $('scope');
  el.classList.toggle('is-pending', pending);
  if (pending) {
    // G17: before scope is confirmed, documents wait and the checkbox sits on this page
    el.innerHTML = '<span class="ok">!</span><div><b>Confirm what’s in scope</b><span class="sub">We hold your documents until you confirm them. Personal details are not removed automatically in this phase, so only include what we agreed on.</span></div>' +
      '<div class="confirm"><label><input type="checkbox" id="scopeChk"> These documents are in scope</label><button class="btn btn--primary btn--sm" id="scopeGo" disabled>Confirm and start processing</button></div>';
    $('scopeChk').onchange = () => { $('scopeGo').disabled = !$('scopeChk').checked; };
    $('scopeGo').onclick = () => { ST.scope.signed = true; ST.__scopeOk = true; save(); renderScope(); render(); toast('Scope confirmed. Processing starts now.'); };
  }
}
function render() {
  const c = counts();
  if (!$('scopeSub')) return renderRows();
  $('scopeSub').textContent = 'By ' + ST.scope.by + ' on ' + ST.scope.at + ' · personal details are not removed automatically';
  renderRows();
}
function renderRows() {
  const c = counts();
  const docx = ST.docx || [];
  $('docMeta').textContent = (c.docs + extra.length + docx.length) + ' documents · ' + c.pages + ' pages · ' + c.passages + ' passages';
  const pending = forceScope ? !ST.__scopeOk : !ST.scope.signed;
  const rows = DOCS.map(d => {
    if (ST.retired[d.id]) return retiredRow({ id: d.id, name: d.name, ext: d.name.split('.').pop(), pages: d.pages, retiredNote: 'Retired just now by Sara Lindqvist' }, true);
    const ext = d.name.split('.').pop(), n = Math.round(d.pages * 4.6), qs = qsFor(d.id);
    let html = '<tr class="row' + (open === d.id ? ' is-open' : '') + '" data-id="' + d.id + '"><td><span class="dname"><span class="ext">' + ext + '</span>' + esc(d.name) +
      (d.faq ? ' <span class="badge badge--info">Your help pages</span>' : '') + '</span></td><td class="num">' + d.pages + '</td><td class="num">' + n + '</td><td class="num">' + qs.length + '</td>' +
      '<td><span class="stage">✓ Indexed</span></td><td class="acts"><button class="btn btn--ghost" data-retire="' + d.id + '">Retire</button></td></tr>';
    if (open === d.id) {
      const ps = passagesFor(d.id).slice(0, 3);
      html += '<tr class="detail"><td colspan="5"><p class="sub" style="margin:10px 0 4px">Sample passages</p>' +
        (ps.length ? ps.map(p => '<div class="passage"><em>' + esc(p.loc) + '</em>' + esc(p.text) + '</div>').join('') : '<p class="sub">No passages sampled yet.</p>') +
        (qs.length ? '<p class="sub" style="margin:10px 0 6px">Questions found here</p><div class="chips">' + qs.map(q => '<a class="chip" href="insights.html">' + esc(q.q) + '</a>').join('') + '</div>' : '') + '</td><td></td></tr>';
    }
    return html;
  });
  extra.forEach(f => rows.push('<tr><td><span class="dname"><span class="ext">' + esc(f.ext) + '</span>' + esc(f.name) + '</span></td><td class="num">' + (f.pages || '–') + '</td><td class="num">' + (f.passages || '–') + '</td><td class="num">–</td><td><span class="stage ' + (f.done ? '' : 'is-run') + '">' + (f.done ? '✓ Indexed' : '<span class="spin" style="width:11px;height:11px"></span> ' + esc(f.stage)) + '</span></td><td></td></tr>'));
  docx.forEach(d => {
    if (d.status === 'retired') { rows.push(retiredRow(d)); return; }
    const head = '<tr class="' + (d.status === 'failed' ? 'is-failed' : '') + '"><td><span class="dname"><span class="ext">' + esc(d.ext) + '</span><span>' + esc(d.name) +
      (d.status === 'failed' ? '<span class="why">' + esc(d.reason) + '</span>' : d.status === 'waiting' ? '<span class="why mute">' + (pending ? 'Waiting for you to confirm scope.' : 'In the queue. Processing starts in about 2 minutes.') + '</span>' : '') + '</span></span></td>' +
      '<td class="num">–</td><td class="num">–</td><td class="num">–</td>';
    if (d.status === 'failed') rows.push(head + '<td><span class="stage is-fail">✕ Couldn’t process</span></td><td class="acts"><button class="btn btn--secondary" data-retry="' + d.id + '">Try again</button> <button class="btn btn--ghost" style="opacity:1" data-remove="' + d.id + '">Remove</button></td></tr>');
    else if (d.status === 'waiting') rows.push(head + '<td><span class="stage is-wait">Waiting</span></td><td class="acts"><button class="btn btn--ghost" style="opacity:1" data-remove="' + d.id + '">Cancel</button></td></tr>');
    else if (d.status === 'running') rows.push(head + '<td><span class="stage is-run"><span class="spin" style="width:11px;height:11px"></span> ' + esc(d.stage || 'Extracting text') + '</span></td><td></td></tr>');
    else rows.push(head.replace('<td class="num">–</td><td class="num">–</td>', '<td class="num">' + (d.pages || 4) + '</td><td class="num">' + Math.round((d.pages || 4) * 4.6) + '</td>') + '<td><span class="stage">✓ Indexed</span></td><td></td></tr>');
  });
  $('docRows').innerHTML = rows.join('');
}
// G4: retired documents stay listed, greyed, and can be restored
function retiredRow(d, base) {
  return '<tr class="is-retired"><td><span class="dname"><span class="ext">' + esc(d.ext) + '</span><span>' + esc(d.name) + '<span class="why mute">' + esc(d.retiredNote) + '</span></span></span></td>' +
    '<td class="num">' + (d.pages || '–') + '</td><td class="num">–</td><td class="num">–</td><td><span class="stage is-ret">Retired</span></td>' +
    '<td class="acts"><button class="btn btn--secondary" data-restore="' + d.id + '"' + (base ? ' data-base="1"' : '') + '>Restore</button></td></tr>';
}
$('docRows').addEventListener('click', (e) => {
  const b = e.target.closest('button'); if (!b) return;
  e.stopPropagation();
  const docx = ST.docx || [];
  if (b.dataset.retry) {
    const d = docx.find(x => x.id === b.dataset.retry); d.status = 'running'; d.stage = 'Extracting text'; renderRows();
    setTimeout(() => { d.status = 'failed'; d.reason = 'Still password-protected. Remove the password in your PDF app, then upload the file again.'; save(); renderRows(); toastError('Holiday policy 2025.pdf still couldn’t be processed.'); }, 1600);
  }
  if (b.dataset.remove) { ST.docx = docx.filter(x => x.id !== b.dataset.remove); save(); renderRows(); toast('Removed'); }
  if (b.dataset.restore) {
    if (b.dataset.base) delete ST.retired[b.dataset.restore]; else { const d = docx.find(x => x.id === b.dataset.restore); d.status = 'indexed'; }
    save(); renderRows(); toast('Restored. Its passages are used for drafts again.');
  }
  if (b.dataset.retire) confirmRetire(b.dataset.retire);
});
function confirmRetire(id) {
  const d = docById(id), qs = qsFor(id).length;
  let dlg = $('retDlg');
  if (!dlg) { dlg = document.createElement('dialog'); dlg.id = 'retDlg'; dlg.className = 'dlg'; document.body.appendChild(dlg); }
  dlg.innerHTML = '<form method="dialog"><div class="dlg__b"><h3>Retire ' + esc(d.name) + '?</h3>' +
    '<p>Retire a document when it’s out of date. Its passages stop being used for new drafts and the chat. It stays listed here, and you can restore it.</p>' +
    (qs ? '<div class="warn" style="background:rgba(217,154,43,.1);color:#7A5710">' + qs + ' question' + (qs === 1 ? '' : 's') + ' cite this document. Approved answers that rely on it are sent back to Build.</div>' : '') +
    '</div><div class="dlg__f"><button class="btn btn--secondary" value="cancel">Cancel</button><button class="btn btn--danger" type="button" id="retGo">Retire document</button></div></form>';
  dlg.showModal();
  $('retGo').onclick = () => { ST.retired[id] = true; save(); dlg.close(); open = null; renderRows(); toast(d.name + ' retired'); };
}
$('docRows').addEventListener('click', (e) => { const tr = e.target.closest('tr.row'); if (!tr || e.target.closest('a')) return; open = open === tr.dataset.id ? null : tr.dataset.id; render(); });
$('scopeToggle').addEventListener('click', () => { const d = $('scopeDetail'); d.hidden = !d.hidden; $('scopeToggle').setAttribute('aria-expanded', !d.hidden); $('scopeToggle').textContent = d.hidden ? 'What’s in scope' : 'Hide'; });
// G3: reject wrong type, too large and duplicates up front; upload the rest
function showUploadErrors(errs) {
  const el = $('upErr');
  if (!errs.length) { el.hidden = true; return; }
  el.innerHTML = '<div class="uperr__h">' + errs.length + ' file' + (errs.length === 1 ? '' : 's') + ' couldn’t be uploaded <button class="btn btn--ghost btn--sm" id="upErrX" type="button">Dismiss</button></div><ul>' +
    errs.map(([n, why]) => '<li><b>' + esc(n) + '</b><span>' + esc(why) + '</span></li>').join('') + '</ul>';
  el.hidden = false; $('upErrX').onclick = () => { el.hidden = true; };
}
window.demoUploadErrors = () => showUploadErrors([['Q3 board deck.pptx', 'This file type isn’t supported. Use PDF, DOCX, MD or TXT.'], ['Call recordings.zip', 'Too large: 212 MB. Each file can be up to 25 MB.'], ['Billing FAQ.docx', 'Already uploaded on 10 Sep. Retire the old one first if this is a newer version.']]);
$('fileInput').addEventListener('change', (e) => {
  const errs = [], names = DOCS.map(d => d.name.toLowerCase()).concat((ST.docx || []).map(d => d.name.toLowerCase()), extra.map(x => x.name.toLowerCase()));
  const files = [...e.target.files].filter(f => {
    const ext = (f.name.split('.').pop() || '').toLowerCase();
    if (!OK_EXT.includes(ext)) { errs.push([f.name, 'This file type isn’t supported. Use PDF, DOCX, MD or TXT.']); return false; }
    if (f.size > MAX_MB * 1048576) { errs.push([f.name, 'Too large: ' + Math.round(f.size / 1048576) + ' MB. Each file can be up to 25 MB.']); return false; }
    if (names.includes(f.name.toLowerCase())) { errs.push([f.name, 'Already uploaded. Retire the old one first if this is a newer version.']); return false; }
    return true;
  });
  showUploadErrors(errs);
  files.forEach(f => {
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

renderScope();
render();
if (new URLSearchParams(location.search).get('demo') === 'upload') demoUploadErrors();
""")

# ============================================================ QUESTIONS & GAPS
QUESTIONS_PAGE = dict(
  active='questions', title='Insights',
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
  .qrow.is-flash{animation:flash 1.6s ease}
  @keyframes flash{0%,40%{background:rgba(232,93,117,.12)}100%{background:transparent}}
  .qrow .note{display:block;margin-top:6px;font-size:.78rem;color:var(--muted)}
  .qrow .note::before{content:"Left out · ";font-weight:700}
  .qrow .failnote{display:block;margin-top:6px;font-size:.78rem;color:var(--error)}
  .stcell{display:grid;justify-items:end;gap:6px}
  .stcell .btn{height:26px;padding:0 10px;font-size:.72rem}
  .leave{grid-column:1/-1;display:flex;gap:8px;align-items:center;flex-wrap:wrap;padding:10px 12px;border-radius:12px;background:var(--bg-soft)}
  .leave input{flex:1;min-width:220px;height:36px}
  .addmsg{flex-basis:100%;display:flex;gap:10px;align-items:center;padding:10px 12px;border-radius:10px;background:rgba(62,111,166,.08);color:var(--info);font-size:.84rem}
  .addmsg b{color:var(--ink);font-weight:600}
  .addmsg .btn{height:28px;font-size:.76rem;margin-left:auto}
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
        <h1>Insights</h1>
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
          <button class="chip" data-f="no" aria-pressed="false">Left out</button>
          <button class="chip" data-f="you" aria-pressed="false">From you</button>
        </div>
        <span class="spacer"></span>
        <form class="add" id="addForm"><input class="text" id="addQ" placeholder="Add a question we missed" aria-label="Add a question"><button class="btn btn--primary">Add</button></form>
        <div class="addmsg" id="addMsg" hidden role="status"></div>
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
ST.asks = ST.asks || {}; ST.notes = ST.notes || {}; ST.draftFailed = ST.draftFailed || {};
let leaving = null, flashId = null;
function statusOf(q) {
  const r = draftByQ(q.id);
  if (matters(q) === false) return ['Left out', 'st-mute'];
  if (ST.draftFailed[q.id] === 'retrying') return ['Drafting…', 'st-q'];
  if (ST.draftFailed[q.id]) return ['Draft failed', 'st-no'];
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
    const asks = ST.asks[q.id] || 0, failed = ST.draftFailed[q.id];
    return '<li class="qrow' + (m === false ? ' is-out' : '') + (m === null ? ' is-call' : '') + (flashId === q.id ? ' is-flash' : '') + '" id="row-' + q.id + '"><div><b>' + esc(q.q) + '</b><div class="qmeta"><span class="badge ' + oc + '">' + ol + '</span>' +
      (asks >= 2 ? '<span class="badge badge--amber" title="Asked in the chat or added by your team">Asked ' + asks + ' times</span>' : '') +
      (q.docs || []).map(d => '<span class="src">' + esc(docShort(d)) + '</span>').join('') + '</div>' +
      (m === false && ST.notes[q.id] ? '<span class="note">' + esc(ST.notes[q.id]) + '</span>' : '') +
      (failed && failed !== 'retrying' && m !== false ? '<span class="failnote">' + esc(failed) + '</span>' : '') + '</div>' +
      '<span class="stcell"><span class="status ' + cls + '">' + (failed === 'retrying' ? '<span class="spin" style="width:10px;height:10px"></span> ' : '') + st + '</span>' +
      (failed && failed !== 'retrying' && m !== false ? '<button class="btn btn--secondary" data-retry="' + q.id + '">Try again</button>' : '') + '</span>' +
      '<span class="seg" role="group" aria-label="Does this matter?"><button class="yes" data-q="' + q.id + '" data-v="1" aria-pressed="' + (m === true) + '">Matters</button><button class="no" data-q="' + q.id + '" data-v="0" aria-pressed="' + (m === false) + '">' + (m === false ? 'Left out' : 'Leave out') + '</button></span>' +
      (leaving === q.id ? '<div class="leave"><input class="text" id="leaveNote" placeholder="Why leave it out? (optional) e.g. we don’t offer this" aria-label="Note"><button class="btn btn--primary btn--sm" data-leave-go="' + q.id + '">Leave out</button><button class="btn btn--ghost btn--sm" data-leave-x="1">Cancel</button></div>' : '') + '</li>';
  }).join('') : '<li class="empty"><b>Nothing here</b>Try another filter.</li>';
  const c = counts();
  $('nQ').textContent = c.questions; $('nG').textContent = c.gaps;
}
$('qlist').addEventListener('click', (e) => {
  const r = e.target.closest('[data-retry]');
  if (r) { const id = r.dataset.retry; ST.draftFailed[id] = 'retrying'; renderQ();
    setTimeout(() => { delete ST.draftFailed[id]; save(); renderQ(); toast('Drafted. It’s waiting in Build.'); }, 1500); return; }
  if (e.target.closest('[data-leave-x]')) { leaving = null; renderQ(); return; }
  const g = e.target.closest('[data-leave-go]');
  if (g) { const id = g.dataset.leaveGo, n = $('leaveNote').value.trim(); ST.matters[id] = false; if (n) ST.notes[id] = n; else delete ST.notes[id]; leaving = null; save(); renderQ(); toast('Left out. It won’t be drafted.'); return; }
  const b = e.target.closest('[data-q]'); if (!b) return;
  if (b.dataset.v === '0' && matters(allQuestions().find(q => q.id === b.dataset.q)) !== false) { leaving = b.dataset.q; renderQ(); $('leaveNote').focus(); return; }
  ST.matters[b.dataset.q] = b.dataset.v === '1'; if (b.dataset.v === '1') delete ST.notes[b.dataset.q]; save(); renderQ();
});
$('qlist').addEventListener('keydown', (e) => { if (e.target.id === 'leaveNote' && e.key === 'Enter') { e.preventDefault(); document.querySelector('[data-leave-go]').click(); } });
$('filters').addEventListener('click', (e) => {
  const b = e.target.closest('[data-f]'); if (!b) return;
  filter = b.dataset.f; document.querySelectorAll('#filters .chip').forEach(x => x.setAttribute('aria-pressed', x === b)); renderQ();
});
$('addQ').addEventListener('input', () => { $('addMsg').hidden = true; });
$('addForm').addEventListener('submit', (e) => {
  e.preventDefault();
  let v = $('addQ').value.trim(); if (!v) return;
  if (!v.endsWith('?')) v += '?';
  // G6: already in the list — count the ask instead of adding a copy
  const norm = (s) => s.toLowerCase().replace(/[^a-z0-9 ]/g, '').replace(/\s+/g, ' ').trim();
  const dup = allQuestions().find(q => norm(q.q) === norm(v));
  if (dup) {
    ST.asks[dup.id] = Math.max(2, (ST.asks[dup.id] || 1) + 1); save();
    $('addMsg').innerHTML = '<span>Already in the list: <b>' + esc(dup.q) + '</b> · now asked ' + ST.asks[dup.id] + ' times.</span><button class="btn btn--secondary" type="button" id="showDup">Show it</button>';
    $('addMsg').hidden = false;
    $('showDup').onclick = () => { filter = 'all'; document.querySelectorAll('#filters .chip').forEach(x => x.setAttribute('aria-pressed', x.dataset.f === 'all')); flashId = dup.id; renderQ(); $('row-' + dup.id).scrollIntoView({ block: 'center', behavior: 'smooth' }); $('addMsg').hidden = true; };
    renderQ(); return;
  }
  $('addMsg').hidden = true;
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
        '<a class="btn btn--secondary btn--sm" href="sources.html">Send a document that explains it</a><button class="btn btn--secondary btn--sm" data-ask="' + g.id + '">Add as a question</button><button class="btn btn--ghost btn--sm" data-skip="' + g.id + '">Not needed</button>') + '</div></article>';
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
const QD = new URLSearchParams(location.search).get('demo');
if (QD === 'dup') { $('addQ').value = 'What are the API rate limits'; $('addForm').requestSubmit(); }
if (QD === 'leave') { leaving = 'q16'; renderQ(); $('row-q16').scrollIntoView({ block: 'center' }); $('leaveNote').focus(); }
if (QD === 'failed') $('row-q17').scrollIntoView({ block: 'center' });
""")

# ============================================================ REVIEW
REVIEW = dict(
  active='review', title='Build',
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
  .quote .more{border:0;background:none;padding:0;margin-top:8px;font-size:.76rem;font-weight:700;color:#B73C54;cursor:pointer}
  .quote .full{margin-top:10px;padding:12px 14px;border-radius:10px;background:var(--bg-soft);font-size:.84rem;line-height:1.65;color:var(--muted)}
  .quote .full mark{background:rgba(255,177,153,.55);color:var(--ink);padding:1px 2px;border-radius:3px}
  :root[data-theme="dark"] .quote .full mark{background:rgba(232,93,117,.35)}
  .other{display:grid;grid-template-columns:36px 1fr;gap:12px;align-items:start;padding:14px 16px;border-radius:12px;background:rgba(62,111,166,.08);border:1px solid rgba(62,111,166,.25);margin-bottom:18px;font-size:.88rem}
  .other .av{width:36px;height:36px;border-radius:10px;background:linear-gradient(135deg,#7A8BA6,#B3C2D6);color:#fff;font-weight:800;font-size:.76rem;display:grid;place-items:center}
  .other b{display:block}
  .other .btns{display:flex;gap:8px;margin-top:10px}
  .hist{margin:0 0 22px;border:1px solid var(--line);border-radius:12px;padding:0 14px}
  .hist summary{cursor:pointer;padding:12px 0;font-size:.84rem;font-weight:700;color:var(--muted)}
  .hist ol{margin:0 0 12px;padding-left:20px;display:grid;gap:10px;font-size:.84rem}
  .hist li span{display:block;color:var(--error);font-size:.76rem;font-weight:600;margin-top:2px}
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
        <h1>Build</h1>
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
const openFull = new Set();
const CONTEXT = {
  'd1|p. 4': ['Plans and features. Every plan includes the help centre, the chat and email support. ', ' Starter workspaces sign in with email or with Google. An Owner turns single sign-on on under Settings → Security.'],
  'd5|Brightline call, 12 Aug': ['Brightline asked about access for their 40-person support team. ', ' They want to roll it out before their October audit. Follow-up: send the SSO setup guide.'],
  'd2|Security & login · 9 months old': ['Security & login. Every account is protected by two-step verification. ', ' Contact sales to enable it. Last updated 14 January.'],
  'd4|§2': ['§2 Cancelling a subscription. A workspace Owner can cancel at any time from Billing. ', ' Refunds go back to the original payment method within 10 working days.'],
  'd1|p. 2': ['Starter is for small teams getting started. ', ' Teams that need more move to Growth, which includes 15 seats and 25,000 transactions a month.'],
  'd3|pp. 2–4': ['Before you start, make sure you are a workspace Owner and are on Growth or Scale. ', ' Test the connection by signing in from a private window before you turn it on for everyone.'],
  'd1|p. 6': ['Changing plans. You can change plan at any time from Billing. ', ' Your invoice shows the change on its own line.'],
  'd6|p. 1': ['Welcome to Nimbus Pay. Here is what happens in your first month. ', ' Growth customers get a 30-minute kickoff and our onboarding guides.'],
  'd9|§1': ['§1 Paying for Nimbus Pay. ', ' Prices are shown in euros and charged in your local currency.'],
  'd9|§4': ['§4 Invoices. ', ' Invoices are sent on the first working day of the month and are due within 30 days.'],
  'd1|p. 5': ['Billing. ', ' Card payments are taken on the same day each month.'],
  'd8|Rate limits': ['Rate limits keep the API fast for everyone. ', ' Limits apply per workspace, not per API key.'],
  'd8|429 responses': ['When you go over the limit. ', ' Retry after the number of seconds given, and back off further if it happens again.'],
  'd10|§2': ['§2 Responding to a dispute. ', ' Late evidence can’t be added once the card network has started its review.'],
  'd10|§4': ['§4 After you respond. ', ' We email the outcome to the workspace Owner as soon as we hear back.'],
  'd7|p. 3': ['Encryption. Data in transit is encrypted with TLS 1.2 or higher. ', ' Encryption keys are rotated every 90 days.'],
  'd7|p. 2': ['Where your data lives. ', ' Backups stay in the same region and are kept for 35 days.'],
  'd7|p. 8': ['Your data, your choice. ', ' Exports include documents, questions and approved answers.'],
  'd2|Exporting your data': ['Exporting your data. Only Owners and Admins can export. ', ' Large exports are emailed to you as a download link.'],
  'd4|§3': ['§3 Annual plans. ', ' Monthly plans are not refunded after the first 30 days.'],
  'd9|§2': ['§2 Renewals. ', ' We email a reminder 30 days before each renewal.'],
};
const Q = (r) => QUESTIONS.find(q => q.id === r.qid).q;
const inTab = (r) => { const s = decision(r).status; return tab === 'pending' ? (s === 'pending' || s === 'redrafting') : s === tab; };
function badges(r) {
  const d = decision(r); let b = '';
  if (r.conflict) b += '<span class="badge badge--amber">Sources disagree</span>';
  if (r.src.length > 1 && !r.conflict) b += '<span class="badge badge--muted">' + r.src.length + ' sources</span>';
  if (d.redrafted) b += '<span class="badge badge--info">' + (d.redrafted === 2 ? 'Rewritten twice' : 'Redrafted') + '</span>';
  if (ST.others && ST.others[r.id] && d.status === 'pending') b += '<span class="badge badge--rose">Decided by ' + esc(ST.others[r.id].by.split(' ')[0]) + '</span>';
  if (d.by) b += '<span class="badge badge--muted">By ' + esc(d.by.split(' ')[0]) + '</span>';
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
    (pickable ? '<input type="checkbox" class="pick" data-pick="' + r.id + '" aria-label="Select: ' + esc(Q(r)) + '"' + (picked.has(r.id) ? ' checked' : '') + (decision(r).status !== 'pending' || (ST.others && ST.others[r.id]) ? ' disabled' : '') + '>' : '<span></span>') +
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
  const other = ST.others && ST.others[r.id];
  // G10: someone else decided this draft while it was open here
  if (other && d.status === 'pending') h += '<div class="other"><span class="av">' + esc(other.by.split(' ').map(x => x[0]).join('')) + '</span><div><b>' + esc(other.by) + ' ' + esc(other.action) + ' this ' + esc(other.when) + '.</b>' +
    'Your screen was out of date, so nothing you do here will change it. Their decision stands.<div class="btns"><button class="btn btn--primary btn--sm" data-a="ackOther">Got it, next draft</button><button class="btn btn--ghost btn--sm" data-a="seeOther">See their version</button></div></div></div>';
  if (d.status === 'approved') h += '<div class="done-note ok">✓ Approved' + (d.by ? ' by ' + esc(d.by) : '') + (d.at ? ' · ' + esc(d.at) : '') + '. It’s in the store and the chat can use it.</div>';
  if (d.status === 'final') h += '<div class="done-note no">Rejected twice (' + esc(d.reason) + '). Write the answer yourself with Edit, or leave it out.</div>';
  if (d.status === 'redrafting') {
    h += '<div class="answer" style="display:flex;gap:10px;align-items:center;color:var(--muted)"><span class="spin"></span>Writing it again with your reason: “' + esc(d.reason) + '”</div>';
  } else if (mode === 'edit') {
    h += '<p class="seclbl">Your answer</p><textarea class="text" id="editBox" style="min-height:120px;margin-bottom:22px">' + esc(ans) + '</textarea>';
  } else {
    h += '<p class="seclbl">' + (d.redrafted === 2 ? 'Third draft' : d.redrafted ? 'Rewritten draft' : 'Draft answer') + '</p><div class="answer">' + md(ans) + '</div>';
  }
  // G14: a draft rewritten more than once keeps its history
  if (d.history && d.history.length) h += '<details class="hist"><summary>Earlier drafts (' + d.history.length + ')</summary><ol>' + d.history.map(x => '<li>' + esc(x.text) + '<span>Rejected · ' + esc(x.reason) + '</span></li>').join('') + '</ol></details>';
  else if (d.redrafted && d.prev) h += '<p class="prev"><b>First draft, rejected</b> (' + esc(d.reason) + '): ' + esc(d.prev) + '</p>';
  h += '<p class="seclbl">Where it came from</p><div class="quotes">' + r.src.map(([doc, loc, text]) => {
    const warn = r.conflict === doc;
    const key = doc + '|' + loc, ctx = CONTEXT[key] || ['', ''], openQ = openFull.has(key);
    // G9: the whole passage, with the quoted words highlighted
    return '<div class="quote' + (warn ? ' is-warn' : '') + '"><div class="qtop"><b>' + esc(docShort(doc)) + '</b><em>' + esc(loc) + '</em>' + (warn ? '<span class="badge badge--amber">Conflicts</span>' : '') + '</div><p>“' + esc(text) + '”</p>' +
      (openQ ? '<div class="full">' + esc(ctx[0]) + '<mark>' + esc(text) + '</mark>' + esc(ctx[1]) + '</div>' : '') +
      '<button class="more" type="button" data-full="' + esc(key) + '" aria-expanded="' + openQ + '">' + (openQ ? 'Hide full passage' : 'Show full passage') + '</button></div>';
  }).join('') + '</div>';
  if (mode === 'reject') {
    h += '<div class="reject"><label class="seclbl" for="why" style="margin:0">Reason</label><select class="text" id="why">' + REASONS.map(x => '<option>' + x + '</option>').join('') + '</select>' +
      '<textarea class="text" id="note" placeholder="What should change? (optional)" style="min-height:70px"></textarea>' +
      '<p class="sub">' + (d.redrafted === 2 ? 'This draft has been rewritten twice. Rejecting it again leaves it for a human answer.' : d.redrafted ? 'This draft was already rewritten once. Rejecting it again leaves it for a human answer.' : 'The agent writes it again once, using your reason.') + '</p></div>';
  }
  let acts = '';
  if (d.status === 'redrafting') acts = '';
  else if (mode === 'edit') acts = '<button class="btn btn--primary" data-a="save">Save &amp; approve</button><button class="btn btn--ghost" data-a="cancel">Cancel</button>';
  else if (mode === 'reject') acts = '<button class="btn btn--danger" data-a="confirm">' + (d.redrafted ? 'Reject' : 'Reject &amp; rewrite') + '</button><button class="btn btn--ghost" data-a="cancel">Cancel</button>';
  else if (d.status === 'pending' && ST.others && ST.others[r.id]) acts = '';
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
  if (a === 'ackOther' || a === 'seeOther') {
    const o = ST.others[r.id]; d.status = 'approved'; d.by = o.by; d.at = o.when; delete ST.others[r.id]; save();
    if (a === 'ackOther') { next(); } else { tab = 'approved'; document.querySelectorAll('#rtabs .tab').forEach(x => x.setAttribute('aria-selected', x.dataset.f === 'approved')); sel = r.id; }
  }
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
      d.status = 'redrafting'; d.reason = reason; d.prev = answerOf(r); d.history = (d.history || []).concat([{ text: answerOf(r), reason }]); save();
      const id = r.id;
      setTimeout(() => { const x = ST.decisions[id]; x.status = 'pending'; x.redrafted = true; save(); if (sel === id || tab === 'pending') render(); toast('Rewritten once. Have another look.'); }, 1500);
    }
  }
  render();
}
$('detail').addEventListener('click', (e) => {
  const f = e.target.closest('[data-full]'); if (f) { const k = f.dataset.full; openFull.has(k) ? openFull.delete(k) : openFull.add(k); renderDetail(); return; }
  const b = e.target.closest('[data-a]'); if (b) act(b.dataset.a);
});
$('items').addEventListener('click', (e) => {
  const cb = e.target.closest('[data-pick]');
  if (cb) { cb.checked ? picked.add(cb.dataset.pick) : picked.delete(cb.dataset.pick); renderList(); return; }
  const li = e.target.closest('[data-id]'); if (li) { sel = li.dataset.id; mode = 'view'; render(); }
});
$('pickAll').addEventListener('change', () => {
  const open = DRAFTS.filter(r => inTab(r) && decision(r).status === 'pending' && !(ST.others && ST.others[r.id]));
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
const RP = new URLSearchParams(location.search);
if (RP.get('sel')) { sel = RP.get('sel'); if (RP.get('full')) { const r = DRAFTS.find(x => x.id === sel); if (r) openFull.add(r.src[0][0] + '|' + r.src[0][1]); } }
render();
""")

# ============================================================ APPROVED
APPROVED = dict(
  active='approved', title='Distribute',
  css=r"""
  .chan{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:12px;margin-bottom:26px}
  .ch{display:grid;grid-template-columns:36px 1fr;gap:4px 12px;align-items:center;padding:14px 16px;border:1px solid var(--line);border-radius:14px;background:var(--panel);text-decoration:none;color:inherit}
  .ch b{display:block;font-size:.9rem}
  .ch span span{display:block;color:var(--muted);font-size:.76rem}
  .ch em{grid-column:2;font-style:normal;font-size:.7rem;font-weight:700;letter-spacing:.06em;text-transform:uppercase}
  .ch__ic{grid-row:1/span 2;width:36px;height:36px;border-radius:10px;display:grid;place-items:center;background:var(--bg-soft);font-size:1rem}
  .ch.is-live em{color:var(--success)}
  a.ch.is-live:hover{border-color:rgba(232,93,117,.4);box-shadow:0 12px 24px -20px rgba(36,26,20,.5);text-decoration:none}
  .ch.is-off{opacity:.6}
  .ch.is-off em{color:var(--muted)}
  .sech{font-size:.8rem;font-weight:800;letter-spacing:.12em;text-transform:uppercase;color:#8E2F45;margin:0 0 12px}
  @media (max-width:1000px){.chan{grid-template-columns:1fr 1fr}}
  .bar{display:flex;gap:12px;align-items:center;margin-bottom:14px}
  .bar .text{max-width:420px}
  .alist{display:grid;gap:12px}
  .ans{background:var(--panel);border:1px solid var(--line);border-radius:14px;padding:16px 20px}
  .ans h3{font-family:var(--display);font-weight:700;font-size:1rem;margin:0 0 6px}
  .ans p{margin:0 0 10px;font-size:.9rem}
  .ansbody{margin:0 0 10px;font-size:.9rem}
  .ans .meta{display:flex;gap:6px;flex-wrap:wrap;align-items:center}
  .ans .by{margin-left:auto;color:var(--muted);font-size:.76rem}
""",
  body=r"""
    <div class="head">
      <div>
        <p class="label">04 Distribute</p>
        <h1>Distribute</h1>
        <p>Approved answers go out from here. In this phase they power the chat and an export; publishing to your own pages comes with the full build.</p>
      </div>
      <span class="spacer"></span>
      <button class="btn btn--secondary" id="csv">Export CSV</button>
      <button class="btn btn--primary" id="json">Export JSON</button>
    </div>
    <section class="chan" aria-label="Where answers go">
      <a class="ch is-live" href="chat.html"><span class="ch__ic"><svg class="i" viewBox="0 0 24 24"><path d="M21 12a8 8 0 0 1-11.6 7.1L4 20l1-4.6A8 8 0 1 1 21 12z"/></svg></span><span><b>Chat</b><span>Reads only approved answers</span></span><em>Live · open →</em></a>
      <div class="ch is-live"><span class="ch__ic"><svg class="i" viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/><path d="M9.5 9.5a2.5 2.5 0 1 1 3.5 2.3c-.6.3-1 .8-1 1.5V14M12 17h.01"/></svg></span><span><b>Ask lojo button</b><span>On every page of this workspace</span></span><em>Live</em></div>
      <div class="ch is-off"><span class="ch__ic"><svg class="i" viewBox="0 0 24 24"><path d="M3 11l9-7 9 7v9a1 1 0 0 1-1 1h-5v-6H9v6H4a1 1 0 0 1-1-1z"/></svg></span><span><b>Help centre</b><span>Publish answers to your own pages</span></span><em>Full build</em></div>
      <div class="ch is-off"><span class="ch__ic"><svg class="i" viewBox="0 0 24 24"><path d="M5 9h14M5 15h14M10 4 8 20M16 4l-2 16"/></svg></span><span><b>Slack &amp; Teams</b><span>Answer where your team asks</span></span><em>Full build</em></div>
    </section>
    <h2 class="sech">Approved answers</h2>
    <div class="bar"><input class="text" id="filter" placeholder="Filter approved answers" aria-label="Filter"><span class="sub" id="meta"></span></div>
    <div class="alist" id="alist"></div>
""",
  js=r"""
const approved = () => DRAFTS.filter(r => decision(r).status === 'approved').map(r => ({ r, q: QUESTIONS.find(q => q.id === r.qid).q, a: answerOf(r), d: decision(r) }));
function render() {
  const f = $('filter').value.trim().toLowerCase(), all = approved();
  const list = all.filter(x => !f || (x.q + ' ' + x.a).toLowerCase().includes(f));
  $('meta').textContent = all.length + ' approved of ' + DRAFTS.length + ' drafts';
  $('alist').innerHTML = list.length ? list.map(x => '<article class="ans"><h3>' + esc(x.q) + '</h3><div class="ansbody">' + md(x.a) + '</div><div class="meta">' +
    x.r.src.map(([d, loc]) => srcChip(d, loc)).join('') + (x.d.edited ? '<span class="badge badge--muted">Edited</span>' : '') + (x.d.redrafted ? '<span class="badge badge--info">Redrafted</span>' : '') +
    '<span class="by">Approved' + (x.d.at ? ' · ' + esc(x.d.at) : '') + '</span></div></article>').join('')
    : '<div class="card empty"><b>' + (all.length ? 'No matches' : 'Nothing approved yet') + '</b>' + (all.length ? 'Try another word.' : '<a href="build.html">Review the first batch</a> to fill the store.') + '</div>';
}
function download(name, text, type) {
  const a = document.createElement('a');
  a.href = URL.createObjectURL(new Blob([text], { type }));
  a.download = name; a.click(); setTimeout(() => URL.revokeObjectURL(a.href), 1000);
}
const rows = () => approved().map(x => ({ question: x.q, answer: x.a, sources: x.r.src.map(([d, loc]) => docById(d).name + ' (' + loc + ')'), edited: !!x.d.edited, approved: x.d.at || '' }));
function exportGuard(run) { if (!navigator.onLine || new URLSearchParams(location.search).get('fail') === 'export') { toastError('Export failed. Your answers are safe; check your connection.', run); return false; } return true; }
$('json').addEventListener('click', () => { if (!exportGuard(() => $('json').click())) return; download('nimbus-pay-approved-answers.json', JSON.stringify(rows(), null, 2), 'application/json'); toast('Exported ' + rows().length + ' answers'); });
$('csv').addEventListener('click', () => { if (!exportGuard(() => $('csv').click())) return;
  const q = (s) => '"' + String(s).replace(/"/g, '""') + '"';
  const csv = ['question,answer,sources,edited,approved'].concat(rows().map(r => [r.question, r.answer, r.sources.join('; '), r.edited, r.approved].map(q).join(','))).join('\n');
  download('nimbus-pay-approved-answers.csv', csv, 'text/csv'); toast('Exported ' + rows().length + ' answers');
});
$('filter').addEventListener('input', render);
render();
""")

# ============================================================ CHAT
CHAT = dict(
  active='approved', title='Chat',
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
    if (SMALLTALK.test(q)) { bubble('bot', esc(smalltalkReply(q))); countChat('smalltalk'); return; }
    let best = null, bs = 0;
    store().forEach(x => { const s = score(q, x.q + ' ' + x.a); if (s.c > 0 && s.s > bs) { best = x; bs = s.s; } });
    if (best && bs >= 2) {
      countChat('answered');
      bubble('bot', md(best.a) + '<span class="from">From the approved answer: ' + esc(best.q) + '</span><div class="srcs">' + best.r.src.map(([d, loc]) => srcChip(d, loc)).join('') + '</div>');
    } else {
      countChat('declined');
      const b = bubble('bot miss', 'I don’t know. Nothing approved covers this yet, so I won’t guess.<br><button class="btn btn--secondary btn--sm" type="button">Add it to your questions</button>');
      b.querySelector('button').addEventListener('click', (e) => {
        const v = q.endsWith('?') ? q : q + '?';
        if (!allQuestions().some(x => x.q.toLowerCase() === v.toLowerCase())) { const id = 'x' + Date.now(); ST.extra.push({ id, q: v, origin: 'you', docs: [] }); ST.matters[id] = true; save(); }
        e.target.disabled = true; e.target.textContent = 'Added to your questions'; toast('Added to Insights');
      });
    }
  }, 600);
}
const n = store().length;
$('chatSub').textContent = 'It answers only from the ' + n + ' approved answer' + (n === 1 ? '' : 's') + ', shows where each answer came from, and says so when it doesn’t know.';
bubble('bot', n ? 'Ask me about Nimbus Pay. I only use the ' + n + ' approved answers.' : 'Nothing is approved yet, so I can’t answer anything. <a href="build.html">Review the first batch</a> to fill the store.');
const SUGG = ['Hi', 'How fast can we call the API?', 'Is our data encrypted?', 'Do you offer a free trial?', 'Thanks'];
$('sugg').innerHTML = SUGG.map(s => '<button type="button" class="chip">' + esc(s) + '</button>').join('');
$('sugg').addEventListener('click', (e) => { const c = e.target.closest('.chip'); if (c) ask(c.textContent); });
$('form').addEventListener('submit', (e) => { e.preventDefault(); const v = $('ask').value.trim(); if (!v) return; $('ask').value = ''; ask(v); });
const SAY = new URLSearchParams(location.search).get('say'); if (SAY) SAY.split('|').forEach((q, i) => setTimeout(() => ask(q), i * 900));
""")

# ============================================================ READOUT
READOUT = dict(
  active='readout', title='Knowledge',
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
        <h1>Knowledge</h1>
        <p>What we found, what it cost to process, and what a full build would take.</p>
      </div>
      <span class="spacer"></span>
      <button class="btn btn--secondary no-print" onclick="window.print()">Print</button>
      <a class="btn btn--primary no-print" href="distribute.html">Export approved answers</a>
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

      <section class="card"><div class="card__head"><h2>How the chat did</h2><span class="sub">Questions people asked in the chat this phase</span></div><div class="card__body">
        <div class="tiles">
          <div class="tile"><b id="chA">0</b><span>questions asked</span></div>
          <div class="tile is-key"><b id="chOk">0</b><span>answered from approved answers</span></div>
          <div class="tile"><b id="chNo">0</b><span>declined: “I don’t know”</span></div>
          <div class="tile"><b id="chRate">0%</b><span>answer rate</span></div>
        </div>
        <p class="sub" style="margin-top:12px" id="chNote"></p>
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
  const ch = ST.chat || { asked: 0, answered: 0, declined: 0, smalltalk: 0 };
  $('chA').textContent = ch.asked; $('chOk').textContent = ch.answered; $('chNo').textContent = ch.declined;
  $('chRate').textContent = (ch.asked ? Math.round(ch.answered / ch.asked * 100) : 0) + '%';
  $('chNote').textContent = 'Greetings and thanks (' + (ch.smalltalk || 0) + ') aren’t counted. Declined questions are added to Insights so they can be answered next.';
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


STATES = dict(
  active='states', title='Design states',
  css=r"""
  .grp{margin-bottom:26px}
  .grp h2{font-size:.8rem;font-weight:800;letter-spacing:.12em;text-transform:uppercase;color:#8E2F45;margin:0 0 12px}
  .cards{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:12px}
  .st{background:var(--panel);border:1px solid var(--line);border-radius:14px;padding:14px 16px;display:flex;flex-direction:column;gap:8px}
  .st__top{display:flex;align-items:center;gap:8px}
  .st__g{font-family:ui-monospace,Menlo,monospace;font-size:.72rem;font-weight:700;padding:2px 7px;border-radius:6px;background:var(--bg-soft);color:var(--muted)}
  .st b{font-size:.92rem}
  .st p{margin:0;color:var(--muted);font-size:.82rem}
  .st .links{display:flex;flex-wrap:wrap;gap:6px;margin-top:auto;padding-top:4px}
  .st .links .btn{height:28px;padding:0 11px;font-size:.74rem}
""",
  body=r"""
    <div class="head">
      <div>
        <p class="label">For review</p>
        <h1>Design states</h1>
        <p>Every screen and state from DESIGN_GAPS.md, designed into the prototype. Open one to see it in place. G numbers match the file.</p>
      </div>
    </div>
    <div id="groups"></div>
""",
  js=r"""
const L = (href, label) => ({ href, label });
const B = (fn, label) => ({ fn, label });
const GROUPS = [
  ['Signing in', [
    ['G25', 'Email, then password', 'Two steps. The email shows as a chip with “Change” on the password step.', [L('login.html', 'Open sign in')]],
    ['G26', 'Forgot your password?', 'Ask for a reset link, then a “Check your email” page with a resend timer.', [L('auth.html?s=forgot', 'Forgot'), L('auth.html?s=sent&email=sara@nimbuspay.com', 'Check your email')]],
    ['G27', 'Set your password', 'From an invite or a reset email. Live rules: length, a number, both match.', [L('auth.html?s=set&from=invite', 'From invite'), L('auth.html?s=set&from=reset', 'From reset')]],
    ['G24', 'Your details', 'First sign-in with a missing last name (e.g. Microsoft didn’t share it).', [L('auth.html?s=details', 'Open')]],
    ['G28', 'Error, notice, expired', 'Sign-in error with a reference, signed-out notice, expired link.', [L('auth.html?s=error', 'Error'), L('auth.html?s=notice', 'Notice'), L('auth.html?s=expired', 'Expired')]],
    ['G15', 'Choose a region', 'For people in more than one region, plus “can’t reach it” and “no access”.', [L('auth.html?s=region', 'Choose'), L('auth.html?s=unreachable', 'Can’t reach'), L('auth.html?s=noaccess', 'No access')]],
    ['G16', 'Loading and failed start', 'Signing-in progress, and “lojo couldn’t start”.', [L('auth.html?s=loading&next=states.html', 'Loading'), L('auth.html?s=failed', 'Couldn’t start')]],
  ]],
  ['Account menu', [
    ['G21', 'Workspaces and +', 'The account menu lists workspaces; + creates a new one.', [B(() => { $('meBtn').click(); }, 'Open the menu'), B(() => { $('meBtn').click(); $('wsAdd').click(); }, 'New workspace')]],
    ['G23', 'Delete a workspace', 'Bin icon on each workspace; type the web-address name to confirm.', [B(() => { $('meBtn').click(); document.querySelector('[data-del="w2"]').click(); }, 'Open the confirmation')]],
  ]],
  ['Sources', [
    ['G2', 'Failed to process', 'Red row with the reason, “Try again” and “Remove”.', [L('sources.html', 'Open sources')]],
    ['G3', 'Upload errors', 'Wrong type, too large, already uploaded — listed above the table.', [L('sources.html?demo=upload', 'Show errors')]],
    ['G4', 'Retire a document', 'Confirmation, then a greyed, struck-through row with “Restore”. Hover a row for “Retire”.', [L('sources.html', 'Open sources')]],
    ['G19', '“Waiting” status', 'Queued before processing starts.', [L('sources.html', 'Open sources')]],
    ['G17', 'Scope checkbox', 'Amber banner with the checkbox before scope is confirmed.', [L('sources.html?scope=unconfirmed', 'Show unconfirmed')]],
  ]],
  ['Insights', [
    ['G5', 'Draft failed', '“Draft failed” with the reason and “Try again”.', [L('insights.html?demo=failed', 'Open')]],
    ['G6', 'Already in the list', 'Adding a duplicate counts the ask and offers “Show it”.', [L('insights.html?demo=dup', 'Show message')]],
    ['G7', '“Asked 3 times” badge', 'On questions asked more than once.', [L('insights.html', 'Open insights')]],
    ['G8', 'Leave out, with a note', 'Optional note; “Left out” filter and the note on the row.', [L('insights.html?demo=leave', 'Leave one out')]],
  ]],
  ['Build', [
    ['G9', 'Full source passage', '“Show full passage” with the quoted words highlighted.', [L('build.html?sel=r1&full=1', 'Open')]],
    ['G10', 'Someone else decided it', 'Banner with who and when; your actions are hidden.', [L('build.html?sel=r12', 'Open')]],
    ['G14', 'Rewritten twice', '“Rewritten twice” badge and the earlier drafts with their reasons.', [L('build.html?sel=r8', 'Open')]],
  ]],
  ['Chat', [
    ['G29', 'Small talk', '“Hi” and “Thanks” get a short reply with no sources.', [L('chat.html?say=Hi|Thanks', 'Open')]],
    ['G30', 'Formatted answers', 'Headings, lists and bold, sized to the bubble.', [L('chat.html?say=How fast can we call the API?', 'Open')]],
  ]],
  ['Distribute', [
    ['—', 'Distribute page', 'Approved answers plus where they go: chat and Ask lojo live, help centre and Slack in the full build.', [L('distribute.html', 'Open')]],
  ]],
  ['Knowledge', [
    ['G11', 'Chat numbers', 'Asked, answered, declined and the answer rate.', [L('knowledge.html', 'Open knowledge')]],
  ]],
  ['Everywhere', [
    ['G12', 'Error pages', 'Page not found, no access, something went wrong.', [L('auth.html?s=404', '404'), L('auth.html?s=403', '403'), L('auth.html?s=500', '500')]],
    ['G13', 'When an action fails', 'Error toast that says what failed and offers “Try again”.', [B(() => toastError('Couldn’t approve. Your edit is kept.', () => toast('Approved')), 'Show it'), L('distribute.html?fail=export', 'Failed export')]],
    ['G18', 'Connection badge', '“Reconnecting…” while offline, “Catching up…” when back.', [B(() => lojoConn('reconnecting'), 'Reconnecting'), B(() => { lojoConn('catching'); setTimeout(() => lojoConn('online'), 1500); }, 'Catching up')]],
  ]],
];
const acts = [];
$('groups').innerHTML = GROUPS.map(([g, items]) => '<section class="grp"><h2>' + esc(g) + '</h2><div class="cards">' + items.map(([code, title, desc, links]) =>
  '<article class="st"><div class="st__top"><span class="st__g">' + code + '</span><b>' + esc(title) + '</b></div><p>' + esc(desc) + '</p><div class="links">' +
  links.map(l => l.href ? '<a class="btn btn--secondary" href="' + l.href + '">' + esc(l.label) + '</a>' : '<button class="btn btn--secondary" type="button" data-act="' + (acts.push(l.fn) - 1) + '">' + esc(l.label) + '</button>').join('') +
  '</div></article>').join('') + '</div></section>').join('');
$('groups').addEventListener('click', (e) => { const b = e.target.closest('[data-act]'); if (b) { e.stopPropagation(); acts[+b.dataset.act](); } });
""")

PAGES = {'states': STATES, 'dashboard': OVERVIEW, 'sources': DOCUMENTS, 'insights': QUESTIONS_PAGE, 'build': REVIEW, 'distribute': APPROVED, 'chat': CHAT, 'knowledge': READOUT}
for name, p in PAGES.items():
    html = page(p['active'], p['title'], p['css'], p['body'], p['js'], p.get('desc', ''))
    with open(os.path.join(OUT, name + '.html'), 'w') as f:
        f.write(html)
    print('wrote', name + '.html', len(html))
