import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from shell import page

OUT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))



# ============================================================ OVERVIEW
OVERVIEW = dict(
  active='overview', title='Dashboard',
  desc='<!-- ASSUMPTION: a light home for the four weeks, not the analytics dashboards the proposal leaves out. Weekly review target (~20 drafts, due Friday) comes from the plan. check with Eric -->',
  css=r"""
  .wave{display:inline-block;transform-origin:70% 70%;animation:wave 1.8s ease-in-out 1}
  @keyframes wave{0%,60%,100%{transform:rotate(0)}10%,30%{transform:rotate(14deg)}20%{transform:rotate(-8deg)}40%{transform:rotate(-4deg)}50%{transform:rotate(10deg)}}
  @media (prefers-reduced-motion:reduce){.wave{animation:none}}
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
  .next__main{position:relative;overflow:hidden;padding:30px 30px;background:radial-gradient(120% 140% at 0% 0%,#FFE3DA 0%,#FFF4EF 38%,#FFFDFB 70%);border-right:1px solid var(--line);isolation:isolate}
  .next__main::before{content:"";position:absolute;inset:0;z-index:-1;background-image:radial-gradient(rgba(232,93,117,.16) 1px,transparent 1.2px);background-size:16px 16px;-webkit-mask-image:linear-gradient(90deg,transparent 30%,#000 75%);mask-image:linear-gradient(90deg,transparent 30%,#000 75%)}
  .next__main::after{content:"";position:absolute;right:-60px;bottom:-80px;width:260px;height:260px;border-radius:50%;z-index:-1;background:radial-gradient(circle,rgba(255,177,153,.45),transparent 65%)}
  .next__main .label{display:inline-flex;align-items:center;gap:8px}
  .next__main .label::before{content:"";width:8px;height:8px;border-radius:50%;background:var(--rose);box-shadow:0 0 0 0 rgba(232,93,117,.5);animation:nudge 2s ease-out infinite}
  @keyframes nudge{0%{box-shadow:0 0 0 0 rgba(232,93,117,.45)}100%{box-shadow:0 0 0 10px rgba(232,93,117,0)}}
  .next__main h2 .num{background:var(--brand-gradient);-webkit-background-clip:text;background-clip:text;color:transparent;font-size:1.35em;font-weight:800;line-height:1}
  .next__main .btn{transition:transform .15s ease,box-shadow .15s ease}
  .next__main .btn:hover{transform:translateY(-1px);box-shadow:0 14px 28px -14px rgba(36,26,20,.7)}
  .next__main .btn .ar{display:inline-block;transition:transform .2s ease}
  .next__main .btn:hover .ar{transform:translateX(4px)}
  .next__copy{position:relative;z-index:1;max-width:60%}
  /* a fanned stack of drafts, purely decorative */
  .stack{position:absolute;right:34px;top:50%;width:190px;height:150px;transform:translateY(-50%);pointer-events:none}
  .stack .card{position:absolute;inset:0;border-radius:16px;background:#fff;border:1px solid rgba(36,26,20,.08);box-shadow:0 18px 30px -20px rgba(36,26,20,.45);padding:16px}
  .stack .card:nth-child(1){transform:rotate(-9deg) translate(-14px,8px);opacity:.6}
  .stack .card:nth-child(2){transform:rotate(-3deg) translate(-6px,3px);opacity:.85}
  .stack .card:nth-child(3){transform:rotate(4deg);animation:float 4s ease-in-out infinite}
  @keyframes float{50%{transform:rotate(4deg) translateY(-5px)}}
  .stack .ln{display:block;height:7px;border-radius:4px;background:#F1E8E3;margin:8px 0}
  .stack .ln.w6{width:60%}.stack .ln.w8{width:82%}.stack .ln.w4{width:42%}
  .stack .top{display:flex;align-items:center;gap:8px}
  .stack .top .agico{width:26px;height:26px}
  .stack .top .ln{flex:1;margin:0;background:#EADFD9}
  .stack .acts{display:flex;gap:6px;margin-top:14px}
  .stack .acts i{height:18px;border-radius:999px;flex:1;background:#F4EEEA}
  .stack .acts i:first-child{background:var(--ink);flex:1.3}
  .stack .count{position:absolute;right:-10px;top:-12px;min-width:34px;height:34px;padding:0 9px;border-radius:999px;background:var(--brand-gradient);color:#fff;font-family:var(--display);font-weight:800;font-size:.95rem;display:grid;place-items:center;box-shadow:0 10px 20px -8px rgba(232,93,117,.8);transform:rotate(4deg);border:3px solid #fff}
  :root[data-theme="dark"] .stack .card{background:var(--panel);border-color:var(--line)}
  :root[data-theme="dark"] .stack .ln,:root[data-theme="dark"] .stack .acts i{background:var(--bg-soft)}
  @media (max-width:1320px){.stack{display:none}.next__copy{max-width:none}}
  body.ask-open .stack{display:none}
  body.ask-open .next__copy{max-width:none}
  @media (max-width:1500px){body.ask-open .next,body.ask-open .duo{grid-template-columns:1fr}body.ask-open .next__main{border-right:0;border-bottom:1px solid var(--line)}}
  @media (prefers-reduced-motion:reduce){.stack .card:nth-child(3),.next__main .label::before{animation:none}}
  .next__main h2{font-family:var(--display);font-weight:700;font-size:1.5rem;letter-spacing:-.01em;margin:8px 0 4px}
  .next__main p{margin:0;color:var(--muted)}
  .next__main .btn{margin-top:26px}
  /* also waiting: two rows visible, the rest scroll */
  #also{max-height:122px;overflow-y:auto;overscroll-behavior:contain;scroll-snap-type:y mandatory;scrollbar-width:thin;scrollbar-color:var(--line-2) transparent;margin-right:-6px;padding-right:6px}
  #also .also{scroll-snap-align:start}
  .also-more{justify-self:start;display:inline-flex;align-items:center;gap:6px;margin-top:4px;height:26px;padding:0 10px;border-radius:999px;border:1px solid var(--line-2);background:var(--panel);font-size:.72rem;font-weight:700;color:var(--muted);cursor:pointer}
  .also-more:hover{color:var(--ink);border-color:rgba(36,26,20,.3)}
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
  .also{display:grid;grid-template-columns:38px 1fr auto;gap:12px;align-items:center;padding:10px 12px;border-radius:14px;border:1px solid transparent;text-decoration:none;color:inherit;transition:background-color .15s ease,border-color .15s ease,box-shadow .15s ease,transform .15s ease}
  .also:hover{background:var(--panel);border-color:var(--line);box-shadow:0 12px 24px -18px rgba(36,26,20,.55);transform:translateY(-1px);text-decoration:none}
  .also .ic{width:38px;height:38px;border-radius:12px;display:grid;place-items:center;background:var(--bg-soft)}
  .also .ic.t-hand{background:rgba(198,69,69,.1);color:var(--error)}
  .also .ic.t-q{background:rgba(123,92,240,.12);color:#6B4FD8}
  .also .ic.t-gap{background:rgba(47,116,232,.12);color:#2F74E8}
  .also em{transition:transform .2s ease,color .2s ease}
  .also:hover em{transform:translateX(3px);color:var(--rose)}
  .also b{display:block;font-size:.88rem;font-weight:600}
  .also span{color:var(--muted);font-size:.78rem}
  .also em{font-style:normal;color:var(--muted)}
  /* worth knowing + feed */
  .duo{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:22px;margin-bottom:22px;align-items:stretch}
  .duo .sec{margin:0}
  .finding{display:grid;gap:12px}
  .finding h3{font-family:var(--display);font-weight:700;font-size:1.15rem;margin:0;line-height:1.3}
  .finding p{margin:0;color:var(--muted);font-size:.86rem}
  .vs{display:grid;grid-template-columns:1fr auto 1fr;gap:10px;align-items:stretch}
  .vs blockquote{margin:0;padding:10px 12px;border-radius:10px;font-size:.82rem;background:var(--bg-soft)}
  .vs blockquote.warn{background:#FBF1E4}
  .vs blockquote em{display:block;font-style:normal;font-size:.7rem;font-weight:700;color:var(--muted);margin-bottom:3px}
  .vs .x{align-self:center;font-size:.7rem;font-weight:800;color:var(--muted)}
  /* agents at work: one list, filtered by stage or status */
  .agl{list-style:none;margin:0;padding:0;border:1px solid var(--line);border-radius:14px;overflow:hidden}
  .agl li + li{border-top:1px solid var(--line)}
  .agl{max-height:330px;overflow-y:auto;scrollbar-width:thin;scrollbar-color:var(--line-2) transparent}
  .agl a{display:grid;gap:14px;align-items:center;padding:12px 16px;color:inherit;text-decoration:none;transition:background-color .15s ease}
  .agl a:hover{background:var(--bg-soft)}
  .agl a{grid-template-columns:44px minmax(0,1fr) auto 64px 14px}
  .agl b{display:block;font-size:.88rem;font-weight:600}
  .agl .what{display:block;font-size:.8rem;color:var(--muted);overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
  .agl .stg{font-size:.76rem;font-weight:600;color:var(--muted)}
  .agl .st{display:inline-flex;align-items:center;gap:6px;font-size:.72rem;font-weight:700;letter-spacing:.04em;text-transform:uppercase;white-space:nowrap}
  .agl .st::before{content:"";width:7px;height:7px;border-radius:50%;background:currentColor}
  .agl .st.run{color:var(--success)}
  .agl .st.run::before{animation:livePulse 1.4s ease-in-out infinite}
  .agl .st.idle{color:var(--muted)}
  .agl .st.off{color:var(--muted);opacity:.6}
  .agl time{font-size:.78rem;color:var(--muted);text-align:right;white-space:nowrap}
  .agl .go{color:var(--muted);font-size:.9rem}
  .agl li.is-off b{color:var(--muted);font-weight:500}
  .agl .none{padding:22px;text-align:center;color:var(--muted);font-size:.86rem}
  .agl .stg{display:none}
  @media (max-width:600px){.agl a{grid-template-columns:44px minmax(0,1fr) auto}.agl time,.agl .go{display:none}}
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
  /* compact top: Up next and Your knowledge today */
  .next__main{padding:22px 26px}
  .next__main h2{font-size:1.3rem;margin:6px 0 4px}
  .next__main .btn{margin-top:16px;height:38px}
  .stack{width:150px;height:118px;right:28px}
  .stack .card{padding:12px}
  .stack .count{min-width:28px;height:28px;font-size:.82rem}
  .next__side{padding:14px 18px}
  .also{padding:7px 10px}
  .also .ic{width:32px;height:32px}
  .tiles{gap:12px}
  .tile{min-height:0;align-items:flex-start;justify-content:flex-start;text-align:left;gap:3px;padding:14px 16px 16px;border-radius:12px}
  .tile--soft{display:grid!important;grid-template-columns:auto 1fr;grid-template-rows:auto auto;column-gap:14px;align-items:center}
  .tile--soft .gauge{grid-row:1/span 2}
  .tile--soft .tile__lbl{white-space:nowrap;align-self:end}
  .tile--soft .tile__sub{align-self:start}
  .tile__lbl{font-size:.66rem}
  .tile__val{font-size:1.6rem}
  .tile__sub{font-size:.78rem;line-height:1.35}
  .tile__tag{top:10px;right:10px;height:20px;font-size:.62rem}
  .tile__go{right:12px;bottom:10px}
  .gauge{width:96px;height:58px;flex:none}
  .gauge svg{width:96px;height:54px}
  .gauge b{font-size:.92rem;bottom:-2px;text-align:center}
  .checks{margin-top:12px;padding-top:10px;font-size:.8rem}
  @media (max-width:1320px){.tile{min-height:0}}
""",
  body=r"""
    <div class="head">
      <div class="hello">
        <div><h1 id="ovTitle">Good evening, Sara <span class="wave" aria-hidden="true">👋</span></h1><p id="ovDate"></p></div>
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


    <section class="sec next" aria-labelledby="nextH">
      <div class="next__main">
        <div class="next__copy">
          <p class="label">Up next</p>
          <h2 id="nextH">Review 10 drafts</h2>
          <p id="nextSub"></p>
          <a class="btn btn--primary" href="build.html" id="nextCta">Start reviewing <span class="ar">→</span></a>
        </div>
        <div class="stack" id="stack" aria-hidden="true">
          <div class="card"></div><div class="card"></div>
          <div class="card"><div class="top"><span class="agico" data-agent="Drafting agent"></span><i class="ln"></i></div><i class="ln w8"></i><i class="ln w6"></i><i class="ln w4"></i><div class="acts"><i></i><i></i><i></i></div></div>
          <span class="count" id="stackN">10</span>
        </div>
      </div>
      <div class="next__side">
        <h3>Also waiting on you</h3>
        <div id="also"></div>
        <button class="also-more" id="alsoMore" type="button" hidden></button>
      </div>
    </section>

    <section class="sec" aria-labelledby="s1">
      <div class="sec__head"><h2 id="s1">Your knowledge today</h2><span>· What Oslo has in lojo right now</span></div>
      <div class="tiles" id="today"></div>
      <div class="checks" id="checks"></div>
    </section>

    <div class="duo">
    <section class="sec" aria-labelledby="agH">
      <div class="sec__head"><h2 id="agH">Agents at work</h2><span>· What each agent in your loop did last</span><a href="activity.html">View all agents →</a></div>
      <div class="agf chips" id="agFilters" role="group" aria-label="Filter agents"></div>
      <ul class="agl" id="agents"></ul>
    </section>

    <section class="sec" aria-labelledby="feedH">
        <div class="sec__head"><h2 id="feedH">Since you last looked</h2></div>
        <ul class="feed" id="feed"></ul>
      </section>
    </div>


    <div class="strip">
      <img src="assets/lojo-icon.png" alt="">
      <span><b>Coming in week 4:</b> Ask lojo opens for your team, and the readout lands.</span>
      <span class="spacer"></span>
      <a class="btn btn--secondary btn--sm" href="chat.html">Preview Ask lojo →</a>
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
$('loopBtn').addEventListener('click', () => { location.href = window.LOOP_URL || 'onboarding.html?inside=1'; });
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
  $('miniWhy').textContent = valNow ? c.pending + ' draft' + (c.pending === 1 ? '' : 's') + ' waiting' : 'Ask lojo ready to try';
  $('miniK').textContent = c.approved;
}
// agents at work: one list, filtered by stage or by who's running now
let agFilter = 'all';

function renderAgents(c) {
  const waits = { ins: c.needCall, bld: c.pending };
  const n = (f) => AGENTS.filter(f).length;
  const chips = [['all', 'All', n(() => true)], ['run', '<i class="live"></i>Working', n(a => a[2] === 0)]]
    .concat(AG_STAGES.map(([k, label]) => [k, (waits[k] ? '<i class="w" title="Waiting on you"></i>' : '') + label.slice(3), n(a => a[0] === k)]));
  $('agFilters').innerHTML = chips.map(([k, label, cnt]) => '<button type="button" class="chip" data-agf="' + k + '" aria-pressed="' + (agFilter === k) + '">' + label + ' <em>' + cnt + '</em></button>').join('');
  const list = AGENTS.filter(a => agFilter === 'all' || (agFilter === 'run' ? a[2] === 0 : a[0] === agFilter));
  $('agents').innerHTML = list.length ? list.map(([k, name, min, what]) => {
    const s = AG_STAGES.find(x => x[0] === k);
    const st = min === null ? '<span class="st off">Not yet</span>' : min === 0 ? '<span class="st run">Working</span>' : '<span class="st idle">Idle</span>';
    return '<li' + (min === null ? ' class="is-off"' : '') + '><a href="' + s[2] + '">' + ava3d(k, name, min) + '<span style="min-width:0"><b>' + esc(name) + '</b><span class="what">' + esc(what) + '</span></span>' +
      '<span class="stg">' + s[1] + '</span>' + st + '<time>' + agAgo(min) + '</time><span class="go">→</span></a></li>';
  }).join('') : '<li class="none">No agent is running right now.</li>';
}
$('agFilters').addEventListener('click', (e) => { const b = e.target.closest('[data-agf]'); if (!b) return; agFilter = b.dataset.agf; renderAgents(counts()); });
function render() {
  const c = counts();
  let first = 'Sara';
  try { const u = JSON.parse(sessionStorage.getItem('lojo-user')); if (u && u.name) first = u.name.trim().split(' ')[0]; } catch (e) {}
  const hr = new Date().getHours();
  $('ovTitle').innerHTML = (hr < 12 ? 'Good morning' : hr < 18 ? 'Good afternoon' : 'Good evening') + ', ' + esc(first) + ' <span class="wave" aria-hidden="true">👋</span>';
  $('ovDate').textContent = new Date().toLocaleDateString('en-GB', { weekday: 'long', day: 'numeric', month: 'long' }) + ' · week ' + POC_WEEK + ' of 4';
  miniLoop(c);

  // up next + weekly target
  const decided = c.approved + c.final, mins = Math.max(1, Math.round(c.pending * 1.2));
  if (c.pending) {
    $('nextH').innerHTML = 'Review <span class="num">' + c.pending + '</span> draft' + (c.pending > 1 ? 's' : '');
    $('stackN').textContent = c.pending; $('stack').hidden = false;
    $('nextSub').textContent = 'Approve, edit, or reject with a reason; a rejected draft is written again up to twice.';
    $('nextCta').innerHTML = 'Start reviewing <span class="ar">→</span>'; $('nextCta').href = 'build.html';
  } else {
    $('nextH').textContent = 'Try Ask lojo';
    $('nextSub').textContent = 'The first batch is reviewed. Ask it questions: it answers only from what you approved.';
    $('nextCta').innerHTML = 'Open Ask lojo <span class="ar">→</span>'; $('nextCta').href = 'chat.html'; $('stack').hidden = true;
  }

  const also = [];
  const noSource = allQuestions().filter(q => (!q.docs || !q.docs.length) && matters(q) !== false).length;
  const human = c.final + noSource, failedDrafts = Object.keys(ST.draftFailed || {}).filter(k => ST.draftFailed[k] && ST.draftFailed[k] !== 'retrying').length;
  if (human) also.push({ ic: 'hand', t: human + ' question' + (human === 1 ? ' needs' : 's need') + ' a human answer', s: 'No source, or rejected three times', href: 'insights.html#questions' });
  if (failedDrafts) also.push({ ic: 'q', t: failedDrafts + ' draft' + (failedDrafts === 1 ? '' : 's') + ' could not be written', s: 'Try ' + (failedDrafts === 1 ? 'it' : 'them') + ' again from Insights', href: 'insights.html?demo=failed' });
  if (c.needCall) also.push({ ic: 'q', t: 'Say whether ' + c.needCall + ' question' + (c.needCall > 1 ? 's matter' : ' matters'), s: 'Only those get drafted', href: 'insights.html#questions' });
  if (c.gaps) also.push({ ic: 'gap', t: c.gaps + ' gaps need a source', s: 'Send a document or add them as questions', href: 'insights.html#gaps' });
  $('alsoMore').hidden = also.length <= 2; $('alsoMore').textContent = '+' + (also.length - 2) + ' more ↓';
  $('also').innerHTML = also.length ? also.map(i => '<a class="also" href="' + i.href + '"><span class="ic t-' + i.ic + '">' + ICON[i.ic] + '</span><div><b>' + esc(i.t) + '</b><span>' + esc(i.s) + '</span></div><em>→</em></a>').join('') : '<p class="sub">Nothing else right now.</p>';

  // since you last looked
  const rewrites = DRAFTS.filter(r => decision(r).redrafted).length;
  const feed = [
    { ic: 'sync', t: rewrites + ' rejected draft' + (rewrites === 1 ? ' was' : 's were') + ' written again', s: 'Using your reasons · overnight' },
    { ic: 'q', t: '4 new questions found', s: 'In Sales call notes, Billing FAQ and your help pages · yesterday' },
    { ic: 'doc', t: 'Security overview indexed', s: '51 passages, searchable by meaning · yesterday' },
    { ic: 'check', t: 'You approved ' + c.approved + ' answers', s: 'They’re in the store, ready for Ask lojo · Tue 29 Sep' },
  ];
  renderAgents(c);
  $('feed').innerHTML = feed.map(f => '<li><span class="dot">' + ICON[f.ic] + '</span><div><b>' + esc(f.t) + '</b><span>' + esc(f.s) + '</span></div></li>').join('');

  // merged tiles
  const yours = allQuestions().filter(q => q.origin === 'you').length;
  $('today').innerHTML = [
    '<a class="tile tile--soft" href="build.html">' + gauge(decided / c.drafts, '#4F7A2F') + '<span class="tile__lbl">Review progress ' + tip('Drafts in the first batch that you have approved, edited or left for a human answer.') + '</span><span class="tile__sub">' + decided + ' of ' + c.drafts + ' decided · ' + c.approved + ' approved</span><span class="tile__go">→</span></a>',
    '<a class="tile tile--ok" href="sources.html"><span class="tile__tag">Indexed</span><span class="tile__lbl">Sources ' + tip('Documents you sent us. Their text is pulled out, split into passages and indexed by meaning.') + '</span><span class="tile__val">' + c.docs + '</span><span class="tile__sub">' + c.pages + ' pages · ' + c.passages + ' passages</span></a>',
    '<a class="tile' + (c.needCall ? ' tile--warn' : '') + '" href="insights.html#questions">' + (c.needCall ? '<span class="tile__tag">' + c.needCall + ' need your call</span>' : '') + '<span class="tile__lbl">Questions ' + tip('Questions your documents answer, found by the agent, plus the ones you added.') + '</span><span class="tile__val">' + c.questions + '</span><span class="tile__sub">' + (c.questions - yours) + ' found · ' + yours + ' from you</span></a>',
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
$('alsoMore').addEventListener('click', () => $('also').scrollBy({ top: 62, behavior: 'smooth' }));
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
  .scope.is-pending{grid-template-columns:36px 1fr;background:rgba(217,154,43,.07);border-color:rgba(217,154,43,.35)}
  .scope.is-pending .ok{background:rgba(217,154,43,.16);color:#94660F}
  .scope .confirm{grid-column:2;display:flex;gap:12px;align-items:center;flex-wrap:wrap;margin-top:4px}
  .scope .confirm label{display:flex;gap:8px;align-items:center;font-size:.86rem;font-weight:600;cursor:pointer}
  .scope .confirm input{width:17px;height:17px;accent-color:var(--rose)}
  .dcard{margin-top:26px;overflow:hidden}
  .dcard .card__head{padding:20px 24px}
  .dscroll{overflow-x:auto}
  .dtable{width:100%;border-collapse:collapse;font-size:.92rem}
  .dtable th{text-align:left;font-size:.7rem;letter-spacing:.12em;text-transform:uppercase;color:var(--muted);font-weight:700;padding:14px 20px;border-bottom:1px solid var(--line);white-space:nowrap}
  .dtable td{padding:14px 20px;border-bottom:1px solid var(--line);vertical-align:middle}
  .dtable tbody tr:last-child td{border-bottom:0}
  .dtable .num{text-align:right;font-variant-numeric:tabular-nums;width:110px}
  .dtable .tacts{width:170px;text-align:right;white-space:nowrap}
  .tacts .btn{height:30px;padding:0 10px;font-size:.76rem;margin-left:4px}
  .dname{display:flex;align-items:center;gap:14px;font-weight:500}
  .dname .ext{width:42px;height:42px;border-radius:10px;background:var(--bg-soft);display:grid;place-items:center;font-size:.62rem;font-weight:700;color:var(--muted);text-transform:uppercase;flex:none}
  .dn{min-width:0}
  .dn .nm{display:flex;align-items:center;gap:8px;flex-wrap:wrap}
  .dst{display:inline-flex;align-items:center;gap:6px;font-size:.88rem;font-weight:500;white-space:nowrap}
  .dst.ok{color:var(--success)} .dst.run{color:var(--info)} .dst.fail{color:var(--error)} .dst.wait,.dst.ret{color:var(--muted)}
  tr.is-row{cursor:pointer}
  tr.is-row:hover td,tr.is-open td{background:var(--bg-soft)}
  tr.is-row .tacts .btn--ghost{opacity:0;transition:opacity .15s ease}
  tr.is-row .tacts .dlbtn{opacity:1}
  tr.is-row:hover .tacts .btn--ghost,tr.is-row .tacts .btn--ghost:focus-visible,tr.is-open .tacts .btn--ghost{opacity:1}
  tr.is-failed td{background:rgba(198,69,69,.03)}
  tr.is-retired .nm,tr.is-retired .ext{opacity:.55}
  tr.is-retired .nm{text-decoration:line-through;text-decoration-color:rgba(36,26,20,.3)}
  tr.ddetail td{background:var(--bg-soft);padding:0 20px 16px 76px}
  tr.drow.is-pin td{background:rgba(255,177,153,.18)}
  .acts .btn{height:30px;padding:0 10px;font-size:.76rem}
  .sr-only{position:absolute;left:-9999px}
  @media (max-width:760px){.dtable th:nth-child(2),.dtable td:nth-child(2),.dtable th:nth-child(4),.dtable td:nth-child(4){display:none}tr.ddetail td{padding-left:20px}}
  .listhead h2{font-family:var(--display);font-weight:700;font-size:1.05rem;margin:0}
  .file{cursor:default}
  .file.is-row{cursor:pointer}
  .file.is-row:hover,.file.is-open{border-color:var(--line-2);background:var(--bg-soft)}
  .file.is-failed{border-color:rgba(198,69,69,.3);background:rgba(198,69,69,.03)}
  .file.is-retired .name{opacity:.6;text-decoration:line-through;text-decoration-color:rgba(36,26,20,.3)}
  .file.is-retired .ext{opacity:.6}
  .why{display:block;font-size:.78rem;color:var(--error);font-weight:500;margin-top:3px;white-space:normal}
  .why.mute{color:var(--muted)}
  .acts{display:flex;gap:6px;justify-content:flex-end;min-width:72px}
  .acts .btn{height:30px;padding:0 12px;font-size:.76rem}
  .file.is-row .acts .btn--ghost{opacity:0}
  .file.is-row:hover .acts .btn--ghost,.file.is-row .acts .btn--ghost:focus-visible{opacity:1}
  .fdetail{grid-column:1/-1;padding:6px 0 4px 50px}
  .passage{border-left:3px solid var(--line-2);padding:6px 12px;margin:8px 0;font-size:.84rem;color:var(--ink);background:var(--panel);border-radius:0 8px 8px 0}
  .passage em{display:block;font-style:normal;color:var(--muted);font-size:.72rem;margin-bottom:2px}
  .passage.is-hit{border-left-color:var(--rose);background:rgba(255,177,153,.22)}
  .file.is-pin{border-color:var(--rose);box-shadow:0 0 0 3px rgba(232,93,117,.14)}
  .folder{display:flex;gap:8px;margin-top:14px}
  .uperr{margin:0 0 16px;padding:14px 16px;border-radius:14px;border:1px solid rgba(198,69,69,.3);background:rgba(198,69,69,.05)}
  .uperr__h{display:flex;align-items:center;gap:10px;font-weight:700;font-size:.9rem;color:var(--error)}
  .uperr__h button{margin-left:auto}
  .uperr ul{list-style:none;margin:10px 0 0;padding:0;display:grid;gap:6px}
  .uperr li{display:grid;grid-template-columns:auto 1fr;gap:10px;font-size:.84rem;align-items:baseline}
  .uperr li b{font-weight:600}
  .uperr li span{color:var(--muted)}
  .synced{display:grid;gap:8px;margin-top:16px}
  .synced .file{grid-template-columns:36px minmax(0,1fr) auto auto}
  @media (max-width:760px){.scope-detail{grid-template-columns:1fr}.fdetail{padding-left:0}.folder{flex-direction:column}}
""",
  body=r"""
    <div class="head">
      <div>
        <p class="label">01 Source</p>
        <h1>Sources</h1>
        <p>Upload documents or connect an app. We pull the text out, split it into passages and index each one by meaning, so a question finds the right passage even when the words differ.</p>
      </div>
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

    <div class="ptabs" role="tablist" aria-label="Source type">
      <button class="ptab" role="tab" data-tab="docs" aria-selected="true"><svg viewBox="0 0 24 24"><path d="M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8z"/><path d="M14 3v5h5"/></svg>Documents <span class="n" id="nDocs">0</span></button>
      <button class="ptab" role="tab" data-tab="connect" aria-selected="false"><svg viewBox="0 0 24 24"><path d="M9 7V3M15 7V3M7 7h10v4a5 5 0 0 1-10 0zM12 16v5"/></svg>Connect <span class="n" id="nConn">0</span></button>
    </div>

    <section id="tabDocs">
      <section class="uperr" id="upErr" hidden role="alert"></section>
      <label class="drop" id="drop">
        <span class="ico"><svg viewBox="0 0 24 24"><path d="M12 16V4M7 9l5-5 5 5"/><path d="M4 16v3a1 1 0 0 0 1 1h14a1 1 0 0 0 1-1v-3"/></svg></span>
        <strong>Drop files here, or browse</strong>
        <p class="hint">PDF, DOCX, Markdown or TXT · up to 25 MB each</p>
        <input type="file" id="fileInput" multiple hidden>
        <span class="row"><span class="btn btn--secondary btn--sm">Browse files</span></span>
      </label>
      <section class="card dcard" aria-labelledby="docH">
        <div class="card__head"><h2 id="docH">Your documents</h2><span class="sub" id="docMeta"></span></div>
        <div class="dscroll"><table class="dtable">
          <thead><tr><th>Document</th><th class="num">Pages</th><th class="num">Passages</th><th class="num">Questions</th><th>Status</th><th class="tacts"><span class="sr-only">Actions</span></th></tr></thead>
          <tbody id="docRows"></tbody>
        </table></div>
      </section>
    </section>

    <section id="tabConnect" hidden>
      <!-- ASSUMPTION: connector list is illustrative; sign-in is simulated. check with Eric -->
      <div class="panel">
        <h3>Connect an app</h3>
        <p class="sub" style="margin-bottom:14px">You sign in with that app and pick what lojo can read. lojo only reads; it never edits your files.</p>
        <div class="apps" id="apps"></div>
        <div class="synced" id="synced"></div>
      </div>
      <div class="panel">
        <h3>Send us a folder</h3>
        <p class="sub">Share a Google Drive, SharePoint or Dropbox folder. Give view access to ingest@lojo.ai, then paste the link.</p>
        <div class="folder">
          <input class="text" id="folderLink" placeholder="https://drive.google.com/drive/folders/…" aria-label="Shared folder link">
          <button class="btn btn--primary" id="folderSend">Send</button>
        </div>
      </div>
    </section>
""",
  js=r"""
let open = null;
const extra = [];
const APPS = [
  { id: 'notion', name: 'Notion', kind: 'Pages & wikis', mono: 'N', color: 'var(--ink)', n: 5 },
  { id: 'website', name: 'Website', kind: 'Web parsing', mono: 'W', color: '#3E6FA6', n: 3 },
  { id: 'gdrive', name: 'Google Drive', kind: 'Docs & files', mono: 'GD', color: '#1A73E8', n: 6 },
  { id: 'sharepoint', name: 'SharePoint', kind: 'Sites & libraries', mono: 'SP', color: '#036C70', n: 5 },
  { id: 'confluence', name: 'Confluence', kind: 'Spaces', mono: 'C', color: '#0C66E4', n: 4 },
  { id: 'gmail', name: 'Gmail', kind: 'Email', mono: 'M', color: '#D93025', n: 3 },
  { id: 'aircall', name: 'Aircall', kind: 'Calls', mono: 'A', color: '#00B388', n: 2 },
  { id: 'gsheets', name: 'Google Sheets', kind: 'Spreadsheets', mono: 'GS', color: '#188038', n: 2 },
];
const LOGO = {"notion": "<path d=\"M4.459 4.208c.746.606 1.026.56 2.428.466l13.215-.793c.28 0 .047-.28-.046-.326L17.86 1.968c-.42-.326-.981-.7-2.055-.607L3.01 2.295c-.466.046-.56.28-.374.466zm.793 3.08v13.904c0 .747.373 1.027 1.214.98l14.523-.84c.841-.046.935-.56.935-1.167V6.354c0-.606-.233-.933-.748-.887l-15.177.887c-.56.047-.747.327-.747.933zm14.337.745c.093.42 0 .84-.42.888l-.7.14v10.264c-.608.327-1.168.514-1.635.514-.748 0-.935-.234-1.495-.933l-4.577-7.186v6.952L12.21 19s0 .84-1.168.84l-3.222.186c-.093-.186 0-.653.327-.746l.84-.233V9.854L7.822 9.76c-.094-.42.14-1.026.793-1.073l3.456-.233 4.764 7.279v-6.44l-1.215-.139c-.093-.514.28-.887.747-.933zM1.936 1.035l13.31-.98c1.634-.14 2.055-.047 3.082.7l4.249 2.986c.7.513.934.653.934 1.213v16.378c0 1.026-.373 1.634-1.68 1.726l-15.458.934c-.98.047-1.448-.093-1.962-.747l-3.129-4.06c-.56-.747-.793-1.306-.793-1.96V2.667c0-.839.374-1.54 1.447-1.632z\"/>", "gdrive": "<path d=\"M12.01 1.485c-2.082 0-3.754.02-3.743.047.01.02 1.708 3.001 3.774 6.62l3.76 6.574h3.76c2.081 0 3.753-.02 3.742-.047-.005-.02-1.708-3.001-3.775-6.62l-3.76-6.574zm-4.76 1.73a789.828 789.861 0 0 0-3.63 6.319L0 15.868l1.89 3.298 1.885 3.297 3.62-6.335 3.618-6.33-1.88-3.287C8.1 4.704 7.255 3.22 7.25 3.214zm2.259 12.653-.203.348c-.114.198-.96 1.672-1.88 3.287a423.93 423.948 0 0 1-1.698 2.97c-.01.026 3.24.042 7.222.042h7.244l1.796-3.157c.992-1.734 1.85-3.23 1.906-3.323l.104-.167h-7.249z\"/>", "gsheets": "<path d=\"M11.318 12.545H7.91v-1.909h3.41v1.91zM14.728 0v6h6l-6-6zm1.363 10.636h-3.41v1.91h3.41v-1.91zm0 3.273h-3.41v1.91h3.41v-1.91zM20.727 6.5v15.864c0 .904-.732 1.636-1.636 1.636H4.909a1.636 1.636 0 0 1-1.636-1.636V1.636C3.273.732 4.005 0 4.909 0h9.318v6.5h6.5zm-3.273 2.773H6.545v7.909h10.91v-7.91zm-6.136 4.636H7.91v1.91h3.41v-1.91z\"/>", "gmail": "<path d=\"M24 5.457v13.909c0 .904-.732 1.636-1.636 1.636h-3.819V11.73L12 16.64l-6.545-4.91v9.273H1.636A1.636 1.636 0 0 1 0 19.366V5.457c0-2.023 2.309-3.178 3.927-1.964L5.455 4.64 12 9.548l6.545-4.91 1.528-1.145C21.69 2.28 24 3.434 24 5.457z\"/>", "confluence": "<path d=\"M.87 18.257c-.248.382-.53.875-.763 1.245a.764.764 0 0 0 .255 1.04l4.965 3.054a.764.764 0 0 0 1.058-.26c.199-.332.454-.763.733-1.221 1.967-3.247 3.945-2.853 7.508-1.146l4.957 2.337a.764.764 0 0 0 1.028-.382l2.364-5.346a.764.764 0 0 0-.382-1 599.851 599.851 0 0 1-4.965-2.361C10.911 10.97 5.224 11.185.87 18.257zM23.131 5.743c.249-.405.531-.875.764-1.25a.764.764 0 0 0-.256-1.034L18.675.404a.764.764 0 0 0-1.058.26c-.195.335-.451.763-.734 1.225-1.966 3.246-3.945 2.85-7.508 1.146L4.437.694a.764.764 0 0 0-1.027.382L1.046 6.422a.764.764 0 0 0 .382 1c1.039.49 3.105 1.467 4.965 2.361 6.698 3.246 12.392 3.029 16.738-4.04z\"/>", "aircall": "<path d=\"M23.451 5.906a6.978 6.978 0 0 0-5.375-5.39C16.727.204 14.508 0 12 0S7.273.204 5.924.516a6.978 6.978 0 0 0-5.375 5.39C.237 7.26.034 9.485.034 12s.203 4.74.515 6.094a6.978 6.978 0 0 0 5.375 5.39C7.273 23.796 9.492 24 12 24s4.727-.204 6.076-.516a6.978 6.978 0 0 0 5.375-5.39c.311-1.354.515-3.578.515-6.094 0-2.515-.203-4.74-.515-6.094zm-5.873 12.396l-.003.001c-.428.152-1.165.283-2.102.377l-.147.014a.444.444 0 0 1-.45-.271 1.816 1.816 0 0 0-1.296-1.074c-.351-.081-.928-.134-1.58-.134s-1.229.053-1.58.134a1.817 1.817 0 0 0-1.291 1.062.466.466 0 0 1-.471.281 8 8 0 0 0-.129-.012c-.938-.094-1.676-.224-2.105-.377l-.003-.001a.76.76 0 0 1-.492-.713c0-.032.003-.066.005-.098.073-.979.666-3.272 1.552-5.89C8.5 8.609 9.559 6.187 10.037 5.714a1.029 1.029 0 0 1 .404-.26l.004-.002c.314-.106.892-.178 1.554-.178.663 0 1.241.071 1.554.178l.005.002a1.025 1.025 0 0 1 .405.26c.478.472 1.537 2.895 2.549 5.887.886 2.617 1.479 4.91 1.552 5.89.002.032.005.066.005.098a.76.76 0 0 1-.491.713z\"/>", "sharepoint": "<path d=\"M24 13.5q0 1.242-.475 2.332-.474 1.09-1.289 1.904-.814.815-1.904 1.29-1.09.474-2.332.474-.762 0-1.523-.2-.106.997-.557 1.858-.451.862-1.154 1.494-.704.633-1.606.99-.902.358-1.91.358-1.09 0-2.045-.416-.955-.416-1.664-1.125-.709-.709-1.125-1.664Q6 19.84 6 18.75q0-.188.018-.375.017-.188.04-.375H.997q-.41 0-.703-.293T0 17.004V6.996q0-.41.293-.703T.996 6h3.54q.14-1.277.726-2.373.586-1.096 1.488-1.904Q7.652.914 8.807.457 9.96 0 11.25 0q1.395 0 2.625.533T16.02 1.98q.914.915 1.447 2.145T18 6.75q0 .188-.012.375-.011.188-.035.375 1.242 0 2.344.469 1.101.468 1.928 1.277.826.809 1.3 1.904Q24 12.246 24 13.5zm-12.75-12q-.973 0-1.857.34-.885.34-1.577.943-.691.604-1.154 1.43Q6.2 5.039 6.06 6h4.945q.41 0 .703.293t.293.703v4.945l.21-.035q.212-.75.61-1.424.399-.673.944-1.218.545-.545 1.213-.944.668-.398 1.43-.61.093-.503.093-.96 0-1.09-.416-2.045-.416-.955-1.125-1.664-.709-.709-1.664-1.125Q12.34 1.5 11.25 1.5zM6.117 15.902q.54 0 1.06-.111.522-.111.932-.37.41-.257.662-.679.252-.422.252-1.055 0-.632-.263-1.054-.264-.422-.662-.703-.399-.282-.856-.463l-.855-.34q-.399-.158-.662-.334-.264-.176-.264-.445 0-.2.14-.323.141-.123.335-.193.193-.07.404-.094.21-.023.351-.023.598 0 1.055.152.457.153.95.457V8.543q-.282-.082-.522-.14-.24-.06-.475-.1-.234-.041-.486-.059-.252-.017-.557-.017-.515 0-1.054.117-.54.117-.979.375-.44.258-.715.68-.275.421-.275 1.03 0 .598.263.997.264.398.663.68.398.28.855.474l.856.363q.398.17.662.358.263.187.263.457 0 .222-.123.351-.123.13-.31.2-.188.07-.393.087-.205.018-.369.018-.703 0-1.248-.234-.545-.235-1.107-.621v1.875q1.195.468 2.472.468zM11.25 22.5q.773 0 1.453-.293t1.19-.803q.51-.51.808-1.195.299-.686.299-1.459 0-.668-.223-1.277-.222-.61-.62-1.096-.4-.486-.95-.826-.55-.34-1.207-.48v1.933q0 .41-.293.703t-.703.293H7.57q-.07.375-.07.75 0 .773.293 1.459t.803 1.195q.51.51 1.195.803.686.293 1.459.293zM18 18q.926 0 1.746-.352.82-.351 1.436-.966.615-.616.966-1.43.352-.815.352-1.752 0-.926-.352-1.746-.351-.82-.966-1.436-.616-.615-1.436-.966Q18.926 9 18 9t-1.74.357q-.815.358-1.43.973t-.973 1.43q-.357.814-.357 1.74 0 .129.006.258t.017.258q.551.27 1.02.65t.838.855q.369.475.627 1.026.258.55.387 1.148Q17.18 18 18 18Z\"/>", "website": "<circle cx=\"12\" cy=\"12\" r=\"9\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"1.8\"/><path d=\"M3 12h18M12 3c2.5 2.6 3.8 5.6 3.8 9s-1.3 6.4-3.8 9c-2.5-2.6-3.8-5.6-3.8-9S9.5 5.6 12 3z\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"1.8\"/>"};
ST.apps = ST.apps || {};
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
const pendingScope = () => forceScope ? !ST.__scopeOk : !ST.scope.signed;
function renderScope() {
  const el = $('scope');
  el.classList.toggle('is-pending', pendingScope());
  if (pendingScope()) {
    // G17: before scope is confirmed, documents wait and the checkbox sits on this page
    el.innerHTML = '<span class="ok">!</span><div><b>Confirm what’s in scope</b><span class="sub">We hold your documents until you confirm them. Personal details are not removed automatically in this phase, so only include what we agreed on.</span></div>' +
      '<div class="confirm"><label><input type="checkbox" id="scopeChk"> These documents are in scope</label><button class="btn btn--primary btn--sm" id="scopeGo" disabled>Confirm and start processing</button></div>';
    $('scopeChk').onchange = () => { $('scopeGo').disabled = !$('scopeChk').checked; };
    $('scopeGo').onclick = () => { ST.scope.signed = true; ST.__scopeOk = true; save(); renderScope(); render(); toast('Scope confirmed. Processing starts now.'); };
  } else {
    $('scopeSub').textContent = 'By ' + ST.scope.by + ' on ' + ST.scope.at + ' · personal details are not removed automatically';
  }
}
// one table row per document; failed, waiting and retired rows say why under the name
const ST_TXT = { done: ['✓ Indexed', 'ok'], run: ['', 'run'], fail: ['✕ Couldn’t process', 'fail'], wait: ['Waiting', 'wait'], ret: ['Retired', 'ret'] };
const docRow = (o) => '<tr class="drow' + (o.cls || '') + '"' + (o.id ? ' data-id="' + o.id + '"' : '') + '><td><span class="dname"><span class="ext">' + esc(o.ext) + '</span><span class="dn"><span class="nm">' + esc(o.name) + (o.badge || '') + '</span>' + (o.why || '') + '</span></span></td>' +
  '<td class="num">' + (o.pages ?? '–') + '</td><td class="num">' + (o.passages ?? '–') + '</td><td class="num">' + (o.qs ? o.qs : '–') + '</td>' +
  '<td><span class="dst ' + ST_TXT[o.st][1] + '">' + (o.st === 'run' ? '<span class="spin" style="width:10px;height:10px"></span> ' + esc(o.stage) : ST_TXT[o.st][0]) + '</span></td>' +
  '<td class="tacts">' + (o.acts || '') + '</td></tr>' + (o.detail ? '<tr class="ddetail"><td colspan="6">' + o.detail + '</td></tr>' : '');
function render() {
  const docx = ST.docx || [];
  const live = DOCS.filter(d => !ST.retired[d.id]).length + extra.length + docx.filter(d => d.status !== 'retired').length;
  $('nDocs').textContent = live;
  $('nConn').textContent = Object.keys(ST.apps).length;
  const c = counts();
  $('docMeta').textContent = live + ' documents · ' + c.pages + ' pages · ' + c.passages + ' passages';
  const rows = [];
  docx.forEach(d => {
    if (d.status === 'retired') return;
    const base = { ext: d.ext, name: d.name };
    if (d.status === 'failed') rows.push(docRow({ ...base, cls: ' is-failed', st: 'fail', why: '<span class="why">' + esc(d.reason) + '</span>',
      acts: '<button class="btn btn--secondary" data-retry="' + d.id + '">Try again</button><button class="btn btn--ghost" style="opacity:1" data-remove="' + d.id + '">Remove</button>' }));
    else if (d.status === 'waiting') rows.push(docRow({ ...base, st: 'wait', why: '<span class="why mute">' + (pendingScope() ? 'Waiting for you to confirm scope.' : 'In the queue. Processing starts in about 2 minutes.') + '</span>',
      acts: '<button class="btn btn--ghost" style="opacity:1" data-remove="' + d.id + '">Cancel</button>' }));
    else if (d.status === 'running') rows.push(docRow({ ...base, st: 'run', stage: d.stage || 'Extracting text' }));
    else rows.push(docRow({ ...base, st: 'done', pages: d.pages || 4, passages: Math.round((d.pages || 4) * 4.6) }));
  });
  extra.forEach(f => rows.push(docRow({ ext: f.ext, name: f.name, st: f.done ? 'done' : 'run', stage: f.stage, pages: f.done ? f.pages : undefined, passages: f.done ? f.passages : undefined })));
  DOCS.forEach(d => {
    if (ST.retired[d.id]) return;
    const ext = d.name.split('.').pop(), n = Math.round(d.pages * 4.6), qs = qsFor(d.id);
    let detail = '';
    if (open === d.id) {
      const all = passagesFor(d.id), hit = typeof pinLoc === 'string' && d.id === pinDoc ? all.filter(p => p.loc === pinLoc) : [];
      const ps = hit.concat(all.filter(p => !hit.includes(p))).slice(0, 3);
      detail = '<div class="fdetail"><p class="sub" style="margin:6px 0 2px">Sample passages</p>' +
        (ps.length ? ps.map(p => '<div class="passage"><em>' + esc(p.loc) + '</em>' + esc(p.text) + '</div>').join('') : '<p class="sub">No passages sampled yet.</p>') +
        (qs.length ? '<p class="sub" style="margin:10px 0 6px">Questions found here</p><div class="chips">' + qs.map(q => '<a class="chip" href="insights.html#questions">' + esc(q.q) + '</a>').join('') + '</div>' : '') + '</div>';
    }
    rows.push(docRow({ id: d.id, cls: ' is-row' + (open === d.id ? ' is-open' : ''), ext, name: d.name, badge: d.faq ? ' <span class="badge badge--info">Your help pages</span>' : '',
      pages: d.pages, passages: n, qs: qs.length, st: 'done',
      acts: '<button class="btn btn--ghost dlbtn" data-dl="' + d.id + '" title="Download" aria-label="Download ' + esc(d.name) + '">' + DL_ICON + '</button><button class="btn btn--ghost" data-retire="' + d.id + '">Retire</button>', detail }));
  });
  // G4: retired documents stay listed, greyed, and can be restored
  DOCS.filter(d => ST.retired[d.id]).forEach(d => rows.push(docRow({ cls: ' is-retired', ext: d.name.split('.').pop(), name: d.name, st: 'ret', pages: d.pages, why: '<span class="why mute">Retired just now by Sara Lindqvist</span>',
    acts: '<button class="btn btn--secondary" data-restore="' + d.id + '" data-base="1">Restore</button>' })));
  docx.filter(d => d.status === 'retired').forEach(d => rows.push(docRow({ cls: ' is-retired', ext: d.ext, name: d.name, st: 'ret', why: '<span class="why mute">' + esc(d.retiredNote) + '</span>',
    acts: '<button class="btn btn--secondary" data-restore="' + d.id + '">Restore</button>' })));
  $('docRows').innerHTML = rows.join('');
  renderApps();
}
function renderApps() {
  $('apps').innerHTML = APPS.map(a => '<button type="button" class="app' + (ST.apps[a.id] ? ' is-on' : '') + '" data-app="' + a.id + '"><span class="mono logo" style="color:' + a.color + '"><svg viewBox="0 0 24 24" aria-hidden="true">' + LOGO[a.id] + '</svg></span><span><b>' + esc(a.name) + '</b><span class="k">' + (ST.apps[a.id] ? 'Connected · ' + a.n + ' documents' : esc(a.kind)) + '</span></span></button>').join('');
  const on = APPS.filter(a => ST.apps[a.id]);
  $('synced').innerHTML = on.map(a => '<div class="file"><span class="mono logo" style="color:' + a.color + '"><svg viewBox="0 0 24 24" aria-hidden="true">' + LOGO[a.id] + '</svg></span><span><span class="name">' + esc(a.name) + '</span><span class="meta">Connected as sara@oslo.com · ' + a.n + ' documents · reads only</span></span><span class="pstage is-done">Synced</span><span class="acts"><button class="btn btn--ghost" style="opacity:1" data-off="' + a.id + '">Disconnect</button></span></div>').join('');
}
$('apps').addEventListener('click', (e) => {
  const b = e.target.closest('[data-app]'); if (!b || ST.apps[b.dataset.app]) return;
  const a = APPS.find(x => x.id === b.dataset.app);
  b.classList.add('is-busy'); b.disabled = true;
  b.querySelector('.k').innerHTML = '<span class="spin" style="width:11px;height:11px;vertical-align:-1px"></span> Connecting…';
  setTimeout(() => { ST.apps[a.id] = true; save(); render(); toast(a.name + ' connected as sara@oslo.com'); }, 900);
});
$('synced').addEventListener('click', (e) => { const b = e.target.closest('[data-off]'); if (!b) return; delete ST.apps[b.dataset.off]; save(); render(); toast('Disconnected. Documents already indexed stay until you retire them.'); });
$('docRows').addEventListener('click', (e) => {
  const b = e.target.closest('button');
  if (!b) { const li = e.target.closest('tr.is-row'); if (li && !e.target.closest('a')) { open = open === li.dataset.id ? null : li.dataset.id; render(); } return; }
  const docx = ST.docx || [];
  if (b.dataset.retry) {
    const d = docx.find(x => x.id === b.dataset.retry); d.status = 'running'; d.stage = 'Extracting text'; render();
    setTimeout(() => { d.status = 'failed'; d.reason = 'Still password-protected. Remove the password in your PDF app, then upload the file again.'; save(); render(); toastError('Holiday policy 2025.pdf still couldn’t be processed.'); }, 1600);
  }
  if (b.dataset.remove) { ST.docx = docx.filter(x => x.id !== b.dataset.remove); save(); render(); toast('Removed'); }
  if (b.dataset.restore) {
    if (b.dataset.base) delete ST.retired[b.dataset.restore]; else { const d = docx.find(x => x.id === b.dataset.restore); d.status = 'indexed'; }
    save(); render(); toast('Restored. Its passages are used for drafts again.');
  }
  if (b.dataset.retire) confirmRetire(b.dataset.retire);
  if (b.dataset.dl) { const d = docById(b.dataset.dl); downloadDoc(d.name, passagesFor(d.id).map(p => p.loc + '\n' + p.text).join('\n\n')); }
});
function confirmRetire(id) {
  const d = docById(id), qs = qsFor(id).length;
  let dlg = $('retDlg');
  if (!dlg) { dlg = document.createElement('dialog'); dlg.id = 'retDlg'; dlg.className = 'dlg'; document.body.appendChild(dlg); }
  dlg.innerHTML = '<form method="dialog"><div class="dlg__b"><h3>Retire ' + esc(d.name) + '?</h3>' +
    '<p>Retire a document when it’s out of date. Its passages stop being used for new drafts and Ask lojo. It stays listed here, and you can restore it.</p>' +
    (qs ? '<div class="warn" style="background:rgba(217,154,43,.1);color:#7A5710">' + qs + ' question' + (qs === 1 ? '' : 's') + ' cite this document. Approved answers that rely on it are sent back to Build.</div>' : '') +
    '</div><div class="dlg__f"><button class="btn btn--secondary" value="cancel">Cancel</button><button class="btn btn--danger" type="button" id="retGo">Retire document</button></div></form>';
  dlg.showModal();
  $('retGo').onclick = () => { ST.retired[id] = true; save(); dlg.close(); open = null; render(); toast(d.name + ' retired'); };
}
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
function addFiles(list) {
  const errs = [], names = DOCS.map(d => d.name.toLowerCase()).concat((ST.docx || []).map(d => d.name.toLowerCase()), extra.map(x => x.name.toLowerCase()));
  const files = [...list].filter(f => {
    const ext = (f.name.split('.').pop() || '').toLowerCase();
    if (!OK_EXT.includes(ext)) { errs.push([f.name, 'This file type isn’t supported. Use PDF, DOCX, MD or TXT.']); return false; }
    if (f.size > MAX_MB * 1048576) { errs.push([f.name, 'Too large: ' + Math.round(f.size / 1048576) + ' MB. Each file can be up to 25 MB.']); return false; }
    if (names.includes(f.name.toLowerCase())) { errs.push([f.name, 'Already uploaded. Retire the old one first if this is a newer version.']); return false; }
    return true;
  });
  showUploadErrors(errs);
  files.forEach(f => {
    const item = { name: f.name, ext: (f.name.split('.').pop() || '').slice(0, 4), stage: 'Extracting text', done: false, pages: Math.max(1, Math.round(f.size / 40000)) };
    extra.unshift(item);
    setTimeout(() => { item.stage = 'Splitting into passages'; render(); }, 900);
    setTimeout(() => { item.stage = 'Indexing by meaning'; render(); }, 1800);
    setTimeout(() => { item.done = true; item.passages = Math.round(item.pages * 4.6); render(); toast(item.name + ' indexed'); }, 2800);
  });
  render();
}
$('fileInput').addEventListener('change', (e) => { addFiles(e.target.files); e.target.value = ''; });
const drop = $('drop');
['dragenter', 'dragover'].forEach(ev => drop.addEventListener(ev, (e) => { e.preventDefault(); drop.classList.add('is-over'); }));
['dragleave', 'drop'].forEach(ev => drop.addEventListener(ev, (e) => { e.preventDefault(); drop.classList.remove('is-over'); }));
drop.addEventListener('drop', (e) => addFiles(e.dataTransfer.files));
$('folderSend').addEventListener('click', () => {
  const v = $('folderLink').value.trim();
  if (!/^https?:\/\/\S+\.\S+/.test(v)) { $('folderLink').focus(); toast('Paste a full folder link'); return; }
  extra.unshift({ name: 'Shared folder · ' + v.replace(/^https?:\/\//, '').slice(0, 32) + '…', ext: 'dir', stage: 'Waiting for access', done: false });
  $('folderLink').value = ''; render(); show('docs');
  toast('We’ll pull the documents once ingest@lojo.ai has view access');
});
function show(tab) {
  document.querySelectorAll('.ptab').forEach(t => t.setAttribute('aria-selected', t.dataset.tab === tab));
  $('tabDocs').hidden = tab !== 'docs'; $('tabConnect').hidden = tab !== 'connect';
}
document.querySelectorAll('.ptab').forEach(t => t.addEventListener('click', () => { show(t.dataset.tab); history.replaceState(null, '', location.search + (t.dataset.tab === 'connect' ? '#connect' : '')); }));
const SP = new URLSearchParams(location.search), pinDoc = SP.get('doc'), pinLoc = SP.get('loc');
if (pinDoc && docById(pinDoc)) open = pinDoc;
renderScope();
render();
show(location.hash === '#connect' ? 'connect' : 'docs');
if (pinDoc && docById(pinDoc)) {
  const li = document.querySelector('tr.drow[data-id="' + pinDoc + '"]');
  if (li) { li.classList.add('is-pin'); li.scrollIntoView({ block: 'center' }); }
  if (pinLoc) document.querySelectorAll('tr.ddetail .passage').forEach(p => { if (p.querySelector('em').textContent === pinLoc) p.classList.add('is-hit'); });
}
if (new URLSearchParams(location.search).get('demo') === 'upload') demoUploadErrors();
""")


# ============================================================ QUESTIONS & GAPS
QUESTIONS_PAGE = dict(
  active='questions', title='Insights',
  css=r"""
  .icount{display:flex;align-items:baseline;gap:28px;flex-wrap:wrap;margin:4px 0 16px;color:var(--muted);font-size:1.02rem}
  .icount b{font-family:var(--display);font-weight:800;font-size:1.3rem;color:var(--ink);margin-right:6px}
  .icount .spacer{flex:1}
  .ifilters{display:flex;gap:10px;flex-wrap:wrap;align-items:center;margin-bottom:18px}
  .ifilters select.text{width:auto;min-width:0;height:42px;padding-right:28px;flex:0 1 auto}
  .isearch{flex:1 1 200px;min-width:180px;display:flex;align-items:center;gap:8px;height:42px;padding:0 13px;border-radius:11px;border:1px solid var(--line-2);background:var(--panel)}
  .isearch:focus-within{border-color:var(--rose);box-shadow:0 0 0 3px rgba(232,93,117,.16)}
  .isearch svg{width:17px;height:17px;fill:none;stroke:var(--muted);stroke-width:1.8;flex:none}
  .isearch input{border:0;outline:0;background:none;flex:1;font:inherit;font-size:.88rem;color:var(--ink)}
  .idate{display:flex;align-items:center;gap:8px;font-size:.82rem;color:var(--muted)}
  .idate .text{width:138px;height:42px;padding:0 10px}
  .ib{display:grid;grid-template-columns:380px minmax(0,1fr);gap:20px;align-items:start}
  .ilist{position:sticky;top:96px;max-height:calc(100vh - 120px);overflow:auto;padding:6px}
  .ilist ul{list-style:none;margin:0;padding:0}
  .iitem{display:grid;grid-template-columns:40px minmax(0,1fr);gap:4px 12px;padding:14px;border-radius:14px;cursor:pointer}
  .iitem:hover{background:var(--bg-soft)}
  .iitem.is-sel{background:var(--bg-soft);box-shadow:inset 3px 0 0 var(--rose)}
  .iitem + .iitem{margin-top:2px}
  .iico{width:40px;height:40px;border-radius:12px;display:grid;place-items:center;background:rgba(232,93,117,.08);color:#D7607A}
  .iico svg{width:19px;height:19px;fill:none;stroke:currentColor;stroke-width:1.7;stroke-linecap:round;stroke-linejoin:round}
  .iitem b{display:block;font-size:.9rem;font-weight:700;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
  .iitem .m{display:block;font-size:.78rem;color:var(--muted)}
  .iitem .ist{grid-column:2;justify-self:start;margin-top:8px}
  .ist{display:inline-flex;align-items:center;gap:6px;height:26px;padding:0 11px;border-radius:999px;border:1px solid var(--line-2);font-size:.64rem;font-weight:800;letter-spacing:.1em;text-transform:uppercase;color:var(--muted);white-space:nowrap}
  .ist.ok{border-color:rgba(63,143,95,.35);background:rgba(63,143,95,.08);color:var(--success)}
  .ist.done{border-color:rgba(62,111,166,.3);background:rgba(62,111,166,.07);color:var(--info)}
  .ist.run{border-color:rgba(232,93,117,.35);background:rgba(232,93,117,.06);color:#C7385B}
  .ist.run::before{content:"";width:10px;height:10px;border-radius:50%;border:2px solid currentColor;border-right-color:transparent;animation:spin .7s linear infinite}
  .ist.err{border-color:rgba(198,69,69,.35);background:rgba(198,69,69,.06);color:var(--error)}
  .ist.wait{border-color:rgba(217,154,43,.4);background:rgba(217,154,43,.08);color:#94660F}
  .idetail{display:grid;gap:14px}
  .ifail{display:flex;align-items:center;gap:14px;padding:16px 20px;border-radius:16px;border:1px solid rgba(198,69,69,.3);background:rgba(198,69,69,.06);color:var(--error);font-weight:600}
  .ifail svg{width:20px;height:20px;fill:none;stroke:currentColor;stroke-width:1.8;flex:none}
  .icard{background:var(--panel);border:1px solid var(--line);border-radius:20px;padding:26px 28px;box-shadow:0 16px 30px -28px rgba(36,26,20,.3)}
  .icard__top{display:flex;align-items:flex-start;gap:16px}
  .icard__top > div{flex:1;min-width:0}
  .icard .kind{font-size:.72rem;font-weight:800;letter-spacing:.14em;text-transform:uppercase;color:var(--rose);margin:0}
  .icard h2{font-family:var(--display);font-weight:700;font-size:1.9rem;letter-spacing:-.02em;margin:10px 0 6px;line-height:1.15;overflow-wrap:anywhere}
  .icard .when{color:var(--muted);font-size:1rem;margin:0}
  .iacts{display:flex;gap:10px;flex-wrap:wrap;margin:22px 0 4px}
  .iacts .btn{height:46px;padding:0 20px}
  .ifound{margin-top:20px;padding:16px 18px;border-radius:14px;background:rgba(62,111,166,.06);border:1px solid rgba(62,111,166,.18)}
  .ifound h3{margin:0 0 10px;font-size:.74rem;font-weight:800;letter-spacing:.12em;text-transform:uppercase;color:var(--info)}
  .ifound .chips{gap:6px}
  .itext{margin-top:22px;padding-top:18px;border-top:1px solid var(--line)}
  .itext summary{cursor:pointer;font-family:var(--display);font-weight:700;font-size:1.1rem;list-style-position:inside}
  .itext .body{margin-top:12px;font-size:.98rem;line-height:1.75;color:var(--ink);white-space:pre-line;display:-webkit-box;-webkit-line-clamp:6;-webkit-box-orient:vertical;overflow:hidden}
  .itext.is-full .body{display:block}
  .iempty{padding:22px;color:var(--muted);text-align:center;font-size:.9rem}
  @media (max-width:1100px){.ib{grid-template-columns:1fr}.ilist{position:static;max-height:420px}}
  .bar{display:flex;gap:12px;align-items:center;flex-wrap:wrap;margin-bottom:14px}
  .bar .spacer{flex:1}
  .add{display:flex;gap:8px;flex:1;max-width:520px}
  .qlist{list-style:none;margin:0;padding:0}
  .qrow{display:grid;grid-template-columns:minmax(0,1fr) auto auto;gap:18px;align-items:center;padding:16px 22px;border-top:1px solid var(--line)}
  .qact{display:flex;gap:14px;align-items:center;justify-content:flex-end;min-width:150px}
  .qact .link{border:0;background:none;padding:0;font:inherit;font-size:.84rem;font-weight:600;color:var(--ink);cursor:pointer;text-decoration:none;white-space:nowrap}
  .qact .link:hover{color:#B73C54;text-decoration:underline;text-underline-offset:3px}
  .qact .link.mute{color:var(--muted)}
  .srclink{display:inline-flex;align-items:center;gap:6px;height:26px;padding:0 9px;border-radius:8px;border:1px solid var(--line-2);background:var(--panel);font-size:.76rem;font-weight:600;color:var(--ink);text-decoration:none;white-space:nowrap;transition:border-color .15s ease,box-shadow .15s ease}
  .srclink svg{width:13px;height:13px;fill:none;stroke:var(--muted);stroke-width:1.9}
  .srclink em{font-style:normal;color:var(--muted);font-weight:500}
  .srclink .go{color:var(--muted);font-size:.72rem;opacity:0;transition:opacity .15s ease}
  .srclink:hover{border-color:var(--rose);box-shadow:0 6px 14px -10px rgba(232,93,117,.8);text-decoration:none}
  .srclink:hover .go{opacity:1;color:#B73C54}
  .gwhy{display:block;margin:-2px 0 8px;color:var(--muted);font-size:.84rem}
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
        <p>Everything your sources send in: documents, pages, email and calls. Analyze each one to find the questions it answers and the gaps it leaves.</p>
      </div>
    </div>
    <div class="ptabs" role="tablist" aria-label="Insights">
      <button class="ptab" role="tab" data-tab="q" aria-selected="true"><svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/><path d="M9.5 9.5a2.5 2.5 0 1 1 3.5 2.3c-.6.3-1 .8-1 1.5V14M12 17h.01"/></svg>Questions <span class="n" id="nQ">0</span></button>
      <button class="ptab" role="tab" data-tab="g" aria-selected="false"><svg viewBox="0 0 24 24"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></svg>Gaps <span class="n" id="nG">0</span></button>
      <button class="ptab" role="tab" data-tab="in" aria-selected="false"><svg viewBox="0 0 24 24"><path d="M22 12h-6l-2 3h-4l-2-3H2"/><path d="M5.5 5.1 2 12v6a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2v-6l-3.5-6.9A2 2 0 0 0 16.8 4H7.2a2 2 0 0 0-1.7 1.1z"/></svg>Inbox <span class="n" id="nIn">0</span></button>
    </div>

    <section id="tabIn" hidden>
      <div class="icount">
        <span><b id="cRec">0</b> received</span><span><b id="cReady">0</b> ready to analyze</span><span><b id="cDone">0</b> analyzed</span>
        <span class="spacer"></span>
        <button class="btn btn--secondary btn--sm" id="analyzeAll" type="button">Analyze all ready</button>
      </div>
      <div class="ifilters">
        <label class="isearch"><svg viewBox="0 0 24 24"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></svg><input id="fQ" placeholder="Search participants or subjects" aria-label="Search"></label>
        <select class="text" id="fCh" aria-label="Channel"></select>
        <select class="text" id="fInt" aria-label="Integration"></select>
        <select class="text" id="fSt" aria-label="Status"></select>
        <label class="idate">From <input class="text" type="date" id="fFrom"></label>
        <label class="idate">To <input class="text" type="date" id="fTo"></label>
      </div>
      <div class="ib">
        <section class="card ilist" aria-label="Received"><ul id="iList"></ul></section>
        <section class="idetail" id="iDetail" aria-live="polite"></section>
      </div>
    </section>

    <section id="tabQ">
      <div class="bar">
        <div class="chips" id="filters">
          <button class="chip" data-f="all" aria-pressed="true">All</button>
          <button class="chip" data-f="need" aria-pressed="false">Needs you</button>
          <button class="chip" data-f="you" aria-pressed="false">From you</button>
          <button class="chip" data-f="no" aria-pressed="false">Left out</button>
        </div>
      </div>
      <section class="card"><ul class="qlist" id="qlist"></ul></section>
    </section>

    <section id="tabG" hidden>
      <section class="card"><ul class="qlist" id="gapList"></ul></section>
    </section>

""",
  js=r"""
let filter = 'all';
const ORIGIN = { chat: ['From Ask lojo', 'badge--info'], found: ['Found in documents', 'badge--muted'], faq: ['From your help pages', 'badge--info'], you: ['From you', 'badge--rose'], gap: ['From a gap', 'badge--amber'] };
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
// a source chip opens Sources at that document with the quoted passage highlighted
function srcLink(docId, loc) {
  return '<a class="srclink" href="sources.html?doc=' + docId + (loc ? '&loc=' + encodeURIComponent(loc) : '') + '" title="Open the source">' +
    '<svg viewBox="0 0 24 24"><path d="M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8z"/><path d="M14 3v5h5"/></svg>' + esc(docShort(docId)) + (loc ? ' <em>' + esc(loc) + '</em>' : '') + '<span class="go">↗</span></a>';
}
function sourcesOf(q) {
  const r = draftByQ(q.id);
  return (q.docs || []).map(d => { const hit = r && r.src.find(s => s[0] === d); return [d, hit ? hit[1] : '']; });
}
const needsYou = (q) => { const s = statusOf(q)[0]; return matters(q) === null || s === 'Draft failed' || s === 'No source yet' || s === 'Needs a human answer'; };
function actionFor(q) {
  const m = matters(q), [st] = statusOf(q), r = draftByQ(q.id), failed = ST.draftFailed[q.id];
  if (m === false) return '<button class="link" data-q="' + q.id + '" data-v="1">Bring back</button>';
  if (failed === 'retrying') return '';
  if (failed) return '<button class="btn btn--secondary btn--sm" data-retry="' + q.id + '">Try again</button>';
  if (st === 'Approved') return '<a class="link" href="build.html?sel=' + r.id + '">See the answer</a>';
  if (st === 'Needs a human answer') return '<a class="link" href="build.html?sel=' + r.id + '">Write the answer</a>';
  if (st === 'Draft in review') return '<a class="link" href="build.html?sel=' + r.id + '">Review the draft</a>';
  if (st === 'No source yet') return '<a class="link" href="sources.html">Send a document</a>';
  if (m === null) return '<span class="seg" role="group" aria-label="Does this matter?"><button class="yes" data-q="' + q.id + '" data-v="1">Matters</button><button class="no" data-q="' + q.id + '" data-v="0">Leave out</button></span>';
  return '<button class="link mute" data-q="' + q.id + '" data-v="0">Leave out</button>';
}
function renderQ() {
  const qs = allQuestions().filter(q => filter === 'all' || (filter === 'need' && needsYou(q) && matters(q) !== false) || (filter === 'no' && matters(q) === false) || (filter === 'you' && q.origin === 'you'));
  $('qlist').innerHTML = qs.length ? qs.map(q => {
    const m = matters(q), [st, cls] = statusOf(q), [ol, oc] = ORIGIN[q.origin];
    const asks = ST.asks[q.id] || 0, failed = ST.draftFailed[q.id];
    return '<li class="qrow' + (m === false ? ' is-out' : '') + (m === null ? ' is-call' : '') + (flashId === q.id ? ' is-flash' : '') + '" id="row-' + q.id + '"><div><b>' + esc(q.q) + '</b><div class="qmeta"><span class="badge ' + oc + '">' + ol + '</span>' +
      (asks >= 2 ? '<span class="badge badge--amber" title="Asked in Ask lojo or added by your team">Asked ' + asks + ' times</span>' : '') +
      sourcesOf(q).map(([d, loc]) => srcLink(d, loc)).join('') + '</div>' +
      (m === false && ST.notes[q.id] ? '<span class="note">' + esc(ST.notes[q.id]) + '</span>' : '') +
      (failed && failed !== 'retrying' && m !== false ? '<span class="failnote">' + esc(failed) + '</span>' : '') + '</div>' +
      '<span class="status ' + cls + '">' + (failed === 'retrying' ? '<span class="spin" style="width:10px;height:10px"></span> ' : '') + st + '</span>' +
      '<span class="qact">' + actionFor(q) + '</span>' +
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

function renderG() {
  $('gapList').innerHTML = GAPS.map(g => {
    const done = ST.gaps[g.id];
    return '<li class="qrow' + (done ? ' is-out' : '') + '"><div><b>' + esc(g.term) + '</b><span class="gwhy">' + esc(g.why) + '</span><div class="qmeta"><span class="badge badge--amber">Referred to, never explained</span>' +
      g.where.map(([d, loc]) => srcLink(d, loc)).join('') + '</div></div>' +
      '<span class="status ' + (done === 'question' ? 'st-q' : done ? 'st-mute' : 'st-rev') + '">' + (done === 'question' ? 'Added as a question' : done ? 'Not needed' : 'Needs a source') + '</span>' +
      '<span class="qact">' + (done ? '<button class="link mute" data-undo="' + g.id + '">Undo</button>' :
        '<a class="link" href="sources.html">Send a document</a><button class="link" data-ask="' + g.id + '">Add as a question</button><button class="link mute" data-skip="' + g.id + '">Not needed</button>') + '</span></li>';
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

// ---------- Inbox: everything sources send in, analyzed into questions and gaps
// Channels and integrations are data. A new connector is one entry in INTEGRATIONS (and a channel, if it brings a new kind of item).
const SVG = (d) => '<svg viewBox="0 0 24 24">' + d + '</svg>';
const CHANNELS = {
  doc: { one: 'Document', many: 'Documents', body: 'Text', none: 'No text found', ic: SVG('<path d="M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8z"/><path d="M14 3v5h5M9 13h6M9 17h4"/>') },
  page: { one: 'Web page', many: 'Web pages', body: 'Page text', none: 'No text found', ic: SVG('<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c2.5 2.6 3.8 5.6 3.8 9s-1.3 6.4-3.8 9c-2.5-2.6-3.8-5.6-3.8-9S9.5 5.6 12 3z"/>') },
  email: { one: 'Email', many: 'Email', body: 'Message', none: 'Empty message', ic: SVG('<rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/>') },
  call: { one: 'Call', many: 'Calls', body: 'Transcript', none: 'No transcript available', ic: SVG('<path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1.9.4 1.8.7 2.7a2 2 0 0 1-.5 2.1L8 9.8a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.7.7a2 2 0 0 1 1.7 2z"/>') },
};
const INTEGRATIONS = {
  upload: { name: 'Upload', ch: 'doc' }, notion: { name: 'Notion', ch: 'doc' }, website: { name: 'Website', ch: 'page' },
  gmail: { name: 'Gmail inbox', ch: 'email' }, aircall: { name: 'Aircall', ch: 'call' },
};
const STATUS = {
  ready: ['Ready', 'ok'], analyzing: ['Analyzing', 'run'], analyzed: ['Analyzed', 'done'], attention: ['Needs attention', 'err'],
  awaiting: ['Awaiting transcript', 'wait'], none: ['No transcript available', ''],
};
const T = (d, h, m, mo = 9) => new Date(2026, mo, d, h, m).toISOString();
const INBOX = DOCS.map((d, i) => ({ id: 'i' + d.id, int: 'upload', title: d.name, at: T(9 + (i > 5 ? 1 : 0), 10 + i % 6, 12 * i % 60, 8), len: d.pages + ' pages', status: 'analyzed', doc: d.id }))
  .concat([
    { id: 'n1', int: 'notion', title: 'Pricing wiki', at: T(5, 16, 40), len: '6 pages', status: 'analyzed', text: 'Starter: 3 seats and 1,000 transactions a month. Growth: 15 seats, SAML SSO included. Scale: unlimited seats, a named onboarding manager.', found: ['q1', 'q3'] },
    { id: 'n2', int: 'notion', title: 'Onboarding playbook', at: T(6, 9, 5), len: '11 pages', status: 'ready', text: 'Week 1: kickoff call and admin set-up. Week 2: import customers and connect your bank. Scale customers get two admin training sessions and a named onboarding manager.' },
    { id: 'w1', int: 'website', title: 'oslo.com/pricing', at: T(5, 8, 2), len: '1 page', status: 'analyzed', text: 'Compare plans. Starter from €29 a month. Growth from €99 a month, includes SAML single sign-on. Scale: talk to sales.', found: ['q1'] },
    { id: 'w2', int: 'website', title: 'help.oslo.com/sso', at: T(6, 7, 48), len: '1 page', status: 'ready', text: 'Single sign-on (SSO). SSO is an Enterprise-only feature. Contact sales to enable it.' },
    { id: 'w3', int: 'website', title: 'oslo.com/legal/refunds', at: T(6, 13, 2), len: '1 page', status: 'analyzing', text: 'Refunds. You can cancel within 30 days for a full refund. After that, refunds are prorated to the unused months.' },
    { id: 'e1', int: 'gmail', title: 'SSO stopped working after we upgraded', who: 'Marta Ruiz · Brightline', at: T(6, 11, 30), len: '4 messages', status: 'attention', text: 'Hi, we moved to Growth yesterday and SSO now shows “not available on your plan”. Our help page says it is Enterprise only, but sales told us Growth includes it. Can you confirm?' },
    { id: 'e2', int: 'gmail', title: 'Invoice for our annual plan', who: 'Lea Martin · Kontor', at: T(6, 10, 14), len: '2 messages', status: 'ready', text: 'Can we pay the annual Growth plan by invoice instead of card? Our finance team needs a PO number on it.' },
    { id: 'e3', int: 'gmail', title: 'Apple Pay in Germany?', who: 'Jonas Weber', at: T(5, 15, 2), len: '1 message', status: 'analyzed', text: 'Do you support Apple Pay for customers in Germany? We could not find it in your docs.', found: ['q16'], gaps: 1 },
    { id: 'c1', int: 'aircall', title: '+33 6 85 36 57 11', at: T(6, 13, 22), len: '7 min', status: 'ready', text: 'Hello, yes, good afternoon. I called last week but didn’t get time to call back. I wanted to ask again about the chargeback fee: your billing FAQ says there is one but not how much. We had two disputes this month and need to know what we will be charged, and whether late evidence can still be added once the bank has started its review.' },
    { id: 'c2', int: 'aircall', title: '+33 7 57 91 26 97', at: T(5, 18, 45), len: '0 min', status: 'none' },
    { id: 'c3', int: 'aircall', title: '+33 7 57 91 26 97', at: T(5, 18, 44), len: '0 min', status: 'none' },
    { id: 'c4', int: 'aircall', title: '+44 20 7946 0958', at: T(6, 13, 50), len: '12 min', status: 'awaiting' },
    { id: 'c5', int: 'aircall', title: '+49 30 901820', at: T(4, 11, 5), len: '9 min', status: 'analyzed', text: 'We are on Starter and want to know if we can move to Scale mid-cycle, and how the invoice handles the change.', found: ['q5'] },
  ]).sort((a, b) => b.at.localeCompare(a.at));
ST.inbox = ST.inbox || {};
const stOf = (it) => (ST.inbox[it.id] || {}).status || it.status;
const foundOf = (it) => (ST.inbox[it.id] || {}).found || it.found || (it.doc ? qsForDoc(it.doc) : []);
const chOf = (it) => INTEGRATIONS[it.int].ch;
const qsForDoc = (id) => allQuestions().filter(q => (q.docs || []).includes(id)).map(q => q.id);
const textOf = (it) => it.text || (it.doc ? passagesOf(it.doc) : '');
function passagesOf(id) {
  const out = [];
  DRAFTS.forEach(r => r.src.forEach(([d, loc, text]) => { if (d === id && !out.includes(text)) out.push(text); }));
  GAPS.forEach(g => g.where.forEach(([d, loc, text]) => { if (d === id && !out.includes(text)) out.push(text); }));
  return out.join('\n\n') || 'Indexed by meaning. Open Sources to see its passages.';
}
const when = (iso) => new Date(iso).toLocaleString('en-US', { month: 'short', day: 'numeric', year: 'numeric', hour: 'numeric', minute: '2-digit' });
const stLabel = (it) => { const s = stOf(it); return s === 'none' ? CHANNELS[chOf(it)].none : STATUS[s][0]; };
const pill = (it) => '<span class="ist ' + STATUS[stOf(it)][1] + '">' + esc(stLabel(it)) + '</span>';
let sel = null, fullText = false;
function fillFilters() {
  $('fCh').innerHTML = '<option value="">All channels</option>' + Object.entries(CHANNELS).map(([k, c]) => '<option value="' + k + '">' + c.many + '</option>').join('');
  $('fSt').innerHTML = '<option value="">All statuses</option>' + Object.entries(STATUS).map(([k, s]) => '<option value="' + k + '">' + (k === 'none' ? 'No transcript or text' : s[0]) + '</option>').join('');
  fillInt();
}
function fillInt() {
  const ch = $('fCh').value, keep = $('fInt').value;
  $('fInt').innerHTML = '<option value="">All integrations</option>' + Object.entries(INTEGRATIONS).filter(([, v]) => !ch || v.ch === ch).map(([k, v]) => '<option value="' + k + '">' + v.name + '</option>').join('');
  if ([...$('fInt').options].some(o => o.value === keep)) $('fInt').value = keep;
}
function visible() {
  const q = $('fQ').value.trim().toLowerCase(), ch = $('fCh').value, it = $('fInt').value, st = $('fSt').value, from = $('fFrom').value, to = $('fTo').value;
  return INBOX.filter(x => (!q || (x.title + ' ' + (x.who || '')).toLowerCase().includes(q)) && (!ch || chOf(x) === ch) && (!it || x.int === it) && (!st || stOf(x) === st) &&
    (!from || x.at.slice(0, 10) >= from) && (!to || x.at.slice(0, 10) <= to));
}
function renderIn() {
  $('cRec').textContent = INBOX.length.toLocaleString('en-GB');
  const ready = INBOX.filter(x => stOf(x) === 'ready').length;
  $('cReady').textContent = ready; $('cDone').textContent = INBOX.filter(x => stOf(x) === 'analyzed').length;
  $('nIn').textContent = ready; $('analyzeAll').disabled = !ready; $('analyzeAll').textContent = 'Analyze all ready (' + ready + ')';
  const list = visible();
  if (!list.some(x => x.id === sel)) sel = list.length ? list[0].id : null;
  $('iList').innerHTML = list.length ? list.map(x => { const ch = CHANNELS[chOf(x)];
    return '<li class="iitem' + (x.id === sel ? ' is-sel' : '') + '" data-id="' + x.id + '"><span class="iico">' + ch.ic + '</span><span style="min-width:0"><b>' + esc(x.title) + '</b>' +
      '<span class="m">' + ch.one + ' · ' + INTEGRATIONS[x.int].name + (x.who ? ' · ' + esc(x.who) : '') + '</span><span class="m">' + when(x.at) + ' · ' + x.len + '</span></span>' + pill(x) + '</li>'; }).join('')
    : '<li class="iempty">Nothing matches these filters.</li>';
  renderDetail();
}
function renderDetail() {
  const x = INBOX.find(i => i.id === sel);
  if (!x) { $('iDetail').innerHTML = '<div class="icard iempty">Pick something on the left to see it here.</div>'; return; }
  const ch = CHANNELS[chOf(x)], s = stOf(x), txt = textOf(x), f = foundOf(x);
  let h = '';
  if (s === 'attention') h += '<div class="ifail"><svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/><path d="M12 8v5M12 16h.01"/></svg>Request failed (502) · we couldn’t analyze this ' + ch.one.toLowerCase() + '<button class="btn btn--secondary btn--sm" data-act="analyze" style="margin-left:auto">Try again</button></div>';
  h += '<article class="icard"><div class="icard__top"><div><p class="kind">' + ch.one + ' · ' + INTEGRATIONS[x.int].name + '</p><h2>' + esc(x.title) + '</h2>' +
    '<p class="when">' + (x.who ? esc(x.who) + ' · ' : '') + when(x.at) + ' · ' + x.len + '</p></div>' + pill(x) + '</div>';
  const acts = [];
  if (s === 'ready') acts.push('<button class="btn btn--grad" data-act="analyze">→ Analyze ' + ch.one.toLowerCase() + '</button>');
  if (s === 'analyzed') acts.push('<button class="btn btn--secondary" data-act="analyze">Analyze again</button>');
  if (s === 'awaiting') acts.push('<button class="btn btn--secondary" disabled>Waiting for the transcript from ' + INTEGRATIONS[x.int].name + '</button>');
  if (x.doc) acts.push('<button class="btn btn--secondary" data-act="dl">' + DL_ICON.replace('<svg', '<svg style="width:16px;height:16px;fill:none;stroke:currentColor;stroke-width:1.9"') + ' Download</button>');
  if (txt) acts.push('<button class="btn btn--secondary" data-act="full">' + (fullText ? 'Show less' : 'Open full ' + ch.body.toLowerCase()) + '</button>');
  if (acts.length) h += '<div class="iacts">' + acts.join('') + '</div>';
  if (s === 'analyzed') {
    const qs = f.map(id => allQuestions().find(q => q.id === id)).filter(Boolean);
    h += '<div class="ifound"><h3>Found here · ' + qs.length + ' question' + (qs.length === 1 ? '' : 's') + (x.gaps ? ' · ' + x.gaps + ' gap' : '') + '</h3>' +
      (qs.length ? '<div class="chips">' + qs.map(q => '<button class="chip" data-q="' + q.id + '">' + esc(q.q) + '</button>').join('') + '</div>' : '<p class="sub">No new questions in this one.</p>') + '</div>';
  }
  if (s === 'none') h += '<p class="sub" style="margin-top:18px">' + (x.len === '0 min' ? 'The call was too short to transcribe.' : 'There was no text to read.') + ' Nothing to analyze.</p>';
  if (txt) h += '<details class="itext' + (fullText ? ' is-full' : '') + '" open><summary>' + ch.body + '</summary><div class="body">' + esc(txt) + '</div></details>';
  $('iDetail').innerHTML = h + '</article>';
}
// analyzing takes a moment; then the item lists what it found
function analyze(ids) {
  ids.forEach(id => { ST.inbox[id] = { status: 'analyzing' }; });
  save(); renderIn();
  setTimeout(() => {
    ids.forEach(id => { const x = INBOX.find(i => i.id === id); ST.inbox[id] = { status: 'analyzed', found: x.found || pick(x) }; });
    save(); renderIn(); renderQ();
    toast(ids.length === 1 ? 'Analyzed. Its questions are in Questions.' : ids.length + ' analyzed. New questions are in Questions.');
  }, 1600);
}
const pick = (x) => { const words = (textOf(x) + ' ' + x.title).toLowerCase(); return allQuestions().filter(q => q.q.toLowerCase().split(/\W+/).filter(w => w.length > 4).some(w => words.includes(w))).slice(0, 3).map(q => q.id); };
$('iList').addEventListener('click', (e) => { const li = e.target.closest('[data-id]'); if (!li) return; sel = li.dataset.id; fullText = false; renderIn(); });
$('iDetail').addEventListener('click', (e) => {
  const b = e.target.closest('[data-act]');
  if (b && b.dataset.act === 'analyze') analyze([sel]);
  if (b && b.dataset.act === 'full') { fullText = !fullText; renderDetail(); }
  if (b && b.dataset.act === 'dl') { const x = INBOX.find(i => i.id === sel); downloadDoc(x.title, textOf(x)); }
  const c = e.target.closest('[data-q]');
  if (c) { show('q'); filter = 'all'; document.querySelectorAll('#filters .chip').forEach(x => x.setAttribute('aria-pressed', x.dataset.f === 'all')); flashId = c.dataset.q; renderQ(); const r = $('row-' + c.dataset.q); if (r) r.scrollIntoView({ block: 'center', behavior: 'smooth' }); }
});
['fQ', 'fSt', 'fInt', 'fFrom', 'fTo'].forEach(id => $(id).addEventListener('input', renderIn));
$('fCh').addEventListener('input', () => { fillInt(); renderIn(); });
$('analyzeAll').addEventListener('click', () => analyze(INBOX.filter(x => stOf(x) === 'ready').map(x => x.id)));
// the page being analyzed finishes while you watch
INBOX.filter(x => stOf(x) === 'analyzing').forEach(x => setTimeout(() => { ST.inbox[x.id] = { status: 'analyzed', found: x.found || pick(x) }; renderIn(); }, 3500));

function show(tab) {
  document.querySelectorAll('.ptab').forEach(t => t.setAttribute('aria-selected', t.dataset.tab === tab));
  $('tabIn').hidden = tab !== 'in'; $('tabQ').hidden = tab !== 'q'; $('tabG').hidden = tab !== 'g';
}
document.querySelectorAll('.ptab').forEach(t => t.addEventListener('click', () => { show(t.dataset.tab); history.replaceState(null, '', location.search + ({ g: '#gaps', in: '#inbox' }[t.dataset.tab] || '')); }));
const QD = new URLSearchParams(location.search).get('demo');
fillFilters(); renderIn(); renderQ(); renderG();
show({ '#gaps': 'g', '#inbox': 'in' }[location.hash] || 'q');
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
  .assist{display:flex;gap:8px;flex-wrap:wrap;align-items:center;margin-top:10px}
  .assist .spacer{flex:1}
  .abtn{display:inline-flex;align-items:center;gap:7px;height:34px;padding:0 13px;border-radius:999px;border:1px solid var(--line-2);background:var(--panel);font:inherit;font-size:.8rem;font-weight:600;color:var(--ink);cursor:pointer}
  .abtn:hover{border-color:rgba(36,26,20,.3);background:var(--bg-soft)}
  .abtn svg{width:15px;height:15px;fill:none;stroke:currentColor;stroke-width:1.9;stroke-linecap:round;stroke-linejoin:round}
  .abtn.ai{border-color:transparent;background:linear-gradient(var(--panel),var(--panel)) padding-box,var(--brand-gradient) border-box;border:1.5px solid transparent;color:#B73C54}
  .abtn.ai:hover{background:linear-gradient(#FFF5F2,#FFF5F2) padding-box,var(--brand-gradient) border-box}
  .abtn[disabled]{opacity:.7;cursor:progress}
  .alink{display:flex;gap:8px;margin-top:10px}
  .arefs{display:flex;gap:8px;flex-wrap:wrap;margin-top:10px}
  .aref{display:inline-flex;align-items:center;gap:7px;height:30px;padding:0 6px 0 11px;border-radius:9px;border:1px solid var(--line-2);background:var(--bg-soft);font-size:.78rem;font-weight:600}
  .aref svg{width:14px;height:14px;fill:none;stroke:var(--muted);stroke-width:1.9}
  .aref button{border:0;background:none;color:var(--muted);cursor:pointer;width:22px;height:22px;border-radius:6px;font-size:.95rem}
  .aref button:hover{background:var(--panel);color:var(--ink)}
  @media (max-width:1000px){.rv{grid-template-columns:1fr}.list{position:static;max-height:none}}
""",
  body=r"""
    <div class="head">
      <div>
        <p class="label">03 Build · Validation</p>
        <h1>Build</h1>
        <p>Approve, edit, or reject with a reason. A rejected draft is written again up to twice; if it’s still wrong, it waits for a human answer.</p>
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
let tab = 'pending', sel = null, mode = 'view', linking = false, refs = [];
const AIC = {
  doc: '<svg viewBox="0 0 24 24"><path d="m21 12-8.6 8.6a6 6 0 0 1-8.5-8.5l8.6-8.6a4 4 0 0 1 5.7 5.7l-8.6 8.6a2 2 0 0 1-2.8-2.8l7.9-7.9"/></svg>',
  link: '<svg viewBox="0 0 24 24"><path d="M10 13a5 5 0 0 0 7.5.5l3-3a5 5 0 0 0-7-7l-1.7 1.7"/><path d="M14 11a5 5 0 0 0-7.5-.5l-3 3a5 5 0 0 0 7 7l1.7-1.7"/></svg>',
  ai: '<svg viewBox="0 0 24 24"><path d="M12 3l1.8 4.7L18.5 9.5l-4.7 1.8L12 16l-1.8-4.7L5.5 9.5l4.7-1.8z"/><path d="M19 15l.8 2.2L22 18l-2.2.8L19 21l-.8-2.2L16 18l2.2-.8z"/></svg>',
};
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
  'd6|p. 1': ['Welcome to Oslo. Here is what happens in your first month. ', ' Growth customers get a 30-minute kickoff and our onboarding guides.'],
  'd9|§1': ['§1 Paying for Oslo. ', ' Prices are shown in euros and charged in your local currency.'],
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
  if (!r) { $('detail').innerHTML = '<div class="empty"><b>Nothing to review. The loop is running.</b>Approved answers are in the store; try them in Ask lojot.</div>'; return; }
  const d = decision(r), ans = answerOf(r);
  let h = '<div class="meta" style="display:flex;gap:6px;flex-wrap:wrap">' + badges(r) + '</div><h2>' + esc(Q(r)) + '</h2>';
  const other = ST.others && ST.others[r.id];
  // G10: someone else decided this draft while it was open here
  if (other && d.status === 'pending') h += '<div class="other"><span class="av">' + esc(other.by.split(' ').map(x => x[0]).join('')) + '</span><div><b>' + esc(other.by) + ' ' + esc(other.action) + ' this ' + esc(other.when) + '.</b>' +
    'Your screen was out of date, so nothing you do here will change it. Their decision stands.<div class="btns"><button class="btn btn--primary btn--sm" data-a="ackOther">Got it, next draft</button><button class="btn btn--ghost btn--sm" data-a="seeOther">See their version</button></div></div></div>';
  if (d.status === 'approved') h += '<div class="done-note ok">✓ Approved' + (d.by ? ' by ' + esc(d.by) : '') + (d.at ? ' · ' + esc(d.at) : '') + '. It’s in the store and Ask lojo can use it.</div>';
  if (d.status === 'final') h += '<div class="done-note no">Rejected three times (' + esc(d.reason) + '). Nothing lojo wrote was right, so write the answer yourself, or leave it out.</div>';
  if (d.status === 'redrafting') {
    h += '<div class="answer" style="display:flex;gap:10px;align-items:center;color:var(--muted)"><span class="spin"></span>Writing it again with your reason: “' + esc(d.reason) + '”</div>';
  } else if (mode === 'edit') {
    // writing an answer: start from a document, a link, or an AI draft from what you attach and what's approved
    h += '<p class="seclbl">Your answer</p><textarea class="text" id="editBox" style="min-height:140px" placeholder="Write the answer as you would give it. Markdown works.">' + (d.status === 'final' ? esc(d.answer || '') : esc(ans)) + '</textarea>' +
      '<div class="assist"><label class="abtn"><input type="file" id="attFile" hidden accept=".pdf,.docx,.doc,.md,.txt">' + AIC.doc + 'Attach document</label>' +
      '<button class="abtn" type="button" data-a="link">' + AIC.link + 'Add link</button><button class="abtn ai" type="button" data-a="ai">' + AIC.ai + 'Draft with AI</button>' +
      '<span class="spacer"></span><span class="sub">Attachments are kept as this answer’s sources.</span></div>' +
      (linking ? '<div class="alink"><input class="text" id="linkIn" placeholder="https://help.oslo.com/…" aria-label="Link"><button class="btn btn--secondary btn--sm" type="button" data-a="addlink">Add</button><button class="btn btn--ghost btn--sm" type="button" data-a="nolink">Cancel</button></div>' : '') +
      (refs.length ? '<div class="arefs">' + refs.map((x, i) => '<span class="aref">' + (x.kind === 'link' ? AIC.link : AIC.doc) + esc(x.name) + '<button type="button" data-rm="' + i + '" aria-label="Remove">×</button></span>').join('') + '</div>' : '') +
      '<div style="height:22px"></div>';
  } else {
    h += '<p class="seclbl">' + (d.redrafted === 2 ? 'Third draft' : d.redrafted ? 'Rewritten draft' : 'Draft answer') + '</p><div class="answer">' + md(ans) + '</div>';
  }
  // G14: a draft rewritten more than once keeps its history
  if (d.history && d.history.length) h += '<details class="hist"><summary>Earlier drafts (' + d.history.length + ')</summary><ol>' + d.history.map(x => '<li>' + esc(x.text) + '<span>Rejected · ' + esc(x.reason) + '</span></li>').join('') + '</ol></details>';
  else if (d.redrafted && d.prev) h += '<p class="prev"><b>First draft, rejected</b> (' + esc(d.reason) + '): ' + esc(d.prev) + '</p>';
  if (d.refs && d.refs.length && mode !== 'edit') h += '<p class="seclbl">Sources you added</p><div class="arefs" style="margin-bottom:22px">' + d.refs.map(x => '<span class="aref">' + (x.kind === 'link' ? AIC.link : AIC.doc) + esc(x.name) + '</span>').join('') + '</div>';
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
  else if (mode === 'edit' && d.status === 'final') acts = '<button class="btn btn--primary" data-a="save">Save &amp; approve</button><button class="btn btn--ghost" data-a="leave">Leave out</button><span class="spacer"></span><span class="sub">Your answer is approved as soon as you save it.</span>';
  else if (mode === 'edit') acts = '<button class="btn btn--primary" data-a="save">' + (d.status === 'approved' ? 'Save changes' : 'Save &amp; approve') + '</button><button class="btn btn--ghost" data-a="cancel">Cancel</button>';
  else if (mode === 'reject') acts = '<button class="btn btn--danger" data-a="confirm">' + (d.redrafted === 2 ? 'Reject' : 'Reject &amp; rewrite') + '</button><button class="btn btn--ghost" data-a="cancel">Cancel</button>';
  else if (d.status === 'pending' && ST.others && ST.others[r.id]) acts = '';
  else if (d.status === 'pending') acts = '<button class="btn btn--primary" data-a="approve">Approve <kbd>A</kbd></button><button class="btn btn--secondary" data-a="edit">Edit &amp; approve <kbd>E</kbd></button><button class="btn btn--danger" data-a="reject">Reject <kbd>R</kbd></button><span class="spacer"></span><span class="sub"><kbd>J</kbd> <kbd>K</kbd> to move</span>';
  else if (d.status === 'final') acts = '<button class="btn btn--primary" data-a="edit">Write the answer</button><button class="btn btn--ghost" data-a="undo">Back to review</button>';
  else acts = '<button class="btn btn--primary" data-a="edit">Edit answer</button><button class="btn btn--ghost" data-a="undo">Undo approval</button><span class="spacer"></span><span class="sub">Edits go live in Ask lojo as soon as you save.</span>';
  if (acts) h += '<div class="acts">' + acts + '</div>';
  $('detail').innerHTML = h;
  if (mode === 'edit') { const t = $('editBox'); if (typed !== null) { t.value = typed; typed = null; } t.focus(); t.setSelectionRange(t.value.length, t.value.length); }
}
function render() { renderList(); renderDetail(); }
// keep what's typed when the editor re-renders
let typed = null;
function keepText() { const t = $('editBox'); if (t) typed = t.value; }
// AI drafts from the attachments and the approved answers; you check it before saving
function draftWithAI(r) {
  keepText();
  const box = $('editBox'), btn = document.querySelector('[data-a="ai"]');
  btn.disabled = true; btn.innerHTML = '<span class="spin" style="width:12px;height:12px"></span> Drafting…';
  setTimeout(() => {
    const from = refs.length ? refs.map(x => x.name).join(', ') : 'your approved answers';
    const q = Q(r).replace(/\?$/, '');
    typed = (typed && typed.trim() ? typed.trim() + '\n\n' : '') + 'Based on ' + from + ': ' + (r.redraft || r.draft);
    renderDetail(); toast('Drafted. Edit it before you save.');
  }, 1300);
}
$('detail').addEventListener('change', (e) => {
  if (e.target.id !== 'attFile' || !e.target.files.length) return;
  keepText(); [...e.target.files].forEach(f => refs.push({ kind: 'doc', name: f.name })); renderDetail(); toast('Attached. It’s kept as this answer’s source.');
});
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
  if (a === 'edit') { mode = 'edit'; refs = (d.refs || []).slice(); linking = false; }
  if (a === 'link') { linking = true; keepText(); renderDetail(); $('linkIn').focus(); return; }
  if (a === 'nolink') { linking = false; keepText(); renderDetail(); return; }
  if (a === 'addlink') { const v = $('linkIn').value.trim(); if (!/^https?:\/\/\S+\.\S+/.test(v)) { $('linkIn').focus(); toast('Paste a full link'); return; } refs.push({ kind: 'link', name: v.replace(/^https?:\/\//, '') }); linking = false; keepText(); renderDetail(); return; }
  if (a === 'ai') { draftWithAI(r); return; }
  if (a === 'leave') { d.status = 'left'; mode = 'view'; save(); toast('Left out. It won’t be answered.'); next(); render(); return; }
  if (a === 'reject') mode = 'reject';
  if (a === 'cancel') mode = 'view';
  if (a === 'undo') { d.status = 'pending'; mode = 'view'; save(); }
  if (a === 'save') {
    const v = $('editBox').value.trim(); if (!v) return;
    d.edited = v !== answerOf(r) || d.edited; d.answer = v; d.status = 'approved'; d.at = today; d.refs = refs.slice(); mode = 'view';
    toast('Edited and approved'); save(); next();
  }
  if (a === 'confirm') {
    const reason = $('why').value + ($('note').value.trim() ? ': ' + $('note').value.trim() : '');
    mode = 'view';
    if (d.redrafted === 2) { d.status = 'final'; d.reason = reason; toast('Left for a human answer'); save(); next(); }
    else {
      d.status = 'redrafting'; d.reason = reason; d.prev = answerOf(r); d.history = (d.history || []).concat([{ text: answerOf(r), reason }]); save();
      const id = r.id;
      setTimeout(() => { const x = ST.decisions[id]; x.status = 'pending'; x.redrafted = (x.redrafted || 0) + 1; save(); if (sel === id || tab === 'pending') render(); toast('Rewritten once. Have another look.'); }, 1500);
    }
  }
  render();
}
$('detail').addEventListener('click', (e) => {
  const rm = e.target.closest('[data-rm]'); if (rm) { keepText(); refs.splice(+rm.dataset.rm, 1); renderDetail(); return; }
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
  const ids = [...picked], again = ids.filter(id => (ST.decisions[id] || {}).redrafted === 2).length;
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
    if (d.redrafted === 2) { d.status = 'final'; d.reason = reason; human++; return; }
    d.status = 'redrafting'; d.reason = reason; d.prev = answerOf(r); rewrite++;
  });
  picked.clear(); $('bulkRej').hidden = true; $('bulkNote').value = ''; save(); render();
  toast(rewrite + ' sent back to be rewritten' + (human ? ' · ' + human + ' left for a human' : ''));
  if (rewrite) setTimeout(() => {
    ids.forEach(id => { const x = ST.decisions[id]; if (x && x.status === 'redrafting') { x.status = 'pending'; x.redrafted = (x.redrafted || 0) + 1; } });
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
if (RP.get('edit')) mode = 'edit';
if (RP.get('sel')) { sel = RP.get('sel'); const sr = DRAFTS.find(x => x.id === sel); if (sr) { const s = decision(sr).status; tab = s === 'redrafting' ? 'pending' : (s === 'approved' || s === 'final') ? s : 'pending'; document.querySelectorAll('#rtabs .tab').forEach(x => x.setAttribute('aria-selected', x.dataset.f === tab)); } if (RP.get('full')) { const r = DRAFTS.find(x => x.id === sel); if (r) openFull.add(r.src[0][0] + '|' + r.src[0][1]); } }
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
  .bar{display:flex;gap:12px;align-items:center;margin:0 0 12px}
  .smart{display:flex;align-items:center;gap:10px;padding:6px 6px 6px 14px;border-radius:14px;border:1.5px solid transparent;background:linear-gradient(var(--panel),var(--panel)) padding-box,var(--brand-gradient) border-box;box-shadow:0 14px 30px -24px rgba(232,93,117,.8)}
  .smart:focus-within{box-shadow:0 0 0 4px rgba(232,93,117,.14),0 14px 30px -24px rgba(232,93,117,.8)}
  .smart__ic{width:18px;height:18px;fill:none;stroke:#C7385B;stroke-width:1.8;stroke-linejoin:round;flex:none}
  .smart input{flex:1;border:0;outline:0;background:none;font:inherit;font-size:.95rem;color:var(--ink);height:40px}
  .smart__tips{display:flex;gap:8px;flex-wrap:wrap;align-items:center;margin:10px 0 16px;font-size:.78rem;color:var(--muted)}
  .smart__tips button{border:1px dashed var(--line-2);background:none;border-radius:999px;padding:4px 10px;font:inherit;font-size:.76rem;color:var(--ink);cursor:pointer}
  .smart__tips button:hover{border-color:var(--rose);color:#B73C54}
  .intent{display:flex;align-items:center;gap:12px;flex-wrap:wrap;padding:12px 16px;border-radius:14px;margin-bottom:14px;background:rgba(232,93,117,.06);border:1px solid rgba(232,93,117,.22);font-size:.88rem}
  .intent.is-del{background:rgba(198,69,69,.06);border-color:rgba(198,69,69,.28)}
  .intent b{font-weight:700}
  .intent .spacer{flex:1}
  .ans{display:grid;grid-template-columns:auto minmax(0,1fr);gap:0 14px}
  .ans > :not(.pick){grid-column:2}
  .ans .pick{grid-row:1/span 3;margin-top:3px}
  .ans.is-picked{border-color:rgba(232,93,117,.45);box-shadow:0 0 0 3px rgba(232,93,117,.08)}
  .ans__acts{display:flex;gap:4px;margin-left:8px}
  .ans__acts a,.ans__acts button{border:0;background:none;padding:4px 8px;border-radius:8px;font:inherit;font-size:.76rem;font-weight:600;color:var(--muted);cursor:pointer;text-decoration:none}
  .ans__acts a:hover,.ans__acts button:hover{background:var(--bg-soft);color:var(--ink);text-decoration:none}
  .ans__acts .del:hover{color:var(--error)}
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
        <p>Approved answers go out from here. In this phase they power Ask lojo and an export; publishing to your own pages comes with the full build.</p>
      </div>
      <span class="spacer"></span>
      <button class="btn btn--secondary" id="csv">Export CSV</button>
      <button class="btn btn--primary" id="json">Export JSON</button>
    </div>
    <section class="chan" aria-label="Where answers go">
      <a class="ch is-live" href="chat.html"><span class="ch__ic"><svg class="i" viewBox="0 0 24 24"><path d="M21 12a8 8 0 0 1-11.6 7.1L4 20l1-4.6A8 8 0 1 1 21 12z"/></svg></span><span><b>Ask lojo page</b><span>Reads only approved answers</span></span><em>Live · open →</em></a>
      <div class="ch is-live"><span class="ch__ic"><svg class="i" viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/><path d="M9.5 9.5a2.5 2.5 0 1 1 3.5 2.3c-.6.3-1 .8-1 1.5V14M12 17h.01"/></svg></span><span><b>Ask lojo button</b><span>On every page of this workspace</span></span><em>Live</em></div>
      <div class="ch is-off"><span class="ch__ic"><svg class="i" viewBox="0 0 24 24"><path d="M3 11l9-7 9 7v9a1 1 0 0 1-1 1h-5v-6H9v6H4a1 1 0 0 1-1-1z"/></svg></span><span><b>Help centre</b><span>Publish answers to your own pages</span></span><em>Full build</em></div>
      <div class="ch is-off"><span class="ch__ic"><svg class="i" viewBox="0 0 24 24"><path d="M5 9h14M5 15h14M10 4 8 20M16 4l-2 16"/></svg></span><span><b>Slack &amp; Teams</b><span>Answer where your team asks</span></span><em>Full build</em></div>
    </section>
    <h2 class="sech">Approved answers</h2>
    <form class="smart" id="smartForm">
      <svg class="smart__ic" viewBox="0 0 24 24"><path d="M12 3l1.8 4.7L18.5 9.5l-4.7 1.8L12 16l-1.8-4.7L5.5 9.5l4.7-1.8z"/><path d="M19 15l.8 2.2L22 18l-2.2.8L19 21l-.8-2.2L16 18l2.2-.8z"/></svg>
      <input id="filter" placeholder="Search or ask: “find everything about refunds”, “remove answers about SSO”, “edit the API answer”" aria-label="Search or ask" autocomplete="off">
      <button class="btn btn--primary btn--sm" type="submit">Go</button>
    </form>
    <div class="smart__tips" id="tips"><span>Try</span><button type="button">find everything about refunds</button><button type="button">edit the API rate limits answer</button><button type="button">remove answers about SSO</button></div>
    <div class="intent" id="intent" hidden></div>
    <div class="bar"><span class="sub" id="meta"></span></div>
    <div class="alist" id="alist"></div>
""",
  js=r"""
const approved = () => DRAFTS.filter(r => decision(r).status === 'approved').map(r => ({ r, q: QUESTIONS.find(q => q.id === r.qid).q, a: answerOf(r), d: decision(r) }));
// smart search: plain words search by meaning; "remove/delete…" and "edit/change…" select the matches to act on
const picked = new Set();
let ask = { verb: 'find', topic: '' };
function parse(v) {
  const s = v.trim().toLowerCase();
  const verb = /^(remove|delete|retire|take out|unpublish)\b/.test(s) ? 'remove' : /^(edit|change|update|fix|rewrite|modify)\b/.test(s) ? 'edit' : 'find';
  const topic = s.replace(/^(please\s+)?(find|show|search|list|get|remove|delete|retire|take out|unpublish|edit|change|update|fix|rewrite|modify)\b/, '')
    .replace(/\b(me|all|every|everything|anything|answers?|the|about|on|for|related to|regarding|that mention|mentioning|with)\b/g, ' ').replace(/\s+/g, ' ').trim();
  return { verb, topic };
}
function matches(x, topic) {
  if (!topic) return true;
  const txt = (x.q + ' ' + x.a).toLowerCase();
  if (txt.includes(topic)) return true;
  const sc = score(topic, x.q + ' ' + x.a);
  return sc.c > 0 || topic.split(' ').filter(w => w.length > 3).some(w => txt.includes(w.replace(/s$/, '')));
}
function render() {
  const all = approved(), list = all.filter(x => matches(x, ask.topic));
  [...picked].forEach(id => { if (!list.some(x => x.r.id === id)) picked.delete(id); });
  $('meta').textContent = (ask.topic ? list.length + ' of ' : '') + all.length + ' approved answers' + (ask.topic ? ' match “' + ask.topic + '”' : '');
  const act = ask.verb !== 'find' && ask.topic;
  $('intent').hidden = !act; $('intent').classList.toggle('is-del', ask.verb === 'remove');
  if (act) $('intent').innerHTML = (ask.verb === 'remove'
    ? '<span><b>Remove ' + picked.size + ' of ' + list.length + '</b> answers about “' + esc(ask.topic) + '” from the store. Ask lojo stops using them; you can bring them back in Build.</span><span class="spacer"></span><button class="btn btn--danger btn--sm" id="doRemove"' + (picked.size ? '' : ' disabled') + '>Remove ' + picked.size + '</button>'
    : '<span><b>' + list.length + ' answer' + (list.length === 1 ? '' : 's') + '</b> about “' + esc(ask.topic) + '”. Pick one to edit it in Build.</span><span class="spacer"></span>') +
    '<button class="btn btn--ghost btn--sm" id="clearAsk">Clear</button>';
  $('alist').innerHTML = list.length ? list.map(x => '<article class="ans' + (picked.has(x.r.id) ? ' is-picked' : '') + '">' +
    (act && ask.verb === 'remove' ? '<input type="checkbox" class="pick" data-pick="' + x.r.id + '"' + (picked.has(x.r.id) ? ' checked' : '') + ' aria-label="Select">' : '') +
    '<h3>' + esc(x.q) + '</h3><div class="ansbody">' + md(x.a) + '</div><div class="meta">' +
    x.r.src.map(([d, loc]) => srcChip(d, loc)).join('') + (x.d.edited ? '<span class="badge badge--muted">Edited</span>' : '') + (x.d.redrafted ? '<span class="badge badge--info">Redrafted</span>' : '') +
    '<span class="by">Approved' + (x.d.at ? ' · ' + esc(x.d.at) : '') + '</span><span class="ans__acts"><a href="build.html?sel=' + x.r.id + '&edit=1">Edit</a><button class="del" data-del="' + x.r.id + '">Remove</button></span></div></article>').join('')
    : '<div class="card empty"><b>' + (all.length ? 'Nothing matches “' + esc(ask.topic) + '”' : 'Nothing approved yet') + '</b>' + (all.length ? 'Try other words, or ask it differently.' : '<a href="build.html">Review the first batch</a> to fill the store.') + '</div>';
}
function removeIds(ids) {
  const before = ids.map(id => [id, { ...(ST.decisions[id] || {}) }]);
  ids.forEach(id => { ST.decisions[id] = { ...(ST.decisions[id] || {}), status: 'pending' }; });
  save(); picked.clear(); render();
  toastError(ids.length + ' answer' + (ids.length === 1 ? '' : 's') + ' removed from the store and sent back to Build.', () => { before.forEach(([id, d]) => { ST.decisions[id] = d; }); save(); render(); toast('Brought back'); });
  const t = $('toast'); const b = t.querySelector('button'); if (b) b.textContent = 'Undo'; t.classList.remove('is-err');
}
function run(v) {
  ask = parse(v); picked.clear();
  if (ask.verb === 'remove') approved().filter(x => matches(x, ask.topic)).forEach(x => picked.add(x.r.id));
  render();
  if (ask.verb === 'edit') { const one = approved().filter(x => matches(x, ask.topic)); if (one.length === 1) location.href = 'build.html?sel=' + one[0].r.id + '&edit=1'; }
}
$('smartForm').addEventListener('submit', (e) => { e.preventDefault(); run($('filter').value); });
$('filter').addEventListener('input', () => { const v = $('filter').value; if (!/^(remove|delete|retire|edit|change|update|fix|rewrite|modify)\b/i.test(v.trim())) run(v); });
$('tips').addEventListener('click', (e) => { const b = e.target.closest('button'); if (!b) return; $('filter').value = b.textContent; run(b.textContent); });
$('intent').addEventListener('click', (e) => {
  if (e.target.id === 'clearAsk') { $('filter').value = ''; run(''); }
  if (e.target.id === 'doRemove') removeIds([...picked]);
});
$('alist').addEventListener('change', (e) => { const c = e.target.closest('[data-pick]'); if (!c) return; c.checked ? picked.add(c.dataset.pick) : picked.delete(c.dataset.pick); render(); });
$('alist').addEventListener('click', (e) => { const d = e.target.closest('[data-del]'); if (d) removeIds([d.dataset.del]); });
function download(name, text, type) {
  const a = document.createElement('a');
  a.href = URL.createObjectURL(new Blob([text], { type }));
  a.download = name; a.click(); setTimeout(() => URL.revokeObjectURL(a.href), 1000);
}
const rows = () => approved().map(x => ({ question: x.q, answer: x.a, sources: x.r.src.map(([d, loc]) => docById(d).name + ' (' + loc + ')'), edited: !!x.d.edited, approved: x.d.at || '' }));
function exportGuard(run) { if (!navigator.onLine || new URLSearchParams(location.search).get('fail') === 'export') { toastError('Export failed. Your answers are safe; check your connection.', run); return false; } return true; }
$('json').addEventListener('click', () => { if (!exportGuard(() => $('json').click())) return; download('oslo-approved-answers.json', JSON.stringify(rows(), null, 2), 'application/json'); toast('Exported ' + rows().length + ' answers'); });
$('csv').addEventListener('click', () => { if (!exportGuard(() => $('csv').click())) return;
  const q = (s) => '"' + String(s).replace(/"/g, '""') + '"';
  const csv = ['question,answer,sources,edited,approved'].concat(rows().map(r => [r.question, r.answer, r.sources.join('; '), r.edited, r.approved].map(q).join(','))).join('\n');
  download('oslo-approved-answers.csv', csv, 'text/csv'); toast('Exported ' + rows().length + ' answers');
});
render();
""")


# ============================================================ ACTIVITY
ACTIVITY = dict(
  active='activity', title='Activity',
  css=r"""
  .acard{background:var(--panel);border:1px solid var(--line);border-radius:20px;padding:24px 26px;box-shadow:0 16px 30px -28px rgba(36,26,20,.3)}
  .acard__h{display:flex;align-items:flex-start;gap:14px;margin-bottom:18px}
  .acard__h h2{font-family:var(--display);font-weight:700;font-size:1.3rem;margin:0}
  .acard__h .sub{margin-top:2px}
  .acard__h .spacer{flex:1}
  .refresh{width:40px;height:40px;border-radius:12px;border:1px solid var(--line-2);background:var(--panel);display:grid;place-items:center;cursor:pointer;color:var(--ink)}
  .refresh:hover{background:var(--bg-soft)}
  .refresh svg{width:18px;height:18px}
  .refresh.is-spin svg{animation:spin .8s linear infinite}
  .agrp{display:flex;align-items:center;gap:10px;margin:22px 0 4px;font-size:.78rem;font-weight:800;letter-spacing:.12em;text-transform:uppercase;color:var(--muted)}
  .agrp.run{color:#8E2F45}
  .agrp b{min-width:24px;height:24px;padding:0 7px;border-radius:7px;border:1px solid var(--line-2);display:grid;place-items:center;font-size:.76rem;letter-spacing:0;color:var(--ink)}
  .anone{color:var(--muted);font-size:.9rem;margin:8px 0 0}
  .arow{display:grid;grid-template-columns:44px minmax(0,1fr) auto;gap:6px 16px;padding:18px 0;border-top:1px solid var(--line)}
  .agrp + .arow{border-top:0}
  .arow h3{margin:0;font-family:var(--display);font-weight:700;font-size:1.05rem;display:flex;align-items:center;gap:8px;flex-wrap:wrap}
  .arow h3 a{font-family:var(--body);font-size:.72rem;font-weight:600;color:var(--muted);border:1px solid var(--line-2);border-radius:999px;padding:2px 8px;text-decoration:none}
  .arow h3 a:hover{color:var(--ink);border-color:rgba(36,26,20,.3)}
  .arow .d{grid-column:2;margin:2px 0 0;color:var(--muted);font-size:.88rem}
  .anums{grid-column:2;display:flex;gap:36px;flex-wrap:wrap;margin-top:12px}
  .anums div b{display:block;font-family:var(--display);font-weight:700;font-size:1.25rem;line-height:1.2}
  .anums div span{font-size:.76rem;color:var(--muted)}
  .anums div.bad b{color:var(--error)}
  .alast{grid-column:2;margin-top:10px;font-size:.78rem;color:var(--muted)}
  .alast b{color:var(--ink);font-weight:600}
  .apill{grid-column:3;grid-row:1;align-self:start;height:26px;padding:0 10px;border-radius:8px;border:1px solid var(--line-2);font-size:.72rem;font-weight:700;display:inline-flex;align-items:center;gap:6px;color:var(--muted);white-space:nowrap}
  .apill.run{border-color:rgba(63,143,95,.35);background:rgba(63,143,95,.08);color:var(--success)}
  .apill.run::before{content:"";width:7px;height:7px;border-radius:50%;background:currentColor;animation:livePulse 1.4s ease-in-out infinite}
  @keyframes livePulse{50%{opacity:.3}}
  .arow.is-off h3,.arow.is-off .anums{opacity:.6}
  .vtog{display:inline-flex;padding:3px;border-radius:12px;border:1px solid var(--line-2);background:var(--bg-soft);margin-right:8px}
  .vtog button{display:inline-flex;align-items:center;gap:6px;height:32px;padding:0 12px;border:0;border-radius:9px;background:none;font:inherit;font-size:.8rem;font-weight:600;color:var(--muted);cursor:pointer}
  .vtog button svg{width:15px;height:15px;fill:none;stroke:currentColor;stroke-width:1.9;stroke-linecap:round;stroke-linejoin:round}
  .vtog button[aria-pressed="true"]{background:var(--panel);color:var(--ink);box-shadow:0 2px 6px -2px rgba(36,26,20,.25)}
  .agrid{display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:14px;margin-top:10px}
  .acardx{display:flex;flex-direction:column;gap:6px;padding:18px;border:1px solid var(--line);border-radius:16px;background:var(--panel);transition:border-color .15s ease,box-shadow .15s ease,transform .15s ease}
  .acardx:hover{border-color:var(--line-2);box-shadow:0 16px 30px -24px rgba(36,26,20,.55);transform:translateY(-2px)}
  .acardx.is-run{border-color:rgba(63,143,95,.35);background:linear-gradient(180deg,rgba(63,143,95,.05),var(--panel) 45%)}
  .acardx.is-off{opacity:.65}
  .acardx__top{display:flex;align-items:flex-start;justify-content:space-between;margin-bottom:6px}
  .acardx .apill{grid-column:auto;grid-row:auto}
  .acardx h3{margin:0;font-family:var(--display);font-weight:700;font-size:1.05rem}
  .acardx__stage{align-self:flex-start;font-size:.7rem;font-weight:600;color:var(--muted);border:1px solid var(--line-2);border-radius:999px;padding:2px 8px;text-decoration:none}
  .acardx__stage:hover{color:var(--ink);text-decoration:none}
  .acardx__d{margin:4px 0 0;color:var(--muted);font-size:.84rem;min-height:2.6em}
  .acardx__nums{display:grid;grid-template-columns:repeat(3,1fr);gap:6px;margin-top:8px;padding:12px 0;border-top:1px solid var(--line);border-bottom:1px solid var(--line)}
  .acardx__nums b{display:block;font-family:var(--display);font-size:1.1rem;font-weight:700}
  .acardx__nums span{font-size:.7rem;color:var(--muted);line-height:1.25;display:block}
  .acardx__nums .bad b{color:var(--error)}
  .acardx__last{margin:6px 0 0;font-size:.76rem;color:var(--muted);display:flex;align-items:center;gap:6px;overflow:hidden;white-space:nowrap;text-overflow:ellipsis}
  .acardx__last b{color:var(--success)}
  .acardx__last .ld{width:7px;height:7px;border-radius:50%;background:var(--success);flex:none;animation:livePulse 1.4s ease-in-out infinite}
  .llist{border:1px solid var(--line);border-radius:14px;overflow:hidden;margin-top:10px}
  .lrow{display:grid;grid-template-columns:44px minmax(150px,200px) minmax(0,1fr) 150px 92px 80px 14px;gap:14px;align-items:center;padding:10px 16px;color:inherit;text-decoration:none;transition:background-color .15s ease}
  .lrow + .lrow{border-top:1px solid var(--line)}
  .lrow:hover{background:var(--bg-soft);text-decoration:none}
  .lrow.is-off{opacity:.6}
  .lrow .ava3d,.lrow .ava3d img,.lrow .ava3d > svg{width:36px;height:36px}
  .lrow__n b{display:block;font-size:.9rem;font-weight:600}
  .lrow__n span{font-size:.74rem;color:var(--muted)}
  .lrow__w{font-size:.82rem;color:var(--muted);white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
  .lrow__k{font-size:.78rem;color:var(--muted);white-space:nowrap}
  .lrow__k b{color:var(--ink);font-family:var(--display)}
  .lrow .apill{justify-self:start;grid-column:auto;grid-row:auto;align-self:center}
  .lrow time{font-size:.76rem;color:var(--muted);text-align:right;white-space:nowrap}
  .lrow__go{color:var(--muted)}
  @media (max-width:900px){.lrow{grid-template-columns:40px minmax(0,1fr) auto}.lrow__w,.lrow__k,.lrow time,.lrow__go{display:none}}
  @media (max-width:640px){.arow{grid-template-columns:44px minmax(0,1fr)}.apill{grid-column:2;grid-row:auto;justify-self:start}.anums{gap:20px}}
""",
  body=r"""
    <div class="head">
      <div>
        <p class="label">Activity</p>
        <h1>Agents at work</h1>
        <p>See who is working, what needs your attention, and each agent’s results.</p>
      </div>
    </div>
    <section class="acard" aria-labelledby="allH">
      <div class="acard__h">
        <div><h2 id="allH">All agents</h2><p class="sub" id="upd"></p></div>
        <span class="spacer"></span>
        <div class="vtog" role="group" aria-label="View">
          <button type="button" data-view="cards" aria-pressed="true" title="Card view"><svg viewBox="0 0 24 24"><rect x="3" y="3" width="7" height="7" rx="1.5"/><rect x="14" y="3" width="7" height="7" rx="1.5"/><rect x="3" y="14" width="7" height="7" rx="1.5"/><rect x="14" y="14" width="7" height="7" rx="1.5"/></svg>Cards</button>
          <button type="button" data-view="list" aria-pressed="false" title="List view"><svg viewBox="0 0 24 24"><path d="M8 6h13M8 12h13M8 18h13M3.5 6h.01M3.5 12h.01M3.5 18h.01"/></svg>List</button>
        </div>
        <button class="refresh" id="refresh" type="button" aria-label="Refresh"><svg class="i" viewBox="0 0 24 24"><path d="M3 12a9 9 0 0 1 15.5-6.2L21 8M21 3v5h-5M21 12a9 9 0 0 1-15.5 6.2L3 16M3 21v-5h5"/></svg></button>
      </div>
      <div class="agf chips" id="agFilters" role="group" aria-label="Filter agents"></div>
      <div id="alist"></div>
    </section>
""",
  js=r"""
let agFilter = new URLSearchParams(location.search).get('stage') || 'all';
// what each agent has done so far, from the same counts the rest of the app uses
function statsFor(name, c) {
  const failed = Object.keys(ST.draftFailed || {}).filter(k => ST.draftFailed[k] && ST.draftFailed[k] !== 'retrying').length;
  const docFail = (ST.docx || []).filter(d => d.status === 'failed').length;
  const ch = ST.chat || {}, rewritten = DRAFTS.filter(r => decision(r).redrafted).length;
  return {
    'Sync agent': [[c.docs + (ST.docx || []).length, 'Documents synced'], [Object.keys(ST.apps || {}).length, 'Apps connected'], [docFail, 'Failed syncs', docFail]],
    'Indexer': [[c.pages, 'Pages read'], [c.passages, 'Passages indexed'], [0, 'Failed runs']],
    'Question finder': [[c.questions, 'Questions found'], [4, 'New since yesterday'], [0, 'Failed runs']],
    'Gap finder': [[c.gaps, 'Open gaps'], [1, 'Contradictions'], [0, 'Failed runs']],
    'Drafting agent': [[c.drafts, 'Drafts written'], [c.pending, 'Waiting for review'], [failed, 'Failed drafts', failed]],
    'Rewrite agent': [[rewritten, 'Drafts rewritten'], [DRAFTS.filter(r => decision(r).redrafted === 2).length, 'Rewritten twice'], [c.final, 'Left for a human']],
    'Chat agent': [[(ch.asked || 0) + 14, 'Questions asked'], [(ch.answered || 0) + 11, 'Answered'], [(ch.declined || 0) + 3, 'Declined']],
    'Publisher': [[0, 'Published'], [0, 'Channels'], ['—', 'Full build']],
  }[name];
}
const at = (min) => { const d = new Date(Date.now() - min * 60000); return (d.toDateString() === new Date().toDateString() ? 'Today' : d.toLocaleDateString('en-GB', { day: 'numeric', month: 'short' })) + ', ' + d.toLocaleTimeString('en-GB', { hour: '2-digit', minute: '2-digit' }); };
function row([k, name, min, last, what], c) {
  const s = AG_STAGES.find(x => x[0] === k);
  const pill = min === 0 ? '<span class="apill run">Working</span>' : min === null ? '<span class="apill">Not yet</span>' : '<span class="apill">Idle</span>';
  return '<article class="arow' + (min === null ? ' is-off' : '') + '">' + ava3d(k, name, min) + '<h3>' + esc(name) + ' <a href="' + s[2] + '">' + s[1] + '</a></h3>' + pill +
    '<p class="d">' + esc(what) + '</p><div class="anums">' + statsFor(name, c).map(([n, l, bad]) => '<div' + (bad ? ' class="bad"' : '') + '><b>' + (typeof n === 'number' ? n.toLocaleString('en-GB') : n) + '</b><span>' + l + '</span></div>').join('') + '</div>' +
    '<p class="alast">' + (min === null ? 'No activity yet' : (min === 0 ? '<b>Running now</b> · ' : 'Last activity ' + at(min) + ' · ') + esc(last)) + '</p></article>';
}
// card view: one card per agent; list view: one row per agent
let view = 'cards';
try { view = localStorage.getItem('lojo-agents-view') || 'cards'; } catch (e) {}
function card([k, name, min, last, what], c) {
  const s = AG_STAGES.find(x => x[0] === k);
  const pill = min === 0 ? '<span class="apill run">Working</span>' : min === null ? '<span class="apill">Not yet</span>' : '<span class="apill">Idle</span>';
  return '<article class="acardx' + (min === 0 ? ' is-run' : '') + (min === null ? ' is-off' : '') + '"><div class="acardx__top">' + ava3d(k, name, min) + pill + '</div>' +
    '<h3>' + esc(name) + '</h3><a class="acardx__stage" href="' + s[2] + '">' + s[1] + '</a><p class="acardx__d">' + esc(what) + '</p>' +
    '<div class="acardx__nums">' + statsFor(name, c).map(([n, l, bad]) => '<div' + (bad ? ' class="bad"' : '') + '><b>' + (typeof n === 'number' ? n.toLocaleString('en-GB') : n) + '</b><span>' + l + '</span></div>').join('') + '</div>' +
    '<p class="acardx__last">' + (min === null ? 'No activity yet' : (min === 0 ? '<i class="ld"></i><b>Running now</b> · ' : agAgo(min) + ' · ') + esc(last)) + '</p></article>';
}
function line([k, name, min, last, what], c) {
  const s = AG_STAGES.find(x => x[0] === k), n = statsFor(name, c)[0];
  const pill = min === 0 ? '<span class="apill run">Working</span>' : min === null ? '<span class="apill">Not yet</span>' : '<span class="apill">Idle</span>';
  return '<a class="lrow' + (min === null ? ' is-off' : '') + '" href="' + s[2] + '">' + ava3d(k, name, min) +
    '<span class="lrow__n"><b>' + esc(name) + '</b><span>' + s[1] + '</span></span>' +
    '<span class="lrow__w">' + (min === null ? 'No activity yet' : esc(last)) + '</span>' +
    '<span class="lrow__k"><b>' + (typeof n[0] === 'number' ? n[0].toLocaleString('en-GB') : n[0]) + '</b> ' + n[1].toLowerCase() + '</span>' +
    pill + '<time>' + (min === null ? '—' : agAgo(min)) + '</time><span class="lrow__go">→</span></a>';
}
function render() {
  const c = counts();
  document.querySelectorAll('.vtog [data-view]').forEach(b => b.setAttribute('aria-pressed', b.dataset.view === view));
  const chips = [['all', 'All', AGENTS.length]].concat(AG_STAGES.map(([k, label]) => [k, label.slice(3), AGENTS.filter(a => a[0] === k).length]));
  $('agFilters').innerHTML = chips.map(([k, label, n]) => '<button type="button" class="chip" data-agf="' + k + '" aria-pressed="' + (agFilter === k) + '">' + label + ' <em>' + n + '</em></button>').join('');
  const list = AGENTS.filter(a => agFilter === 'all' || a[0] === agFilter), run = list.filter(a => a[2] === 0), rest = list.filter(a => a[2] !== 0);
  const wrapG = (items) => view === 'cards' ? '<div class="agrid">' + items.map(a => card(a, c)).join('') + '</div>' : '<div class="llist">' + items.map(a => line(a, c)).join('') + '</div>';
  $('alist').innerHTML = '<div class="agrp run">Now running <b>' + run.length + '</b></div>' + (run.length ? wrapG(run) : '<p class="anone">No agents are running right now.</p>') +
    '<div class="agrp">Other agents <b>' + rest.length + '</b></div>' + wrapG(rest);
  $('upd').textContent = 'Updated ' + at(0);
}
$('agFilters').addEventListener('click', (e) => { const b = e.target.closest('[data-agf]'); if (!b) return; agFilter = b.dataset.agf; render(); });
document.querySelector('.vtog').addEventListener('click', (e) => { const b = e.target.closest('[data-view]'); if (!b) return; view = b.dataset.view; try { localStorage.setItem('lojo-agents-view', view); } catch (err) {} render(); });
$('refresh').addEventListener('click', () => { const b = $('refresh'); b.classList.add('is-spin'); setTimeout(() => { b.classList.remove('is-spin'); render(); toast('Up to date'); }, 700); });
render();
""")

# ============================================================ CHAT
CHAT = dict(
  active='approved', title='Ask lojo',
  css=r"""
""",
  body=r"""
    <div class="head">
      <div>
        <p class="label">04 Distribute</p>
        <h1>Ask lojo</h1>
        <p>Answers only from approved knowledge, with the source for every answer. If something isn’t approved yet, it says so.</p>
      </div>
      <span class="spacer"></span>
      <span class="badge badge--muted">Not published anywhere in this phase</span>
    </div>
    <div class="askhost" id="askHost"></div>
""",
  js=r"""
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

      <section class="card"><div class="card__head"><h2>How Ask lojo did</h2><span class="sub">Questions people asked Ask lojo this phase</span></div><div class="card__body">
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
  if ($('decision')) $('decision').innerHTML = d ? '<div class="decided ' + (d === 'go' ? 'go' : 'stop') + '">' + (d === 'go' ? '✓ You chose to go on to the full build. We’ll send a plan for the twelve weeks.' : 'You chose not to go on for now. You keep the approved answers as an export.') +
    ' <button class="btn btn--ghost btn--sm" id="undoD">Change</button></div>'
    : '<p class="sub" style="margin-bottom:14px">After trying Ask lojo, decide whether to go on. Either way, you keep the approved answers.</p><div class="decide"><button class="btn btn--grad" id="go">Go on to the full build</button><button class="btn btn--secondary" id="stop">Not now</button></div>';
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
    ['G26', 'Forgot your password?', 'Ask for a reset link, then a “Check your email” page with a resend timer.', [L('auth.html?s=forgot', 'Forgot'), L('auth.html?s=sent&email=sara@oslo.com', 'Check your email')]],
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
    ['G7', '“Asked 3 times” badge', 'On questions asked more than once.', [L('insights.html#questions', 'Open questions')]],
    ['G8', 'Leave out, with a note', 'Optional note; “Left out” filter and the note on the row.', [L('insights.html?demo=leave', 'Leave one out')]],
  ]],
  ['Build', [
    ['G9', 'Full source passage', '“Show full passage” with the quoted words highlighted.', [L('build.html?sel=r1&full=1', 'Open')]],
    ['G10', 'Someone else decided it', 'Banner with who and when; your actions are hidden.', [L('build.html?sel=r12', 'Open')]],
    ['G14', 'Rewritten twice', '“Rewritten twice” badge and the earlier drafts with their reasons.', [L('build.html?sel=r8', 'Open')]],
  ]],
  ['Ask lojo', [
    ['G29', 'Small talk', '“Hi” and “Thanks” get a short reply with no sources.', [L('chat.html?say=Hi|Thanks', 'Open')]],
    ['G30', 'Formatted answers', 'Headings, lists and bold, sized to the bubble.', [L('chat.html?say=How fast can we call the API?', 'Open')]],
  ]],
  ['Distribute', [
    ['—', 'Distribute page', 'Approved answers plus where they go: the Ask lojo page and button live, help centre and Slack in the full build.', [L('distribute.html', 'Open')]],
  ]],
  ['Knowledge', [
    ['G11', 'Ask lojo numbers', 'Asked, answered, declined and the answer rate.', [L('knowledge.html', 'Open knowledge')]],
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

PAGES = {'states': STATES, 'dashboard': OVERVIEW, 'sources': DOCUMENTS, 'insights': QUESTIONS_PAGE, 'build': REVIEW, 'distribute': APPROVED, 'chat': CHAT, 'knowledge': READOUT, 'activity': ACTIVITY}
for name, p in PAGES.items():
    html = page(p['active'], p['title'], p['css'], p['body'], p['js'], p.get('desc', ''))
    with open(os.path.join(OUT, name + '.html'), 'w') as f:
        f.write(html)
    print('wrote', name + '.html', len(html))
