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
  .resume{display:flex;align-items:center;gap:16px;margin:0 0 20px;padding:14px 16px 14px 20px;border:1px solid #FFB199;border-radius:16px;background:#FFF0E8}
  .resume[hidden]{display:none}
  .resume > span{flex:1;min-width:0;font-size:.88rem;color:var(--muted)}
  .resume b{display:block;color:var(--ink);font-size:.95rem}
  .resume__x{width:30px;height:30px;border:0;border-radius:8px;background:none;color:var(--muted);font-size:1.2rem;cursor:pointer}
  .resume__x:hover{background:rgba(36,26,20,.06)}
  :root[data-theme="dark"] .resume{background:rgba(255,177,153,.1);border-color:rgba(255,177,153,.35)}
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
  .next__main{position:relative;overflow:hidden;padding:30px 30px;background:radial-gradient(120% 140% at 0% 0%,#FFF1EC 0%,#FFF9F6 40%,#FFFFFF 75%);border-right:1px solid var(--line);isolation:isolate}
  .next__main::before{content:"";position:absolute;inset:0;z-index:-1;background-image:radial-gradient(rgba(232,93,117,.16) 1px,transparent 1.2px);background-size:16px 16px;opacity:.5;-webkit-mask-image:linear-gradient(90deg,transparent 30%,#000 75%);mask-image:linear-gradient(90deg,transparent 30%,#000 75%)}
  .next__main::after{content:"";position:absolute;right:-60px;bottom:-80px;width:260px;height:260px;border-radius:50%;z-index:-1;background:radial-gradient(circle,rgba(255,177,153,.16),transparent 65%)}
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
  .stack{width:172px;height:142px;right:28px}
  .stack .card{padding:12px}
  .stack .count{min-width:28px;height:28px;font-size:.82rem}
  .next__side{padding:14px 18px}
  .also{padding:7px 10px}
  .also .ic{width:32px;height:32px}
  .tiles{gap:14px}
  .tile{min-height:0;align-items:flex-start;justify-content:flex-start;text-align:left;gap:4px;padding:18px 20px 20px;border-radius:12px}
  .tile--soft{display:grid!important;grid-template-columns:auto minmax(0,1fr);grid-template-rows:auto auto;column-gap:12px;align-items:center;padding-right:16px}
  .tile--soft .gauge{grid-row:1/span 2}
  .tile--soft .tile__lbl{align-self:end;white-space:nowrap;letter-spacing:.06em;margin-bottom:2px}
  .tile--soft .gauge{width:76px;height:46px}
  .tile--soft .gauge svg{width:76px;height:43px}
  .tile--soft .gauge b{font-size:.82rem}
  .tile--soft .tile__sub{align-self:start}
  .tile__lbl{font-size:.72rem;font-weight:800;margin-bottom:6px}
  .tile__val{margin-bottom:4px}
  .tile__val{font-size:1.6rem}
  .tile__sub{font-size:.78rem;line-height:1.35}
  .tile__tag{top:10px;right:10px;height:20px;font-size:.62rem}
  .tile__go{right:12px;bottom:10px}
  .gauge{width:96px;height:58px;flex:none}
  .gauge svg{width:96px;height:54px}
  .gauge b{font-size:.92rem;bottom:-2px;text-align:center}
  .checks{margin-top:12px;padding-top:10px;font-size:.8rem}
  @media (max-width:1320px){.tile{min-height:0}}
  /* Your loop: the same peach-to-white as Up next */
  .mini{background:radial-gradient(120% 160% at 0% 0%,#FFE3DA 0%,#FFF4EF 45%,#FFFFFF 85%);border-color:#F6D5CB}
  .mini:hover{border-color:#F0BBAB;box-shadow:0 12px 26px -18px rgba(232,93,117,.6)}
  .mini .sep{background:#F3DCD4}
  .mini .m-track{stroke:rgba(232,93,117,.14)}
  :root[data-theme="dark"] .mini{background:radial-gradient(120% 160% at 0% 0%,rgba(232,93,117,.18),var(--panel) 70%);border-color:var(--line-2)}
  .stack .card.qa{display:flex;flex-direction:column;gap:6px;padding:12px 13px}
  .qa__src{display:inline-flex;align-items:center;gap:5px;align-self:flex-start;height:18px;padding:0 7px;border-radius:999px;background:var(--bg-soft);font-size:.58rem;font-weight:700;letter-spacing:.04em;color:var(--muted)}
  .qa__src svg{width:10px;height:10px;fill:none;stroke:currentColor;stroke-width:2;stroke-linecap:round;stroke-linejoin:round}
  .qa__q{font-size:.68rem;line-height:1.3;flex:none;color:var(--ink);display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden}
  .qa__a{margin:0;font-size:.6rem;line-height:1.35;color:var(--muted);display:-webkit-box;-webkit-line-clamp:1;-webkit-box-orient:vertical;overflow:hidden}
  .stack .card.qa .acts{margin-top:auto}
  .stack .card.qa .acts i{height:14px}
  .stack .card.qa.in{animation:qaIn .45s ease}
  @keyframes qaIn{from{opacity:0;transform:rotate(4deg) translateY(6px)}}
  /* knowledge tiles: centred, with room for the tag */
  .tile{align-items:center!important;text-align:center!important;padding-top:34px!important}
  .tile--soft{display:flex!important;flex-direction:column;padding-top:22px!important}
  .tile--soft .gauge{grid-row:auto}
  .tile--soft .tile__lbl,.tile--soft .tile__sub{align-self:center}
  .tile .tip::after{left:50%;transform:translate(-50%,4px)}
""",
  body=r"""
    <div class="head">
      <div class="hello">
        <div><h1 id="ovTitle">Good evening, Eric <span class="wave" aria-hidden="true">👋</span></h1><p id="ovDate"></p></div>
      </div>
      <span class="spacer"></span>
      <button class="mini" id="loopBtn" type="button" aria-label="Open the loop">
        <svg viewBox="0 0 52 52" aria-hidden="true"><defs><linearGradient id="miniGrad" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#E85D75"/><stop offset="1" stop-color="#FFB199"/></linearGradient></defs>
          <circle class="m-track" cx="26" cy="26" r="21"/><circle class="m-arc" id="miniArc" cx="26" cy="26" r="21" transform="rotate(-90 26 26)"/><text id="miniFrac" x="26" y="30.5" text-anchor="middle">4/5</text></svg>
        <span><small>Your loop</small><b id="miniNow">Human validation</b><em id="miniWhy">10 drafts waiting</em></span>
        <span class="sep"></span>
        <span class="k"><small>Approved</small><b id="miniK">6</b></span>
      </button>
    </div>


    <div class="resume" id="resumeBar" hidden><span><b>Finish setting up <span id="resumeWs">your workspace</span></b>Connect a source and lojo drafts your first answers.</span><a class="btn btn--primary btn--sm" href="onboarding.html?resume=1">Resume setup →</a><button type="button" class="resume__x" id="resumeX" aria-label="Dismiss">×</button></div>

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
          <div class="card qa" id="stackCard"></div>
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

    <section class="sec" aria-labelledby="feedH">
      <div class="sec__head"><h2 id="feedH">Since you last looked</h2></div>
      <ul class="feed" id="feed"></ul>
    </section>


    <section class="sec" aria-labelledby="agH" data-feature="agents">
      <div class="sec__head"><h2 id="agH">Agents at work</h2><span>· What each agent in your loop did last</span><a href="activity.html">View all agents →</a></div>
      <div class="agf chips" id="agFilters" role="group" aria-label="Filter agents"></div>
      <ul class="agl" id="agents"></ul>
    </section>




    <!-- ASSUMPTION: server location wording is a placeholder until the week-1 sign-off is written up. check with Eric -->
    <div class="scope">
      <span class="ok">✓</span>
      <span id="scopeBy"></span>
      <span class="spacer"></span>
      <button class="btn btn--ghost btn--sm" id="scopeToggle" aria-expanded="false">Details</button>
    </div>
    <div class="scope-more" id="scopeMore" hidden>
      <div><h4>In scope</h4><ul><li>10 documents you sent us, on one lojo-run server</li><li>One fixed model, called through our proxy</li><li>Personal details are not removed automatically</li><li>Three fixed roles: Admin, Editor, Viewer</li></ul></div>
      <div><h4>Not in this phase</h4><ul><li>Publishing to a help centre or widget</li><li>Live sources such as mail and calls</li><li>Dashboards, billing and uptime guarantees</li></ul></div>
    </div>
""",
  js=r"""
try { const sk = JSON.parse(sessionStorage.getItem('lojo-setup-skipped')); if (sk) { $('resumeWs').textContent = sk.workspace || 'your workspace'; $('resumeBar').hidden = false; } } catch (e) {}
$('resumeX').addEventListener('click', () => { $('resumeBar').hidden = true; try { sessionStorage.removeItem('lojo-setup-skipped'); } catch (e) {} });
$('loopBtn').addEventListener('click', () => { location.href = window.LOOP_URL || 'onboarding.html?loop=1'; });
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
  $('miniNow').textContent = valNow ? 'Human validation' : '04 Distribute';
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
// the front card shows a real waiting draft: its question, the start of the answer, and where it came from
const SRCKIND = (docId) => /call/i.test(docById(docId).name) ? ['Call', '<path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1.9.4 1.8.7 2.7a2 2 0 0 1-.5 2.1L8 9.8a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.7.7a2 2 0 0 1 1.7 2z"/>']
  : docById(docId).faq ? ['Help page', '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c2.5 2.6 3.8 5.6 3.8 9s-1.3 6.4-3.8 9c-2.5-2.6-3.8-5.6-3.8-9S9.5 5.6 12 3z"/>']
  : /\.md$/.test(docById(docId).name) ? ['Notion', '<path d="M5 4h11l3 3v13H5z"/><path d="M9 9v7M9 9l6 7V9"/>'] : ['Document', '<path d="M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8z"/><path d="M14 3v5h5"/>'];
let stackI = 0, stackT = null;
function stackCycle() {
  const pend = DRAFTS.filter(r => decision(r).status === 'pending');
  if (!pend.length) return;
  const show = () => {
    const r = pend[stackI++ % pend.length], q = allQuestions().find(x => x.id === r.qid).q, [kind, ic] = SRCKIND(r.src[0][0]);
    $('stackCard').innerHTML = '<span class="qa__src"><svg viewBox="0 0 24 24">' + ic + '</svg>' + kind + '</span><b class="qa__q">' + esc(q) + '</b>' +
      '<p class="qa__a">' + esc(answerOf(r).replace(/[#*_>]/g, '').slice(0, 70)) + '…</p><div class="acts"><i></i><i></i><i></i></div>';
    $('stackCard').classList.remove('in'); void $('stackCard').offsetWidth; $('stackCard').classList.add('in');
  };
  show(); clearInterval(stackT);
  if (!matchMedia('(prefers-reduced-motion: reduce)').matches) stackT = setInterval(show, 3200);
}
function render() {
  const c = counts();
  let first = 'Eric';
  try { const u = JSON.parse(sessionStorage.getItem('lojo-user')); if (u && u.name) first = u.name.trim().split(' ')[0]; } catch (e) {}
  const hr = new Date().getHours();
  $('ovTitle').innerHTML = (hr < 12 ? 'Good morning' : hr < 18 ? 'Good afternoon' : 'Good evening') + ', ' + esc(first) + ' <span class="wave" aria-hidden="true">👋</span>';
  $('ovDate').textContent = new Date().toLocaleDateString('en-GB', { weekday: 'long', day: 'numeric', month: 'long' });
  miniLoop(c);

  // up next + weekly target
  const decided = c.approved + c.final, mins = Math.max(1, Math.round(c.pending * 1.2));
  if (c.pending) {
    $('nextH').innerHTML = 'Review <span class="num">' + c.pending + '</span> draft' + (c.pending > 1 ? 's' : '');
    $('stackN').textContent = c.pending; $('stack').hidden = false; stackCycle();
    $('nextSub').textContent = 'Approve, edit, or reject with a reason. Reject to have it rewritten, or send it to a person.';
    $('nextCta').innerHTML = 'Start reviewing <span class="ar">→</span>'; $('nextCta').href = 'build.html';
  } else {
    $('nextH').textContent = 'Try Ask lojo';
    $('nextSub').textContent = 'The first batch is reviewed. Ask it questions: it answers only from what you approved.';
    $('nextCta').innerHTML = 'Open Ask lojo <span class="ar">→</span>'; $('nextCta').href = 'chat.html'; $('stack').hidden = true;
  }

  const also = [];
  // the same counts as the Build tabs and the nav badge
  const T = tasks(), human = T.human, failedDrafts = T.failed.length;
  if (human) also.push({ ic: 'hand', t: human + ' question' + (human === 1 ? ' needs' : 's need') + ' a human answer', s: 'No source, or sent to a person', href: 'build.html?tab=final' });
  if (failedDrafts) also.push({ ic: 'q', t: failedDrafts + ' draft' + (failedDrafts === 1 ? '' : 's') + ' could not be written', s: 'Try ' + (failedDrafts === 1 ? 'it' : 'them') + ' again in Build', href: 'build.html?tab=needs&fq=' + T.failed[0].id });
  if (T.triage.length) also.push({ ic: 'q', t: 'Say whether ' + T.triage.length + ' question' + (T.triage.length > 1 ? 's matter' : ' matters'), s: 'Only those get drafted', href: 'build.html?tab=needs&kind=triage' });
  if (T.gaps.length) also.push({ ic: 'gap', t: T.gaps.length + ' gap' + (T.gaps.length === 1 ? ' needs' : 's need') + ' a source', s: 'Upload a document, ask an owner, or add them as questions', href: 'build.html?tab=needs&kind=gap' });
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
  const yours = allQuestions().filter(q => q.origin === 'you').length, S = sourceSummary();
  $('today').innerHTML = [
    '<a class="tile tile--soft" href="build.html">' + gauge(decided / c.drafts, '#4F7A2F') + '<span class="tile__lbl">Review progress ' + tip('Drafts in the first batch that you have approved, edited or left for a human answer.') + '</span><span class="tile__sub">' + decided + ' of ' + c.drafts + ' decided · ' + c.approved + ' approved</span><span class="tile__go">→</span></a>',
    '<a class="tile ' + (S.warn ? 'tile--warn' : 'tile--ok') + '" href="sources.html"><span class="tile__tag">' + (S.warn ? S.warn + ' need' + (S.warn === 1 ? 's' : '') + ' attention' : 'Healthy') + '</span><span class="tile__lbl">Sources ' + tip('Uploaded documents plus the apps lojo reads: Website, Notion, Gmail and ZIWO calls.') + '</span><span class="tile__val">' + S.sources + '</span><span class="tile__sub">connected · ' + S.passages.toLocaleString('en-GB') + ' passages</span></a>',
    '<a class="tile' + (c.needCall ? ' tile--warn' : '') + '" href="' + (c.needCall ? 'build.html?tab=needs&kind=triage' : 'build.html') + '">' + (c.needCall ? '<span class="tile__tag">' + c.needCall + ' need your call</span>' : '') + '<span class="tile__lbl">Questions ' + tip('Questions your documents answer, found by the agent, plus the ones you added.') + '</span><span class="tile__val">' + c.questions + '</span><span class="tile__sub">' + (c.questions - yours) + ' found · ' + yours + ' from you</span></a>',
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
// first visit: explain the loop with a short tour of this page
const TOUR = [
  { kicker: 'Welcome to lojo', title: 'Your company’s answers, kept true', body: 'lojo reads what your company already knows, drafts the answers people keep asking for, and only shares an answer once <b>a person has approved it</b>.<div class="tour-loop"><span>Sources</span><em>→</em><span>Insights</span><em>→</em><span class="you">You approve</span><em>→</em><span>Ask lojo</span></div>', cta: 'Show me around' },
  { el: '.side nav', side: 'right', kicker: 'The loop', title: 'Four stages, top to bottom', body: '<b>Sources</b>: documents and apps lojo reads. <b>Insights</b>: questions and gaps it finds. <b>Build</b>: drafts you approve, edit or reject. <b>Distribute</b>: where approved answers go. <b>Knowledge</b> keeps them all with their evidence.' },
  { el: '#loopBtn', kicker: 'Where you are', title: 'Your loop at a glance', body: 'This shows which stage needs you now and how many answers are approved. Click it to see the whole loop.' },
  { el: '.next', kicker: 'Start here', title: 'The one thing to do next', body: 'Right now that’s reviewing drafts. Each draft shows its sources. Approve it, fix it, or reject it with a reason and lojo writes it again.' },
  { el: '#today', kicker: 'Your knowledge', title: 'What lojo knows today', body: 'Your sources, the questions found in them, gaps nobody has explained yet, and how far the review has got. Hover the <b>i</b> for what each means.' },
  { el: 'section[aria-labelledby="agH"]', kicker: 'Agents', title: 'The agents doing the work', body: 'Each stage has agents that read, find questions, draft and answer. They never publish on their own: everything waits for a person.' },
  { el: '#fab', side: 'left', pad: 6, radius: 999, kicker: 'Ask lojo', title: 'Ask anything, any time', body: 'Ask lojo answers only from approved answers and shows where each one came from. Open it with <b>⌘K</b>, or drop a document on any page to check it.', cta: 'Start reviewing' },
];
// shown when you land on the dashboard: once per visit (sign-in session), and whenever ?tour=1
const startTour = () => runTour(TOUR, (done) => { try { sessionStorage.setItem('lojo-toured', '1'); } catch (e) {} if (done) location.href = 'build.html'; });
// lojo support in a company's workspace never gets the welcome tour
let toured = null; try { toured = sessionStorage.getItem('lojo-toured') || sessionStorage.getItem('lojo-imp'); } catch (e) {}
if (new URLSearchParams(location.search).get('tour') || !toured) setTimeout(startTour, 700);
// already here: start it in place
document.addEventListener('click', (e) => { const a = e.target.closest('#tourAgain'); if (!a) return; e.preventDefault(); const p = $('mePop'); if (p) p.hidden = true; startTour(); });
render();
""")

# ============================================================ DOCUMENTS
DOCUMENTS = dict(
  active='documents', title='Sources',
  css=r"""
  /* drop zone: a hoop appears while dragging; dropping shoots a ball through it */
  .drop{position:relative;overflow:hidden}
  .hoop{position:absolute;top:10px;right:22px;width:64px;overflow:visible;height:92px;opacity:0;transform:translateY(-8px) scale(.9);transition:opacity .2s ease,transform .25s ease;pointer-events:none}
  .drop.is-over .hoop,.drop.is-shot .hoop{opacity:1;transform:none}
  .hoop__board{position:absolute;top:0;left:0;width:64px;height:56px;fill:#fff;stroke:var(--line-2);stroke-width:2}
  .hoop__board rect:last-child{fill:none;stroke:var(--rose)}
  .hoop__rim{position:absolute;top:40px;left:12px;width:40px;height:6px;border-radius:3px;background:#E8743B;z-index:2}
  .hoop__net{position:absolute;top:44px;left:12px;width:40px;height:26px;fill:none;stroke:rgba(36,26,20,.35);stroke-width:1.4;transform-origin:top center}
  .ball{position:absolute;top:0;left:20px;width:26px;height:26px;opacity:0;z-index:1}
  .ball svg{width:100%;height:100%;fill:#F28C38;stroke:#7A3410;stroke-width:1.3}
  .swish{position:absolute;top:36px;right:68px;left:auto;transform:none;font-family:var(--display);font-weight:800;font-size:.8rem;color:var(--rose);white-space:nowrap;opacity:0}
  .drop.is-over .ball{opacity:1;top:-30px;left:-110px;animation:bob 1s ease-in-out infinite}
  .drop.is-shot .ball{animation:shoot 1.1s cubic-bezier(.3,.7,.4,1) forwards}
  .drop.is-shot .hoop__net{animation:netsw .5s ease .62s}
  .drop.is-shot .swish{animation:swish 1s ease .7s forwards}
  @keyframes bob{50%{transform:translateY(-6px) rotate(20deg)}}
  @keyframes shoot{
    0%{opacity:1;left:-150px;top:80px;transform:rotate(0)}
    45%{left:-40px;top:-60px;transform:rotate(240deg)}
    70%{left:19px;top:18px;transform:rotate(360deg)}
    85%{left:19px;top:52px;opacity:1}
    100%{left:19px;top:96px;opacity:0;transform:rotate(420deg)}}
  @keyframes netsw{40%{transform:scaleY(1.35)}100%{transform:none}}
  @keyframes swish{0%{opacity:0;transform:translateY(6px)}30%{opacity:1;transform:none}100%{opacity:0;transform:translateY(-8px)}}
  @media (prefers-reduced-motion:reduce){.drop.is-over .ball{animation:none}}

  #logsBtn{gap:8px}
  .logs__n{height:20px;padding:0 8px;border-radius:999px;background:rgba(198,69,69,.12);color:var(--error);font-size:.72rem;font-weight:700;display:inline-grid;place-items:center}

  .dvdlg{width:calc(100vw - 32px);height:calc(100vh - 32px);max-width:none;max-height:none;margin:16px;padding:0;border:0;border-radius:18px;background:var(--panel);color:var(--ink);flex-direction:column;box-shadow:0 40px 90px -30px rgba(36,26,20,.5)}
  .dvdlg[open]{display:flex}
  .dvdlg::backdrop{background:rgba(36,26,20,.35)}
  .dv__h{display:flex;align-items:center;gap:12px;padding:18px 22px;border-bottom:1px solid var(--line)}
  .dv__h h2{margin:0;font-family:var(--display);font-size:1.2rem}
  .dv__h .spacer{flex:1}
  .dv__bar{display:flex;align-items:center;gap:10px;flex-wrap:wrap;padding:12px 22px;border-bottom:1px solid var(--line)}
  .dv__q{position:relative;flex:1;min-width:220px;max-width:420px}
  .dv__q svg{position:absolute;left:11px;top:50%;width:16px;height:16px;transform:translateY(-50%);fill:none;stroke:var(--muted);stroke-width:2;stroke-linecap:round}
  .dv__q input{width:100%;height:36px;padding:0 12px 0 34px;border-radius:10px;border:1px solid var(--line-2);font:inherit;font-size:.88rem;background:var(--panel)}
  .dv__st{display:flex;gap:6px;flex-wrap:wrap}
  .dv__chip{height:32px;padding:0 12px;border-radius:999px;border:1px solid var(--line-2);background:var(--panel);font:inherit;font-size:.8rem;font-weight:600;cursor:pointer;display:inline-flex;align-items:center;gap:6px}
  .dv__chip span{color:var(--muted);font-weight:700}
  .dv__chip.is-bad{color:var(--error);border-color:rgba(198,69,69,.35)}
  .dv__chip[aria-pressed="true"]{background:var(--ink);border-color:var(--ink);color:#fff}
  .dv__chip[aria-pressed="true"] span{color:rgba(255,255,255,.7)}
  .dv__type{width:auto;height:36px}
  .dv__body{flex:1;overflow:auto}
  .dv__body thead th{position:sticky;top:0;background:var(--panel);z-index:1}
  .dv__empty{padding:40px;text-align:center;color:var(--muted)}

  .zform{display:grid;gap:14px}
  .zform__h{display:flex;align-items:center;gap:12px}
  .zform__ic{width:40px;height:40px;border-radius:11px;display:grid;place-items:center;background:rgba(106,63,212,.1);color:#6A3FD4}
  .zform__ic svg{width:22px;height:22px}
  .zform__ic--w{background:rgba(62,111,166,.1);color:var(--info)}
  .wrow{display:flex;gap:10px}
  .wrow .text{flex:1;min-width:0}
  .wrow .btn{flex:none}
  .text.is-bad{border-color:var(--error)}
  .wprog{display:grid;gap:6px}
  .wprog .gm-bar{height:4px;border-radius:4px;background:var(--bg-soft);overflow:hidden}
  .wprog .gm-bar i{display:block;height:100%;background:var(--brand-gradient);transition:width .3s ease}
  .wprog .sub{margin:0}
  .zform__h b{display:block;font-size:1rem}
  .zform__h span{font-size:.82rem;color:var(--muted)}
  .zform .fld{display:grid;gap:6px}
  .zform .fld label{font-size:.84rem;font-weight:600}
  .zform .fhint{font-size:.78rem;color:var(--muted)}
  .zok{display:flex;gap:12px;align-items:flex-start;padding:14px 16px;border-radius:12px;background:var(--bg-soft);font-size:.86rem;line-height:1.5;cursor:pointer}
  .zok input{width:18px;height:18px;margin:2px 0 0;flex:none;accent-color:var(--rose)}
  .zform__f{display:flex;gap:10px;align-items:center}

  .gm-h{display:flex;align-items:center;justify-content:space-between;margin-bottom:12px}
  .gm-h h3{margin:0}
  .gm-card{border:1px solid var(--line);border-radius:16px;padding:16px 18px;display:grid;gap:12px}
  .gm-card + .gm-card{margin-top:10px}
  .gm-top{display:flex;align-items:center;gap:10px;flex-wrap:wrap}
  .gm-av{width:40px;height:40px;border-radius:11px;flex:none;display:grid;place-items:center;background:#D93025;color:#fff;font-weight:800}
  .gm-id{flex:1;min-width:180px}
  .gm-id b{display:block;font-size:.95rem}
  .gm-id span{font-size:.82rem;color:var(--muted)}
  .gm-top .btn.is-on{border-color:var(--ink)}
  .gm-top .btn .spin,.gm-foot .btn .spin{width:12px;height:12px;margin-right:6px}
  .gm-bar{height:4px;border-radius:4px;background:var(--bg-soft);overflow:hidden}
  .gm-bar i{display:block;height:100%;background:var(--brand-gradient);transition:width .4s ease}
  .gm-note{margin:0;color:var(--muted);font-size:.86rem}
  .gm-labels{display:grid;gap:8px}
  .gm-l{display:flex;align-items:center;gap:12px;padding:12px 14px;border:1px solid var(--line-2);border-radius:12px;cursor:pointer;font-size:.92rem}
  .gm-l.is-on{border-color:rgba(232,93,117,.35);background:#FFF8F6}
  .gm-l input{width:18px;height:18px;margin:0;accent-color:var(--rose);cursor:pointer}
  .gm-l span{flex:1}
  .gm-l em{font-style:normal;font-size:.8rem;color:var(--muted);display:inline-flex;align-items:center;gap:6px}
  .gm-l em .spin{width:12px;height:12px}
  .gm-run{color:var(--info)!important;font-weight:600}
  .gm-ok{color:var(--success)!important;font-weight:600}
  .gm-foot{display:flex;align-items:center;gap:12px}
  :root[data-theme="dark"] .gm-l.is-on{background:rgba(232,93,117,.08)}

  .forgap{display:flex;align-items:center;gap:12px;margin:0 0 14px;padding:12px 14px;border-radius:14px;border:1px solid rgba(47,116,232,.3);background:rgba(47,116,232,.06)}
  .forgap__ic{width:34px;height:34px;border-radius:50%;flex:none;display:grid;place-items:center;background:rgba(47,116,232,.12)}
  .forgap > div{flex:1;min-width:0}
  .forgap small{display:block;font-size:.66rem;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:#2F74E8}
  .forgap b{display:block;font-size:.92rem}
  .forgap span{font-size:.82rem;color:var(--muted)}

  .soon{cursor:not-allowed!important;opacity:.55;background:var(--bg-soft)!important;box-shadow:none!important;transform:none!important}
  .soon:hover{border-color:var(--line-2)!important}
  .soon .logo,.soon .tile,.soon .mono{filter:grayscale(1)}
  .soon__tag{display:inline-block;margin-left:0;font-style:normal;height:18px;padding:0 7px;border-radius:999px;background:rgba(36,26,20,.07);color:var(--muted);font-size:.58rem;font-weight:800;letter-spacing:.08em;text-transform:uppercase;vertical-align:1px;line-height:18px}
  .about{position:relative;display:inline-flex}
  .aboutpop{position:absolute;top:calc(100% + 8px);right:0;z-index:30;width:300px;padding:14px 16px;border-radius:14px;border:1px solid var(--line);background:var(--panel);box-shadow:0 24px 50px -24px rgba(36,26,20,.45);opacity:0;pointer-events:none;transform:translateY(4px);transition:opacity .15s ease,transform .15s ease}
  .about.is-open .aboutpop,.about:hover .aboutpop{opacity:1;pointer-events:auto;transform:none}
  .aboutpop dl{margin:0;display:grid;gap:10px}
  .aboutpop dt{font-size:.66rem;font-weight:800;letter-spacing:.1em;text-transform:uppercase;color:var(--ink)}
  .aboutpop dd{color:var(--muted)!important}
  .aboutpop dd{margin:2px 0 0;font-size:.84rem;color:var(--ink)}
  .srcsum{margin:-8px 0 16px;font-size:.86rem;color:var(--muted)}
  .srcsum b{color:var(--ink)}
  .srcwrap{display:grid;grid-template-columns:320px minmax(0,1fr);gap:18px;align-items:start}
  .srclist{position:sticky;top:96px;display:flex;flex-direction:column;height:calc(100vh - 166px);overflow:hidden}
  .srclist__h{padding:16px 16px 12px;border-bottom:1px solid var(--line)}
  .srclist__h h2{margin:0 0 10px;font-family:var(--display);font-weight:700;font-size:1.05rem}
  .srcq{display:flex;align-items:center;gap:8px;height:38px;padding:0 12px;border-radius:10px;border:1px solid var(--line-2);background:var(--panel)}
  .srcq:focus-within{border-color:var(--rose)}
  .srcq svg{width:16px;height:16px;fill:none;stroke:var(--muted);stroke-width:1.8}
  .srcq input{border:0;outline:0;background:none;flex:1;font:inherit;font-size:.86rem}
  .srclist__b{overflow:auto;padding:6px 8px}
  .sgrp{display:flex;justify-content:space-between;margin:12px 8px 6px;font-size:.64rem;font-weight:800;letter-spacing:.12em;text-transform:uppercase;color:var(--muted)}
  .sitem{display:grid;grid-template-columns:38px minmax(0,1fr) 10px;gap:12px;align-items:center;width:100%;padding:10px;border:1px solid transparent;border-radius:12px;background:none;text-align:left;font:inherit;color:inherit;cursor:pointer}
  .sitem:hover{background:var(--bg-soft)}
  .sitem.is-sel{border-color:rgba(232,93,117,.4);background:linear-gradient(90deg,rgba(232,93,117,.06),transparent);box-shadow:inset 3px 0 0 var(--rose)}
  .sitem b{display:block;font-size:.88rem;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
  .sitem span{display:block;font-size:.74rem;color:var(--muted);white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
  .sitem .sico{display:grid;place-items:center;white-space:normal;overflow:visible}
  .sitem .sico svg{display:block}
  .sitem .dot{width:9px;height:9px;border-radius:50%;background:var(--success)}
  .sitem .dot.warn{background:#C9A24A}
  .sico{width:38px;height:38px;border-radius:10px;display:grid;place-items:center;background:var(--panel);border:1px solid var(--line)}
  .sico svg{width:19px;height:19px}
  .sico.doc{background:rgba(232,93,117,.08);color:#C7385B;border-color:transparent}
  .sico.doc svg{fill:none;stroke:currentColor;stroke-width:1.8}
  .srclist__f{padding:12px;border-top:1px solid var(--line)}
  .srcdet{display:grid;grid-template-columns:minmax(0,1fr);gap:14px;min-width:0;align-content:start}
  /* the page stays put: the source list is fixed and the right side scrolls on its own */
  @media (min-width:1101px){.wrap{padding-bottom:0}.srcdet{position:sticky;top:96px;height:calc(100vh - 166px);overflow:auto;overscroll-behavior:contain;padding:0 4px 20px 0;margin-right:-4px}}
  .srcdet > *{min-width:0}
  .srcwrap > *{min-width:0}
  .sh__top{flex-wrap:wrap}
  .dtable .dname .dn{min-width:140px}
  #uploadBody .dtable th:nth-child(2),#uploadBody .dtable td:nth-child(2){display:none}
  #uploadBody .dtable td,#uploadBody .dtable th{padding-left:14px;padding-right:14px}
  #uploadBody .dtable .num{width:84px}
  .srchead{padding:20px 22px;background:radial-gradient(120% 140% at 100% 0%,#FFF1EC,var(--panel) 60%)}
  .sh__top{display:flex;align-items:flex-start;gap:14px}
  .sh__top .sico{width:52px;height:52px;border-radius:14px}
  .sh__top .sico svg{width:24px;height:24px}
  .sh__top h2{margin:0;font-family:var(--display);font-weight:700;font-size:1.5rem;letter-spacing:-.01em}
  .sh__top p{margin:2px 0 0;color:var(--muted);font-size:.86rem}
  .sh__top .spacer{flex:1}
  .sh__top .btn{height:36px}
  .admin{display:flex;align-items:center;gap:10px;flex-wrap:wrap;margin:16px 0 12px;padding:12px 14px;border:1px solid var(--line);border-radius:12px;background:var(--panel);font-size:.84rem}
  .admin .ava3d,.admin .ava3d > svg{width:28px;height:28px}
  .admin a{font-weight:700;color:var(--ink);text-decoration:underline;text-underline-offset:3px}
  .admin em{font-style:normal;color:var(--muted)}
  .health{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:10px}
  .hcard{padding:12px 14px;border:1px solid var(--line);border-radius:12px;background:var(--panel)}
  .hcard small{display:flex;justify-content:space-between;align-items:center;font-size:.62rem;font-weight:800;letter-spacing:.12em;text-transform:uppercase;color:var(--muted)}
  .hcard small i{width:8px;height:8px;border-radius:50%;background:var(--success)}
  .hcard small i.warn{background:#C9A24A}
  .hcard b{display:block;margin:4px 0 2px;font-size:.98rem}
  .hcard span{font-size:.78rem;color:var(--muted)}
  .supply{display:grid;grid-template-columns:1fr 1fr;gap:18px;margin-top:12px;padding:14px 16px;border:1px solid var(--line);border-radius:12px;background:var(--panel)}
  .supply h4{margin:0 0 4px;font-size:.88rem}
  .supply p{margin:0;font-size:.82rem;color:var(--muted)}
  .supply .note{grid-column:1/-1;padding-top:10px;border-top:1px solid var(--line);font-size:.78rem;color:var(--muted)}
  #uploadBody .scope{margin-bottom:14px}
  #uploadBody .dcard{margin-top:0}
  .dcard .card__head .spacer{flex:1}
  .srcitems{padding:18px 20px}
  .srcitems h3{display:flex;align-items:center;gap:10px;margin:0 0 12px;font-family:var(--display);font-size:1.05rem}
  .srcitems h3 .spacer{flex:1}
  .sirow{display:grid;grid-template-columns:minmax(0,1fr) auto auto;gap:14px;align-items:center;padding:10px 0;border-top:1px solid var(--line);font-size:.86rem}
  .sirow:first-of-type{border-top:0}
  .sirow em{font-style:normal;color:var(--muted);font-size:.78rem}
  .addsrc{border:0;padding:0;border-radius:20px;width:min(760px,calc(100vw - 32px));max-height:calc(100vh - 40px);box-shadow:0 40px 90px -30px rgba(36,26,20,.5);color:var(--ink);background:var(--panel)}
  .addsrc::backdrop{background:rgba(36,26,20,.35);backdrop-filter:blur(2px)}
  .addsrc[open]{display:block;padding:22px 24px 24px;animation:fadeIn .2s ease}
  .addsrc__h{display:flex;align-items:flex-start;gap:12px;margin-bottom:16px}
  .addsrc__h > div{flex:1}
  .addsrc__h h2{margin:0;font-family:var(--display);font-weight:700;font-size:1.3rem}
  @media (max-width:1100px){.srcwrap{grid-template-columns:1fr}.srclist{position:static;max-height:none;height:auto}.health,.supply{grid-template-columns:1fr}}
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
  .uperr{margin:0 0 16px;padding:14px 16px;border-radius:14px;border:1px solid rgba(198,69,69,.3);background:rgba(198,69,69,.05)}
  .uperr__h{display:flex;align-items:center;gap:10px;font-weight:700;font-size:.9rem;color:var(--error)}
  .uperr__h button{margin-left:auto}
  .uperr ul{list-style:none;margin:10px 0 0;padding:0;display:grid;gap:6px}
  .uperr li{display:grid;grid-template-columns:auto 1fr;gap:10px;font-size:.84rem;align-items:baseline}
  .uperr li b{font-weight:600}
  .uperr li span{color:var(--muted)}
  .synced{display:grid;gap:8px;margin-top:16px}
  .synced .file{grid-template-columns:36px minmax(0,1fr) auto auto}
  @media (max-width:760px){.scope-detail{grid-template-columns:1fr}.fdetail{padding-left:0}}
""",
  body=r"""
    <div class="head">
      <div>
        <p class="label">01 Source</p>
        <h1>Sources</h1>
        <p>Select a source to see its health, what it gives lojo, and the one thing to do next.</p>
      </div>
      <span class="spacer"></span>
      <button class="btn btn--secondary" id="logsBtn" type="button"><svg viewBox="0 0 24 24" style="width:16px;height:16px;fill:none;stroke:currentColor;stroke-width:1.9;stroke-linecap:round;stroke-linejoin:round"><path d="M8 6h13M8 12h13M8 18h13M3 6h.01M3 12h.01M3 18h.01"/></svg>All logs <span class="logs__n" id="logsN"></span></button>
      <button class="btn btn--grad" id="addSrc" type="button"><svg class="i" viewBox="0 0 24 24" style="width:16px;height:16px;fill:none;stroke:currentColor;stroke-width:2.2;stroke-linecap:round"><path d="M12 5v14M5 12h14"/></svg>Add source</button>
    </div>
    <p class="srcsum" id="srcSum"></p>

    <div class="srcwrap">
      <aside class="card srclist">
        <div class="srclist__h"><h2>Connected sources</h2>
          <label class="srcq"><svg viewBox="0 0 24 24"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></svg><input id="srcQ" placeholder="Search sources…" aria-label="Search sources"></label></div>
        <div class="srclist__b" id="srcList"></div>
      </aside>

      <section class="srcdet" id="srcDet" aria-live="polite">
        <div class="card srchead" id="srcHead"></div>
        <div id="uploadBody">
          <div class="forgap" id="forGap" hidden></div>
          <section class="scope" id="scope">
            <span class="ok">✓</span>
            <div><b id="scopeTitle">Data in scope, signed off</b><span class="sub" id="scopeSub"></span></div>
            <button class="btn btn--ghost btn--sm" id="scopeToggle" aria-expanded="false">What’s in scope</button>
            <div class="scope-detail" id="scopeDetail" hidden>
              <div><h4>In scope</h4><ul><li>The documents on this page</li><li>Your current help pages</li><li>Questions you add</li></ul></div>
              <div><h4>Out of scope</h4><ul><li>Customer records and tickets</li><li>Mail and call recordings</li><li>Anything not listed here</li></ul></div>
              <div><h4>Good to know</h4><ul><li>Personal details are not removed automatically</li><li>Everyone who signs in can see everything</li><li>Data sits on one lojo-run server</li></ul></div>
            </div>
          </section>
          <section class="card dcard" aria-labelledby="docH">
            <div class="card__head"><h2 id="docH">Everything lojo reads</h2><span class="sub" id="docMeta"></span><span class="spacer"></span><button class="btn btn--ghost btn--sm" id="dvOpen" type="button">View all</button><button class="btn btn--secondary btn--sm" id="addDocs" type="button">Upload documents</button></div>
            <div class="dscroll"><table class="dtable">
              <thead><tr><th>Item</th><th class="num">Pages</th><th class="num">Passages</th><th class="num">Questions</th><th>Status</th><th class="tacts"><span class="sr-only">Actions</span></th></tr></thead>
              <tbody id="docRows"></tbody>
            </table></div>
          </section>
        </div>
        <div class="card srcitems" id="appBody" hidden></div>
        <dialog class="dvdlg" id="dvDlg" aria-labelledby="dvH">
          <div class="dv__h"><div><h2 id="dvH">Everything lojo reads</h2><span class="sub" id="dvMeta"></span></div><span class="spacer"></span><button class="btn btn--ghost btn--sm" type="button" data-dvx aria-label="Close">Close ×</button></div>
          <div class="dv__bar">
            <label class="dv__q"><svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></svg><input id="dvQ" type="search" placeholder="Search everything lojo reads" aria-label="Search everything lojo reads"></label>
            <div class="dv__st" id="dvSt" role="group" aria-label="Status"></div>
            <select class="text dv__type" id="dvType" aria-label="Source"></select>
          </div>
          <div class="dv__body"><table class="dtable"><thead><tr><th>Item</th><th class="num">Pages</th><th class="num">Passages</th><th class="num">Questions</th><th>Status</th><th class="tacts"><span class="sr-only">Actions</span></th></tr></thead><tbody id="dvRows"></tbody></table>
            <p class="dv__empty" id="dvEmpty" hidden>Nothing matches. Try other words or another filter.</p></div>
        </dialog>
      </section>
    </div>

    <dialog class="addsrc" id="addDlg" aria-labelledby="addH">
      <div class="addsrc__h"><div><h2 id="addH">Add a source</h2><p class="sub">Upload documents or connect an app. lojo only reads; it never edits your files.</p></div><button class="hbtn" id="addX" type="button" aria-label="Close"><svg viewBox="0 0 24 24"><path d="M18 6 6 18M6 6l12 12"/></svg></button></div>
      <div class="ptabs" role="tablist" aria-label="Source type">
        <button class="ptab" role="tab" data-tab="docs" aria-selected="true"><svg viewBox="0 0 24 24"><path d="M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8z"/><path d="M14 3v5h5"/></svg>Documents <span class="n" id="nDocs">0</span></button>
        <button class="ptab" role="tab" data-tab="connect" aria-selected="false"><svg viewBox="0 0 24 24"><path d="M9 7V3M15 7V3M7 7h10v4a5 5 0 0 1-10 0zM12 16v5"/></svg>Connect <span class="n" id="nConn">0</span></button>
      </div>
      <section id="tabDocs">
        <section class="uperr" id="upErr" hidden role="alert"></section>
        <label class="drop" id="drop">
          <span class="hoop" aria-hidden="true">
            <svg class="hoop__board" viewBox="0 0 64 56"><rect x="6" y="2" width="52" height="34" rx="4"/><rect x="22" y="12" width="20" height="14" rx="2"/></svg>
            <span class="hoop__rim"></span>
            <svg class="hoop__net" viewBox="0 0 40 26"><path d="M2 2l6 22M12 2l3 22M20 2v22M28 2l-3 22M38 2l-6 22M4 10h32M7 18h26"/></svg>
            <span class="ball"><svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><path d="M2 12h20M12 2v20M5 5c3 3 3 11 0 14M19 5c-3 3-3 11 0 14"/></svg></span>
            <span class="swish">Swish!</span>
          </span>
          <span class="ico"><svg viewBox="0 0 24 24"><path d="M12 16V4M7 9l5-5 5 5"/><path d="M4 16v3a1 1 0 0 0 1 1h14a1 1 0 0 0 1-1v-3"/></svg></span>
          <strong>Drop files here, or browse</strong>
          <p class="hint">PDF, DOCX, Markdown or TXT · up to 25 MB each</p>
          <input type="file" id="fileInput" multiple hidden>
          <span class="row"><span class="btn btn--secondary btn--sm">Browse files</span></span>
        </label>
      </section>
      <section id="tabConnect" hidden>
        <div class="apps" id="apps"></div>
        <form class="zform" id="wForm" hidden novalidate>
          <div class="zform__h"><span class="zform__ic zform__ic--w"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3a14 14 0 0 1 0 18M12 3a14 14 0 0 0 0 18"/></svg></span><div><b>Connect a website</b><span>Public pages, read the same way as documents.</span></div></div>
          <div class="fld"><label for="wUrl">Website address</label>
            <div class="wrow"><input class="text" id="wUrl" type="url" placeholder="https://help.yourcompany.com" autocomplete="off"><button class="btn btn--primary" type="submit" id="wGo" disabled>Read the site</button></div>
            <span class="fhint" id="wHint">lojo reads the public pages under this address, up to 200. It never signs in.</span><span class="ferr" id="wErr"></span></div>
          <div class="wprog" id="wProg" hidden></div>
          <div class="zform__f"><button class="btn btn--ghost" type="button" id="wCancel">Cancel</button></div>
        </form>
        <form class="zform" id="zForm" hidden novalidate>
          <div class="zform__h"><span class="zform__ic"><svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"></svg></span><div><b>Connect ZIWO</b><span>Calls and their transcripts. lojo only reads.</span></div></div>
          <div class="fld"><label for="zAcc">ZIWO account name</label><input class="text" id="zAcc" autocomplete="off"><span class="fhint">The name of your account in ZIWO, as your ZIWO admin gives it.</span><span class="ferr"></span></div>
          <div class="fld"><label for="zKey">API key</label><input class="text" id="zKey" type="password" autocomplete="off"><span class="ferr"></span></div>
          <label class="zok"><input type="checkbox" id="zOk"><span>On behalf of the <b>“Oslo”</b> workspace, I confirm that we may share these call recordings with lojo, that callers were told their calls are recorded, and that we are responsible for this personal data.</span></label>
          <div class="zform__f"><button class="btn btn--primary" type="submit" id="zGo" disabled>Connect ZIWO</button><button class="btn btn--ghost" type="button" id="zCancel">Cancel</button></div>
        </form>
        <div class="synced" id="synced" hidden></div>
      </section>
    </dialog>
""",
  js=r"""
let open = null;
const extra = [];
const APPS = [
  { id: 'website', name: 'Website', kind: 'Web parsing', mono: 'W', color: '#3E6FA6', n: 3 },
  { id: 'notion', name: 'Notion', kind: 'Pages & wikis', mono: 'N', color: 'var(--ink)', n: 5 },
  { id: 'gmail', name: 'Gmail', kind: 'Email', mono: 'M', color: '#D93025', n: 3 },
  { id: 'ziwo', name: 'ZIWO', kind: 'Calls & transcripts', mono: 'Z', color: '#AC3378', n: 2 },
  { id: 'slack', name: 'Slack', kind: 'Channels & threads', mono: 'S', color: '#4A154B', n: 3 },
  { id: 'gdrive', soon: true, name: 'Google Drive', kind: 'Docs & files', mono: 'GD', color: '#1A73E8', n: 6 },
  { id: 'sharepoint', soon: true, name: 'SharePoint', kind: 'Sites & libraries', mono: 'SP', color: '#036C70', n: 5 },
  { id: 'confluence', soon: true, name: 'Confluence', kind: 'Spaces', mono: 'C', color: '#0C66E4', n: 4 },
  { id: 'aircall', soon: true, name: 'Aircall', kind: 'Calls', mono: 'A', color: '#00B388', n: 2 },
  { id: 'gsheets', soon: true, name: 'Google Sheets', kind: 'Spreadsheets', mono: 'GS', color: '#188038', n: 2 },
];
const LOGO = {"slack": "<g transform=\"translate(.3 .3) scale(.184)\"><path d=\"M27.2 80c0 7.3-5.9 13.2-13.2 13.2C6.7 93.2.8 87.3.8 80c0-7.3 5.9-13.2 13.2-13.2h13.2V80zm6.6 0c0-7.3 5.9-13.2 13.2-13.2 7.3 0 13.2 5.9 13.2 13.2v33c0 7.3-5.9 13.2-13.2 13.2-7.3 0-13.2-5.9-13.2-13.2V80z\" fill=\"#E01E5A\"/><path d=\"M47 27c-7.3 0-13.2-5.9-13.2-13.2C33.8 6.5 39.7.6 47 .6c7.3 0 13.2 5.9 13.2 13.2V27H47zm0 6.7c7.3 0 13.2 5.9 13.2 13.2 0 7.3-5.9 13.2-13.2 13.2H13.9C6.6 60.1.7 54.2.7 46.9c0-7.3 5.9-13.2 13.2-13.2H47z\" fill=\"#36C5F0\"/><path d=\"M99.9 46.9c0-7.3 5.9-13.2 13.2-13.2 7.3 0 13.2 5.9 13.2 13.2 0 7.3-5.9 13.2-13.2 13.2H99.9V46.9zm-6.6 0c0 7.3-5.9 13.2-13.2 13.2-7.3 0-13.2-5.9-13.2-13.2V13.8C66.9 6.5 72.8.6 80.1.6c7.3 0 13.2 5.9 13.2 13.2v33.1z\" fill=\"#2EB67D\"/><path d=\"M80.1 99.8c7.3 0 13.2 5.9 13.2 13.2 0 7.3-5.9 13.2-13.2 13.2-7.3 0-13.2-5.9-13.2-13.2V99.8h13.2zm0-6.6c-7.3 0-13.2-5.9-13.2-13.2 0-7.3 5.9-13.2 13.2-13.2h33.1c7.3 0 13.2 5.9 13.2 13.2 0 7.3-5.9 13.2-13.2 13.2H80.1z\" fill=\"#ECB22E\"/></g>", "ziwo": "<g transform=\"translate(-47.8 -4.9) scale(.6)\"><path d=\"M95.0623 48C95.0623 48 94.4942 47.3268 94.2984 47.0929C92.9783 45.5054 91.5627 43.9561 90.1876 42.4139C89.8391 42.0224 89.4977 41.6428 89.1563 41.2633C88.5452 40.5853 87.9126 39.8811 87.2275 39.0981C82.835 34.3713 81.0756 29.647 81.6915 24.2304C82.6965 15.3977 90.2163 8.49379 99.1803 8.17151C100.522 8.12377 101.873 8.22642 103.196 8.48185C109.474 9.6874 113.831 13.3327 116.146 19.3199C117.662 23.2373 117.65 27.2956 116.115 31.3825C114.174 36.5437 110.555 40.1962 105.356 42.2373C103.494 42.9678 101.558 43.3736 99.6005 43.4452C98.2899 43.4929 96.9411 43.3903 95.5923 43.1396C95.5064 43.1229 95.4395 43.1182 95.3799 43.1205C95.2772 43.1253 95.196 43.1563 95.1411 43.2184C95.0552 43.3115 95.0433 43.4428 95.0528 43.6266C95.0814 44.2234 95.0623 48.0048 95.0623 48.0048V48ZM106.681 30.3202C106.392 31.3563 105.783 32.2324 104.819 32.9987C103.437 34.0968 101.747 34.7223 99.7938 34.8583C99.6482 34.8679 99.505 34.875 99.3617 34.8822C97.1798 34.961 95.3512 34.4549 93.778 33.3353C92.7443 32.6 92.1046 31.7048 91.8229 30.5948C91.6629 29.9645 91.1736 29.5706 90.5791 29.5921C90.4956 29.5945 90.4096 29.6064 90.3237 29.6255C89.6362 29.7855 89.2327 30.4444 89.3807 31.1629C89.6171 32.2968 90.1685 33.3329 91.0184 34.2472C92.594 35.9374 94.6398 36.9281 97.2801 37.2718C98.0249 37.3697 98.7649 37.4055 99.4811 37.3793C101.298 37.3148 103.012 36.8684 104.721 36.0161C106.817 34.9085 108.192 33.4523 108.923 31.5616C108.989 31.3897 109.049 31.2059 109.102 31.0149C109.319 30.2367 109.006 29.5754 108.326 29.3677C108.183 29.3247 108.037 29.3056 107.891 29.3104C107.321 29.3319 106.843 29.7282 106.679 30.3226L106.681 30.3202Z\"/></g>", "notion": "<path d=\"M4.459 4.208c.746.606 1.026.56 2.428.466l13.215-.793c.28 0 .047-.28-.046-.326L17.86 1.968c-.42-.326-.981-.7-2.055-.607L3.01 2.295c-.466.046-.56.28-.374.466zm.793 3.08v13.904c0 .747.373 1.027 1.214.98l14.523-.84c.841-.046.935-.56.935-1.167V6.354c0-.606-.233-.933-.748-.887l-15.177.887c-.56.047-.747.327-.747.933zm14.337.745c.093.42 0 .84-.42.888l-.7.14v10.264c-.608.327-1.168.514-1.635.514-.748 0-.935-.234-1.495-.933l-4.577-7.186v6.952L12.21 19s0 .84-1.168.84l-3.222.186c-.093-.186 0-.653.327-.746l.84-.233V9.854L7.822 9.76c-.094-.42.14-1.026.793-1.073l3.456-.233 4.764 7.279v-6.44l-1.215-.139c-.093-.514.28-.887.747-.933zM1.936 1.035l13.31-.98c1.634-.14 2.055-.047 3.082.7l4.249 2.986c.7.513.934.653.934 1.213v16.378c0 1.026-.373 1.634-1.68 1.726l-15.458.934c-.98.047-1.448-.093-1.962-.747l-3.129-4.06c-.56-.747-.793-1.306-.793-1.96V2.667c0-.839.374-1.54 1.447-1.632z\"/>", "gdrive": "<path d=\"M12.01 1.485c-2.082 0-3.754.02-3.743.047.01.02 1.708 3.001 3.774 6.62l3.76 6.574h3.76c2.081 0 3.753-.02 3.742-.047-.005-.02-1.708-3.001-3.775-6.62l-3.76-6.574zm-4.76 1.73a789.828 789.861 0 0 0-3.63 6.319L0 15.868l1.89 3.298 1.885 3.297 3.62-6.335 3.618-6.33-1.88-3.287C8.1 4.704 7.255 3.22 7.25 3.214zm2.259 12.653-.203.348c-.114.198-.96 1.672-1.88 3.287a423.93 423.948 0 0 1-1.698 2.97c-.01.026 3.24.042 7.222.042h7.244l1.796-3.157c.992-1.734 1.85-3.23 1.906-3.323l.104-.167h-7.249z\"/>", "gsheets": "<path d=\"M11.318 12.545H7.91v-1.909h3.41v1.91zM14.728 0v6h6l-6-6zm1.363 10.636h-3.41v1.91h3.41v-1.91zm0 3.273h-3.41v1.91h3.41v-1.91zM20.727 6.5v15.864c0 .904-.732 1.636-1.636 1.636H4.909a1.636 1.636 0 0 1-1.636-1.636V1.636C3.273.732 4.005 0 4.909 0h9.318v6.5h6.5zm-3.273 2.773H6.545v7.909h10.91v-7.91zm-6.136 4.636H7.91v1.91h3.41v-1.91z\"/>", "gmail": "<path d=\"M24 5.457v13.909c0 .904-.732 1.636-1.636 1.636h-3.819V11.73L12 16.64l-6.545-4.91v9.273H1.636A1.636 1.636 0 0 1 0 19.366V5.457c0-2.023 2.309-3.178 3.927-1.964L5.455 4.64 12 9.548l6.545-4.91 1.528-1.145C21.69 2.28 24 3.434 24 5.457z\"/>", "confluence": "<path d=\"M.87 18.257c-.248.382-.53.875-.763 1.245a.764.764 0 0 0 .255 1.04l4.965 3.054a.764.764 0 0 0 1.058-.26c.199-.332.454-.763.733-1.221 1.967-3.247 3.945-2.853 7.508-1.146l4.957 2.337a.764.764 0 0 0 1.028-.382l2.364-5.346a.764.764 0 0 0-.382-1 599.851 599.851 0 0 1-4.965-2.361C10.911 10.97 5.224 11.185.87 18.257zM23.131 5.743c.249-.405.531-.875.764-1.25a.764.764 0 0 0-.256-1.034L18.675.404a.764.764 0 0 0-1.058.26c-.195.335-.451.763-.734 1.225-1.966 3.246-3.945 2.85-7.508 1.146L4.437.694a.764.764 0 0 0-1.027.382L1.046 6.422a.764.764 0 0 0 .382 1c1.039.49 3.105 1.467 4.965 2.361 6.698 3.246 12.392 3.029 16.738-4.04z\"/>", "aircall": "<path d=\"M23.451 5.906a6.978 6.978 0 0 0-5.375-5.39C16.727.204 14.508 0 12 0S7.273.204 5.924.516a6.978 6.978 0 0 0-5.375 5.39C.237 7.26.034 9.485.034 12s.203 4.74.515 6.094a6.978 6.978 0 0 0 5.375 5.39C7.273 23.796 9.492 24 12 24s4.727-.204 6.076-.516a6.978 6.978 0 0 0 5.375-5.39c.311-1.354.515-3.578.515-6.094 0-2.515-.203-4.74-.515-6.094zm-5.873 12.396l-.003.001c-.428.152-1.165.283-2.102.377l-.147.014a.444.444 0 0 1-.45-.271 1.816 1.816 0 0 0-1.296-1.074c-.351-.081-.928-.134-1.58-.134s-1.229.053-1.58.134a1.817 1.817 0 0 0-1.291 1.062.466.466 0 0 1-.471.281 8 8 0 0 0-.129-.012c-.938-.094-1.676-.224-2.105-.377l-.003-.001a.76.76 0 0 1-.492-.713c0-.032.003-.066.005-.098.073-.979.666-3.272 1.552-5.89C8.5 8.609 9.559 6.187 10.037 5.714a1.029 1.029 0 0 1 .404-.26l.004-.002c.314-.106.892-.178 1.554-.178.663 0 1.241.071 1.554.178l.005.002a1.025 1.025 0 0 1 .405.26c.478.472 1.537 2.895 2.549 5.887.886 2.617 1.479 4.91 1.552 5.89.002.032.005.066.005.098a.76.76 0 0 1-.491.713z\"/>", "sharepoint": "<path d=\"M24 13.5q0 1.242-.475 2.332-.474 1.09-1.289 1.904-.814.815-1.904 1.29-1.09.474-2.332.474-.762 0-1.523-.2-.106.997-.557 1.858-.451.862-1.154 1.494-.704.633-1.606.99-.902.358-1.91.358-1.09 0-2.045-.416-.955-.416-1.664-1.125-.709-.709-1.125-1.664Q6 19.84 6 18.75q0-.188.018-.375.017-.188.04-.375H.997q-.41 0-.703-.293T0 17.004V6.996q0-.41.293-.703T.996 6h3.54q.14-1.277.726-2.373.586-1.096 1.488-1.904Q7.652.914 8.807.457 9.96 0 11.25 0q1.395 0 2.625.533T16.02 1.98q.914.915 1.447 2.145T18 6.75q0 .188-.012.375-.011.188-.035.375 1.242 0 2.344.469 1.101.468 1.928 1.277.826.809 1.3 1.904Q24 12.246 24 13.5zm-12.75-12q-.973 0-1.857.34-.885.34-1.577.943-.691.604-1.154 1.43Q6.2 5.039 6.06 6h4.945q.41 0 .703.293t.293.703v4.945l.21-.035q.212-.75.61-1.424.399-.673.944-1.218.545-.545 1.213-.944.668-.398 1.43-.61.093-.503.093-.96 0-1.09-.416-2.045-.416-.955-1.125-1.664-.709-.709-1.664-1.125Q12.34 1.5 11.25 1.5zM6.117 15.902q.54 0 1.06-.111.522-.111.932-.37.41-.257.662-.679.252-.422.252-1.055 0-.632-.263-1.054-.264-.422-.662-.703-.399-.282-.856-.463l-.855-.34q-.399-.158-.662-.334-.264-.176-.264-.445 0-.2.14-.323.141-.123.335-.193.193-.07.404-.094.21-.023.351-.023.598 0 1.055.152.457.153.95.457V8.543q-.282-.082-.522-.14-.24-.06-.475-.1-.234-.041-.486-.059-.252-.017-.557-.017-.515 0-1.054.117-.54.117-.979.375-.44.258-.715.68-.275.421-.275 1.03 0 .598.263.997.264.398.663.68.398.28.855.474l.856.363q.398.17.662.358.263.187.263.457 0 .222-.123.351-.123.13-.31.2-.188.07-.393.087-.205.018-.369.018-.703 0-1.248-.234-.545-.235-1.107-.621v1.875q1.195.468 2.472.468zM11.25 22.5q.773 0 1.453-.293t1.19-.803q.51-.51.808-1.195.299-.686.299-1.459 0-.668-.223-1.277-.222-.61-.62-1.096-.4-.486-.95-.826-.55-.34-1.207-.48v1.933q0 .41-.293.703t-.703.293H7.57q-.07.375-.07.75 0 .773.293 1.459t.803 1.195q.51.51 1.195.803.686.293 1.459.293zM18 18q.926 0 1.746-.352.82-.351 1.436-.966.615-.616.966-1.43.352-.815.352-1.752 0-.926-.352-1.746-.351-.82-.966-1.436-.616-.615-1.436-.966Q18.926 9 18 9t-1.74.357q-.815.358-1.43.973t-.973 1.43q-.357.814-.357 1.74 0 .129.006.258t.017.258q.551.27 1.02.65t.838.855q.369.475.627 1.026.258.55.387 1.148Q17.18 18 18 18Z\"/>", "website": "<circle cx=\"12\" cy=\"12\" r=\"9\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"1.8\"/><path d=\"M3 12h18M12 3c2.5 2.6 3.8 5.6 3.8 9s-1.3 6.4-3.8 9c-2.5-2.6-3.8-5.6-3.8-9S9.5 5.6 12 3z\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"1.8\"/>"};
ST.apps = ST.apps || {};
// name, length, passages, questions found, state; names match the ZIWO list in the source detail
const ZIWO_CALLS = [['Inbound call · Emmanuel · 25 Sep', '7 min', 9, 1, 'analysed'], ['Inbound call · Emmanuel · 19 Aug', '13 min', 14, 1, 'analysed'], ['Outbound call · Maria · 12 Aug', '7 min', 8, 1, 'analysed'], ['Inbound call · Emmanuel · 2 Oct', '4 min', 5, 0, 'ready']];
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
const docRow = (o) => '<tr class="drow' + (o.cls || '') + '" data-st="' + (o.st || 'done') + '" data-ext="' + esc((o.ext || '').toLowerCase()) + '"' + (o.id ? ' data-id="' + o.id + '"' : '') + '><td><span class="dname"><span class="ext">' + esc(o.ext) + '</span><span class="dn"><span class="nm">' + esc(o.name) + (o.badge || '') + '</span>' + (o.why || '') + '</span></span></td>' +
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
  DOCS.filter(d => ST.retired[d.id]).forEach(d => rows.push(docRow({ cls: ' is-retired', ext: d.name.split('.').pop(), name: d.name, st: 'ret', pages: d.pages, why: '<span class="why mute">Retired just now by Eric Ouisse</span>',
    acts: '<button class="btn btn--secondary" data-restore="' + d.id + '" data-base="1">Restore</button>' })));
  docx.filter(d => d.status === 'retired').forEach(d => rows.push(docRow({ cls: ' is-retired', ext: d.ext, name: d.name, st: 'ret', why: '<span class="why mute">' + esc(d.retiredNote) + '</span>',
    acts: '<button class="btn btn--secondary" data-restore="' + d.id + '">Restore</button>' })));
  // ZIWO calls: transcripts split by speaker, read like documents
  if (ST.apps.ziwo) ZIWO_CALLS.forEach(([n, mins, ps, qn, st]) => rows.push(docRow({ ext: 'call', name: n, pages: undefined, passages: ps, qs: qn, st: st === 'ready' ? 'wait' : 'done',
    why: '<span class="why mute">ZIWO · ' + mins + (st === 'ready' ? ' · waiting to be analysed' : '') + '</span>' })));
  rows.push(docRow({ ext: 'gmail', name: 'SSO stopped working after we upgraded', cls: ' is-failed', st: 'fail', why: '<span class="why">The email body is an image only, so there’s no text to read. Paste the text into a document and upload it.</span>',
    acts: '<button class="btn btn--secondary" data-retrymail="1">Try again</button>' }));
  rows.push(docRow({ ext: 'web', name: 'help.oslo.com/sso', cls: ' is-failed', st: 'fail', why: '<span class="why">The page asks visitors to sign in, and lojo never signs in. Make the page public, or upload it as a document.</span>',
    acts: '<button class="btn btn--secondary" data-retrymail="1">Try again</button>' }));
  $('docRows').innerHTML = rows.join('');
  if ($('dvDlg').open) dvRender();
  const nf = $('docRows').querySelectorAll('tr[data-st="fail"]').length; $('logsN').textContent = nf ? nf + ' failed' : ''; $('logsN').hidden = !nf;
  renderApps();
}
function renderApps() {
  $('apps').innerHTML = APPS.map(a => '<button type="button" class="app' + (ST.apps[a.id] ? ' is-on' : '') + (a.soon ? ' soon' : '') + '" data-app="' + a.id + '"' + (a.soon ? ' aria-disabled="true" title="Coming soon"' : '') + '><span class="mono logo" style="color:' + a.color + '"><svg viewBox="0 0 24 24" aria-hidden="true">' + LOGO[a.id] + '</svg></span><span><b>' + esc(a.name) + '</b><span class="k">' + (a.soon ? '<em class="soon__tag">Coming soon</em>' : ST.apps[a.id] ? 'Connected · ' + a.n + ' documents' : esc(a.kind)) + '</span></span></button>').join('');
  const on = APPS.filter(a => ST.apps[a.id]);
  $('synced').innerHTML = on.map(a => '<div class="file"><span class="mono logo" style="color:' + a.color + '"><svg viewBox="0 0 24 24" aria-hidden="true">' + LOGO[a.id] + '</svg></span><span><span class="name">' + esc(a.name) + '</span><span class="meta">Connected as eric@oslo.com · ' + a.n + ' documents · reads only</span></span><span class="pstage is-done">Synced</span><span class="acts"><button class="btn btn--ghost" style="opacity:1" data-off="' + a.id + '">Disconnect</button></span></div>').join('');
}
$('apps').addEventListener('click', (e) => {
  const b = e.target.closest('[data-app]'); if (!b || ST.apps[b.dataset.app]) return;
  const a = APPS.find(x => x.id === b.dataset.app);
  if (a.soon) { e.stopImmediatePropagation(); toast(a.name + ' is coming soon. Connect Website, Notion, Gmail, ZIWO or Slack for now.'); return; }
  // ZIWO needs an account, an API key and a recording consent
  if (a.id === 'website') { $('wForm').reset(); $('wGo').disabled = true; $('wErr').textContent = ''; $('wProg').hidden = true; $('apps').hidden = true; $('wForm').hidden = false; $('wUrl').focus(); return; }
  if (a.id === 'ziwo') { $('zForm').reset(); $('zGo').disabled = true; $('apps').hidden = true; $('zForm').hidden = false; $('zForm').querySelector('svg').innerHTML = LOGO.ziwo; $('zAcc').focus(); return; }
  b.classList.add('is-busy'); b.disabled = true;
  b.querySelector('.k').innerHTML = '<span class="spin" style="width:11px;height:11px;vertical-align:-1px"></span> Connecting…';
  setTimeout(() => { ST.apps[a.id] = true; save(); render(); toast(a.name + ' connected as eric@oslo.com'); }, 900);
});
// website: check the address, then show pages being read
$('wUrl').addEventListener('input', () => { $('wGo').disabled = !$('wUrl').value.trim(); $('wErr').textContent = ''; $('wUrl').classList.remove('is-bad'); });
$('wCancel').addEventListener('click', () => { $('wForm').hidden = true; $('apps').hidden = false; });
$('wForm').addEventListener('submit', (e) => {
  e.preventDefault();
  let v = $('wUrl').value.trim(); if (!/^https?:\/\//i.test(v)) v = 'https://' + v;
  let host = ''; try { host = new URL(v).hostname; } catch (err) {}
  if (!/\.[a-z]{2,}$/i.test(host)) { $('wErr').textContent = 'Use a full address, like https://help.yourcompany.com.'; $('wUrl').classList.add('is-bad'); return; }
  $('wUrl').value = v; $('wUrl').disabled = true; $('wGo').disabled = true; $('wGo').innerHTML = '<span class="spin" style="width:12px;height:12px;margin-right:6px"></span>Reading…';
  const pages = ['/', '/getting-started', '/billing', '/security', '/sso', '/refunds'];
  $('wProg').hidden = false;
  const draw = (n) => { $('wProg').innerHTML = '<div class="gm-bar"><i style="width:' + Math.round(n / pages.length * 100) + '%"></i></div><p class="sub">' + (n < pages.length ? 'Reading ' + host + pages[n] + '…' : 'Read ' + pages.length + ' pages from ' + host) + '</p>'; };
  draw(0);
  pages.forEach((_, i) => setTimeout(() => { draw(i + 1); if (i === pages.length - 1) setTimeout(() => {
    ST.apps.website = true; save(); $('wForm').hidden = true; $('apps').hidden = false; $('wUrl').disabled = false; $('wGo').textContent = 'Read the site'; render(); toast(host + ' connected · ' + pages.length + ' pages read'); }, 600); }, 450 * (i + 1)));
});
const zReady = () => { $('zGo').disabled = !($('zAcc').value.trim() && $('zKey').value.trim() && $('zOk').checked); };
['zAcc', 'zKey', 'zOk'].forEach(id => $(id).addEventListener('input', zReady)); $('zOk').addEventListener('change', zReady);
$('zCancel').addEventListener('click', () => { $('zForm').hidden = true; $('apps').hidden = false; });
$('zForm').addEventListener('submit', (e) => {
  e.preventDefault(); const acc = $('zAcc').value.trim();
  $('zGo').disabled = true; $('zGo').innerHTML = '<span class="spin" style="width:12px;height:12px;margin-right:6px"></span>Connecting…';
  setTimeout(() => { ST.apps.ziwo = true; save(); $('zForm').hidden = true; $('apps').hidden = false; $('zGo').textContent = 'Connect ZIWO'; render(); toast('ZIWO connected · ' + acc + '. lojo reads calls after they end.'); }, 1100);
});
$('synced').addEventListener('click', (e) => { const b = e.target.closest('[data-off]'); if (!b) return; delete ST.apps[b.dataset.off]; save(); render(); toast('Disconnected. Documents already indexed stay until you retire them.'); });
// full-screen documents log with search, status and type filters
const DV_ST = [['all', 'All'], ['fail', 'Failed'], ['run', 'Processing'], ['wait', 'Waiting'], ['done', 'Indexed'], ['ret', 'Retired']];
const DV_TYPE = { pdf: 'Uploads', docx: 'Uploads', doc: 'Uploads', md: 'Uploads', txt: 'Uploads', call: 'ZIWO', slack: 'Slack', gmail: 'Gmail', web: 'Website', website: 'Website', notion: 'Notion', ziwo: 'ZIWO' };
const dvSrc = (ext) => DV_TYPE[ext] || 'Uploads';
let dvSt = 'all', dvType = '';
function dvRender() {
  const rows = [...$('docRows').querySelectorAll('tr.drow')].map(r => r.cloneNode(true));
  const q = $('dvQ').value.trim().toLowerCase();
  // items from connected apps join the uploads
  Object.keys(ST.apps || {}).filter(id => ST.apps[id] && APPINFO[id]).forEach(id => APPINFO[id].items.forEach(([n, st]) => {
    if (rows.some(r => r.textContent.includes(n))) return;
    const bad = /couldn|changed/.test(st), t = document.createElement('tbody');
    t.innerHTML = docRow({ ext: id === 'website' ? 'web' : id, name: n, st: bad ? 'fail' : /awaiting|running/.test(st) ? 'run' : 'done', cls: bad ? ' is-failed' : '', why: '<span class="why' + (bad ? '' : ' mute') + '">' + esc(st) + '</span>' });
    rows.push(t.firstElementChild);
  }));
  const srcs = [...new Set(rows.map(r => dvSrc(r.dataset.ext)))];
  $('dvType').innerHTML = '<option value="">All sources</option>' + srcs.map(t => '<option value="' + t + '"' + (t === dvType ? ' selected' : '') + '>' + t + ' · ' + rows.filter(r => dvSrc(r.dataset.ext) === t).length + '</option>').join('');
  $('dvSt').innerHTML = DV_ST.map(([k, l]) => { const n = k === 'all' ? rows.length : rows.filter(r => r.dataset.st === k).length; return (k === 'all' || n) ? '<button type="button" class="dv__chip' + (k === 'fail' ? ' is-bad' : '') + '" data-dvst="' + k + '" aria-pressed="' + (dvSt === k) + '">' + l + ' <span>' + n + '</span></button>' : ''; }).join('');
  const shown = rows.filter(r => (dvSt === 'all' || r.dataset.st === dvSt) && (!dvType || dvSrc(r.dataset.ext) === dvType) && (!q || r.textContent.toLowerCase().includes(q)));
  $('dvRows').replaceChildren(...shown); $('dvEmpty').hidden = shown.length > 0;
  $('dvMeta').textContent = shown.length + ' of ' + rows.length + ' · ' + rows.filter(r => r.dataset.st === 'fail').length + ' failed';
}
$('logsBtn').addEventListener('click', () => $('dvOpen').click());
$('dvOpen').addEventListener('click', () => { dvSt = 'all'; dvType = ''; $('dvQ').value = ''; dvRender(); $('dvDlg').showModal(); $('dvQ').focus(); });
$('dvDlg').addEventListener('click', (e) => {
  if (e.target.closest('[data-dvx]')) { $('dvDlg').close(); return; }
  const c = e.target.closest('[data-dvst]'); if (c) { dvSt = c.dataset.dvst; dvRender(); return; }
  // actions inside the log act on the real row
  const b = e.target.closest('#dvRows button'); if (b) { const attr = [...b.attributes].find(a => a.name.startsWith('data-')); if (attr) { const real = $('docRows').querySelector('[' + attr.name + '="' + attr.value + '"]'); if (real) real.click(); setTimeout(dvRender, 50); } }
});
$('dvQ').addEventListener('input', dvRender);
$('dvType').addEventListener('change', (e) => { dvType = e.target.value; dvRender(); });
$('docRows').addEventListener('click', (e) => {
  if (e.target.closest('[data-retrymail]')) { toast('Trying again…'); setTimeout(() => toastError('Still couldn’t be read. Follow the note under it.'), 1200); return; }
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
// arriving from Build to explain a gap
const FOR_GAP = GAPS.find(g => g.id === SP0().get('gap'));
if (FOR_GAP) {
  $('forGap').hidden = false;
  $('forGap').innerHTML = '<span class="forgap__ic">🧩</span><div><small>From Build · Gap</small><b>' + esc(FOR_GAP.term) + '</b><span>' + esc(FOR_GAP.why) + ' Upload a document that explains it.</span></div><a class="btn btn--ghost btn--sm" href="build.html?gap=' + FOR_GAP.id + '">Back to Build</a>';
}
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
  // the first file sent for a gap shows as "Document sent" on that gap in Build
  if (FOR_GAP && files.length) { ST.gapDocs = ST.gapDocs || {}; ST.gapDocs[FOR_GAP.id] = files[0].name; save(); $('forGap').querySelector('span:last-of-type').textContent = files[0].name + ' sent for this gap. lojo reads it and checks the gap.'; }
  files.forEach(f => {
    const item = { name: f.name, ext: (f.name.split('.').pop() || '').slice(0, 4), stage: 'Extracting text', done: false, pages: Math.max(1, Math.round(f.size / 40000)) };
    extra.unshift(item);
    setTimeout(() => { item.stage = 'Splitting into passages'; render(); }, 900);
    setTimeout(() => { item.stage = 'Indexing by meaning'; render(); }, 1800);
    setTimeout(() => { item.done = true; item.passages = Math.round(item.pages * 4.6); render(); toast(item.name + ' indexed'); }, 2800);
  });
  render();
}
$('fileInput').addEventListener('change', (e) => { if (e.target.files.length) shoot(); addFiles(e.target.files); e.target.value = ''; });
const drop = $('drop');
['dragenter', 'dragover'].forEach(ev => drop.addEventListener(ev, (e) => { e.preventDefault(); drop.classList.add('is-over'); }));
['dragleave', 'drop'].forEach(ev => drop.addEventListener(ev, (e) => { e.preventDefault(); drop.classList.remove('is-over'); }));
drop.addEventListener('drop', (e) => { shoot(); addFiles(e.dataTransfer.files); });
// a basketball drops through the hoop when files go in
function shoot() {
  if (matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  drop.classList.remove('is-shot'); void drop.offsetWidth; drop.classList.add('is-shot');
  clearTimeout(shoot.t); shoot.t = setTimeout(() => drop.classList.remove('is-shot'), 1600);
}
function show(tab) {
  document.querySelectorAll('.ptab').forEach(t => t.setAttribute('aria-selected', t.dataset.tab === tab));
  $('tabDocs').hidden = tab !== 'docs'; $('tabConnect').hidden = tab !== 'connect';
}
document.querySelectorAll('.ptab').forEach(t => t.addEventListener('click', () => show(t.dataset.tab)));
// connected sources: uploaded documents plus every connected app, each with its health
if (!ST.apps || !ST.__appsSeeded) { ST.apps = Object.assign({ notion: true, website: true, gmail: true }, ST.apps || {}); ST.apps = Object.fromEntries(Object.entries(ST.apps).filter(([k]) => !(APPS.find(a => a.id === k) || {}).soon)); ST.__appsSeeded = true; save(); }
const DOCICO = '<svg viewBox="0 0 24 24"><path d="M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8z"/><path d="M14 3v5h5"/></svg>';
const APPINFO = {
  notion: { what: 'Oslo wiki', items: [['Pricing wiki', '6 pages'], ['Onboarding playbook', '11 pages'], ['Security docs', '4 pages'], ['Policies', '5 pages'], ['Help centre drafts', '3 pages']], state: 'ok', fresh: 'Synced 6 min ago', supplies: 'Pages and wikis from the teamspaces you chose, split into passages for drafting answers.' },
  website: { what: 'help.oslo.com · oslo.com/pricing', items: [['help.oslo.com/sso', 'changed since last sync'], ['oslo.com/pricing', 'synced'], ['oslo.com/legal/refunds', 'synced']], state: 'warn', fresh: '1 page changed since the last sync', next: 'Sync now to pick up the changed page. Drafts that cite it will be checked again.', supplies: 'Public pages from your website and help centre, read the same way as documents.' },
  gmail: { what: 'support@oslo.com', items: [['SSO stopped working after we upgraded', 'couldn’t be analysed'], ['Invoice for our annual plan', 'ready'], ['Apple Pay in Germany?', 'analysed']], state: 'warn', fresh: '1 email couldn’t be analysed', next: 'Open it in Insights and try the analysis again.', nextHref: 'insights.html#inbox', supplies: 'Incoming email threads, participants and message text, analysed in Insights for new questions.' },
  ziwo: { what: 'Support line · inbound and outbound', items: [['Inbound call · Emmanuel · 25 Sep', 'analysed'], ['Inbound call · Emmanuel · 19 Aug', 'analysed'], ['Outbound call · Maria · 12 Aug', 'analysed'], ['Inbound call · Emmanuel · 2 Oct', 'ready']], state: 'ok', fresh: 'Synced 12 min ago', supplies: 'Call recordings and their transcripts, split by speaker, analysed in Insights for new questions.' },
  slack: { what: '#support · #sales-questions · #billing', items: [['#support', '214 threads'], ['#sales-questions', '88 threads'], ['#billing', '41 threads']], state: 'ok', fresh: 'Synced just now', supplies: 'Messages and threads from the channels you choose, analysed in Insights for the questions your team keeps asking.' },
  aircall: { what: 'Support line · Sales line', items: [['+44 20 7946 0958', 'awaiting transcript'], ['+33 6 85 36 57 11', 'ready'], ['+33 7 57 91 26 97', 'too short to transcribe']], state: 'warn', fresh: 'Waiting for 1 transcript', next: 'Nothing to do: the transcript arrives from Aircall, then the call can be analysed.', supplies: 'Call recordings and transcripts, analysed in Insights for the questions customers ask.' },
};
Object.keys(ST.synced || {}).forEach(id => { if (APPINFO[id]) APPINFO[id].items = APPINFO[id].items.map(([n, st]) => [n, /changed/.test(st) ? 'synced' : st]); });
const DEF = { what: 'Connected just now', items: [['First sync', 'running']], state: 'ok', fresh: 'First sync in progress', supplies: 'Files and pages from this app, read like documents.' };
let srcSel = SP0().get('src') || ST.srcSel || 'upload';
function SP0() { return new URLSearchParams(location.search); }
function sources() {
  const docx = ST.docx || [], failed = docx.filter(d => d.status === 'failed').length, live = DOCS.filter(d => !ST.retired[d.id]).length + extra.length + docx.filter(d => d.status !== 'retired').length;
  const c = counts();
  const list = [{ id: 'upload', name: 'Uploaded documents', sub: 'Upload · PDF, DOCX, Markdown, TXT', icon: '<span class="sico doc">' + DOCICO + '</span>', state: failed ? 'warn' : 'ok',
    line: (failed ? failed + ' couldn’t be processed · ' : '') + live + ' documents', conn: 'Connected', connS: 'Files you upload are read straight away.', fresh: failed ? failed + ' document couldn’t be processed' : 'Indexed today',
    freshS: failed ? 'Remove the password and upload it again.' : 'Every document is indexed by meaning.', contrib: c.passages.toLocaleString('en-GB') + ' passages', contribS: c.questions + ' questions found in them.',
    supplies: 'Documents you upload: their text is pulled out, split into passages and indexed by meaning.', next: failed ? 'Fix the document that couldn’t be processed, below.' : 'Nothing to do. Upload more when you have them.' }];
  APPS.filter(a => ST.apps[a.id]).forEach(a => {
    const i = APPINFO[a.id] || DEF;
    if (APP_IDS.includes(a.id) && !appWarn(a.id)) { i.state = 'ok'; delete i.next; }
    list.push({ id: a.id, name: a.name, sub: a.name + ' · ' + i.what, icon: '<span class="sico" style="color:' + a.color + '"><svg viewBox="0 0 24 24" fill="currentColor">' + LOGO[a.id] + '</svg></span>', state: i.state,
      line: (i.state === 'warn' ? 'Needs attention · ' : '') + i.fresh, conn: 'Connected', connS: 'Signed in as eric@oslo.com. lojo only reads.', fresh: i.fresh, freshS: i.state === 'warn' ? 'See what happens next below.' : 'Checked for changes every hour.',
      contrib: i.items.length + ' item' + (i.items.length === 1 ? '' : 's'), contribS: 'Imported knowledge can be reviewed in Insights and Knowledge.', supplies: i.supplies, next: i.next || 'Nothing to do. lojo keeps it in sync.', nextHref: i.nextHref, items: i.items });
  });
  return list;
}
// what a source is and how lojo reads it
const ABOUT = (s) => {
  const app = { upload: ['Uploaded documents', 'Files you upload here', 'When you upload'], notion: ['Notion', 'Teamspaces: Pricing wiki, Onboarding playbook, Security docs, Policies', 'Automatic · every hour'],
    website: ['Website', 'help.oslo.com and oslo.com/pricing, oslo.com/legal', 'Automatic · daily'], gmail: ['Gmail', 'support@oslo.com inbox', 'Automatic · as emails arrive'],
    ziwo: ['ZIWO', 'Support line calls, inbound and outbound, with transcripts', 'Automatic · after each call'],
    slack: ['Slack', 'Public channels: #support, #sales-questions, #billing. Never DMs or private channels.', 'Automatic · every 15 minutes'],
    aircall: ['Aircall', 'Support line and Sales line, with transcripts', 'Automatic · after each call'] }[s.id] || [s.name, 'Everything the account can read', 'Automatic · every hour'];
  return [['Source type', app[0]], ['Configured scope', app[1]], ['Sync mode', app[2]], ['Connected by', s.id === 'upload' ? 'Anyone who uploads' : 'Eric Ouisse · eric@oslo.com'], ['Access', 'Read only. lojo never edits your files.']];
};
document.addEventListener('click', (e) => { if (!e.target.closest('.about')) document.querySelectorAll('.about.is-open').forEach(w => { w.classList.remove('is-open'); w.querySelector('[data-about]').setAttribute('aria-expanded', 'false'); }); });
function renderSources() {
  const all = sources(), q = $('srcQ').value.trim().toLowerCase(), list = all.filter(s => !q || (s.name + ' ' + s.sub).toLowerCase().includes(q));
  if (!all.some(s => s.id === srcSel)) srcSel = 'upload';
  // the same numbers as the Dashboard Sources card and Activity
  const S = sourceSummary();
  $('srcSum').innerHTML = '<b>' + S.sources + ' connected sources</b> · ' + S.warn + ' need' + (S.warn === 1 ? 's' : '') + ' attention · ' + S.passages.toLocaleString('en-GB') + ' passages';
  const row = (s) => '<button type="button" class="sitem' + (s.id === srcSel ? ' is-sel' : '') + '" data-src="' + s.id + '">' + s.icon + '<span><b>' + esc(s.name) + '</b><span>' + esc(s.line) + '</span></span><i class="dot' + (s.state === 'warn' ? ' warn' : '') + '"></i></button>';
  const w = list.filter(s => s.state === 'warn'), ok = list.filter(s => s.state !== 'warn');
  $('srcList').innerHTML = (w.length ? '<p class="sgrp">Needs attention <span>' + w.length + '</span></p>' + w.map(row).join('') : '') + (ok.length ? '<p class="sgrp">Healthy <span>' + ok.length + '</span></p>' + ok.map(row).join('') : '') || '<p class="sub" style="padding:14px">No source matches.</p>';
  const s = all.find(x => x.id === srcSel);
  $('srcHead').innerHTML = '<div class="sh__top">' + s.icon + '<div><h2>' + esc(s.name) + '</h2><p>' + esc(s.sub) + '</p></div><span class="spacer"></span>' +
    '<span class="about"><button class="btn btn--secondary" type="button" data-about aria-expanded="false"><svg class="i" viewBox="0 0 24 24" style="width:15px;height:15px;fill:none;stroke:currentColor;stroke-width:1.9"><circle cx="12" cy="12" r="9"/><path d="M12 11v5M12 8h.01"/></svg>About this source</button>' +
    '<span class="aboutpop" role="dialog" aria-label="About this source"><dl>' + ABOUT(s).map(([k, v]) => '<div><dt>' + k + '</dt><dd>' + esc(v) + '</dd></div>').join('') + '</dl></span></span>' +
    (s.id === 'upload' ? '<button class="btn btn--grad" type="button" data-upload>Upload documents</button>' : '<button class="btn btn--grad" type="button" data-sync>Sync now</button>') + '</div>';
  $('uploadBody').hidden = s.id !== 'upload'; $('appBody').hidden = s.id === 'upload';
  if (s.id === 'gmail') { renderGmail(); return; }
  if (s.id !== 'upload') $('appBody').innerHTML = '<h3>What’s synced<span class="spacer"></span><button class="btn btn--ghost btn--sm" type="button" data-off="' + s.id + '">Disconnect</button></h3>' +
    s.items.map(([n, st]) => '<div class="sirow"><span>' + esc(n) + '</span><em>' + esc(st) + '</em><span class="pstage ' + (/couldn|changed/.test(st) ? 'is-fail' : /awaiting|running|ready/.test(st) ? 'is-wait' : 'is-done') + '">' + (/couldn|changed/.test(st) ? 'Needs attention' : /awaiting|running/.test(st) ? 'Waiting' : /ready/.test(st) ? 'Ready' : 'Synced') + '</span></div>').join('');
}
// ---------- Gmail: one card per address; pick labels, then lojo reads them
ST.gmail = ST.gmail || { open: true, accounts: [{ id: 'g1', email: 'support@oslo.com', docs: 31, fresh: 16, at: '23 Oct, 00:42',
  labels: [['Inbox', 1, 24], ['Sent', 1, 11], ['Starred', 1, 6], ['Important', 1, 9], ['Support', 0, 42], ['Billing', 0, 17]] }] };
let gRead = null; // { id, done: [] } while labels are being read
function renderGmail() {
  const G = ST.gmail;
  $('appBody').innerHTML = '<div class="gm-h"><h3>Gmail</h3><button class="btn btn--secondary btn--sm" type="button" data-gm="add">+ Add another address</button></div>' +
    G.accounts.map(a => {
      const reading = gRead && gRead.id === a.id, open = G.open === a.id || G.open === true;
      const on = a.labels.filter(l => l[1]), total = on.reduce((n, l) => n + l[2], 0), done = reading ? gRead.done.length : 0;
      return '<div class="gm-card"><div class="gm-top"><span class="gm-av">M</span><div class="gm-id"><b>' + esc(a.email) + '</b><span>' +
        (reading ? 'Reading ' + on.length + ' label' + (on.length === 1 ? '' : 's') + '…' : a.docs + ' documents · ' + a.fresh + ' new · synced ' + esc(a.at)) + '</span></div>' +
        '<button class="btn btn--secondary btn--sm" type="button" data-gm="sync" data-a="' + a.id + '"' + (reading ? ' disabled' : '') + '>Sync again</button>' +
        '<button class="btn btn--secondary btn--sm' + (open ? ' is-on' : '') + '" type="button" data-gm="labels" data-a="' + a.id + '">Labels</button>' +
        '<button class="btn btn--ghost btn--sm" type="button" data-gm="retire" data-a="' + a.id + '">Retire</button></div>' +
        (reading ? '<div class="gm-bar"><i style="width:' + Math.round(done / on.length * 100) + '%"></i></div>' : '') +
        (open ? '<p class="gm-note">Choose the labels to read. lojo reads their threads from the last 12 months, up to 200, and PDF, DOCX, TXT and MD attachments.</p>' +
          '<div class="gm-labels">' + a.labels.map(([n, chk, t], i) => {
            const st = reading && chk ? (gRead.done.includes(i) ? '<em class="gm-ok">✓ Read · ' + t + ' threads</em>' : gRead.done.length === on.filter(l => a.labels.indexOf(l) < i).length ? '<em class="gm-run"><span class="spin"></span>Reading ' + t + ' threads…</em>' : '<em class="gm-wait">Waiting</em>') : '<em class="gm-t">' + t + ' threads</em>';
            return '<label class="gm-l' + (chk ? ' is-on' : '') + '"><input type="checkbox" data-gl="' + i + '" data-a="' + a.id + '"' + (chk ? ' checked' : '') + (reading ? ' disabled' : '') + '><span>' + esc(n) + '</span>' + st + '</label>'; }).join('') + '</div>' +
          '<div class="gm-foot"><button class="btn btn--primary" type="button" data-gm="read" data-a="' + a.id + '"' + (reading || !on.length ? ' disabled' : '') + '>' + (reading ? '<span class="spin"></span>Reading…' : 'Read labels') + '</button>' +
          '<span class="sub">' + (on.length ? on.length + ' label' + (on.length === 1 ? '' : 's') + ' · about ' + Math.min(total, 200) + ' threads' : 'Pick at least one label') + '</span></div>' : '') + '</div>';
    }).join('');
}
$('appBody').addEventListener('change', (e) => {
  const c = e.target.closest('[data-gl]'); if (!c) return;
  const a = ST.gmail.accounts.find(x => x.id === c.dataset.a); a.labels[+c.dataset.gl][1] = c.checked ? 1 : 0; save(); renderGmail();
});
$('appBody').addEventListener('click', (e) => {
  const b = e.target.closest('[data-gm]'); if (!b) return;
  const G = ST.gmail, a = G.accounts.find(x => x.id === b.dataset.a), k = b.dataset.gm;
  if (k === 'labels') { G.open = G.open === a.id || G.open === true ? null : a.id; save(); renderGmail(); }
  if (k === 'add') toast('Sign in with the Google account to add. lojo only reads.');
  if (k === 'retire') { G.accounts = G.accounts.filter(x => x !== a); save(); renderGmail(); toast(a.email + ' retired. What it already gave lojo stays.'); }
  if (k === 'sync') { b.disabled = true; b.innerHTML = '<span class="spin"></span>Syncing…'; setTimeout(() => { a.at = 'just now'; a.fresh = 0; save(); renderGmail(); toast(a.email + ' is up to date'); }, 1400); }
  if (k === 'read') {
    // read each ticked label in turn, then show what came in
    const idx = a.labels.map((l, i) => l[1] ? i : -1).filter(i => i >= 0);
    gRead = { id: a.id, done: [] }; renderGmail();
    idx.forEach((i, n) => setTimeout(() => { gRead.done.push(i); renderGmail(); if (n === idx.length - 1) setTimeout(() => {
      const got = Math.min(200, idx.reduce((t, j) => t + a.labels[j][2], 0)); a.fresh = got - a.docs > 0 ? got - a.docs : 3; a.docs = got; a.at = 'just now'; gRead = null; save(); renderGmail();
      toast('Read ' + idx.length + ' label' + (idx.length === 1 ? '' : 's') + ' · ' + got + ' threads. New questions show up in Insights.'); }, 700); }, 900 * (n + 1)));
  }
});
$('srcList').addEventListener('click', (e) => { const b = e.target.closest('[data-src]'); if (!b) return; srcSel = b.dataset.src; ST.srcSel = srcSel; save(); renderSources(); $('srcDet').scrollTop = 0; });
$('srcQ').addEventListener('input', renderSources);
$('srcDet').addEventListener('click', (e) => {
  if (e.target.closest('[data-upload]')) { openAdd('docs'); return; }
  const sy = e.target.closest('[data-sync]');
  if (sy) { sy.disabled = true; sy.innerHTML = '<span class="spin" style="width:12px;height:12px"></span> Syncing…'; setTimeout(() => { ST.synced = ST.synced || {}; ST.synced[srcSel] = true; save(); if (APPINFO[srcSel]) { APPINFO[srcSel].state = 'ok'; APPINFO[srcSel].fresh = 'Synced just now'; APPINFO[srcSel].items = APPINFO[srcSel].items.map(([n, st]) => [n, /changed/.test(st) ? 'synced' : st]); delete APPINFO[srcSel].next; } renderSources(); toast('Synced'); }, 1400); }
  const ab = e.target.closest('[data-about]'); if (ab) { const w = ab.parentNode; w.classList.toggle('is-open'); ab.setAttribute('aria-expanded', w.classList.contains('is-open')); }
  const off = e.target.closest('[data-off]'); if (off) { delete ST.apps[off.dataset.off]; save(); srcSel = 'upload'; render(); renderSources(); toast('Disconnected. Knowledge already imported stays until you retire it.'); }
});
// Add source: the same Documents / Connect choice as setup, in a popup
const dlg = $('addDlg');
const openAdd = (tab) => { show(tab); dlg.showModal(); };
$('addSrc').addEventListener('click', () => openAdd('docs'));
$('addDocs').addEventListener('click', () => openAdd('docs'));
$('addX').addEventListener('click', () => dlg.close());
dlg.addEventListener('click', (e) => { if (e.target === dlg) dlg.close(); });
// close the popup once something is added, and show where it went
$('fileInput').addEventListener('change', () => { if (!$('upErr').hidden && !extra.length) return; setTimeout(() => { if ($('upErr').hidden) { dlg.close(); srcSel = 'upload'; renderSources(); } }, 50); });
$('drop').addEventListener('drop', () => setTimeout(() => { if ($('upErr').hidden) { dlg.close(); srcSel = 'upload'; renderSources(); } }, 50));
$('apps').addEventListener('click', (e) => { const b = e.target.closest('[data-app]'); if (!b) return; const id = b.dataset.app; const wasOn = ST.apps[id];
  setTimeout(() => { if (ST.apps[id] && !wasOn) { dlg.close(); srcSel = id; ST.srcSel = id; save(); renderSources(); } else if (wasOn) { dlg.close(); srcSel = id; renderSources(); } }, wasOn ? 0 : 1000); });
const _render = render; render = function () { _render(); if ($('srcList')) renderSources(); };
const SP = new URLSearchParams(location.search), pinDoc = SP.get('doc'), pinLoc = SP.get('loc');
if (pinDoc && docById(pinDoc)) open = pinDoc;
renderScope();
render();
show('docs');
if (location.hash === '#connect') openAdd('connect');
if (pinDoc && docById(pinDoc)) { srcSel = 'upload'; renderSources();
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
  .fsbtn{gap:6px}
  .fsbtn svg{width:15px;height:15px;fill:none;stroke:currentColor;stroke-width:1.9;stroke-linecap:round;stroke-linejoin:round}
  body.is-fs .side,body.is-fs .mnav,body.is-fs .fab{display:none!important}
  body.is-fs .main{margin-left:0}
  body.is-fs .wrap{max-width:none;padding:16px 24px 24px}
  body.is-fs .head{margin:-16px -24px 16px;padding:12px 24px}
  body.is-fs .head > div:first-child > p:not(.label),body.is-fs .head .htip{display:none}
  body.is-fs .head h1{font-size:1.3rem;margin:2px 0 0}
  body.is-fs .wrap2{grid-template-columns:minmax(380px,32%) minmax(0,1fr)}
  body.is-fs .owrap{grid-template-columns:minmax(300px,26%) minmax(0,1fr)}
  body.is-fs .tlist{top:76px;max-height:calc(100vh - 96px);overflow:auto}
  body.is-fs .fsbtn{background:var(--ink);border-color:var(--ink);color:#fff}

  /* rows like Build: grey cards, avatar, tags, count pill */
  .tlist{padding-bottom:8px}
  .titem.is-row{grid-template-columns:32px minmax(0,1fr) auto;column-gap:12px;row-gap:8px;margin:8px 8px 0;width:calc(100% - 16px);padding:14px;border:0;border-radius:12px;background:#F7F6F4;align-items:center}
  .titem.is-row:hover{background:#F0EEEB}
  .titem.is-row.is-sel{background:var(--panel);box-shadow:inset 3px 0 0 var(--rose),0 0 0 1px var(--line-2),0 6px 16px -12px rgba(36,26,20,.4)}
  .titem.is-row.is-sel::before{display:none}
  .titem.is-row.is-failed{background:rgba(198,69,69,.06)}
  .titem.is-row.is-failed.is-sel{background:rgba(198,69,69,.12);box-shadow:inset 3px 0 0 var(--error)}
  .titem.is-row b{grid-column:2;grid-row:1}
  .titem.is-row .tmeta{grid-column:2;grid-row:2;display:flex;gap:6px;flex-wrap:wrap}
  .titem.is-row .tside{grid-column:3;grid-row:1/span 2;align-self:center;display:grid;justify-items:end;gap:4px}
  .titem.is-row .rav{grid-column:1;grid-row:1/span 2;align-self:center}
  .tfail{font-style:normal;font-size:.76rem;font-weight:600;color:var(--error);white-space:nowrap}
  .rav{width:32px;height:32px;border-radius:50%;display:grid;place-items:center;font-size:.95rem;line-height:1}
  .rav--question{background:#FFF0E8}
  .rav--gap{background:rgba(47,116,232,.12)}
  .rav--failed{background:rgba(198,69,69,.14)}
  .rav--down{background:rgba(62,111,166,.12)}
  .srcb{display:inline-flex;align-items:center;gap:4px;height:22px;padding:0 8px;border-radius:999px;background:#FFF0E8;border:1px solid rgba(232,93,117,.22);color:#B73C54;font-size:.72rem;font-weight:700}
  .srcb svg{width:12px;height:12px;fill:none;stroke:currentColor;stroke-width:2;stroke-linejoin:round}
  .badge--q{background:rgba(36,26,20,.06);color:var(--ink)}
  .badge--gap{background:rgba(47,116,232,.1);color:#2F74E8}
  .badge--bad{background:rgba(198,69,69,.1);color:var(--error)}
  :root[data-theme="dark"] .titem.is-row{background:rgba(255,255,255,.04)}

  .ico{width:18px;height:18px;fill:none;stroke:currentColor;stroke-width:1.8;stroke-linecap:round;stroke-linejoin:round;flex:none}
  .utabs{display:flex;gap:8px;margin:0 0 26px;overflow-x:auto;scrollbar-width:none}
  .utab{flex:none;height:36px;padding:0 16px;border:1px solid var(--line-2);border-radius:999px;background:var(--panel);font:inherit;font-size:.9rem;font-weight:600;color:var(--muted);cursor:pointer;white-space:nowrap}
  .utab:hover{border-color:#FFB199;color:var(--ink)}
  .utab[aria-selected="true"]{background:#FFF0E8;border-color:#FFB199;color:#8A4B2F}
  :root[data-theme="dark"] .utab[aria-selected="true"]{background:rgba(255,177,153,.14);border-color:rgba(255,177,153,.45);color:#FFC7B2}
  .kicker{margin:0 0 6px;font-size:.9rem;font-weight:600;color:var(--muted)}
  .ihead{display:flex;align-items:flex-start;gap:16px 28px;flex-wrap:wrap;margin:0 0 24px}
  .ihead > div:first-child{flex:1 1 420px;min-width:0}
  .ihead h2{font-family:var(--display);font-weight:700;font-size:1.75rem;letter-spacing:-.02em;line-height:1.2;margin:0}
  .ihead h2 em{font-style:normal;color:var(--rose)}
  .ihead p{margin:8px 0 0;color:var(--muted);font-size:.95rem}
  .ihead{justify-content:flex-end;margin-bottom:20px}
  .ihead > div:first-child{display:none}
  @media (min-width:1200px){#tabQ .ihead,#tabT .ihead{position:relative;z-index:1;margin-top:-62px;margin-left:auto;width:max-content}}
  @media (min-width:1360px){#tabG .ihead{position:relative;z-index:1;margin-top:-62px;margin-left:auto;width:max-content}}
  @media (min-width:1200px){#tabO .ihead{position:relative;z-index:1;margin-top:-62px;margin-left:auto;width:max-content}}
  .ihead .ictl{display:flex;align-items:center;gap:10px 14px;flex-wrap:wrap;justify-content:flex-end}
  .prog{display:flex;align-items:center;gap:14px;margin-top:16px;font-size:.86rem;color:var(--muted)}
  .prog .trk{width:200px;height:6px;border-radius:999px;background:var(--line);overflow:hidden}
  .prog .trk span{display:block;height:100%;border-radius:999px;background:var(--success);transition:width .4s ease}
  .prog b{color:var(--ink);font-weight:600}
  .segp{display:inline-flex;gap:2px;padding:4px;border:1px solid var(--line);border-radius:999px;background:var(--panel)}
  .segp button{height:38px;padding:0 18px;border:0;background:none;border-radius:999px;font:inherit;font-size:.9rem;color:var(--muted);cursor:pointer;white-space:nowrap}
  .segp button:hover{color:var(--ink)}
  .segp button[aria-pressed="true"]{background:var(--ink);color:var(--bg)}
  .found{font-size:.84rem;color:var(--muted);white-space:nowrap}
  .wrap2{display:grid;grid-template-columns:minmax(260px,380px) minmax(0,1fr);gap:22px;align-items:start}
  .tlist{background:var(--panel);border:1px solid var(--line);border-radius:18px;overflow:hidden;position:sticky;top:110px}
  .tlist .th{display:flex;justify-content:space-between;padding:14px 22px;font-size:.84rem;color:var(--muted);border-bottom:1px solid var(--line)}
  .titem{position:relative;display:grid;grid-template-columns:minmax(0,1fr) auto;justify-items:start;align-items:start;gap:4px 14px;width:100%;text-align:left;padding:16px 22px;border:0;border-top:1px solid var(--line);background:none;font:inherit;color:inherit;cursor:pointer}
  .titem.has-ic{grid-template-columns:32px minmax(0,1fr) auto}
  .titem.has-ic .tic{grid-column:1}
  .titem.has-ic b,.titem.has-ic .st{grid-column:2}
  .titem.has-ic .tn{grid-column:3}
  .th + .titem,.tgroup .titem:first-of-type{border-top:0}
  .titem:hover{background:var(--bg-soft)}
  .titem.is-sel{background:rgba(232,93,117,.07)}
  .titem.is-sel::before{content:"";position:absolute;left:0;top:0;bottom:0;width:3px;background:var(--rose)}
  .titem .tic{grid-row:1/3;width:32px;height:32px;border-radius:50%;display:grid;place-items:center}
  .titem .tic .ico{width:16px;height:16px}
  .titem b{grid-column:1;font-weight:600;font-size:.95rem;line-height:1.4}
  .titem .st{grid-column:1}
  .titem .tn{grid-column:2;grid-row:1/3;justify-self:end;text-align:right;font-family:var(--display);font-weight:700;font-size:1.25rem;line-height:1.2}
  .titem .tn small{display:block;font:500 .7rem var(--body);color:var(--muted)}
  .st{display:inline-flex;align-items:center;gap:7px;font-size:.84rem}
  .st::before{content:"";width:6px;height:6px;border-radius:50%;background:currentColor}
  .st.plain::before{display:none}
  .c-amber{color:#8A6212} .c-grey{color:var(--muted)} .c-red{color:var(--error)} .c-blue{color:var(--info)} .c-green{color:var(--success)}
  .bg-amber{background:var(--amber-soft)} .bg-red{background:rgba(198,69,69,.08)} .bg-blue{background:rgba(62,111,166,.1)}
  .tgroup{border-top:1px solid var(--line)}
  .tgroup summary{display:flex;align-items:center;gap:8px;padding:14px 22px;color:var(--muted);font-size:.88rem;cursor:pointer;list-style:none}
  .tgroup summary::-webkit-details-marker{display:none}
  .tgroup summary::before{content:"›";font-size:1.1rem;line-height:1;transition:transform .15s ease}
  .tgroup[open] summary::before{transform:rotate(90deg)}
  .tgroup[open] summary{border-bottom:1px solid var(--line)}
  .tnone{padding:26px 22px;color:var(--muted);font-size:.88rem;text-align:center}
  .dcard{background:var(--panel);border:1px solid var(--line);border-radius:20px}
  .dbody{padding:30px 34px}
  .dtop{display:flex;gap:20px;align-items:flex-start}
  .dtop > div:first-child{flex:1;min-width:0}
  .pill{display:inline-flex;align-items:center;gap:8px;min-height:30px;padding:4px 13px;border-radius:999px;font-size:.86rem;font-weight:600}
  .pill .ico{width:16px;height:16px}
  .pill .dot{width:7px;height:7px;border-radius:50%;background:currentColor}
  .pill.amber{background:var(--amber-soft);color:#7A5A12} .pill.grey{background:var(--bg-soft);color:var(--muted)} .pill.green{background:rgba(63,143,95,.1);color:var(--success)} .pill.red{background:rgba(198,69,69,.08);color:var(--error)} .pill.blue{background:rgba(62,111,166,.1);color:var(--info)}
  :root[data-theme="dark"] .pill.amber,:root[data-theme="dark"] .bg-amber{background:rgba(201,162,74,.16);color:#E2C47A}
  :root[data-theme="dark"] .c-amber{color:#E2C47A}
  .dcard h2{font-family:var(--display);font-weight:700;font-size:1.85rem;letter-spacing:-.02em;line-height:1.2;margin:0 0 8px;overflow-wrap:anywhere}
  .dsub{margin:0;color:var(--muted);font-size:.98rem}
  .dtop .pill{margin-top:14px}
  .dnum{text-align:right;flex:none}
  .dnum b{display:block;font-family:var(--display);font-weight:800;font-size:2.7rem;line-height:1}
  .dnum span{font-size:.86rem;color:var(--muted)}
  .merge{display:grid;grid-template-columns:auto minmax(0,1fr) auto;gap:16px;align-items:center;margin-top:24px;padding:18px 22px;border-radius:14px;background:var(--bg-soft)}
  .merge > .ico{color:var(--rose)}
  .merge p{margin:0;color:var(--muted);font-size:.92rem;line-height:1.55}
  .merge p b{color:var(--ink)}
  .merge .acts{display:flex;gap:8px;align-items:center}
  .askline{margin-top:24px}
  .askline .cells{display:grid;grid-template-columns:repeat(var(--n),minmax(0,1fr));gap:4px;height:48px}
  .askline .cell{display:flex;flex-direction:column-reverse;gap:2px;border-radius:6px;background:var(--bg-soft);overflow:hidden;cursor:default;transition:transform .15s ease}
  .askline .cell i{display:block;min-height:4px}
  .askline .cell.is-on:hover{transform:translateY(-2px)}
  .askline .cell.is-now{outline:1.5px solid var(--line-2);outline-offset:2px}
  .askline .ends{display:flex;justify-content:space-between;margin-top:10px;font-size:.78rem;color:var(--muted)}
  .legend{display:flex;gap:18px;flex-wrap:wrap;margin-top:10px;font-size:.88rem;color:var(--muted)}
  .legend span{display:inline-flex;align-items:center;gap:7px}
  .legend span::before{content:"";width:10px;height:10px;border-radius:3px;background:var(--c)}
  .legend b{color:var(--ink)}
  .dsplit{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:28px;margin-top:28px;padding-top:28px;border-top:1px solid var(--line)}
  .dsec{margin-top:28px;padding-top:24px;border-top:1px solid var(--line)}
  .dsplit h4,.dsec h4{margin:0 0 14px;font-size:.98rem;font-weight:700}
  .dsec > p{margin:0 0 6px;color:var(--muted)}
  .asked{list-style:none;margin:0;padding:0;display:grid;gap:14px}
  .asked li{display:grid;grid-template-columns:20px minmax(0,1fr) auto;gap:12px;align-items:start;font-size:.95rem;line-height:1.45}
  .asked .ico{color:var(--rose);margin-top:1px}
  .asked time{color:var(--muted);font-size:.82rem;white-space:nowrap;padding-top:2px}
  .linkbtn{border:0;background:none;padding:0;font:inherit;font-size:.86rem;font-weight:600;color:#B73C54;cursor:pointer}
  .linkbtn:hover{text-decoration:underline;text-underline-offset:3px}
  .sidebox{border:1px dashed var(--line-2);border-radius:14px;padding:22px 24px;align-self:start}
  .sidebox h4{margin:0 0 6px}
  .sidebox p{margin:0;color:var(--muted);font-size:.92rem;line-height:1.6}
  .sidebox .btn{margin-top:16px}
  .sidebox .ans{font-size:.92rem;line-height:1.6;margin-top:8px}
  .mention{display:grid;grid-template-columns:20px minmax(0,1fr);gap:12px;padding:16px 0;border-top:1px solid var(--line)}
  .mention:first-of-type{border-top:0}
  .mention .ico{color:var(--muted)}
  .mention small{display:block;color:var(--muted);font-size:.82rem;margin-bottom:4px}
  .mention div{font-size:.98rem}
  mark{background:var(--amber-soft);color:inherit;padding:0 2px;border-radius:4px}
  .quote{padding:14px 16px;border-radius:12px;background:var(--bg-soft);font-size:.95rem;line-height:1.55}
  .dfoot{display:flex;align-items:center;gap:12px 20px;flex-wrap:wrap;padding:18px 34px;border-top:1px solid var(--line)}
  .btn--go{display:inline-flex;align-items:center;gap:10px;height:48px;padding:0 24px;border-radius:999px;border:1px solid var(--rose);background:var(--rose);color:#fff;font-weight:600;font-size:.95rem;text-decoration:none;white-space:nowrap}
  .btn--go:hover{background:#D24E67;border-color:#D24E67;color:#fff;text-decoration:none}
  .btn--ink{background:var(--ink);border-color:var(--ink);color:var(--bg)}
  .btn--ink:hover{background:var(--ink);opacity:.9;color:var(--bg)}
  .ghost{display:inline-flex;align-items:center;gap:8px;height:40px;padding:0 6px;border:0;background:none;font:inherit;font-size:.95rem;color:var(--muted);cursor:pointer;white-space:nowrap}
  .ghost:hover{color:var(--ink)}
  .ghost.on{color:var(--success)}
  .pillbtn{display:inline-flex;align-items:center;gap:8px;height:44px;padding:0 20px;border-radius:999px;border:1px solid var(--line-2);background:var(--panel);font:inherit;font-size:.95rem;color:var(--ink);cursor:pointer;white-space:nowrap}
  .pillbtn:hover{border-color:rgba(36,26,20,.3)}
  .pillbtn.on{border-color:rgba(63,143,95,.4);color:var(--success)}
  kbd{display:inline-grid;place-items:center;min-width:24px;height:24px;padding:0 6px;border:1px solid var(--line-2);border-radius:6px;font:600 .74rem var(--body);color:var(--muted);background:var(--panel)}
  .keys{margin-left:auto;display:flex;align-items:center;gap:6px;font-size:.84rem;color:var(--muted)}
  /* trends */
  .tleg{display:flex;align-items:center;gap:22px;flex-wrap:wrap;margin:0 0 18px;font-size:.88rem;color:var(--muted)}
  .tleg span{display:inline-flex;align-items:center;gap:10px}
  .tleg .cur::before{content:"";width:22px;border-top:2px solid var(--ink)}
  .tleg .prv::before{content:"";width:22px;border-top:2px dashed var(--muted)}
  .tleg small{font-size:.82rem;opacity:.75}
  .tgrid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:20px}
  .tcard{display:flex;flex-direction:column;background:var(--panel);border:1px solid var(--line);border-radius:20px;overflow:hidden}
  .tcard__head{display:flex;align-items:flex-start;justify-content:space-between;gap:12px;padding:22px 24px 0}
  .tcard__num{text-align:right}
  .tcard__num > b{display:block;font-family:var(--display);font-weight:700;font-size:2rem;line-height:1}
  .tcard__num small{display:block;margin-top:6px;font-size:.84rem;color:var(--muted)}
  .tcard__num small b{color:var(--ink);font-weight:700}
  .tplot{position:relative;height:190px;margin:16px 24px 0;cursor:crosshair}
  .tplot svg{position:absolute;inset:0;width:100%;height:100%;overflow:visible}
  .tplot .xl{position:absolute;bottom:-24px;font-size:.78rem;color:var(--muted);white-space:nowrap}
  .tplot .vl{position:absolute;top:0;bottom:0;border-left:1px solid var(--line-2);pointer-events:none}
  .tplot .hd{position:absolute;width:10px;height:10px;border-radius:50%;transform:translate(-50%,-50%);box-shadow:0 0 0 2px var(--panel);pointer-events:none}
  .tplot .ttip{position:absolute;top:-6px;padding:6px 10px;border:1px solid var(--line);border-radius:10px;background:var(--panel);box-shadow:0 10px 24px -16px rgba(36,26,20,.4);font-size:.78rem;color:var(--muted);white-space:nowrap;pointer-events:none}
  .tplot .ttip b{color:var(--ink)}
  .tcard__foot{display:grid;grid-template-columns:auto minmax(0,1fr);gap:28px;margin-top:44px;padding:16px 24px 18px;border-top:1px solid var(--line)}
  .tcard__foot small{display:block;margin-bottom:4px;font-size:.8rem;color:var(--muted)}
  .tcard__foot > div > b{font-weight:700}
  .tcard__foot .rising{display:block;max-width:100%;color:var(--ink);white-space:nowrap}
  @media (max-width:1000px){.tgrid{grid-template-columns:1fr}}
  .chhead{display:flex;align-items:center;justify-content:space-between;gap:12px;flex-wrap:wrap;padding:24px 30px 0}
  .chhead h3{margin:0;font-size:1.02rem;font-weight:600}
  .lchips{display:flex;gap:8px;flex-wrap:wrap}
  .lchips button{display:inline-flex;align-items:center;gap:8px;height:34px;padding:0 14px;border-radius:999px;border:1px solid var(--line);background:var(--panel);font:inherit;font-size:.88rem;color:var(--muted);cursor:pointer}
  .lchips button::before{content:"";width:9px;height:9px;border-radius:50%;background:var(--c)}
  .lchips button[aria-pressed="false"]{opacity:.45}
  .plot{position:relative;height:300px;margin:18px 30px 0 64px}
  .plot svg{position:absolute;inset:0;width:100%;height:100%;overflow:visible}
  .plot .grid{position:absolute;left:0;right:0;border-top:1px solid var(--line)}
  .plot .yl{position:absolute;left:-40px;transform:translateY(-50%);font-size:.8rem;color:var(--muted)}
  .plot .xl{position:absolute;bottom:-28px;transform:translateX(-50%);font-size:.8rem;color:var(--muted);white-space:nowrap}
  .plot .hit{position:absolute;inset:0;cursor:crosshair}
  .plot .vl{position:absolute;top:0;bottom:0;border-left:1px solid var(--line-2);pointer-events:none}
  .plot .hd{position:absolute;width:11px;height:11px;border-radius:50%;transform:translate(-50%,-50%);box-shadow:0 0 0 2px var(--panel);pointer-events:none}
  .plot .tip{position:absolute;top:18px;min-width:170px;padding:14px 16px;border:1px solid var(--line);border-radius:12px;background:var(--panel);box-shadow:0 18px 40px -22px rgba(36,26,20,.5);pointer-events:none;font-size:.88rem;z-index:2}
  .plot .tip b{display:block;margin-bottom:8px}
  .plot .tip div{display:flex;align-items:center;gap:8px;padding:2px 0}
  .plot .tip div::before{content:"";width:9px;height:9px;border-radius:50%;background:var(--c)}
  .plot .tip div span{flex:1;color:var(--muted)}
  .plot .tip div em{font-style:normal;font-weight:700}
  .ctable{margin-top:48px;border-top:1px solid var(--line)}
  .crow{display:grid;grid-template-columns:minmax(130px,1fr) minmax(110px,.8fr) minmax(150px,1fr) minmax(220px,1.4fr) minmax(200px,1.7fr);gap:16px;align-items:center;padding:20px 30px}
  .crow + .crow{border-top:1px solid var(--line)}
  .crow.hdr{padding:16px 30px;font-size:.88rem;color:var(--muted)}
  .chn{display:flex;align-items:center;gap:14px;font-size:.98rem}
  .chn span{width:40px;height:40px;border-radius:50%;display:grid;place-items:center;color:var(--c);background:color-mix(in srgb,var(--c) 14%,transparent)}
  .asks b{font-family:var(--display);font-weight:600;font-size:1.4rem;margin-right:8px}
  .asks small{font-size:.84rem;color:var(--muted);white-space:nowrap}
  .crow svg{width:100%;max-width:200px;height:36px;overflow:visible}
  .rate{display:flex;align-items:center;gap:14px;font-size:.98rem}
  .rate .bar{width:130px;height:8px;border-radius:999px;background:var(--line);overflow:hidden;flex:none}
  .rate .bar span{display:block;height:100%;border-radius:999px;background:var(--ink)}
  .rate small{font-size:.84rem;font-weight:600}
  .rising{border:0;background:none;padding:0;text-align:left;font:inherit;font-size:.95rem;color:var(--muted);cursor:pointer;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
  .rising:hover{color:#B73C54;text-decoration:underline;text-underline-offset:3px}
  /* opportunities */
  .owrap{display:grid;grid-template-columns:minmax(220px,320px) minmax(0,1fr);gap:30px;align-items:start}
  .themes{display:grid;gap:4px}
  .ocol{position:sticky;top:110px}
  .osync{display:flex;align-items:center;justify-content:space-between;gap:10px;margin:0 0 10px;padding:0 4px 0 16px;min-height:32px}
  .osync .found{font-size:.8rem}
  .osync__btn{display:inline-flex;align-items:center;gap:6px;height:32px;padding:0 12px;border-radius:999px;border:1px solid var(--line-2);background:var(--panel);font:inherit;font-size:.8rem;font-weight:600;color:var(--ink);cursor:pointer;white-space:nowrap}
  .osync__btn:hover{border-color:#FFB199}
  .osync__btn:disabled{opacity:.6;cursor:default}
  .osync__btn svg{width:14px;height:14px}
  .theme{display:grid;grid-template-columns:minmax(0,1fr) auto;gap:8px 12px;width:100%;text-align:left;padding:14px 18px;border:0;border-radius:14px;background:none;font:inherit;color:inherit;cursor:pointer}
  .theme:hover{background:var(--bg-soft)}
  .theme.is-sel{background:var(--panel);box-shadow:0 1px 0 var(--line),0 10px 24px -20px rgba(36,26,20,.45)}
  .theme b{font-weight:500;font-size:.98rem}
  .theme .tb{grid-column:1/-1;height:5px;border-radius:999px;background:var(--line);overflow:hidden}
  .theme .tb span{display:block;height:100%;border-radius:999px;background:var(--rose)}
  .theme small{grid-column:1/-1;margin-top:-2px;font-size:.82rem;color:var(--muted)}
  .ohead{display:flex;align-items:baseline;gap:12px;justify-content:space-between;margin:2px 0 14px}
  .ohead h3{margin:0;font-family:var(--display);font-size:1.35rem;font-weight:700}
  .ohead p{margin:4px 0 0;color:var(--muted)}
  .ohead span{flex:none;font-size:.88rem;color:var(--muted)}
  .oacc{list-style:none;margin:0;padding:0;background:var(--panel);border:1px solid var(--line);border-radius:18px;overflow:hidden}
  .oitem + .oitem{border-top:1px solid var(--line)}
  .ohd{display:grid;grid-template-columns:minmax(0,1fr) auto 20px;gap:4px 16px;align-items:start;width:100%;text-align:left;padding:22px 28px;border:0;background:none;font:inherit;color:inherit;cursor:pointer}
  .ohd:hover{background:var(--bg-soft)}
  .ohd b{font-weight:600;font-size:1.02rem}
  .ohd .ds{grid-column:1;color:var(--muted);font-size:.92rem;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
  .oitem.is-open .ohd .ds{display:none}
  .ohd .on{grid-row:1/3;grid-column:2;text-align:center;font-family:var(--display);font-weight:700;font-size:1.25rem;line-height:1.2}
  .ohd .on small{display:block;font:500 .74rem var(--body);color:var(--muted)}
  .ohd .chev{grid-row:1/3;grid-column:3;color:var(--muted);margin-top:8px;transition:transform .15s ease}
  .oitem.is-open .ohd .chev{transform:rotate(180deg)}
  .tag{display:inline-flex;align-items:center;height:24px;padding:0 10px;margin-left:10px;border-radius:999px;font-size:.78rem;font-weight:600;vertical-align:2px}
  .tag.feature{background:rgba(62,111,166,.1);color:var(--info)} .tag.expansion{background:rgba(63,143,95,.1);color:var(--success)}
  .obody{padding:0 28px 24px}
  .obody > p{margin:0 0 18px;line-height:1.75;font-size:.98rem}
  .obody h5{margin:0 0 10px;font-size:.88rem;font-weight:600;color:var(--muted)}
  .oq{display:grid;grid-template-columns:20px minmax(0,1fr) auto;gap:12px;align-items:start;margin-bottom:8px}
  .oq .ico{color:var(--amber);margin-top:2px}
  .oq time{font-size:.82rem;color:var(--muted);white-space:nowrap}
  .oacts{display:flex;align-items:center;gap:18px;margin-top:18px}
  .ooff{margin-top:12px;font-size:.86rem;color:var(--muted)}
  .tempty{padding:34px 24px;text-align:center;color:var(--muted);font-size:.9rem}
  .tempty b{display:block;color:var(--ink);font-size:.98rem;margin-bottom:4px}
  .spin{display:inline-block;width:14px;height:14px;border-radius:50%;border:2px solid currentColor;border-right-color:transparent;animation:spin .7s linear infinite;vertical-align:-2px}
  @media (max-width:1100px){.crow{grid-template-columns:minmax(120px,1fr) minmax(100px,.8fr) minmax(200px,1.4fr)}.crow > :nth-child(3),.crow > :nth-child(5){display:none}}
  @media (max-width:1000px){.wrap2,.owrap{grid-template-columns:1fr}.tlist,.ocol{position:static}.dsplit{grid-template-columns:1fr}.dbody{padding:24px 22px}.dfoot{padding:16px 22px}.keys{display:none}}
  @media (max-width:640px){.plot{margin-left:46px;margin-right:16px}.crow{grid-template-columns:1fr 1fr;padding:16px 18px}.crow > :nth-child(4){grid-column:1/-1}.crow.hdr{display:none}.merge{grid-template-columns:1fr}.merge > .ico{display:none}}
""",
  body=r"""
    <div class="head">
      <div>
        <p class="label">03 Insights · Monitoring</p>
        <h1>Insights</h1>
        <p>What people keep asking, and what you don’t have an answer for yet: from chat, email, calls and your documents.</p>
      </div>
      <span class="spacer"></span>
      <button class="btn btn--secondary btn--sm fsbtn" id="fsBtn" type="button" aria-pressed="false" title="Full screen (F)"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M15 3h6v6M9 21H3v-6M21 3l-7 7M3 21l7-7"/></svg><span>Full screen</span></button>
    </div>
    <div class="utabs" role="tablist" aria-label="Insights">
      <button class="utab" role="tab" data-tab="q" aria-selected="true">Recurring questions</button>
      <button class="utab" role="tab" data-tab="g" aria-selected="false">Knowledge gaps</button>
      <button class="utab" role="tab" data-tab="t" aria-selected="false">Trends</button>
      <button class="utab" role="tab" data-tab="o" aria-selected="false">Opportunities</button>
    </div>

    <section id="tabQ">
      <div class="ihead">
        <div></div>
        <div class="segp" id="qRange" role="group" aria-label="Period"><button data-r="day" aria-pressed="false">Day</button><button data-r="week" aria-pressed="false">Week</button><button data-r="month" aria-pressed="true">Month</button></div>
      </div>
      <div class="wrap2"><aside class="tlist" id="qList" aria-label="Recurring questions"></aside><section id="qDetail" aria-live="polite"></section></div>
    </section>

    <section id="tabG" hidden>
      <div class="ihead">
        <div></div>
        <div class="segp" id="gFil" role="group" aria-label="Show"><button data-f="all" aria-pressed="true">All</button><button data-f="never" aria-pressed="false">Never explained</button><button data-f="un" aria-pressed="false">Unanswered</button><button data-f="wrong" aria-pressed="false">Marked wrong</button></div>
      </div>
      <div class="wrap2"><aside class="tlist" id="gList" aria-label="Knowledge gaps"></aside><section id="gDetail" aria-live="polite"></section></div>
    </section>

    <section id="tabT" hidden>
      <div class="ihead">
        <div></div>
        <div class="segp" id="tRange" role="group" aria-label="Period"><button data-r="week" aria-pressed="false">Week</button><button data-r="month" aria-pressed="true">Month</button></div>
      </div>
      <div class="tleg"><span class="cur">This period</span><span class="prv" id="tPrev">Previous 30 days</span><small>All charts share one scale, so heights compare directly.</small></div>
      <div class="tgrid" id="tGrid"></div>
    </section>

    <section id="tabO" hidden>
      <div class="ihead">
        <div></div>
        <div class="ictl">
          <div class="segp" id="oFil" role="group" aria-label="Show"><button data-f="all" aria-pressed="true">All</button><button data-f="feature" aria-pressed="false">Feature requests</button><button data-f="expansion" aria-pressed="false">Expansion</button></div>
        </div>
      </div>
      <div class="owrap"><div class="ocol"><div class="osync"><span class="found" id="oFound"></span><button class="osync__btn" id="oRefresh" type="button"></button></div><nav class="themes" id="oThemes" aria-label="Themes"></nav></div><section id="oDetail"></section></div>
    </section>
""",
  js=r"""
// full screen, as in Build: hides the sidebar and widens both columns; F toggles, Esc leaves
function setFs(on) {
  document.body.classList.toggle('is-fs', on); $('fsBtn').setAttribute('aria-pressed', on);
  $('fsBtn').querySelector('span').textContent = on ? 'Exit full screen' : 'Full screen';
  $('fsBtn').querySelector('svg').innerHTML = on ? '<path d="M4 14h6v6M20 10h-6V4M14 10l7-7M3 21l7-7"/>' : '<path d="M15 3h6v6M9 21H3v-6M21 3l-7 7M3 21l7-7"/>';
  try { sessionStorage.setItem('lojo-ins-fs', on ? '1' : ''); } catch (err) {}
}
$('fsBtn').addEventListener('click', () => setFs(!document.body.classList.contains('is-fs')));
try { if (sessionStorage.getItem('lojo-ins-fs')) setFs(true); } catch (err) {}
document.addEventListener('keydown', (e) => {
  if (e.target.closest('input,textarea,select') || e.metaKey || e.ctrlKey || document.querySelector('dialog[open]')) return;
  if (e.key.toLowerCase() === 'f') setFs(!document.body.classList.contains('is-fs'));
  if (e.key === 'Escape' && document.body.classList.contains('is-fs')) setFs(false);
});

const I = (d) => '<svg class="ico" viewBox="0 0 24 24" aria-hidden="true">' + d + '</svg>';
const IC = {
  c: '<path d="M21 12a8 8 0 0 1-11.6 7.1L4 20l1-4.6A8 8 0 1 1 21 12z"/>',
  e: '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/>',
  k: '<path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1.9.4 1.8.7 2.7a2 2 0 0 1-.5 2.1L8 9.8a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.7.7a2 2 0 0 1 1.7 2z"/>',
  d: '<path d="M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8z"/><path d="M14 3v5h5M9 13h6M9 17h4"/>',
  book: '<path d="M2 5h6a4 4 0 0 1 4 4v11a3 3 0 0 0-3-3H2z"/><path d="M22 5h-6a4 4 0 0 0-4 4v11a3 3 0 0 1 3-3h7z"/>',
  help: '<circle cx="12" cy="12" r="9"/><path d="M9.5 9.5a2.5 2.5 0 1 1 3.5 2.3c-.6.3-1 .8-1 1.5V14M12 17h.01"/>',
  down: '<path d="M17 3v11M9.5 21 11 15H5a2 2 0 0 1-2-2.3l1.3-7.5A2 2 0 0 1 6.3 3H17h3v11h-3l-4.5 7z"/>',
  merge: '<circle cx="6" cy="5" r="2.5"/><circle cx="18" cy="19" r="2.5"/><path d="M6 7.5V11a8 8 0 0 0 8 8h1.5"/>',
  check: '<path d="m5 12 5 5 9-10"/>',
  refresh: '<path d="M21 12a9 9 0 0 1-15.5 6.2L3 16M3 12a9 9 0 0 1 15.5-6.2L21 8M21 3v5h-5M3 21v-5h5"/>',
  chev: '<path d="m6 9 6 6 6-6"/>',
};
const CH = { c: 'Chat', e: 'Email', k: 'Calls', d: 'Documents' };
const CH_COLOR = { c: 'var(--rose)', e: 'var(--amber)', k: 'var(--info)', d: '#A39890' };
const NOW = new Date(2026, 9, 19, 15, 0);
const DAY = 864e5;
const ago = (d) => { const h = Math.round((NOW - d) / 36e5); if (h < 1) return 'just now'; if (h < 24) return h + ' hour' + (h === 1 ? '' : 's') + ' ago'; const n = Math.round(h / 24); return n + ' day' + (n === 1 ? '' : 's') + ' ago'; };
const dm = (d) => d.getDate() + ' ' + d.toLocaleString('en-GB', { month: 'short' });
const plural = (n, one, many) => n + ' ' + (n === 1 ? one : (many || one + 's'));
['merged', 'keepSep', 'gapDone', 'oppOff'].forEach(k => { ST[k] = ST[k] || {}; });
ST.draftFailed = ST.draftFailed || {};

// every time a question came in: channel (c chat, e email, k call, d documents), day in October, hour
const ASKED = {
  q22: 'k2.10 e6.14 c9.11 c13.15 k15.10 c17.9 e18.16 c19.11', q9: 'd4.9 c4.15 c8.10 e12.14 c16.11 c18.15 c19.9',
  q1: 'd4.10 e6.11 c11.9 k14.13 c16.10 e19.10', q21: 'e5.15 c10.12 c15.14 c18.10 e19.13', q10: 'c4.11 d4.12 c13.16 c18.14',
  q5: 'k4.11 c9.10 c17.15', q8: 'e6.10 c12.11 e17.9', q2: 'c3.14 c16.9 c19.15', q23: 'k8.10 c14.11 k18.12',
  q17: 'k5.9 c15.10', q16: 'e3.11 c13.14', q4: 'c7.10 d4.13', q7: 'c9.9 c17.10', q12: 'c11.15 k18.11',
  q19: 'c12.9 c16.16', q20: 'e14.10 c18.9', q3: 'd4.14 c19.12', q11: 'k3.15 e9.10', q14: 'e7.11',
};
const ASKS = Object.fromEntries(Object.entries(ASKED).map(([id, v]) => [id, v.split(' ').map(t => { const [d, h] = t.slice(1).split('.'); return { ch: t[0], at: new Date(2026, 9, +d, +h) }; })]));
const asksFor = (id) => (ASKS[id] || []).concat(...Object.keys(ST.merged).filter(k => ST.merged[k] === id).map(k => ASKS[k] || []));
// the different ways people put each question
const HEARD = {
  q22: ['What’s the chargeback fee on Scale?', 'how much per dispute', 'Is there a fee when a customer disputes a payment?', 'We had two disputes, what will we be charged?', 'chargeback cost?'],
  q9: ['API limits on Growth?', 'whats the api limit', 'api limit?', 'How many requests per second can we make?'],
  q1: ['Is SSO included on Growth?', 'SSO says “not available on your plan”', 'Do we need Enterprise for SAML?', 'okta login on growth?'],
  q21: ['Do you support Apple Pay in Germany?', 'apple pay germany', 'Can customers in Berlin pay with Apple Pay?'],
  q10: ['We’re getting 429 errors, why?', 'what happens over the rate limit', 'What does Retry-After mean?'],
  q5: ['Can we move to Scale mid-cycle?', 'How is an upgrade billed mid-month?', 'upgrade to scale now?'],
  q8: ['Can Starter pay by invoice?', 'Our finance team needs an invoice with a PO number', 'bank transfer on starter?'],
  q2: ['How long do we have to ask for a refund?', 'refund window?', 'Can I still get a refund after 3 weeks?'],
  q23: ['How long do you keep call recordings?', 'when are recordings deleted', 'Retention period for calls?'],
};
// likely the same question asked two ways
const MERGE = { q10: ['q9', 'Both ask about API request limits.'], q12: ['q11', 'Both ask about chargeback disputes.'] };

const RANGES = { day: { slots: 12, ms: 2 * 36e5, now: 'today', labels: [0, 2, 4, 6, 8, 10] }, week: { slots: 7, ms: DAY, now: 'this week', labels: [0, 1, 2, 3, 4, 5, 6] }, month: { slots: 30, ms: DAY, now: 'in the last 30 days', labels: [0, 7, 14, 21, 28] } };
const END = +new Date(2026, 9, 20);
const winFor = (r) => [END - RANGES[r].slots * RANGES[r].ms, END];
const inWin = (list, [a, b]) => list.filter(x => x.at >= a && x.at < b);
const isApproved = (q) => { const r = draftByQ(q.id); return !!r && decision(r).status === 'approved'; };
const qById = (id) => allQuestions().find(q => q.id === id);
const buildHref = (q) => { const r = draftByQ(q.id); return r ? 'build.html?sel=' + r.id : 'build.html?q=' + q.id; };
function dotsFor(list, r) {
  const R = RANGES[r], [a] = winFor(r), bins = Array.from({ length: R.slots }, () => ({}));
  list.forEach(x => { const i = Math.floor((x.at - a) / R.ms); if (i >= 0 && i < R.slots) bins[i][x.ch] = (bins[i][x.ch] || 0) + 1; });
  const when = (i) => { const t = new Date(a + i * R.ms); return r === 'day' ? String(t.getHours()).padStart(2, '0') + ':00' : t.toLocaleString('en-GB', { weekday: 'short' }) + ' ' + dm(t); };
  const chs = (b) => Object.keys(CH).filter(k => b[k]);
  return '<div class="askline" aria-label="' + plural(list.length, 'ask') + ' ' + R.now + '"><div class="cells" style="--n:' + R.slots + '">' + bins.map((b, i) => {
    const n = Object.values(b).reduce((s, v) => s + v, 0), last = i === R.slots - 1;
    return '<span class="cell' + (n ? ' is-on' : '') + (last ? ' is-now' : '') + '" title="' + (last ? (r === 'day' ? 'Now' : 'Today') : when(i)) + ' · ' + (n ? plural(n, 'ask') + ': ' + chs(b).map(k => b[k] + ' ' + CH[k].toLowerCase()).join(', ') : 'no asks') + '">' +
      chs(b).map(k => '<i style="flex:' + b[k] + ';background:' + CH_COLOR[k] + '"></i>').join('') + '</span>';
  }).join('') + '</div><div class="ends"><span>' + when(0) + '</span><span>' + (r === 'day' ? 'Now' : 'Today') + '</span></div></div>' +
    '<div class="legend">' + Object.keys(CH).map(k => [k, list.filter(x => x.ch === k).length]).filter(([, n]) => n).map(([k, n]) => '<span style="--c:' + CH_COLOR[k] + '"><b>' + n + '</b>' + CH[k].toLowerCase() + '</span>').join('') + '</div>';
}
function askedList(q, list, all) {
  const ph = HEARD[q.id] || [q.q], rows = list.slice().sort((a, b) => b.at - a.at), shown = all ? rows : rows.slice(0, 4);
  return '<ul class="asked">' + shown.map((x, i) => '<li>' + I(IC[x.ch]) + '<span>“' + esc(ph[rows.indexOf(x) % ph.length]) + '”</span><time>' + dm(x.at) + '</time></li>').join('') + '</ul>' +
    (rows.length > shown.length ? '<button class="linkbtn" data-more="1" style="margin-top:12px">+' + (rows.length - shown.length) + ' more</button>' : '');
}
function footer(primary, extra) {
  return '<div class="dfoot">' + primary + (extra || '') + '<span class="keys"><kbd>J</kbd><kbd>K</kbd> to move</span></div>';
}
function progress(done, total) { return '<span class="trk"><span style="width:' + (total ? done / total * 100 : 0) + '%"></span></span><span><b>' + done + '</b> of ' + total + ' handled</span>'; }
function listGroup(key, label, items, render, openSet) {
  if (!items.length) return '';
  return '<details class="tgroup" data-g="' + key + '"' + (openSet.has(key) ? ' open' : '') + '><summary>' + label + ' · ' + items.length + '</summary>' + items.map(render).join('') + '</details>';
}

// ---------- Recurring questions
let qRange = 'month', qSel = null, qMore = false;
const qOpen = new Set();
function qRows() {
  const w = winFor(qRange);
  return allQuestions().filter(q => !ST.merged[q.id]).map(q => ({ q, r: draftByQ(q.id), list: inWin(asksFor(q.id), w) })).filter(x => x.list.length)
    .sort((a, b) => b.list.length - a.list.length);
}
const qState = (x) => isApproved(x.q) ? 'ok' : matters(x.q) === false ? 'out' : 'todo';
// list rows follow Build: emoji avatar, title, tag, count pill on the right, plain status text for failures
const RAV = { q: ['❓', 'rav--question'], gap: ['🧩', 'rav--gap'], fail: ['⚠️', 'rav--failed'], down: ['👎', 'rav--down'] };
const rav = (k) => '<span class="rav ' + RAV[k][1] + '" aria-hidden="true">' + RAV[k][0] + '</span>';
const CNT_IC = { ask: '<path d="M21 12a8 8 0 0 1-11.6 7.1L4 20l1-4.6A8 8 0 1 1 21 12z"/>', doc: '<path d="M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8z"/><path d="M14 3v5h5"/>' };
const cntPill = (n, ic, label) => '<span class="srcb" title="' + label + '" aria-label="' + label + '"><svg viewBox="0 0 24 24" aria-hidden="true">' + CNT_IC[ic] + '</svg>' + n + '</span>';
function qLabel(x) {
  const s = qState(x);
  if (s === 'ok') return ['Approved', 'c-green'];
  if (s === 'out') return ['Left out', 'c-grey'];
  if (ST.draftFailed[x.q.id]) return ['Draft failed', 'c-red'];
  if (x.r) return ['Draft', 'c-grey'];
  return ['No answer', 'c-amber'];
}
function renderQ() {
  const rows = qRows(), by = (s) => rows.filter(x => qState(x) === s), todo = by('todo');
  if (!rows.some(x => x.q.id === qSel)) qSel = (todo[0] || rows[0] || {}).q?.id || null;
  const R = RANGES[qRange], n = todo.reduce((a, x) => a + x.list.length, 0);
  const item = (x) => { const [l, c] = qLabel(x);
    const failed = l === 'Draft failed', n = x.list.length;
    return '<button class="titem is-row' + (failed ? ' is-failed' : '') + (x.q.id === qSel ? ' is-sel' : '') + '" data-sel="' + x.q.id + '">' + rav(failed ? 'fail' : x.q.gap ? 'gap' : 'q') + '<b>' + esc(x.q.q) + '</b>' +
      '<span class="tmeta"><span class="badge badge--q">Question</span>' + (failed ? '' : '<span class="badge ' + (c === 'c-amber' ? 'badge--amber' : c === 'c-green' ? 'badge--ok' : 'badge--muted') + '">' + l + '</span>') + '</span>' +
      '<span class="tside">' + (failed ? '<em class="tfail">Draft failed</em>' : '') + cntPill(n, 'ask', 'Asked ' + n + (n === 1 ? ' time' : ' times')) + '</span></button>'; };
  $('qList').innerHTML = '<div class="th"><span>To handle</span><span>' + todo.length + '</span></div>' + (todo.length ? todo.map(item).join('') : '<div class="tnone">Nothing to handle ' + R.now + '.</div>') +
    listGroup('ok', 'Approved', by('ok'), item, qOpen) + listGroup('out', 'Left out', by('out'), item, qOpen);
  renderQDetail(rows.find(x => x.q.id === qSel));
}
function renderQDetail(x) {
  if (!x) { $('qDetail').innerHTML = '<div class="dcard tempty"><b>Nothing asked ' + RANGES[qRange].now + '</b>Try Week or Month.</div>'; return; }
  const q = x.q, r = x.r, s = qState(x), failed = ST.draftFailed[q.id], last = x.list.reduce((a, y) => y.at > a ? y.at : a, x.list[0].at);
  const pill = s === 'ok' ? '<span class="pill green">' + I(IC.check) + 'Approved answer</span>' : s === 'out' ? '<span class="pill grey"><span class="dot"></span>Left out</span>'
    : failed ? '<span class="pill red"><span class="dot"></span>Draft failed</span>' : r ? '<span class="pill grey"><span class="dot"></span>Draft waiting for review</span>' : '<span class="pill amber"><span class="dot"></span>No approved answer yet</span>';
  const m = MERGE[q.id], target = m && qById(m[0]);
  const merge = m && target && !ST.keepSep[q.id] && !ST.merged[m[0]] ? '<div class="merge">' + I(IC.merge) + '<p><b>Looks like the same question as “' + esc(target.q) + '”</b>. ' + esc(m[1]) + ' Merging keeps “' + esc(target.q) + '” and combines the asks.</p><div class="acts"><button class="ghost" data-keep="' + q.id + '">Keep separate</button><button class="pillbtn" data-merge="' + q.id + '">Merge</button></div></div>' : '';
  let side, primary;
  if (s === 'ok') { side = '<h4>The approved answer</h4><div class="ans md">' + md(answerOf(r)) + '</div><a class="btn btn--secondary" href="' + buildHref(q) + '">Open in Build</a>'; primary = '<a class="btn--go btn--ink" href="' + buildHref(q) + '">Edit in Build →</a>'; }
  else if (failed) { side = '<h4>Drafting failed</h4><p>' + esc(failed) + '</p><a class="btn btn--secondary" href="' + buildHref(q) + '">Open in Build</a>'; primary = '<a class="btn--go" href="' + buildHref(q) + '">Try again in Build →</a>'; }
  else if (r) { side = '<h4>A draft is waiting in Build</h4><p>“' + esc(answerOf(r).replace(/[#*_>]+/g, '').slice(0, 150)) + (answerOf(r).length > 150 ? '…' : '') + '”</p><a class="btn btn--secondary" href="' + buildHref(q) + '">Open in Build</a>'; primary = '<a class="btn--go" href="' + buildHref(q) + '">Review the draft →</a>'; }
  else if (q.docs && q.docs.length) { side = '<h4>Your documents cover this</h4><p>Lojo can draft it from ' + esc(q.docs.map(docShort).join(', ')) + '. Check it in Build before it goes live.</p><a class="btn btn--secondary" href="' + buildHref(q) + '">Open in Build</a>'; primary = '<a class="btn--go" href="' + buildHref(q) + '">Write an answer →</a>'; }
  else { side = '<h4>Nothing in your documents answers this yet</h4><p>Write an answer once and Lojo reuses it every time the question comes up.</p><a class="btn btn--secondary" href="' + buildHref(q) + '">Open in Build</a>'; primary = '<a class="btn--go" href="' + buildHref(q) + '">Write an answer →</a>'; }
  $('qDetail').innerHTML = '<article class="dcard"><div class="dbody"><div class="dtop"><div><h2>' + esc(q.q) + '</h2><p class="dsub">Last asked ' + ago(last) + '</p>' + pill + '</div>' +
    '<div class="dnum"><b>' + x.list.length + '</b><span>times ' + RANGES[qRange].now + '</span></div></div>' + merge + dotsFor(x.list, qRange) +
    '<div class="dsplit"><div><h4>How people asked it</h4>' + askedList(q, x.list, qMore) + '</div><div class="sidebox">' + side + '</div></div></div>' +
    footer(primary) + '</article>';
}
function moveSel(list, cur, dir) { const i = list.indexOf(cur); return list[Math.min(list.length - 1, Math.max(0, (i < 0 ? 0 : i + dir)))]; }
$('qList').addEventListener('click', (e) => {
  const b = e.target.closest('[data-sel]'); if (b) { qSel = b.dataset.sel; qMore = false; renderQ(); return; }
  const g = e.target.closest('summary'); if (g) { const k = g.parentElement.dataset.g; qOpen.has(k) ? qOpen.delete(k) : qOpen.add(k); }
});
$('qDetail').addEventListener('click', (e) => {
  const t = e.target.closest('button'); if (!t) return;
  if (t.dataset.more) { qMore = true; renderQ(); }
  if (t.dataset.keep) { ST.keepSep[t.dataset.keep] = true; save(); renderQ(); toast('Kept as two questions'); }
  if (t.dataset.merge) { const id = t.dataset.merge; ST.merged[id] = MERGE[id][0]; qSel = MERGE[id][0]; save(); renderQ(); toast('Merged. The asks are combined.'); }
});
document.querySelector('#qRange').addEventListener('click', (e) => { const b = e.target.closest('[data-r]'); if (!b) return; qRange = b.dataset.r; document.querySelectorAll('#qRange button').forEach(x => x.setAttribute('aria-pressed', x === b)); renderQ(); });


// ---------- Knowledge gaps
const GAP_SEEN = { g1: [17, 11], g2: [18, 16], g3: [18, 12], g4: [12, 9], g5: [18, 16] };
const WRONG = [
  { id: 'w1', qid: 'q5', said: 'Can I downgrade from Scale to Growth mid-cycle?', reports: 1, at: new Date(2026, 9, 17, 10), why: 'The answer only covers upgrades. It doesn’t say downgrades wait for the next renewal.' },
  { id: 'w2', qid: 'q9', said: 'Does the API rate limit apply per user?', reports: 1, at: new Date(2026, 9, 16, 14), why: 'The customer expected a limit per API key; the answer says per workspace without saying so plainly.' },
  { id: 'w3', qid: 'q2', said: 'Can I get a refund on an annual plan after 30 days?', reports: 1, at: new Date(2026, 9, 14, 9), why: 'The answer gives the monthly refund rule. Annual plans are prorated differently.' },
];
const KIND = {
  never: { label: 'Never explained', c: 'amber', ic: IC.book, pill: 'Mentioned in documents, never explained' },
  un: { label: 'Unanswered', c: 'red', ic: IC.help, pill: 'People asked, nothing answers it' },
  wrong: { label: 'Marked wrong', c: 'blue', ic: IC.down, pill: 'Marked wrong in Ask lojo' },
};
let gFil = 'all', gSel = null;
const gOpen = new Set();
function gapItems() {
  const never = GAPS.map(g => ({ id: g.id, kind: 'never', title: g.term, n: g.where.length, unit: 'document', g, last: new Date(2026, 9, GAP_SEEN[g.id][0], GAP_SEEN[g.id][1]) }));
  const un = allQuestions().filter(q => !(q.docs || []).length && !isApproved(q) && !ST.merged[q.id]).map(q => { const list = inWin(asksFor(q.id), winFor('month'));
    return { id: q.id, kind: 'un', title: q.q, n: list.length, unit: 'ask', q, list, last: list.reduce((a, y) => y.at > a ? y.at : a, (list[0] || {}).at) }; }).filter(x => x.n);
  const wrong = WRONG.map(w => ({ ...w, kind: 'wrong', title: w.said, n: w.reports, unit: 'report', q: qById(w.qid), last: w.at }));
  const sort = (a, b) => b.n - a.n;
  return never.sort(sort).concat(un.sort(sort), wrong.sort(sort));
}
const gDone = (x) => !!(ST.gapDone[x.id] || (x.kind === 'never' && ST.gaps[x.id]));
const gState = (x) => gDone(x) ? 'done' : 'todo';
function renderG() {
  const all = gapItems(), items = all.filter(x => gFil === 'all' || x.kind === gFil), todo = items.filter(x => gState(x) === 'todo');
  if (!items.some(x => x.id === gSel)) gSel = (todo[0] || items[0] || {}).id || null;
  const cnt = (k) => all.filter(x => x.kind === k).length;
  const item = (x) => { const K = KIND[x.kind];
    const u = x.n === 1 ? x.unit : x.unit + 's';
    return '<button class="titem is-row' + (x.id === gSel ? ' is-sel' : '') + '" data-sel="' + x.id + '">' + rav(x.kind === 'never' ? 'gap' : x.kind === 'wrong' ? 'down' : 'q') + '<b>' + esc(x.title) + '</b>' +
      '<span class="tmeta"><span class="badge badge--gap">Gap</span><span class="badge badge--' + (K.c === 'amber' ? 'amber' : K.c === 'red' ? 'bad' : 'info') + '">' + K.label + '</span></span>' +
      '<span class="tside">' + cntPill(x.n, x.unit === 'document' ? 'doc' : 'ask', x.n + ' ' + u) + '</span></button>'; };
  $('gList').innerHTML = '<div class="th"><span>To handle</span><span>' + todo.length + '</span></div>' + (todo.length ? todo.map(item).join('') : '<div class="tnone">Nothing left to handle here.</div>') +
    listGroup('done', 'Handled', items.filter(x => gState(x) === 'done'), item, gOpen);
  renderGDetail(items.find(x => x.id === gSel));
}
function hl(text, term) {
  const t = term.replace(/^the /i, '').toLowerCase(), words = [t].concat(t.split(' ').filter(w => w.length > 4));
  for (const w of words) { const i = text.toLowerCase().indexOf(w); if (i >= 0) return esc(text.slice(0, i)) + '<mark>' + esc(text.slice(i, i + w.length)) + '</mark>' + esc(text.slice(i + w.length)); }
  return esc(text);
}
function renderGDetail(x) {
  if (!x) { $('gDetail').innerHTML = '<div class="dcard tempty"><b>Nothing here</b>Try another filter.</div>'; return; }
  const K = KIND[x.kind], done = gDone(x);
  let body = '', primary;
  if (x.kind === 'never') {
    body = '<div class="dsec"><h4>Where it’s mentioned</h4><p>' + esc(x.g.why) + '</p>' + x.g.where.map(([d, loc, t]) => '<div class="mention">' + I(IC.d) + '<div><small>' + esc(docById(d).name) + ' · ' + esc(loc) + '</small>' + hl(t, x.title) + '</div></div>').join('') + '</div>';
    primary = '<a class="btn--go btn--ink" href="build.html?gap=' + x.id + '">Explain it in Build ↗</a>';
  } else if (x.kind === 'un') {
    const gap = x.q.gap && GAPS.find(g => g.id === x.q.gap);
    body = dotsFor(x.list, 'month') + '<div class="dsplit"><div><h4>How people asked it</h4>' + askedList(x.q, x.list, true) + '</div><div class="sidebox"><h4>Nothing answers this yet</h4><p>' +
      (gap ? 'Your documents mention the ' + esc(gap.term.toLowerCase()) + ' but never give it. ' : 'No document covers it. ') + 'Write the answer once and lojo reuses it.</p></div></div>';
    primary = '<a class="btn--go btn--ink" href="' + buildHref(x.q) + '">Write an answer in Build ↗</a>';
  } else {
    const r = draftByQ(x.qid);
    body = '<div class="dsec"><h4>The answer they got</h4><p style="margin-bottom:10px">Approved answer to “' + esc(x.q.q) + '”</p><div class="quote md">' + md(answerOf(r)) + '</div></div>' +
      '<div class="dsec"><h4>Why it was flagged</h4><p>' + esc(x.why) + '</p></div>';
    primary = '<a class="btn--go btn--ink" href="build.html?sel=' + r.id + '">Fix the answer in Build ↗</a>';
  }
  const mark = '<button class="pillbtn' + (done ? ' on' : '') + '" data-done="' + x.id + '">' + I(IC.check) + (done ? 'Handled · undo' : 'Mark handled') + '</button>';
  $('gDetail').innerHTML = '<article class="dcard"><div class="dbody"><div class="dtop"><div><h2>' + esc(x.title) + '</h2>' +
    '<p class="dsub">' + (x.kind === 'wrong' ? 'Reported ' : 'Last seen ') + ago(x.last) + '</p><span class="pill ' + K.c + '">' + I(K.ic) + K.pill + '</span></div>' +
    '<div class="dnum"><b>' + x.n + '</b><span>' + ({ never: x.n === 1 ? 'document mentions it' : 'documents mention it', un: 'asks in the last 30 days', wrong: x.n === 1 ? 'report' : 'reports' })[x.kind] + '</span></div></div>' + body + '</div>' +
    footer(primary, mark) + '</article>';
}
$('gList').addEventListener('click', (e) => {
  const b = e.target.closest('[data-sel]'); if (b) { gSel = b.dataset.sel; renderG(); return; }
  const g = e.target.closest('summary'); if (g) { const k = g.parentElement.dataset.g; gOpen.has(k) ? gOpen.delete(k) : gOpen.add(k); }
});
$('gDetail').addEventListener('click', (e) => {
  const t = e.target.closest('button'); if (!t) return;
  if (t.dataset.done) {
    const id = t.dataset.done, x = gapItems().find(i => i.id === id);
    if (gDone(x)) { delete ST.gapDone[id]; if (x.kind === 'never') delete ST.gaps[id]; }
    else { ST.gapDone[id] = true; const ids = gapItems().filter(i => gState(i) === 'todo').map(i => i.id); gSel = ids[ids.indexOf(id) + 1] || ids[ids.indexOf(id) - 1] || id; toast('Marked handled'); }
    save(); renderG(); return;
  }
});
$('gFil').addEventListener('click', (e) => { const b = e.target.closest('[data-f]'); if (!b) return; gFil = b.dataset.f; document.querySelectorAll('#gFil button').forEach(x => x.setAttribute('aria-pressed', x === b)); gSel = null; renderG(); });

// ---------- Trends: 60 days of questions per channel; day 59 is 19 Oct
const SERIES = (() => {
  let seed = 11; const rnd = () => (seed = (seed * 16807) % 2147483647) / 2147483647;
  const mk = (a, b, amp, f) => Array.from({ length: 60 }, (_, i) => Math.max(0, Math.round(a + (b - a) * i / 59 + Math.sin(i / f) * amp + (rnd() - .5) * amp * 1.4)));
  return { c: mk(9, 18, 2.2, 2.1), e: mk(6, 6, 1.4, 1.7), k: mk(5, 2, 1, 1.4), d: mk(2.5, 9.5, 1.4, 2.6) };
})();
const RATE = { c: [74, 82], e: [63, 61], k: [38, 40], d: [55, 70] };
const RISING = { c: 'q9', e: 'q8', k: 'q22', d: 'q10' };
let tRange = 'month', tIdx = null;
const sum = (a) => a.reduce((x, y) => x + y, 0);
function smooth(pts) {
  let d = 'M' + pts[0][0] + ',' + pts[0][1];
  for (let i = 0; i < pts.length - 1; i++) {
    const p0 = pts[i - 1] || pts[i], p1 = pts[i], p2 = pts[i + 1], p3 = pts[i + 2] || p2;
    d += ' C' + (p1[0] + (p2[0] - p0[0]) / 6) + ',' + (p1[1] + (p2[1] - p0[1]) / 6) + ' ' + (p2[0] - (p3[0] - p1[0]) / 6) + ',' + (p2[1] - (p3[1] - p1[1]) / 6) + ' ' + p2[0] + ',' + p2[1];
  }
  return d;
}
function renderT() {
  const n = tRange === 'week' ? 7 : 30, cur = (k) => SERIES[k].slice(60 - n), prev = (k) => SERIES[k].slice(60 - 2 * n, 60 - n);
  const ch = Object.keys(CH).map(k => { const a = sum(cur(k)), b = sum(prev(k)); return { k, a, b, pct: Math.round((a - b) / Math.max(1, b) * 100) }; });
  const up = ch.slice().sort((x, y) => y.pct - x.pct)[0], down = ch.slice().sort((x, y) => x.pct - y.pct)[0];
  const sgn = (v) => (v > 0 ? '+' : '') + v;
  const pc = (c) => '<span style="color:' + CH_COLOR[c.k] + '">' + sgn(c.pct) + '%</span>';
  const all = sum(ch.map(c => c.a)), allPrev = sum(ch.map(c => c.b));
  $('tPrev').textContent = 'Previous ' + n + ' days';
  // one shared scale, so the four charts compare directly
  const max = Math.max(...Object.keys(CH).flatMap(k => cur(k).concat(prev(k)))) * 1.3;
  const X = (i) => i / (n - 1) * 1000, Y = (v) => 200 - v / max * 200, P = (i) => i / (n - 1) * 100;
  const date = (i) => dm(new Date(+new Date(2026, 9, 19) - (n - 1 - i) * DAY));
  $('tGrid').innerHTML = ch.slice().sort((x, y) => y.a - x.a).map(c => {
    const k = c.k, a = cur(k), line = smooth(a.map((v, i) => [X(i), Y(v)])), [r0, r1] = RATE[k], q = qById(RISING[k]);
    const arrow = c.pct > 3 ? '↗' : c.pct < -3 ? '↘' : '→';
    let hover = '';
    if (tIdx !== null && tIdx < n) {
      const l = P(tIdx);
      hover = '<span class="vl" style="left:' + l + '%"></span><span class="hd" style="left:' + l + '%;top:' + (Y(a[tIdx]) / 2) + '%;background:' + CH_COLOR[k] + '"></span>' +
        '<span class="ttip" style="' + (l > 60 ? 'right:' + (100 - l + 2) : 'left:' + (l + 2)) + '%">' + date(tIdx) + ' · <b>' + a[tIdx] + '</b> vs ' + prev(k)[tIdx] + '</span>';
    }
    return '<article class="tcard"><div class="tcard__head"><span class="chn"><span style="--c:' + CH_COLOR[k] + '">' + I(IC[k]) + '</span>' + CH[k] + '</span>' +
      '<div class="tcard__num"><b>' + c.a + '</b><small>' + arrow + ' <b>' + sgn(c.pct) + '%</b> vs previous ' + n + ' days</small></div></div>' +
      '<div class="tplot" data-k="' + k + '"><svg viewBox="0 0 1000 200" preserveAspectRatio="none" aria-hidden="true">' +
        '<path d="' + line + ' L1000,200 L0,200 Z" fill="' + CH_COLOR[k] + '" fill-opacity=".1"/>' +
        '<path d="' + smooth(prev(k).map((v, i) => [X(i), Y(v)])) + '" fill="none" stroke="var(--muted)" stroke-opacity=".7" stroke-width="1.5" stroke-dasharray="5 5" vector-effect="non-scaling-stroke"/>' +
        '<path d="' + line + '" fill="none" stroke="' + CH_COLOR[k] + '" stroke-width="2.5" stroke-linecap="round" vector-effect="non-scaling-stroke"/></svg>' +
        '<span class="xl" style="left:0">' + date(0) + '</span><span class="xl" style="right:0">' + date(n - 1) + '</span>' + hover + '</div>' +
      '<div class="tcard__foot"><div><small>Answered by Lojo</small><b>' + r1 + '%</b> <span class="' + (r1 >= r0 ? 'c-green' : 'c-red') + '">' + sgn(r1 - r0) + ' pts</span></div>' +
        '<div style="min-width:0"><small>Rising question</small><button class="rising" data-q="' + q.id + '" title="' + esc(q.q) + '">' + esc(q.q) + '</button></div></div></article>';
  }).join('');
}
$('tGrid').addEventListener('mousemove', (e) => { const pl = e.target.closest('.tplot'); if (!pl) return; const b = pl.getBoundingClientRect(), n = tRange === 'week' ? 7 : 30, i = Math.max(0, Math.min(n - 1, Math.round((e.clientX - b.left) / b.width * (n - 1)))); if (i !== tIdx) { tIdx = i; renderT(); } });
$('tGrid').addEventListener('mouseleave', () => { tIdx = null; renderT(); });
$('tGrid').addEventListener('click', (e) => { const b = e.target.closest('[data-q]'); if (b) goToQuestion(b.dataset.q); });
$('tRange').addEventListener('click', (e) => { const b = e.target.closest('[data-r]'); if (!b) return; tRange = b.dataset.r; tIdx = null; document.querySelectorAll('#tRange button').forEach(x => x.setAttribute('aria-pressed', x === b)); renderT(); });

// ---------- Opportunities: questions that point to something to build or sell
const THEMES = [
  { id: 't1', name: 'Payment methods', desc: 'Customers want to take payments Oslo doesn’t support yet.', items: [
    { id: 'o1', type: 'feature', title: 'Apple Pay in Germany', desc: 'Let merchants accept Apple Pay from shoppers in Germany at checkout, the way they already can in France and Spain.', asks: 3, quotes: [['e', 5, 'Do you support Apple Pay for customers in Germany? We could not find it in your docs.'], ['c', 15, 'Can customers in Berlin pay with Apple Pay?']] },
    { id: 'o2', type: 'feature', title: 'iDEAL for Dutch customers', desc: 'Add iDEAL as a payment method for shoppers in the Netherlands, where most online payments go through it.', asks: 2, quotes: [['c', 12, 'Can my customers in the Netherlands pay with iDEAL?']] },
    { id: 'o3', type: 'feature', title: 'Pay later with Klarna', desc: 'Offer buy-now-pay-later at checkout for larger baskets.', asks: 1, quotes: [['e', 9, 'Our average order is €400. Any plans for Klarna or another pay-later option?']] },
    { id: 'o4', type: 'expansion', title: 'Bank transfer on Starter', desc: 'Starter merchants whose finance team can only pay by transfer. Annual Growth already allows it, so this is an upgrade conversation.', asks: 1, quotes: [['e', 17, 'Our finance team can only pay by bank transfer. Is that possible on Starter?']] },
  ] },
  { id: 't2', name: 'Invoicing & finance', desc: 'Finance teams need invoices that fit how they already work.', items: [
    { id: 'o5', type: 'feature', title: 'PO numbers on invoices', desc: 'Let customers add their purchase-order number so invoices clear their approval process.', asks: 2, quotes: [['e', 6, 'Can we pay the annual Growth plan by invoice? Our finance team needs a PO number on it.']] },
    { id: 'o6', type: 'feature', title: 'Export invoices as CSV', desc: 'A CSV export of all invoices for the accounting system, instead of downloading PDFs one by one.', asks: 1, quotes: [['c', 14, 'Can I export invoices as a CSV?']] },
    { id: 'o7', type: 'expansion', title: 'Annual billing for growing teams', desc: 'Teams paying monthly on Growth asking about annual terms: a chance to lock in a year.', asks: 1, quotes: [['k', 9, 'If we commit for a year on Growth, is there a better price?']] },
  ] },
  { id: 't3', name: 'Seats & plans', desc: 'Teams outgrowing their plan before they need everything in the next one.', items: [
    { id: 'o8', type: 'expansion', title: 'More seats on Growth', desc: 'Teams hitting the 15-seat cap on Growth. Scale is the answer today; a seat add-on could keep them from churning.', asks: 2, quotes: [['k', 9, 'We have 18 people now. Do we really have to move to Scale for three more seats?']] },
    { id: 'o9', type: 'feature', title: 'Sandbox workspace', desc: 'A test workspace to try integrations without touching live payments.', asks: 1, quotes: [['c', 11, 'Is there a sandbox environment for testing?']] },
  ] },
  { id: 't4', name: 'Disputes', desc: 'Merchants with disputes want more control and clearer costs.', items: [
    { id: 'o10', type: 'feature', title: 'Automatic evidence upload', desc: 'Attach order records and delivery proof to a dispute automatically instead of uploading them by hand.', asks: 1, quotes: [['k', 3, 'We had two disputes this month. Can the order record be attached automatically?']] },
  ] },
];
let oFil = 'all', oTheme = 'all', oOpenId = null, oAt = new Date(2026, 9, 19, 15, 3), oBusy = false;
const oItems = (t) => t.items.filter(i => (oFil === 'all' || i.type === oFil) && !ST.oppOff[i.id]);
function renderO() {
  const themes = THEMES.map(t => ({ t, items: oItems(t) })).filter(x => x.items.length), all = themes.flatMap(x => x.items);
  const top = themes.slice().sort((a, b) => b.items.length - a.items.length)[0], asks = sum(all.map(i => i.asks));
  $('oFound').innerHTML = oBusy ? 'Looking for new requests…' : 'Updated ' + dm(oAt) + ', ' + oAt.toLocaleTimeString('en-GB', { hour: '2-digit', minute: '2-digit' });
  $('oRefresh').innerHTML = oBusy ? '<span class="spin"></span>Refreshing' : I(IC.refresh) + 'Refresh'; $('oRefresh').disabled = oBusy;
  if (oTheme !== 'all' && !themes.some(x => x.t.id === oTheme)) oTheme = 'all';
  const max = Math.max(1, ...themes.map(x => sum(x.items.map(i => i.asks))));
  $('oThemes').innerHTML = '<button class="theme' + (oTheme === 'all' ? ' is-sel' : '') + '" data-th="all"><b>All themes</b><span>' + asks + '</span></button>' + themes.map(({ t, items }) => { const a = sum(items.map(i => i.asks));
    return '<button class="theme' + (oTheme === t.id ? ' is-sel' : '') + '" data-th="' + t.id + '"><b>' + esc(t.name) + '</b><span>' + a + '</span><span class="tb"><span style="width:' + (a / max * 100) + '%"></span></span><small>' + plural(items.length, 'request') + '</small></button>'; }).join('');
  const cur = oTheme === 'all' ? null : themes.find(x => x.t.id === oTheme), list = (cur ? cur.items : all).slice().sort((a, b) => b.asks - a.asks);
  if (!list.some(i => i.id === oOpenId)) oOpenId = (list[0] || {}).id;
  const off = Object.keys(ST.oppOff).length;
  $('oDetail').innerHTML = (list.length ? '<div class="ohead"><div><h3>' + esc(cur ? cur.t.name : 'All themes') + '</h3><p>' + esc(cur ? cur.t.desc : 'Every request, most asked first.') + '</p></div><span>' + plural(sum(list.map(i => i.asks)), 'ask') + '</span></div>' +
    '<ul class="oacc">' + list.map(i => { const open = i.id === oOpenId;
      return '<li class="oitem' + (open ? ' is-open' : '') + '"><button class="ohd" data-oi="' + i.id + '" aria-expanded="' + open + '"><span><b>' + esc(i.title) + '</b><span class="tag ' + i.type + '">' + (i.type === 'feature' ? 'Feature request' : 'Expansion') + '</span></span>' +
        '<span class="on">' + i.asks + '<small>' + (i.asks === 1 ? 'ask' : 'asks') + '</small></span><span class="chev">' + I(IC.chev) + '</span><span class="ds">' + esc(i.desc) + '</span></button>' +
        (open ? '<div class="obody"><p>' + esc(i.desc) + '</p><h5>What customers asked</h5>' + i.quotes.map(([c, d, t]) => '<div class="quote oq">' + I(IC[c]) + '<span>“' + esc(t) + '”</span><time>' + d + ' Oct</time></div>').join('') +
          '<div class="oacts"><a class="btn--go btn--ink" href="build.html?opp=' + i.id + '&t=' + encodeURIComponent(i.title) + '">Take it to Build →</a><button class="ghost" data-off="' + i.id + '">Not now</button></div></div>' : '') + '</li>'; }).join('') + '</ul>'
    : '<div class="dcard tempty"><b>Nothing here</b>Try another filter.</div>') +
    (off ? '<p class="ooff">' + plural(off, 'request') + ' set aside · <button class="linkbtn" data-back="1">Bring back</button></p>' : '');
}
$('oThemes').addEventListener('click', (e) => { const b = e.target.closest('[data-th]'); if (!b) return; oTheme = b.dataset.th; oOpenId = null; renderO(); });
$('oDetail').addEventListener('click', (e) => {
  const h = e.target.closest('[data-oi]'); if (h) { oOpenId = oOpenId === h.dataset.oi ? '' : h.dataset.oi; renderO(); return; }
  const o = e.target.closest('[data-off]'); if (o) { ST.oppOff[o.dataset.off] = true; oOpenId = null; save(); renderO(); toast('Set aside'); return; }
  if (e.target.closest('[data-back]')) { ST.oppOff = {}; save(); renderO(); }
});
$('oFil').addEventListener('click', (e) => { const b = e.target.closest('[data-f]'); if (!b) return; oFil = b.dataset.f; oOpenId = null; document.querySelectorAll('#oFil button').forEach(x => x.setAttribute('aria-pressed', x === b)); renderO(); });
$('oRefresh').addEventListener('click', () => { oBusy = true; renderO(); setTimeout(() => { oBusy = false; oAt = new Date(2026, 9, 19, new Date().getHours(), new Date().getMinutes()); renderO(); toast('Up to date. No new requests.'); }, 1400); });

// ---------- tabs and keys
const TABS = { q: 'tabQ', g: 'tabG', t: 'tabT', o: 'tabO' }, HASH = { q: '#questions', g: '#gaps', t: '#trends', o: '#opportunities' };
let tab = 'q';
function show(t) {
  tab = t;
  document.querySelectorAll('.utab').forEach(x => x.setAttribute('aria-selected', x.dataset.tab === t));
  Object.entries(TABS).forEach(([k, id]) => { $(id).hidden = t !== k; });
}
document.querySelectorAll('.utab').forEach(x => x.addEventListener('click', () => { show(x.dataset.tab); history.replaceState(null, '', location.pathname + location.search + HASH[x.dataset.tab]); }));
function goToQuestion(id) {
  if (!inWin(asksFor(id), winFor(qRange)).length) { qRange = 'month'; document.querySelectorAll('#qRange button').forEach(x => x.setAttribute('aria-pressed', x.dataset.r === 'month')); }
  qSel = id; show('q'); history.replaceState(null, '', location.pathname + location.search + HASH.q); renderQ(); window.scrollTo({ top: 0, behavior: 'smooth' });
}
document.addEventListener('keydown', (e) => {
  if (e.metaKey || e.ctrlKey || e.altKey || /input|textarea|select/i.test(e.target.tagName) || e.target.isContentEditable) return;
  const k = e.key.toLowerCase(); if (!['j', 'k'].includes(k) || (tab !== 'q' && tab !== 'g')) return;
  if (tab === 'q') {
    const ids = qRows().filter(x => qState(x) === 'todo').map(x => x.q.id);
    if (ids.length) { qSel = moveSel(ids, qSel, k === 'j' ? 1 : -1); qMore = false; renderQ(); }
  } else {
    const ids = gapItems().filter(i => gState(i) === 'todo' && (gFil === 'all' || i.kind === gFil)).map(i => i.id);
    if (ids.length) { gSel = moveSel(ids, gSel, k === 'j' ? 1 : -1); renderG(); }
  }
  e.preventDefault();
});
if (new URLSearchParams(location.search).get('demo') === 'failed') qSel = 'q17';
renderQ(); renderG(); renderT(); renderO();
show(Object.keys(HASH).find(k => HASH[k] === location.hash) || 'q');
""")

# ============================================================ REVIEW
REVIEW = dict(
  active='review', title='Build',
  css=r"""
  .fromins{display:flex;align-items:flex-start;gap:14px;margin:0 0 18px;padding:16px 20px;border-radius:14px;border:1px solid rgba(232,93,117,.3);background:rgba(232,93,117,.05)}
  .fromins > div{flex:1;min-width:0}
  .fromins small{display:block;font-size:.7rem;font-weight:800;letter-spacing:.12em;text-transform:uppercase;color:#B73C54}
  .fromins b{display:block;margin:4px 0 2px;font-size:1rem}
  .fromins p{margin:0;color:var(--muted);font-size:.9rem}
  .fromins a{white-space:nowrap;font-size:.88rem}
  .fromins button{border:0;background:none;font-size:1.2rem;line-height:1;color:var(--muted);cursor:pointer;padding:0 2px}
  .meter{min-width:260px}
  .meter b{font-family:var(--display);font-size:1rem}
  .meter span{color:var(--muted);font-size:.8rem;margin-left:6px}
  .meter .bar{height:6px;border-radius:6px;background:var(--bg-soft);margin-top:8px;overflow:hidden}
  .meter .bar i{display:block;height:100%;background:var(--brand-gradient);transition:width .4s ease}
  .rv{display:grid;grid-template-columns:420px minmax(0,1fr);gap:20px;align-items:start}
  .fsbtn{gap:6px}
  .fsbtn svg{width:15px;height:15px;fill:none;stroke:currentColor;stroke-width:1.9;stroke-linecap:round;stroke-linejoin:round}
  /* full screen: no sidebar, full width, both columns use the whole height */
  body.is-fs .side,body.is-fs .mnav,body.is-fs .fab{display:none!important}
  body.is-fs .main{margin-left:0}
  body.is-fs .wrap{max-width:none;padding:16px 24px 24px}
  body.is-fs .head{margin:-16px -24px 16px;padding:12px 24px}
  body.is-fs .head > div:first-child > p:not(.label),body.is-fs .head .htip{display:none}
  body.is-fs .head h1{font-size:1.3rem;margin:2px 0 0}
  body.is-fs .rv{grid-template-columns:minmax(380px,32%) minmax(0,1fr)}
  body.is-fs .list{top:76px;max-height:calc(100vh - 96px)}
  body.is-fs .detail{min-height:calc(100vh - 96px)}
  body.is-fs .fsbtn{background:var(--ink);border-color:var(--ink);color:#fff}
  .list{position:sticky;top:84px;max-height:calc(100vh - 110px);display:flex;flex-direction:column;overflow:hidden}
  .list .tabs{padding:0 10px;margin:0}
  .list .tab{padding:12px 8px;font-size:.8rem;white-space:nowrap}
  .items{list-style:none;margin:0;padding:8px;overflow:auto;display:grid;gap:6px;align-content:start}
  .item{padding:14px 14px;border-radius:12px;cursor:pointer;display:grid;row-gap:8px;align-items:start;background:#F7F6F4}
  .item:hover{background:#F0EEEB}
  :root[data-theme="dark"] .item{background:rgba(255,255,255,.04)}
  :root[data-theme="dark"] .item:hover{background:rgba(255,255,255,.07)}
  .item.is-sel{background:var(--panel);box-shadow:inset 3px 0 0 var(--rose),0 0 0 1px var(--line-2),0 6px 16px -12px rgba(36,26,20,.4)}
  .item b{font-size:.84rem;font-weight:600;line-height:1.35}
  .item .meta{display:flex;gap:6px;flex-wrap:wrap}
  .detail{padding:24px 26px}
  .detail h2{font-family:var(--display);font-weight:700;font-size:1.3rem;letter-spacing:-.01em;margin:10px 0 16px;line-height:1.25}
  .seclbl{font-size:.68rem;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--muted);margin:0 0 8px}
  .answer{font-size:.98rem;line-height:1.6;margin:0 0 22px;padding:16px 18px;border-radius:12px;background:var(--bg-soft)}
  .quotes{display:grid;gap:10px;margin-bottom:22px}
  .quote{background:var(--panel);border:1px solid var(--line);border-radius:12px;padding:12px 14px}
  .quote.is-warn{border-color:rgba(217,154,43,.5);background:rgba(217,154,43,.05)}
  .quote.is-gap{border-color:rgba(47,116,232,.4);background:rgba(47,116,232,.04)}
  .quote mark.gapw{background:rgba(47,116,232,.16);color:inherit;padding:1px 2px;border-radius:3px}
  .badge--gap{background:rgba(47,116,232,.1);color:#2F74E8}
  .lfind{display:grid;gap:8px;padding:12px 14px;border-bottom:1px solid var(--line)}
  .lfind .text{height:36px}
  .lfrow{display:flex;gap:8px}
  .lfsearch{position:relative;flex:1;min-width:0;display:block}
  .lfsearch svg{position:absolute;left:11px;top:50%;width:16px;height:16px;transform:translateY(-50%);fill:none;stroke:var(--muted);stroke-width:2;stroke-linecap:round;pointer-events:none}
  .lfsearch .text{width:100%;padding-left:34px}
  .lfdrop{position:relative}
  .lfbtn{height:36px;padding:0 13px;font-size:.8rem;gap:6px}
  .lfbtn svg{width:15px;height:15px;fill:none;stroke:currentColor;stroke-width:1.8;stroke-linejoin:round}
  .lfbtn.is-on{border-color:var(--ink);background:var(--ink);color:#fff}
  .lfmenu{position:absolute;right:0;top:calc(100% + 6px);z-index:20;width:230px;padding:6px;border:1px solid var(--line);border-radius:12px;background:var(--panel);box-shadow:0 18px 40px -20px rgba(36,26,20,.45)}
  .lfitem{display:flex;align-items:center;gap:10px;width:100%;height:34px;padding:0 10px;border-radius:8px;font-size:.86rem;color:var(--ink);cursor:pointer}
  .lfitem:hover{background:var(--bg-soft)}
  .lfitem input{width:16px;height:16px;margin:0;accent-color:var(--ink);cursor:pointer}
  .lfitem span{flex:1}
  .lfitem em{font-style:normal;font-weight:700;font-size:.76rem;color:var(--muted)}
  .lfclear{display:block;width:100%;margin-top:4px;padding:8px 10px;border:0;border-top:1px solid var(--line);background:none;font:inherit;font-size:.8rem;font-weight:600;color:var(--muted);text-align:left;cursor:pointer}
  .lfclear:hover{color:var(--ink)}
  .lfactive{flex-wrap:wrap}
  .lfactive{display:flex;align-items:center;gap:8px}
  .lfchip{display:inline-flex;align-items:center;gap:6px;height:28px;padding:0 4px 0 11px;border-radius:999px;background:var(--ink);color:#fff;font-size:.78rem;font-weight:600}
  .lfchip button{width:22px;height:22px;border:0;border-radius:50%;background:rgba(255,255,255,.18);color:#fff;font-size:.9rem;line-height:1;cursor:pointer}
  .lfreset{border:0;background:none;font:inherit;font-size:.78rem;font-weight:600;color:var(--muted);cursor:pointer}
  .lfreset:hover{color:var(--ink)}
  .badge--q{background:rgba(36,26,20,.06);color:var(--ink)}
  .badge--fromgap{background:transparent;color:#2F74E8;box-shadow:inset 0 0 0 1px rgba(47,116,232,.35)}
  .item.is-failed{grid-template-columns:minmax(0,1fr) auto;column-gap:10px;background:rgba(198,69,69,.06)}
  .item.is-failed:hover{background:rgba(198,69,69,.1)}
  .item.is-failed.is-sel{background:rgba(198,69,69,.12);box-shadow:inset 3px 0 0 var(--error)}
  .item.is-failed > b,.item.is-failed > .meta{grid-column:1}
  .fstate{grid-column:2;grid-row:1/span 2;align-self:center;font-size:.76rem;font-weight:600;color:var(--error);white-space:nowrap;text-align:right}
  .fstate small{display:block;font-size:.74rem;font-weight:500;color:var(--muted)}
  .item.has-side{grid-template-columns:minmax(0,1fr) auto;column-gap:16px}
  .item.has-side > b,.item.has-side > .meta{grid-column:1}
  .srcb{display:inline-flex;align-items:center;gap:4px;height:22px;padding:0 8px;border-radius:999px;background:#FFF0E8;border:1px solid rgba(232,93,117,.22);color:#B73C54;font-size:.72rem;font-weight:700;cursor:default}
  :root[data-theme="dark"] .srcb{background:rgba(232,93,117,.14);border-color:rgba(232,93,117,.3);color:#FFB199}
  .srcb svg{width:12px;height:12px;fill:none;stroke:currentColor;stroke-width:2;stroke-linejoin:round}
  .fstate small{margin-top:4px}
  .item.has-av{grid-template-columns:32px minmax(0,1fr);column-gap:12px}
  .item.has-av.has-side,.item.has-av.is-failed{grid-template-columns:32px minmax(0,1fr) auto}
  .item.has-av > b,.item.has-av > .meta{grid-column:2}
  .item.has-av > .rside,.item.has-av > .fstate{grid-column:3}
  .rav{grid-column:1;grid-row:1/span 2;align-self:center;width:32px;height:32px;border-radius:50%;display:grid;place-items:center;font-size:.95rem;line-height:1}
  .rav--question{background:#FFF0E8}
  .rav--gap{background:rgba(47,116,232,.12)}
  .rav--failed{background:rgba(198,69,69,.14)}
  :root[data-theme="dark"] .rav--question{background:rgba(255,177,153,.14)}
  .rside{grid-column:2;grid-row:1/span 2;align-self:center;font-size:.74rem;color:var(--muted);white-space:nowrap;text-align:right}
  .item.is-redo{background:rgba(63,143,95,.07)}
  .item.is-redo:hover{background:rgba(63,143,95,.11)}
  .item.is-redo.is-sel{background:rgba(63,143,95,.13);box-shadow:inset 3px 0 0 var(--success)}
  .rstate{display:block;margin-bottom:4px;font-size:.76rem;font-weight:600;color:var(--success)}
  .item.is-other{background:rgba(123,92,240,.07)}
  .item.is-other:hover{background:rgba(123,92,240,.11)}
  .item.is-other.is-sel{background:rgba(123,92,240,.13);box-shadow:inset 3px 0 0 #7B5CF0}
  .item.is-other .rstate{color:#6A48D7}
  .badge--bad{background:rgba(198,69,69,.1);color:var(--error)}
  .fnote2{display:grid;gap:4px;margin:0 0 22px;padding:12px 14px;border-radius:12px;background:rgba(198,69,69,.06);border:1px solid rgba(198,69,69,.2);font-size:.88rem}
  .fnote2 b{color:var(--error)}
  .fnote2 span{color:var(--muted)}
  .item.is-hl{background:rgba(47,116,232,.07);box-shadow:inset 3px 0 0 #2F74E8}
  .item.is-hl.is-sel{background:rgba(47,116,232,.12)}
  .gapnote .g.is-hl{margin:-6px -8px;padding:8px;border-radius:10px;background:rgba(47,116,232,.1);box-shadow:0 0 0 2px #2F74E8;animation:hlPulse 1.6s ease-out 2}
  .quote.is-hl{border-color:#2F74E8;box-shadow:0 0 0 2px rgba(47,116,232,.25)}
  @keyframes hlPulse{0%{box-shadow:0 0 0 2px #2F74E8,0 0 0 0 rgba(47,116,232,.45)}100%{box-shadow:0 0 0 2px #2F74E8,0 0 0 12px rgba(47,116,232,0)}}
  @media (prefers-reduced-motion:reduce){.gapnote .g.is-hl{animation:none}}
  .gapnote{display:grid;gap:10px;margin:0 0 18px;padding:12px 14px;border-radius:12px;border:1px solid rgba(47,116,232,.3);background:rgba(47,116,232,.05)}
  .gapnote .g{display:flex;gap:10px;align-items:flex-start}
  .gapnote .g > div{flex:1;min-width:0;font-size:.84rem;color:var(--muted)}
  .gapnote .g b{display:block;color:var(--ink);font-size:.88rem}
  .gapnote .g .btn{height:30px;padding:0 12px;font-size:.76rem}
  .gacts{display:flex;gap:8px;flex-wrap:wrap;margin-top:10px}
  .gwhy{margin:-6px 0 20px;color:var(--muted);font-size:.95rem;line-height:1.6}
  .gsent{display:flex;align-items:center;gap:10px;margin:-8px 0 20px;padding:10px 12px;border-radius:10px;background:rgba(63,143,95,.08);font-size:.86rem;color:var(--muted)}
  .gsent b{color:var(--ink)}
  .gdrafts{display:grid;gap:8px;margin-bottom:22px}
  .gdraft{display:flex;justify-content:space-between;gap:12px;padding:10px 14px;border-radius:10px;border:1px solid var(--line);background:var(--panel);font:inherit;font-size:.88rem;font-weight:600;text-align:left;cursor:pointer}
  .gdraft:hover{border-color:rgba(36,26,20,.24)}
  .gdraft span{color:#B73C54;font-size:.8rem;white-space:nowrap}
  .quote .qtop{display:flex;gap:8px;align-items:center;margin-bottom:4px}
  .quote .qtop b{font-size:.8rem}
  .quote .qtop em{font-style:normal;color:var(--muted);font-size:.74rem}
  .quote p{margin:0;font-size:.86rem}
  .quote .more{border:0;background:none;padding:0;margin-top:8px;font-size:.76rem;font-weight:700;color:#B73C54;cursor:pointer}
  .quote .full{margin-top:10px;padding:12px 14px;border-radius:10px;background:var(--bg-soft);font-size:.84rem;line-height:1.65;color:var(--muted)}
  .callq .qtop{gap:8px}
  .cl-dir{width:28px;height:28px;border-radius:50%;flex:none;display:grid;place-items:center}
  .cl-dir svg{width:15px;height:15px;fill:none;stroke:currentColor;stroke-width:1.9;stroke-linecap:round;stroke-linejoin:round}
  .cl-dir--in{background:rgba(62,111,166,.12);color:var(--info)}
  .cl-dir--out{background:rgba(63,143,95,.13);color:var(--success)}
  .badge--in{background:rgba(62,111,166,.1);color:var(--info)}
  .badge--out{background:rgba(63,143,95,.12);color:var(--success)}
  .cl-used{margin-left:auto;font-size:.74rem;font-weight:600;color:#8A6212}
  .cl-meta{margin:2px 0 10px!important;font-size:.78rem!important;color:var(--muted)}
  .cl-log{display:grid;gap:2px;border-left:2px solid var(--line);padding-left:10px}
  .cl-log.is-open{max-height:320px;overflow:auto}
  .cl-row{display:grid;grid-template-columns:44px 104px minmax(0,1fr);gap:8px;align-items:baseline;padding:5px 8px;border-radius:8px;font-size:.85rem;line-height:1.5}
  .cl-row.is-used{background:#FFF4D6;box-shadow:inset 2px 0 0 #E0B04A}
  .cl-t{font-family:ui-monospace,Menlo,monospace;font-size:.72rem;color:var(--muted)}
  .cl-who{font-size:.74rem;font-weight:700;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
  .cl-who--a{color:#B73C54}
  .cl-who--c{color:var(--info)}
  .cl-gap{padding:2px 8px 2px 60px;color:var(--muted);font-size:.8rem;letter-spacing:.2em}
  :root[data-theme="dark"] .cl-row.is-used{background:rgba(224,176,74,.16)}
  @media (max-width:700px){ .cl-row{grid-template-columns:1fr} }
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
  /* Link to SOP: map this answer to a step, or build a new SOP around it */
  .badge--sop{background:rgba(62,111,166,.1);color:var(--info)}
  .soplink{display:flex;align-items:center;gap:10px;flex-wrap:wrap;margin:-8px 0 22px;padding:10px 12px;border-radius:10px;background:rgba(62,111,166,.07);font-size:.84rem}
  .soplink svg,.sopp svg{width:16px;height:16px;flex:none;fill:none;stroke:var(--info);stroke-width:1.9;stroke-linecap:round;stroke-linejoin:round}
  .soplink .spacer{flex:1}
  .sid{font:600 .72rem/1 ui-monospace,Menlo,monospace;color:var(--muted);background:var(--bg-soft);border-radius:6px;padding:4px 6px;white-space:nowrap}
  .sopp{margin-top:16px;border:1.5px solid rgba(62,111,166,.35);border-radius:14px;background:var(--panel);box-shadow:0 18px 40px -30px rgba(36,26,20,.5);animation:askIn .18s ease}
  .sopp__h{display:flex;align-items:flex-start;gap:10px;padding:14px 16px 10px}
  .sopp__h > div{flex:1}
  .sopp__h b{display:block;font-size:.95rem}
  .sopp__h .sub{font-size:.8rem}
  .sopp__tabs{display:grid;grid-template-columns:1fr 1fr;gap:6px;padding:0 16px}
  .sopp__tabs button{display:flex;align-items:center;gap:8px;padding:10px 12px;border-radius:10px;border:1px solid var(--line-2);background:var(--panel);font:inherit;font-size:.84rem;font-weight:600;color:var(--muted);cursor:pointer;text-align:left}
  .sopp__tabs button b{width:22px;height:22px;border-radius:7px;display:grid;place-items:center;flex:none;background:var(--bg-soft);font-size:.72rem;color:var(--muted)}
  .sopp__tabs button em{margin-left:auto;font-style:normal;font-size:.72rem;color:var(--muted)}
  .sopp__tabs button[aria-selected="true"]{border-color:var(--info);color:var(--ink);background:rgba(62,111,166,.05)}
  .sopp__tabs button[aria-selected="true"] b{background:var(--info);color:#fff}
  .sopp__b{padding:14px 16px 16px}
  .sopm{list-style:none;margin:0;padding:0;display:grid;gap:8px}
  .sopm li{display:grid;grid-template-columns:minmax(0,1fr) 90px auto;gap:12px;align-items:center;padding:10px 12px;border:1px solid var(--line);border-radius:12px}
  .sopm li.is-top{border-color:rgba(62,111,166,.4);background:rgba(62,111,166,.04)}
  .sopm .t{display:block;font-size:.88rem;font-weight:600}
  .sopm .t .sid{margin-right:6px}
  .sopm small{display:block;color:var(--muted);font-size:.78rem;margin-top:4px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
  .pct{display:grid;gap:4px;font-size:.74rem;font-weight:700;color:var(--info);text-align:right}
  .pct i{display:block;height:4px;border-radius:4px;background:var(--bg-soft);overflow:hidden}
  .pct i::before{content:"";display:block;height:100%;width:var(--w);background:var(--info);border-radius:4px}
  .sopnew{display:grid;gap:14px}
  .sopfmt{display:flex;gap:6px;flex-wrap:wrap}
  .sopfmt .chip{display:inline-flex;align-items:center;gap:6px}
  .sopfmt .chip small{font-size:.66rem;font-weight:800;letter-spacing:.06em;text-transform:uppercase;color:var(--success)}
  .sopfmt .chip[aria-pressed="true"] small{color:#9ED8B0}
  .sopwhy{font-size:.8rem;color:var(--muted);margin:6px 0 0}
  .soprel{list-style:none;margin:0;padding:0;display:grid;gap:6px}
  .soprel label{display:flex;align-items:center;gap:10px;padding:8px 10px;border-radius:10px;background:var(--bg-soft);font-size:.84rem;font-weight:500}
  .soprel input{width:16px;height:16px;accent-color:var(--rose);flex:none}
  .soprel span:not(.badge){flex:1}
  .sopp .dx{width:30px;height:30px;border-radius:50%;border:0;background:var(--bg-soft);color:var(--muted);font-size:1.05rem;cursor:pointer;flex:none}
  .sopp .dx:hover{color:var(--ink)}
  .sopgo{display:flex;align-items:center;gap:12px;flex-wrap:wrap}
  .sopgo .sub{flex:1;min-width:200px;font-size:.8rem}
  .vs{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-bottom:14px}
  .vs .quote{display:flex;flex-direction:column;gap:10px}
  .vs .quote p{flex:1}
  .vs .quote .btn{align-self:flex-start}
  .picked{display:flex;align-items:center;gap:10px;margin:-8px 0 22px;padding:10px 12px;border-radius:10px;background:rgba(63,143,95,.08);font-size:.86rem;color:var(--muted)}
  .picked b{color:var(--ink)}
  .picked .spacer{flex:1}
  @media (max-width:700px){.vs{grid-template-columns:1fr}}
  /* calmer list: rows on lines, not cards; one accent for the selected row */
  .items{padding:0;gap:0}
  .item,.item.is-failed,.item.is-redo,.item.is-other,:root[data-theme="dark"] .item{border-radius:0;background:none;padding:13px 18px;row-gap:5px;border-bottom:1px solid var(--line)}
  .item:hover,.item.is-failed:hover,.item.is-redo:hover,.item.is-other:hover,:root[data-theme="dark"] .item:hover{background:var(--bg-soft)}
  .item.is-sel,.item.is-failed.is-sel,.item.is-redo.is-sel,.item.is-other.is-sel,.item.is-hl.is-sel{background:rgba(232,93,117,.05);box-shadow:inset 3px 0 0 var(--rose)}
  .item.is-hl{background:rgba(47,116,232,.04);box-shadow:inset 3px 0 0 rgba(47,116,232,.5)}
  .item b{font-weight:600;display:-webkit-box;-webkit-box-orient:vertical;-webkit-line-clamp:2;line-clamp:2;overflow:hidden;overflow-wrap:anywhere}
  .item .meta:empty{display:none}
  .item .meta .badge{height:19px;padding:0 7px;font-size:.6rem}
  .item.has-av{grid-template-columns:24px minmax(0,1fr)}
  .item.has-av.has-side,.item.has-av.is-failed{grid-template-columns:24px minmax(0,1fr) auto}
  .rav{width:24px;height:24px;font-size:.78rem;align-self:start;margin-top:1px}
  .srcb,:root[data-theme="dark"] .srcb{background:none;border:0;padding:0;height:auto;color:var(--muted);font-weight:600}
  .fstate{font-size:.74rem}
  .list .tabs{border-bottom:1px solid var(--line)}
  .lfind{padding:10px 14px}
  /* detail: fewer boxes, more air between sections */
  .detail h2{margin:8px 0 18px}
  .gapnote{gap:12px;padding:10px 14px;border:0;border-left:3px solid #2F74E8;border-radius:0 10px 10px 0;background:rgba(47,116,232,.05)}
  .gapnote .g > div{font-size:.84rem}
  .gapnote .g b{display:inline;margin-right:4px}
  .gacts{margin-top:8px;gap:4px}
  .gacts .btn{height:28px;padding:0 10px;font-size:.76rem}
  .acts{gap:8px}
  .item.is-drafting{cursor:default;opacity:.8}
  .gflow{margin:0 0 4px;font-size:.84rem;color:var(--muted)}
  /* the review panel stays put beside the list and scrolls on its own */
  .detail{position:sticky;top:84px;height:calc(100vh - 140px);max-height:none;overflow:auto;overscroll-behavior:contain;display:flex;flex-direction:column}
  .detail > *{flex-shrink:0}
  /* the decision bar always sits on the bottom edge, however short the item */
  .detail.card > .acts{margin-top:auto}
  @media (max-width:1240px){.detail.card > .acts{margin-top:22px}}
  .detail > .empty{margin:auto 0}
  .list{height:calc(100vh - 140px);max-height:none}
  @media (min-width:1001px){.wrap{padding-bottom:0}}
  @media (max-width:1000px){.detail,.list{height:auto}.detail{display:block}}
  body.is-fs .detail{top:76px;min-height:0;height:calc(100vh - 96px);max-height:none}
  @media (max-width:1000px){.detail{position:static;max-height:none;overflow:visible}}
  /* the decision bar stays in reach at the bottom while you read the sources */
  .detail .acts{position:sticky;bottom:-24px;z-index:5;flex-wrap:nowrap;gap:6px;margin:22px -26px -24px;padding:12px 96px 12px 26px;border-top:1px solid var(--line);background:var(--panel);border-radius:0 0 16px 16px;box-shadow:0 -14px 24px -18px rgba(36,26,20,.35)}
  .detail .acts .btn{height:36px;padding:0 12px;font-size:.8rem;white-space:nowrap;flex:none;gap:6px}
  .detail .acts .btn--ghost{padding:0 8px}
  .detail .acts .sub{white-space:nowrap;overflow:hidden;text-overflow:ellipsis;min-width:0}
  /* the right end stays clear for the Ask lojo button */
  /* not enough room for one row: drop the J/K hint, then let the bar scroll with the page */
  @media (max-width:1600px){.detail .acts .spacer + .sub:has(kbd),.detail .acts .btn kbd{display:none}}
  @media (max-width:1240px){.detail .acts{position:static;flex-wrap:wrap;margin:22px 0 0;padding:18px 0 0;box-shadow:none;border-radius:0}}
  body.is-fs .detail .acts .spacer + .sub:has(kbd){display:inline}
  .lgrp{list-style:none;padding:14px 18px 6px;font-size:.66rem;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--muted);border-bottom:1px solid var(--line)}
  .lgrp em{font-style:normal;margin-left:4px}
  @media (max-width:700px){.sopp__tabs{grid-template-columns:1fr}.sopm li{grid-template-columns:1fr auto}.pct{display:none}}
""",
  body=r"""
    <div class="head">
      <div>
        <p class="label">02 Build · Review</p>
        <h1>Build</h1>
        <p>Approve, edit, or reject with a reason. A rejected draft is written again with your reason, or sent to a person to answer.</p>
      </div>
      <span class="spacer"></span>
      <div class="meter"><b id="mCount">0 of 0</b><span>reviewed</span><div class="bar"><i id="mBar"></i></div></div>
      <button class="btn btn--secondary btn--sm fsbtn" id="fsBtn" type="button" aria-pressed="false" title="Full screen (F)"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M15 3h6v6M9 21H3v-6M21 3l-7 7M3 21l7-7"/></svg><span>Full screen</span></button>
    </div>
    <div class="fromins" id="fromIns" hidden></div>
    <div class="rv">
      <section class="card list" aria-label="Drafts">
        <div class="tabs" role="tablist" id="rtabs">
          <button class="tab" data-f="pending" aria-selected="true" title="Drafts to review">Drafts <span class="n" id="nP">0</span></button>
          <button class="tab" data-f="needs" aria-selected="false" title="Questions, gaps and failed drafts that need a decision">Needs you <span class="n" id="nN">0</span></button>
          <button class="tab" data-f="final" aria-selected="false" title="Answers only a person can write">Human <span class="n" id="nF">0</span></button>
          <button class="tab" data-f="approved" aria-selected="false">Approved <span class="n" id="nA">0</span></button>
        </div>
        <div class="lfind">
          <div class="lfrow">
            <label class="lfsearch"><svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></svg><input class="text" id="lq" type="search" placeholder="Search drafts" aria-label="Search drafts" autocomplete="off"></label>
            <div class="lfdrop">
              <button class="btn btn--secondary lfbtn" id="lfBtn" type="button" aria-haspopup="true" aria-expanded="false"><svg viewBox="0 0 24 24"><path d="M4 5h16l-6 8v5l-4 2v-7z"/></svg><span>Filter</span></button>
              <div class="lfmenu" id="ltags" role="menu" hidden></div>
            </div>
          </div>
          <div class="lfactive" id="lfActive" hidden></div>
        </div>
        <ul class="items" id="items"></ul>
      </section>
      <section class="card detail" id="detail" aria-live="polite"></section>
    </div>
""",
  js=r"""
let tab = 'pending', sel = null, mode = 'view', linking = false, refs = [];
let sopOpen = false, sopTab = 'map', sopFmt = null, sopTitle = null, sopRel = null;
const AIC = {
  doc: '<svg viewBox="0 0 24 24"><path d="m21 12-8.6 8.6a6 6 0 0 1-8.5-8.5l8.6-8.6a4 4 0 0 1 5.7 5.7l-8.6 8.6a2 2 0 0 1-2.8-2.8l7.9-7.9"/></svg>',
  link: '<svg viewBox="0 0 24 24"><path d="M10 13a5 5 0 0 0 7.5.5l3-3a5 5 0 0 0-7-7l-1.7 1.7"/><path d="M14 11a5 5 0 0 0-7.5-.5l-3 3a5 5 0 0 0 7 7l1.7-1.7"/></svg>',
  ai: '<svg viewBox="0 0 24 24"><path d="M12 3l1.8 4.7L18.5 9.5l-4.7 1.8L12 16l-1.8-4.7L5.5 9.5l4.7-1.8z"/><path d="M19 15l.8 2.2L22 18l-2.2.8L19 21l-.8-2.2L16 18l2.2-.8z"/></svg>',
};
const REASONS = ['Wrong answer', 'Outdated source', 'Missing detail', 'Not a question we answer'];
const openFull = new Set();
const CONTEXT = {
  'd1|p. 4': ['Plans and features. Every plan includes the help centre, the chat and email support. ', ' Starter workspaces sign in with email or with Google. An Admin turns single sign-on on under Settings → Security.'],
  'd5|Brightline call, 12 Aug': ['Brightline asked about access for their 40-person support team. ', ' They want to roll it out before their October audit. Follow-up: send the SSO setup guide.'],
  'd2|Security & login · 9 months old': ['Security & login. Every account is protected by two-step verification. ', ' Contact sales to enable it. Last updated 14 January.'],
  'd4|§2': ['§2 Cancelling a subscription. A workspace Admin can cancel at any time from Billing. ', ' Refunds go back to the original payment method within 10 working days.'],
  'd1|p. 2': ['Starter is for small teams getting started. ', ' Teams that need more move to Growth, which includes 15 seats and 25,000 transactions a month.'],
  'd3|pp. 2–4': ['Before you start, make sure you are a workspace Admin and are on Growth or Scale. ', ' Test the connection by signing in from a private window before you turn it on for everyone.'],
  'd1|p. 6': ['Changing plans. You can change plan at any time from Billing. ', ' Your invoice shows the change on its own line.'],
  'd6|p. 1': ['Welcome to Oslo. Here is what happens in your first month. ', ' Growth customers get a 30-minute kickoff and our onboarding guides.'],
  'd9|§1': ['§1 Paying for Oslo. ', ' Prices are shown in euros and charged in your local currency.'],
  'd9|§4': ['§4 Invoices. ', ' Invoices are sent on the first working day of the month and are due within 30 days.'],
  'd1|p. 5': ['Billing. ', ' Card payments are taken on the same day each month.'],
  'd8|Rate limits': ['Rate limits keep the API fast for everyone. ', ' Limits apply per workspace, not per API key.'],
  'd8|429 responses': ['When you go over the limit. ', ' Retry after the number of seconds given, and back off further if it happens again.'],
  'd10|§2': ['§2 Responding to a dispute. ', ' Late evidence can’t be added once the card network has started its review.'],
  'd10|§4': ['§4 After you respond. ', ' We email the outcome to the workspace Admin as soon as we hear back.'],
  'd7|p. 3': ['Encryption. Data in transit is encrypted with TLS 1.2 or higher. ', ' Encryption keys are rotated every 90 days.'],
  'd7|p. 2': ['Where your data lives. ', ' Backups stay in the same region and are kept for 35 days.'],
  'd7|p. 8': ['Your data, your choice. ', ' Exports include documents, questions and approved answers.'],
  'd2|Exporting your data': ['Exporting your data. Only Admins can export. ', ' Large exports are emailed to you as a download link.'],
  'd4|§3': ['§3 Annual plans. ', ' Monthly plans are not refunded after the first 30 days.'],
  'd9|§2': ['§2 Renewals. ', ' We email a reminder 30 days before each renewal.'],
};
const Q = (r) => allQuestions().find(q => q.id === r.qid).q;
// gaps a draft leans on: a source quote mentions something no document explains
const GAP_WORDS = { g1: /enterprise/i, g2: /chargeback fee/i, g3: /retention/i, g4: /onboarding manager/i, g5: /over the limit|requests per second|burst/i };
const gapsOf = (r) => GAPS.filter(g => !ST.gaps[g.id] && r.src.some(s => GAP_WORDS[g.id].test(s[2])));
const gapIn = (text, gs) => gs.find(g => GAP_WORDS[g.id].test(text));
// arriving from an Insights gap: highlight every draft that leans on it
const HL_GAP = new URLSearchParams(location.search).get('gap');
const hasHl = (r) => !!HL_GAP && gapsOf(r).some(g => g.id === HL_GAP);
const inTab = (r) => { const s = decision(r).status; return tab === 'pending' ? (s === 'pending' || s === 'redrafting') : s === tab; };
// every draft answers a question; some also lean on a gap
const isGap = (r) => gapsOf(r).length > 0;
// questions someone added from a gap (Add as a question)
const fromGap = (qid) => { const q = allQuestions().find(x => x.id === qid); return !!(q && q.gap); };
let lq = '', gsel = null, fsel = null, fwrite = false;
// Needs you: one list of triage, gaps and failed drafts; nsel is "kind:id"
let nsel = null, tsel = null, asking = null;
// Human: questions no source answers, written by a person
let osel = null, owrite = false;
const JK = '<span class="spacer"></span><span class="sub"><kbd>J</kbd> <kbd>K</kbd> to move</span>';
const needsPick = (r) => !!r.conflict && decision(r).status === 'pending' && !decision(r).pick;
// filters: several can be on; a row shows if it matches any of them
const ltags = new Set();
const onlyGaps = () => false;
// questions lojo couldn't draft: no answer with sources that check out
const failedQs = () => tab !== 'needs' ? [] : allQuestions().filter(q => (ST.draftFailed || {})[q.id] && (!lq || q.q.toLowerCase().includes(lq)));
// open gaps: things the documents mention but never explain
const openGaps = () => GAPS.filter(g => !ST.gaps[g.id] && (!lq || (g.term + ' ' + g.why).toLowerCase().includes(lq)));
const gapDrafts = (g) => DRAFTS.filter(r => decision(r).status !== 'approved' && gapsOf(r).some(x => x.id === g.id));
const TAGS_DRAFTS = [['all', 'All', () => true], ['question', 'Questions', (r) => !isGap(r)], ['gap', 'Relies on a gap', isGap], ['conflict', 'Sources disagree', (r) => !!r.conflict]];
const TAGS_NEEDS = [['all', 'All', () => true], ['triage', 'Triage', () => false], ['gap', 'Gaps', () => false], ['failed', 'Draft failed', () => false]];
let TAGS = TAGS_DRAFTS;
const tagOk = (r) => !ltags.size || [...ltags].some(k => TAGS.find(t => t[0] === k)[2](r));
const showFailed = () => !ltags.size || ltags.has('failed');
const triageQs = () => tasks().triage.filter(q => !lq || q.q.toLowerCase().includes(lq));
function needItems() {
  const on = (k) => !ltags.size || ltags.has(k), out = [];
  if (on('triage')) triageQs().forEach(q => out.push(['triage', q.id]));
  if (on('gap')) openGaps().forEach(g => out.push(['gap', g.id]));
  if (on('failed')) failedQs().forEach(q => out.push(['failed', q.id]));
  return out;
}
const ownQs = () => tasks().noSource.filter(q => !lq || q.q.toLowerCase().includes(lq));
function renderTags() {
  TAGS = tab === 'needs' ? TAGS_NEEDS : TAGS_DRAFTS;
  const base = DRAFTS.filter(inTab), nf = failedQs().length;
  const count = (k, f) => tab === 'needs' ? (k === 'triage' ? triageQs().length : k === 'gap' ? openGaps().length : nf) : base.filter(f).length;
  $('ltags').innerHTML = TAGS.filter(t => t[0] !== 'all').map(([k, l, f]) => { const n = count(k, f), on = ltags.has(k); return (n || on) ? '<label class="lfitem"><input type="checkbox" data-tag="' + k + '"' + (on ? ' checked' : '') + '><span>' + l + '</span><em>' + n + '</em></label>' : ''; }).join('') +
    (ltags.size ? '<button type="button" class="lfclear" data-reset>Clear all</button>' : '');
  $('lfActive').hidden = !ltags.size;
  $('lfActive').innerHTML = [...ltags].map(k => '<span class="lfchip">' + TAGS.find(t => t[0] === k)[1] + '<button type="button" data-untag="' + k + '" aria-label="Remove ' + TAGS.find(t => t[0] === k)[1] + '">×</button></span>').join('') + (ltags.size ? '<button type="button" class="lfreset" data-reset>Reset</button>' : '');
  $('lfBtn').classList.toggle('is-on', ltags.size > 0);
  $('lfBtn').lastChild.textContent = ltags.size ? 'Filter · ' + ltags.size : 'Filter';
}
const nsrc = (n) => n === 1 ? '1 source' : n + ' sources';
// a small avatar at the start of each row says what it is
const ROW_ICON = { question: ['❓', 'Question'], gap: ['🧩', 'Gap'], failed: ['⚠️', 'Draft failed'] };
const rowAv = (k) => '<span class="rav rav--' + k + '" title="' + ROW_ICON[k][1] + '" aria-hidden="true">' + ROW_ICON[k][0] + '</span>';
// compact source count for list rows; hover says "3 sources"
const srcBadge = (n) => '<span class="srcb" title="' + nsrc(n) + '" aria-label="' + nsrc(n) + '"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8z"/><path d="M14 3v5h5"/></svg>' + n + '</span>';
function badges(r, inList) {
  const d = decision(r); let b = '';
  if (r.conflict) b += '<span class="badge badge--amber">Sources disagree</span>';
  const gs = gapsOf(r); if (gs.length) b = '<span class="badge badge--gap" title="' + esc(gs.map(g => g.term).join(', ')) + '">Gap</span>' + b;
  if (fromGap(r.qid)) b += '<span class="badge badge--fromgap" title="Added as a question from a gap">From gap</span>';
  if (d.by) b += '<span class="badge badge--muted">By ' + esc(d.by.split(' ')[0]) + '</span>';
  if (d.edited) b += '<span class="badge badge--muted">Edited</span>';
  if (ST.sopLinks[r.id]) b += '<span class="badge badge--sop" title="Linked to ' + ST.sopLinks[r.id].sop + '">SOP</span>';
  return b;
}
function renderList() {
  const c = counts(), T = tasks();
  $('nP').textContent = c.pending; $('nN').textContent = T.needs; $('nA').textContent = c.approved; $('nF').textContent = T.human;
  const done = c.approved + c.final;
  $('mCount').textContent = done + ' of ' + c.drafts; $('mBar').style.width = (done / c.drafts * 100) + '%';
  renderTags();
  if (tab === 'needs') {
    const its = needItems(), key = (i) => i[0] + ':' + i[1];
    if (!its.some(i => key(i) === nsel)) nsel = its.length ? key(its[0]) : null;
    const [nk, nid] = nsel ? nsel.split(':') : [null, null];
    tsel = nk === 'triage' ? nid : null; gsel = nk === 'gap' ? nid : null; fsel = nk === 'failed' ? nid : null;
    const sl = (k, id) => (k + ':' + id === nsel ? ' is-sel' : '');
    // one heading per kind instead of a tag on every row
    const GRP = { triage: 'Say whether it matters', gap: 'Gaps that need a source', failed: 'Drafts that failed' };
    const head = (k, i) => i === 0 || its[i - 1][0] !== k ? '<li class="lgrp" aria-hidden="true">' + GRP[k] + '<em>' + its.filter(x => x[0] === k).length + '</em></li>' : '';
    $('items').innerHTML = its.length ? its.map(([k, id], i) => head(k, i) + (() => {
      if (k === 'triage') { const q = allQuestions().find(x => x.id === id);
        return '<li class="item has-av has-side' + sl(k, id) + '" data-nk="' + k + ':' + id + '">' + rowAv('question') + '<b>' + esc(q.q) + '</b><span class="meta"></span><span class="rside">Matters?</span></li>'; }
      if (k === 'gap') { const g = GAPS.find(x => x.id === id);
        return '<li class="item has-av' + sl(k, id) + (id === HL_GAP ? ' is-hl' : '') + '" data-nk="' + k + ':' + id + '">' + rowAv('gap') + '<b>' + esc(g.term) + '</b><span class="meta">' + ((ST.gapDocs || {})[id] ? '<span class="badge badge--ok">Document sent</span>' : (ST.gapAsked || {})[id] ? '<span class="badge badge--info">Asked ' + esc(ST.gapAsked[id].split(' ')[0]) + '</span>' : '') + '</span></li>'; }
      const q = allQuestions().find(x => x.id === id), n = (q.docs || []).length;
      return '<li class="item has-av is-failed' + sl(k, id) + '" data-nk="' + k + ':' + id + '">' + rowAv('failed') + '<b>' + esc(q.q) + '</b><span class="meta">' + (q.gap ? '<span class="badge badge--fromgap">From gap</span>' : '') +
        '</span><span class="fstate">' + ((ST.draftFailed || {})[q.id] === 'retrying' ? 'Drafting again…' : 'Draft failed') + '<small>' + srcBadge(n) + '</small></span></li>';
    })()).join('') : '<li class="empty"><b>' + (lq || ltags.size ? 'Nothing matches.' : 'Nothing needs you.') + '</b>' + (lq || ltags.size ? 'Try other words or another tag.' : 'Every question, gap and failed draft is handled.') + '</li>';
    return;
  }
  if (onlyGaps()) {
    const gl = openGaps();
    if (!gl.some(g => g.id === gsel)) gsel = gl.length ? gl[0].id : null;
    $('items').innerHTML = gl.length ? gl.map(g => {
      return '<li class="item has-av' + (g.id === gsel ? ' is-sel' : '') + (g.id === HL_GAP ? ' is-hl' : '') + '" data-gapid="' + g.id + '">' + rowAv('gap') + '<b>' + esc(g.term) + '</b><span class="meta"><span class="badge badge--gap">Gap</span>' + ((ST.gapDocs || {})[g.id] ? '<span class="badge badge--ok">Document sent</span>' : '') + '</span></li>'; }).join('')
      : '<li class="empty"><b>' + (lq ? 'Nothing matches.' : 'No open gaps.') + '</b>' + (lq ? 'Try other words.' : 'Every gap is explained or set aside.') + '</li>';
    return;
  }
  const fl = showFailed() ? failedQs() : [];
  const drafting = tab === 'pending' ? ST.extra.filter(q => q.drafting) : [];
  const list = (ltags.size === 1 && ltags.has('failed')) ? [] : DRAFTS.filter(inTab).filter(r => tagOk(r) && (!lq || (Q(r) + ' ' + answerOf(r)).toLowerCase().includes(lq)));
  if (fsel && !fl.some(q => q.id === fsel)) fsel = null;
  if (!list.length && !fsel && fl.length) fsel = fl[0].id;
  const fhtml = fl.map(q => { const n = (q.docs || []).length;
    return '<li class="item has-av is-failed' + (q.id === fsel ? ' is-sel' : '') + '" data-fq="' + q.id + '">' + rowAv('failed') + '<b>' + esc(q.q) + '</b><span class="meta"><span class="badge badge--q">Question</span>' + (q.gap ? '<span class="badge badge--fromgap">From gap</span>' : '') +
      '</span><span class="fstate">' + ((ST.draftFailed || {})[q.id] === 'retrying' ? 'Drafting again…' : 'Draft failed') + '<small>' + srcBadge(n) + '</small></span></li>'; }).join('');
  if (!list.some(r => r.id === sel)) { sel = list.length ? list[0].id : null; mode = 'view'; }
  const oq = tab === 'final' ? ownQs() : [];
  if (osel && !oq.some(q => q.id === osel)) { osel = null; owrite = false; }
  if (tab === 'final' && !list.length && !osel && oq.length) osel = oq[0].id;
  const rows = list.map(r => '<li class="item has-av has-side' + '' + (r.id === sel && !fsel && !osel ? ' is-sel' : '') + (hasHl(r) ? ' is-hl' : '') + '" data-id="' + r.id + '">' + rowAv(isGap(r) ? 'gap' : 'question') + '' +
    '<b>' + esc(Q(r)) + '</b><span class="meta">' + badges(r, true) + '</span><span class="rside">' + '' + srcBadge(r.src.length) + '</span></li>');
  rows.splice(Math.min(3, rows.length), 0, fhtml);
  drafting.slice().reverse().forEach(q => rows.unshift('<li class="item has-av has-side is-drafting" aria-busy="true">' + rowAv('question') + '<b>' + esc(q.q) + '</b><span class="meta"><span class="badge badge--fromgap">From gap</span></span><span class="rside"><span class="spin" style="width:10px;height:10px"></span> Drafting…</span></li>'));
  // questions no source answers: only a person can write these
  oq.forEach(q => { const n = (ST.asks || {})[q.id];
    rows.push('<li class="item has-av has-side' + (q.id === osel ? ' is-sel' : '') + '" data-oq="' + q.id + '">' + rowAv('question') + '<b>' + esc(q.q) + '</b><span class="meta"><span class="badge badge--muted">No source</span>' + (q.gap ? '<span class="badge badge--fromgap">From gap</span>' : '') + '</span><span class="rside">' + (n ? 'Asked ' + n + '×' : '') + '</span></li>'); });
  $('items').innerHTML = (list.length || fl.length || oq.length || drafting.length) ? rows.join('')
    : (lq || ltags.size) ? '<li class="empty"><b>Nothing matches.</b>Try other words or another tag.</li>'
    : '<li class="empty"><b>' + (tab === 'pending' ? 'Nothing to review.' : 'Nothing here yet.') + '</b>' + (tab === 'pending' ? 'The first batch is done.' : '') + '</li>';
}
function renderGap() {
  const g = GAPS.find(x => x.id === gsel);
  if (!g) { $('detail').innerHTML = '<div class="empty"><b>No open gaps.</b>Everything your documents mention is explained, or set aside.</div>'; return; }
  const ds = gapDrafts(g);
  $('detail').innerHTML = '<div class="meta" style="display:flex;gap:6px"><span class="badge badge--gap">' + (g.id === HL_GAP ? 'From Insights' : 'Gap') + '</span></div><h2>' + esc(g.term) + '</h2>' +
    '<p class="gwhy">' + esc(g.why) + '</p>' +
    ((ST.gapDocs || {})[g.id] ? '<div class="gsent"><span class="spin"></span><span><b>' + esc(ST.gapDocs[g.id]) + '</b> is being read. The gap closes once it’s explained.</span></div>' : '') +
    '<p class="seclbl">Where it’s mentioned</p><div class="quotes">' + g.where.map(([doc, loc, text]) => '<div class="quote is-gap"><div class="qtop"><b>' + esc(docShort(doc)) + '</b><em>' + esc(loc) + '</em></div><p>“' + esc(text) + '”</p></div>').join('') + '</div>' +
    (ds.length ? '<p class="seclbl">Drafts that rely on it</p><div class="gdrafts">' + ds.map(r => '<button type="button" class="gdraft" data-open="' + r.id + '">' + esc(Q(r)) + ' <span>Open →</span></button>').join('') + '</div>' : '') +
    ((ST.gapAsked || {})[g.id] && asking !== g.id ? '<div class="gsent"><span>✓</span><span><b>Asked ' + esc(ST.gapAsked[g.id]) + '.</b> Their answer comes back here.</span></div>' : '') +
    (asking === g.id ? '<div class="reject"><label class="seclbl" for="ownerSel" style="margin:0">Who knows the answer?</label><select class="text" id="ownerSel">' + ST.people.filter(p => p.status === 'member').map(p => '<option>' + esc(p.name) + '</option>').join('') + '</select>' +
      '<textarea class="text" id="ownerNote" placeholder="Add a note (optional)" style="min-height:70px"></textarea><p class="sub">They get an email with the passages above. Their answer comes back to this gap.</p></div>' +
      '<div class="acts"><button class="btn btn--primary" type="button" data-askgo="' + g.id + '">Send</button><button class="btn btn--ghost" type="button" data-askx>Cancel</button></div>'
    : '<p class="gflow">Add as a question: lojo drafts it first. It goes to a person only if lojo can’t find an answer.</p><div class="acts"><button class="btn btn--primary" type="button" data-senddoc="' + g.id + '">Upload a document</button><button class="btn btn--secondary" type="button" data-ask="' + g.id + '">Ask an owner</button><button class="btn btn--secondary" type="button" data-gapq="' + g.id + '">Add as a question</button><button class="btn btn--ghost" type="button" data-gap="' + g.id + '">Dismiss</button>' + JK + '</div>');
  if (asking === g.id) $('ownerSel').focus();
}
function renderFailed() {
  const q = allQuestions().find(x => x.id === fsel), why = (ST.draftFailed || {})[q.id], again = why === 'retrying';
  $('detail').innerHTML = '<div class="meta" style="display:flex;gap:6px"><span class="badge badge--bad">Draft failed</span></div><h2>' + esc(q.q) + '</h2>' +
    (again ? '<div class="answer" style="display:flex;gap:10px;align-items:center;color:var(--muted)"><span class="spin"></span>lojo is drafting it again from its sources.</div>'
      : '<div class="fnote2"><b>No draft with sources that check out could be written.</b>' + (why && why !== true ? '<span>' + esc(why) + '</span>' : '') + '</div>') +
    ((q.docs || []).length ? '<p class="seclbl">Sources it tried</p><div class="quotes" style="display:flex;flex-wrap:wrap;gap:6px">' + q.docs.map(d => srcChip(d, '')).join('') + '</div>' : '') +
    (fwrite ? '<p class="seclbl">Your answer</p><textarea class="text" id="fBox" style="min-height:130px;padding:12px 13px" placeholder="Write the answer as you would give it."></textarea>' : '') +
    (again ? '' : '<div class="acts">' + (fwrite ? '<button class="btn btn--primary" data-fa="save">Save &amp; approve</button><button class="btn btn--ghost" data-fa="cancel">Cancel</button>'
      : '<button class="btn btn--primary" data-fa="retry">Try again</button><button class="btn btn--secondary" data-fa="write">Write my own answer</button><button class="btn btn--ghost" data-fa="leave">Dismiss</button>' + JK) + '</div>');
  if (fwrite) $('fBox').focus();
}
function renderTriage() {
  const q = allQuestions().find(x => x.id === tsel);
  $('detail').innerHTML = '<div class="meta" style="display:flex;gap:6px"><span class="badge badge--amber">Triage</span></div><h2>' + esc(q.q) + '</h2>' +
    '<p class="gwhy">lojo found this question in your sources. Say whether it matters. Only questions that matter get drafted.</p>' +
    ((q.docs || []).length ? '<p class="seclbl">Found in</p><div class="quotes" style="display:flex;flex-wrap:wrap;gap:6px">' + q.docs.map(d => srcChip(d, '')).join('') + '</div>' : '') +
    '<div class="acts"><button class="btn btn--primary" type="button" data-ta="yes">It matters</button><button class="btn btn--ghost" type="button" data-ta="no">Doesn’t matter</button>' + JK + '</div>';
}
function renderOwn() {
  const q = allQuestions().find(x => x.id === osel), g = q.gap && GAPS.find(x => x.id === q.gap), n = (ST.asks || {})[q.id];
  $('detail').innerHTML = '<div class="meta" style="display:flex;gap:6px;flex-wrap:wrap"><span class="badge badge--muted">No source</span>' + (q.gap ? '<span class="badge badge--fromgap">From gap</span>' : '') + '</div><h2>' + esc(q.q) + '</h2>' +
    '<div class="done-note no">' + (q.why ? esc(q.why) + ' Write the answer yourself, or upload a document that does.' : 'No source answers this yet. Write the answer yourself, or upload a document that does.') + '</div>' +
    (n ? '<p class="gwhy">Asked ' + n + ' times in Ask lojo and email.</p>' : '') + (g ? '<p class="gwhy">' + esc(g.why) + '</p>' : '') +
    (owrite ? '<p class="seclbl">Your answer</p><textarea class="text" id="oBox" style="min-height:130px;padding:12px 13px" placeholder="Write the answer as you would give it."></textarea><div style="height:22px"></div>' : '') +
    '<div class="acts">' + (owrite ? '<button class="btn btn--primary" type="button" data-oa="save">Save &amp; approve</button><button class="btn btn--ghost" type="button" data-oa="cancel">Cancel</button>'
      : '<button class="btn btn--primary" type="button" data-oa="write">Write my own answer</button><button class="btn btn--secondary" type="button" data-oa="upload">Upload a document</button><button class="btn btn--ghost" type="button" data-oa="leave">Leave out</button>' + JK) + '</div>';
  if (owrite) $('oBox').focus();
}
// a call as one readable log: who, when, how long; only the turns lojo used, with a little context
const CALLS = {
  'd5|ZIWO call, 25 Sep': { dir: 'in', title: 'ZIWO call', meta: 'Oslo · Emmanuel · 25 Sep 2026, 04:59 · 7 min', who: { a: 'Emmanuel (Oslo)', c: 'Caller' }, lines: [
    ['00:02', 'c', 'I mean, I have no idea what everything is, so…'],
    ['00:09', 'a', 'So that means, yeah, the first claim they will remove only $500 and not $1,000. So you are saving $500.'],
    ['00:21', 'a', 'And that’s annually, so every time I renew it, it resets.'],
    ['00:34', 'a', 'But you can choose, and you can change everything at the renewal time. Upgrade, downgrade, change your co-payment, change the deductible.'],
    ['00:52', 'c', 'And also, is it covered in Abu Dhabi as well?'],
    ['00:57', 'a', 'You can go to any vet clinic in the UAE.', 1],
    ['01:01', 'a', 'You can go to Al Ain, Abu Dhabi, Dubai, wherever you want.', 1],
    ['01:06', 'c', 'Okay, perfect. And when I, say, for example, make a report, I just have to get the vet to fill in a form or a letter?'],
    ['01:18', 'a', 'No, no. It’s much easier than that.'],
    ['01:22', 'a', 'You go to any vet in the UAE, you pay the bill, and after that you will have access to your Oslo paid cloud in the login.', 1],
    ['01:31', 'a', 'So you will enter your paid cloud, you upload the bill, and this is exactly what you have to do, nothing else.', 1],
    ['01:40', 'a', 'You don’t have to fill in any paper or put any licence or medical report.', 1],
    ['01:46', 'a', 'We do everything for you. You just have to upload the bill.', 1],
    ['01:51', 'c', 'Okay. Because every time I ask, obviously, Abu Dhabi, I’m not in Dubai, they ask, do they accept pet insurance?'],
    ['02:03', 'a', 'Everyone says no, because we don’t have an agreement with them. We do only reimbursement.'],
    ['02:12', 'a', 'But the bill that you have paid, so it can be any bill in the UAE.'],
  ] },
  'd5|ZIWO call, 19 Aug': { dir: 'in', title: 'ZIWO call', meta: 'Oslo · Emmanuel · 19 Aug 2026, 13:27 · 13 min', who: { a: 'Emmanuel (Oslo)', c: 'Caller' }, lines: [
    ['00:03', 'c', 'And I want to know, like, me, please.'],
    ['04:10', 'a', 'There’s a payment link, so you pay with your debit card, credit card, on the website.'],
    ['04:22', 'c', 'And what do I have to put about that? Do I have…'],
    ['09:41', 'c', 'All clinics, all clinics on your way?'],
    ['09:45', 'a', 'You can go to Sharjah, you can go to Abu Dhabi, you can go to Al Ain, you can go to Dubai. You can go everywhere.', 1],
    ['09:53', 'c', 'Yes, but is it written on the website or no?'],
    ['09:58', 'a', 'It’s in the policy summary and the policy wording, under coverage.'],
    ['12:40', 'c', 'Okay, thank you. Have a great evening.'],
  ] },
  'd5|Brightline call, 12 Aug': { dir: 'out', title: 'Brightline call', meta: 'Maria Eide with Brightline · 12 Aug, 14:05 · 7 min', who: { a: 'Maria (Oslo)', c: 'Brightline' }, lines: [
    ['00:04', 'c', 'Hi, thanks for taking the call. We’re looking at rolling lojo out to our support team.'],
    ['00:11', 'a', 'Great. How many people would use it?'],
    ['00:15', 'c', 'About forty, all in support. We have an audit in October, so we’d like it live before then.'],
    ['00:24', 'a', 'That works. Which plan are you on today?'],
    ['00:28', 'c', 'Growth, the annual one.'],
    ['00:31', 'c', 'One thing we need is single sign-on. Our security team won’t approve it without SSO.'],
    ['00:38', 'a', 'Your Growth plan covers SSO, yes. You can turn it on in Settings, Security.', 1],
    ['00:45', 'c', 'Oh good, I thought it was Enterprise only.'],
    ['00:49', 'a', 'Not any more. SAML single sign-on is on Growth and Scale since the 2026 pricing.', 1],
    ['00:57', 'c', 'Perfect. Can you send us the setup guide?'],
    ['01:02', 'a', 'I’ll send the Okta guide after this call.'],
    ['01:06', 'c', 'And refunds, if it doesn’t work out?'],
    ['01:10', 'a', 'Thirty days for a full refund. After that it’s prorated.'],
    ['01:16', 'c', 'Okay. That covers it, thanks.'],
  ] },
};
function callLog(k) {
  const c = CALLS[k], open = openFull.has(k), L = c.lines;
  // marked lines plus one line either side; gaps between excerpts show as a divider
  const keep = new Set(); L.forEach((l, i) => { if (l[3]) [i - 1, i, i + 1].forEach(j => { if (j >= 0 && j < L.length) keep.add(j); }); });
  const row = (l) => '<div class="cl-row' + (l[3] ? ' is-used' : '') + '"><span class="cl-t">' + l[0] + '</span><span class="cl-who cl-who--' + l[1] + '">' + esc(c.who[l[1]]) + '</span><span class="cl-x">' + esc(l[2]) + '</span></div>';
  let body = '', last = -1;
  if (open) body = L.map(row).join('');
  else [...keep].sort((a, b) => a - b).forEach(i => { if (last >= 0 && i > last + 1) body += '<div class="cl-gap">· · ·</div>'; body += row(L[i]); last = i; });
  const used = L.filter(l => l[3]).length;
  const out = c.dir === 'out';
  const ic = '<span class="cl-dir cl-dir--' + (out ? 'out' : 'in') + '" title="' + (out ? 'Outbound call' : 'Inbound call') + '"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 4h3l2 5-2.5 1.5a11 11 0 0 0 6 6L15 14l5 2v3a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2"/>' +
    (out ? '<path d="M15 3h6v6M21 3l-7 7"/>' : '<path d="M21 3l-7 7M14 4v6h6"/>') + '</svg></span>';
  return '<div class="quote callq"><div class="qtop">' + ic + '<b>' + esc(c.title) + '</b><span class="badge ' + (out ? 'badge--out' : 'badge--in') + '">' + (out ? 'Outbound' : 'Inbound') + '</span><span class="cl-used">' + used + ' line' + (used === 1 ? '' : 's') + ' used</span></div>' +
    '<p class="cl-meta">' + esc(c.meta) + '</p><div class="cl-log' + (open ? ' is-open' : '') + '">' + body + '</div>' +
    '<button class="more" type="button" data-full="' + esc(k) + '" aria-expanded="' + open + '">' + (open ? 'Show only what was used' : 'Show full call (' + L.length + ' turns)') + '</button></div>';
}
function renderDetail() {
  if (tab === 'needs') {
    if (tsel) return renderTriage(); if (gsel) return renderGap(); if (fsel) return renderFailed();
    $('detail').innerHTML = '<div class="empty"><b>Nothing needs you.</b>Every question, gap and failed draft is handled.</div>'; return;
  }
  if (tab === 'final' && osel) return renderOwn();
  const r = DRAFTS.find(x => x.id === sel);
  if (!r) { $('detail').innerHTML = '<div class="empty"><b>Nothing to review. The loop is running.</b>Approved answers are in the store; try them in Ask lojot.</div>'; return; }
  const d = decision(r), ans = answerOf(r);
  let h = '<div class="meta" style="display:flex;gap:6px;flex-wrap:wrap">' + badges(r) + '</div><h2>' + esc(Q(r)) + '</h2>';
  const other = ST.others && ST.others[r.id], gs = gapsOf(r);
  // the answer relies on something the documents never explain: check it before approving
  if (gs.length && d.status !== 'approved') h += '<div class="gapnote">' + gs.map(g => '<div class="g' + (g.id === HL_GAP ? ' is-hl' : '') + '"><div><b>' + (g.id === HL_GAP ? 'From Insights · ' : 'Relies on a gap · ') + esc(g.term) + '.</b>' + esc(g.why) + ' Check this answer doesn’t rely on it.' +
    '<div class="gacts"><button class="btn btn--ghost" type="button" data-senddoc="' + g.id + '">Upload a document</button><button class="btn btn--ghost" type="button" data-gapq="' + g.id + '">Add as a question</button><button class="btn btn--ghost" type="button" data-gap="' + g.id + '">Dismiss</button></div></div></div>').join('') + '</div>';
  // G10: someone else decided this draft while it was open here
  if (other && d.status === 'pending') h += '<div class="other"><span class="av av--p ' + tone(other.by) + '">' + esc(other.by.split(' ').map(x => x[0]).join('')) + '</span><div><b>' + esc(other.by) + ' ' + esc(other.action) + ' this ' + esc(other.when) + '.</b>' +
    'Your screen was out of date, so nothing you do here will change it. Their decision stands.<div class="btns"><button class="btn btn--primary btn--sm" data-a="ackOther">Got it, next draft</button><button class="btn btn--ghost btn--sm" data-a="seeOther">See their version</button></div></div></div>';
  if (d.status === 'approved') h += '<div class="done-note ok">✓ Approved' + (d.by ? ' by ' + esc(d.by) : '') + (d.at ? ' · ' + esc(d.at) : '') + '. It’s in the store and Ask lojo can use it.</div>';
  if (d.status === 'final') h += '<div class="done-note no">' + (d.own ? 'You’re writing this one yourself. Save to approve it, or leave it out.' : 'Sent to a person (' + esc(d.reason) + '). Write the answer yourself, or leave it out.') + '</div>';
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
    h += '<p class="seclbl">' + (d.redrafted ? 'Rewritten draft' : 'Draft answer') + '</p><div class="answer">' + md(ans) + '</div>';
    const ln = ST.sopLinks[r.id], ls = ln && sopById(ln.sop);
    if (ls) h += '<div class="soplink">' + SOPIC + '<span>Step ' + (ln.step + 1) + ' of <a href="sops.html?id=' + ls.id + '&amp;step=' + ln.step + '">' + esc(ls.title) + '</a></span><span class="sid">' + ls.id + '</span></div>';
  }
  // G14: a draft rewritten more than once keeps its history
  if (d.history && d.history.length) h += '<details class="hist"><summary>Earlier drafts (' + d.history.length + ')</summary><ol>' + d.history.map(x => '<li>' + esc(x.text) + '<span>Rejected · ' + esc(x.reason) + '</span></li>').join('') + '</ol></details>';
  else if (d.redrafted && d.prev) h += '<p class="prev"><b>First draft, rejected</b> (' + esc(d.reason) + '): ' + esc(d.prev) + '</p>';
  if (d.refs && d.refs.length && mode !== 'edit') h += '<p class="seclbl">Sources you added</p><div class="arefs" style="margin-bottom:22px">' + d.refs.map(x => '<span class="aref">' + (x.kind === 'link' ? AIC.link : AIC.doc) + esc(x.name) + '</span>').join('') + '</div>';
  // several quotes from the same call show as one log
  const calls = {}; r.src.forEach(([doc, loc]) => { const k = doc + '|' + loc; if (CALLS[k]) calls[k] = 1; });
  h += '<p class="seclbl">Where it came from</p><div class="quotes">' + Object.keys(calls).map(k => callLog(k)).join('') + r.src.filter(([doc, loc]) => !CALLS[doc + '|' + loc]).map(([doc, loc, text]) => {
    const warn = r.conflict === doc, gw = !warn && gapIn(text, gs), hl = gw && gw.id === HL_GAP;
    const key = doc + '|' + loc, ctx = CONTEXT[key] || ['', ''], openQ = openFull.has(key);
    // G9: the whole passage, with the quoted words highlighted
    const said = gw ? esc(text).replace(new RegExp(GAP_WORDS[gw.id].source, 'i'), m => '<mark class="gapw">' + m + '</mark>') : esc(text);
    return '<div class="quote' + (warn ? ' is-warn' : gw ? ' is-gap' : '') + (hl ? ' is-hl' : '') + '"><div class="qtop"><b>' + esc(docShort(doc)) + '</b><em>' + esc(loc) + '</em>' + (warn ? '<span class="badge badge--amber">Conflicts</span>' : gw ? '<span class="badge badge--gap">Gap</span>' : '') + '</div><p>“' + said + '”</p>' +
      (openQ ? '<div class="full">' + esc(ctx[0]) + '<mark>' + esc(text) + '</mark>' + esc(ctx[1]) + '</div>' : '') +
      '<button class="more" type="button" data-full="' + esc(key) + '" aria-expanded="' + openQ + '">' + (openQ ? 'Hide full passage' : 'Show full passage') + '</button></div>';
  }).join('') + '</div>';
  if (mode === 'reject') {
    h += '<div class="reject"><label class="seclbl" for="why" style="margin:0">Reason</label><select class="text" id="why">' + REASONS.map(x => '<option>' + x + '</option>').join('') + '</select>' +
      '<textarea class="text" id="note" placeholder="What should change? (optional)" style="min-height:70px"></textarea>' +
      '<p class="sub">Rewrite: lojo writes it again using your reason. Send to Human: it waits in Human for a person to answer.</p></div>';
  }
  let acts = '';
  if (d.status === 'redrafting') acts = '';
  else if (mode === 'edit' && d.status === 'final') acts = '<button class="btn btn--primary" data-a="save">Save &amp; approve</button><button class="btn btn--ghost" data-a="leave">Leave out</button><span class="spacer"></span><span class="sub">Your answer is approved as soon as you save it.</span>';
  else if (mode === 'edit') acts = '<button class="btn btn--primary" data-a="save">' + (d.status === 'approved' ? 'Save changes' : 'Save &amp; approve') + '</button><button class="btn btn--ghost" data-a="cancel">Cancel</button>';
  else if (mode === 'reject') acts = '<button class="btn btn--danger" data-a="confirm">Reject &amp; rewrite</button><button class="btn btn--secondary" data-a="tohuman">Send to Human</button><button class="btn btn--ghost" data-a="cancel">Cancel</button>';
  else if (d.status === 'pending' && ST.others && ST.others[r.id]) acts = '';
  else if (needsPick(r)) {
    const old = r.src.find(x => x[0] === r.conflict), nw = r.src.find(x => x[0] !== r.conflict);
    h += '<p class="seclbl">Sources disagree. Which one is right?</p><div class="vs">' + [nw, old].map(x => '<div class="quote' + (x === old ? ' is-warn' : '') + '"><div class="qtop"><b>' + esc(docShort(x[0])) + '</b><em>' + esc(x[1]) + '</em>' + (x === old ? '<span class="badge badge--amber">Older</span>' : '<span class="badge badge--ok">Newer</span>') + '</div><p>“' + esc(x[2]) + '”</p>' +
      '<button class="btn btn--secondary btn--sm" type="button" data-use="' + x[0] + '">Use this source</button></div>').join('') + '</div>';
    acts = '<button class="btn btn--danger" type="button" data-a="retireold">Retire the old one</button><span class="sub">' + esc(docShort(old[0])) + ' stops being used for drafts and Ask lojo.</span>' + JK;
  }
  else if (d.status === 'pending') acts = '<button class="btn btn--primary" data-a="approve" title="Approve (A)">Approve <kbd>A</kbd></button><button class="btn btn--secondary" data-a="edit" title="Edit &amp; approve (E)">Edit &amp; approve <kbd>E</kbd></button><button class="btn btn--danger" data-a="reject" title="Reject (R)">Reject <kbd>R</kbd></button><button class="btn btn--secondary" data-a="sop" aria-expanded="' + sopOpen + '" title="Link to SOP (L)">Link to SOP <kbd>L</kbd></button><button class="btn btn--ghost" data-a="own">Write my own answer</button><span class="spacer"></span><span class="sub"><kbd>J</kbd> <kbd>K</kbd> to move</span>';
  else if (d.status === 'final') acts = '<button class="btn btn--primary" data-a="edit">Write the answer</button><button class="btn btn--ghost" data-a="undo">Back to review</button>';
  else acts = '<button class="btn btn--primary" data-a="edit">Edit answer</button><button class="btn btn--secondary" data-a="sop" aria-expanded="' + sopOpen + '">Link to SOP <kbd>L</kbd></button><button class="btn btn--ghost" data-a="undo">Undo approval</button><span class="spacer"></span><span class="sub">Edits go live in Ask lojo as soon as you save.</span>';
  if (r.conflict && d.pick && d.status === 'pending' && mode === 'view') h += '<div class="picked"><span>✓</span><span>Using <b>' + esc(docShort(d.pick)) + '</b>. The draft follows it.</span><span class="spacer"></span><button class="btn btn--ghost btn--sm" type="button" data-a="repick">Change</button></div>';
  if (acts) h += '<div class="acts">' + acts + '</div>';
  if (sopOpen && mode === 'view' && (d.status === 'pending' || d.status === 'approved')) h += sopPanel(r);
  $('detail').innerHTML = h;
  if (sopOpen && sopFocus) { sopFocus = false; const p = $('sopp'); if (p) { p.scrollIntoView({ block: 'nearest', behavior: 'smooth' }); const f = p.querySelector('[data-sopl], #sopT'); if (f) f.focus({ preventScroll: true }); } }
  if (mode === 'edit') { const t = $('editBox'); if (typed !== null) { t.value = typed; typed = null; } t.focus(); t.setSelectionRange(t.value.length, t.value.length); }
}
// titles stop at two lines; the full text shows on hover, only where it was cut
function clampTitles() { document.querySelectorAll('#items .item > b').forEach(b => { if (b.scrollHeight > b.clientHeight + 1) b.title = b.textContent; else b.removeAttribute('title'); }); }
let shownKey = null;
function render() {
  renderList(); renderDetail(); clampTitles();
  // a new item opens at its top
  const k = [tab, sel, nsel, osel].join('|'); if (k !== shownKey) { shownKey = k; $('detail').scrollTop = 0; }
}
const SOPIC = '<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="5" y="4" width="14" height="17" rx="2"/><path d="M9 4V3h6v1M9 10l1.5 1.5L13 9M9 16l1.5 1.5L13 15"/></svg>';
let sopFocus = false;
// ranked by meaning: the step this answer fits best in each SOP
function sopMatches(r) {
  const text = Q(r) + ' ' + answerOf(r);
  return ST.sops.filter(s => s.from !== 'external' && s.status !== 'retired').map(s => {
    let step = -1, best = 0;
    s.steps.forEach((st, i) => { const lk = st.ans && DRAFTS.find(x => x.id === st.ans); const v = (st.ans === r.id ? 9 : 0) + score(text, s.title + ' ' + st.t + (lk ? ' ' + Q(lk) : '')).s; if (v > best) { best = v; step = i; } });
    return { s, step, pct: Math.min(97, Math.round(50 + best * 6)) };
  }).filter(m => m.step >= 0 && m.pct >= 62).sort((a, b) => b.pct - a.pct).slice(0, 3);
}
// the question says what it's about; the answer only adds detail
const sopTopics = (r) => { const c = conceptsOf(Q(r)); return c.length ? c : conceptsOf(answerOf(r)); };
function sopRelated(r) {
  const cs = sopTopics(r);
  return DRAFTS.filter(x => x.id !== r.id && ['approved', 'pending'].includes(decision(x).status) && conceptsOf(Q(x)).some(c => cs.includes(c))).slice(0, 2);
}
function sopSuggest(r, rel) {
  const all = [r].concat(rel.filter(x => sopRel.has(x.id)));
  const n = all.reduce((a, x) => a + Math.min(2, answerOf(x).split(/(?<=\.)\s+|\n+/).filter(t => t.trim().length > 12).length), 0);
  const listy = all.some(x => /(^|\s)(1\.|-)\s/m.test(answerOf(x)));
  return listy || n > 3 ? ['steps', n + ' linear steps, one actor, no branches'] : ['check', n + ' short check' + (n === 1 ? '' : 's') + ', done in any order'];
}
function sopPanel(r) {
  const ms = sopMatches(r), ln = ST.sopLinks[r.id], rel = sopRelated(r);
  if (sopRel === null) sopRel = new Set(rel.map(x => x.id));
  const sug = sopSuggest(r, rel); if (!sopFmt) sopFmt = sug[0];
  if (sopTitle === null) sopTitle = (SOP_AREA[sopTopics(r)[0]] || [])[1] || Q(r).replace(/\?$/, '');
  let b;
  if (sopTab === 'map') b = ms.length ? '<ul class="sopm">' + ms.map((m, i) => { const on = ln && ln.sop === m.s.id;
      return '<li' + (i === 0 ? ' class="is-top"' : '') + '><span><span class="t"><span class="sid">' + m.s.id + '</span>' + esc(m.s.title) + '</span><small>Step ' + (m.step + 1) + ' · ' + esc(m.s.steps[m.step].t) + '</small></span>' +
        '<span class="pct" style="--w:' + m.pct + '%">' + m.pct + '% match<i></i></span>' +
        (on ? '<span class="badge badge--ok">Linked</span>' : '<button class="btn ' + (i === 0 ? 'btn--primary' : 'btn--secondary') + ' btn--sm" type="button" data-sopl="' + m.s.id + '|' + m.step + '">Link</button>') + '</li>'; }).join('') + '</ul>' +
      '<p class="sub" style="margin:12px 0 0">None of these? <a href="#" data-st="new">Build a new SOP</a></p>'
    : '<div class="empty" style="padding:18px"><b>No SOP covers this yet.</b>Build one around this answer.<div style="margin-top:12px"><button class="btn btn--primary btn--sm" type="button" data-st="new">Build a new SOP</button></div></div>';
  else {
    const n = 1 + rel.filter(x => sopRel.has(x.id)).length;
    b = '<div class="sopnew"><div class="fld"><label class="seclbl" for="sopT" style="margin:0">Title</label><input class="text" id="sopT" value="' + esc(sopTitle) + '"></div>' +
      '<div><p class="seclbl">Format</p><div class="sopfmt">' + Object.keys(SOP_FORMATS).map(f => '<button class="chip" type="button" data-fmt="' + f + '" aria-pressed="' + (sopFmt === f) + '">' + SOP_FORMATS[f] + (f === sug[0] ? '<small>Suggested</small>' : '') + '</button>').join('') + '</div><p class="sopwhy">' + esc(sug[1]) + '. You can switch views later.</p></div>' +
      '<div><p class="seclbl">From these answers</p><ul class="soprel"><li><label><span>' + esc(Q(r)) + '</span><span class="badge badge--muted">This one</span></label></li>' +
      rel.map(x => '<li><label><span>' + esc(Q(x)) + '</span>' + (decision(x).status === 'approved' ? '' : '<span class="badge badge--amber">In review</span>') + '</label></li>').join('') + '</ul></div>' +
      '<div class="sopgo"><button class="btn btn--grad" type="button" data-a="sopdraft">Draft SOP from ' + n + ' related answer' + (n === 1 ? '' : 's') + '</button><span class="sub">lojo fills the 10-section template and cites every step. It goes to review like any draft.</span></div></div>';
  }
  return '<div class="sopp" id="sopp" role="region" aria-label="Link to SOP"><div class="sopp__h">' + SOPIC + '<div><b>Link to SOP</b><span class="sub">This answer becomes a step. Its rule stays in the answer and isn’t copied.</span></div><button class="dx" type="button" data-a="sopx" aria-label="Close">×</button></div>' +
    '<div class="sopp__tabs" role="tablist"><button type="button" role="tab" data-st="map" aria-selected="' + (sopTab === 'map') + '"><b>A</b>Add to an existing SOP<em>' + (ms.length || 'none') + '</em></button><button type="button" role="tab" data-st="new" aria-selected="' + (sopTab === 'new') + '"><b>B</b>Build a new SOP</button></div>' +
    '<div class="sopp__b">' + b + '</div></div>';
}
function sopToggle(r) {
  sopOpen = !sopOpen; sopFmt = null; sopTitle = null; sopRel = null;
  if (sopOpen) { sopTab = sopMatches(r).length ? 'map' : 'new'; sopFocus = true; }
  renderDetail();
}
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
// the agent's rewrite, faked with a short wait
function finishRewrite(id) {
  setTimeout(() => { const x = ST.decisions[id]; if (!x || x.status !== 'redrafting') return; x.status = 'pending'; x.redrafted = (x.redrafted || 0) + 1; save(); if (sel === id || tab === 'pending') render(); toast('Rewritten once. Have another look.'); }, 1500);
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
  if (a === 'repick') { delete d.pick; save(); }
  if (a === 'retireold') { ST.retired = ST.retired || {}; ST.retired[r.conflict] = true; d.pick = r.src.find(x => x[0] !== r.conflict)[0]; save(); toast(docShort(r.conflict) + ' retired. You can restore it in Sources.'); }
  // a person answers it from scratch instead of fixing the draft
  if (a === 'own') {
    // the draft moves to Human, opened for you to write
    d.status = 'final'; d.own = true; d.reason = 'You chose to write it'; mode = 'edit'; refs = []; linking = false; typed = ''; save();
    tab = 'final'; document.querySelectorAll('#rtabs .tab').forEach(x => x.setAttribute('aria-selected', x.dataset.f === 'final'));
    toast('Moved to Human. Write your answer.');
  }
  if (a === 'link') { linking = true; keepText(); renderDetail(); $('linkIn').focus(); return; }
  if (a === 'nolink') { linking = false; keepText(); renderDetail(); return; }
  if (a === 'addlink') { const v = $('linkIn').value.trim(); if (!/^https?:\/\/\S+\.\S+/.test(v)) { $('linkIn').focus(); toast('Paste a full link'); return; } refs.push({ kind: 'link', name: v.replace(/^https?:\/\//, '') }); linking = false; keepText(); renderDetail(); return; }
  if (a === 'ai') { draftWithAI(r); return; }
  if (a === 'sop') { sopToggle(r); return; }
  if (a === 'sopx') { sopOpen = false; renderDetail(); return; }
  if (a === 'sopdraft') {
    const t = $('sopT').value.trim(); if (!t) { $('sopT').focus(); return; }
    const me = ST.people.find(p => p.id === ROLE_PERSON[window.LOJO_ROLE || 'admin']);
    const s = draftSop({ title: t, rids: [r.id].concat([...sopRel]), fmt: sopFmt, from: 'answers', by: me ? me.name : 'You' });
    save(); location.href = 'sops.html?id=' + s.id + '&new=1'; return;
  }
  if (a === 'leave') { d.status = 'left'; mode = 'view'; save(); toast('Left out. It won’t be answered.'); next(); render(); return; }
  if (a === 'reject') mode = 'reject';
  if (a === 'cancel') mode = 'view';
  if (a === 'undo') { d.status = 'pending'; mode = 'view'; save(); }
  if (a === 'save') {
    const v = $('editBox').value.trim(); if (!v) return;
    d.edited = v !== answerOf(r) || d.edited; d.answer = v; d.status = 'approved'; d.at = today; d.refs = refs.slice(); mode = 'view';
    toast(d.own ? 'Your answer is approved' : 'Edited and approved'); save(); next();
  }
  if (a === 'confirm') {
    const reason = $('why').value + ($('note').value.trim() ? ': ' + $('note').value.trim() : '');
    mode = 'view';
    d.status = 'redrafting'; d.reason = reason; d.prev = answerOf(r); d.history = (d.history || []).concat([{ text: answerOf(r), reason }]); save();
    finishRewrite(r.id);
  }
  // the reviewer decides a person should answer it
  if (a === 'tohuman') {
    const reason = $('why').value + ($('note').value.trim() ? ': ' + $('note').value.trim() : '');
    mode = 'view'; d.status = 'final'; d.reason = reason; toast('Sent to Human'); save(); next();
  }
  render();
}
$('detail').addEventListener('click', (e) => {
  const rm = e.target.closest('[data-rm]'); if (rm) { keepText(); refs.splice(+rm.dataset.rm, 1); renderDetail(); return; }
  const f = e.target.closest('[data-full]'); if (f) { const k = f.dataset.full; openFull.has(k) ? openFull.delete(k) : openFull.add(k); renderDetail(); return; }
  const fa = e.target.closest('[data-fa]');
  if (fa) {
    const id = fsel, act2 = fa.dataset.fa; ST.draftFailed = ST.draftFailed || {};
    if (act2 === 'write') { fwrite = true; renderDetail(); }
    if (act2 === 'cancel') { fwrite = false; renderDetail(); }
    if (act2 === 'save') { const v = $('fBox').value.trim(); if (!v) { $('fBox').focus(); return; } ST.answered = ST.answered || {}; ST.answered[id] = v; delete ST.draftFailed[id]; fwrite = false; fsel = null; save(); toast('Your answer is approved'); render(); }
    if (act2 === 'leave') { delete ST.draftFailed[id]; ST.matters = ST.matters || {}; ST.matters[id] = false; fsel = null; save(); toast('Dismissed. It won’t be drafted.'); render(); }
    if (act2 === 'retry') {
      ST.draftFailed[id] = 'retrying'; save(); render();
      setTimeout(() => { delete ST.draftFailed[id]; if (fsel === id) fsel = null; save(); render(); toast('Drafted. It joins the next batch to review.'); }, 1600);
    }
    return;
  }
  const us = e.target.closest('[data-use]'); if (us) { const d = ST.decisions[sel] = ST.decisions[sel] || { status: 'pending' }; d.pick = us.dataset.use; save(); toast('Using ' + docShort(d.pick)); render(); return; }
  const ta = e.target.closest('[data-ta]'); if (ta) { ST.matters[tsel] = ta.dataset.ta === 'yes'; save(); toast(ta.dataset.ta === 'yes' ? 'It matters. lojo drafts it for the next batch.' : 'Left out. It won’t be drafted.'); render(); return; }
  const ak = e.target.closest('[data-ask]'); if (ak) { asking = ak.dataset.ask; renderDetail(); return; }
  if (e.target.closest('[data-askx]')) { asking = null; renderDetail(); return; }
  const ag = e.target.closest('[data-askgo]'); if (ag) { ST.gapAsked = ST.gapAsked || {}; ST.gapAsked[ag.dataset.askgo] = $('ownerSel').value; asking = null; save(); toast('Asked ' + ST.gapAsked[ag.dataset.askgo] + '. Their answer comes back here.'); render(); return; }
  const oa = e.target.closest('[data-oa]');
  if (oa) {
    const k2 = oa.dataset.oa;
    if (k2 === 'write') { owrite = true; renderDetail(); }
    if (k2 === 'cancel') { owrite = false; renderDetail(); }
    if (k2 === 'upload') location.href = 'sources.html?src=upload';
    if (k2 === 'save') { const v = $('oBox').value.trim(); if (!v) { $('oBox').focus(); return; } ST.answered = ST.answered || {}; ST.answered[osel] = v; owrite = false; osel = null; save(); toast('Your answer is approved'); render(); }
    if (k2 === 'leave') { ST.matters[osel] = false; owrite = false; osel = null; save(); toast('Left out. It won’t be answered.'); render(); }
    return;
  }
  const sd = e.target.closest('[data-senddoc]'); if (sd) { location.href = 'sources.html?src=upload&gap=' + sd.dataset.senddoc; return; }
  const od = e.target.closest('[data-open]'); if (od) { ltags.clear(); sel = od.dataset.open; const s0 = decision(DRAFTS.find(x => x.id === sel)).status; tab = s0 === 'final' ? 'final' : 'pending'; document.querySelectorAll('#rtabs .tab').forEach(x => x.setAttribute('aria-selected', x.dataset.f === tab)); mode = 'view'; render(); return; }
  const gb = e.target.closest('[data-gap]'); if (gb) { ST.gaps[gb.dataset.gap] = true; save(); toast('Dismissed'); render(); return; }
  // turn the gap into a question someone answers
  // the question goes to lojo first; a person gets it only if lojo can't find an answer
  const gq = e.target.closest('[data-gapq]'); if (gq) { const g = GAPS.find(x => x.id === gq.dataset.gapq); const q = { id: 'qx' + Date.now(), q: 'What is the ' + (/^The /.test(g.term) ? g.term.slice(4) : g.term.replace(/^([A-Z])(?=[a-z])/, m => m.toLowerCase())) + '?', origin: 'you', docs: [], gap: g.id, drafting: true }; ST.extra.push(q); ST.gaps[g.id] = true; save(); toast('Added. lojo is drafting it.'); render(); finishGapDraft(q.id); return; }
  const st = e.target.closest('[data-st]'); if (st) { e.preventDefault(); if ($('sopT')) sopTitle = $('sopT').value; sopTab = st.dataset.st; sopFocus = true; renderDetail(); return; }
  const fm = e.target.closest('[data-fmt]'); if (fm) { sopTitle = $('sopT').value; sopFmt = fm.dataset.fmt; renderDetail(); return; }
  const sl = e.target.closest('[data-sopl]'); if (sl) { const [sid, step] = sl.dataset.sopl.split('|'); ST.sopLinks[sel] = { sop: sid, step: +step }; sopOpen = false; save(); render(); toast('Linked to ' + sid + ', step ' + (+step + 1)); return; }
  const b = e.target.closest('[data-a]'); if (b) act(b.dataset.a);
});
$('items').addEventListener('click', (e) => {
  const nk = e.target.closest('[data-nk]'); if (nk) { nsel = nk.dataset.nk; fwrite = false; asking = null; render(); return; }
  const oq = e.target.closest('[data-oq]'); if (oq) { osel = oq.dataset.oq; owrite = false; render(); return; }
  const gi = e.target.closest('[data-gapid]'); if (gi) { gsel = gi.dataset.gapid; render(); return; }
  const fq = e.target.closest('[data-fq]'); if (fq) { fsel = fq.dataset.fq; fwrite = false; render(); return; }
  const li = e.target.closest('[data-id]'); if (li) { fsel = null; osel = null; owrite = false; sel = li.dataset.id; mode = 'view'; sopOpen = false; render(); }
});
const todayStr = () => new Date().toLocaleDateString('en-GB', { weekday: 'short', day: 'numeric', month: 'short' }).replace(',', '');
$('lq').addEventListener('input', (e) => { lq = e.target.value.trim().toLowerCase(); sel = null; render(); });
const refilter = () => { sel = null; fsel = null; nsel = null; fwrite = false; render(); };
$('lfBtn').addEventListener('click', (e) => { e.stopPropagation(); const m = $('ltags'); m.hidden = !m.hidden; $('lfBtn').setAttribute('aria-expanded', !m.hidden); });
$('ltags').addEventListener('change', (e) => { const c = e.target.closest('[data-tag]'); if (!c) return; c.checked ? ltags.add(c.dataset.tag) : ltags.delete(c.dataset.tag); refilter(); });
$('ltags').addEventListener('click', (e) => { e.stopPropagation(); if (e.target.closest('[data-reset]')) { ltags.clear(); refilter(); } });
$('lfActive').addEventListener('click', (e) => { const u = e.target.closest('[data-untag]'); if (u) { ltags.delete(u.dataset.untag); refilter(); } if (e.target.closest('[data-reset]')) { ltags.clear(); refilter(); } });
document.addEventListener('click', (e) => { if (!e.target.closest('.lfdrop')) { $('ltags').hidden = true; $('lfBtn').setAttribute('aria-expanded', 'false'); } });
document.querySelectorAll('#rtabs .tab').forEach(t => t.addEventListener('click', () => {
  tab = t.dataset.f; document.querySelectorAll('#rtabs .tab').forEach(x => x.setAttribute('aria-selected', x === t)); sel = null; fsel = null; nsel = null; osel = null; owrite = false; asking = null; mode = 'view'; ltags.clear(); render();
}));
// full screen review: hides the sidebar and widens both columns; F toggles, Esc leaves
function setFs(on) {
  document.body.classList.toggle('is-fs', on); $('fsBtn').setAttribute('aria-pressed', on);
  $('fsBtn').querySelector('span').textContent = on ? 'Exit full screen' : 'Full screen';
  $('fsBtn').querySelector('svg').innerHTML = on ? '<path d="M4 14h6v6M20 10h-6V4M14 10l7-7M3 21l7-7"/>' : '<path d="M15 3h6v6M9 21H3v-6M21 3l-7 7M3 21l7-7"/>';
  try { sessionStorage.setItem('lojo-build-fs', on ? '1' : ''); } catch (err) {}
}
$('fsBtn').addEventListener('click', () => setFs(!document.body.classList.contains('is-fs')));
try { if (sessionStorage.getItem('lojo-build-fs')) setFs(true); } catch (err) {}
document.addEventListener('keydown', (e) => {
  if (e.target.closest('input,textarea,select') || e.metaKey || e.ctrlKey) return;
  if (e.key.toLowerCase() === 'f') { setFs(!document.body.classList.contains('is-fs')); return; }
  if (e.key === 'Escape' && document.body.classList.contains('is-fs') && mode === 'view' && !document.querySelector('dialog[open]')) { setFs(false); return; }
  const k = e.key.toLowerCase(), r = DRAFTS.find(x => x.id === sel);
  if (k === 'j' || k === 'k') {
    const its = [...document.querySelectorAll('#items .item')], i = its.findIndex(x => x.classList.contains('is-sel'));
    const n = its[Math.max(0, Math.min(its.length - 1, i + (k === 'j' ? 1 : -1)))];
    if (n) { mode = 'view'; n.click(); const s2 = document.querySelector('#items .item.is-sel'); if (s2) s2.scrollIntoView({ block: 'nearest' }); }
    return;
  }
  const onDraft = r && !(tab === 'needs') && !(tab === 'final' && osel) && !needsPick(r);
  if (onDraft && decision(r).status === 'pending' && mode === 'view') {
    if (k === 'a') act('approve'); if (k === 'e') act('edit'); if (k === 'r') act('reject');
  }
  if (onDraft && ['pending', 'approved'].includes(decision(r).status) && mode === 'view' && k === 'l') act('sop');
  if (k === 'escape' && sopOpen) { sopOpen = false; renderDetail(); }
  if (k === 'escape' && mode !== 'view') act('cancel');
});
const RP = new URLSearchParams(location.search);
// arriving from an Insights action that has no draft to open yet
(function fromInsights() {
  const q = RP.get('q') && allQuestions().find(x => x.id === RP.get('q')), g = RP.get('gap') && GAPS.find(x => x.id === RP.get('gap')), o = RP.get('opp') && RP.get('t');
  const v = q ? ['Recurring question', q.q, (q.docs && q.docs.length ? 'lojo is drafting it from ' + q.docs.map(docShort).join(', ') + '. It lands in Drafts when it’s ready.' : 'Nothing in your documents answers it yet. Write the answer once and lojo reuses it every time it comes up.'), '#questions']
    : g ? ['Knowledge gap', g.term, g.why + ' Explain it here so answers that mention it can be approved.', '#gaps']
    : o ? ['Opportunity', o, 'Write how support should answer this until it exists, so people get a straight answer today.', '#opportunities'] : null;
  if (!v) return;
  const el = $('fromIns'); el.hidden = false;
  el.innerHTML = '<div><small>From Insights · ' + v[0] + '</small><b>' + esc(v[1]) + '</b><p>' + esc(v[2]) + '</p></div><a href="insights.html' + v[3] + '">Back to Insights</a><button type="button" aria-label="Dismiss">×</button>';
  el.querySelector('button').addEventListener('click', () => { el.hidden = true; });
})();
if (RP.get('edit')) mode = 'edit';
// open a tab directly, e.g. from the dashboard
if (RP.get('fq')) nsel = 'failed:' + RP.get('fq');
if (['pending', 'needs', 'approved', 'final'].includes(RP.get('tab'))) { tab = RP.get('tab'); document.querySelectorAll('#rtabs .tab').forEach(x => x.setAttribute('aria-selected', x.dataset.f === tab)); }
// from an Insights gap: open the first pending draft that leans on it
if (RP.get('gap') && !RP.get('sel')) { const gr = DRAFTS.find(r => decision(r).status === 'pending' && gapsOf(r).some(g => g.id === RP.get('gap'))); if (gr) sel = gr.id; }
if (RP.get('sel')) { sel = RP.get('sel'); const sr = DRAFTS.find(x => x.id === sel); if (sr) { const s = decision(sr).status; tab = s === 'redrafting' ? 'pending' : (s === 'approved' || s === 'final') ? s : 'pending'; document.querySelectorAll('#rtabs .tab').forEach(x => x.setAttribute('aria-selected', x.dataset.f === tab)); } if (RP.get('full')) { const r = DRAFTS.find(x => x.id === sel); if (r) openFull.add(r.src[0][0] + '|' + r.src[0][1]); } }
if (HL_GAP) setTimeout(() => { const it = document.querySelector('.item.is-sel.is-hl') || document.querySelector('.item.is-hl'); if (it) it.scrollIntoView({ block: 'nearest' }); const n = document.querySelector('.gapnote .g.is-hl'); if (n) n.scrollIntoView({ block: 'center', behavior: 'smooth' }); }, 300);
if (RP.get('sop') === 'new' && !RP.get('sel')) {
  const ok = (x) => decision(x).status === 'approved' && !ST.sopLinks[x.id];
  const fr = [DRAFTS.find(x => x.id === 'r9')].filter(x => x && ok(x))[0] || DRAFTS.filter(x => decision(x).status === 'approved' && !ST.sopLinks[x.id]).sort((a, b) => (sopRelated(b).length - sopRelated(a).length) || (sopMatches(a).length - sopMatches(b).length))[0];
  if (fr) { sel = fr.id; sopOpen = true; sopTab = 'new'; sopFocus = true; }
}
if (tab === 'needs' && RP.get('kind') && !nsel) { const it = needItems().find(i => i[0] === RP.get('kind')); if (it) nsel = it[0] + ':' + it[1]; }
// a gap question drafted by lojo: from the document sent for the gap if there is one, otherwise it goes to a person
function finishGapDraft(qid) {
  setTimeout(() => {
    const q = ST.extra.find(x => x.id === qid); if (!q || !q.drafting) return;
    const g = GAPS.find(x => x.id === q.gap), sent = (ST.gapDocs || {})[q.gap];
    q.drafting = false;
    if (sent) {
      const n = Date.now(), doc = { id: 'dx' + n, name: sent, pages: 2, size: '—', added: 'Today' };
      const r = { id: 'rx' + n, qid: q.id, src: [[doc.id, 'p. 1', 'Sent to explain ' + g.term.replace(/^The /, 'the ') + '.']],
        draft: 'Drafted from ' + sent.replace(/\.[a-z]+$/i, '') + '. Check the details against the document before you approve.', redraft: 'Drafted again from ' + sent.replace(/\.[a-z]+$/i, '') + '.' };
      q.docs = [doc.id]; ST.xdocs = (ST.xdocs || []).concat([doc]); ST.xdrafts = (ST.xdrafts || []).concat([r]); DOCS.push(doc); DRAFTS.push(r);
      save(); render(); toast('Drafted from ' + sent + '. It’s in Drafts.');
    } else { q.why = 'lojo tried to draft it and couldn’t find an answer in your sources.'; save(); render(); toast('lojo couldn’t find an answer. It’s in Human for a person.'); }
  }, 1800);
}
ST.extra.filter(q => q.drafting).forEach(q => finishGapDraft(q.id));
// a rewrite cut short by leaving the page finishes when you come back
Object.keys(ST.decisions).forEach(id => { if (ST.decisions[id].status === 'redrafting') finishRewrite(id); });
render();
""")

# ============================================================ APPROVED
APPROVED = dict(
  active='approved', title='Distribute',
  css=r"""
  .srcsel{width:auto;min-width:220px;height:36px;padding:0 34px 0 12px}
  .bar{display:flex;align-items:center;gap:12px;flex-wrap:wrap}

  .apilead{margin:0 0 18px;color:var(--muted);max-width:70ch}
  .apih{font-size:1rem;font-weight:700;margin:0 0 2px}
  .apisub{margin:0 0 10px;color:var(--muted);font-size:.86rem}
  .apicard{border:1px solid var(--line);border-radius:16px;background:var(--panel);padding:18px 20px;margin-bottom:22px;display:grid;gap:12px}
  .apicard p{margin:0;color:var(--muted);font-size:.88rem}
  .apilist{padding:0;gap:0}
  .apirow{display:flex;align-items:center;gap:14px;padding:14px 20px}
  .apirow + .apirow{border-top:1px solid var(--line)}
  .apirow > div{flex:1;min-width:0}
  .apirow b{display:block;font-size:.92rem}
  .apirow span{display:block;color:var(--muted);font-size:.8rem}
  .apiempty{padding:26px 20px;text-align:center;color:var(--muted)}
  .apiempty b{display:block;color:var(--ink);margin-bottom:4px}
  .modes{display:flex;gap:8px;flex-wrap:wrap}
  .modes button{height:34px;padding:0 14px;border-radius:999px;border:1px solid var(--line-2);background:var(--panel);font-weight:600;font-size:.84rem;cursor:pointer}
  .modes button[aria-pressed="true"]{background:var(--ink);border-color:var(--ink);color:#fff}
  .modes button:disabled{cursor:default}
  .addr{display:flex;align-items:center;gap:12px;padding:10px 12px 10px 14px;border-radius:12px;background:var(--bg-soft)}
  .addr code{flex:1;font-family:ui-monospace,Menlo,monospace;font-size:.86rem;overflow:hidden;text-overflow:ellipsis}
  .keyrow{display:flex;gap:10px}
  .keyrow .text{flex:1}
  .scopes{display:flex;gap:8px;flex-wrap:wrap}
  .scopes button{height:32px;padding:0 13px;border-radius:999px;border:1px solid var(--line-2);background:var(--panel);font-size:.82rem;font-weight:600;cursor:pointer}
  .scopes button[aria-pressed="true"]{background:var(--ink);border-color:var(--ink);color:#fff}
  .scopes em{font-style:normal;font-weight:500;opacity:.7;margin-left:4px}
  .newkey{display:grid;gap:8px;padding:12px 14px;border-radius:12px;background:#EFF7F1;border:1px solid rgba(63,143,95,.25)}
  .newkey b{font-size:.88rem}
  .kchips{display:flex;gap:6px;flex-wrap:wrap;margin-top:4px}
  .kchips i{font-style:normal;font-size:.72rem;font-weight:600;padding:2px 8px;border-radius:999px;background:var(--bg-soft);color:var(--muted)}
  :root[data-theme="dark"] .newkey{background:rgba(63,143,95,.12)}

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

  /* hub: the approved answers, then one row per channel */
  .head .back{display:inline-flex;font-size:.8rem;font-weight:600;color:var(--muted);margin:0 0 2px;text-decoration:none}
  .head .back:hover{color:var(--ink)}
  .hacts{display:flex;align-items:center;gap:10px;flex-wrap:wrap}
  .hacts:empty{display:none}
  .store{display:flex;align-items:center;gap:16px;padding:18px 20px;margin:0 0 26px}
  .store div{flex:1;min-width:0}
  .store b{display:block;font-family:var(--display);font-size:1.05rem}
  .store span{display:block;color:var(--muted);font-size:.86rem}
  .chl{list-style:none;margin:0;padding:0;border:1px solid var(--line);border-radius:16px;background:var(--panel);overflow:hidden}
  .chl li + li{border-top:1px solid var(--line)}
  .chrow{display:flex;align-items:center;gap:16px;padding:16px 20px;color:inherit;text-decoration:none;transition:background-color .15s ease}
  .chrow:hover{background:var(--bg-soft);text-decoration:none}
  .chrow:focus-visible{outline:2px solid var(--rose);outline-offset:-2px}
  .chrow__ic{width:40px;height:40px;border-radius:12px;display:grid;place-items:center;background:var(--bg-soft);flex:none}
  .chrow__ic svg{width:20px;height:20px;fill:none;stroke:var(--ink);stroke-width:1.7;stroke-linecap:round;stroke-linejoin:round}
  .chrow__t{flex:1;min-width:0}
  .chrow__t b{display:block;font-size:.95rem}
  .chrow__t span,.chrow__m > span:last-child{display:block;color:var(--muted);font-size:.82rem}
  .chrow__m{display:grid;justify-items:end;gap:4px;text-align:right;max-width:46%}
  .chrow__go{font-size:1.4rem;color:var(--muted);line-height:1}
  .chl__more{margin:12px 2px 0;color:var(--muted);font-size:.82rem}
  @media (max-width:700px){.chrow{flex-wrap:wrap}.chrow__m{justify-items:start;text-align:left;max-width:none;order:3;width:100%;padding-left:56px}.chrow__go{display:none}.store{flex-wrap:wrap}}

  /* Help Center: setup, then the managed page */
  .steps{list-style:none;display:flex;gap:8px;flex-wrap:wrap;margin:0 0 16px;padding:0}
  .steps li{display:flex;align-items:center;gap:8px;height:34px;padding:0 14px 0 6px;border-radius:999px;border:1px solid var(--line);background:var(--panel);font-size:.82rem;font-weight:600;color:var(--muted)}
  .steps i{font-style:normal;width:22px;height:22px;border-radius:50%;display:grid;place-items:center;background:var(--bg-soft);font-size:.72rem}
  .steps .is-on{border-color:var(--ink);color:var(--ink)}
  .steps .is-on i{background:var(--ink);color:#fff}
  .steps .is-done i{background:rgba(63,143,95,.15);color:var(--success)}
  .hcs{padding:22px 24px;display:grid;gap:12px;max-width:820px}
  .hcs h2,.hcc h2{font-family:var(--display);font-size:1.05rem;margin:0}
  .hcs__p,.hcc__p{margin:0;color:var(--muted);font-size:.88rem;max-width:68ch}
  .hcs__note,.hcc__note{margin:0;color:var(--muted);font-size:.8rem}
  .hcs__f{display:flex;align-items:center;gap:10px;flex-wrap:wrap;padding-top:14px;border-top:1px solid var(--line);font-size:.84rem;color:var(--muted)}
  .hcs__f .spacer{flex:1}
  .tgrp{font-size:.72rem;font-weight:800;letter-spacing:.1em;text-transform:uppercase;color:var(--muted);margin:8px 0 0}
  .tgrp span{font-weight:600;letter-spacing:0;margin-left:4px}
  .publ{list-style:none;margin:0;padding:0;border:1px solid var(--line);border-radius:12px}
  .publ li{display:flex;align-items:center;gap:10px;padding:10px 14px;flex-wrap:wrap}
  .publ li + li{border-top:1px solid var(--line)}
  .publ label{display:flex;align-items:center;gap:10px;flex:1;min-width:0;cursor:pointer;font-size:.9rem}
  .publ input{width:16px;height:16px;accent-color:var(--ink);flex:none}
  .publ .spacer{flex:1}
  .pubq{font-size:.9rem;min-width:0}
  .pubq .badge{margin-left:6px;vertical-align:1px}
  .opts{display:grid;gap:10px}
  .opt{display:flex;gap:12px;align-items:flex-start;padding:14px 16px;border:1px solid var(--line-2);border-radius:12px;cursor:pointer}
  .opt:has(input:checked){border-color:var(--ink);box-shadow:0 0 0 3px rgba(36,26,20,.06)}
  .opt input{margin-top:3px;accent-color:var(--ink)}
  .opt > span{display:grid;gap:4px;flex:1}
  .opt b{font-size:.92rem}
  .opt span span{color:var(--muted);font-size:.82rem}
  .opt .text{max-width:320px;margin-top:6px}
  .sum{display:grid;gap:0;margin:0;border:1px solid var(--line);border-radius:12px}
  .sum div{display:grid;grid-template-columns:140px 1fr;gap:12px;padding:10px 14px}
  .sum div + div{border-top:1px solid var(--line)}
  .sum dt{color:var(--muted);font-size:.82rem}
  .sum dd{margin:0;font-size:.88rem;font-weight:600}
  .hcban{display:flex;align-items:center;gap:16px;padding:16px 20px;border-radius:16px;margin:0 0 16px;background:var(--ink);color:#fff}
  .hcban div{flex:1}
  .hcban b{display:block;font-size:.98rem}
  .hcban span{display:block;font-size:.84rem;opacity:.75}
  .hcban.is-draft{background:var(--amber-soft);color:var(--ink)}
  .hcban.is-off{background:var(--bg-soft);color:var(--ink)}
  .hcban .sw{width:30px;height:17px}
  .hcban .sw::after{top:2.5px;left:2.5px;width:12px;height:12px}
  .hcban .sw[aria-checked="true"]::after{transform:translateX(13px)}
  .hcc{padding:18px 20px;margin:0 0 14px;display:grid;gap:12px}
  .hcc__h{display:flex;align-items:baseline;gap:10px;flex-wrap:wrap}
  .hcc__l{display:flex;gap:8px;flex-wrap:wrap}
  .rows{display:grid;gap:12px}
  .hcc .srow,.rows .srow{display:flex;align-items:center;gap:14px;padding:12px 0 0;border-top:1px solid var(--line)}
  .hcc .srow:first-child,.rows .srow:first-child{border-top:0;padding-top:0}
  .hcc .srow > div,.rows .srow > div{flex:1;min-width:0}
  .hcc .srow b,.rows .srow b{display:block;font-size:.9rem}
  .hcc .srow span,.rows .srow span{display:block;color:var(--muted);font-size:.8rem}
  .hcc .srow .badge,.rows .srow .badge{display:inline-flex;margin-left:6px;vertical-align:1px}
  .hcc__e{margin:0;color:var(--muted);font-size:.86rem}
  .sw{position:relative;width:40px;height:22px;border-radius:999px;border:0;background:var(--line-2);cursor:pointer;flex:none;transition:background-color .15s ease}
  .sw::after{content:"";position:absolute;top:3px;left:3px;width:16px;height:16px;border-radius:50%;background:#fff;box-shadow:0 1px 2px rgba(0,0,0,.2);transition:transform .15s ease}
  .sw[aria-checked="true"]{background:var(--ink)}
  .sw[aria-checked="true"]::after{transform:translateX(18px)}
  .sw:disabled{opacity:.45;cursor:default}
  .sw:focus-visible{outline:2px solid var(--rose);outline-offset:2px}
  .fixed{font-size:.72rem;font-weight:700;color:var(--muted);white-space:nowrap}
  .seg{display:inline-flex;border:1px solid var(--line-2);border-radius:999px;padding:2px;flex:none}
  .seg button{height:28px;padding:0 12px;border:0;border-radius:999px;background:none;font:inherit;font-size:.78rem;font-weight:600;color:var(--muted);cursor:pointer}
  .seg button[aria-pressed="true"]{background:var(--ink);color:#fff}
  .swatches{display:flex;gap:8px}
  .swatches button{width:28px;height:28px;border-radius:50%;border:2px solid var(--panel);box-shadow:0 0 0 1px var(--line-2);cursor:pointer}
  .swatches button[aria-checked="true"]{box-shadow:0 0 0 2px var(--ink)}
  .logo-pv{font-family:var(--display);font-weight:800;font-size:1.2rem}
  .rows .srow--col{flex-direction:column;align-items:stretch;gap:10px}
  #vSub .sr-only{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}
  .swatches{flex-wrap:wrap}
  .swcustom{position:relative;width:28px;height:28px;border-radius:50%;border:2px solid var(--panel);box-shadow:0 0 0 1px var(--line-2);background:conic-gradient(#E53E3E,#DD6B20,#D69E2E,#38A169,#3182CE,#805AD5,#D53F8C,#E53E3E);cursor:pointer;display:grid;place-items:center}
  .swcustom.is-on{box-shadow:0 0 0 2px var(--ink)}
  .swcustom input{position:absolute;inset:0;opacity:0;width:100%;height:100%;cursor:pointer;border:0;padding:0}
  .swcustom:focus-within{outline:2px solid var(--ink);outline-offset:2px}
  .bgsw{display:flex;gap:8px;flex-wrap:wrap}
  .bgsw button{display:grid;gap:4px;justify-items:center;padding:0;border:0;background:none;font:inherit;font-size:.72rem;color:var(--muted);cursor:pointer}
  .bgsw button i{width:52px;height:34px;border-radius:9px;box-shadow:0 0 0 1px var(--line-2);border:2px solid var(--panel)}
  .bgsw button[aria-checked="true"] i{box-shadow:0 0 0 2px var(--ink)}
  .bgsw button[aria-checked="true"]{color:var(--ink);font-weight:700}
  .lchips{display:flex;gap:6px;flex-wrap:wrap}
  .lchip{display:inline-flex;align-items:center;gap:6px;padding:6px 12px;border:1px solid var(--line-2);border-radius:999px;background:var(--panel);font:inherit;font-size:.84rem;color:var(--ink);cursor:pointer}
  .lchip svg{width:13px;height:13px;fill:none;stroke:currentColor;stroke-width:2.2;stroke-linecap:round;stroke-linejoin:round}
  .lchip[aria-pressed="true"]{background:var(--ink);border-color:var(--ink);color:#fff}
  .lchip.is-main{background:var(--bg-soft);border-color:var(--line);cursor:default}
  .lchip.is-main small{font-size:.7rem;color:var(--muted)}
  .pv__wave{display:inline-block;margin-right:.3em}
  .rows .srow .bgsw,.rows .srow .swatches{display:flex;flex-wrap:wrap;gap:8px}
  .rows .srow .lchips{display:flex}
  .rows .srow .lchip.is-main small{display:inline;color:var(--muted)}
  .pvv.has-vid{color:var(--ok,#2E7D4F)}
  .hed{display:grid;gap:12px}
  .hed__back{justify-self:start;border:0;background:none;padding:4px 0;font:inherit;font-size:.86rem;font-weight:600;color:var(--muted);cursor:pointer}
  .hed__back:hover{color:var(--ink)}
  .hed .fld{max-width:none}
  .hed .fld b{font-size:.84rem}
  .hed .fld small{color:var(--muted);font-size:.78rem}
  .rows .srow--col .fld{max-width:none}
  .rows .srow--col .fld b{font-size:.84rem}
  .rows .srow--col .fld small{color:var(--muted);font-size:.78rem}
  .rows .srow--col .hed__2{width:100%}
  .hed textarea.text{min-height:76px}
  .hed__2{display:grid;grid-template-columns:1fr 1fr;gap:10px}
  .hed__ans{padding:12px 14px;border-radius:12px;background:var(--bg-soft);border:1px solid var(--line);max-height:220px;overflow:auto}
  .hed__ans .ansbody{margin:0;font-size:.86rem}
  .hed__meta{font-size:.78rem;color:var(--muted)}
  .hed__acts{display:flex;gap:8px;flex-wrap:wrap;align-items:center}
  .hed__cv{display:grid;gap:10px;padding-top:12px;border-top:1px solid var(--line)}
  .hed__cv h3{display:flex;align-items:center;gap:8px;margin:0;font-size:.92rem}
  .hed__cv p{margin:0;font-size:.8rem;color:var(--muted)}
  .hed__stale{padding:10px 12px;border-radius:10px;background:#FFF4DC;color:#8A6212;font-size:.82rem}
  .pubq .badge--vid{background:color-mix(in srgb,var(--ok,#2E7D4F) 12%,transparent);color:var(--ok,#2E7D4F)}
  .pv__art .pv__go{margin-top:6px}
  @media (max-width:1100px){.hed__2{grid-template-columns:1fr}}
  .sugv{list-style:none;margin:0;padding:0}
  .sugv li{display:flex;align-items:center;gap:12px;padding:10px 0;border-top:1px solid var(--line)}
  .sugv li:first-child{border-top:0}
  .sugv div{flex:1;min-width:0}
  .sugv b{display:block;font-size:.9rem}
  .sugv span{color:var(--muted);font-size:.8rem}
  .vdlg{width:min(520px,calc(100vw - 32px))}
  .vdlg .seg{margin-bottom:14px}
  .vdlg .fld{max-width:none;margin-bottom:14px}
  .vdlg .fld b{font-size:.82rem}
  .vdlg__hint{display:block;margin-top:6px;font-size:.8rem;color:var(--muted)}
  .vdlg__hint.is-ok{color:var(--ok,#2E7D4F);font-weight:600}
  .vdlg__hint.is-err{color:var(--error)}
  .vdrop{display:flex;align-items:center;gap:12px;padding:14px;border:1.5px dashed var(--line-2);border-radius:14px;margin-bottom:14px}
  .vdrop.is-over{border-color:var(--ink);background:color-mix(in srgb,var(--ink) 4%,transparent)}
  .vdrop div{flex:1;min-width:0;display:grid;gap:2px;font-size:.84rem}
  .vdrop div b{overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
  .vdrop div span{color:var(--muted);font-size:.78rem}
  .vdlg__f{justify-content:flex-start}
  .vdlg__f .spacer{flex:1}
  .srow--col > div:first-child{display:grid;gap:2px}
  .lgdrop{display:flex;align-items:center;gap:14px;padding:14px;border:1.5px dashed var(--line-2);border-radius:14px;transition:border-color .15s,background .15s}
  .lgdrop.is-over{border-color:var(--ink);background:color-mix(in srgb,var(--ink) 4%,transparent)}
  .lgdrop__pv{flex:none;width:132px;height:64px;border-radius:10px;border:1px solid var(--line);display:grid;place-items:center;overflow:hidden;
    background:#fff conic-gradient(#F1EEEB 25%,#fff 0 50%,#F1EEEB 0 75%,#fff 0) 0 0/12px 12px}
  .lgdrop__pv img{max-width:116px;max-height:48px;object-fit:contain}
  .lgdrop__pv svg{width:22px;height:22px;fill:none;stroke:var(--muted);stroke-width:1.7}
  .lgdrop__t{flex:1;min-width:0;display:grid;gap:2px;font-size:.84rem}
  .lgdrop__t b{overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
  .lgdrop__t span{color:var(--muted);font-size:.78rem}
  .lgdrop__a{display:flex;gap:6px;flex-wrap:wrap}
  .lglink{display:flex;align-items:center;border:1px solid var(--line-2);border-radius:10px;background:var(--panel);overflow:hidden}
  .lglink span{padding:0 10px;color:var(--muted);font-size:.84rem;border-right:1px solid var(--line);align-self:stretch;display:grid;place-items:center;background:color-mix(in srgb,var(--ink) 3%,transparent)}
  .lglink input{flex:1;min-width:0;border:0;padding:9px 10px;font:inherit;font-size:.88rem;background:none;color:inherit}
  .lglink:focus-within{outline:2px solid var(--ink);outline-offset:1px}
  .srow .lgdrop{flex-wrap:wrap}
  .srow .lgdrop .lgdrop__pv{display:grid;color:inherit}
  .srow .lgdrop .lgdrop__t{display:grid;flex:1 1 120px;font-size:.84rem;color:var(--ink)}
  .srow .lgdrop .lgdrop__t span{color:var(--muted);font-size:.78rem}
  .srow .lgdrop .lgdrop__t b{white-space:normal;overflow-wrap:anywhere}
  .srow .lgdrop .lgdrop__a{display:flex}
  .srow .lglink > span{display:grid;place-items:center;font-size:.84rem}
  .rows .srow > div:first-child{flex:1;min-width:0}
  .lglink input:focus{outline:none}
  .langs{display:flex;gap:14px;flex-wrap:wrap;font-size:.86rem}
  .langs label{display:flex;gap:6px;align-items:center}
  .fld{display:grid;gap:6px;max-width:420px}
  .fld b{font-size:.86rem}

  /* visitor preview: the customer's site, always light */
  .dlg.pv{width:100vw;height:100vh;max-width:none;max-height:none;margin:0;border-radius:0;overflow:auto;background:#fff}
  .dlg.pv .pv__bar--v{position:sticky;top:0;z-index:5}
  .pv__bar{position:sticky;top:0;z-index:2;display:flex;align-items:center;gap:6px;padding:10px 14px;background:#EFECE9;border-bottom:1px solid #E2DDD8}
  .pv__bar i{width:10px;height:10px;border-radius:50%;background:#D9D3CD}
  .pv__bar code{flex:1;margin:0 10px;padding:5px 12px;border-radius:8px;background:#fff;color:#6B625C;font-size:.8rem;font-family:ui-monospace,Menlo,monospace;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
  .pv__site{--hc:#1F7A7A;background:#fff;color:#1E2A2A;font-size:.9rem}
  .pv__site{--hc2:#E5194C}
  .pv__top{display:flex;align-items:center;gap:22px;padding:14px 28px;border-bottom:1px solid #EEE;font-size:.8rem}
  .pv__logo{display:grid;line-height:1;color:var(--hc);text-decoration:none}
  .pv__logo img{display:block;width:auto;max-width:220px;object-fit:contain}
  .pv__logo b{font-family:var(--body);font-weight:800;font-size:1.45rem;letter-spacing:-.02em}
  .pv__logo small{font-size:.48rem;font-weight:700;letter-spacing:.18em;color:#557;white-space:nowrap}
  .pv__nav{display:flex;gap:20px;color:#3B4747;white-space:nowrap;font-size:.84rem}
  .pv__nav span.is-on{color:var(--hc);font-weight:700}
  .pv__top .spacer{flex:1}
  .pv__lang{display:inline-flex;align-items:center;gap:6px;color:#3B4747;font-size:.8rem;white-space:nowrap}
  .pv__lang svg{width:14px;height:14px;fill:none;stroke:currentColor;stroke-width:1.8}
  .pv__btn{font-style:normal;font-weight:700;font-size:.8rem;color:#fff;background:var(--hc2);padding:7px 14px;border-radius:999px;white-space:nowrap}
  .pv__hero{padding:40px 28px 30px;text-align:center;background:var(--hbg,color-mix(in srgb,var(--hc) 12%,#fff))}
  .pv__hero h2{font-family:Georgia,'Times New Roman',serif;font-weight:600;font-size:2rem;letter-spacing:-.01em;line-height:1.15;margin:0 0 8px;color:#1A2626}
  .pv__hero > p{margin:0 0 20px;color:#5B6767;font-size:.9rem}
  .pv__search{display:flex;align-items:center;gap:10px;max-width:620px;margin:0 auto;padding:6px 6px 6px 18px;border-radius:999px;border:2px solid color-mix(in srgb,var(--hc) 75%,#fff);background:#fff;text-align:left;color:#8A9494;box-shadow:0 10px 26px -20px rgba(0,0,0,.5)}
  .pv__search > span{flex:1;min-width:0;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;font-size:.86rem}
  .pv__search > svg{width:18px;height:18px;flex:none;fill:none;stroke:#556;stroke-width:1.8}
  .pv__mic{width:34px;height:34px;border-radius:50%;display:grid;place-items:center;background:color-mix(in srgb,var(--hc) 12%,#fff);flex:none}
  .pv__mic svg{width:16px;height:16px;fill:none;stroke:var(--hc);stroke-width:1.8}
  .pv__search em{font-style:normal;font-size:.8rem;font-weight:700;color:#fff;background:var(--hc);padding:9px 16px;border-radius:999px;white-space:nowrap}
  .pv__pop{display:flex;flex-wrap:wrap;justify-content:center;align-items:center;gap:6px;margin-top:14px;font-size:.78rem;color:#5B6767}
  .pv__pop button{padding:4px 10px;border:0;border-radius:999px;background:color-mix(in srgb,var(--hc) 14%,#fff);color:color-mix(in srgb,var(--hc) 80%,#000);font:inherit;font-weight:600;cursor:pointer;max-width:200px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
  .pv__talk{display:inline-flex;align-items:center;gap:8px;margin-top:12px;padding:7px 14px;border:1px solid #D5DEDE;border-radius:999px;background:#fff;font-size:.8rem;font-weight:600;color:#2C3B3B}
  .pv__talk svg{width:14px;height:14px;fill:none;stroke:currentColor;stroke-width:1.8}
  .pv__main{padding:24px 28px 30px;display:grid;gap:24px}
  .pv__sh{display:flex;align-items:baseline;justify-content:space-between;gap:10px;margin:0 0 12px}
  .pv__sh h3{font-weight:700;font-size:1.05rem;margin:0;color:#1A2222}
  .pv__sh em{font-style:normal;color:var(--hc);font-weight:700;font-size:.8rem}
  .pv__topics{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:10px}
  .pv__topics button{display:flex;align-items:center;gap:12px;padding:14px;border:1px solid #E1E7E7;border-radius:12px;background:#fff;font:inherit;color:inherit;text-align:left;cursor:pointer}
  .pv__topics button:hover{border-color:color-mix(in srgb,var(--hc) 50%,#fff)}
  .pv__topics i{flex:none;width:38px;height:38px;border-radius:10px;display:grid;place-items:center;background:color-mix(in srgb,var(--hc) 10%,#fff)}
  .pv__topics svg{width:18px;height:18px;fill:none;stroke:var(--hc);stroke-width:1.8;stroke-linecap:round;stroke-linejoin:round}
  .pv__topics b{display:block;font-size:.88rem}
  .pv__topics b + span{display:block;font-size:.74rem;color:#667}
  .pv__low{display:grid;gap:22px;width:100%;max-width:620px;margin:0 auto}
  .pv__help{display:flex;flex-wrap:wrap;align-items:center;justify-content:center;gap:8px;padding:12px 16px;border-radius:12px;background:color-mix(in srgb,var(--hc) 7%,#fff);border:1px solid color-mix(in srgb,var(--hc) 14%,#fff)}
  .pv__help b{font-size:.84rem;margin-right:4px;color:#1A2626}
  .pv__help span{display:inline-flex;align-items:center;gap:6px;padding:5px 11px;border-radius:999px;background:#fff;border:1px solid #DDE5E5;font-size:.78rem;font-weight:600;color:#2C3B3B}
  .pv__help svg{width:14px;height:14px;fill:none;stroke:var(--hc);stroke-width:1.9;stroke-linecap:round;stroke-linejoin:round}
  .hlp{display:grid;grid-template-columns:auto 1fr;gap:8px 12px;align-items:center}
  .hlp small{grid-column:2;margin-top:-4px;color:var(--muted);font-size:.76rem}
  .pv__low .pv__sh{justify-content:center;position:relative}
  .pv__low .pv__sh em{position:absolute;right:0}
  .pv__trend{list-style:none;margin:0;padding:0}
  .pv__trend li{border-bottom:1px solid #E6EBEB}
  .pv__trend button{width:100%;display:flex;align-items:center;gap:8px;padding:10px 0;border:0;background:none;font:inherit;font-size:.84rem;color:inherit;text-align:left;cursor:pointer}
  .pv__trend button > span{flex:1;min-width:0}
  .pv__trend button:hover > span{color:var(--hc)}
  .pv__trend small{flex:none;font-size:.62rem;font-weight:800;letter-spacing:.06em;padding:2px 6px;border-radius:5px;background:color-mix(in srgb,var(--hc) 14%,#fff);color:color-mix(in srgb,var(--hc) 80%,#000)}
  .pv__trend i{font-style:normal;color:#889}
  .pv__vids{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:10px;align-items:start}
  .pv__vids button{display:grid;align-content:start;gap:6px;padding:0;border:0;background:none;font:inherit;color:inherit;text-align:left;cursor:pointer}
  .pv__vids i{aspect-ratio:16/9;border-radius:10px;display:grid;place-items:center;background:linear-gradient(135deg,color-mix(in srgb,var(--hc) 90%,#000),color-mix(in srgb,var(--hc) 75%,#fff))}
  .pv__vids i::after{content:'';width:28px;height:28px;border-radius:50%;background:#fff url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'%3E%3Cpath d='M9 7l9 5-9 5z' fill='%23222'/%3E%3C/svg%3E") center/16px no-repeat}
  .pv__vids b{font-size:.78rem;line-height:1.35;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden}
  .pv__vids span{font-size:.7rem;color:#889}
  .pv__player{position:relative;aspect-ratio:16/9;max-width:560px;margin:0 0 16px;border-radius:12px;display:grid;place-items:center;background:linear-gradient(135deg,color-mix(in srgb,var(--hc) 90%,#000),color-mix(in srgb,var(--hc) 70%,#fff))}
  .pv__player::after{content:'';width:46px;height:46px;border-radius:50%;background:#fff url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'%3E%3Cpath d='M9 7l9 5-9 5z' fill='%23222'/%3E%3C/svg%3E") center/22px no-repeat}
  .pv__player small{position:absolute;left:12px;bottom:10px;color:#fff;font-size:.74rem;font-weight:600}
  .pv__art{padding:22px 28px 30px;max-width:720px}
  .pv__crumb{border:0;background:none;padding:0;font:inherit;font-size:.8rem;color:var(--hc);cursor:pointer;margin-bottom:10px}
  .pv__art h2{font-family:Georgia,serif;font-weight:600;font-size:1.45rem;margin:0 0 6px}
  .pv__val{margin:0 0 16px;color:#3F8F5F;font-size:.8rem;font-weight:600}
  .pv__fb{display:flex;align-items:center;gap:8px;flex-wrap:wrap;margin-top:18px;padding-top:14px;border-top:1px solid #EEE;font-size:.84rem}
  .pv__fb span{padding:5px 12px;border:1px solid #DDE;border-radius:999px}
  .pv__fb em{margin-left:auto;font-style:normal;color:var(--hc);font-weight:600}
  .pv__empty{padding:30px 28px;text-align:center;color:#667}
  .pv__foot{display:flex;gap:10px;padding:14px 28px;border-top:1px solid #EEE;font-size:.76rem;color:#889}
  .pv__foot .spacer{flex:1}
  .pv__by{display:inline-flex;align-items:center;gap:5px}
  .pv__by img{display:block}
  @media (max-width:760px){.pv__topics{grid-template-columns:1fr 1fr}.pv__vids{grid-template-columns:1fr 1fr}}

  /* builder: steps on the left, live preview on the right */
  .hcb{display:grid;grid-template-columns:minmax(340px,440px) minmax(0,1fr);gap:24px;align-items:start}
  .hcb__side{display:grid;gap:12px;min-width:0}
  .hcb__side > .hcc,.hcb__side > .bar{margin:0}
  .hcb__intro{margin:0 0 2px;color:var(--muted);font-size:.86rem}
  .bcard{display:flex;align-items:center;gap:12px;width:100%;padding:14px 16px;border:1px solid var(--line);border-radius:14px;background:var(--panel);font:inherit;color:inherit;text-align:left;cursor:pointer;transition:border-color .15s ease,box-shadow .15s ease}
  .bcard:hover{border-color:var(--ink);box-shadow:0 14px 30px -24px rgba(36,26,20,.5)}
  .bcard:focus-visible{outline:2px solid var(--ink);outline-offset:2px}
  .bcard i{font-style:normal;width:26px;height:26px;border-radius:50%;display:grid;place-items:center;background:var(--bg-soft);font-size:.78rem;font-weight:700;flex:none}
  .bcard__t{flex:1;min-width:0;display:grid;gap:2px}
  .bcard__t b{font-size:.95rem}
  .bcard__t span{color:var(--muted);font-size:.8rem;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
  .bcard__go{flex:none;color:var(--muted);font-size:.82rem;font-weight:600}
  .bcard i svg,.bstep__h i svg{width:15px;height:15px;fill:none;stroke:currentColor;stroke-width:1.9;stroke-linecap:round;stroke-linejoin:round}
  .bcard.is-alert{border-color:#E3C277;background:#FFFAEC}
  .bcard.is-alert i{background:#F8E7BC;color:#8A6212}
  .hacts .sw{width:30px;height:17px}
  .hacts .sw::after{top:2.5px;left:2.5px;width:12px;height:12px}
  .hacts .sw[aria-checked="true"]::after{transform:translateX(13px)}
  .hcstat{display:inline-flex;align-items:center;gap:8px}
  .bstep__b .bar{margin:0}
  .bstep__b .publ li{padding:8px 8px 8px 12px}
  .hcpub__t{margin:0;font-size:.88rem}
  .hcpub__t b{font-weight:700}
  .bcard:hover .bcard__go{color:var(--ink)}
  .bstep{border:1px solid var(--line);border-radius:14px;background:var(--panel);transition:border-color .15s ease,box-shadow .15s ease}
  .bstep.is-on{border-color:var(--ink);box-shadow:0 14px 30px -24px rgba(36,26,20,.5)}
  .bstep__h{display:flex;align-items:center;gap:12px;padding:14px 16px}
  .bstep__h i{font-style:normal;width:26px;height:26px;border-radius:50%;display:grid;place-items:center;background:var(--bg-soft);font-size:.78rem;font-weight:700;flex:none}
  .bstep.is-on .bstep__h i{background:var(--ink);color:#fff}
  .bstep.is-done .bstep__h i{background:rgba(63,143,95,.15);color:var(--success)}
  .bstep__h div{flex:1;min-width:0}
  .bstep__h h2{font-family:var(--body,inherit);font-size:.95rem;font-weight:700;margin:0;outline:0}
  .bstep__h span{display:block;color:var(--muted);font-size:.8rem;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
  .bstep:not(.is-on):not(.is-done) .bstep__h h2{color:var(--muted);font-weight:600}
  .bstep__b{padding:0 16px 16px;display:grid;gap:12px}
  .bstep .publ li{padding:8px 8px 8px 12px}
  .bstep .publ label{align-items:flex-start}
  .bstep .publ input{margin-top:2px}
  .bstep .pubq .badge{display:flex;width:max-content;margin:5px 0 0}
  .bstep .opt{padding:12px 14px}
  .bstep .sum div{grid-template-columns:96px 1fr}
  .publ li:has(.pubacts){flex-wrap:nowrap;align-items:center}
  .publ li:has(.pubacts) .pubq{flex:1;min-width:0}
  .pubacts{display:flex;align-items:center;gap:6px;flex:none}
  #subT .hinfo{position:relative;display:inline-flex;vertical-align:middle;margin-left:8px;font-family:var(--body);font-weight:400;letter-spacing:0}
  .hinfo__b{width:26px;height:26px;border-radius:50%;border:1px solid var(--line);background:var(--panel);color:var(--muted);display:inline-grid;place-items:center;cursor:pointer;padding:0}
  .hinfo__b:hover,.hinfo.is-open .hinfo__b{color:var(--ink);border-color:var(--ink)}
  .hinfo__b:focus-visible{outline:2px solid var(--ink);outline-offset:2px}
  .hinfo__b svg{width:15px;height:15px;fill:none;stroke:currentColor;stroke-width:1.9}
  .hinfo__p{position:absolute;top:calc(100% + 8px);left:0;z-index:30;width:320px;max-width:calc(100vw - 32px);padding:14px 16px;border-radius:14px;border:1px solid var(--line);background:var(--panel);box-shadow:0 24px 50px -24px rgba(36,26,20,.45);font-size:.86rem;font-weight:400;line-height:1.5;color:var(--muted);opacity:0;pointer-events:none;transform:translateY(4px);transition:opacity .15s ease,transform .15s ease}
  .hinfo.is-open .hinfo__p,.hinfo:hover .hinfo__p{opacity:1;pointer-events:auto;transform:none}
  .hinfo__p b{display:block;color:var(--ink);font-weight:700;margin-bottom:4px}
  .pvv{border:0;background:none;font:inherit;font-size:.76rem;font-weight:600;color:var(--muted);padding:5px 9px;border-radius:8px;cursor:pointer;flex:none}
  .pvv:hover,.pvv[aria-pressed="true"]{background:var(--bg-soft);color:var(--ink)}
  .hcb__pv{position:sticky;top:156px;height:calc(100vh - 180px);min-height:460px;display:flex;flex-direction:column;overflow:hidden}
  .pvp__bar{display:flex;align-items:center;gap:10px;padding:10px 12px 10px 16px;border-bottom:1px solid var(--line)}
  .pvp__bar .spacer{flex:1}
  .pvp__t{font-size:.7rem;font-weight:800;letter-spacing:.12em;text-transform:uppercase;color:var(--muted)}
  .pvp__t::before{content:"";display:inline-block;width:7px;height:7px;border-radius:50%;background:var(--success);margin-right:7px;vertical-align:1px}
  .pvp__stage{flex:1;overflow:auto;overscroll-behavior:contain;background:var(--bg-soft);padding:16px}
  .pvp__fit{overflow:hidden}
  .pvp__frame{background:#fff;border-radius:12px;box-shadow:0 18px 40px -26px rgba(36,26,20,.55);overflow:hidden;transform-origin:0 0}
  .pvp__frame.is-desk{width:880px}
  .pvp__frame.is-phone{width:375px;margin:0 auto;border-radius:34px;border:10px solid #1F1A17}
  .pvp__frame.is-phone .pvp__url{justify-content:center}
  .pvp__frame.is-phone .pvp__url i{display:none}
  .pvp__url{display:flex;align-items:center;gap:5px;padding:8px 12px;background:#EFECE9;border-bottom:1px solid #E2DDD8}
  .pvp__url i{width:9px;height:9px;border-radius:50%;background:#D9D3CD}
  .pvp__url code{margin-left:8px;padding:3px 10px;border-radius:6px;background:#fff;color:#6B625C;font-size:.72rem;font-family:ui-monospace,Menlo,monospace;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
  .pv__hidden{margin:0;padding:8px 14px;background:#FFF4DC;color:#8A6212;font-size:.8rem;font-weight:600}
  .pv__site{container-type:inline-size}
  @container (max-width:900px){.pv__nav{gap:14px}.pv__nav span:nth-child(n+3){display:none}}
  @container (max-width:620px){
    .pv__top{padding:12px 16px;gap:10px}
    .pv__hero{padding:24px 16px 20px}
    .pv__hero h2{font-size:1.45rem}
    .pv__main{padding:18px 16px 22px;gap:18px}
    .pv__topics{grid-template-columns:1fr}
    .pv__nav,.pv__btn{display:none}
    .pv__pop,.pv__talk{font-size:.74rem}
    .pv__vids{grid-template-columns:1fr 1fr}
    .pv__art{padding:18px 16px 22px}
    .pv__art h2{font-size:1.2rem}
    .pv__foot{padding:12px 16px;flex-wrap:wrap}
  }
  @media (max-width:1100px){.hcb{grid-template-columns:minmax(280px,1fr) minmax(0,1fr);gap:16px}}
  @media (max-width:760px){.hcb{grid-template-columns:1fr}.hcb__pv{position:static;height:620px}}
  /* ---------- Help Center visual editor */
  :root{--sel:var(--info);--sel-soft:color-mix(in srgb,var(--info) 10%,#fff);--ease-out-strong:cubic-bezier(.23,1,.32,1)}
  #tabHc{margin:-6px 0 0}
  .ve{display:flex;min-height:560px;border:1px solid var(--line);border-radius:16px;background:var(--panel);overflow:hidden}
  .ve__out{width:256px;flex:none;border-right:1px solid var(--line);display:flex;flex-direction:column;min-height:0}
  .ve__otabs{display:flex;gap:4px;padding:10px 10px 0;border-bottom:1px solid var(--line)}
  .ve__otabs button{flex:1;display:inline-flex;align-items:center;justify-content:center;gap:6px;height:36px;border:0;border-bottom:2px solid transparent;background:none;font:inherit;font-size:.84rem;font-weight:600;color:var(--muted);cursor:pointer;white-space:nowrap}
  .ve__otabs button[aria-selected="true"]{color:var(--ink);border-bottom-color:var(--ink)}
  .ve__dot{min-width:18px;height:18px;padding:0 5px;border-radius:999px;background:var(--amber-soft);color:#8A6212;font-size:.68rem;font-weight:800;display:inline-grid;place-items:center}
  .ve__ob{flex:1;overflow:auto;padding:12px 10px 16px;overscroll-behavior:contain}
  .ve__sty{width:100%;display:flex;align-items:center;gap:10px;padding:10px;border:1px solid var(--line);border-radius:12px;background:var(--panel);font:inherit;text-align:left;color:inherit;cursor:pointer;transition:border-color .15s ease,background-color .15s ease}
  .ve__sty:hover{border-color:var(--line-2)}
  .ve__sty.is-sel{background:var(--sel-soft);border-color:color-mix(in srgb,var(--sel) 40%,#fff)}
  .ve__sty i{width:26px;height:26px;border-radius:8px;flex:none;box-shadow:inset 0 0 0 1px rgba(0,0,0,.08)}
  .ve__sty span,.ve__orb span{flex:1;min-width:0;display:grid}
  .ve__sty b,.ve__orb b{font-size:.84rem;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
  .ve__sty small,.ve__orb small{font-size:.74rem;color:var(--muted);white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
  .ve__sty svg,.ve__orb svg,.ve__eye svg,.ve__ib svg,.ve__chk svg,.ve__pubw svg,.ve__pop svg,.blk__tools svg,.blk--hid svg,.ve__ai svg,.ve__drp svg,.pv__note svg{width:16px;height:16px;fill:none;stroke:currentColor;stroke-width:1.9;stroke-linecap:round;stroke-linejoin:round;flex:none}
  .ve__og{display:flex;align-items:baseline;justify-content:space-between;gap:8px;margin:16px 4px 6px;font-size:.68rem;font-weight:800;letter-spacing:.1em;text-transform:uppercase;color:var(--muted)}
  .ve__og span{font-weight:600;letter-spacing:0;text-transform:none;font-size:.72rem}
  .ve__ol{list-style:none;margin:0;padding:0;display:grid;gap:2px}
  .ve__or{position:relative;display:flex;align-items:center;border-radius:10px;transition:background-color .15s ease}
  .ve__or:hover{background:var(--bg-soft)}
  .ve__or.is-sel{background:var(--sel-soft)}
  .ve__or.is-sel b{color:var(--sel)}
  .ve__or.is-hid .ve__orb{opacity:.55}
  .ve__or.is-drag{opacity:.4}
  .ve__or.is-before{box-shadow:inset 0 2px 0 var(--sel)}
  .ve__or.is-after{box-shadow:inset 0 -2px 0 var(--sel)}
  .ve__orb{flex:1;min-width:0;display:flex;align-items:center;gap:10px;padding:8px 8px 8px 10px;border:0;background:none;font:inherit;text-align:left;color:inherit;cursor:pointer;border-radius:10px}
  .ve__orb svg{color:var(--muted);width:14px;height:14px}
  .ve__or.is-mov .ve__orb{cursor:grab}
  .ve__eye{width:28px;height:28px;margin-right:4px;border:0;border-radius:8px;background:none;color:var(--muted);display:grid;place-items:center;cursor:pointer;opacity:0;transition:opacity .15s ease,background-color .15s ease}
  .ve__or:hover .ve__eye,.ve__or.is-hid .ve__eye,.ve__eye:focus-visible{opacity:1}
  .ve__eye:hover{background:var(--panel);color:var(--ink)}
  .ve__oh{margin:14px 4px 0;font-size:.74rem;color:var(--muted);line-height:1.45}
  .ve__alert{width:100%;padding:10px 12px;border:1px solid #E3C277;border-radius:12px;background:#FFFAEC;color:#8A6212;font:inherit;font-size:.8rem;font-weight:700;text-align:left;cursor:pointer;margin-bottom:10px}
  .ve__auto{display:flex;gap:10px;align-items:flex-start;padding:10px;border:1px solid var(--line);border-radius:12px}
  .ve__auto span{flex:1;display:grid;gap:2px}
  .ve__auto b{font-size:.8rem}
  .ve__auto small{font-size:.72rem;color:var(--muted);line-height:1.4}
  .ve__al{list-style:none;margin:0;padding:0;border:1px solid var(--line);border-radius:12px}
  .ve__al li{display:grid;gap:6px;padding:9px 10px}
  .ve__al li + li{border-top:1px solid var(--line)}
  .ve__al li.is-sel{background:var(--sel-soft)}
  .ve__aq{border:0;background:none;padding:0;font:inherit;font-size:.82rem;font-weight:600;text-align:left;color:var(--ink);cursor:pointer;line-height:1.35}
  .ve__aq:hover{text-decoration:underline}
  .ve__am{display:flex;align-items:center;gap:6px;justify-content:space-between}
  .ve__am small{font-size:.7rem;color:var(--success);white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
  .seg--xs button{height:22px;padding:0 8px;font-size:.68rem}
  .ve__main{position:relative;flex:1;min-width:0;display:flex;flex-direction:column;background:var(--bg-soft)}
  .ve__tb{display:flex;align-items:center;gap:10px;padding:10px 14px;border-bottom:1px solid var(--line);background:var(--panel)}
  .ve__mid{flex:1;display:flex;align-items:center;justify-content:center;gap:4px}
  .seg--ic button{width:34px;padding:0;display:grid;place-items:center}
  .seg--ic svg{width:15px;height:15px;fill:none;stroke:currentColor;stroke-width:1.9;stroke-linecap:round;stroke-linejoin:round}
  .seg button{white-space:nowrap;transition:background-color .15s ease,color .15s ease}
  .ve__ib{width:32px;height:32px;border:0;border-radius:999px;background:none;color:var(--muted);display:grid;place-items:center;cursor:pointer;transition:background-color .15s ease,color .15s ease}
  .ve__ib:hover:not(:disabled){background:var(--bg-soft);color:var(--ink)}
  .ve__ib:disabled{opacity:.35;cursor:default}
  .ve__ib:focus-visible,.ve__orb:focus-visible,.ve__sty:focus-visible,.ve__stb:focus-visible,.ve__aq:focus-visible,.ve__otabs button:focus-visible,.ve__chk:focus-visible,.blk__tools button:focus-visible{outline:2px solid var(--ink);outline-offset:2px}
  .ve__stb{display:inline-flex;align-items:center;gap:8px;height:34px;padding:0 14px 0 10px;border:1px solid var(--line-2);border-radius:999px;background:var(--panel);font:inherit;font-size:.8rem;font-weight:600;color:var(--ink);cursor:pointer;white-space:nowrap}
  .ve__stb i{width:14px;height:14px;border-radius:50%;box-shadow:inset 0 0 0 1px rgba(0,0,0,.1)}
  .ve__stb[aria-pressed="true"]{background:var(--ink);color:#fff;border-color:var(--ink)}
  .ve__stage{position:relative;flex:1;overflow:auto;padding:24px 24px 112px;overscroll-behavior:contain}
  .ve__page{margin:0 auto;max-width:1120px;background:#fff;border-radius:14px;box-shadow:0 1px 2px rgba(36,26,20,.06),0 20px 44px -30px rgba(36,26,20,.45);overflow:hidden;transition:max-width .28s var(--ease-out-strong)}
  .ve__page.is-tab{max-width:768px}
  .ve__page.is-phone{max-width:390px;border-radius:26px}
  .ve__stage.has-insp .ve__page.is-phone{margin-left:max(0px,calc(50% - 390px))}
  .ve__page{transition:max-width .28s var(--ease-out-strong),margin .28s var(--ease-out-strong)}
  .ve__page .pv__site{min-height:100%}
  /* section chrome: hover shows its name, a click selects it */
  .blk{position:relative}
  .blk::after{content:"";position:absolute;inset:0;pointer-events:none;box-shadow:inset 0 0 0 1px transparent;z-index:3;transition:box-shadow .15s ease}
  .blk:hover::after{box-shadow:inset 0 0 0 1px var(--sel)}
  .blk.is-sel::after{box-shadow:inset 0 0 0 2px var(--sel)}
  .blk:not(.is-sel){cursor:pointer}
  .blk__tag{position:absolute;top:0;left:0;z-index:4;padding:3px 8px;border-radius:0 0 8px 0;background:var(--sel);color:#fff;font:600 .68rem/1.3 var(--body);letter-spacing:.02em;opacity:0;pointer-events:none;transition:opacity .15s ease;white-space:nowrap}
  .blk:hover > .blk__tag,.blk.is-sel > .blk__tag{opacity:1}
  .blk__tools{position:absolute;top:8px;right:8px;z-index:5;display:flex;align-items:center;gap:2px;padding:3px;border-radius:999px;background:var(--ink);box-shadow:0 10px 24px -12px rgba(0,0,0,.5)}
  .blk__tools button{display:inline-flex;align-items:center;gap:5px;height:28px;min-width:28px;padding:0 8px;border:0;border-radius:999px;background:none;color:#fff;font:600 .74rem var(--body);cursor:pointer;justify-content:center}
  .blk__tools button:hover:not(:disabled){background:rgba(255,255,255,.14)}
  .blk__tools button:disabled{opacity:.35;cursor:default}
  .blk__tools svg{width:14px;height:14px}
  .blk__tools i{width:1px;height:16px;background:rgba(255,255,255,.25);margin:0 2px}
  .blk--hid{display:flex;align-items:center;gap:10px;padding:10px 14px;border:1.5px dashed var(--line-2);border-radius:12px;color:var(--muted);font:500 .8rem var(--body);background:#fff}
  .blk--hid span{flex:1}
  .blk__ph{margin:0;padding:14px;border:1.5px dashed var(--line-2);border-radius:12px;text-align:center;color:var(--muted);font:.8rem var(--body)}
  .inl{outline:1.5px dashed var(--sel);outline-offset:3px;border-radius:3px;cursor:text;min-width:2ch;display:inline-block}
  .inl:focus{outline-style:solid;background:color-mix(in srgb,var(--sel) 6%,transparent)}
  /* settings beside the selected section */
  .vi{position:absolute;z-index:8;width:340px;max-width:calc(100% - 16px);display:flex;flex-direction:column;max-height:480px;border:1px solid var(--line);border-radius:16px;background:var(--panel);box-shadow:0 24px 50px -24px rgba(36,26,20,.45);animation:viIn .18s var(--ease-out-strong)}
  .vi--style{top:62px;right:14px;max-height:min(580px,calc(100% - 8rem))}
  @keyframes viIn{from{opacity:0;transform:scale(.97)}to{opacity:1;transform:none}}
  .vi__h{display:flex;align-items:center;justify-content:space-between;gap:8px;padding:10px 10px 10px 16px;border-bottom:1px solid var(--line)}
  .vi__h b{font-size:.9rem}
  .vi__b{overflow:auto;padding:14px 16px 16px;display:grid;gap:12px;overscroll-behavior:contain}
  .vi__b .rows .srow{flex-wrap:wrap}
  .vi__b .fld{max-width:none}
  .vi__b .fld b{font-size:.8rem}
  .vi__b .fld small{color:var(--muted);font-size:.74rem}
  .vi__b .text{height:36px;font-size:.84rem}
  .vi__b textarea.text{height:auto}
  .vi__b .rows .srow b{font-size:.84rem}
  .vi__b .rows .srow span{font-size:.76rem}
  .vi__b .hed__2{grid-template-columns:1fr}
  .vi__b .lgdrop__pv{width:96px;height:52px}
  .vi__b .opt{padding:10px 12px}
  .vi__b .opt b{font-size:.84rem}
  .vi__b .hed{gap:12px}
  .vi__b .hcc{padding:12px;border-radius:12px;box-shadow:none}
  .vi__b .hcc h2{font-size:.86rem}
  .vi__tip,.vi__note{margin:0;font-size:.76rem;color:var(--muted);line-height:1.45}
  .vi__tip{padding:8px 10px;border-radius:10px;background:var(--sel-soft);color:color-mix(in srgb,var(--sel) 80%,#000)}
  .vi__g{margin:4px 0 0;font-size:.68rem;font-weight:800;letter-spacing:.1em;text-transform:uppercase;color:var(--muted)}
  .vi__topic{display:grid;gap:6px;padding-top:10px;border-top:1px solid var(--line)}
  .vi__acts{display:flex !important;gap:6px;flex-wrap:wrap}
  .vi__b .sugv li{padding:8px 10px}
  /* AI bar */
  .ve__ai{position:absolute;left:50%;bottom:18px;transform:translateX(-50%);z-index:9;width:min(576px,calc(100% - 32px));display:flex;align-items:center;gap:10px;padding:6px 6px 6px 16px;border:1px solid var(--line-2);border-radius:999px;background:var(--panel);box-shadow:0 18px 40px -20px rgba(36,26,20,.5)}
  .ve__ai > svg{color:var(--rose)}
  .ve__ai input{flex:1;min-width:0;border:0;background:none;font:inherit;font-size:.88rem;color:var(--ink);height:34px}
  .ve__ai input:focus{outline:none}
  .ve__ai:focus-within{border-color:var(--ink)}
  .ve__aigo{width:34px;height:34px;border-radius:50%;border:0;background:var(--ink);color:#fff;display:grid;place-items:center;cursor:pointer;flex:none;transition:transform .15s var(--ease-out-strong),opacity .15s ease}
  .ve__aigo:active:not(:disabled){transform:scale(.97)}
  .ve__aigo:disabled{opacity:.3;cursor:default}
  .ve__chips{position:absolute;left:0;right:0;bottom:calc(100% + 8px);display:flex;flex-wrap:wrap;gap:6px;align-items:center;justify-content:center;font-size:.76rem;color:var(--muted)}
  .ve__chips[hidden]{display:none}
  .ve__chips span{width:100%;text-align:center}
  .ve__chips button{padding:6px 12px;border:1px solid var(--line-2);border-radius:999px;background:var(--panel);font:inherit;font-size:.78rem;font-weight:600;color:var(--ink);cursor:pointer;white-space:nowrap;box-shadow:0 6px 16px -12px rgba(36,26,20,.5)}
  .ve__chips button:hover{border-color:var(--ink)}
  body.ve-on .toast{bottom:96px}
  .toast__undo{border:0;background:rgba(255,255,255,.16);color:#fff;font:inherit;font-size:.8rem;font-weight:700;padding:4px 10px;border-radius:999px;cursor:pointer}
  .toast.has-act{pointer-events:auto}
  /* top bar */
  .ve__st{height:24px}
  .ve__chk{display:inline-flex;align-items:center;gap:6px;height:32px;padding:0 12px;border:1px solid #E3C277;border-radius:999px;background:#FFFAEC;color:#8A6212;font:inherit;font-size:.8rem;font-weight:700;cursor:pointer;white-space:nowrap}
  .ve__chk svg{width:14px;height:14px}
  .ve__pubw{position:relative}
  .ve__pubw > .btn svg{width:14px;height:14px;margin-right:-4px}
  .ve__spin{width:13px;height:13px;border-radius:50%;border:2px solid rgba(255,255,255,.35);border-top-color:#fff;animation:veSpin .7s linear infinite}
  @keyframes veSpin{to{transform:rotate(360deg)}}
  .ve__pop{position:absolute;top:calc(100% + 8px);right:0;z-index:40;width:320px;padding:16px;display:grid;gap:12px;border:1px solid var(--line);border-radius:16px;background:var(--panel);box-shadow:0 24px 50px -24px rgba(36,26,20,.5);animation:viIn .18s var(--ease-out-strong);transform-origin:top right}
  .ve__pop .sum{margin:0;border:1px solid var(--line);border-radius:12px}
  .ve__pop .sum div{grid-template-columns:84px 1fr;padding:8px 12px}
  .ve__pop .sum dd{font-size:.82rem;overflow-wrap:anywhere}
  .ve__pt{margin:0;font-size:.84rem;color:var(--muted)}
  .ve__pt b{color:var(--ink);font-size:.95rem}
  .ve__wait{margin:0;padding:10px 12px;border-radius:12px;background:#FFFAEC;color:#8A6212;font-size:.8rem;line-height:1.45}
  .ve__wait button{border:0;background:none;padding:0;font:inherit;font-weight:700;color:inherit;text-decoration:underline;cursor:pointer}
  .ve__wide{width:100%}
  .ve__live{display:flex;align-items:center;gap:8px;margin:0;font-weight:700;color:var(--success)}
  .ve__addr{display:flex;align-items:center;justify-content:space-between;gap:8px;padding:9px 12px;border-radius:12px;background:rgba(63,143,95,.1);color:var(--success);font:600 .82rem ui-monospace,Menlo,monospace;text-decoration:none}
  .ve__off{justify-self:start;padding:0}
  /* review drawer */
  .ve__dr{position:fixed;inset:0;z-index:70}
  .ve__drbg{position:absolute;inset:0;background:rgba(36,26,20,.2);animation:drBg .28s var(--ease-out-strong)}
  .ve__drp{position:absolute;top:0;right:0;bottom:0;width:min(460px,100%);display:flex;flex-direction:column;background:var(--panel);box-shadow:-24px 0 60px -30px rgba(36,26,20,.5);animation:drIn .28s var(--ease-out-strong)}
  @keyframes drIn{from{transform:translateX(100%)}to{transform:none}}
  @keyframes drBg{from{opacity:0}to{opacity:1}}
  .ve__drp header{display:flex;gap:12px;align-items:flex-start;padding:20px 20px 16px;border-bottom:1px solid var(--line)}
  .ve__drp header div{flex:1}
  .ve__drp h2{margin:0 0 4px;font-family:var(--display);font-size:1.2rem;outline:0}
  .ve__drp header p{margin:0;font-size:.82rem;color:var(--muted)}
  .ve__drb{flex:1;overflow:auto;padding:16px 20px 24px;display:grid;gap:12px;align-content:start}
  .ve__card{display:grid;gap:10px;padding:14px;border:1px solid var(--line);border-radius:14px}
  .ve__cm{margin:0;font-size:.74rem;font-weight:700;color:var(--muted)}
  .ve__cm .is-ok{color:var(--success)}
  .ve__cm .is-warn{color:#8A6212}
  .ve__flag{display:flex;gap:8px;align-items:flex-start;margin:0;padding:9px 11px;border-radius:10px;background:#FFF4DC;color:#8A6212;font-size:.8rem}
  .ve__card h3{margin:0;font-size:.95rem;line-height:1.35}
  .ve__ans{margin:0;max-height:150px;overflow:auto;padding:10px 12px;border-radius:10px;background:var(--bg-soft);font-size:.82rem}
  .ve__src{display:flex;align-items:center;gap:6px;margin:0;font-size:.74rem;color:var(--muted)}
  .ve__src svg{width:13px;height:13px}
  .ve__ca{display:flex;gap:6px;align-items:center;flex-wrap:wrap}
  .ve__ca .spacer{flex:1}
  .ve__ca svg{width:14px;height:14px}
  .ve__done{display:grid;justify-items:center;gap:8px;padding:48px 16px;text-align:center}
  .ve__done svg{width:36px;height:36px;color:var(--success)}
  .ve__done p{margin:0 0 8px;color:var(--muted);font-size:.86rem;max-width:30ch}
  /* the page itself: style options */
  .pv__site h2,.pv__site .pv__sh h3,.pv__site .pv__help b{font-family:var(--hfont,Georgia,serif)}
  .pv__site .pv__sh h3{font-weight:700}
  .pv__site .pv__topics button,.pv__site .pv__help,.pv__site .pv__vids i,.pv__site .pv__player,.pv__site .pv__ai{border-radius:var(--hr,12px)}
  .pv__site .pv__topics i{border-radius:calc(var(--hr,12px) - 2px)}
  .pv__site .pv__search,.pv__site .pv__search em,.pv__site .pv__go2,.pv__site .pv__pop button,.pv__site .pv__btn,.pv__site .pv__help span,.pv__site .pv__mic{border-radius:var(--hpill,999px)}
  .pv__hero.is-left{text-align:left}
  .pv__hero.is-left .pv__search{margin:0}
  .pv__site .pv__main{gap:20px}
  .pv__site .pv__main > .blk > .pv__pop,.pv__site .pv__main > .pv__pop{margin:0}
  .pv__pop{color:#5B6767}
  .pv__tlist{display:grid;grid-template-columns:1fr 1fr;gap:18px 28px}
  .pv__tlist h4{margin:0 0 6px;font-size:.9rem}
  .pv__tlist h4 small{font-weight:600;color:#889;font-size:.74rem}
  .pv__tlist ul{list-style:none;margin:0;padding:0;display:grid;gap:4px}
  .pv__tlist button{border:0;background:none;padding:0;font:inherit;font-size:.84rem;color:var(--hc);text-align:left;cursor:pointer}
  .pv__fb span{display:inline-flex;align-items:center;gap:6px}
  .pv__fb svg{width:14px;height:14px;fill:none;stroke:currentColor;stroke-width:1.8;stroke-linecap:round;stroke-linejoin:round}
  .pv__rel{margin-top:22px}
  .pv__rel h3{font-size:.95rem;margin:0 0 6px}
  .pv__art .pv__hidden{border-radius:8px;margin:0 0 14px}
  .pv__search input{flex:1;min-width:0;border:0;background:none;font:inherit;font-size:.86rem;color:inherit;height:34px}
  .pv__search input:focus{outline:none}
  .pv__search:focus-within{box-shadow:0 0 0 3px color-mix(in srgb,var(--hc) 20%,transparent)}
  .pv__go2{border:0;font:inherit;font-size:.8rem;font-weight:700;color:#fff;background:var(--hc);padding:9px 16px;cursor:pointer;white-space:nowrap}
  .pv__ask{padding:22px 28px 30px;max-width:720px;display:grid;gap:14px;justify-items:start}
  .pv__ask h2{margin:0;font-weight:600;font-size:1.45rem;outline:0}
  .pv__ask .pv__search{width:100%;margin:0}
  .pv__ask .pv__crumb{margin:0}
  .pv__ai{width:100%;display:grid;gap:8px;padding:16px;background:color-mix(in srgb,var(--hc) 7%,#fff);border:1px solid color-mix(in srgb,var(--hc) 18%,#fff)}
  .pv__ai > b{font-size:.84rem;color:color-mix(in srgb,var(--hc) 80%,#000)}
  .pv__ai p{margin:0;font-size:.92rem;line-height:1.6}
  .pv__ai small{font-size:.7rem;font-weight:800;letter-spacing:.08em;text-transform:uppercase;color:#778}
  .pv__ai ul{list-style:none;margin:0;padding:0;display:grid;gap:4px}
  .pv__ai li button{border:0;background:none;padding:0;font:inherit;font-size:.84rem;font-weight:600;color:var(--hc);text-align:left;cursor:pointer}
  .pv__ai li button span{font-weight:400;color:#778}
  .pv__ai.is-none{background:#fff;border-color:#E1E7E7}
  .pv__mail{display:flex;gap:8px;flex-wrap:wrap}
  .pv__mail input{flex:1 1 200px;height:38px;padding:0 12px;border:1px solid #D5DEDE;border-radius:10px;font:inherit}
  .pv__mail button{height:38px;padding:0 16px;border:0;border-radius:var(--hpill,999px);background:var(--hc);color:#fff;font:inherit;font-weight:700;cursor:pointer;white-space:nowrap}
  .pv__logo[data-pvhome]{cursor:pointer}
  .pv__bar--v{background:var(--ink);border-bottom:0;color:#fff;padding:10px 16px}
  .pv__back{border:0;background:rgba(255,255,255,.12);color:#fff;font:inherit;font-size:.82rem;font-weight:700;padding:7px 14px;border-radius:999px;cursor:pointer;white-space:nowrap}
  .pv__back:focus-visible{outline:2px solid #fff;outline-offset:2px}
  .pv__bar--v .spacer{flex:1}
  .pv__note{display:inline-flex;align-items:center;gap:8px;font-size:.8rem;opacity:.85}
  @container (max-width:620px){.pv__tlist{grid-template-columns:1fr}.pv__ask{padding:18px 16px 22px}}
  @media (max-width:1240px){.ve__out{display:none}}
  /* full screen: the app sidebar goes away and the editor fills the window */
  body.is-fs .side,body.is-fs .mnav,body.is-fs .fab{display:none!important}
  body.is-fs .main{margin-left:0}
  body.is-fs .wrap{max-width:none;padding:12px 16px 16px}
  body.is-fs .head{margin:-12px -16px 12px;padding:10px 16px}
  body.is-fs .head h1{font-size:1.3rem;margin:2px 0 0}
  body.is-fs .ve__out{display:flex}
  body.is-fs .toast{left:50%}
  .ve__fs[aria-pressed="true"]{background:var(--ink);color:#fff}
  .ve__fs[aria-pressed="true"]:hover:not(:disabled){background:var(--ink);color:#fff}
  @media (max-width:900px){.ve__mid{display:none}.ve__tb{justify-content:space-between}}
  @media (max-width:640px){.ve__pvb,.ve__st,.ve__chk span,.pv__n1{display:none}.ve__stage{padding:12px 12px 112px}}
  @media (prefers-reduced-motion:reduce){.ve__page,.vi,.ve__pop,.ve__drp,.ve__drbg,.blk::after,.blk__tag{transition:none;animation:none}}

""",
  body=r"""
    <div id="vHub">
      <div class="head">
        <div>
          <p class="label">04 Distribute</p>
          <h1>Distribute</h1>
          <p>Your approved answers, and where they go.</p>
        </div>
      </div>
      <section class="card store" id="store"></section>
      <h2 class="sech">Channels</h2>
      <ul class="chl" id="chl"></ul>
      <p class="chl__more">More channels are coming: an FAQ widget for your site, a smart contact form and WhatsApp.</p>
    </div>
    <div id="vSub" hidden>
      <div class="head">
        <div>
          <a class="back" href="distribute.html" id="backHub">← Distribute</a>
          <h1 id="subT"></h1>
          <p id="subP"></p>
        </div>
        <span class="spacer"></span>
        <span class="hacts" id="hcActs"></span>
        <button class="btn btn--secondary" id="csv">Export CSV</button>
        <button class="btn btn--primary" id="json">Export JSON</button>
      </div>
    <div id="tabAsk" hidden>
      <div class="askhost" id="askHost"></div>
    </div>
    <div id="tabAnswers">
    <form class="smart" id="smartForm">
      <svg class="smart__ic" viewBox="0 0 24 24"><path d="M12 3l1.8 4.7L18.5 9.5l-4.7 1.8L12 16l-1.8-4.7L5.5 9.5l4.7-1.8z"/><path d="M19 15l.8 2.2L22 18l-2.2.8L19 21l-.8-2.2L16 18l2.2-.8z"/></svg>
      <input id="filter" placeholder="Search or ask: “find everything about refunds”, “remove answers about SSO”, “edit the API answer”" aria-label="Search or ask" autocomplete="off">
      <button class="btn btn--primary btn--sm" type="submit">Go</button>
    </form>
    <div class="smart__tips" id="tips"><span>Try</span><button type="button">find everything about refunds</button><button type="button">edit the API rate limits answer</button><button type="button">remove answers about SSO</button></div>
    <div class="intent" id="intent" hidden></div>
    <div class="bar"><select class="text srcsel" id="srcSel" aria-label="Filter by source"></select><span class="sub" id="meta"></span></div>
    <div class="alist" id="alist"></div>
    </div>

    <div id="tabApi" hidden>
      <h2 class="apih">MCP connector</h2>
      <p class="apisub">For any AI assistant that supports MCP connectors.</p>
      <section class="apicard" id="mcpCard"></section>
      <h2 class="apih">Connected apps</h2>
      <section class="apicard apilist" id="appsCard"></section>
      <div id="keysWrap">
        <h2 class="apih">API keys</h2>
        <p class="apisub">For your own systems and agents. A key belongs to this workspace and does only what you choose from what your role allows.</p>
        <section class="apicard" id="keyMake"></section>
        <section class="apicard apilist" id="keyList"></section>
      </div>
    </div>
    <div id="tabHc" hidden></div>
    </div>
""",
  js=r"""
const approved = () => DRAFTS.filter(r => decision(r).status === 'approved').map(r => ({ r, q: allQuestions().find(q => q.id === r.qid).q, a: answerOf(r), d: decision(r) }));
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
// filter by the document an answer came from
let srcF = '';
function fillSources() {
  const used = [...new Set(approved().flatMap(x => x.r.src.map(s => s[0])))];
  $('srcSel').innerHTML = '<option value="">All sources</option>' + used.map(d => '<option value="' + d + '"' + (d === srcF ? ' selected' : '') + '>' + esc(docShort(d)) + '</option>').join('');
}
function render() {
  const all = approved(), list = all.filter(x => matches(x, ask.topic) && (!srcF || x.r.src.some(s => s[0] === srcF)));
  [...picked].forEach(id => { if (!list.some(x => x.r.id === id)) picked.delete(id); });
  const filtered = ask.topic || srcF;
  $('meta').textContent = (filtered ? list.length + ' of ' : '') + all.length + ' approved answers' + (ask.topic ? ' match “' + ask.topic + '”' : '') + (srcF ? ' from ' + docShort(srcF) : '');
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
$('srcSel').addEventListener('change', (e) => { srcF = e.target.value; render(); });
fillSources();
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


// ---------- API & MCP: the Admin sets the mode and makes keys; everyone connects their own assistant
ST.api = ST.api || { mode: 'signin', apps: [
  { id: 'a1', app: 'claude.ai', pid: 'p1', on: '22 Oct 2026', used: '22 Oct 2026' },
  { id: 'a2', app: 'claude.ai', pid: 'p2', on: '22 Oct 2026', used: '22 Oct 2026' },
], keys: [] };
const APIROLE = window.LOJO_ROLE || 'admin', OWNS = APIROLE === 'admin';
const ME_ID = ({ admin: 'p1', editor: 'p2', viewer: 'p4' })[APIROLE];
const SCOPES = [['adddoc', 'Add documents'], ['addq', 'Add questions'], ['ask', 'Ask'], ['read', 'Read approved answers'], ['readq', 'Read questions']];
let pick = { ask: true, read: true }, fresh = null;
const MODES = { off: ['Off', 'No AI assistant can connect.'], public: ['Public', 'Anyone with the address can read Oslo’s approved answers, without signing in.'], signin: ['Sign-in', 'People of this workspace sign in with lojo and connect their AI assistant.'] };
const ADDR = 'https://mcp.poc.lojo.ai';
const who = (pid) => (ST.people.find(p => p.id === pid) || { name: 'Someone' }).name;
function renderApi() {
  const m = ST.api.mode;
  $('mcpCard').innerHTML = '<div class="modes" role="group" aria-label="MCP connector">' + Object.keys(MODES).map(k => '<button type="button" data-mode="' + k + '" aria-pressed="' + (m === k) + '"' + (OWNS ? '' : ' disabled') + '>' + MODES[k][0] + '</button>').join('') + '</div>' +
    '<p>' + MODES[m][1] + (OWNS ? '' : ' Only Admins change this.') + '</p>' +
    (m === 'off' ? '' : '<div class="addr"><code>' + ADDR + '</code><button class="btn btn--secondary btn--sm" type="button" data-copy="' + ADDR + '">Copy</button></div>' +
      '<p>Add it as a custom connector in your AI assistant, and paste the address.' + (m === 'signin' ? ' You then sign in with lojo and choose this workspace.' : '') + '</p>');
  const apps = ST.api.apps.filter(a => OWNS || a.pid === ME_ID);
  $('appsCard').innerHTML = apps.length ? apps.map(a => '<div class="apirow"><div><b>' + esc(a.app) + '</b><span>Connected by ' + esc(who(a.pid)) + ' on ' + esc(a.on) + ' · Last used ' + esc(a.used) + '</span></div><button class="btn btn--secondary btn--sm" type="button" data-revoke-app="' + a.id + '">Revoke</button></div>').join('')
    : '<div class="apiempty"><b>No connected apps.</b>' + (m === 'off' ? 'Turn the connector on first.' : 'Connect an AI assistant with the address above.') + '</div>';
  $('keysWrap').hidden = !OWNS;
  if (!OWNS) return;
  $('keyMake').innerHTML = '<div class="keyrow"><input class="text" id="keyName" placeholder="Name the key, such as Voicebot" autocomplete="off"><button class="btn btn--primary" type="button" data-make>Make key</button></div>' +
    '<div class="scopes" role="group" aria-label="What the key can do">' + SCOPES.map(([k, l, warn]) => '<button type="button" data-scope="' + k + '" aria-pressed="' + !!pick[k] + '" title="' + (warn ? 'This key can ' + warn : '') + '">' + l + (warn ? '<em>· ' + warn + '</em>' : '') + '</button>').join('') + '</div>' +
    '<p>As Admin, you can give a key any of these.</p>' +
    (fresh ? '<div class="newkey"><b>Copy your key for “' + esc(fresh.name) + '” now. You won’t see it again.</b><div class="addr"><code>' + fresh.secret + '</code><button class="btn btn--secondary btn--sm" type="button" data-copy="' + fresh.secret + '">Copy</button></div></div>' : '');
  $('keyList').innerHTML = ST.api.keys.length ? ST.api.keys.map(k => '<div class="apirow"><div><b>' + esc(k.name) + '</b><span>Made by ' + esc(who(k.pid)) + ' on ' + esc(k.on) + ' · ' + esc(k.hint) + '</span><div class="kchips">' + k.scopes.map(x => '<i>' + (SCOPES.find(s => s[0] === x) || [, x])[1] + '</i>').join('') + '</div></div><button class="btn btn--secondary btn--sm" type="button" data-revoke-key="' + k.id + '">Revoke</button></div>').join('')
    : '<div class="apiempty"><b>No keys yet.</b>Make one above to call lojo from your systems.</div>';
}
function askConfirm(title, body, go) {
  return new Promise((res) => {
    let d = $('apiDlg'); if (!d) { d = document.createElement('dialog'); d.id = 'apiDlg'; d.className = 'dlg'; document.body.appendChild(d); }
    d.innerHTML = '<div class="dlg__b"><h3>' + title + '</h3><p>' + body + '</p></div><div class="dlg__f"><button class="btn btn--secondary" type="button" data-cf="0">Cancel</button><button class="btn btn--primary" type="button" data-cf="1">' + go + '</button></div>';
    d.onclick = (e) => { const b = e.target.closest('[data-cf]'); if (b || e.target === d) { d.close(); res(!!(b && b.dataset.cf === '1')); } };
    d.oncancel = () => res(false); d.showModal();
  });
}
const today = () => new Date().toLocaleDateString('en-GB', { day: 'numeric', month: 'short', year: 'numeric' });
$('tabApi').addEventListener('click', async (e) => {
  const t = e.target;
  const md = t.closest('[data-mode]'); if (md && OWNS && md.dataset.mode !== ST.api.mode) {
    if (md.dataset.mode === 'public' && !(await askConfirm('Make Oslo’s answers public?', 'Anyone with the address can read every approved answer, without signing in. You can turn it off any time.', 'Make public'))) return;
    ST.api.mode = md.dataset.mode; save(); renderApi(); toast('MCP connector: ' + MODES[ST.api.mode][0]); return;
  }
  const cp = t.closest('[data-copy]'); if (cp) { try { navigator.clipboard.writeText(cp.dataset.copy); } catch (err) {} toast('Copied'); return; }
  const ra = t.closest('[data-revoke-app]'); if (ra) { const a = ST.api.apps.find(x => x.id === ra.dataset.revokeApp); if (!(await askConfirm('Revoke ' + esc(a.app) + '?', 'It stops reading Oslo’s answers straight away.', 'Revoke'))) return; ST.api.apps = ST.api.apps.filter(x => x !== a); save(); renderApi(); toast(a.app + ' revoked'); return; }
  const sc = t.closest('[data-scope]'); if (sc) { pick[sc.dataset.scope] = !pick[sc.dataset.scope]; const n = $('keyName').value; renderApi(); $('keyName').value = n; return; }
  if (t.closest('[data-make]')) {
    const name = $('keyName').value.trim(), scopes = SCOPES.map(x => x[0]).filter(k => pick[k]);
    if (!name) { $('keyName').classList.add('is-bad'); $('keyName').focus(); toastError('Name the key first, so you know what uses it.'); return; }
    if (!scopes.length) { toastError('Tick at least one thing the key can do.'); return; }
    const secret = 'lojo_sk_' + Math.random().toString(36).slice(2, 10) + Math.random().toString(36).slice(2, 10);
    ST.api.keys.unshift({ id: 'k' + Date.now(), name, scopes, pid: ME_ID, on: today(), hint: 'ends in …' + secret.slice(-4) });
    fresh = { name, secret }; save(); renderApi(); toast('Key made'); return;
  }
  const rk = t.closest('[data-revoke-key]'); if (rk) { const k = ST.api.keys.find(x => x.id === rk.dataset.revokeKey); if (!(await askConfirm('Revoke “' + esc(k.name) + '”?', 'Anything using this key stops working straight away.', 'Revoke'))) return; ST.api.keys = ST.api.keys.filter(x => x !== k); fresh = null; save(); renderApi(); toast('Key revoked'); }
});
$('tabApi').addEventListener('input', (e) => { if (e.target.id === 'keyName') e.target.classList.remove('is-bad'); });

// ---------- Help Center: built from the approved answers a person makes public
const HC0 = { status: 'new', step: 1, pub: {}, seen: {}, addr: 'sub', domain: 'help.oslopet.com', auto: false, dirty: false,
  modules: { faq: true, search: true, ai: true, voice: true, videos: true, agent: false }, logo: null, logoSize: 'm', logoLink: 'oslopet.com', langSwitch: true, videos: {}, pages: {}, hero: '', sub: '', ph: '', trendT: '', helpT: '', help: {}, wave: true, bg: 'soft', topics: {}, nav: [{ t: 'Pet Insurance', u: 'oslopet.com/insurance' }, { t: 'Vets', u: 'oslopet.com/vets' }, { t: '', u: '' }], btn: { t: 'Get a Quote', u: 'oslopet.com/quote' }, color: '#1F7A7A', langs: { en: true, ar: true, fr: false },
  support: 'care@oslopet.com', sales: 'HubSpot · Sales' };
ST.hc = Object.assign({}, HC0, ST.hc || {}); ST.hc.modules = Object.assign({}, HC0.modules, ST.hc.modules); ST.hc.videos = ST.hc.videos || {}; ST.hc.pages = ST.hc.pages || {}; ST.hc.topics = ST.hc.topics || {}; ST.hc.help = ST.hc.help || {}; ST.hc.nav = ST.hc.nav || HC0.nav.map(x => ({ ...x })); ST.hc.btn = ST.hc.btn || { ...HC0.btn }; delete ST.hc.modules.banner; delete ST.hc.ban;
let hcEdit = null, pvArt = null;
const HC_TOPICS = [['API & limits', /\b(api|rate)\b/i], ['Vets & claims', /vet|clinic|clinique|claim/i], ['Billing & refunds', /refund|pay|invoice|chargeback|billing/i],
  ['Security & login', /sso|saml|okta|data|encrypt|stor|secur/i], ['Plans', /plan|upgrade|limit|onboard|starter|growth|scale/i]];
const topicOf = (q) => (HC_TOPICS.find(t => t[1].test(q)) || ['General'])[0];
// lojo holds back answers that look internal; a person still decides
function hcFlag(x) {
  if (/\b(we|our|us)\b/i.test(x.q)) return 'Reads like a team process';
  if (/still says|told |internal|\bcall\b/i.test(x.a)) return 'Mentions internal notes';
  return '';
}
const MODS = [['faq', 'FAQ pages', 'One page per answer, with steps and documents'], ['search', 'Search', 'Results as you type, forgives typos'],
  ['ai', 'Ask AI', 'Chat answers from your public answers, with sources'], ['voice', 'Voice notes', 'Ask by recording a question'],
  ['videos', 'Short videos', 'Your videos, under the topics and on answer pages. Hidden until you add one'],
  ['agent', 'Voice agent', 'A live voice conversation', true]];
const LANGS = [['en', 'English'], ['ar', 'Arabic'], ['fr', 'French']];
const HC_COLS = [['#1F7A7A', 'Teal'], ['#0E7490', 'Ocean'], ['#3E6FA6', 'Blue'], ['#4F46E5', 'Indigo'], ['#7C3AED', 'Violet'], ['#C7385B', 'Rose'], ['#E0603B', 'Coral'], ['#B7791F', 'Amber'], ['#2F855A', 'Green'], ['#241A14', 'Ink']];
// the background behind the heading and search: a soft tint of the main colour, or a gradient
const HC_BGS = [['soft', 'Soft', 'color-mix(in srgb,var(--hc) 12%,#fff)'], ['brand', 'Brand', 'linear-gradient(135deg,color-mix(in srgb,var(--hc) 26%,#fff),color-mix(in srgb,var(--hc) 5%,#fff))'],
  ['mint', 'Mint', 'linear-gradient(135deg,#DDF5EE,#D6E8FB)'], ['peach', 'Peach', 'linear-gradient(135deg,#FFE7D9,#FBE1EC)'], ['lilac', 'Lilac', 'linear-gradient(135deg,#ECE5FF,#DCEEFF)'], ['sunrise', 'Sunrise', 'linear-gradient(135deg,#FFF2D2,#FFDEDE)'], ['white', 'White', '#fff']];
const hcBg = () => (HC_BGS.find(b => b[0] === ST.hc.bg) || HC_BGS[0])[2];
const hcAddr = () => ST.hc.addr === 'own' ? (ST.hc.domain || 'help.oslopet.com') : 'oslo.help.lojo.ai';
const hcLangs = () => LANGS.filter(([k]) => ST.hc.langs[k]).map(l => l[1]).join(' · ');
const hcMods = () => MODS.filter(([k]) => k !== 'faq' && ST.hc.modules[k]).map(m => m[1]).join(', ');
const hcPublic = () => approved().filter(x => ST.hc.pub[x.r.id]);
const hcCheck = () => approved().filter(x => !ST.hc.seen[x.r.id]);
// videos: the company's own, linked or uploaded, attached to an answer
const VPROV = [['YouTube', /(?:youtube\.com\/(?:watch\?(?:.*&)?v=|shorts\/|embed\/)|youtu\.be\/)[\w-]{6,}/i], ['Vimeo', /vimeo\.com\/(?:video\/)?\d+/i], ['Loom', /loom\.com\/(?:share|embed)\/\w+/i]];
const vProv = (u) => (VPROV.find(([, re]) => re.test(u)) || [''])[0];
const hcVid = (x) => ST.hc.videos[x.r.id];
// how often each answer is asked a month (from Insights)
const asks = (x) => { let h = 0; for (const c of x.r.id) h = (h * 31 + c.charCodeAt(0)) % 997; return 24 + h % 140; };
// how each answer's page reads on the Help Center. The answer itself stays the approved one
const pg = (x) => ST.hc.pages[x.r.id] || {};
const pTitle = (x) => pg(x).title || x.q;
const pTopic = (x) => pg(x).topic || topicOf(x.q);
const cvOf = (x) => pg(x).cv;
const cvStale = (x) => !!(cvOf(x) && cvOf(x).base !== x.a);
const pBody = (x) => { const c = cvOf(x); return c && c.status === 'ok' && !cvStale(x) ? c.text : x.a; };
const pSum = (x) => pg(x).sum || brief(pBody(x));
// lojo's first draft of a customer version: drop team-only lines, speak as the company
function cvDraft(x) {
  const keep = String(x.a).split(/(?<=[.!?])\s+/).filter(t => !/still says|told |internal|\bcall\b/i.test(t))
    .map(t => t.replace(/\bwe\b/g, 'Oslo').replace(/\bWe\b/g, 'Oslo').replace(/\bour\b/gi, 'Oslo’s').replace(/\bus\b/g, 'Oslo'));
  return keep.join(' ').trim() || 'Contact Oslo’s support team and they’ll help you with this.';
}
function groups(list) { const g = {}; list.forEach(x => { const t = pTopic(x); (g[t] = g[t] || []).push(x); }); return Object.entries(g); }
// with "automatically" on, new answers that look safe go public; the rest still wait in To check
function hcSync() {
  if (ST.hc.status === 'new' || !ST.hc.auto) return;
  approved().forEach(x => { if (!ST.hc.seen[x.r.id] && !hcFlag(x)) { ST.hc.seen[x.r.id] = true; ST.hc.pub[x.r.id] = true; } });
}
// re-render, then put focus back on the control the person used
function keepFocus(fn) {
  const a = document.activeElement, sel = a && a !== document.body ? [...a.attributes].filter(x => x.name.startsWith('data-') || (a.type === 'radio' && (x.name === 'name' || x.name === 'value'))).map(x => '[' + x.name + '="' + CSS.escape(x.value) + '"]').join('') : '';
  fn(); if (sel) { const n = document.querySelector('#vSub ' + sel); if (n) n.focus(); }
}

// ---------- shared rows: look and modules, used in setup and after
// the small "Still need help?" strip at the bottom: each option can be switched off and renamed
const HELP_OPTS = [['ai', 'Ask AI', '<path d="M12 3l1.8 4.7 4.7 1.8-4.7 1.8L12 16l-1.8-4.7L5.5 9.5l4.7-1.8z"/>', 'ai'], ['voice', 'Leave a voice note', '<rect x="9" y="3" width="6" height="11" rx="3"/><path d="M5 11a7 7 0 0 0 14 0M12 18v3"/>', 'voice'],
  ['call', 'Request a callback', '<rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4M16 3v4"/>'], ['email', 'Email us', '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/>']];
const helpOn = (k, mod) => (ST.hc.help[k] || {}).on !== false && (!mod || ST.hc.modules[mod]);
const tName = (t) => (ST.hc.topics[t] || {}).title || t;
const tDesc = (t) => (ST.hc.topics[t] || {}).desc || (TOPIC_UI[t] || TOPIC_UI.General)[0];
const HERO0 = 'How can we help?', SUB0 = 'Answers checked by Oslo’s team and in-house vet.', PH0 = 'Search or ask anything… e.g. “Is dental cleaning covered?”';
// the big heading on the home page
function homeRows() {
  const H = ST.hc, other = LANGS.filter(([k]) => k !== 'en' && H.langs[k]).map(l => l[1]);
  return '<div class="srow"><div><b>Wave 👋</b><span>Before the heading, to say hello.</span></div><button class="sw" type="button" role="switch" aria-checked="' + !!H.wave + '" aria-label="Wave before the heading" data-wave></button></div>' +
    '<div class="srow srow--col"><label class="fld"><b>Heading</b><input class="text" data-hf="hero" value="' + esc(H.hero) + '" placeholder="' + esc(HERO0) + '" maxlength="60" autocomplete="off"><small>The big line at the top. Leave empty to use “' + esc(HERO0) + '”.</small></label>' +
    '<label class="fld"><b>Search hint</b><input class="text" data-hf="ph" value="' + esc(H.ph || '') + '" placeholder="' + esc(PH0) + '" maxlength="80" autocomplete="off"><small>The grey text inside the search box.</small></label>' +
    '<label class="fld"><b>Line under it</b><input class="text" data-hf="sub" value="' + esc(H.sub || '') + '" placeholder="' + esc(SUB0) + '" maxlength="90" autocomplete="off"><small>' + (other.length ? 'lojo translates both into ' + other.join(' and ') + '.' : 'One short sentence.') + '</small></label></div>' +
    '<div class="srow srow--col"><div><b>Section titles</b><span>Leave empty to use the default.</span></div><label class="fld"><b>Popular list</b><input class="text" data-hf="trendT" value="' + esc(H.trendT || '') + '" placeholder="Trending this week" maxlength="40" autocomplete="off"></label></div>' +
    '<div class="srow srow--col"><div><b>Help at the bottom</b><span>A small strip at the end of the page. Switch options off, or rename them.</span></div>' +
      '<label class="fld"><b>Title</b><input class="text" data-hf="helpT" value="' + esc(H.helpT || '') + '" placeholder="Still need help?" maxlength="40" autocomplete="off"></label>' +
      HELP_OPTS.map(([k, d, , mod]) => { const off = mod && !H.modules[mod], on = !off && (H.help[k] || {}).on !== false;
        return '<div class="hlp"><button class="sw" type="button" role="switch" aria-checked="' + on + '" aria-label="Show ' + d + '" data-help="' + k + '"' + (off ? ' disabled' : '') + '></button><input class="text" data-hf="help.' + k + '.t" value="' + esc((H.help[k] || {}).t || '') + '" placeholder="' + esc(d) + '" maxlength="30" autocomplete="off" aria-label="Label for ' + d + '"' + (on ? '' : ' disabled') + '>' + (off ? '<small>Turn on ' + (mod === 'ai' ? 'Ask AI' : 'Voice notes') + ' in “On the site” to use this.</small>' : '') + '</div>'; }).join('') + '</div>' +
    '<div class="srow srow--col"><div><b>Topic cards</b><span>lojo makes the topics from your public answers. Rename them or change the line under each.</span></div>' +
    (groups(pvList()).map(([t, xs]) => '<div class="hed__2"><label class="fld"><b>' + esc(t) + ' · ' + xs.length + '</b><input class="text" data-hf="t:' + esc(t) + ':title" value="' + esc((H.topics[t] || {}).title || '') + '" placeholder="' + esc(t) + '" maxlength="40" autocomplete="off" aria-label="Name for ' + esc(t) + '"></label>' +
      '<label class="fld"><b>Description</b><input class="text" data-hf="t:' + esc(t) + ':desc" value="' + esc((H.topics[t] || {}).desc || '') + '" placeholder="' + esc((TOPIC_UI[t] || TOPIC_UI.General)[0]) + '" maxlength="90" autocomplete="off" aria-label="Description for ' + esc(t) + '"></label></div>').join('') || '<span class="hed__meta">Make some answers public to see topics here.</span>') + '</div>';
}
const LOGO_H = { s: 22, m: 30, l: 40 };
const IMG_IC = '<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="4" width="18" height="16" rx="2"/><circle cx="9" cy="10" r="2"/><path d="M21 16l-5-5-9 9"/></svg>';
const kb = (n) => n < 1024 ? n + ' B' : Math.round(n / 1024) + ' KB';
// the header: logo, where it links, and the language switch
function headRows() {
  const H = ST.hc, L = H.logo, many = LANGS.filter(([k]) => H.langs[k]).length > 1;
  return '<div class="srow srow--col"><div><b>Logo</b><span>Shows at the top left of every page. PNG, SVG, JPG or WebP, up to 1 MB. A transparent background works best.</span></div>' +
    '<div class="lgdrop" data-lgdrop><span class="lgdrop__pv">' + (L ? '<img src="' + L.src + '" alt="Your logo">' : IMG_IC) + '</span>' +
    '<span class="lgdrop__t">' + (L ? '<b>' + esc(L.name) + '</b><span>' + kb(L.size) + '</span>' : '<b>Drop your logo here</b><span>or choose a file. Until then the site shows your name.</span>') + '</span>' +
    '<span class="lgdrop__a"><button class="btn btn--secondary btn--sm" type="button" data-logo>' + (L ? 'Replace' : 'Choose file') + '</button>' + (L ? '<button class="btn btn--ghost btn--sm" type="button" data-logorm>Remove</button>' : '') + '</span>' +
    '<input type="file" id="hcLogoFile" accept="image/png,image/svg+xml,image/jpeg,image/webp" hidden></div></div>' +
    '<div class="srow"><div><b>Logo size</b><span>How tall it shows in the header.</span></div><span class="seg" role="group" aria-label="Logo size">' + [['s', 'Small'], ['m', 'Medium'], ['l', 'Large']].map(([k, l]) => '<button type="button" data-lsize="' + k + '" aria-pressed="' + (H.logoSize === k) + '">' + l + '</button>').join('') + '</span></div>' +
    '<div class="srow srow--col"><div><b>Logo link</b><span>Where visitors go when they click the logo, such as your main site. Leave empty to go to the Help Center home.</span></div>' +
    '<label class="lglink"><span>https://</span><input id="hcLogoLink" value="' + esc(H.logoLink || '') + '" placeholder="oslopet.com" autocomplete="off" spellcheck="false" aria-label="Logo link"></label></div>' +
    '<div class="srow srow--col"><div><b>Menu links</b><span>Next to “Help Center” at the top. Leave a name empty to hide it.</span></div>' +
      H.nav.map((n, i) => '<div class="hed__2"><label class="fld"><b class="sr-only">Link ' + (i + 1) + ' name</b><input class="text" data-hf="nav.' + i + '.t" value="' + esc(n.t) + '" placeholder="Name, such as Vets" maxlength="24" autocomplete="off" aria-label="Link ' + (i + 1) + ' name"></label><label class="lglink"><span>https://</span><input data-hf="nav.' + i + '.u" value="' + esc(n.u) + '" placeholder="oslopet.com/vets" autocomplete="off" spellcheck="false" aria-label="Link ' + (i + 1) + ' address"></label></div>').join('') + '</div>' +
    '<div class="srow srow--col"><div><b>Button</b><span>At the top right, such as “Get a Quote”. Leave the text empty for no button.</span></div><div class="hed__2"><label class="fld"><input class="text" data-hf="btn.t" value="' + esc(H.btn.t) + '" placeholder="Get a Quote" maxlength="24" autocomplete="off" aria-label="Button text"></label><label class="lglink"><span>https://</span><input data-hf="btn.u" value="' + esc(H.btn.u) + '" placeholder="oslopet.com/quote" autocomplete="off" spellcheck="false" aria-label="Button link"></label></div></div>' +
    '<div class="srow"><div><b>Language switch</b><span>' + (many ? 'At the top right, so visitors can change language.' : 'Turn on a second language below to use it.') + '</span></div><button class="sw" type="button" role="switch" aria-checked="' + !!(H.langSwitch && many) + '" aria-label="Language switch" data-lswitch' + (many ? '' : ' disabled') + '></button></div>';
}
function lookRows(withFooter) {
  const H = ST.hc, custom = !HC_COLS.some(c => c[0] === H.color), CK = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 12l5 5 9-10"/></svg>', PL = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 5v14M5 12h14"/></svg>';
  return '<div class="srow srow--col"><div><b>Main colour</b><span>Buttons, links, icons and tints. Pick one, or choose your own.</span></div><span class="swatches" role="radiogroup" aria-label="Main colour">' + HC_COLS.map(([c, n]) => '<button type="button" role="radio" aria-checked="' + (H.color === c) + '" aria-label="' + n + '" title="' + n + '" style="background:' + c + '" data-col="' + c + '"></button>').join('') +
      '<label class="swcustom' + (custom ? ' is-on' : '') + '" title="Your own colour"><input type="color" data-colpick value="' + esc(H.color) + '" aria-label="Your own colour"></label></span></div>' +
    '<div class="srow srow--col"><div><b>Top background</b><span>Behind the heading and search.</span></div><span class="bgsw" role="radiogroup" aria-label="Top background">' + HC_BGS.map(([k, n, css]) => '<button type="button" role="radio" aria-checked="' + ((H.bg || 'soft') === k) + '" data-bg="' + k + '"><i style="--hc:' + H.color + ';background:' + css + '"></i>' + n + '</button>').join('') + '</span></div>' +
    '<div class="srow srow--col"><div><b>Languages</b><span>English is the main language. Arabic pages read right to left.</span></div><span class="lchips" role="group" aria-label="Languages">' + LANGS.map(([k, n]) => k === 'en' ? '<span class="lchip is-main">' + n + ' <small>Main</small></span>' : '<button type="button" class="lchip" data-lang="' + k + '" aria-pressed="' + !!H.langs[k] + '">' + (H.langs[k] ? CK : PL) + n + '</button>').join('') + '</span></div>' +
    (withFooter ? '<div class="srow"><div><b>Footer</b><span>“Powered by lojo.ai” shows at the bottom of every page.</span></div><span class="fixed">Always on</span></div>' : '');
}
const modRows = () => MODS.filter(m => m[0] !== 'faq').map(([k, n, d, later]) => '<div class="srow"><div><b>' + n + (later ? '<span class="badge badge--muted">Later</span>' : '') + '</b><span>' + d + '</span></div><button class="sw" type="button" role="switch" aria-checked="' + !!ST.hc.modules[k] + '" aria-label="' + n + '" data-mod="' + k + '"' + (later ? ' disabled' : '') + '></button></div>').join('');

// ---------- the visitor site, built from the public answers and the settings
const pvList = () => hcPublic();
const TOPIC_UI = {
  'Plans': ['Plans, prices, waiting periods', '<path d="M7 3h8l4 4v14H7z"/><path d="M10 11h6M10 15h6"/>'],
  'Vets & claims': ['Submit, track, reimbursement', '<path d="M6 3h12v18l-3-2-3 2-3-2-3 2z"/><path d="M9 8h6M9 12h6"/>'],
  'Billing & refunds': ['Payments, invoices, refunds', '<rect x="3" y="6" width="18" height="13" rx="2"/><path d="M3 10h18"/>'],
  'Security & login': ['Account, login, your data', '<path d="M12 3l8 3v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6z"/><path d="M9 12l2 2 4-4"/>'],
  'API & limits': ['For your developers', '<path d="M8 8l-4 4 4 4M16 8l4 4-4 4"/>'],
  'General': ['Everything else', '<circle cx="12" cy="12" r="9"/><path d="M12 11v5M12 8h.01"/>'],
};
// first one or two sentences of an answer, as plain text, for the AI answer card
const brief = (a) => { const t = String(a).replace(/[#*_`>\[\]]|\(http[^)]*\)/g, '').replace(/\s+/g, ' ').trim(); const m = t.match(/^(.{40,220}?[.!?])(\s|$)/); return m ? m[1] : t.slice(0, 200) + (t.length > 200 ? '…' : ''); };
// ---------- the visitor site: one renderer for the editor (with section chrome) and the visitor preview
const VE_SEC = {
  header: ['Header', 'Logo, menu and button'], hero: ['Welcome & search', 'Heading, search and features'],
  popular: ['Popular questions', 'Shortcuts to the most-read answers'], topics: ['Browse by topic', 'Topic cards from your public answers'],
  trending: ['Trending', 'What visitors read most'], videos: ['Videos', 'Watch in 1 minute'], help: ['Still need help?', 'Ways to reach your team'],
  footer: ['Footer', 'Links and Powered by lojo.ai'], article: ['Answer page', 'How every answer shows'],
};
const VE_MOV = ['popular', 'topics', 'trending', 'videos', 'help'];
const hcOrder = () => { const o = (ST.hc.order || []).filter(k => VE_MOV.includes(k)); VE_MOV.forEach(k => { if (!o.includes(k)) o.push(k); }); return o; };
const hcHid = (k) => (ST.hc.hidden || []).includes(k);
const HC_RAD = { square: '6px', soft: '12px', round: '22px' };
const HC_FONT = { serif: "Georgia,'Times New Roman',serif", sans: 'var(--body)' };
const VI = (d) => '<svg viewBox="0 0 24 24" aria-hidden="true">' + d + '</svg>';
const EYE = '<path d="M2 12s3.5-7 10-7 10 7 10 7-3.5 7-10 7S2 12 2 12z"/><circle cx="12" cy="12" r="3"/>';
const EYE_OFF = '<path d="M3 3l18 18M10.6 5.1A10 10 0 0 1 12 5c6.5 0 10 7 10 7a17 17 0 0 1-3.2 4.1M6.6 6.6C3.8 8.4 2 12 2 12s3.5 7 10 7c1.8 0 3.4-.5 4.8-1.3M9.9 9.9a3 3 0 0 0 4.2 4.2"/>';
const pvSearch = (H, M, mic, IC, live) => {
  const ph = M.ai ? (H.ph || PH0) : 'Search answers';
  const inner = IC('<circle cx="11" cy="11" r="7"/><path d="M20 20l-4-4"/>') + (live ? '<input name="q" placeholder="' + esc(ph) + '" aria-label="Search or ask" autocomplete="off">' : '<span>' + esc(ph) + '</span>') +
    (M.voice ? '<i class="pv__mic">' + mic + '</i>' : '') + (live ? '<button type="submit" class="pv__go2">' + (M.ai ? '✦ Ask AI' : 'Search') + '</button>' : '<em>' + (M.ai ? '✦ Ask AI' : 'Search') + '</em>');
  return live ? '<form class="pv__search" data-pvask role="search">' + inner + '</form>' : '<div class="pv__search">' + inner + '</div>';
};
// o.edit: section chrome and inline text; o.sel: selected section; o.ask: a visitor's question (preview only)
function pvSite(list, art, o) {
  o = o || {}; const E = !!o.edit, sel = o.sel, H = ST.hc, M = H.modules, live = !E;
  const mic = '<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="9" y="3" width="6" height="11" rx="3"/><path d="M5 11a7 7 0 0 0 14 0M12 18v3"/></svg>';
  const ls = LANGS.filter(([k]) => H.langs[k]), lh = LOGO_H[H.logoSize] || 30;
  const logo = H.logo ? '<img src="' + H.logo.src + '" alt="Oslo" style="height:' + lh + 'px">' : '<b style="font-size:' + (lh * 0.8 / 16).toFixed(2) + 'rem">Oslo</b><small>PET INSURANCE</small>';
  const IC = (d) => '<svg viewBox="0 0 24 24" aria-hidden="true">' + d + '</svg>';
  const order = hcOrder();
  const inl = (k, txt, bk, max) => E && sel === bk ? '<span class="inl" data-inl="' + k + '" contenteditable="true" spellcheck="true" role="textbox" aria-label="' + esc(VE_SEC[bk][0]) + ': edit text" data-max="' + (max || 60) + '">' + esc(txt) + '</span>' : esc(txt);
  const blk = (k, html) => {
    if (VE_MOV.includes(k) && hcHid(k)) return E ? '<div class="blk--hid">' + VI(EYE_OFF) + '<span>' + VE_SEC[k][0] + ' is hidden from visitors</span><button type="button" class="btn btn--secondary btn--sm" data-veshow="' + k + '">Show</button></div>' : '';
    if (!E) return html;
    const i = order.indexOf(k), on = sel === k;
    const tools = on && i >= 0 ? '<span class="blk__tools" role="toolbar" aria-label="' + VE_SEC[k][0] + '"><button type="button" data-vemv="-1" aria-label="Move up"' + (i === 0 ? ' disabled' : '') + '>' + VI('<path d="M12 19V5M6 11l6-6 6 6"/>') + '</button><button type="button" data-vemv="1" aria-label="Move down"' + (i === order.length - 1 ? ' disabled' : '') + '>' + VI('<path d="M12 5v14M6 13l6 6 6-6"/>') + '</button><i></i><button type="button" data-vehide="' + k + '">' + VI(EYE_OFF) + 'Hide</button></span>' : '';
    return '<div class="blk' + (on ? ' is-sel' : '') + '" data-blk="' + k + '"><span class="blk__tag">' + VE_SEC[k][0] + '</span>' + tools + html + '</div>';
  };
  let b = '<div class="pv__site' + (H.font === 'sans' ? ' is-sans' : '') + '" style="--hc:' + H.color + ';--hbg:' + hcBg() + ';--hr:' + (HC_RAD[H.corners] || HC_RAD.soft) + ';--hpill:' + (H.corners === 'square' ? '6px' : '999px') + ';--hfont:' + (HC_FONT[H.font] || HC_FONT.serif) + '">';
  b += blk('header', '<header class="pv__top"><span class="pv__logo"' + (live ? ' data-pvhome role="link" tabindex="0"' : '') + ' title="Goes to ' + esc(H.logoLink ? 'https://' + H.logoLink : 'the Help Center home') + '">' + logo + '</span>' +
    '<nav class="pv__nav" aria-label="Site"><span class="is-on">Help Center</span>' + H.nav.filter(n => n.t).map(n => '<span title="' + esc(n.u ? 'https://' + n.u : '') + '">' + esc(n.t) + '</span>').join('') + '</nav><span class="spacer"></span>' +
    (H.langSwitch && ls.length > 1 ? '<span class="pv__lang">' + IC('<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c3 3.2 3 14.8 0 18M12 3c-3 3.2-3 14.8 0 18"/>') + ls.map(([k]) => ({ en: 'EN', ar: 'عربي', fr: 'FR' })[k]).join(' | ') + '</span>' : '') +
    (H.btn.t ? '<em class="pv__btn" title="' + esc(H.btn.u ? 'https://' + H.btn.u : '') + '">' + esc(H.btn.t) + '</em>' : '') + '</header>');
  if (o.ask != null) {
    b += pvAsk(list, o.ask, H, M, mic, IC);
  } else if (art) {
    const pub = list.some(y => y.r.id === art.r.id), rel = list.filter(y => y.r.id !== art.r.id && pTopic(y) === pTopic(art)).slice(0, 3);
    b += blk('article', '<article class="pv__art"><button class="pv__crumb" type="button" data-pvhome>← Help Center · ' + esc(tName(pTopic(art))) + '</button><h2>' + esc(pTitle(art)) + '</h2>' +
      (H.showVal !== false ? '<p class="pv__val">✓ Checked by Oslo’s team' + (art.d.at ? ' · Updated ' + esc(art.d.at) : '') + '</p>' : '') +
      (pub ? '' : '<p class="pv__hidden">Only your team can see this answer</p>') +
      (M.videos && hcVid(art) ? '<div class="pv__player" role="img" aria-label="Video: ' + esc(hcVid(art).title || art.q) + '"><small>' + esc(hcVid(art).title || art.q) + (hcVid(art).src === 'Upload' ? '' : ' · ' + esc(hcVid(art).src)) + '</small></div>' : '') +
      '<div class="ansbody">' + md(pBody(art)) + '</div>' + (pg(art).cta ? '<span class="pv__go">' + esc(pg(art).cta) + ' →</span>' : '') +
      (H.showFb !== false ? '<div class="pv__fb">Was this helpful? <span>' + IC('<path d="M7 10v11H3V10zM7 10l4-7a2 2 0 0 1 3 2l-1 4h6a2 2 0 0 1 2 2.3l-1.3 7A2 2 0 0 1 17.7 21H7"/>') + 'Yes</span><span>' + IC('<path d="M17 14V3h4v11zM17 14l-4 7a2 2 0 0 1-3-2l1-4H5a2 2 0 0 1-2-2.3l1.3-7A2 2 0 0 1 6.3 3H17"/>') + 'No</span>' + (M.ai ? '<em>✦ Ask AI about this</em>' : '') + '</div>' : '') +
      (H.showRel !== false && rel.length ? '<div class="pv__rel"><h3>More in ' + esc(tName(pTopic(art))) + '</h3><ul class="pv__trend">' + rel.map(x => '<li><button type="button" data-pvq="' + x.r.id + '"><span>' + esc(pTitle(x)) + '</span><i aria-hidden="true">›</i></button></li>').join('') + '</ul></div>' : '') + '</article>');
  } else {
    const hot = list.slice().sort((a, b) => asks(b) - asks(a));
    b += blk('hero', '<section class="pv__hero' + (H.heroAlign === 'left' ? ' is-left' : '') + '"><h2>' + (H.wave ? '<span class="pv__wave" aria-hidden="true">👋</span>' : '') + inl('hero', H.hero || HERO0, 'hero', 60) + '</h2><p>' + inl('sub', H.sub || SUB0, 'hero', 90) + '</p>' +
      (M.search || M.ai ? pvSearch(H, M, mic, IC, live) : '') +
      (M.voice ? '<span class="pv__talk">' + IC('<path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2"/>') + 'Prefer to talk? Leave a voice note</span>' : '') + '</section>');
    if (!list.length) b += '<p class="pv__empty">No public answers yet. Make some public to fill the page.</p>';
    else {
      const S = {
        popular: () => '<div class="pv__pop">' + inl('popT', H.popT || 'Popular:', 'popular', 30) + hot.slice(0, 4).map(x => '<button type="button" data-pvq="' + x.r.id + '" title="' + esc(pTitle(x)) + '">' + esc(pTitle(x)) + '</button>').join('') + '</div>',
        topics: () => { const g = groups(list), cnt = H.counts !== false;
          return '<section><div class="pv__sh"><h3>' + inl('topicsT', H.topicsT || 'Browse by topic', 'topics', 40) + '</h3></div>' + (H.topicLayout === 'list'
            ? '<div class="pv__tlist">' + g.map(([t, xs]) => '<div><h4>' + esc(tName(t)) + (cnt ? ' <small>' + xs.length + '</small>' : '') + '</h4><ul>' + xs.slice(0, 4).map(x => '<li><button type="button" data-pvq="' + x.r.id + '">' + esc(pTitle(x)) + '</button></li>').join('') + '</ul></div>').join('') + '</div>'
            : '<div class="pv__topics">' + g.map(([t, xs]) => { const u = TOPIC_UI[t] || TOPIC_UI.General; return '<button type="button" data-pvq="' + xs[0].r.id + '"><i>' + IC(u[1]) + '</i><span><b>' + esc(tName(t)) + '</b><span>' + esc(tDesc(t)) + (cnt ? ' · ' + xs.length : '') + '</span></span></button>'; }).join('') + '</div>') + '</section>'; },
        trending: () => '<div class="pv__low"><section><div class="pv__sh"><h3>' + inl('trendT', H.trendT || 'Trending this week', 'trending', 40) + '</h3></div><ul class="pv__trend">' +
          hot.slice(0, H.trendN || 4).map(x => '<li><button type="button" data-pvq="' + x.r.id + '">' + (M.videos && hcVid(x) ? '<small>VIDEO</small>' : '') + '<span>' + esc(pTitle(x)) + '</span><i aria-hidden="true">›</i></button></li>').join('') + '</ul></section></div>',
        videos: () => { const vids = list.filter(hcVid);
          if (!M.videos || !vids.length) return E ? '<p class="blk__ph">' + (M.videos ? 'No videos yet. Select this section to add one to an answer.' : 'Short videos are off. Turn them on in Site style.') + ' Visitors don’t see this.</p>' : '';
          return '<section><div class="pv__sh"><h3>' + inl('vidT', H.vidT || 'Watch in 1 minute', 'videos', 40) + '</h3></div><div class="pv__vids">' + vids.slice(0, 4).map(x => '<button type="button" data-pvq="' + x.r.id + '"><i aria-hidden="true"></i><b>' + esc(hcVid(x).title || pTitle(x)) + '</b><span>' + (hcVid(x).src === 'Upload' ? 'Video' : esc(hcVid(x).src)) + '</span></button>').join('') + '</div></section>'; },
        help: () => { const hs = HELP_OPTS.filter(([k, , , mod]) => helpOn(k, mod));
          if (!hs.length) return E ? '<p class="blk__ph">Every option is off. Select this section to turn one on.</p>' : '';
          return '<aside class="pv__help"><b>' + inl('helpT', H.helpT || 'Still need help?', 'help', 40) + '</b>' + hs.map(([k, d, ic]) => '<span>' + IC(ic) + esc((H.help[k] || {}).t || d) + '</span>').join('') + '</aside>'; },
      };
      b += '<div class="pv__main">' + order.map(k => { const h = S[k](); return h || (E && hcHid(k)) ? blk(k, h) : ''; }).join('') + '</div>';
    }
  }
  return b + blk('footer', '<footer class="pv__foot">' + esc(H.footT || '© Oslo Pet Insurance · Privacy · Terms') + '<span class="spacer"></span><span class="pv__by">Powered by <img src="assets/lojo-logo.svg" alt="" width="18" height="15"><b>lojo.ai</b></span></footer>') + '</div>';
}
// a visitor's question in the preview: answered only from public answers, or handed to the team
const HC_STOP = new Set('what when where which does have with this that your from about there their they them will would could should into than then also just only been being more most some such dont cant much many'.split(' '));
function pvMatch(list, q) {
  const ws = (q.toLowerCase().match(/[a-zà-ÿ]{4,}/g) || []).filter(w => !HC_STOP.has(w));
  return list.map(x => { const t = (pTitle(x) + ' ' + pBody(x)).toLowerCase(); return [x, ws.filter(w => t.includes(w)).length]; }).filter(s => s[1] > 0).sort((a, b) => b[1] - a[1]).slice(0, 2).map(s => s[0]);
}
function pvAsk(list, q, H, M, mic, IC) {
  const top = pvMatch(list, q);
  let h = '<section class="pv__ask"><button class="pv__crumb" type="button" data-pvhome>← Help Center</button><h2>“' + esc(q) + '”</h2>';
  if (top.length && M.ai) h += '<div class="pv__ai"><b>✦ AI answer, built only from checked answers</b><p>' + esc(pSum(top[0])) + '</p><small>Based on</small><ul>' + top.map(x => '<li><button type="button" data-pvq="' + x.r.id + '">✓ ' + esc(pTitle(x)) + ' <span>· Checked by Oslo’s team</span></button></li>').join('') + '</ul></div>';
  else if (top.length) h += '<ul class="pv__trend">' + top.map(x => '<li><button type="button" data-pvq="' + x.r.id + '"><span>' + esc(pTitle(x)) + '</span><i aria-hidden="true">›</i></button></li>').join('') + '</ul>';
  else h += '<div class="pv__ai is-none">' + (pvAsk.sent ? '<p><b>Sent.</b> Someone from Oslo’s team will reply by email, usually within a few hours.</p>'
    : '<p>We don’t have a checked answer for this yet, so we won’t guess. Leave your email and someone from Oslo’s team will reply, usually within a few hours.</p><form class="pv__mail" data-pvmail><input type="email" name="em" placeholder="you@example.com" aria-label="Your email" required><button type="submit">Send to the team</button></form>') + '</div>';
  return h + pvSearch(H, M, mic, IC, true) + '</section>';
}
// ---------- the visual editor: click a section of the real page to change it
let veSel = null, veStyle = false, vePage = 'home', veDev = 'desk', veTab = 'page', veDrawer = false, vePop = false, veBusy = false, veDrag = null;
// undo and redo cover every change to the site. Approving answers is not undone here
const VE_PAST = [], VE_FUT = [], VE_SKIP = ['status', 'dirty', 'pub', 'seen', 'auto', 'init'];
let veSnap = null, veLast = 0;
const veState = () => { const o = {}; Object.keys(ST.hc).forEach(k => { if (!VE_SKIP.includes(k)) o[k] = ST.hc[k]; }); return JSON.stringify(o); };
function veCommit() {
  const cur = veState(); if (veSnap === null) { veSnap = cur; return; } if (cur === veSnap) return;
  // quick changes in a row, like typing, undo together
  if (Date.now() - veLast > 900) { VE_PAST.push(veSnap); if (VE_PAST.length > 30) VE_PAST.shift(); }
  veLast = Date.now(); VE_FUT.length = 0; veSnap = cur;
}
function hcChange() { if (ST.hc.status === 'live') ST.hc.dirty = true; veCommit(); save(); }
// a single action: its own undo step, with a toast that can undo it
function veDo(fn, msg) { veLast = 0; fn(); hcChange(); renderHc(); if (msg) veToast(msg); }
function veApply(s) { Object.assign(ST.hc, JSON.parse(s)); veSnap = s; veLast = 0; if (ST.hc.status === 'live') ST.hc.dirty = true; save(); renderHc(); }
function veUndo() { if (!VE_PAST.length) return; VE_FUT.push(veSnap); veApply(VE_PAST.pop()); toast('Undone'); }
function veRedo() { if (!VE_FUT.length) return; VE_PAST.push(veSnap); veApply(VE_FUT.pop()); toast('Redone'); }
function veToast(msg) {
  const t = $('toast'); t.classList.remove('is-err');
  t.innerHTML = '<span>' + esc(msg) + '</span><button type="button" class="toast__undo">Undo</button>'; t.classList.add('show', 'has-act');
  t.querySelector('button').onclick = () => { t.classList.remove('show'); veUndo(); };
  clearTimeout(toast.t); toast.t = setTimeout(() => t.classList.remove('show', 'has-act'), 3200);
}
function veInit() {
  const H = ST.hc;
  if (!Array.isArray(H.order)) H.order = VE_MOV.slice(); if (!Array.isArray(H.hidden)) H.hidden = [];
  // first visit: answers that look safe for customers start public; the rest wait in To check
  if (H.status === 'new' && !H.init) { approved().forEach(x => { if (!hcFlag(x)) { H.seen[x.r.id] = true; H.pub[x.r.id] = true; } }); H.init = true; save(); }
  if (!pvArt || !approved().some(x => x.r.id === pvArt)) { const l = hcPublic().sort((a, b) => asks(b) - asks(a)); pvArt = l[0] ? l[0].r.id : (approved()[0] ? approved()[0].r.id : null); }
  if (veSnap === null) veSnap = veState();
}
const veArt = () => vePage === 'article' && pvArt ? approved().find(x => x.r.id === pvArt) || null : null;
function veSelect(k) {
  veSel = k || null; veStyle = false;
  if (veSel === 'article') vePage = 'article'; else if (veSel) vePage = 'home';
  renderHc(); veReveal();
}
function veOpenArt(id) { pvArt = id; vePage = 'article'; veSel = 'article'; veStyle = false; renderHc(); const st = $('veStage'); if (st) st.scrollTop = 0; veReveal(); }
function veReveal() {
  const st = $('veStage'), b = st && st.querySelector('[data-blk="' + veSel + '"]'); if (!b) return;
  const sr = st.getBoundingClientRect(), br = b.getBoundingClientRect();
  if (br.top < sr.top + 8 || br.top > sr.bottom - 160) st.scrollTop += br.top - sr.top - 24;
  vePlace();
}

// ---------- settings rows for the inspector
const vf = (key, label, val, ph, max, hint) => '<label class="fld"><b>' + label + '</b><input class="text" data-hf="' + key + '" value="' + esc(val || '') + '" placeholder="' + esc(ph) + '" maxlength="' + max + '" autocomplete="off">' + (hint ? '<small>' + hint + '</small>' : '') + '</label>';
const vseg = (key, label, opts, cur) => '<div class="srow"><div><b>' + label + '</b></div><span class="seg" role="group" aria-label="' + label + '">' + opts.map(([v, l]) => '<button type="button" data-veset="' + key + '" data-v="' + v + '" aria-pressed="' + (String(cur) === String(v)) + '">' + l + '</button>').join('') + '</span></div>';
const vtog = (key, label, hint, on) => '<div class="srow"><div><b>' + label + '</b>' + (hint ? '<span>' + hint + '</span>' : '') + '</div><button class="sw" type="button" role="switch" aria-checked="' + !!on + '" aria-label="' + label + '" data-vetog="' + key + '"></button></div>';
const featRows = (keys) => MODS.filter(m => keys.includes(m[0])).map(([k, n, d, later]) => '<div class="srow"><div><b>' + n + (later ? '<span class="badge badge--muted">Later</span>' : '') + '</b><span>' + d + '</span></div><button class="sw" type="button" role="switch" aria-checked="' + !!ST.hc.modules[k] + '" aria-label="' + n + '" data-mod="' + k + '"' + (later ? ' disabled' : '') + '></button></div>').join('');
function colRow() {
  const H = ST.hc, custom = !HC_COLS.some(c => c[0] === H.color);
  return '<div class="srow srow--col"><div><b>Main colour</b><span>Buttons, links, icons and tints.</span></div><span class="swatches" role="radiogroup" aria-label="Main colour">' + HC_COLS.map(([c, n]) => '<button type="button" role="radio" aria-checked="' + (H.color === c) + '" aria-label="' + n + '" title="' + n + '" style="background:' + c + '" data-col="' + c + '"></button>').join('') +
    '<label class="swcustom' + (custom ? ' is-on' : '') + '" title="Your own colour"><input type="color" data-colpick value="' + esc(H.color) + '" aria-label="Your own colour"></label></span></div>';
}
const bgRow = () => '<div class="srow srow--col"><div><b>Background</b><span>Behind the heading and search.</span></div><span class="bgsw" role="radiogroup" aria-label="Background">' + HC_BGS.map(([k, n, css]) => '<button type="button" role="radio" aria-checked="' + ((ST.hc.bg || 'soft') === k) + '" data-bg="' + k + '"><i style="--hc:' + ST.hc.color + ';background:' + css + '"></i>' + n + '</button>').join('') + '</span></div>';
function langRow() {
  const H = ST.hc, CK = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 12l5 5 9-10"/></svg>', PL = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 5v14M5 12h14"/></svg>';
  return '<div class="srow srow--col"><div><b>Languages</b><span>Arabic pages read right to left. lojo drafts the translations.</span></div><span class="lchips" role="group" aria-label="Languages">' + LANGS.map(([k, n]) => k === 'en' ? '<span class="lchip is-main">' + n + ' <small>Main</small></span>' : '<button type="button" class="lchip" data-lang="' + k + '" aria-pressed="' + !!H.langs[k] + '">' + (H.langs[k] ? CK : PL) + n + '</button>').join('') + '</span></div>';
}
function addrRow() {
  const H = ST.hc, snip = '<script src="https://hc.lojo.ai/widget.js" data-workspace="oslo" async></' + 'script>';
  return '<div class="srow srow--col"><div><b>Address</b><span>Where customers find the Help Center.</span></div><div class="opts" role="radiogroup" aria-label="Address">' +
    '<label class="opt"><input type="radio" name="addr" value="sub"' + (H.addr !== 'own' ? ' checked' : '') + '><span><b>oslo.help.lojo.ai</b><span>Ready now. Nothing to set up.</span></span></label>' +
    '<label class="opt"><input type="radio" name="addr" value="own"' + (H.addr === 'own' ? ' checked' : '') + '><span><b>Your own address</b><span>Add a CNAME record that points to hc.lojo.ai. lojo adds SSL.</span>' +
      (H.addr === 'own' ? '<input class="text" id="hcDomain" value="' + esc(H.domain) + '" aria-label="Your address" placeholder="help.oslopet.com" autocomplete="off">' : '') + '</span></label></div>' +
    '<span class="vi__acts"><button class="btn btn--secondary btn--sm" type="button" data-copy="https://' + esc(hcAddr()) + '">Copy link</button><button class="btn btn--ghost btn--sm" type="button" data-copy="' + esc(snip) + '" title="A small widget for your own site">Copy embed snippet</button></span></div>';
}
function helpRows() {
  const H = ST.hc;
  return HELP_OPTS.map(([k, d, , mod]) => { const off = mod && !H.modules[mod], on = !off && (H.help[k] || {}).on !== false;
    return '<div class="hlp"><button class="sw" type="button" role="switch" aria-checked="' + on + '" aria-label="Show ' + d + '" data-help="' + k + '"' + (off ? ' disabled' : '') + '></button><input class="text" data-hf="help.' + k + '.t" value="' + esc((H.help[k] || {}).t || '') + '" placeholder="' + esc(d) + '" maxlength="30" autocomplete="off" aria-label="Label for ' + d + '"' + (on ? '' : ' disabled') + '>' + (off ? '<small>Turn on ' + (mod === 'ai' ? 'Ask AI' : 'Voice notes') + ' in Welcome &amp; search.</small>' : '') + '</div>'; }).join('');
}
const topicRows = () => groups(pvList()).map(([t, xs]) => '<div class="vi__topic"><label class="fld"><b>' + esc(t) + ' · ' + xs.length + '</b><input class="text" data-hf="t:' + esc(t) + ':title" value="' + esc((ST.hc.topics[t] || {}).title || '') + '" placeholder="' + esc(t) + '" maxlength="40" autocomplete="off" aria-label="Name for ' + esc(t) + '"></label>' +
  '<input class="text" data-hf="t:' + esc(t) + ':desc" value="' + esc((ST.hc.topics[t] || {}).desc || '') + '" placeholder="' + esc((TOPIC_UI[t] || TOPIC_UI.General)[0]) + '" maxlength="90" autocomplete="off" aria-label="Description for ' + esc(t) + '"></div>').join('') || '<span class="hed__meta">Make some answers public to see topics here.</span>';
function veFields(k) {
  const H = ST.hc, R = (s) => '<div class="rows">' + s + '</div>';
  if (k === 'header') return R(headRows());
  if (k === 'hero') return '<p class="vi__tip">Click the heading or the line under it on the page to type straight into it.</p>' + R(vtog('wave', 'Wave 👋', 'Before the heading, to say hello.', H.wave) +
    '<div class="srow srow--col">' + vf('hero', 'Heading', H.hero, HERO0, 60) + vf('sub', 'Line under it', H.sub, SUB0, 90) + vf('ph', 'Search hint', H.ph, PH0, 80, 'The grey text inside the search box.') + '</div>' +
    vseg('heroAlign', 'Align', [['center', 'Centre'], ['left', 'Left']], H.heroAlign || 'center') + bgRow() + featRows(['search', 'ai', 'voice']));
  if (k === 'popular') return R('<div class="srow srow--col">' + vf('popT', 'Label', H.popT, 'Popular:', 30) + '</div><p class="vi__note">Shows the 4 public answers visitors ask most, from Insights.</p>');
  if (k === 'topics') return R('<div class="srow srow--col">' + vf('topicsT', 'Title', H.topicsT, 'Browse by topic', 40) + '</div>' + vseg('topicLayout', 'Layout', [['grid', 'Cards'], ['list', 'List']], H.topicLayout || 'grid') +
    vtog('counts', 'Show how many answers', '', H.counts !== false) + '<div class="srow srow--col"><div><b>Topics</b><span>lojo makes them from your public answers. Rename them or change the line under each.</span></div>' + topicRows() + '</div>');
  if (k === 'trending') return R('<div class="srow srow--col">' + vf('trendT', 'Title', H.trendT, 'Trending this week', 40) + '</div>' + vseg('trendN', 'How many', [[3, '3'], [4, '4'], [5, '5']], H.trendN || 4));
  if (k === 'videos') {
    const pub = hcPublic(), sug = pub.filter(x => !hcVid(x)).sort((a, b) => asks(b) - asks(a)).slice(0, 3), has = pub.filter(hcVid);
    return R(featRows(['videos']) + '<div class="srow srow--col">' + vf('vidT', 'Title', H.vidT, 'Watch in 1 minute', 40) + '</div>' +
      '<div class="srow srow--col"><div><b>Suggested</b><span>Your most-asked answers without a video. Link from YouTube, Vimeo or Loom, or upload.</span></div>' + (sug.length ? '<ul class="sugv">' + sug.map(x => '<li><div><b>' + esc(pTitle(x)) + '</b><span>Asked ' + asks(x) + ' times a month</span></div><button class="btn btn--secondary btn--sm" type="button" data-vid="' + x.r.id + '">Add</button></li>').join('') + '</ul>' : '<span class="hed__meta">Every public answer has a video.</span>') + '</div>' +
      (has.length ? '<div class="srow srow--col"><div><b>Has a video · ' + has.length + '</b></div><ul class="sugv">' + has.map(x => '<li><div><b>' + esc(hcVid(x).title || pTitle(x)) + '</b><span>' + (hcVid(x).src === 'Upload' ? 'Uploaded file' : hcVid(x).src + ' link') + '</span></div><button class="btn btn--ghost btn--sm" type="button" data-vid="' + x.r.id + '">Change</button></li>').join('') + '</ul></div>' : ''));
  }
  if (k === 'help') return R('<div class="srow srow--col">' + vf('helpT', 'Title', H.helpT, 'Still need help?', 40) + '</div><div class="srow srow--col"><div><b>Options</b><span>Switch them off, or rename them.</span></div>' + helpRows() + '</div>' +
    '<div class="srow srow--col"><div><b>Where requests go</b><span>Your team gets the question, an AI summary and the transcript. Visitors always agree first.</span></div><label class="fld"><b>Support callbacks and email replies</b><input class="text" data-route="support" value="' + esc(H.support) + '" autocomplete="off"></label>' +
    '<label class="fld"><b>Sales callbacks</b><select class="text" data-route="sales">' + ['HubSpot · Sales', 'sales@oslopet.com', 'Off'].map(o => '<option' + (H.sales === o ? ' selected' : '') + '>' + o + '</option>').join('') + '</select></label></div>');
  if (k === 'footer') return R('<div class="srow srow--col">' + vf('footT', 'Footer text', H.footT, '© Oslo Pet Insurance · Privacy · Terms', 80) + '</div><p class="vi__note">“Powered by lojo.ai” always shows on the right.</p>');
  if (k === 'article') {
    const x = approved().find(y => y.r.id === pvArt);
    return '<h4 class="vi__g">Every answer page</h4>' + R(vtog('showVal', 'Checked by Oslo’s team', 'The line under the question.', H.showVal !== false) + vtog('showFb', 'Was this helpful?', 'Yes and No under the answer.', H.showFb !== false) + vtog('showRel', 'More in this topic', 'Up to 3 other answers.', H.showRel !== false)) +
      (x ? '<h4 class="vi__g">This answer</h4>' + hcEditor(x).replace(/<button class="hed__back"[^>]*>.*?<\/button>/, '') : '');
  }
  return '';
}
const veStyleFields = () => '<div class="rows">' + colRow() + vseg('font', 'Headings', [['serif', 'Serif'], ['sans', 'Sans']], ST.hc.font || 'serif') + vseg('corners', 'Corners', [['square', 'Square'], ['soft', 'Soft'], ['round', 'Round']], ST.hc.corners || 'soft') + langRow() + addrRow() + '</div>';

// ---------- the top bar: status, what to check, preview and publish
function drawActs() {
  const H = ST.hc, chk = hcCheck().length, pub = hcPublic(), tps = groups(pub).length, live = H.status === 'live';
  const st = veBusy ? ['muted', 'Publishing'] : live ? (H.dirty ? ['amber', 'Unpublished changes'] : ['ok', 'Live']) : H.status === 'off' ? ['muted', 'Off'] : ['muted', 'Not published'];
  const lbl = veBusy ? '<span class="ve__spin" aria-hidden="true"></span>Publishing' : live ? (H.dirty ? 'Publish changes' : 'Published') : H.status === 'off' ? 'Turned off' : 'Publish';
  let pop = '';
  if (vePop) {
    const rows = '<dl class="sum"><div><dt>Answers</dt><dd>' + pub.length + ' in ' + tps + ' topic' + (tps === 1 ? '' : 's') + '</dd></div><div><dt>Address</dt><dd>' + esc(hcAddr()) + '</dd></div><div><dt>Languages</dt><dd>' + hcLangs() + '</dd></div></dl>';
    const wait = chk ? '<p class="ve__wait">' + chk + ' answer' + (chk === 1 ? '' : 's') + ' still need you to check ' + (chk === 1 ? 'it' : 'them') + '. ' + (chk === 1 ? 'It stays' : 'They stay') + ' hidden until approved. <button type="button" data-vedrawer>Check now →</button></p>' : '';
    pop = '<div class="ve__pop" role="dialog" aria-label="Publish">' + (live
      ? '<p class="ve__live">' + VI('<path d="M5 12l5 5 9-10"/>') + 'Your Help Center is live</p><a class="ve__addr" href="#" data-copy="https://' + esc(hcAddr()) + '">' + esc(hcAddr()) + VI('<path d="M14 4h6v6M20 4l-9 9M18 14v6H4V6h6"/>') + '</a>' +
        (H.dirty ? '<p class="ve__pt">You have changes that aren’t online yet.</p>' + wait + '<button class="btn btn--primary ve__wide" type="button" data-vego>Publish changes</button>' : wait) +
        '<button class="btn btn--ghost btn--sm ve__off" type="button" data-master>Turn off the Help Center</button>'
      : H.status === 'off' ? '<p class="ve__pt"><b>The Help Center is off.</b> Pages are offline and widgets are hidden. Your settings are kept.</p><button class="btn btn--primary ve__wide" type="button" data-master>Turn back on</button>'
      : '<p class="ve__pt"><b>Ready to go live?</b></p>' + rows + wait + '<button class="btn btn--primary ve__wide" type="button" data-vego' + (pub.length ? '' : ' disabled') + '>Publish to ' + esc(hcAddr()) + '</button>' + (pub.length ? '' : '<p class="ve__pt">Make at least one answer public first.</p>')) + '</div>';
  }
  $('hcActs').innerHTML = '<span class="badge badge--' + st[0] + ' ve__st">' + st[1] + '</span>' +
    (chk ? '<button class="ve__chk" type="button" data-vedrawer>' + VI('<path d="M12 9v4M12 17h.01"/><path d="M10.3 3.9L2 18a2 2 0 0 0 1.7 3h16.6a2 2 0 0 0 1.7-3L13.7 3.9a2 2 0 0 0-3.4 0z"/>') + chk + '<span> to check</span></button>' : '') +
    '<button class="btn btn--secondary ve__pvb" type="button" data-pv>Preview as visitor</button>' +
    '<span class="ve__pubw"><button class="btn btn--primary" type="button" data-vepop aria-expanded="' + vePop + '"' + (veBusy ? ' disabled' : '') + '>' + lbl + VI('<path d="M6 9l6 6 6-6"/>') + '</button>' + pop + '</span>';
}

// ---------- the editor
function veOutline() {
  const H = ST.hc, chk = hcCheck(), GRIP = VI('<circle cx="9" cy="6" r="1"/><circle cx="15" cy="6" r="1"/><circle cx="9" cy="12" r="1"/><circle cx="15" cy="12" r="1"/><circle cx="9" cy="18" r="1"/><circle cx="15" cy="18" r="1"/>'), LOCK = VI('<rect x="5" y="11" width="14" height="10" rx="2"/><path d="M8 11V7a4 4 0 0 1 8 0v4"/>');
  const fixed = (k) => '<li class="ve__or' + (veSel === k ? ' is-sel' : '') + '"><button type="button" class="ve__orb" data-vesel="' + k + '" aria-current="' + (veSel === k) + '">' + LOCK + '<span><b>' + VE_SEC[k][0] + '</b><small>' + VE_SEC[k][1] + '</small></span></button></li>';
  const mov = (k) => { const hid = hcHid(k); return '<li class="ve__or is-mov' + (veSel === k ? ' is-sel' : '') + (hid ? ' is-hid' : '') + '" draggable="true" data-vedrag="' + k + '"><button type="button" class="ve__orb" data-vesel="' + k + '" aria-current="' + (veSel === k) + '">' + GRIP + '<span><b>' + VE_SEC[k][0] + '</b><small>' + (hid ? 'Hidden from visitors' : VE_SEC[k][1]) + '</small></span></button>' +
    '<button type="button" class="ve__eye" ' + (hid ? 'data-veshow' : 'data-vehide') + '="' + k + '" aria-label="' + (hid ? 'Show ' : 'Hide ') + VE_SEC[k][0] + '">' + VI(hid ? EYE_OFF : EYE) + '</button></li>'; };
  const tabs = '<div class="ve__otabs" role="tablist" aria-label="Outline">' + [['page', 'Page'], ['answers', 'Answers']].map(([k, l]) => '<button type="button" role="tab" aria-selected="' + (veTab === k) + '" data-veotab="' + k + '">' + l + (k === 'answers' && chk.length ? '<span class="ve__dot">' + chk.length + '</span>' : '') + '</button>').join('') + '</div>';
  let body;
  if (veTab === 'page') {
    body = '<button type="button" class="ve__sty' + (veStyle ? ' is-sel' : '') + '" data-vestyle><i style="background:' + H.color + '"></i><span><b>Site style</b><small>Colour, fonts, corners, address</small></span>' + VI('<path d="M14 4l6 6-9 9H5v-6z"/>') + '</button>' +
      '<h4 class="ve__og">Home page</h4><ul class="ve__ol" id="veOl">' + fixed('header') + fixed('hero') + hcOrder().map(mov).join('') + fixed('footer') + '</ul>' +
      '<h4 class="ve__og">Every answer page</h4><ul class="ve__ol">' + fixed('article') + '</ul><p class="ve__oh">Drag to reorder. Hover a section to hide it. The header and welcome always stay on top.</p>';
  } else {
    const all = approved().filter(x => H.seen[x.r.id]);
    body = (chk.length ? '<button type="button" class="ve__alert" data-vedrawer>' + chk.length + ' new answer' + (chk.length === 1 ? '' : 's') + ' waiting for you to check →</button>' : '') +
      '<div class="ve__auto"><span><b>New answers go public automatically</b><small>Off is safer. lojo still holds back anything that looks internal.</small></span><button class="sw" type="button" role="switch" aria-checked="' + !!H.auto + '" aria-label="New answers go public automatically" data-auto></button></div>' +
      (all.length ? groups(all).map(([t, xs]) => '<h4 class="ve__og">' + esc(tName(t)) + '<span>' + xs.filter(x => H.pub[x.r.id]).length + ' of ' + xs.length + ' public</span></h4><ul class="ve__al">' + xs.map(x => { const on = !!H.pub[x.r.id];
        return '<li' + (vePage === 'article' && pvArt === x.r.id ? ' class="is-sel"' : '') + '><button type="button" class="ve__aq" data-veart="' + x.r.id + '">' + esc(pTitle(x)) + '</button><span class="ve__am"><small>✓ Approved' + (x.d.at ? ' · ' + esc(x.d.at) : '') + '</small><span class="seg seg--xs" role="group" aria-label="Who sees it"><button type="button" data-vis="pub" data-id="' + x.r.id + '" aria-pressed="' + on + '">Public</button><button type="button" data-vis="int" data-id="' + x.r.id + '" aria-pressed="' + !on + '">Internal</button></span></span></li>'; }).join('') + '</ul>').join('')
        : '<div class="empty"><b>Nothing approved yet.</b> <a href="build.html">Approve answers in Build</a> first.</div>');
  }
  return '<aside class="ve__out" aria-label="Outline">' + tabs + '<div class="ve__ob" id="veOb">' + body + '</div></aside>';
}
const VE_CHIPS = ['Make it feel warmer', 'Use our blue', 'Put trending above topics', 'Hide popular questions'];
function veView() {
  const H = ST.hc, art = veArt(), D = [['desk', 'Desktop', '<rect x="3" y="4" width="18" height="12" rx="2"/><path d="M8 20h8M12 16v4"/>'], ['tab', 'Tablet', '<rect x="5" y="3" width="14" height="18" rx="2"/><path d="M11 18h2"/>'], ['phone', 'Phone', '<rect x="7" y="3" width="10" height="18" rx="2"/><path d="M11 18h2"/>']];
  const tb = '<div class="ve__tb"><span class="seg" role="group" aria-label="Page">' + [['home', 'Home page'], ['article', 'Answer page']].map(([k, l]) => '<button type="button" data-vepage="' + k + '" aria-pressed="' + (vePage === k) + '">' + l + '</button>').join('') + '</span>' +
    '<span class="ve__mid"><span class="seg seg--ic" role="group" aria-label="Screen size">' + D.map(([k, l, d]) => '<button type="button" data-vedev="' + k + '" aria-pressed="' + (veDev === k) + '" aria-label="' + l + '" title="' + l + '">' + VI(d) + '</button>').join('') + '</span>' +
    '<button type="button" class="ve__ib" data-veundo aria-label="Undo" title="Undo (⌘Z)"' + (VE_PAST.length ? '' : ' disabled') + '>' + VI('<path d="M9 14L4 9l5-5"/><path d="M4 9h11a5 5 0 0 1 0 10h-3"/>') + '</button><button type="button" class="ve__ib" data-veredo aria-label="Redo" title="Redo (⇧⌘Z)"' + (VE_FUT.length ? '' : ' disabled') + '>' + VI('<path d="M15 14l5-5-5-5"/><path d="M20 9H9a5 5 0 0 0 0 10h3"/>') + '</button></span>' +
    '<button type="button" class="ve__ib ve__fs" data-vefs aria-pressed="' + document.body.classList.contains('is-fs') + '" aria-label="' + (document.body.classList.contains('is-fs') ? 'Exit full screen' : 'Full screen') + '" title="' + (document.body.classList.contains('is-fs') ? 'Exit full screen (F)' : 'Full screen (F)') + '">' + VI(document.body.classList.contains('is-fs') ? '<path d="M4 14h6v6M20 10h-6V4M14 10l7-7M3 21l7-7"/>' : '<path d="M15 3h6v6M9 21H3v-6M21 3l-7 7M3 21l7-7"/>') + '</button>' +
    '<button type="button" class="ve__stb" data-vestyle aria-pressed="' + veStyle + '"><i style="background:' + H.color + '"></i>Site style</button></div>';
  const insp = veSel ? '<div class="vi" id="veInsp" role="dialog" aria-label="' + VE_SEC[veSel][0] + ' settings"><div class="vi__h"><b>' + VE_SEC[veSel][0] + '</b><button type="button" class="ve__ib" data-vesel="" aria-label="Close settings">' + VI('<path d="M6 6l12 12M18 6L6 18"/>') + '</button></div><div class="vi__b">' + veFields(veSel) + '</div></div>' : '';
  const sty = veStyle ? '<div class="vi vi--style" id="veSty" role="dialog" aria-label="Site style"><div class="vi__h"><b>Site style</b><button type="button" class="ve__ib" data-vestyle aria-label="Close site style">' + VI('<path d="M6 6l12 12M18 6L6 18"/>') + '</button></div><div class="vi__b">' + veStyleFields() + '</div></div>' : '';
  const ai = '<form class="ve__ai" id="veAi" autocomplete="off"><div class="ve__chips" id="veChips" hidden><span id="veAiMsg">Try</span>' + VE_CHIPS.map(c => '<button type="button" data-vechip>' + c + '</button>').join('') + '</div>' +
    VI('<path d="M12 3l1.8 4.7 4.7 1.8-4.7 1.8L12 16l-1.8-4.7L5.5 9.5l4.7-1.8z"/><path d="M19 15l.8 2.2 2.2.8-2.2.8L19 21l-.8-2.2L16 18l2.2-.8z"/>') +
    '<input id="veAiIn" placeholder="Tell lojo what to change…" aria-label="Tell lojo what to change"><button type="submit" class="ve__aigo" aria-label="Send" disabled>' + VI('<path d="M12 19V5M6 11l6-6 6 6"/>') + '</button></form>';
  const chk = hcCheck();
  const dr = veDrawer ? '<div class="ve__dr"><div class="ve__drbg" data-vedrawerx></div><aside class="ve__drp" role="dialog" aria-modal="true" aria-labelledby="veDrT"><header><div><h2 id="veDrT" tabindex="-1">Check new answers</h2><p>Approved in Build, waiting for you to decide who sees them. Nothing goes public until you say so.</p></div><button type="button" class="ve__ib" data-vedrawerx aria-label="Close">' + VI('<path d="M6 6l12 12M18 6L6 18"/>') + '</button></header><div class="ve__drb">' +
    (chk.length ? chk.map(x => { const f = hcFlag(x), src = x.r.src && x.r.src[0] ? x.r.src[0][1] : '';
      return '<article class="ve__card"><p class="ve__cm">' + esc(tName(pTopic(x))) + ' · <span class="' + (f ? 'is-warn' : 'is-ok') + '">' + (f ? 'Check before making public' : 'Looks safe for customers') + '</span></p>' + (f ? '<p class="ve__flag">' + VI('<path d="M12 9v4M12 17h.01"/><circle cx="12" cy="12" r="9"/>') + f + '. It may be for your team only.</p>' : '') +
        '<h3>' + esc(pTitle(x)) + '</h3><div class="ve__ans ansbody">' + md(pBody(x)) + '</div>' + (src ? '<p class="ve__src">' + VI('<path d="M7 3h8l4 4v14H7z"/><path d="M15 3v4h4"/>') + 'From ' + esc(src) + '</p>' : '') +
        '<div class="ve__ca"><button class="btn btn--primary btn--sm" type="button" data-mkpub="' + x.r.id + '">' + VI('<path d="M5 12l5 5 9-10"/>') + 'Make public</button><button class="btn btn--secondary btn--sm" type="button" data-keep="' + x.r.id + '">Team only</button><span class="spacer"></span><button class="btn btn--ghost btn--sm" type="button" data-veart="' + x.r.id + '">Open page</button></div></article>'; }).join('')
      : '<div class="ve__done">' + VI('<circle cx="12" cy="12" r="9"/><path d="M8 12l3 3 5-6"/>') + '<b>All caught up</b><p>New answers show up here when someone approves them in Build.</p><button class="btn btn--secondary" type="button" data-vedrawerx>Back to the page</button></div>') + '</div></aside></div>' : '';
  return '<div class="ve" id="ve">' + veOutline() + '<div class="ve__main">' + tb + '<div class="ve__stage' + (veSel ? ' has-insp' : '') + '" id="veStage"><div class="ve__page is-' + veDev + '" id="vePage">' + pvSite(pvList(), art, { edit: true, sel: veSel }) + '</div>' + insp + '</div>' + sty + ai + '</div></div>' + dr;
}
function renderHc() {
  hcSync(); veInit();
  hcEdit = veSel === 'article' ? pvArt : null;
  const st = $('veStage'), sTop = st ? st.scrollTop : 0, ib = document.querySelector('#veInsp .vi__b, #veSty .vi__b'), iTop = ib ? ib.scrollTop : 0, ob = $('veOb'), oTop = ob ? ob.scrollTop : 0;
  drawActs();
  $('tabHc').innerHTML = veView();
  document.body.classList.add('ve-on');
  if ($('veStage')) $('veStage').scrollTop = sTop; const ib2 = document.querySelector('#veInsp .vi__b, #veSty .vi__b'); if (ib2) ib2.scrollTop = iTop; if ($('veOb')) $('veOb').scrollTop = oTop;
  fitPane();
}
// after typing: redraw only the page, so the field keeps focus
function drawPane() {
  const p = $('vePage'); if (!p) return;
  p.innerHTML = pvSite(pvList(), veArt(), { edit: true, sel: veSel }); drawActs();
  const u = document.querySelector('[data-veundo]'); if (u) u.disabled = !VE_PAST.length; const r = document.querySelector('[data-veredo]'); if (r) r.disabled = !VE_FUT.length;
  vePlace();
}
// the editor fills the screen under the header; settings sit beside the section they change
function fitPane() {
  const v = $('ve'); if (!v) return;
  v.style.height = Math.max(560, window.innerHeight - v.getBoundingClientRect().top - 20) + 'px';
  vePlace();
}
function vePlace() {
  const ins = $('veInsp'), st = $('veStage'); if (!ins || !st) return;
  const b = st.querySelector('[data-blk="' + veSel + '"]'), pgEl = $('vePage'); if (!b) { ins.hidden = true; return; } ins.hidden = false;
  const sr = st.getBoundingClientRect(), br = b.getBoundingClientRect(), pr = pgEl.getBoundingClientRect(), w = ins.offsetWidth;
  let top = br.top - sr.top + st.scrollTop + (VE_MOV.includes(veSel) ? 46 : 10);
  if (veSel === 'footer') top = Math.max(8, br.top - sr.top + st.scrollTop - ins.offsetHeight - 10);
  const outside = pr.right - sr.left + 16;
  const left = outside + w <= st.clientWidth - 8 ? outside : Math.max(8, Math.min(br.right, sr.right) - sr.left - w - 14);
  ins.style.top = top + 'px'; ins.style.left = left + 'px';
}

// ---------- plain-language changes: "put trending above topics", "use our blue"
const VE_COLW = [[/\bocean|navy\b/, 'Ocean'], [/\bblue\b/, 'Blue'], [/\bindigo\b/, 'Indigo'], [/\bpurple|violet|plum\b/, 'Violet'], [/\brose|pink\b/, 'Rose'], [/\borange|coral|red|rust\b/, 'Coral'], [/\bamber|yellow|gold\b/, 'Amber'], [/\bgreen|forest\b/, 'Green'], [/\bteal\b/, 'Teal'], [/\bdark|black|ink|grey|gray|graphite\b/, 'Ink']];
function veAsk(text) {
  const s = text.toLowerCase(), H = ST.hc;
  const found = [[/popular/, 'popular'], [/topic/, 'topics'], [/trend/, 'trending'], [/video/, 'videos'], [/hand|contact|talk|need help|help strip|still need/, 'help']].map(([re, k]) => [s.search(re), k]).filter(m => m[0] >= 0).sort((a, b) => a[0] - b[0]).map(m => m[1]);
  const A = found[0], B = found[1];
  if (A && /\b(hide|remove|drop)\b/.test(s)) return { fn: () => { if (!hcHid(A)) H.hidden.push(A); }, msg: 'Hid ' + VE_SEC[A][0] };
  if (A && /\b(show|bring back|unhide)\b/.test(s)) return { fn: () => { H.hidden = H.hidden.filter(k => k !== A); }, msg: 'Showing ' + VE_SEC[A][0], sel: A };
  if (A && /\b(above|before|first|top|up)\b/.test(s)) return { fn: () => { const o = hcOrder().filter(k => k !== A), i = B ? o.indexOf(B) : 0; o.splice(Math.max(0, i), 0, A); H.order = o; }, msg: 'Moved ' + VE_SEC[A][0] + ' up', sel: A };
  if (A && /\b(below|after|last|bottom|down)\b/.test(s)) return { fn: () => { const o = hcOrder().filter(k => k !== A), i = B ? o.indexOf(B) + 1 : o.length; o.splice(i, 0, A); H.order = o; }, msg: 'Moved ' + VE_SEC[A][0] + ' down', sel: A };
  if (/warm|friendl|casual|playful/.test(s)) return { fn: () => { H.hero = 'Hi there, what can we help with?'; H.sub = 'Real answers, checked by Oslo’s team and our in-house vet.'; H.corners = 'round'; H.wave = true; }, msg: 'Friendlier welcome and rounder corners', sel: 'hero' };
  if (/formal|serious|professional/.test(s)) return { fn: () => { H.hero = 'Help Center'; H.font = 'sans'; H.corners = 'square'; H.wave = false; }, msg: 'More formal heading and style', sel: 'hero' };
  const bg = HC_BGS.find(([k, n]) => k !== 'soft' && new RegExp('\\b' + n.toLowerCase() + '\\b').test(s));
  if (bg && /gradient|background|\b(mint|peach|lilac|sunrise)\b/.test(s)) return { fn: () => { H.bg = bg[0]; }, msg: 'Background is now ' + bg[1], sel: 'hero' };
  const col = VE_COLW.find(([re]) => re.test(s));
  if (col) { const c = HC_COLS.find(x => x[1] === col[1]); return { fn: () => { H.color = c[0]; }, msg: 'Main colour is now ' + c[1], style: true }; }
  if (/\bleft\b/.test(s)) return { fn: () => { H.heroAlign = 'left'; }, msg: 'Welcome is now left-aligned', sel: 'hero' };
  if (/\bcent(er|re)\b/.test(s)) return { fn: () => { H.heroAlign = 'center'; }, msg: 'Welcome is now centred', sel: 'hero' };
  if (/\blist\b/.test(s)) return { fn: () => { H.topicLayout = 'list'; }, msg: 'Topics show as a list', sel: 'topics' };
  if (/\b(grid|cards)\b/.test(s)) return { fn: () => { H.topicLayout = 'grid'; }, msg: 'Topics show as cards', sel: 'topics' };
  if (/\bsans\b/.test(s)) return { fn: () => { H.font = 'sans'; }, msg: 'Headings use a sans font', style: true };
  if (/\bserif\b/.test(s)) return { fn: () => { H.font = 'serif'; }, msg: 'Headings use a serif font', style: true };
  if (/\bround/.test(s)) return { fn: () => { H.corners = 'round'; }, msg: 'Rounder corners', style: true };
  if (/\bsquare|sharp/.test(s)) return { fn: () => { H.corners = 'square'; }, msg: 'Square corners', style: true };
  return null;
}
function veRun(text) {
  const r = veAsk(text);
  if (!r) { const m = $('veAiMsg'), c = $('veChips'); if (m) m.textContent = 'I can’t do that one yet. Try:'; if (c) c.hidden = false; return false; }
  veLast = 0; r.fn(); hcChange();
  if (r.style) { veSel = null; veStyle = true; } else if (r.sel) { veSel = r.sel; veStyle = false; if (r.sel !== 'article') vePage = 'home'; }
  renderHc(); veReveal(); veToast(r.msg); return true;
}
// one answer's page: the parts the Help Center owns, and the answer it shows
function hcEditor(x) {
  const P = pg(x), cv = cvOf(x), v = hcVid(x), id = x.r.id;
  const topics = [...new Set(HC_TOPICS.map(t => t[0]).concat('General'))];
  let h = '<div class="hed"><button class="hed__back" type="button" data-hedone>← Answers</button>' +
    '<section class="card hcc"><div class="hcc__h"><h2>Page</h2><span class="sub">Only how it shows on the Help Center.</span></div>' +
    '<label class="fld"><b>Page title</b><input class="text" data-pf="title" value="' + esc(P.title || '') + '" placeholder="' + esc(x.q) + '" autocomplete="off"><small>How customers read the question. Leave empty to use the approved wording.</small></label>' +
    '<label class="fld"><b>Topic</b><select class="text" data-pf="topic"><option value="">Automatic (' + esc(topicOf(x.q)) + ')</option>' + topics.map(t => '<option' + (P.topic === t ? ' selected' : '') + '>' + esc(t) + '</option>').join('') + '</select></label>' +
    '<label class="fld"><b>Short answer</b><textarea class="text" data-pf="sum" rows="3" placeholder="' + esc(brief(pBody(x))) + '">' + esc(P.sum || '') + '</textarea><small>Shown in the AI answer card when this is the best match. Leave empty and lojo uses the first lines of the answer.</small></label>' +
    '<div class="hed__2"><label class="fld"><b>Button text</b><input class="text" data-pf="cta" value="' + esc(P.cta || '') + '" placeholder="Get a quote for your pet" autocomplete="off"></label>' +
    '<label class="fld"><b>Button link</b><input class="text" data-pf="ctaUrl" value="' + esc(P.ctaUrl || '') + '" placeholder="oslopet.com/quote" autocomplete="off" spellcheck="false"></label></div>' +
    '<small class="hed__meta">The button shows under the answer. Leave the text empty for no button.</small></section>';
  h += '<section class="card hcc"><div class="hcc__h"><h2>Video</h2></div><div class="srow" style="border:0;padding:0"><div><b>' + (v ? esc(v.title || pTitle(x)) : 'No video') + '</b><span>' + (v ? (v.src === 'Upload' ? 'Uploaded file' : v.src + ' link') : 'Asked ' + asks(x) + ' times a month.') + '</span></div><span class="spacer"></span><button class="btn btn--secondary btn--sm" type="button" data-vid="' + id + '">' + (v ? 'Change' : 'Add video') + '</button></div></section>';
  h += '<section class="card hcc"><div class="hcc__h"><h2>Answer</h2><span class="sub">Approved in Build. Ask lojo and the API use it too.</span></div>' +
    '<div class="hed__ans"><div class="ansbody">' + md(x.a) + '</div></div><span class="hed__meta">Approved' + (x.d.at ? ' · ' + esc(x.d.at) : '') + '</span>' +
    '<div class="hed__acts"><a class="btn btn--secondary btn--sm" href="build.html?sel=' + id + '&edit=1">Edit answer in Build</a>' + (cv ? '' : '<button class="btn btn--ghost btn--sm" type="button" data-cvnew>✦ Write a customer version</button>') + '</div>';
  if (cv) {
    const st = cvStale(x) ? ['amber', 'Out of date'] : cv.status === 'ok' ? ['ok', 'Approved'] : ['amber', 'Needs approval'];
    h += '<div class="hed__cv"><h3>Customer version <span class="badge badge--' + st[0] + '">' + st[1] + '</span></h3>' +
      '<p>Only the Help Center shows this. Ask lojo and the API keep the approved answer.</p>' +
      (cvStale(x) ? '<div class="hed__stale">The approved answer changed since this was written. Check it still says the same thing.</div>' : '') +
      (cv.status === 'ok' && !cvStale(x) ? '<div class="hed__ans"><div class="ansbody">' + md(cv.text) + '</div></div><div class="hed__acts"><button class="btn btn--secondary btn--sm" type="button" data-cvedit>Edit</button><button class="btn btn--ghost btn--sm" type="button" data-cvx>Remove</button></div>'
        : '<textarea class="text" data-cv rows="5" aria-label="Customer version">' + esc(cv.text) + '</textarea>' +
          '<div class="hed__acts"><button class="btn btn--primary btn--sm" type="button" data-cvok>Approve</button>' + (cvStale(x) ? '<button class="btn btn--secondary btn--sm" type="button" data-cvnew>Redraft from the new answer</button>' : '') + '<button class="btn btn--ghost btn--sm" type="button" data-cvx>' + (cv.status === 'ok' ? 'Remove' : 'Discard') + '</button></div>') + '</div>';
  }
  return h + '</section></div>';
}
// add or edit an answer's video: paste a link, or upload a file
function hcVideo(id, opener) {
  const x = approved().find(y => y.r.id === id); if (!x) return;
  const H = ST.hc, cur = H.videos[id];
  let d = $('vidDlg');
  if (!d) { d = document.createElement('dialog'); d.id = 'vidDlg'; d.className = 'dlg vdlg'; d.setAttribute('aria-labelledby', 'vidT'); document.body.appendChild(d); }
  let mode = cur && cur.src === 'Upload' ? 'file' : 'link', file = cur && cur.src === 'Upload' ? { name: cur.name, size: cur.size } : null;
  const mb = (n) => n > 1048576 ? (n / 1048576).toFixed(1) + ' MB' : Math.max(1, Math.round(n / 1024)) + ' KB';
  const draw = () => {
    d.innerHTML = '<form method="dialog" novalidate><div class="dlg__b"><h3 id="vidT">' + (cur ? 'Edit video' : 'Add a video') + '</h3><p>For “' + esc(x.q) + '”. It shows on the answer’s page and in “Watch in 1 minute”.</p>' +
      '<span class="seg" role="group" aria-label="Where the video is">' + [['link', 'Paste a link'], ['file', 'Upload a file']].map(([k, l]) => '<button type="button" data-vm="' + k + '" aria-pressed="' + (mode === k) + '">' + l + '</button>').join('') + '</span>' +
      (mode === 'link'
        ? '<label class="fld"><b>Video link</b><input class="text" id="vidUrl" type="url" placeholder="https://youtu.be/…" value="' + esc(cur && cur.url || '') + '" autocomplete="off" spellcheck="false" aria-describedby="vidHint"><span class="vdlg__hint" id="vidHint" aria-live="polite">YouTube, Vimeo or Loom. Unlisted videos work too.</span></label>'
        : '<div class="vdrop" data-vdrop><div>' + (file ? '<b>' + esc(file.name) + '</b><span>' + mb(file.size) + '</span>' : '<b>Drop a video here</b><span>MP4, MOV or WebM, up to 500 MB.</span>') + '</div><button class="btn btn--secondary btn--sm" type="button" data-vpick>' + (file ? 'Replace' : 'Choose file') + '</button><input type="file" id="vidFile" accept="video/mp4,video/quicktime,video/webm" hidden></div>') +
      '<label class="fld"><b>Title</b><input class="text" id="vidTitle" value="' + esc(cur ? cur.title : x.q) + '" autocomplete="off"></label></div>' +
      '<div class="dlg__f vdlg__f">' + (cur ? '<button class="btn btn--ghost" type="button" data-vrm>Remove video</button>' : '') + '<span class="spacer"></span><button class="btn btn--secondary" type="button" data-vx>Cancel</button><button class="btn btn--primary" type="submit" data-vok>' + (cur ? 'Save' : 'Add video') + '</button></div></form>';
  };
  const hint = (msg, cls) => { const h = $('vidHint'); if (h) { h.textContent = msg; h.className = 'vdlg__hint' + (cls ? ' ' + cls : ''); } };
  const takeFile = (f) => {
    if (!/^video\/(mp4|quicktime|webm)$/.test(f.type)) { toastError('Use an MP4, MOV or WebM file.'); return; }
    if (f.size > 500 * 1048576) { toastError('That file is ' + mb(f.size) + '. Use one under 500 MB.'); return; }
    file = { name: f.name, size: f.size }; const t = $('vidTitle').value; draw(); $('vidTitle').value = t; d.querySelector('[data-vpick]').focus();
  };
  const done = (msg) => { hcChange(); d.close(); renderHc(); drawPane(); toast(msg); };
  d.onclick = (e) => {
    if (e.target === d || e.target.closest('[data-vx]')) { d.close(); return; }
    const m = e.target.closest('[data-vm]'); if (m) { const t = $('vidTitle').value; mode = m.dataset.vm; draw(); $('vidTitle').value = t; d.querySelector('[data-vm="' + mode + '"]').focus(); return; }
    if (e.target.closest('[data-vpick]')) { $('vidFile').click(); return; }
    if (e.target.closest('[data-vrm]')) { delete H.videos[id]; done('Video removed'); }
  };
  d.onchange = (e) => { if (e.target.id === 'vidFile' && e.target.files[0]) takeFile(e.target.files[0]); };
  d.oninput = (e) => { if (e.target.id === 'vidUrl') { const v = e.target.value.trim(), p = vProv(v); hint(!v ? 'YouTube, Vimeo or Loom. Unlisted videos work too.' : p ? '✓ ' + p + ' video' : 'Not a YouTube, Vimeo or Loom video link yet.', v ? (p ? 'is-ok' : '') : ''); } };
  d.ondragover = (e) => { const z = e.target.closest('[data-vdrop]'); if (z) { e.preventDefault(); z.classList.add('is-over'); } };
  d.ondragleave = (e) => { const z = e.target.closest('[data-vdrop]'); if (z && !z.contains(e.relatedTarget)) z.classList.remove('is-over'); };
  d.ondrop = (e) => { const z = e.target.closest('[data-vdrop]'); if (!z) return; e.preventDefault(); z.classList.remove('is-over'); if (e.dataTransfer.files[0]) takeFile(e.dataTransfer.files[0]); };
  d.onsubmit = (e) => {
    e.preventDefault();
    const title = $('vidTitle').value.trim() || x.q;
    if (mode === 'link') {
      const u = $('vidUrl').value.trim(), p = vProv(u);
      if (!p) { hint(u ? 'Use a YouTube, Vimeo or Loom video link.' : 'Paste a video link.', 'is-err'); $('vidUrl').focus(); return; }
      H.videos[id] = { src: p, url: /^https?:/i.test(u) ? u : 'https://' + u, title };
    } else {
      if (!file) { toastError('Choose a video file first.'); d.querySelector('[data-vpick]').focus(); return; }
      H.videos[id] = { src: 'Upload', name: file.name, size: file.size, title };
    }
    done(cur ? 'Video saved' : 'Video added' + (H.status === 'live' ? '. It goes online when you publish.' : ''));
  };
  d.onclose = () => { const o = document.querySelector('#vSub [data-vid="' + id + '"]') || opener; if (o && o.isConnected) o.focus(); };
  draw(); d.showModal(); const f = $('vidUrl') || d.querySelector('[data-vpick]'); if (f) f.focus();
}

$('vSub').addEventListener('click', async (e) => {
  const t = e.target, H = ST.hc;
  const pv = t.closest('[data-pv]'); if (pv) { hcPreview(pv); return; }
  if (t.closest('[data-master]')) {
    if (H.status === 'live') { if (!(await askConfirm('Turn off the Help Center?', 'Its pages go offline and the widgets hide. Your settings and answers stay.', 'Turn off'))) return; H.status = 'off'; }
    else { H.status = 'live'; H.dirty = false; }
    save(); keepFocus(renderHc); toast(H.status === 'live' ? 'Help Center is back online' : 'Help Center turned off'); return;
  }
  const vis = t.closest('[data-vis]');
  if (vis) { const on = vis.dataset.vis === 'pub'; if (!!H.pub[vis.dataset.id] === on) return; H.pub[vis.dataset.id] = on; hcChange(); keepFocus(renderHc); toast(on ? 'Visible on the Help Center' + (H.status === 'live' ? ' when you publish' : '') : 'Hidden. Your team still sees it in Ask lojo.'); return; }
  const mp = t.closest('[data-mkpub]'), kp = t.closest('[data-keep]');
  if (mp || kp) { const id = mp ? mp.dataset.mkpub : kp.dataset.keep; H.seen[id] = true; H.pub[id] = !!mp; hcChange(); renderHc(); toast(mp ? 'Approved. It’s on the Help Center' + (H.status === 'live' ? ' when you publish.' : '.') : 'Approved for your team only'); const n = document.querySelector('.ve__drb [data-mkpub], .ve__drb [data-vedrawerx]'); if (n) n.focus(); return; }
  if (t.closest('[data-auto]')) { H.auto = !H.auto; save(); keepFocus(renderHc); return; }
  const md_ = t.closest('[data-mod]'); if (md_) { H.modules[md_.dataset.mod] = !H.modules[md_.dataset.mod]; hcChange(); keepFocus(renderHc); return; }
  const lg = t.closest('button[data-lang]'); if (lg) { H.langs[lg.dataset.lang] = !H.langs[lg.dataset.lang]; hcChange(); keepFocus(renderHc); return; }
  const bgb = t.closest('[data-bg]'); if (bgb) { H.bg = bgb.dataset.bg; hcChange(); keepFocus(renderHc); return; }
  const hp = t.closest('[data-help]'); if (hp) { const o = H.help[hp.dataset.help] = H.help[hp.dataset.help] || {}; o.on = o.on === false; hcChange(); keepFocus(renderHc); return; }
  if (t.closest('[data-wave]')) { H.wave = !H.wave; hcChange(); keepFocus(renderHc); return; }
  const cl = t.closest('[data-col]'); if (cl) { H.color = cl.dataset.col; hcChange(); keepFocus(renderHc); return; }
  const vb = t.closest('[data-vid]'); if (vb) { hcVideo(vb.dataset.vid, vb); return; }
  if (hcEdit && t.closest('[data-cvnew],[data-cvok],[data-cvx],[data-cvedit]')) {
    const x = approved().find(y => y.r.id === hcEdit), P = H.pages[hcEdit] = H.pages[hcEdit] || {};
    if (t.closest('[data-cvnew]')) { P.cv = { text: cvDraft(x), status: 'review', base: x.a }; toast('lojo drafted a customer version. Check it, then approve.'); }
    else if (t.closest('[data-cvedit]')) P.cv.status = 'review';
    else if (t.closest('[data-cvok]')) { const ta = $('tabHc').querySelector('[data-cv]'); if (ta && !ta.value.trim()) { toastError('Write the customer version first.'); ta.focus(); return; } if (ta) P.cv.text = ta.value.trim(); P.cv.status = 'ok'; P.cv.base = x.a; toast('Customer version approved'); }
    else { delete P.cv; toast('Customer version removed. The page shows the approved answer.'); }
    hcChange(); renderHc(); const f = $('tabHc').querySelector('[data-cv]') || $('tabHc').querySelector('[data-cvedit]') || $('tabHc').querySelector('[data-cvnew]'); if (f) f.focus(); return;
  }
  if (t.closest('[data-logo]')) { $('hcLogoFile').click(); return; }
  if (t.closest('[data-logorm]')) { H.logo = null; hcChange(); renderHc(); const c = $('tabHc').querySelector('[data-logo]'); if (c) c.focus(); toast('Logo removed. The site shows your name.'); return; }
  const lz = t.closest('[data-lsize]'); if (lz) { H.logoSize = lz.dataset.lsize; hcChange(); keepFocus(renderHc); return; }
  if (t.closest('[data-lswitch]')) { H.langSwitch = !H.langSwitch; hcChange(); keepFocus(renderHc); return; }
  const cp = t.closest('#tabHc [data-copy]'); if (cp) { try { navigator.clipboard.writeText(cp.dataset.copy); } catch (err) {} toast('Copied'); }
});
$('vSub').addEventListener('change', (e) => {
  const t = e.target, H = ST.hc;
  if (t.id === 'hcLogoFile') { if (t.files[0]) readLogo(t.files[0]); return; }
  if (t.id === 'hcLogoLink') { H.logoLink = t.value.trim().replace(/^https?:\/\//i, '').replace(/\/$/, ''); t.value = H.logoLink; hcChange(); drawPane(); return; }
  if (t.name === 'addr') { H.addr = t.value; hcChange(); keepFocus(renderHc); if (t.value === 'own' && $('hcDomain')) $('hcDomain').focus(); return; }
  if (t.hasAttribute('data-colpick')) { H.color = t.value.toUpperCase(); hcChange(); keepFocus(renderHc); return; }
  if (t.dataset.route) { H[t.dataset.route] = t.value.trim(); hcChange(); keepFocus(renderHc); toast('Saved'); }
});
$('vSub').addEventListener('input', (e) => {
  if (e.target.id === 'hcDomain') { ST.hc.domain = e.target.value.trim(); hcChange(); drawPane(); }
  if (e.target.id === 'hcLogoLink') { ST.hc.logoLink = e.target.value.trim().replace(/^https?:\/\//i, ''); save(); drawPane(); }
  if (e.target.hasAttribute('data-colpick')) { ST.hc.color = e.target.value.toUpperCase(); save(); drawPane(); return; }
  const hf = e.target.dataset.hf;
  if (hf) { const v = e.target.value.trim(); if (hf.startsWith('t:')) { const [, t, k] = hf.split(':'); (ST.hc.topics[t] = ST.hc.topics[t] || {})[k] = v; } else if (hf.includes('.')) { const ks = hf.split('.'); let o = ST.hc; ks.slice(0, -1).forEach(k => { o = o[k] = o[k] || {}; }); o[ks[ks.length - 1]] = ks[ks.length - 1] === 'u' ? v.replace(/^https?:\/\//i, '') : v; } else ST.hc[hf] = v; hcChange(); drawPane(); const pb = document.querySelector('#hcActs [data-publish]'); if (pb) { pb.disabled = false; pb.removeAttribute('title'); } return; }
  const pf = e.target.dataset.pf, isCv = e.target.hasAttribute('data-cv');
  if ((pf || isCv) && hcEdit) {
    const P = ST.hc.pages[hcEdit] = ST.hc.pages[hcEdit] || {};
    if (pf) P[pf] = e.target.value.trim(); else P.cv.text = e.target.value;
    hcChange(); drawPane();
    const pb = document.querySelector('#hcActs [data-publish]'); if (pb) { pb.disabled = false; pb.removeAttribute('title'); }
  }
});
// logo upload: choose a file or drop it on the box
function readLogo(f) {
  if (!/^image\/(png|svg\+xml|jpeg|webp)$/.test(f.type)) { toastError('Use a PNG, SVG, JPG or WebP file.'); return; }
  if (f.size > 1024 * 1024) { toastError('That file is ' + kb(f.size) + '. Use one under 1 MB.'); return; }
  const r = new FileReader();
  r.onload = () => { ST.hc.logo = { src: r.result, name: f.name, size: f.size }; hcChange(); renderHc(); const c = $('tabHc').querySelector('[data-logo]'); if (c) c.focus(); toast('Logo added'); };
  r.readAsDataURL(f);
}
['dragenter', 'dragover'].forEach(ev => $('vSub').addEventListener(ev, (e) => { const z = e.target.closest('[data-lgdrop]'); if (z) { e.preventDefault(); z.classList.add('is-over'); } }));
$('vSub').addEventListener('dragleave', (e) => { const z = e.target.closest('[data-lgdrop]'); if (z && !z.contains(e.relatedTarget)) z.classList.remove('is-over'); });
$('vSub').addEventListener('drop', (e) => { const z = e.target.closest('[data-lgdrop]'); if (!z) return; e.preventDefault(); z.classList.remove('is-over'); const f = e.dataTransfer.files[0]; if (f) readLogo(f); });

window.addEventListener('resize', fitPane);
// full screen editing: F toggles it, Esc leaves when nothing else is open
function veFs(on) {
  document.body.classList.toggle('is-fs', on);
  try { sessionStorage.setItem('lojo-hc-fs', on ? '1' : ''); } catch (err) {}
  renderHc(); const b = document.querySelector('[data-vefs]'); if (b) b.focus();
}
// publishing takes a moment; the button shows it
function vePublish() {
  const H = ST.hc;
  if (H.addr === 'own' && !(H.domain || '').trim()) { vePop = false; veSel = null; veStyle = true; renderHc(); toastError('Type your address first, such as help.oslopet.com.'); if ($('hcDomain')) $('hcDomain').focus(); return; }
  const was = H.status; vePop = false; veBusy = true; drawActs();
  setTimeout(() => { veBusy = false; H.status = 'live'; H.dirty = false; save(); drawActs(); toast(was === 'live' ? 'Changes published' : 'Help Center is live at ' + hcAddr()); const b = document.querySelector('[data-vepop]'); if (b) b.focus(); }, 900);
}
function veOpenDrawer() { veDrawer = true; vePop = false; renderHc(); const h = $('veDrT'); if (h) h.focus(); }
$('hcActs').addEventListener('click', (e) => {
  const t = e.target;
  if (t.closest('[data-vepop]')) { e.stopPropagation(); vePop = !vePop; drawActs(); const f = vePop && document.querySelector('.ve__pop button:not([disabled]), .ve__pop a'); if (f) f.focus(); else if (!vePop) document.querySelector('[data-vepop]').focus(); return; }
  if (t.closest('[data-vedrawer]')) { e.stopPropagation(); veOpenDrawer(); return; }
  const cp = t.closest('[data-copy]'); if (cp) { e.preventDefault(); e.stopPropagation(); try { navigator.clipboard.writeText(cp.dataset.copy); } catch (err) {} toast('Link copied'); return; }
  if (t.closest('[data-vego]')) { e.stopPropagation(); vePublish(); return; }
  if (t.closest('[data-master]')) vePop = false;
});
document.addEventListener('click', (e) => { if (vePop && !e.target.closest('.ve__pubw')) { vePop = false; drawActs(); } });
// first click on a section only selects it. Once selected, its links and text work
$('tabHc').addEventListener('click', (e) => {
  const b = e.target.closest('#vePage [data-blk]');
  if (b && b.dataset.blk !== veSel) { e.preventDefault(); e.stopPropagation(); veSelect(b.dataset.blk); }
}, true);
$('tabHc').addEventListener('click', (e) => {
  const t = e.target, H = ST.hc; let h;
  const stop = () => e.stopPropagation();
  if (t.id === 'veStage') { if (veSel || veStyle) { veSel = null; veStyle = false; renderHc(); } return; }
  if ((h = t.closest('[data-vesel]'))) { stop(); const was = veSel; veSelect(h.dataset.vesel); if (!h.dataset.vesel) { const r = document.querySelector('.ve__orb[data-vesel="' + was + '"]'); if (r) r.focus(); } else if (h.classList.contains('ve__orb')) { const r = document.querySelector('.ve__orb[data-vesel="' + h.dataset.vesel + '"]'); if (r) r.focus(); } return; }
  if ((h = t.closest('[data-vestyle]'))) { stop(); veStyle = !veStyle; veSel = null; renderHc(); const f = veStyle ? document.querySelector('#veSty [data-col]') : document.querySelector('.ve__stb'); if (f) f.focus(); return; }
  if ((h = t.closest('[data-vepage]'))) { stop(); vePage = h.dataset.vepage; veSel = vePage === 'article' ? 'article' : null; veStyle = false; renderHc(); $('veStage').scrollTop = 0; vePlace(); document.querySelector('[data-vepage="' + vePage + '"]').focus(); return; }
  if ((h = t.closest('[data-vedev]'))) { stop(); veDev = h.dataset.vedev; renderHc(); document.querySelector('[data-vedev="' + veDev + '"]').focus(); setTimeout(vePlace, 300); return; }
  if (t.closest('[data-vefs]')) { stop(); veFs(!document.body.classList.contains('is-fs')); return; }
  if (t.closest('[data-veundo]')) { stop(); veUndo(); const b = document.querySelector('[data-veundo]'); if (b && !b.disabled) b.focus(); return; }
  if (t.closest('[data-veredo]')) { stop(); veRedo(); const b = document.querySelector('[data-veredo]'); if (b && !b.disabled) b.focus(); return; }
  if ((h = t.closest('[data-veotab]'))) { stop(); veTab = h.dataset.veotab; renderHc(); document.querySelector('[data-veotab="' + veTab + '"]').focus(); return; }
  if ((h = t.closest('[data-veart]'))) { stop(); veDrawer = false; veOpenArt(h.dataset.veart); return; }
  if (t.closest('[data-vedrawer]')) { stop(); veOpenDrawer(); return; }
  if (t.closest('[data-vedrawerx]')) { stop(); veDrawer = false; renderHc(); const b = document.querySelector('[data-vedrawer]'); if (b) b.focus(); return; }
  if ((h = t.closest('[data-vehide]'))) { stop(); const k = h.dataset.vehide, out = !!h.closest('.ve__out'); veDo(() => { if (!hcHid(k)) H.hidden.push(k); if (veSel === k) veSel = null; }, VE_SEC[k][0] + ' hidden'); const f = document.querySelector(out ? '.ve__eye[data-veshow="' + k + '"]' : '#vePage [data-veshow="' + k + '"]'); if (f) f.focus(); return; }
  if ((h = t.closest('[data-veshow]'))) { stop(); const k = h.dataset.veshow, out = !!h.closest('.ve__out'); veDo(() => { H.hidden = H.hidden.filter(x => x !== k); }, VE_SEC[k][0] + ' is visible again'); const f = document.querySelector(out ? '.ve__eye[data-vehide="' + k + '"]' : '.ve__orb[data-vesel="' + k + '"]'); if (f) f.focus(); return; }
  if ((h = t.closest('[data-vemv]'))) {
    stop(); const d = +h.dataset.vemv, o = hcOrder(), i = o.indexOf(veSel), j = i + d; if (j < 0 || j >= o.length) return;
    const k = veSel; veDo(() => { o.splice(i, 1); o.splice(j, 0, k); H.order = o; }, 'Moved ' + VE_SEC[k][0] + (d < 0 ? ' up' : ' down')); veReveal();
    const f = document.querySelector('#vePage [data-vemv="' + d + '"]:not([disabled])') || document.querySelector('#vePage [data-vemv]:not([disabled])'); if (f) f.focus(); return;
  }
  if ((h = t.closest('[data-veset]'))) { stop(); const k = h.dataset.veset; veLast = 0; H[k] = k === 'trendN' ? +h.dataset.v : h.dataset.v; hcChange(); keepFocus(renderHc); return; }
  if ((h = t.closest('[data-vetog]'))) { stop(); const k = h.dataset.vetog; veLast = 0; H[k] = !(H[k] !== false); hcChange(); keepFocus(renderHc); return; }
  if ((h = t.closest('[data-vechip]'))) { stop(); veRun(h.textContent); return; }
  if ((h = t.closest('#vePage [data-pvq]'))) { stop(); veOpenArt(h.dataset.pvq); return; }
  if (t.closest('#vePage [data-pvhome]')) { stop(); vePage = 'home'; veSel = null; renderHc(); $('veStage').scrollTop = 0; return; }
  const cp = t.closest('#vePage [data-copy]'); if (cp) { stop(); return; }
});
// the AI bar
$('tabHc').addEventListener('submit', (e) => { if (e.target.id !== 'veAi') return; e.preventDefault(); const v = $('veAiIn').value.trim(); if (v) veRun(v); });
$('tabHc').addEventListener('mousedown', (e) => { const c = e.target.closest('[data-vechip]'); if (c) { e.preventDefault(); veRun(c.textContent); } });
$('tabHc').addEventListener('input', (e) => {
  if (e.target.id === 'veAiIn') { const v = e.target.value.trim(); e.target.form.querySelector('.ve__aigo').disabled = !v; $('veChips').hidden = !!v; return; }
  const il = e.target.closest && e.target.closest('[data-inl]'); if (il && il.textContent.length > +il.dataset.max) { il.textContent = il.textContent.slice(0, +il.dataset.max); }
});
$('tabHc').addEventListener('focusin', (e) => { if (e.target.id === 'veAiIn' && !e.target.value.trim()) { $('veAiMsg').textContent = 'Try'; $('veChips').hidden = false; } });
const INL0 = { hero: HERO0, sub: SUB0, popT: 'Popular:', topicsT: 'Browse by topic', trendT: 'Trending this week', vidT: 'Watch in 1 minute', helpT: 'Still need help?' };
$('tabHc').addEventListener('focusout', (e) => {
  if (e.target.id === 'veAiIn') { if (!(e.relatedTarget && e.relatedTarget.closest('#veChips'))) $('veChips').hidden = true; return; }
  const il = e.target.closest && e.target.closest('[data-inl]'); if (!il) return;
  const k = il.dataset.inl, v = il.textContent.replace(/\s+/g, ' ').trim(), nv = v === INL0[k] ? '' : v, H = ST.hc;
  if (!v && k === 'hero') { drawPane(); toastError('The heading can’t be empty.'); return; }
  if ((H[k] || '') === nv) return;
  veLast = 0; H[k] = nv; hcChange(); drawPane(); veToast(k === 'hero' ? 'Heading updated' : k === 'sub' ? 'Line under the heading updated' : 'Title updated');
  const inp = document.querySelector('#veInsp [data-hf="' + k + '"]'); if (inp) inp.value = nv;
});
$('tabHc').addEventListener('keydown', (e) => {
  const il = e.target.closest && e.target.closest('[data-inl]'); if (!il) return;
  if (e.key === 'Enter') { e.preventDefault(); il.blur(); }
  if (e.key === 'Escape') { e.preventDefault(); e.stopPropagation(); il.textContent = ST.hc[il.dataset.inl] || INL0[il.dataset.inl]; il.blur(); }
});
// drag a section in the outline to reorder it
$('tabHc').addEventListener('dragstart', (e) => { const li = e.target.closest && e.target.closest('[data-vedrag]'); if (!li) return; veDrag = li.dataset.vedrag; e.dataTransfer.effectAllowed = 'move'; try { e.dataTransfer.setData('text/plain', veDrag); } catch (err) {} li.classList.add('is-drag'); });
const veDropAt = (e) => { const li = e.target.closest && e.target.closest('[data-vedrag]'); if (!li || !veDrag) return null; const r = li.getBoundingClientRect(); return [li, e.clientY > r.top + r.height / 2]; };
$('tabHc').addEventListener('dragover', (e) => {
  const at = veDropAt(e); if (!at) return; e.preventDefault();
  document.querySelectorAll('.ve__or.is-before,.ve__or.is-after').forEach(n => n.classList.remove('is-before', 'is-after'));
  if (at[0].dataset.vedrag !== veDrag) at[0].classList.add(at[1] ? 'is-after' : 'is-before');
});
$('tabHc').addEventListener('drop', (e) => {
  const at = veDropAt(e); if (!at) return; e.preventDefault();
  const k = veDrag, to = at[0].dataset.vedrag; veDrag = null; if (k === to) { renderHc(); return; }
  veDo(() => { const o = hcOrder().filter(x => x !== k); o.splice(o.indexOf(to) + (at[1] ? 1 : 0), 0, k); ST.hc.order = o; }, 'Moved ' + VE_SEC[k][0]);
});
$('tabHc').addEventListener('dragend', () => { veDrag = null; document.querySelectorAll('.ve__or.is-drag,.ve__or.is-before,.ve__or.is-after').forEach(n => n.classList.remove('is-drag', 'is-before', 'is-after')); });
document.addEventListener('keydown', (e) => {
  if ($('tabHc').hidden || document.querySelector('dialog[open]')) return;
  if ((e.metaKey || e.ctrlKey) && e.key.toLowerCase() === 'z') { const a = document.activeElement; if (a && (a.matches('input,textarea,select') || a.isContentEditable)) return; e.preventDefault(); if (e.shiftKey) veRedo(); else veUndo(); return; }
  if (e.key.toLowerCase() === 'f' && !e.metaKey && !e.ctrlKey && !e.altKey && !e.target.closest('input,textarea,select,[contenteditable]')) { veFs(!document.body.classList.contains('is-fs')); return; }
  if (e.key !== 'Escape') return;
  if (veDrawer) { veDrawer = false; renderHc(); const b = document.querySelector('[data-vedrawer]'); if (b) b.focus(); }
  else if (vePop) { vePop = false; drawActs(); document.querySelector('[data-vepop]').focus(); }
  else if (veStyle) { veStyle = false; renderHc(); document.querySelector('.ve__stb').focus(); }
  else if (veSel && !e.target.closest('.hinfo')) { const k = veSel; veSel = null; renderHc(); const r = document.querySelector('.ve__orb[data-vesel="' + k + '"]') || document.querySelector('.ve__stb'); if (r) r.focus(); }
  else if (document.body.classList.contains('is-fs') && !e.target.closest('.hinfo')) veFs(false);
});

// visitor preview: the same page, read only, full screen
function hcPreview(opener) {
  let d = $('pvDlg');
  if (!d) { d = document.createElement('dialog'); d.id = 'pvDlg'; d.className = 'dlg pv'; d.setAttribute('aria-label', 'Help Center as a visitor sees it'); document.body.appendChild(d); }
  let art = veArt(), q = null; const H = ST.hc;
  const draw = () => {
    const note = H.status === 'live' ? (H.dirty ? 'Your latest changes aren’t live yet.' : 'This is live.') : 'Not published yet.';
    d.innerHTML = '<div class="pv__bar pv__bar--v"><button class="pv__back" type="button" data-pvx>← Back to editor</button><span class="spacer"></span><span class="pv__note">' + VI(EYE) + '<span class="pv__n1">Seeing it as a visitor would. </span>' + note + '</span></div>' + pvSite(pvList(), q === null ? art : null, q === null ? {} : { ask: q });
  };
  const home = () => { art = null; q = null; draw(); d.scrollTop = 0; };
  d.onclick = (e) => {
    if (e.target.closest('[data-pvx]')) { d.close(); return; }
    const p = e.target.closest('[data-pvq]'); if (p) { art = approved().find(x => x.r.id === p.dataset.pvq); q = null; draw(); d.scrollTop = 0; const c = d.querySelector('.pv__crumb'); if (c) c.focus(); return; }
    if (e.target.closest('[data-pvhome]')) home();
  };
  d.onkeydown = (e) => { if (e.key === 'Enter' && e.target.matches('.pv__logo[data-pvhome]')) home(); };
  d.onsubmit = (e) => {
    e.preventDefault(); const f = e.target;
    if (f.matches('[data-pvask]')) { q = f.q.value.trim() || 'Is dental cleaning covered?'; pvAsk.sent = false; art = null; draw(); d.scrollTop = 0; const h = d.querySelector('.pv__ask h2'); if (h) { h.tabIndex = -1; h.focus(); } }
    else if (f.matches('[data-pvmail]')) { pvAsk.sent = true; draw(); toast('Sent to ' + H.support); }
  };
  d.onclose = () => { if (opener && opener.isConnected) opener.focus(); };
  draw(); d.showModal(); d.scrollTop = 0; d.querySelector('[data-pvx]').focus();
}
// ---------- views: the hub lists the channels; each channel opens its own page
const VIEWS = {
  answers: ['All approved answers', 'Every answer a person approved. Each channel uses these.'],
  ask: ['Ask lojo', 'Your team asks, and lojo answers from the approved answers.'],
  api: ['API &amp; MCP', 'Let AI assistants and your own systems read the approved answers. They read only what a person approved, like the chat.'],
  hc: ['Help Center', 'A public site where customers find answers. lojo builds it from the answers you make public.'],
};
const CH_IC = {
  ask: '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 5h16v11H9l-5 4z"/></svg>',
  hc: '<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c3 3.2 3 14.8 0 18M12 3c-3 3.2-3 14.8 0 18"/></svg>',
  api: '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M13 3L5 14h6l-1 7 8-11h-6z"/></svg>',
};
function renderHub() {
  hcSync();
  const all = approved(), pub = hcPublic().length, H = ST.hc, api = ST.api, n = all.length;
  $('store').innerHTML = '<div><b>' + n + ' approved answer' + (n === 1 ? '' : 's') + '</b><span>Every channel below uses these. ' + (H.status === 'new' ? 'None are public yet.' : pub + ' of them ' + (pub === 1 ? 'is' : 'are') + ' public on the Help Center.') + '</span></div><a class="btn btn--secondary btn--sm" href="#answers">See all answers</a>';
  const hcSt = {
    new: ['muted', 'Not set up', 'Choose what customers see, pick an address, publish'],
    draft: ['amber', 'Draft', pub + ' public answers · not online yet'],
    live: ['ok', 'Live', pub + ' public answers · ' + hcAddr() + (H.dirty ? ' · changes to publish' : '') + (hcCheck().length ? ' · ' + hcCheck().length + ' to check' : '')],
    off: ['muted', 'Off', 'Offline · settings kept'],
  }[H.status];
  const rows = [
    ['ask', 'Ask lojo', 'Your team asks, lojo answers', 'ok', 'On', 'Uses all ' + n + ' answers'],
    ['hc', 'Help Center', 'A public site for your customers', hcSt[0], hcSt[1], hcSt[2]],
    ['api', 'API &amp; MCP', 'For AI assistants and your own systems', api.mode === 'off' ? 'muted' : 'ok', MODES[api.mode][0], api.apps.length + ' connected app' + (api.apps.length === 1 ? '' : 's') + ' · ' + api.keys.length + ' key' + (api.keys.length === 1 ? '' : 's')],
  ];
  $('chl').innerHTML = rows.map(([id, name, d, tone, st, m]) => '<li><a class="chrow" href="#' + id + '"><span class="chrow__ic">' + CH_IC[id] + '</span><span class="chrow__t"><b>' + name + '</b><span>' + d + '</span></span><span class="chrow__m"><span class="badge badge--' + tone + '">' + st + '</span><span>' + esc(m) + '</span></span><span class="chrow__go" aria-hidden="true">›</span></a></li>').join('');
}
function view(v) {
  $('vHub').hidden = !!v; $('vSub').hidden = !v;
  $('tabAnswers').hidden = v !== 'answers'; $('tabAsk').hidden = v !== 'ask'; $('tabApi').hidden = v !== 'api'; $('tabHc').hidden = v !== 'hc';
  $('csv').hidden = $('json').hidden = v !== 'answers'; $('hcActs').hidden = v !== 'hc';
  if (v) {
    const info = v === 'hc';
    $('subT').innerHTML = VIEWS[v][0] + (info ? '<span class="hinfo"><button type="button" class="hinfo__b" data-hinfo aria-expanded="false" aria-controls="hinfoP" aria-label="About the Help Center"><svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M12 11v5M12 8h.01"/></svg></button><span class="hinfo__p" id="hinfoP" role="note"><b>About the Help Center</b>' + VIEWS[v][1] + '</span></span>' : '');
    $('subP').innerHTML = info ? '' : VIEWS[v][1]; $('subP').hidden = info;
  }
  let fs = false; try { fs = v === 'hc' && !!sessionStorage.getItem('lojo-hc-fs'); } catch (err) {}
  document.body.classList.toggle('is-fs', fs); if (v !== 'hc') document.body.classList.remove('ve-on');
  if (!v) renderHub(); if (v === 'answers') render(); if (v === 'api') renderApi(); if (v === 'hc') renderHc();
}
function hinfoClose() { const w = document.querySelector('.hinfo.is-open'); if (w) { w.classList.remove('is-open'); w.querySelector('[data-hinfo]').setAttribute('aria-expanded', 'false'); } }
document.addEventListener('click', (e) => {
  const b = e.target.closest('[data-hinfo]');
  if (b) { const w = b.parentElement, open = !w.classList.contains('is-open'); hinfoClose(); w.classList.toggle('is-open', open); b.setAttribute('aria-expanded', String(open)); return; }
  if (!e.target.closest('.hinfo')) hinfoClose();
});
document.addEventListener('keydown', (e) => { if (e.key === 'Escape' && document.querySelector('.hinfo.is-open')) { hinfoClose(); document.querySelector('[data-hinfo]').focus(); } });
function route() {
  const [v, sub] = location.hash.slice(1).split('/');
  if (v === 'hc') { veDrawer = sub === 'check'; veTab = sub === 'answers' || sub === 'content' ? 'answers' : veTab; veStyle = ['look', 'modules', 'address'].includes(sub); veSel = ({ videos: 'videos', handoff: 'help' })[sub] || null; vePage = 'home'; }
  view(VIEWS[v] ? v : ''); window.scrollTo(0, 0);
}
window.addEventListener('hashchange', route);
$('backHub').addEventListener('click', (e) => { e.preventDefault(); history.pushState(null, '', location.pathname + location.search); route(); });
route();
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
  .lrow{display:grid;grid-template-columns:44px minmax(150px,190px) minmax(0,1fr) 140px 230px 92px 80px 14px;gap:14px;align-items:center;padding:10px 16px;color:inherit;text-decoration:none;transition:background-color .15s ease}
  .lgrp + .lgrp{border-top:1px solid var(--line)}
  .lrow{position:relative}
  .lrow__link{color:inherit;text-decoration:none}
  .lrow__link::after{content:"";position:absolute;inset:0;border-radius:inherit}
  .lrow__link:focus-visible{outline:none}
  .lrow__link:focus-visible::after{box-shadow:inset 0 0 0 3px rgba(232,93,117,.3)}
  .lrow__m{position:relative;z-index:1}
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
  @media (max-width:1180px){.lrow{grid-template-columns:44px minmax(140px,180px) minmax(0,1fr) 230px 92px 80px 14px}.lrow__k{display:none}}
  @media (max-width:900px){.lrow{grid-template-columns:40px minmax(0,1fr) auto}.lrow__w,.lrow__k,.lrow time,.lrow__go,.lrow__m{display:none}}
  @media (max-width:640px){.arow{grid-template-columns:44px minmax(0,1fr)}.apill{grid-column:2;grid-row:auto;justify-self:start}.anums{gap:20px}}
  /* models: the hosting badge is the Storybook badge plus an icon, so colour never carries the meaning alone */
  .hb svg{width:11px;height:11px;flex:none;fill:none;stroke:currentColor;stroke-width:2.2;stroke-linecap:round;stroke-linejoin:round}
  .hbi{display:inline-grid;place-items:center;width:22px;height:22px;border-radius:50%;flex:none;background:rgba(63,143,95,.12);color:var(--success)}
  .hbi svg{width:12px;height:12px;fill:none;stroke:currentColor;stroke-width:2.2;stroke-linecap:round;stroke-linejoin:round}
  .mrow .hbi{margin-left:auto}
  .mname{font-family:ui-monospace,Menlo,monospace;font-size:.76rem;color:var(--ink);overflow-wrap:anywhere}
  /* ---------- 1. data boundary: where text goes, drawn ---------- */
  .dbx{margin:0 0 18px;padding:16px 18px 18px;border:1px solid var(--line);border-radius:18px;background:var(--panel);box-shadow:0 16px 30px -28px rgba(36,26,20,.3)}
  .dbx__head{display:flex;align-items:center;gap:12px;flex-wrap:wrap;margin-bottom:14px}
  .dbx__head p{flex:1;min-width:240px;margin:0;font-size:.88rem;color:var(--ink)}
  .dbx__head .btn{height:32px;font-size:.8rem}
  .dbx__hint{font-size:.74rem;color:var(--muted)}
  .dbx--one{display:flex;align-items:center;gap:10px 14px;flex-wrap:wrap;padding:12px 16px}
  .dbx--one p{flex:1;min-width:240px;margin:0;font-size:.88rem;color:var(--ink)}
  .dbx--one .btn{height:32px;font-size:.8rem}
  .dbx__st{display:inline-flex;align-items:center;gap:7px;font-size:.76rem;font-weight:600;color:var(--muted);white-space:nowrap}
  .dbx__st .zst{margin:0}
  .dbx__flow{display:grid;grid-template-columns:minmax(120px,150px) 34px minmax(0,1fr) 34px minmax(120px,150px);align-items:center}
  .dbx__end{display:grid;gap:4px;justify-items:start;padding:12px 14px;border-radius:14px;background:var(--bg-soft)}
  .dbx__end i{display:grid;place-items:center;width:30px;height:30px;border-radius:9px;background:var(--panel);color:var(--muted);box-shadow:0 1px 3px rgba(36,26,20,.12)}
  .dbx__end svg{width:16px;height:16px;fill:none;stroke:currentColor;stroke-width:1.9;stroke-linecap:round;stroke-linejoin:round}
  .dbx__end b{font-size:.84rem}
  .dbx__end span{font-size:.72rem;color:var(--muted);line-height:1.35}
  .dbx__arr{position:relative;height:2px;margin:0 4px;background:repeating-linear-gradient(90deg,var(--line-3,rgba(36,26,20,.3)) 0 5px,transparent 5px 9px)}
  .dbx__arr::after{content:"";position:absolute;right:-2px;top:-4px;border:5px solid transparent;border-left:7px solid rgba(36,26,20,.35);border-right:0}
  .dbx__arr i{position:absolute;top:50%;left:0;width:6px;height:6px;margin-top:-3px;border-radius:50%;background:var(--success);animation:dbxFlow 2.2s linear infinite}
  @keyframes dbxFlow{0%{left:0;opacity:0}15%{opacity:1}85%{opacity:1}100%{left:calc(100% - 6px);opacity:0}}
  /* the boundary itself: lojo's machines */
  .dbx__in{position:relative;padding:22px 14px 14px;border:2px dashed rgba(63,143,95,.55);border-radius:16px;background:rgba(63,143,95,.04)}
  .dbx__tag{position:absolute;top:-11px;left:14px;display:inline-flex;align-items:center;gap:6px;height:22px;padding:0 10px;border-radius:999px;background:var(--panel);border:1px solid rgba(63,143,95,.45);font-size:.66rem;font-weight:800;letter-spacing:.1em;text-transform:uppercase;color:var(--success)}
  .dbx__tag svg{width:12px;height:12px;fill:none;stroke:currentColor;stroke-width:2.2;stroke-linecap:round;stroke-linejoin:round}
  .dbx__boxes{display:flex;flex-wrap:wrap;gap:10px}
  .dbx__box{flex:1 1 180px;padding:10px 12px;border-radius:12px;background:var(--panel);border:1px solid var(--line)}
  .dbx__box b{display:flex;align-items:center;gap:7px;font-size:.8rem}
  .dbx__box b svg{width:14px;height:14px;fill:none;stroke:var(--muted);stroke-width:1.9;stroke-linecap:round;stroke-linejoin:round}
  .dbx__box small{font-size:.7rem;font-weight:500;color:var(--muted)}
  .dbx__chips{display:flex;flex-wrap:wrap;gap:6px;margin-top:8px}
  .dbx__chip{display:inline-flex;flex-direction:column;align-items:flex-start;gap:1px;padding:6px 11px;border-radius:10px;border:1px solid var(--line-2);background:var(--bg-soft);font:inherit;text-align:left;color:var(--ink);cursor:pointer}
  .dbx__chip b{font-size:.78rem;font-weight:700;line-height:1.25}
  .dbx__chip small{font-size:.68rem;color:var(--muted);line-height:1.25}
  .dbx__chip:hover,.dbx__chip:focus-visible{border-color:var(--rose);outline:none;box-shadow:0 0 0 3px rgba(232,93,117,.14)}
  /* outside the boundary: third-party vendors */
  .dbx__out{display:grid;grid-template-columns:minmax(120px,150px) 34px minmax(0,1fr) 34px minmax(120px,150px);margin-top:4px}
  .dbx__cross{grid-column:3;display:flex;align-items:center;gap:8px;padding:6px 0 6px 22px;margin-left:22px;border-left:2px dashed rgba(201,162,74,.8);font-size:.74rem;font-weight:700;color:#8A6212}
  .dbx__cross svg{width:13px;height:13px;fill:none;stroke:currentColor;stroke-width:2.2;stroke-linecap:round;stroke-linejoin:round}
  .dbx__ven{grid-column:3;position:relative;padding:22px 14px 14px;border:2px solid rgba(201,162,74,.6);border-radius:16px;background:var(--amber-soft)}
  .dbx__ven .dbx__tag{border-color:rgba(201,162,74,.7);color:#8A6212}
  .dbx__ven .dbx__box{border-color:rgba(201,162,74,.35)}
  .dbx.is-unk .dbx__arr i{display:none}
  /* status of each setup */
  .zst{margin-left:6px;padding:2px 8px;border-radius:999px;font-style:normal;font-size:.6rem;font-weight:800;letter-spacing:.06em}
  .zst--on{background:rgba(63,143,95,.14);color:var(--success)}
  .zst--ven{background:rgba(201,162,74,.22);color:#8A6212}
  .zst--off{background:rgba(36,26,20,.07);color:var(--muted)}
  .dbx__cap{margin:10px 2px 0;font-size:.72rem;color:var(--muted)}
  .dbx__out.is-off .dbx__cross{border-left-color:var(--line-2);color:var(--muted)}
  .dbx__ven.is-off{border:2px dashed var(--line-2);background:var(--bg-soft)}
  .dbx__ven.is-off .dbx__tag{border-color:var(--line-2);color:var(--muted)}
  .dbx__ven.is-off .dbx__box{border-color:var(--line)}
  .dbx__ven.is-off .dbx__box > b,.dbx__ven.is-off .dbx__chip > b,.dbx__ven.is-off .dbx__chip > small{opacity:.6}
  .dbx__ven.is-off .dbx__chip{background:transparent;border-style:dashed}
  .dbx__offnote{margin:0 0 10px;font-size:.78rem;color:var(--muted)}
  .ctip__off{font-weight:700;color:var(--ink)}
  .ctip .ctip__if{margin:12px 0 -6px;font-size:.62rem;font-weight:800;letter-spacing:.12em;text-transform:uppercase;color:var(--muted)}
  .dbx--lite{display:flex;align-items:center;gap:12px;padding:12px 16px;border-color:rgba(63,143,95,.28);background:rgba(63,143,95,.06);box-shadow:none}
  .dbx--lite.is-ven{border-color:rgba(201,162,74,.5);background:var(--amber-soft)}
  .dbx--lite.is-unk{border-color:var(--line-2);background:var(--bg-soft)}
  .dbx--lite p{margin:0;font-size:.88rem;color:var(--ink)}
  .dbx--lite p b{font-weight:700}
  .dbx__ic{display:grid;place-items:center;width:32px;height:32px;flex:none;border-radius:10px;background:var(--panel);color:var(--success);box-shadow:0 1px 3px rgba(36,26,20,.12)}
  .dbx--lite.is-ven .dbx__ic{color:#8A6212} .dbx--lite.is-unk .dbx__ic{color:var(--muted)}
  .dbx__ic svg{width:16px;height:16px;fill:none;stroke:currentColor;stroke-width:2;stroke-linecap:round;stroke-linejoin:round}
  body.ml-lite .lrow{grid-template-columns:44px minmax(150px,200px) minmax(0,1fr) 150px 92px 80px 14px}
  @media (max-width:900px){body.ml-lite .lrow{grid-template-columns:40px minmax(0,1fr) auto}}
  .dbx.is-unk .dbx__in{border-color:var(--line-2);background:var(--bg-soft)}
  .dbx.is-unk .dbx__tag{border-color:var(--line-2);color:var(--muted)}
  .dbx__q{margin:0;font-size:.82rem;color:var(--muted)}
  @media (max-width:900px){
    .dbx__flow,.dbx__out{grid-template-columns:1fr}
    .dbx__arr{width:2px;height:22px;margin:4px 0 4px 26px;background:repeating-linear-gradient(180deg,rgba(36,26,20,.3) 0 5px,transparent 5px 9px)}
    .dbx__arr::after,.dbx__arr i{display:none}
    .dbx__cross,.dbx__ven{grid-column:1}
    .dbx__body{display:flex;flex-direction:column}
    .dbx__flow,.dbx__out{display:contents}
    .o1{order:1}.o2{order:2}.o3{order:3}.o4{order:4}.o5{order:5}.o6{order:6}.o7{order:7}
    .dbx__cross{margin:0 0 0 26px;padding-top:10px}
    .dbx__ven{margin-bottom:4px}
  }
  :root[data-theme="dark"] .dbx__ven .dbx__tag,:root[data-theme="dark"] .dbx__cross{color:#E3C27A}

  /* model chip hover card: the facts for that one model, where the model is */
  .dbx__chip{position:relative;cursor:help;outline:none}
  .ctip{position:absolute;left:0;top:calc(100% + 8px);z-index:30;width:300px;padding:16px 18px 14px;border-radius:16px;background:var(--panel);border:1px solid var(--line);color:var(--ink);box-shadow:0 24px 50px -20px rgba(36,26,20,.45);
    opacity:0;visibility:hidden;transform:translateY(-4px);transition:opacity .15s ease,transform .15s ease,visibility .15s;pointer-events:none;text-align:left;font-weight:400}
  .ctip::before{content:"";position:absolute;left:22px;bottom:100%;width:12px;height:12px;margin-bottom:-6px;background:var(--panel);border-left:1px solid var(--line);border-top:1px solid var(--line);transform:rotate(45deg)}
  .dbx__chip:hover .ctip,.dbx__chip:focus-visible .ctip,.dbx__chip:focus .ctip{opacity:1;visibility:visible;transform:none}
  .ctip > b{display:block;font-family:var(--display);font-size:1.02rem;color:var(--ink)}
  .ctip > b small{font-family:var(--body);font-weight:500;font-size:.78rem;color:var(--muted)}
  .ctip > span{display:block;margin-top:4px;font-size:.8rem;line-height:1.45;color:var(--muted)}
  .ctip dl{margin:12px 0 0;padding-top:6px;border-top:1px solid var(--line)}
  .ctip dl div{display:flex;justify-content:space-between;gap:12px;padding:6px 0;font-size:.8rem}
  .ctip dt{color:var(--muted);flex:none}
  .ctip dd{margin:0;text-align:right;font-weight:600;color:var(--ink)}
  .ctip dd.ok{color:var(--success)} .ctip dd.warn{color:#8A6212}
  .ctip p{margin:8px 0 0;font-size:.76rem;line-height:1.45;color:var(--muted)}
  .ctip p.terms{padding:8px 10px;border-radius:9px;background:var(--amber-soft);color:#5E4310}
  .ctip em{display:block;margin-top:8px;font-style:normal;font-family:ui-monospace,Menlo,monospace;font-size:.68rem;color:var(--muted)}
  /* card: one row per model, label · name · badge; the badge drops below the name when the card is narrow */
  .amods{display:grid;gap:4px;margin-top:4px;padding-top:10px;border-top:1px solid var(--line)}
  .amods summary{display:flex;align-items:center;gap:8px;list-style:none;cursor:pointer;margin:0 -8px;padding:4px 8px;border-radius:9px}
  .amods summary::-webkit-details-marker{display:none}
  .amods summary:hover{background:var(--bg-soft)}
  .amods summary:focus-visible{outline:none;box-shadow:0 0 0 3px rgba(232,93,117,.16)}
  .amods__h{font-size:.64rem;font-weight:800;letter-spacing:.12em;text-transform:uppercase;color:var(--muted)}
  .amods__h em{font-style:normal;margin-left:4px;padding:1px 6px;border-radius:6px;border:1px solid var(--line-2);letter-spacing:0;color:var(--ink)}
  .amods__sum{display:flex;flex-wrap:wrap;gap:4px;margin-left:auto}
  .amods[open] .amods__sum{display:none}
  .amods__chev{width:15px;height:15px;flex:none;fill:none;stroke:var(--muted);stroke-width:2.2;stroke-linecap:round;stroke-linejoin:round;transition:transform .2s ease}
  .amods[open] .amods__chev{transform:rotate(180deg);margin-left:auto}
  .amods--none{padding-top:10px}
  .mrow{position:relative;display:flex;align-items:center;flex-wrap:wrap;gap:3px 8px;margin:0 -8px;padding:4px 8px;border-radius:9px;cursor:help;outline:none;transition:background-color .15s ease}
  .mrow:hover,.mrow:focus-visible{background:var(--bg-soft)}
  .mrow:focus-visible{box-shadow:0 0 0 3px rgba(232,93,117,.16)}
  .mrow__l{text-decoration:underline dotted rgba(36,26,20,.3);text-underline-offset:3px}
  /* hover cards: light, like a model card: name, one line on what it does, divider, facts */
  .mtip{position:absolute;left:0;right:0;bottom:calc(100% + 8px);z-index:20;padding:14px 16px 12px;border-radius:16px;background:var(--panel);border:1px solid var(--line);color:var(--ink);box-shadow:0 24px 50px -20px rgba(36,26,20,.45);
    opacity:0;visibility:hidden;transform:translateY(4px);transition:opacity .15s ease,transform .15s ease,visibility .15s;pointer-events:none;cursor:default}
  .mtip::after{content:"";position:absolute;left:24px;top:100%;width:12px;height:12px;margin-top:-6px;background:var(--panel);border-right:1px solid var(--line);border-bottom:1px solid var(--line);transform:rotate(45deg)}
  .mrow:hover .mtip,.mrow:focus-visible .mtip{opacity:1;visibility:visible;transform:none}
  .mtip .mtip__id{display:block;margin-top:8px;font-style:normal;font-family:ui-monospace,Menlo,monospace;font-size:.68rem;color:var(--muted)}
  .mtip b{display:block;font-family:var(--display);font-size:.98rem;font-weight:700;color:var(--ink)}
  .mtip span{display:block;margin-top:4px;padding-bottom:10px;border-bottom:1px solid var(--line);font-size:.8rem;line-height:1.45;color:var(--muted)}
  .mtip small{display:flex;align-items:center;gap:6px;margin-top:10px;font-size:.76rem;font-weight:600;color:var(--success)}
  .mtip small.ven{color:#8A6212}
  .mtip small svg{width:12px;height:12px;fill:none;stroke:currentColor;stroke-width:2.2;stroke-linecap:round;stroke-linejoin:round}
  .acardx{position:relative}
  .acardx:hover,.acardx:focus-within{z-index:3}
  .mrow__l{flex:none;width:58px;font-size:.72rem;font-weight:600;color:var(--muted)}
  .mrow .mname{flex:1 1 auto;min-width:0}
  .mrow .badge{margin-left:auto}
  .amods__none{margin:0;font-size:.78rem;color:var(--muted)}
  .acardx .acardx__last{margin-bottom:2px}
  .mrow .mprod{font-size:.84rem;font-weight:500}
  .mprev{display:flex;align-items:center;gap:4px;flex-wrap:wrap;margin:0 0 12px;padding:4px;border-radius:12px;border:1px dashed var(--line-2);width:max-content;max-width:100%}
  .mprev[hidden]{display:none}
  .mprev span{padding:0 8px 0 6px;font-size:.66rem;font-weight:800;letter-spacing:.1em;text-transform:uppercase;color:var(--muted)}
  .mprev button{height:28px;padding:0 11px;border:0;border-radius:8px;background:none;font:inherit;font-size:.78rem;font-weight:600;color:var(--muted);cursor:pointer}
  .mprev button[aria-pressed="true"]{background:var(--ink);color:var(--bg)}
  /* list: first model, +N, badge */
  button.lrow__m{display:flex;flex-direction:column;align-items:flex-start;gap:4px;min-width:0;max-width:100%;padding:6px 8px;margin:-6px -8px;border:1px solid transparent;border-radius:10px;background:none;font:inherit;color:inherit;text-align:left;cursor:pointer}
  button.lrow__m:hover,button.lrow__m[aria-expanded="true"]{border-color:var(--line-2);background:var(--panel)}
  button.lrow__m:focus-visible{outline:none;box-shadow:0 0 0 3px rgba(232,93,117,.2)}
  .lrow__mt{display:flex;align-items:center;gap:6px;max-width:100%;white-space:nowrap}
  .lrow__mt .mprod{overflow:hidden;text-overflow:ellipsis;font-size:.84rem;font-weight:600}
  .lrow__mt em{font-style:normal;font-size:.72rem;font-weight:700;color:var(--muted)}
  .lrow__chev{width:14px;height:14px;flex:none;fill:none;stroke:var(--muted);stroke-width:2.2;stroke-linecap:round;stroke-linejoin:round;transition:transform .2s ease}
  button.lrow__m[aria-expanded="true"] .lrow__chev{transform:rotate(180deg)}
  .lrow__mb{display:flex;flex-wrap:wrap;gap:4px}
  .lrow__m--none{color:var(--muted)}
  /* the models panel under a list row */
  .lmods{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,360px));gap:4px 28px;padding:6px 16px 14px 74px;background:var(--bg-soft);border-top:1px dashed var(--line-2)}
  .lmods[hidden]{display:none}
  .lmods .mrow{margin:0}
  .lmods .mrow:hover,.lmods .mrow:focus-visible{background:var(--panel)}
  .lgrp.is-open .lrow{background:var(--bg-soft)}
  /* in the list the hover card opens downward, and the list no longer clips it */
  .llist{overflow:visible}
  .llist > .lgrp:first-child .lrow{border-radius:14px 14px 0 0}
  .llist > .lgrp:last-child .lrow,.llist > .lgrp:last-child .lmods{border-radius:0 0 14px 14px}
  .lmods .mtip{bottom:auto;top:calc(100% + 8px);right:auto;width:320px}
  .lmods .mtip::after{top:auto;bottom:100%;margin:0 0 -6px;transform:rotate(225deg)}
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
      <div class="mprev" id="mprev" role="group" aria-label="Prototype only: preview a setup"></div>
      <div class="dbx" id="dbx"></div>
      <div class="agf chips" id="agFilters" role="group" aria-label="Filter agents"></div>
      <div id="alist"></div>
    </section>
""",
  js=r"""
// ---------- models (D113 design) ----------
// The live page reads the models from the env, so names can differ per env. The prototype fakes three envs:
// activity.html (the POC today: all self-hosted), ?models=vendor (the third-party setup the code supports), ?models=unknown.
// model name: [what it does, hosting, where it runs (self-hosted) or provider (third-party)]
const MODEL_INFO = {
  'qwen3.5:9b': ['Reads, writes, answers', 'self', 'Mac mini (Ollama)'],
  'bge-m3': ['Search by meaning', 'self', 'Mac mini (Ollama)'],
  'whisper-large-v3-turbo': ['Call recordings to text', 'self', 'Mac mini (whisper.cpp)'],
  'tesseract': ['Reads scanned pages (OCR)', 'self', 'lojo’s server'],
  'claude-haiku-4-5': ['Finds questions, masking', 'vendor', 'Anthropic'],
  'claude-opus-5-5': ['Drafts answers and SOPs', 'vendor', 'Anthropic'],
  'claude-sonnet-5-5': ['Chat answers', 'vendor', 'Anthropic'],
  'text-embedding-3-small': ['Search by meaning', 'vendor', 'OpenAI'],
  'whisper-1': ['Call recordings to text', 'vendor', 'OpenAI'],
  // ASSUMPTION: for the Mixed design preview only. Not in the ticket’s supported list; IDs follow each vendor’s naming. check with Eric
  'gpt-5.6-terra': ['Balanced, efficient language model', 'vendor', 'OpenAI'],
  'gemini-3.8-flash': ['Fast language model', 'vendor', 'Google'],
  'gemini-4-argon': ['Language model', 'vendor', 'Google'],
};
// CX names: lead with what the model is, in plain words, then the product name as people write it.
// The env’s technical ID (qwen3.5:9b) is kept for engineers: hover card and AI facts. An ID not listed here shows as it comes.
const FRIENDLY = {
  'bge-m3': ['Meaning search', 'BGE-M3'], 'qwen3.5:9b': ['Language model', 'Qwen 3.5'],
  'tesseract': ['Scan reader', 'Tesseract'], 'whisper-large-v3-turbo': ['Call transcriber', 'Whisper'],
  'claude-haiku-4-5': ['Quick language model', 'Claude Haiku 4.5'], 'claude-opus-5-5': ['Drafting model', 'Claude Opus 5.5'],
  'claude-sonnet-5-5': ['Chat model', 'Claude Sonnet 5.5'], 'text-embedding-3-small': ['Meaning search', 'OpenAI Embeddings'],
  'whisper-1': ['Call transcriber', 'OpenAI Whisper'],
  'gpt-5.6-terra': ['Language model', 'GPT-5.6 Terra'], 'gemini-3.8-flash': ['Quick language model', 'Gemini 3.8 Flash'], 'gemini-4-argon': ['Language model', 'Gemini 4 Argon'],
};
const nice = (m) => FRIENDLY[m] || [m, ''];
const prod = (m) => (FRIENDLY[m] || [, m])[1];
const Q = 'qwen3.5:9b', E = 'bge-m3';
const AGENT_MODELS = {
  poc: {
    'Indexer': [['Search', E], ['Masking', Q], ['Scans', 'tesseract'], ['Calls', 'whisper-large-v3-turbo']],
    'Drafting agent': [['Model', Q], ['Search', E]], 'Rewrite agent': [['Model', Q]], 'SOP builder': [['Model', Q]],
    'Question finder': [['Model', Q]], 'Gap finder': [['Model', Q]], 'Topic grouper': [['Model', Q]], 'Opportunity finder': [['Model', Q]],
    'Chat agent': [['Model', Q], ['Search', E]],
  },
  // ASSUMPTION: the ticket names a third-party model for finding questions, masking, drafting/SOPs, chat, search and calls only.
  // Rewrite follows drafting (Opus); Gap finder, Topic grouper and Opportunity finder follow the question finder (Haiku). check with Eric
  // Mixed: a design preview with self-hosted and current third-party models side by side, so every badge shows
  mixed: {
    'Indexer': [['Search', E], ['Masking', Q], ['Scans', 'tesseract'], ['Calls', 'whisper-large-v3-turbo']],
    'Drafting agent': [['Model', 'claude-opus-5-5'], ['Search', E]], 'Rewrite agent': [['Model', 'claude-opus-5-5']], 'SOP builder': [['Model', 'gpt-5.6-terra']],
    'Question finder': [['Model', Q]], 'Gap finder': [['Model', 'gemini-3.8-flash']], 'Topic grouper': [['Model', Q]], 'Opportunity finder': [['Model', 'gemini-4-argon']],
    'Chat agent': [['Model', 'claude-sonnet-5-5'], ['Search', 'text-embedding-3-small']],
  },
  vendor: {
    'Indexer': [['Search', 'text-embedding-3-small'], ['Masking', 'claude-haiku-4-5'], ['Scans', 'tesseract'], ['Calls', 'whisper-1']],
    'Drafting agent': [['Model', 'claude-opus-5-5'], ['Search', 'text-embedding-3-small']], 'Rewrite agent': [['Model', 'claude-opus-5-5']], 'SOP builder': [['Model', 'claude-opus-5-5']],
    'Question finder': [['Model', 'claude-haiku-4-5']], 'Gap finder': [['Model', 'claude-haiku-4-5']], 'Topic grouper': [['Model', 'claude-haiku-4-5']], 'Opportunity finder': [['Model', 'claude-haiku-4-5']],
    'Chat agent': [['Model', 'claude-sonnet-5-5'], ['Search', 'text-embedding-3-small']],
  },
};
// what each model does, in plain words, for the hover card on a model row
const JOB = {
  'Search': ['Finds by meaning', 'Turns each passage into numbers that capture its meaning, so a search for “refund window” also finds “money back within 30 days”.'],
  'Masking': ['Hides personal data', 'Spots names, emails and phone numbers in documents and calls, and hides them before anything is stored.'],
  'Scans': ['Reads scanned pages', 'Reads the text in scanned PDFs and images (OCR), so they can be searched like any other document.'],
  'Calls': ['Transcribes calls', 'Turns call recordings into text, so calls are indexed and searched like documents.'],
};
const MODEL_JOB = {
  'Drafting agent': 'Writes each draft answer from your sources, with the passages it used.',
  'Rewrite agent': 'Writes a rejected draft again, using the reason the reviewer gave.',
  'SOP builder': 'Turns approved answers into step-by-step SOPs, citing a source for every step.',
  'Question finder': 'Reads your sources and finds the questions they answer.',
  'Gap finder': 'Compares your sources to find what’s missing or contradicts itself.',
  'Topic grouper': 'Groups questions into topics so you can see which are rising.',
  'Opportunity finder': 'Spots questions that point to something to build or sell.',
  'Chat agent': 'Writes the reply to a question, using approved answers only.',
};
function modelTip(agent, label, model) {
  const j = label === 'Model' ? ['Language model', MODEL_JOB[agent] || 'Reads, writes and answers for this agent.'] : (JOB[label] || [label, '']);
  const m = MODEL_INFO[model];
  const host = !m ? '<small>' + IC_UNK + 'Not reported where this runs</small>'
    : m[1] === 'self' ? '<small>' + IC_SELF + 'Self-hosted · runs on ' + PLACE + '</small>'
    : '<small class="ven">' + IC_VEN + 'Third-party · text is sent to ' + esc(m[2]) + '</small>';
  return '<span class="mtip" role="tooltip"><b>' + j[0] + '</b><span>' + j[1] + '</span>' + host + '<em class="mtip__id">Technical name: ' + esc(model) + '</em></span>';
}
// CX: customers see “lojo’s own servers”, not the machines (Mac mini, server). Machine names stay in MODEL_INFO for engineers.
// ASSUMPTION: the region isn’t known yet. Set REGION (e.g. 'UAE') once confirmed and it shows wherever the place is named. check with Eric
const REGION = '';
const PLACE = 'lojo’s own servers' + (REGION ? ' in ' + REGION : '');
// Admins see models, the boundary and AI facts; Editors get one plain sentence (Viewers can’t open Activity)
const isLite = () => (window.LOJO_ROLE || 'admin') !== 'admin';
const NO_MODEL = { 'Sync agent': 'No model: it only reads the sources', 'Publisher': 'No model: it only publishes approved answers' };
let modelEnv = ['vendor', 'mixed', 'unknown'].includes(new URLSearchParams(location.search).get('models')) ? new URLSearchParams(location.search).get('models') : 'poc';
const modelsOf = (name) => modelEnv === 'unknown' ? null : (AGENT_MODELS[modelEnv][name] || []);
const IC_SELF = '<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="4" width="18" height="7" rx="2"/><rect x="3" y="13" width="18" height="7" rx="2"/><path d="M7 7.5h.01M7 16.5h.01"/></svg>';
const IC_VEN = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M14 4h6v6M20 4l-9 9M18 14v5a1 1 0 0 1-1 1H5a1 1 0 0 1-1-1V7a1 1 0 0 1 1-1h5"/></svg>';
const IC_UNK = '<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M9.5 9.5a2.5 2.5 0 1 1 3.5 2.3c-.6.3-1 .9-1 1.6M12 17h.01"/></svg>';
// the hosting badge: Self-hosted, or Third-party · vendor; where it runs is in the tooltip and in “Show all models”
function hostBadge(model, quiet, inRow) {
  const m = MODEL_INFO[model];
  if (quiet && m && m[1] === 'self') return '<span class="hbi" role="img" aria-label="Self-hosted, runs on ' + PLACE + '"' + (inRow ? '' : ' title="Self-hosted: runs on ' + PLACE + '"') + '>' + IC_SELF + '</span>';
  if (!m) return '<span class="badge badge--muted hb" title="The env didn’t say where this model runs">' + IC_UNK + 'Unknown</span>';
  return m[1] === 'self'
    ? '<span class="badge badge--ok hb"' + (inRow ? '' : ' title="Self-hosted: runs on ' + PLACE + '"') + '>' + IC_SELF + 'Self-hosted</span>'
    : '<span class="badge badge--amber hb"' + (inRow ? '' : ' title="Third-party: text is sent to ' + esc(m[2]) + '"') + '>' + IC_VEN + 'Third-party · ' + esc(m[2]) + '</span>';
}
// open or closed per agent, remembered; open by default
let MOPEN = {};
try { MOPEN = JSON.parse(localStorage.getItem('lojo-models-open')) || {}; } catch (e) {}
function modelsBlock(name) {
  if (isLite()) return '';
  if (NO_MODEL[name]) return '<div class="amods amods--none"><p class="amods__none">' + NO_MODEL[name] + '</p></div>';
  const ms = modelsOf(name);
  if (ms === null) return '<div class="amods amods--none"><p class="amods__none">Models couldn’t be read just now</p></div>';
  // collapsed, the summary still says where the text goes: one badge per hosting kind
  const kinds = [...new Set(ms.map(([, m]) => (MODEL_INFO[m] || [])[1] === 'vendor' ? 'v:' + MODEL_INFO[m][2] : 's'))];
  const sumBadges = kinds.map(k => k === 's' ? '<span class="badge badge--ok hb">' + IC_SELF + 'Self-hosted</span>' : '<span class="badge badge--amber hb">' + IC_VEN + esc(k.slice(2)) + '</span>').join('');
  return '<details class="amods" data-models-of="' + esc(name) + '"' + (MOPEN[name] === false ? '' : ' open') + '><summary><span class="amods__h">Models <em>' + ms.length + '</em></span><span class="amods__sum">' + sumBadges + '</span>' +
    '<svg class="amods__chev" viewBox="0 0 24 24" aria-hidden="true"><path d="m6 9 6 6 6-6"/></svg></summary>' +
    ms.map(([label, model]) =>
      '<div class="mrow" tabindex="0" aria-label="' + esc(label + ': ' + prod(model)) + '"><span class="mrow__l">' + label + '</span><span class="mprod">' + esc(prod(model)) + '</span>' + hostBadge(model, false, true) + modelTip(name, label, model) + '</div>').join('') + '</details>';
}
// list: the first model, +N, and one badge; the badge is third-party if any of the agent’s models is, so it never hides a vendor
function modelsCell(name, open) {
  if (isLite()) return '';
  const ms = modelsOf(name);
  if (NO_MODEL[name] || !ms || !ms.length) return '<span class="lrow__m lrow__m--none" title="' + esc(NO_MODEL[name] || 'Models couldn’t be read just now') + '">—</span>';
  // one badge per hosting kind, like the collapsed card summary
  const kinds = [...new Set(ms.map(([, m]) => (MODEL_INFO[m] || [])[1] === 'vendor' ? 'v:' + MODEL_INFO[m][2] : 's'))];
  const badges = kinds.map(k => k === 's' ? '<span class="badge badge--ok hb">' + IC_SELF + 'Self-hosted</span>' : '<span class="badge badge--amber hb">' + IC_VEN + esc(k.slice(2)) + '</span>').join('');
  return '<button type="button" class="lrow__m" data-lmods="' + esc(name) + '" aria-expanded="' + !!open + '" aria-controls="' + lmId(name) + '" aria-label="' + esc('Models for ' + name + ': ' + ms.map(([l, m]) => l + ' ' + prod(m)).join(', ')) + '">' +
    '<span class="lrow__mt"><span class="mprod">' + esc(prod(ms[0][1])) + '</span>' + (ms.length > 1 ? '<em>+' + (ms.length - 1) + '</em>' : '') +
    '<svg class="lrow__chev" viewBox="0 0 24 24" aria-hidden="true"><path d="m6 9 6 6 6-6"/></svg></span><span class="lrow__mb">' + badges + '</span></button>';
}
// ---------- 1. the data boundary: your sources → lojo’s machines (→ vendors) → your team ----------
// who made each model; separate from who runs it (whisper is made by OpenAI but runs on lojo’s Mac mini)
const MAKER = {
  'qwen3.5:9b': 'Alibaba (Qwen)', 'bge-m3': 'BAAI', 'whisper-large-v3-turbo': 'OpenAI (open weights)', 'tesseract': 'Open source (Tesseract)',
  'claude-haiku-4-5': 'Anthropic', 'claude-opus-5-5': 'Anthropic', 'gpt-5.6-terra': 'OpenAI', 'gemini-3.8-flash': 'Google', 'gemini-4-argon': 'Google', 'claude-sonnet-5-5': 'Anthropic', 'text-embedding-3-small': 'OpenAI', 'whisper-1': 'OpenAI',
};
// ASSUMPTION: the Indexer masks personal data when it indexes, so later jobs see masked text. The masking, call and scan
// models read the original text, because they run before masking (or are the masking). check with Eric
const RAW_JOBS = ['Masking', 'Calls', 'Scans'];
const IC_DOCS = '<svg viewBox="0 0 24 24"><path d="M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8z"/><path d="M14 3v5h5M9 13h6M9 17h4"/></svg>';
const IC_TEAM = '<svg viewBox="0 0 24 24"><circle cx="9" cy="8" r="4"/><path d="M2 20a7 7 0 0 1 14 0M16 4a4 4 0 0 1 0 8M22 20a7 7 0 0 0-4-6"/></svg>';
const IC_LOCK = '<svg viewBox="0 0 24 24"><rect x="4" y="10" width="16" height="11" rx="2"/><path d="M8 10V7a4 4 0 0 1 8 0v3"/></svg>';
const IC_MAC = '<svg viewBox="0 0 24 24"><rect x="4" y="5" width="16" height="12" rx="3"/><path d="M9 20h6"/></svg>';
const IC_CLOUD = '<svg viewBox="0 0 24 24"><path d="M17.5 19a4.5 4.5 0 1 0-1.4-8.8A6 6 0 0 0 4.5 12a3.5 3.5 0 0 0 1 7z"/></svg>';
function modelUse() {
  const used = {};
  if (modelEnv !== 'unknown') AGENTS.forEach(([, name]) => (modelsOf(name) || []).forEach(([label, m]) => { (used[m] = used[m] || { agents: [], jobs: [] }); used[m].agents.push(name); used[m].jobs.push(label); }));
  return used;
}
// a model in the diagram: its plain name, and on hover (or tap) the facts for that model
function chipTip(m, u) {
  const n = nice(m), i = MODEL_INFO[m] || ['Not reported', '', 'Not reported'], self = i[1] === 'self';
  const raw = u.jobs.some(j => RAW_JOBS.includes(j)), masks = u.jobs.includes('Masking');
  const row = (k, v, cls) => '<div><dt>' + k + '</dt><dd' + (cls ? ' class="' + cls + '"' : '') + '>' + v + '</dd></div>';
  // personal data, always with the reason: the masking model reads it to mask it; the call and scan models read the original
  const pd = !raw ? (self ? 'Masked before it gets here' : 'Masked before it’s sent')
    : self ? (masks ? 'Reads it to mask it' : 'Reads the original text') : 'Sent before it’s masked';
  return '<span class="ctip" role="tooltip"><b>' + esc(n[0]) + (n[1] ? ' <small>· ' + esc(n[1]) + '</small>' : '') + '</b><span>' + esc(i[0]) + '</span>' + (u.agents.length ? '' : '<p class="ctip__if">If it were switched on</p>') + '<dl>' +
    row('Made by', esc(MAKER[m] || 'Not reported')) +
    row('Runs on', self ? PLACE : esc(i[2]) + '’s cloud') +
    row('Text leaves lojo', self ? 'No' : 'Yes, to ' + esc(i[2]), self ? 'ok' : 'warn') +
    row('Personal data', pd, !raw ? 'ok' : self ? '' : 'warn') +
    (self ? row('Trains on your data', 'No', 'ok') + row('Keeps your text', 'Only on lojo’s servers', 'ok') : '') +
    '</dl>' + (self ? '' : '<p class="terms">Training and retention follow lojo’s agreement with ' + esc(i[2]) + '. Ask us for the terms.</p>') +
    '<p>' + (u.agents.length ? 'Used by ' + esc([...new Set(u.agents)].join(', ')) : '<b class="ctip__off">Not used in this workspace.</b> Supported by lojo, switched off here.') + '</p><em>Technical name: ' + esc(m) + '</em></span>';
}
// “Anthropic”, “Anthropic and OpenAI”, “Anthropic, Google and OpenAI”
const listAnd = (xs) => xs.length < 3 ? xs.join(' and ') : xs.slice(0, -1).join(', ') + ' and ' + xs[xs.length - 1];
let USED = {};
// third-party models the code supports (ticket D113), shown greyed out when the workspace doesn’t use them
const SUPPORTED_VEN = ['claude-haiku-4-5', 'claude-opus-5-5', 'claude-sonnet-5-5', 'text-embedding-3-small', 'whisper-1'];
const SUP_VENDORS = [...new Set(SUPPORTED_VEN.map(m => MODEL_INFO[m][2]))].sort();
const chip = (m) => { const n = nice(m); return '<span class="dbx__chip" tabindex="0" aria-label="' + esc(n[0] + (n[1] ? ', ' + n[1] : '')) + '"><b>' + esc(n[0]) + '</b>' + (n[1] ? '<small>' + esc(n[1]) + '</small>' : '') + chipTip(m, USED[m] || { agents: [], jobs: [] }) + '</span>'; };
function renderBoundary() {
  const used = modelUse(), names = Object.keys(used), box = $('dbx');
  USED = used;
  const self = names.filter(m => (MODEL_INFO[m] || [])[1] === 'self'), ven = names.filter(m => (MODEL_INFO[m] || [])[1] === 'vendor');
  const vendors = [...new Set(ven.map(m => MODEL_INFO[m][2]))].sort();
  document.body.classList.toggle('ml-lite', isLite());
  if (isLite()) {
    // Editors: the one answer they care about, in plain words; no model names
    box.className = 'dbx dbx--lite' + (modelEnv === 'unknown' ? ' is-unk' : vendors.length ? ' is-ven' : '');
    box.innerHTML = modelEnv === 'unknown'
      ? '<span class="dbx__ic">' + IC_UNK + '</span><p>We couldn’t check where your text is processed just now.</p>'
      : vendors.length
        ? '<span class="dbx__ic">' + IC_VEN + '</span><p><b>Some text is processed by outside AI companies: ' + listAnd(vendors) + '.</b> Your admin can see which parts and why.</p>'
        : '<span class="dbx__ic">' + IC_LOCK + '</span><p><b>Your documents and questions stay on ' + PLACE + '.</b> Nothing is sent to outside AI companies.</p>';
    return;
  }
  // Admins: one line. The status, where text goes, and whether the interim and third-party setups are in use
  box.className = 'dbx dbx--one' + (modelEnv === 'unknown' ? ' is-unk' : '');
  if (modelEnv === 'unknown') {
    box.innerHTML = '<span class="badge badge--muted hb">' + IC_UNK + 'Unknown</span><p>The models could not be read just now.</p><button class="btn btn--secondary" type="button" id="mRetry">Try again</button>';
    return;
  }
  const st = (on, cls) => '<i class="zst zst--' + (on ? cls : 'off') + '">' + (on ? 'In use' : 'Not in use') + '</i>';
  box.innerHTML = (vendors.length
      ? '<span class="badge badge--amber hb">' + IC_VEN + 'Third-party</span><p role="status">Some models are third-party: text is sent to ' + listAnd(vendors) + '.</p>'
      : '<span class="badge badge--ok hb">' + IC_SELF + 'Self-hosted</span><p role="status">Every model is self-hosted: documents and questions never leave lojo’s own machines.</p>') +
    '<span class="dbx__st">' + (modelEnv === 'poc' ? 'Interim (POC)' : 'Self-hosted') + st(self.length, 'on') + '</span>' +
    '<span class="dbx__st">Third-party' + st(vendors.length, 'ven') + '</span>';
}

// prototype only: flip between setups to review the design; the live page reads the setup from the env
const PREVIEWS = [['poc', 'POC today'], ['mixed', 'Mixed'], ['vendor', 'Third-party'], ['unknown', 'Not known']];
function renderPreview() {
  $('mprev').hidden = isLite();
  $('mprev').innerHTML = '<span>Prototype · preview setup</span>' + PREVIEWS.map(([k, l]) => '<button type="button" data-env="' + k + '" aria-pressed="' + (modelEnv === k) + '">' + l + '</button>').join('');
}
$('mprev').addEventListener('click', (e) => {
  const b = e.target.closest('[data-env]'); if (!b) return;
  modelEnv = b.dataset.env;
  const u = new URL(location.href); if (modelEnv === 'poc') u.searchParams.delete('models'); else u.searchParams.set('models', modelEnv);
  history.replaceState(null, '', u); render();
});
$('dbx').addEventListener('click', (e) => {
  if (e.target.closest('#mRetry')) toast('Still can’t read the models. Try again in a minute.');
});

let agFilter = new URLSearchParams(location.search).get('stage') || 'all';
// what each agent has done so far, from the same counts the rest of the app uses
function statsFor(name, c) {
  const failed = Object.keys(ST.draftFailed || {}).filter(k => ST.draftFailed[k] && ST.draftFailed[k] !== 'retrying').length;
  const docFail = (ST.docx || []).filter(d => d.status === 'failed').length;
  const ch = ST.chat || {}, rewritten = DRAFTS.filter(r => decision(r).redrafted).length;
  return {
    'Sync agent': [[c.docs + (ST.docx || []).length, 'Documents synced'], [sourceSummary().sources, 'Sources connected'], [docFail, 'Failed syncs', docFail]],
    'Indexer': [[c.pages, 'Pages read'], [c.passages, 'Passages indexed'], [0, 'Failed runs']],
    'Question finder': [[c.questions, 'Questions found'], [4, 'New since yesterday'], [0, 'Failed runs']],
    'Gap finder': [[c.gaps, 'Open gaps'], [1, 'Contradictions'], [0, 'Failed runs']],
    'Drafting agent': [[c.drafts, 'Drafts written'], [c.pending, 'Waiting for review'], [failed, 'Failed drafts', failed]],
    'Rewrite agent': [[rewritten, 'Drafts rewritten'], [DRAFTS.filter(r => decision(r).redrafted > 1).length, 'Rewritten more than once'], [c.final, 'Left for a human']],
    'Chat agent': [[(ch.asked || 0) + 14, 'Questions asked'], [(ch.answered || 0) + 11, 'Answered'], [(ch.declined || 0) + 3, 'Declined']],
    'Publisher': [[0, 'Published'], [0, 'Channels'], ['—', 'Full build']],
    'SOP builder': [[(ST.sops || []).length, 'SOPs'], [(ST.sops || []).filter(s => s.status === 'review').length, 'In review'], [(ST.sops || []).filter(s => s.status === 'due').length, 'Due for a check']],
    'Topic grouper': [[c.questions, 'Questions grouped'], [4, 'Channels compared'], [0, 'Failed runs']],
    'Opportunity finder': [[10, 'Opportunities'], [4, 'Themes'], [0, 'Failed runs']],
  }[name] || [['—', ''], ['—', ''], ['—', '']];
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
if (location.hash === '#list' || location.hash === '#cards') view = location.hash.slice(1);
function card([k, name, min, last, what], c) {
  const s = AG_STAGES.find(x => x[0] === k);
  const pill = min === 0 ? '<span class="apill run">Working</span>' : min === null ? '<span class="apill">Not yet</span>' : '<span class="apill">Idle</span>';
  return '<article class="acardx' + (min === 0 ? ' is-run' : '') + (min === null ? ' is-off' : '') + '"><div class="acardx__top">' + ava3d(k, name, min) + pill + '</div>' +
    '<h3>' + esc(name) + '</h3><a class="acardx__stage" href="' + s[2] + '">' + s[1] + '</a><p class="acardx__d">' + esc(what) + '</p>' +
    '<div class="acardx__nums">' + statsFor(name, c).map(([n, l, bad]) => '<div' + (bad ? ' class="bad"' : '') + '><b>' + (typeof n === 'number' ? n.toLocaleString('en-GB') : n) + '</b><span>' + l + '</span></div>').join('') + '</div>' +
    '<p class="acardx__last">' + (min === null ? 'No activity yet' : (min === 0 ? '<i class="ld"></i><b>Running now</b> · ' : agAgo(min) + ' · ') + esc(last)) + '</p>' + modelsBlock(name) + '</article>';
}
document.getElementById('alist').addEventListener('toggle', (e) => {
  const d = e.target; if (!d.matches || !d.matches('details.amods')) return;
  MOPEN[d.dataset.modelsOf] = d.open; try { localStorage.setItem('lojo-models-open', JSON.stringify(MOPEN)); } catch (err) {}
}, true);
function line([k, name, min, last, what], c) {
  const s = AG_STAGES.find(x => x[0] === k), n = statsFor(name, c)[0];
  const pill = min === 0 ? '<span class="apill run">Working</span>' : min === null ? '<span class="apill">Not yet</span>' : '<span class="apill">Idle</span>';
  const open = LOPEN[name] === true;
  return '<div class="lgrp' + (open ? ' is-open' : '') + '"><div class="lrow' + (min === null ? ' is-off' : '') + '">' + ava3d(k, name, min) +
    '<span class="lrow__n"><a class="lrow__link" href="' + s[2] + '"><b>' + esc(name) + '</b></a><span>' + s[1] + '</span></span>' +
    '<span class="lrow__w">' + (min === null ? 'No activity yet' : esc(last)) + '</span>' +
    '<span class="lrow__k"><b>' + (typeof n[0] === 'number' ? n[0].toLocaleString('en-GB') : n[0]) + '</b> ' + n[1].replace(/^[A-Z](?=[a-z])/, (ch) => ch.toLowerCase()) + '</span>' +
    modelsCell(name, open) + pill + '<time>' + (min === null ? '—' : agAgo(min)) + '</time><span class="lrow__go">→</span></div>' + listModels(name, open) + '</div>';
}
// list view: models fold out under the row, in the same rows as the cards (label · name · badge, with hover)
let LOPEN = {};
try { LOPEN = JSON.parse(localStorage.getItem('lojo-models-open-list')) || {}; } catch (e) {}
const lmId = (name) => 'lm-' + name.replace(/\W/g, '');
function listModels(name, open) {
  if (isLite() || NO_MODEL[name]) return '';
  const ms = modelsOf(name); if (!ms || !ms.length) return '';
  return '<div class="lmods" id="' + lmId(name) + '"' + (open ? '' : ' hidden') + '>' + ms.map(([label, model]) =>
    '<div class="mrow" tabindex="0" aria-label="' + esc(label + ': ' + prod(model)) + '"><span class="mrow__l">' + label + '</span><span class="mprod">' + esc(prod(model)) + '</span>' + hostBadge(model, false, true) + modelTip(name, label, model) + '</div>').join('') + '</div>';
}
document.getElementById('alist').addEventListener('click', (e) => {
  const b = e.target.closest('[data-lmods]'); if (!b) return;
  e.preventDefault();
  const name = b.dataset.lmods, g = b.closest('.lgrp'), panel = document.getElementById(lmId(name)), open = panel.hidden;
  panel.hidden = !open; b.setAttribute('aria-expanded', open); g.classList.toggle('is-open', open);
  LOPEN[name] = open; try { localStorage.setItem('lojo-models-open-list', JSON.stringify(LOPEN)); } catch (err) {}
});
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
  renderBoundary(); renderPreview();
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
  css=r"""
  .head .fsbtn{gap:6px;margin-right:6px}
  .fsbtn svg{width:15px;height:15px;fill:none;stroke:currentColor;stroke-width:1.9;stroke-linecap:round;stroke-linejoin:round}
  body.is-fs .side,body.is-fs .mnav,body.is-fs .fab{display:none!important}
  body.is-fs .main{margin-left:0}
  body.is-fs .wrap{max-width:none;padding:16px 24px 24px}
  body.is-fs .head{margin:-16px -24px 16px;padding:12px 24px}
  body.is-fs .head > div:first-child > p:not(.label),body.is-fs .head .htip,body.is-fs .rocard{display:none}
  body.is-fs .head h1{font-size:1.3rem;margin:2px 0 0}
  body.is-fs .kb{grid-template-columns:minmax(380px,32%) minmax(0,1fr)}
  body.is-fs .klist{top:76px;max-height:calc(100vh - 96px)}
  body.is-fs .fsbtn{background:var(--ink);border-color:var(--ink);color:#fff}

  body.kview .ktabs{display:none!important}

  /* simpler Knowledge: the library is the page */
  .ksec,.kover,#fSpace,#fType{display:none!important}
  .klib{margin-top:0}

  .rocard{display:flex;align-items:center;gap:14px;margin:0 0 18px;padding:16px 20px;border-radius:16px;border:1px solid rgba(232,93,117,.3);background:linear-gradient(90deg,#FFF0E8,#FFFFFF);color:var(--ink);text-decoration:none}
  .rocard:hover{text-decoration:none;box-shadow:0 12px 26px -20px rgba(232,93,117,.6)}
  .rocard__ic{width:42px;height:42px;border-radius:12px;flex:none;display:grid;place-items:center;background:#fff;font-size:1.2rem;box-shadow:0 2px 6px -3px rgba(36,26,20,.3)}
  .rocard__t{flex:1;min-width:0}
  .rocard__t small{display:block;font-size:.66rem;font-weight:800;letter-spacing:.12em;text-transform:uppercase;color:var(--rose)}
  .rocard__t b{display:block;font-family:var(--display);font-size:1.05rem}
  .rocard__t span{font-size:.84rem;color:var(--muted)}
  .rocard__go{font-weight:700;color:#B73C54;white-space:nowrap}
  :root[data-theme="dark"] .rocard{background:linear-gradient(90deg,rgba(232,93,117,.12),transparent)}

  .kstats{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:14px;margin-bottom:14px}
  .kstat{padding:18px 20px;border:1px solid var(--line);border-radius:16px;background:var(--panel)}
  .kstat i{display:block;width:28px;height:4px;border-radius:4px;margin-bottom:10px;background:var(--line-2)}
  .kstat.ok i{background:var(--success)} .kstat.warn i{background:#C9A24A} .kstat.ref i{background:#8C817B} .kstat.all i{background:var(--rose)}
  .kstat small{display:block;font-size:.68rem;font-weight:800;letter-spacing:.12em;text-transform:uppercase;color:var(--muted)}
  .kstat b{display:block;font-family:var(--display);font-weight:800;font-size:2rem;line-height:1.1;margin:4px 0 2px}
  .kstat span{font-size:.8rem;color:var(--muted);line-height:1.4}
  .kgrid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:14px;margin-bottom:26px}
  .kbox{padding:16px 18px;border:1px solid var(--line);border-radius:16px;background:var(--panel)}
  .kbox h3{display:flex;align-items:center;gap:8px;margin:0 0 4px;font-size:.74rem;font-weight:800;letter-spacing:.12em;text-transform:uppercase}
  .kbox h3 svg{width:16px;height:16px;fill:none;stroke:currentColor;stroke-width:1.9;stroke-linecap:round;stroke-linejoin:round}
  .kbox p{margin:0 0 10px;font-size:.8rem;color:var(--muted)}
  .kbox .pills{display:flex;flex-wrap:wrap;gap:6px}
  .kpill{display:inline-flex;align-items:center;gap:8px;height:28px;padding:0 11px;border-radius:999px;border:1px solid var(--line-2);background:var(--bg-soft);font-size:.78rem;cursor:pointer;font-family:inherit;color:var(--ink)}
  .kpill b{font-weight:700;color:var(--muted)}
  .kpill:hover{border-color:rgba(36,26,20,.3)}
  .kbox .sub2{margin:10px 0 6px;font-size:.74rem;color:var(--muted);font-weight:600}
  .recent{list-style:none;margin:0;padding:0}
  .recent li{display:flex;justify-content:space-between;gap:12px;padding:7px 0;border-top:1px solid var(--line);font-size:.82rem}
  .recent li:first-child{border-top:0}
  .recent button{border:0;background:none;padding:0;font:inherit;color:var(--ink);text-align:left;cursor:pointer;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
  .recent button:hover{color:#B73C54}
  .recent time{color:var(--muted);white-space:nowrap;font-size:.76rem}
  .kfil{display:grid;grid-template-columns:minmax(200px,1.4fr) repeat(5,minmax(0,1fr));gap:10px;margin-bottom:14px;align-items:end}
  .kfil label{display:grid;gap:4px;font-size:.72rem;font-weight:600;color:var(--muted)}
  .kfil select,.kfil input{height:40px}
  .kb{display:grid;grid-template-columns:400px minmax(0,1fr);gap:18px;align-items:start}
  .klist{position:sticky;top:96px;max-height:calc(100vh - 116px);display:flex;flex-direction:column;overflow:hidden}
  .klist__h{padding:12px 16px;border-bottom:1px solid var(--line);font-size:.82rem;color:var(--muted)}
  .klist ul{list-style:none;margin:0;padding:6px;overflow:auto}
  .kitem{padding:14px;border-radius:12px;cursor:pointer;display:grid;gap:6px}
  .kitem + .kitem{margin-top:2px}
  .kitem:hover{background:var(--bg-soft)}
  .kitem.is-sel{background:linear-gradient(90deg,rgba(232,93,117,.07),transparent);box-shadow:inset 3px 0 0 var(--rose)}
  .kitem b{font-size:.9rem;font-weight:700;line-height:1.35}
  .kitem .ex{font-size:.8rem;color:var(--muted);display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden}
  .kitem .ft{font-size:.74rem;color:var(--muted)}
  .chipsrow{display:flex;gap:6px;flex-wrap:wrap}
  .kc{display:inline-flex;align-items:center;gap:5px;height:22px;padding:0 9px;border-radius:999px;background:var(--bg-soft);font-size:.7rem;font-weight:600;color:var(--muted)}
  .kc svg{width:12px;height:12px;fill:none;stroke:currentColor;stroke-width:2}
  .kc.pub{background:rgba(63,143,95,.12);color:var(--success)} .kc.rev{background:var(--amber-soft);color:#8A6212} .kc.drf{background:rgba(62,111,166,.1);color:var(--info)} .kc.sp{background:rgba(62,111,166,.08);color:var(--info)}
  .ksrc{display:flex;align-items:center;gap:8px;padding:7px 10px;border-radius:9px;background:var(--bg-soft);font-size:.78rem;font-weight:600}
  .ksrc svg{width:14px;height:14px;fill:none;stroke:var(--muted);stroke-width:1.8;flex:none}
  .kdet{padding:26px 30px}
  .kdet__acts{display:flex;gap:8px;margin:14px 0 4px}
  .kdet__acts .btn{height:34px}
  .kdet__acts .arch{color:#B73C54}
  .kdet h2{font-family:var(--display);font-weight:700;font-size:1.7rem;letter-spacing:-.02em;line-height:1.2;margin:14px 0 14px}
  .kdet .ask{display:inline-flex;align-items:center;gap:8px;height:40px;padding:0 16px;border-radius:12px;border:1px solid var(--line-2);background:var(--panel);font:inherit;font-weight:600;font-size:.86rem;cursor:pointer;color:var(--ink);margin-bottom:16px}
  .kdet .ask:hover{border-color:rgba(232,93,117,.4)}
  .kdet .ask svg{width:16px;height:16px;fill:none;stroke:currentColor;stroke-width:1.9}
  .kdet__body{font-size:.98rem;line-height:1.7;margin-bottom:20px}
  .kpanel{border:1px solid var(--line);border-radius:14px;padding:16px 18px;margin-bottom:12px}
  .kpanel h4{display:flex;align-items:center;gap:8px;margin:0 0 10px;font-size:.84rem;font-weight:700}
  .kpanel h4 svg{width:16px;height:16px;fill:none;stroke:currentColor;stroke-width:1.9}
  .kpanel .open{display:inline-flex;align-items:center;gap:6px;margin-top:10px;font-size:.82rem;font-weight:600;color:var(--ink)}
  .kpanel .open svg{width:13px;height:13px;fill:none;stroke:currentColor;stroke-width:2}
  .gov{background:var(--bg-soft)}
  .gov p{margin:0 0 10px;font-size:.84rem;color:var(--muted)}
  .gov .row{display:flex;gap:8px;flex-wrap:wrap}
  .kempty{padding:30px;text-align:center;color:var(--muted)}
  .archived{opacity:.6}
  @media (max-width:1200px){.kfil{grid-template-columns:repeat(3,minmax(0,1fr))}.kgrid{grid-template-columns:1fr 1fr}}
  @media (max-width:1000px){.kb{grid-template-columns:1fr}.klist{position:static;max-height:420px}.kstats{grid-template-columns:1fr 1fr}}
  /* compact */
  .kstats{gap:10px;margin-bottom:10px}
  .kstat{padding:12px 16px;border-radius:12px;display:grid;grid-template-columns:auto 1fr;grid-template-rows:auto auto;column-gap:12px;align-items:center}
  .kstat i{grid-column:1/-1;width:22px;height:3px;margin-bottom:8px}
  .kstat small{grid-column:1/-1;font-size:.62rem}
  .kstat b{font-size:1.5rem;margin:2px 0 0}
  .kstat span{font-size:.72rem;line-height:1.3}
  .kgrid{gap:10px;margin-bottom:16px}
  .kbox{padding:12px 14px;border-radius:12px}
  .kbox h3{font-size:.66rem}
  .kbox p{font-size:.74rem;margin-bottom:8px}
  .kpill{height:24px;padding:0 9px;font-size:.72rem}
  .recent li{padding:5px 0;font-size:.78rem}
  .kfil{gap:8px;margin-bottom:10px}
  .kfil label{font-size:.66rem}
  .kfil select,.kfil input{height:36px;font-size:.84rem}
  .kb{grid-template-columns:360px minmax(0,1fr);gap:14px}
  .klist__h{padding:10px 14px;font-size:.76rem}
  .kitem{padding:10px 12px;gap:4px}
  .kitem b{font-size:.84rem}
  .kitem .ex{font-size:.76rem;-webkit-line-clamp:1}
  .kitem .ksrc{display:none}
  .kc{height:20px;font-size:.66rem;padding:0 8px}
  .kdet{padding:20px 24px}
  .kdet h2{font-size:1.35rem;margin:10px 0}
  .kdet__acts{margin:10px 0 0}
  .kdet__acts .btn{height:30px;font-size:.78rem}
  .kdet .ask{height:34px;font-size:.8rem;margin-bottom:12px}
  .kdet__body{font-size:.9rem;line-height:1.6;margin-bottom:14px}
  .kpanel{padding:12px 14px;margin-bottom:10px;border-radius:12px}
  .kpanel h4{font-size:.78rem;margin-bottom:8px}
  .gov p{font-size:.78rem;margin-bottom:8px}
  /* charts */
  .donut{display:flex;align-items:center;gap:16px}
  .donut svg{width:96px;height:96px;flex:none}
  .dn__n{font-family:var(--display);font-weight:800;font-size:17px;fill:var(--ink)}
  .dn__l{font-size:8px;fill:var(--muted);letter-spacing:.06em}
  .legend{list-style:none;margin:0;padding:0;display:grid;gap:4px;flex:1;min-width:0}
  .legend button{display:grid;grid-template-columns:10px 1fr auto 34px;gap:8px;align-items:center;width:100%;padding:4px 6px;border:0;border-radius:7px;background:none;font:inherit;font-size:.78rem;color:var(--ink);cursor:pointer;text-align:left}
  .legend button:hover{background:var(--bg-soft)}
  .legend i{width:10px;height:10px;border-radius:3px}
  .legend b{font-weight:700}
  .legend em{font-style:normal;color:var(--muted);font-size:.72rem;text-align:right}
  .hbars{display:grid;gap:5px}
  .hb{display:grid;grid-template-columns:76px 1fr 24px;gap:8px;align-items:center;padding:3px 4px;border:0;border-radius:6px;background:none;font:inherit;font-size:.74rem;color:var(--ink);cursor:pointer;text-align:left}
  .hb:hover{background:var(--bg-soft)}
  .hb__l{white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
  .hb__t{height:8px;border-radius:4px;background:var(--bg-soft);overflow:hidden}
  .hb__t i{display:block;height:100%;border-radius:4px;background:linear-gradient(90deg,#E85D75,#FFB199)}
  .hb b{text-align:right;font-weight:700}
  .kbox .sub2{margin:10px 0 5px}
  .stackbar{display:flex;gap:2px;height:8px;border-radius:4px;overflow:hidden}
  .stackl{margin:5px 0 0!important;font-size:.72rem!important;white-space:pre}
  .spark{display:flex;align-items:flex-end;gap:6px;height:62px;margin:6px 0 8px;padding-bottom:14px;position:relative}
  .sp__c{flex:1;height:100%;display:flex;flex-direction:column;justify-content:flex-end;align-items:center;position:relative}
  .sp__c i{width:100%;max-width:22px;border-radius:4px 4px 2px 2px;background:linear-gradient(180deg,#FFB199,#E85D75)}
  .sp__c em{position:absolute;bottom:-14px;font-style:normal;font-size:.58rem;color:var(--muted);white-space:nowrap}
  /* stat tiles: small squares, left aligned, details in the i tooltip */
  .kstats{display:flex;flex-wrap:wrap;gap:10px;grid-template-columns:none}
  .kstat{display:flex!important;flex-direction:column;align-items:center;text-align:center;width:168px;padding:14px 16px;border-radius:14px}
  .kstat i.bar{display:block;width:22px;height:3px;border-radius:3px;margin-bottom:10px;background:var(--line-2)}
  .kstat.ok i.bar{background:var(--success)} .kstat.warn i.bar{background:#C9A24A} .kstat.ref i.bar{background:#8C817B} .kstat.all i.bar{background:var(--rose)}
  .kstat small{display:flex;align-items:center;gap:6px;font-size:.62rem;white-space:nowrap}
  .kstat b{font-size:1.9rem;margin:6px 0 0;line-height:1}
  .tip{position:relative;width:16px;height:16px;border-radius:50%;background:#8E2F45;color:#fff;font-style:normal;font-size:.62rem;font-weight:800;display:grid;place-items:center;letter-spacing:0;cursor:help}
  .tip::after{content:attr(data-tip);position:absolute;bottom:calc(100% + 8px);left:50%;transform:translate(-50%,4px);width:220px;padding:9px 11px;border-radius:10px;background:var(--ink);color:#fff;font-size:.74rem;font-weight:500;line-height:1.4;letter-spacing:0;text-transform:none;text-align:left;opacity:0;pointer-events:none;transition:opacity .15s ease,transform .15s ease;z-index:5}
  .tip:hover::after,.tip:focus::after{opacity:1;transform:translate(-50%,0)}
  .kstat i.tip{display:grid!important;width:15px!important;height:15px!important;margin:0!important;border-radius:50%!important;background:#8E2F45!important;color:#fff;font-size:.58rem;place-items:center;flex:none}
  .kstat{position:relative}
  .kstat .tip::after{white-space:normal;width:210px;left:50%;transform:translate(-50%,4px);text-transform:none;letter-spacing:0;font-weight:500;font-size:.76rem;line-height:1.4;z-index:30}
  .kstat .tip:hover::after,.kstat .tip:focus::after{transform:translate(-50%,0)}
  /* bigger squares, plus the spaces tile with its hover card */
  .kstat{width:196px;min-height:150px;justify-content:center;padding:18px}
  .kstat b{font-size:2.3rem;margin-top:10px}
  .kstat.sp i.bar{background:#3E6FA6}
  .kstat.sp{cursor:default}
  .kstat__hint{margin-top:6px;font-size:.66rem;color:var(--muted)}
  .kpop{position:absolute;top:calc(100% + 8px);left:50%;transform:translate(-50%,6px);width:340px;padding:14px 16px;border-radius:14px;border:1px solid var(--line);background:var(--panel);box-shadow:0 24px 50px -24px rgba(36,26,20,.45);text-align:left;opacity:0;pointer-events:none;transition:opacity .15s ease,transform .15s ease;z-index:40}
  .kstat.sp:hover .kpop,.kstat.sp:focus-within .kpop{opacity:1;transform:translate(-50%,0);pointer-events:auto}
  .kpop::before{content:"";position:absolute;left:0;right:0;top:-10px;height:10px}
  .kpop__h{margin:0 0 10px!important;font-size:.7rem!important;font-weight:800;letter-spacing:.1em;text-transform:uppercase;color:var(--muted)}
  .kpop{align-items:stretch}
  .kpop .donut{display:flex!important;flex-direction:row;align-items:center;gap:14px}
  .kpop .donut svg{width:88px;height:88px}
  .kpop .legend b{font-size:.8rem!important;margin:0!important;line-height:1.2!important;font-family:var(--body)!important}
  .kpop .legend i{display:block!important;width:10px!important;height:10px!important;margin:0!important;border-radius:3px!important}
  .kpop{text-align:left!important}
  .kpop .legend i,.kpop .legend b,.kpop .legend em,.kpop .legend span{grid-column:auto!important;grid-row:auto!important}
  .kpop .legend{display:grid!important;flex:1}
  .kpop .legend li{display:block}
  .kpop .legend button{display:grid!important;grid-template-columns:10px minmax(0,1fr) auto 36px!important;align-items:center!important;text-align:left!important;flex-direction:row!important}
  /* KPI group, like Your knowledge today on the dashboard */
  .ksec{background:var(--panel);border:1px solid var(--line);border-radius:20px;padding:18px 20px 20px;margin-bottom:14px;box-shadow:0 16px 30px -28px rgba(36,26,20,.3)}
  .ksec__h{display:flex;align-items:baseline;gap:8px;margin-bottom:14px;flex-wrap:wrap}
  .ksec__h h2{margin:0;font-size:.8rem;font-weight:800;letter-spacing:.12em;text-transform:uppercase;color:#8E2F45}
  .ksec__h span{color:var(--muted);font-size:.86rem}
  .ksec .kstats{display:grid!important;grid-template-columns:repeat(5,minmax(0,1fr));gap:14px;margin:0}
  .kt{position:relative;display:flex;flex-direction:column;align-items:flex-start;gap:4px;padding:18px 20px 20px;border-radius:12px;border:1px solid var(--line-2);background:var(--bg-soft);color:inherit;text-decoration:none;transition:box-shadow .15s ease,transform .15s ease}
  a.kt[href]:hover{text-decoration:none;transform:translateY(-1px);box-shadow:0 14px 26px -20px rgba(36,26,20,.55)}
  .kt small{display:inline-flex;align-items:center;gap:6px;font-size:.72rem;font-weight:800;letter-spacing:.1em;text-transform:uppercase;color:var(--ink);margin-bottom:4px;white-space:nowrap}
  .kt b{font-family:var(--display);font-weight:800;font-size:1.6rem;line-height:1.05;letter-spacing:-.02em}
  .kt__sub{font-size:.78rem;color:var(--muted)}
  .kt{padding-top:34px}
  .kt{align-items:center;text-align:center}
  .kt{min-width:0;overflow:visible}
  .kt small{white-space:normal!important;flex-wrap:wrap;justify-content:center;letter-spacing:.06em;line-height:1.3;max-width:100%}
  .ksec .kstats{grid-template-columns:repeat(auto-fit,minmax(150px,1fr))!important}
  .kt .tip::after{left:50%;transform:translate(-50%,4px)}
  .kt .tip:hover::after,.kt .tip:focus::after{transform:translate(-50%,0)}
  .kt__tag{position:absolute;top:10px;right:10px;height:20px;padding:0 9px;border-radius:999px;font-size:.62rem;font-weight:700;display:inline-flex;align-items:center;color:#fff}
  .kt--ok{background:#F2F7EC;border-color:#DCE8CE}.kt--ok b{color:#2F6B47}.kt--ok .kt__tag{background:var(--success)}
  .kt--warn{background:#FBF1E4;border-color:#F0DCC0}.kt--warn b{color:#8A5A12}.kt--warn .kt__tag{background:#C98A2E}
  .kt--sp{background:#EEF3FA;border-color:#D6E2F2;cursor:default}.kt--sp b{color:#2C5A91}
  .kt .tip{position:relative}
  .kt .tip::after{left:0;transform:translate(0,4px);width:220px;white-space:normal;text-transform:none;letter-spacing:0;font-weight:500;font-size:.76rem;line-height:1.4;z-index:30}
  .kt .tip:hover::after,.kt .tip:focus::after{transform:translate(0,0)}
  .kt--sp:hover .kpop,.kt--sp:focus-within .kpop{opacity:1;transform:translate(-50%,0);pointer-events:auto}
  .kt--sp .kpop{left:50%}
  :root[data-theme="dark"] .kt--ok,:root[data-theme="dark"] .kt--warn,:root[data-theme="dark"] .kt--sp{background:var(--bg-soft);border-color:var(--line-2)}
  @media (max-width:1200px){.ksec .kstats{grid-template-columns:repeat(3,minmax(0,1fr))}}
  /* structure: summary · library (tabs, filters, list + detail) · overview */
  .klib{margin-top:6px}
  .klib__h{display:flex;align-items:center;gap:16px;flex-wrap:wrap;margin:0 0 12px}
  .klib__h h2,.kover__h{margin:0;font-size:.8rem;font-weight:800;letter-spacing:.12em;text-transform:uppercase;color:#8E2F45}
  .ktabs{display:flex;gap:4px;flex-wrap:wrap;padding:3px;border-radius:12px;background:var(--bg-soft);border:1px solid var(--line)}
  .ktab{display:inline-flex;align-items:center;gap:7px;height:32px;padding:0 12px;border:0;border-radius:9px;background:none;font:inherit;font-size:.8rem;font-weight:600;color:var(--muted);cursor:pointer;white-space:nowrap}
  .ktab span{min-width:20px;height:18px;padding:0 6px;border-radius:999px;background:rgba(36,26,20,.07);font-size:.68rem;display:grid;place-items:center;color:var(--ink)}
  .ktab.warn span{background:var(--amber-soft);color:#8A6212}
  .ktab:hover{color:var(--ink)}
  .ktab[aria-selected="true"]{background:var(--panel);color:var(--ink);box-shadow:0 2px 6px -2px rgba(36,26,20,.25)}
  .kfil{display:flex!important;flex-wrap:wrap;gap:8px;align-items:center;margin-bottom:12px}
  .kfil select.text{width:auto;min-width:0;height:38px;font-size:.84rem;flex:0 1 auto}
  .kfil label.kq{display:flex!important;flex-direction:row;font-size:inherit}
  .kq{flex:1 1 260px;display:flex;align-items:center;gap:8px;height:38px;padding:0 12px;border-radius:11px;border:1px solid var(--line-2);background:var(--panel)}
  .kq:focus-within{border-color:var(--rose);box-shadow:0 0 0 3px rgba(232,93,117,.14)}
  .kq svg{width:16px;height:16px;fill:none;stroke:var(--muted);stroke-width:1.8}
  .kq input{border:0;outline:0;background:none;flex:1;font:inherit;font-size:.86rem;height:auto!important;padding:0;color:var(--ink)}
  .kd__top{display:flex;align-items:center;gap:6px}
  .kd__top .spacer{flex:1}
  .kdet h2{margin:12px 0 12px}
  .kstatus{display:flex;align-items:center;gap:12px;padding:12px 14px;border-radius:12px;border:1px solid var(--line);background:var(--bg-soft);margin-bottom:16px}
  .kstatus > div{flex:1;min-width:0}
  .kstatus b{display:block;font-size:.88rem}
  .kstatus span{font-size:.8rem;color:var(--muted)}
  .kstatus__dot{width:10px;height:10px;border-radius:50%;background:#8C817B;flex:none}
  .kstatus.ok{background:#F2F7EC;border-color:#DCE8CE}.kstatus.ok .kstatus__dot{background:var(--success)}
  .kstatus.drf{background:rgba(62,111,166,.06);border-color:rgba(62,111,166,.2)}.kstatus.drf .kstatus__dot{background:var(--info)}
  .kstatus.rev{background:#FBF1E4;border-color:#F0DCC0}.kstatus.rev .kstatus__dot{background:#C98A2E}
  .kd__lbl{margin:0 0 6px;font-size:.66rem;font-weight:800;letter-spacing:.12em;text-transform:uppercase;color:var(--muted)}
  .kdet__body{margin-bottom:18px}
  .ksrcs{display:grid;gap:6px;margin-bottom:18px}
  .ksrc2{display:grid;grid-template-columns:18px minmax(0,1fr) auto;gap:10px;align-items:start;padding:10px 12px;border:1px solid var(--line);border-radius:10px;color:inherit;text-decoration:none}
  .ksrc2:hover{border-color:rgba(232,93,117,.4);text-decoration:none}
  .ksrc2.is-warn{border-color:rgba(217,154,43,.5);background:rgba(217,154,43,.06)}
  .ksrc2 svg{width:16px;height:16px;fill:none;stroke:var(--muted);stroke-width:1.8;margin-top:2px}
  .ksrc2 b{font-size:.84rem;margin-right:6px}
  .ksrc2 em{font-style:normal;font-size:.76rem;color:var(--muted)}
  .ksrc2 q{display:block;margin-top:3px;font-size:.8rem;color:var(--ink);quotes:"“" "”"}
  .ksrc2 .go{color:var(--muted)}
  .khist{list-style:none;margin:0 0 16px;padding:0 0 0 14px;border-left:2px solid var(--line);display:grid;gap:10px}
  .khist li{position:relative;display:grid;grid-template-columns:minmax(0,1fr) auto;gap:2px 10px;font-size:.82rem}
  .khist li::before{content:"";position:absolute;left:-20px;top:4px;width:10px;height:10px;border-radius:50%;background:var(--panel);border:2px solid var(--rose)}
  .khist span{grid-column:1;color:var(--muted);font-size:.76rem}
  .khist time{grid-row:1;grid-column:2;color:var(--muted);font-size:.74rem}
  .kd__note{display:flex;align-items:center;gap:8px;margin:0;padding-top:12px;border-top:1px solid var(--line);font-size:.76rem;color:var(--muted)}
  .kd__note svg{width:14px;height:14px;fill:none;stroke:currentColor;stroke-width:1.9}
  .kover{margin-top:24px}
  .kover__h{margin-bottom:10px}
""",
  body=r"""
    <div class="head">
      <div>
        <p class="label">Company knowledge</p>
        <h1>Knowledge</h1>
        <p>Every approved answer, with where it came from and who approved it. Search it, or pick a topic.</p>
      </div>
      <span class="spacer"></span>
      <button class="btn btn--secondary btn--sm fsbtn" id="fsBtn" type="button" aria-pressed="false" title="Full screen (F)"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M15 3h6v6M9 21H3v-6M21 3l-7 7M3 21l7-7"/></svg><span>Full screen</span></button>
    </div>

    <a class="rocard" href="readout.html" data-admin-only>
      <span class="rocard__ic">📋</span>
      <span class="rocard__t"><small>Week 4 · Admin only</small><b>Your readout is ready</b><span>What four weeks produced, and your decision to continue.</span></span>
      <span class="rocard__go">Open readout →</span>
    </a>
    <section class="ksec" aria-labelledby="kH"><div class="ksec__h"><h2 id="kH">Your knowledge</h2><span>· What Oslo has in lojo right now</span></div><div class="kstats" id="kstats"></div></section>

    <section class="klib" aria-labelledby="libH">
    <div class="klib__h"><h2 id="libH">Library</h2><div class="ktabs" id="ktabs" role="tablist" aria-label="State"></div></div>
    <div class="kfil">
      <label class="kq"><svg viewBox="0 0 24 24"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></svg><input id="kq" placeholder="Search questions and answers" aria-label="Search"></label>
      <select class="text" id="fSpace" aria-label="Knowledge space"></select>
      <select class="text" id="fType" aria-label="Source type"></select>
      <select class="text" id="fTopic" aria-label="Topic"></select>
      <select id="fState" hidden></select><select id="fConn" hidden></select>
    </div>
    <div class="kb">
      <section class="card klist"><div class="klist__h" id="kcount"></div><ul id="klist"></ul></section>
      <section class="card kdet" id="kdet" aria-live="polite"></section>
    </div>
    </section>

    <section class="kover" aria-labelledby="ovH"><h2 id="ovH" class="kover__h">Overview</h2>
    <div class="kgrid">
      <section class="kbox"><h3><svg viewBox="0 0 24 24"><path d="M12 3 4 6v6c0 4.5 3.4 8.3 8 9 4.6-.7 8-4.5 8-9V6z"/><path d="m9 12 2 2 4-4"/></svg>Where it comes from</h3><div id="ktypes"></div><p class="sub2">Sensitivity</p><div id="ksens"></div></section>
      <section class="kbox"><h3><svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg>Recently updated</h3><p>Newest first.</p><div id="kspark" hidden></div><ul class="recent" id="krecent"></ul></section>
    </div>
    </section>
""",
  js=r"""
// full screen, as in Build and Insights: F toggles, Esc leaves
function setFs(on) {
  document.body.classList.toggle('is-fs', on); $('fsBtn').setAttribute('aria-pressed', on);
  $('fsBtn').querySelector('span').textContent = on ? 'Exit full screen' : 'Full screen';
  $('fsBtn').querySelector('svg').innerHTML = on ? '<path d="M4 14h6v6M20 10h-6V4M14 10l7-7M3 21l7-7"/>' : '<path d="M15 3h6v6M9 21H3v-6M21 3l-7 7M3 21l7-7"/>';
  try { sessionStorage.setItem('lojo-kn-fs', on ? '1' : ''); } catch (err) {}
}
$('fsBtn').addEventListener('click', () => setFs(!document.body.classList.contains('is-fs')));
try { if (sessionStorage.getItem('lojo-kn-fs')) setFs(true); } catch (err) {}
document.addEventListener('keydown', (e) => {
  if (e.target.closest('input,textarea,select') || e.metaKey || e.ctrlKey || document.querySelector('dialog[open]')) return;
  if (e.key.toLowerCase() === 'f') setFs(!document.body.classList.contains('is-fs'));
  if (e.key === 'Escape' && document.body.classList.contains('is-fs')) setFs(false);
});

// every piece of company knowledge: drafts with their state, plus reference passages saved from sources
const IC = {
  layers: '<svg viewBox="0 0 24 24"><path d="M12 3 2 8l10 5 10-5z"/><path d="m2 13 10 5 10-5"/></svg>',
  shield: '<svg viewBox="0 0 24 24"><path d="M12 3 4 6v6c0 4.5 3.4 8.3 8 9 4.6-.7 8-4.5 8-9V6z"/></svg>',
  doc: '<svg viewBox="0 0 24 24"><path d="M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8z"/><path d="M14 3v5h5"/></svg>',
};
const TOPICS = { sso: 'Sign-in & SSO', refund: 'Refunds', plan: 'Plans & pricing', upgrade: 'Plan changes', pay: 'Payments & billing', api: 'API', chargeback: 'Disputes', security: 'Security', storage: 'Data & hosting', export: 'Data export', onboarding: 'Onboarding', annual: 'Renewals', contact: 'Support' };
const SPACE = (docId) => ({ d7: 'Security', d8: 'Product', d3: 'Product' })[docId] || 'General';
const TYPE = (docId) => docId === 'd5' ? 'Call notes' : docById(docId).faq ? 'Help pages' : docById(docId).name.endsWith('.md') ? 'Markdown' : docById(docId).name.split('.').pop().toUpperCase();
const CONN = (docId) => docById(docId).faq ? 'Website' : 'Upload';
const DAY = ['Sep 9, 2026', 'Sep 10, 2026', 'Sep 28, 2026', 'Sep 29, 2026', 'Oct 2, 2026', 'Oct 5, 2026'];
ST.archived = ST.archived || {};
function entries() {
  const out = [];
  DRAFTS.forEach((r, i) => {
    const d = decision(r), q = allQuestions().find(x => x.id === r.qid), s = d.status;
    const state = s === 'approved' ? 'Published' : (s === 'final' || r.conflict) ? 'Needs review' : 'Draft';
    const doc = r.src[0][0];
    out.push({ id: r.id, kind: 'answer', state, title: q.q, body: answerOf(r), src: r.src, space: SPACE(doc), type: TYPE(doc), conn: CONN(doc),
      topic: (conceptsOf(q.q)[0] || 'contact'), sens: 'Internal', at: s === 'approved' ? DAY[3 + i % 3] : DAY[i % 2], by: d.by || (s === 'approved' ? 'Eric Ouisse' : '') });
  });
  const seen = new Set();
  DRAFTS.concat(GAPS.map(g => ({ src: g.where }))).forEach(r => r.src.forEach(([doc, loc, text], i) => {
    const k = doc + loc; if (seen.has(k)) return; seen.add(k);
    out.push({ id: 'ref-' + k.replace(/\W/g, ''), kind: 'ref', state: 'Reference', title: docShort(doc) + ' · ' + loc, body: text, src: [[doc, loc, text]], space: SPACE(doc), type: TYPE(doc), conn: CONN(doc),
      topic: conceptsOf(text)[0] || 'contact', sens: 'Internal', at: DAY[seen.size % 2], by: '' });
  }));
  return out.filter(e => !ST.archived[e.id]);
}
const stateChip = (s) => '<span class="kc ' + STATE_UI[s][1] + '">' + STATE_UI[s][0] + '</span>';
let sel = null, ktab = new URLSearchParams(location.search).get('state') || 'answers';
// Viewers read only what's live in Ask lojo: no other states, no export
const KVIEW = window.LOJO_ROLE === 'viewer';
if (KVIEW) { ktab = 'Published'; document.body.classList.add('kview'); }
// plain-language states
const STATE_UI = { Published: ['Live in Ask lojo', 'pub'], Draft: ['Waiting for approval', 'drf'], 'Needs review': ['Needs review', 'rev'], Reference: ['Reference', ''] };
const TABS = [['answers', 'All answers'], ['Published', 'Live in Ask lojo'], ['Draft', 'Waiting for approval']];
const uniq = (arr) => [...new Set(arr)];
function opts(id, label, vals) { const keep = $(id).value; $(id).innerHTML = '<option value="">' + label + '</option>' + vals.map(v => '<option value="' + esc(v) + '">' + esc(id === 'fTopic' ? TOPICS[v] || v : v) + '</option>').join(''); $(id).value = vals.includes(keep) ? keep : ''; }
function filtered(all) {
  const q = $('kq').value.trim().toLowerCase();
  return all.filter(e => (!q || (e.title + ' ' + e.body).toLowerCase().includes(q)) && (!$('fSpace').value || e.space === $('fSpace').value) && (ktab === 'answers' ? e.kind === 'answer' : e.state === ktab) &&
    (!$('fType').value || e.type === $('fType').value) && (!$('fConn').value || e.conn === $('fConn').value) && (!$('fTopic').value || e.topic === $('fTopic').value));
}
function render() {
  const all = entries(), n = (s) => all.filter(e => e.state === s).length;
  const pubPct = all.filter(e => e.kind === 'answer').length ? Math.round(n('Published') / all.filter(e => e.kind === 'answer').length * 100) : 0;
  const tile = (c, l, tipT, v, sub, tag, tab) => '<a class="kt kt--' + c + '"' + (tab ? ' href="#libH" data-tab="' + tab + '"' : '') + '>' + (tag ? '<span class="kt__tag">' + tag + '</span>' : '') +
    '<small>' + l + ' <i class="tip" tabindex="0" data-tip="' + esc(tipT) + '">i</i></small><b>' + v + '</b><span class="kt__sub">' + sub + '</span></a>';
  $('kstats').innerHTML =
    tile('all', 'Knowledge entries', 'Everything lojo holds for this workspace: answers and the reference passages behind them.', all.length, all.filter(e => e.kind === 'answer').length + ' answers · ' + n('Reference') + ' reference') +
    tile('ok', 'Published', 'Approved by a person, then published as company truth. Ask lojo answers from these.', n('Published'), pubPct + '% of answers', 'Live', 'Published') +
    tile('warn', 'Needs review', 'Conflicting or rejected. Not company truth until a person reviews it.', n('Needs review'), n('Draft') + ' more drafts waiting', n('Needs review') ? 'Needs you' : '', 'Needs review') +
    tile('ref', 'Reference', 'Saved from an authorised source. Never published on its own.', n('Reference'), 'Passages kept as evidence', '', 'Reference') +
    '<div class="kt kt--sp" tabindex="0"><small>Knowledge spaces <i class="tip" tabindex="0" data-tip="Access is decided per space. A space you can’t read is never listed here.">i</i></small><b id="kspN"></b><span class="kt__sub">Hover to see all</span><div class="kpop" id="kspaces"></div></div>';
  const count = (key) => uniq(all.map(e => e[key])).map(v => [v, all.filter(e => e[key] === v).length]);
  const pills = (key, sel) => count(key).map(([v, c]) => '<button type="button" class="kpill" data-pick="' + sel + '" data-v="' + esc(v) + '">' + esc(v) + ' <b>' + c + '</b></button>').join('');
  // spaces: a donut with a clickable legend
  const COLS = ['#E85D75', '#3E6FA6', '#C9A24A', '#3F8F5F', '#8C6FD8', '#8C817B'];
  const sp = count('space').sort((a, b) => b[1] - a[1]), tot = all.length, R0 = 34, C0 = 2 * Math.PI * R0;
  let off = 0;
  $('kspN').textContent = sp.length;
  $('kspaces').innerHTML = '<p class="kpop__h">' + sp.length + ' spaces · ' + tot + ' entries</p><div class="donut"><svg viewBox="0 0 90 90"><circle cx="45" cy="45" r="' + R0 + '" fill="none" stroke="var(--bg-soft)" stroke-width="12"/>' +
    sp.map(([v, n], i) => { const len = C0 * n / tot, s = '<circle cx="45" cy="45" r="' + R0 + '" fill="none" stroke="' + COLS[i % 6] + '" stroke-width="12" stroke-dasharray="' + (len - 1.5).toFixed(1) + ' ' + C0.toFixed(1) + '" stroke-dashoffset="' + (-off).toFixed(1) + '" transform="rotate(-90 45 45)"><title>' + esc(v) + ': ' + n + '</title></circle>'; off += len; return s; }).join('') +
    '<text x="45" y="43" text-anchor="middle" class="dn__n">' + tot + '</text><text x="45" y="56" text-anchor="middle" class="dn__l">entries</text></svg>' +
    '<ul class="legend">' + sp.map(([v, n], i) => '<li><button type="button" data-pick="fSpace" data-v="' + esc(v) + '"><i style="background:' + COLS[i % 6] + '"></i>' + esc(v) + '<b>' + n + '</b><em>' + Math.round(n / tot * 100) + '%</em></button></li>').join('') + '</ul></div>';
  // source types: horizontal bars
  const ty = count('type').sort((a, b) => b[1] - a[1]), mx = Math.max(...ty.map(x => x[1]));
  $('ktypes').innerHTML = '<div class="hbars">' + ty.map(([v, n]) => '<button type="button" class="hb" data-pick="fType" data-v="' + esc(v) + '"><span class="hb__l">' + esc(v) + '</span><span class="hb__t"><i style="width:' + (n / mx * 100).toFixed(0) + '%"></i></span><b>' + n + '</b></button>').join('') + '</div>';
  const se = count('sens');
  $('ksens').innerHTML = '<div class="stackbar">' + se.map(([v, n], i) => '<i style="flex:' + n + ';background:' + ['#8C817B', '#E85D75', '#C9A24A'][i % 3] + '" title="' + esc(v) + ': ' + n + '"></i>').join('') + '</div><p class="stackl">' + se.map(([v, n]) => esc(v) + ' · ' + n).join('   ') + '</p>';
  // recently updated: updates per day, then the newest five
  const ans = all.filter(e => e.kind === 'answer'), days = [...new Set(ans.map(e => e.at))].sort((a, b) => Date.parse(a) - Date.parse(b)), per = days.map(d => ans.filter(e => e.at === d).length), pm = Math.max(...per);
  $('kspark').innerHTML = days.map((d, i) => '<span class="sp__c" title="' + d + ': ' + per[i] + ' updated"><i style="height:' + Math.max(8, per[i] / pm * 100).toFixed(0) + '%"></i><em>' + d.replace(/, \d{4}$/, '').replace(/^(\w{3}) /, '$1 ') + '</em></span>').join('');
  $('krecent').innerHTML = ans.sort((a, b) => Date.parse(b.at) - Date.parse(a.at)).slice(0, 5).map(e => '<li><button type="button" data-open="' + e.id + '">' + esc(e.title) + '</button><time>' + e.at.replace(/, \d{4}$/, '') + '</time></li>').join('');
  opts('fSpace', 'All spaces', uniq(all.map(e => e.space))); opts('fState', 'Any state', ['Published', 'Needs review', 'Draft', 'Reference']);
  opts('fType', 'All source types', uniq(all.map(e => e.type))); opts('fConn', 'All connected sources', uniq(all.map(e => e.conn))); opts('fTopic', 'All topics', uniq(all.map(e => e.topic)));
  $('ktabs').innerHTML = TABS.map(([k, l]) => { const c = k === 'answers' ? all.filter(e => e.kind === 'answer').length : n(k);
    return '<button type="button" role="tab" class="ktab' + (k === 'Needs review' && c ? ' warn' : '') + '" data-tab="' + k + '" aria-selected="' + (ktab === k) + '">' + l + ' <span>' + c + '</span></button>'; }).join('');
  const list = filtered(all);
  if (!list.some(e => e.id === sel)) sel = list.length ? list[0].id : null;
  $('kcount').textContent = list.length + (ktab === 'Reference' ? ' passage' : ' answer') + (list.length === 1 ? '' : 's') + (TABS.find(x => x[0] === ktab) && ktab !== 'answers' ? ' · ' + TABS.find(x => x[0] === ktab)[1].toLowerCase() : '');
  $('klist').innerHTML = list.length ? list.map(e => '<li class="kitem' + (e.id === sel ? ' is-sel' : '') + '" data-id="' + e.id + '"><div class="chipsrow">' + stateChip(e.state) + '<span class="kc sp">' + IC.layers + esc(e.space) + '</span><span class="kc">' + IC.shield + e.sens + '</span></div>' +
    '<b>' + esc(e.title) + '</b><span class="ex">' + esc(e.body.replace(/[#*_>-]/g, '')) + '</span><span class="ksrc">' + IC.doc + esc(e.type) + ' · ' + esc(docShort(e.src[0][0])) + '</span><span class="ft">' + e.src.length + ' source' + (e.src.length === 1 ? '' : 's') + ' · Updated ' + e.at + '</span></li>').join('')
    : '<li class="kempty">Nothing matches these filters.</li>';
  detail(all.find(e => e.id === sel));
}
function detail(e) {
  if (!e) { $('kdet').innerHTML = '<div class="kempty">Nothing here yet. Try another tab or filter.</div>'; return; }
  const S = {
    Published: ['ok', 'Live in Ask lojo', 'Approved by ' + (e.by || 'a person') + '. Ask lojo answers from it.', '<a class="btn btn--secondary btn--sm" href="build.html?sel=' + e.id + '&edit=1">Edit answer</a>'],
    Draft: ['drf', 'Waiting for approval', 'lojo drafted it with sources. It isn’t used anywhere until a person approves it.', '<a class="btn btn--primary btn--sm" href="build.html?sel=' + e.id + '">Review in Build</a>'],
    'Needs review': ['rev', 'Needs review', 'Its sources disagree, or it was rejected. It isn’t company truth until a person resolves it.', '<a class="btn btn--primary btn--sm" href="build.html?sel=' + e.id + '">Resolve in Build</a>'],
    Reference: ['ref', 'Reference passage', 'A passage saved from a source. It backs up answers and is never shown on its own.', ''],
  }[e.state];
  const hist = e.kind === 'answer' ? [['Drafted by lojo', 'from ' + e.src.length + ' source' + (e.src.length === 1 ? '' : 's'), DAY[0]]]
    .concat(e.state === 'Needs review' ? [['Flagged for review', 'sources disagree', e.at]] : [])
    .concat(e.state === 'Published' ? [['Approved by ' + (e.by || 'Eric Ouisse'), 'now live in Ask lojo', e.at]] : [])
    .concat(e.state === 'Draft' ? [['Waiting for a person', 'in Build', 'now']] : []) : [['Saved from ' + docShort(e.src[0][0]), e.src[0][1], e.at]];
  $('kdet').innerHTML =
    '<div class="kd__top"><div class="chipsrow"><span class="kc sp">' + IC.layers + esc(e.space) + '</span><span class="kc">' + IC.shield + e.sens + '</span><span class="kc">' + esc(TOPICS[e.topic] || e.topic) + '</span></div>' +
      '<span class="spacer"></span>' + (e.kind === 'answer' ? '<button class="hbtn" type="button" data-askq="' + esc(e.title) + '" title="Ask lojo" aria-label="Ask lojo"><svg viewBox="0 0 24 24"><path d="M21 11.5a8.5 8.5 0 0 1-12.4 7.6L3 21l1.9-5.6A8.5 8.5 0 1 1 21 11.5z"/></svg></button>' : '') +
      '<button class="hbtn" type="button" data-arch="' + e.id + '" title="Archive" aria-label="Archive"><svg viewBox="0 0 24 24"><rect x="3" y="4" width="18" height="4" rx="1"/><path d="M5 8v11a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1V8M10 12h4"/></svg></button></div>' +
    '<h2>' + esc(e.title) + '</h2>' +
    '<div class="kstatus ' + S[0] + '"><span class="kstatus__dot"></span><div><b>' + S[1] + '</b><span>' + S[2] + '</span></div>' + S[3] + '</div>' +
    '<p class="kd__lbl">' + (e.kind === 'answer' ? 'Answer' : 'Passage') + '</p><div class="kdet__body">' + md(e.body) + '</div>' +
    '<p class="kd__lbl">Where it came from</p><div class="ksrcs">' + e.src.map(([d, loc, text]) => '<a class="ksrc2' + (e.state === 'Needs review' && /months? old/.test(loc) ? ' is-warn' : '') + '" href="sources.html?doc=' + d + '&loc=' + encodeURIComponent(loc) + '">' + IC.doc +
      '<span><b>' + esc(docShort(d)) + '</b><em>' + esc(loc) + '</em>' + (text ? '<q>' + esc(text) + '</q>' : '') + '</span><span class="go">↗</span></a>').join('') + '</div>' +
    '<p class="kd__lbl">History</p><ol class="khist">' + hist.map(([a, b, c]) => '<li><b>' + esc(a) + '</b><span>' + esc(b) + '</span><time>' + esc(c) + '</time></li>').join('') + '</ol>' +
    '<p class="kd__note">' + IC.shield + 'lojo proposes. A person approves. Only then does an answer become company truth.</p>';
}
$('kstats').addEventListener('click', (ev) => { const a = ev.target.closest('a.kt[data-tab]'); if (!a || ev.target.closest('.tip')) return; ev.preventDefault(); ktab = a.dataset.tab; sel = null; render(); document.querySelector('.klib').scrollIntoView({ behavior: 'smooth', block: 'start' }); });
$('klist').addEventListener('click', (ev) => { const li = ev.target.closest('[data-id]'); if (li) { sel = li.dataset.id; render(); } });
document.querySelector('.kgrid').addEventListener('click', (ev) => {
  const p = ev.target.closest('[data-pick]'); if (p) { $(p.dataset.pick).value = $(p.dataset.pick).value === p.dataset.v ? '' : p.dataset.v; render(); document.querySelector('.kfil').scrollIntoView({ behavior: 'smooth', block: 'start' }); }
  const o = ev.target.closest('[data-open]'); if (o) { ['kq', 'fSpace', 'fType', 'fTopic'].forEach(id => { $(id).value = ''; }); ktab = 'answers'; sel = o.dataset.open; render(); document.querySelector('.kb').scrollIntoView({ behavior: 'smooth', block: 'start' }); }
});
$('kdet').addEventListener('click', (ev) => {
  const a = ev.target.closest('[data-arch]'); if (a) { ST.archived[a.dataset.arch] = true; save(); sel = null; render(); toast('Archived. It no longer appears in Knowledge.'); }
  const q = ev.target.closest('[data-askq]'); if (q && window.__askQ) window.__askQ(q.dataset.askq);
});
['kq', 'fSpace', 'fType', 'fTopic'].forEach(id => $(id).addEventListener('input', render));
$('ktabs').addEventListener('click', (ev) => { const b = ev.target.closest('[data-tab]'); if (!b) return; ktab = b.dataset.tab; sel = null; render(); });
render();
""")


STATES = dict(
  active='states', title='Design use cases',
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
        <h1>Design use cases</h1>
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
    ['G26', 'Forgot your password?', 'Ask for a reset link, then a “Check your email” page with a resend timer.', [L('auth.html?s=forgot', 'Forgot'), L('auth.html?s=sent&email=eric@oslo.com', 'Check your email')]],
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
    ['G14', 'Rewritten more than once', '“Rewritten 2 times” badge and the earlier drafts with their reasons.', [L('build.html?sel=r8', 'Open')]],
  ]],
  ['Ask lojo', [
    ['G29', 'Small talk', '“Hi” and “Thanks” get a short reply with no sources.', [L('chat.html?say=Hi|Thanks', 'Open')]],
    ['G30', 'Formatted answers', 'Headings, lists and bold, sized to the bubble.', [L('chat.html?say=How fast can we call the API?', 'Open')]],
  ]],
  ['Activity', [
    ['D113', 'Models and hosting', 'Where text goes, drawn as a boundary around lojo’s servers; hover a model for its facts. Admins see models on each agent; Editors get one plain sentence.', [L('activity.html', 'All self-hosted'), L('activity.html?models=vendor', 'Third-party'), L('activity.html?models=unknown', 'Not known'), L('activity.html?models=vendor#list', 'List view'), L('activity.html?as=editor', 'As Editor'), L('activity.html?as=editor&models=vendor', 'As Editor, third-party'), L('activity.html?as=admin', 'Back to Admin')]],
  ]],
  ['Distribute', [
    ['—', 'Distribute page', 'Approved answers plus where they go: the Ask lojo page and button live, help centre and Slack in the full build.', [L('distribute.html', 'Open')]],
  ]],
  ['Knowledge', [
    ['—', 'Knowledge', 'Every entry with its state, provenance and governance; filter by space, state, source and topic.', [L('knowledge.html', 'Open knowledge')]],
  ]],
  ['Emails', [
    ['E1', 'Company admin invitation', 'From the super admin. The future Admin sets up the company.', [L('emails.html#admin-invite', 'Open')]],
    ['E2', 'Teammate invitation', 'From an Admin, with each workspace and role.', [L('emails.html#team-invite', 'Open')]],
    ['E3', 'Confirm your email', 'First sign-in with email.', [L('emails.html#verify', 'Open')]],
    ['E4', 'Reset password', 'From “Forgot password?” on sign-in.', [L('emails.html#reset', 'Open')]],
    ['E5', 'Your role changed', 'When an Admin changes someone’s role.', [L('emails.html#role', 'Open')]],
    ['E6', 'Removed from a workspace', 'When an Admin removes someone.', [L('emails.html#removed', 'Open')]],
    ['E7', 'Workspace deleted', 'To everyone in a deleted workspace.', [L('emails.html#deleted', 'Open')]],
    ['E8', 'Drafts waiting', 'A new batch lands in Build. Admins and Editors.', [L('emails.html#drafts', 'Open')]],
    ['E9', 'Friday review reminder', 'How many of the week’s drafts are done.', [L('emails.html#weekly', 'Open')]],
    ['E10', 'New gaps found', 'Things the documents mention but never explain.', [L('emails.html#gaps', 'Open')]],
    ['E11', 'Ask lojo declined a question', 'Nothing approved answers it yet.', [L('emails.html#declined', 'Open')]],
    ['E12', 'Admin accepted', 'To super admins when a company becomes active.', [L('emails.html#accepted', 'Open')]],
    ['E13', 'Invitation about to expire', 'To super admins, 4 hours before the link runs out.', [L('emails.html#expiring', 'Open')]],
    ['E14', 'Weekly platform summary', 'To super admins, counts only.', [L('emails.html#summary', 'Open')]],
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

# ============================================================ PEOPLE + COMPANIES
# shared by the admin's People page and the super admin's Companies page
ADMIN_CSS = r"""
  .roster{display:grid;gap:8px}
  .rrow2{display:grid;align-items:center;gap:6px 18px;padding:14px 16px;border:1px solid var(--line);border-radius:14px;background:var(--panel);transition:border-color .15s ease,box-shadow .15s ease}
  .rrow2.is-click{cursor:pointer}
  .rrow2.is-click:hover{border-color:rgba(36,26,20,.24);box-shadow:0 10px 24px -20px rgba(36,26,20,.5)}
  .rhead{display:grid;gap:18px;padding:0 16px 8px;font-size:.66rem;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--muted)}
  .who{display:flex;align-items:center;gap:12px;min-width:0}
  .who .av{width:40px;height:40px;border-radius:12px;flex:none;display:grid;place-items:center;color:#fff;font-family:var(--display);font-weight:800;font-size:.82rem;background:var(--brand-gradient)}
  .who .av.c1{background:linear-gradient(135deg,#E85D75,#FFB199)}
  .who .av.c2{background:linear-gradient(135deg,#7B5CF0,#C4AEFF)}
  .who .av.c3{background:linear-gradient(135deg,#E39A12,#FFD978)}
  .who .av.c4{background:linear-gradient(135deg,#3F8F5F,#9ED8B0)}
  .who .av.is-pending{background:var(--bg-soft);color:var(--muted);border:1.5px dashed var(--line-2)}
  .who b{display:flex;align-items:center;gap:4px 8px;flex-wrap:wrap;font-size:.92rem;line-height:1.3}
  .who span{display:block;color:var(--muted);font-size:.8rem;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
  .who > div{min-width:0}
  .cell b{display:block;font-size:.88rem;font-weight:600}
  .cell span{display:block;color:var(--muted);font-size:.8rem}
  .num{font-family:var(--display);font-weight:700;font-size:1.1rem}
  .num.is-none{color:var(--muted);font-weight:500}
  .wsl{display:flex;flex-wrap:wrap;gap:6px}
  .wsc{display:inline-flex;align-items:center;gap:5px;height:26px;padding:0 10px;border-radius:999px;border:1px solid var(--line-2);font-size:.76rem;font-weight:600;white-space:nowrap}
  .wsc em{font-style:normal;color:var(--muted);font-weight:500}
  .rstat{display:flex;align-items:center;justify-content:flex-end;gap:8px;flex-wrap:wrap}
  .rstat .btn{height:30px;padding:0 12px;font-size:.76rem}
  .empty2{padding:28px 16px;text-align:center;color:var(--muted);border:1.5px dashed var(--line-2);border-radius:14px}
  .empty2 b{display:block;color:var(--ink);margin-bottom:4px}
  /* forms in dialogs and the invite drawer */
  .fgrid{display:grid;grid-template-columns:1fr 1fr;gap:14px}
  .fld{display:grid;gap:6px}
  .fld label{font-size:.82rem;font-weight:600;margin:0}
  .fld .text.is-bad{border-color:var(--error)}
  .ferr{font-size:.78rem;color:var(--error);min-height:0}
  .fhint{font-size:.78rem;color:var(--muted)}
  .fnote{display:flex;gap:10px;padding:10px 12px;border-radius:10px;background:var(--amber-soft);color:#8A6212;font-size:.82rem}
  .dlg--wide{width:min(560px,calc(100vw - 32px))}
  .dlg .label{margin-bottom:6px}
  .drawer{margin:12px 12px 12px auto;height:calc(100vh - 24px);max-height:none;width:min(480px,calc(100vw - 24px));flex-direction:column}
  .drawer[open]{display:flex}
  .drawer .dlg__b{flex:1;overflow:auto;display:grid;gap:18px;align-content:start}
  .drawer .dlg__f{border-radius:0 0 18px 18px}
  .drawer h3{margin:0}
  .dx{width:34px;height:34px;border-radius:50%;border:0;background:var(--bg-soft);color:var(--muted);font-size:1.1rem;cursor:pointer;flex:none}
  .dx:hover{color:var(--ink)}
  .dtop{display:flex;align-items:center;gap:12px}
  .dtop .spacer{flex:1}
  .wsp{display:grid;gap:8px}
  .wso{display:flex;align-items:center;gap:12px;padding:12px 14px;border:1px solid var(--line);border-radius:12px;background:var(--panel);transition:border-color .15s ease,background-color .15s ease}
  .wso.is-on{border-color:#FFB199;background:#FFF6F3}
  .wso input{width:18px;height:18px;margin:0;accent-color:var(--rose);flex:none;cursor:pointer}
  .wso .n{flex:1;min-width:0;cursor:pointer}
  .wso .n b{display:block;font-size:.9rem}
  .wso .n span{display:block;color:var(--muted);font-size:.78rem}
  .rseg{display:inline-flex;padding:3px;border-radius:999px;background:var(--bg-soft);gap:2px}
  .rseg button{height:28px;padding:0 11px;border:0;border-radius:999px;background:none;font-size:.76rem;font-weight:600;color:var(--muted);cursor:pointer}
  .rseg button[aria-pressed="true"]{background:var(--panel);color:var(--ink);box-shadow:0 1px 3px rgba(36,26,20,.15)}
  .rseg button:disabled{cursor:default;opacity:.45}
  .rhelp{margin:0;color:var(--muted);font-size:.78rem}
  .rhelp b{color:var(--ink);font-weight:600}
  .mail{padding:16px 18px;border-radius:14px;background:var(--bg-soft);display:grid;gap:10px}
  .mail b{font-family:var(--display);font-size:1.02rem;line-height:1.3}
  .mail p{margin:0;color:var(--muted);font-size:.82rem}
  .kv{display:grid;grid-template-columns:120px 1fr;gap:10px 14px;font-size:.86rem;margin:4px 0 16px}
  .kv dt{color:var(--muted)}
  .kv dd{margin:0;font-weight:600}
  .lock{display:flex;gap:10px;padding:10px 12px;border-radius:10px;background:var(--bg-soft);color:var(--muted);font-size:.8rem}
  :root[data-theme="dark"] .wso.is-on{background:rgba(255,177,153,.08)}
  :root[data-theme="dark"] .fnote{background:rgba(201,162,74,.14);color:#E9CF8E}
  @media (max-width:860px){ .rhead{display:none} .rrow2{grid-template-columns:1fr!important} .rstat{justify-content:flex-start} .fgrid{grid-template-columns:1fr} }
"""
ADMIN_JS = r"""
// what each fixed role can do
const CAPS = [
  ['Ask lojo and read Knowledge', 1, 1, 1], ['Add and remove sources', 1, 1, 0], ['Decide which questions matter', 1, 1, 0],
  ['Approve, edit and reject drafts', 1, 1, 0], ['Export approved answers', 1, 1, 0], ['Change workspace settings', 1, 0, 0],
  ['Invite people and change roles', 1, 0, 0], ['Delete the workspace', 1, 0, 0],
];
const admins = (wsId) => ST.people.filter(p => p.ws[wsId] === 'admin' && p.status === 'member');
function roleLog(msg) { ST.roleLog = ST.roleLog || []; ST.roleLog.unshift({ msg, by: 'Eric Ouisse', at: new Date().toLocaleString('en-GB', { day: 'numeric', month: 'short', hour: '2-digit', minute: '2-digit' }) }); ST.roleLog = ST.roleLog.slice(0, 8); }
// change one person's role in one workspace; null removes access. Returns an error or ''.
function setRole(person, wsId, role) {
  const was = person.ws[wsId];
  if (was === role) return '';
  if (was === 'admin' && person.status === 'member' && admins(wsId).length === 1) return 'Every workspace needs at least one Admin. Make someone else Admin first.';
  const wn = (ST.workspaces.find(w => w.id === wsId) || {}).name;
  if (role) person.ws[wsId] = role; else delete person.ws[wsId];
  roleLog(role ? person.name + ' is now ' + ROLES[role][0] + ' in ' + wn + (was ? ' (was ' + ROLES[was][0] + ')' : '') : person.name + ' removed from ' + wn);
  return '';
}
// a small confirm dialog in the design system; resolves true or false
function confirmDlg(title, body, go, danger) {
  return new Promise((res) => {
    let d = $('cfDlg'); if (!d) { d = document.createElement('dialog'); d.id = 'cfDlg'; d.className = 'dlg'; document.body.appendChild(d); }
    d.innerHTML = '<div class="dlg__b"><h3>' + title + '</h3><p>' + body + '</p></div><div class="dlg__f"><button class="btn btn--secondary" type="button" data-cf="0">Cancel</button><button class="btn ' + (danger ? 'btn--danger' : 'btn--primary') + '" type="button" data-cf="1">' + go + '</button></div>';
    d.onclick = (e) => { const b = e.target.closest('[data-cf]'); if (b || e.target === d) { d.close(); res(!!(b && b.dataset.cf === '1')); } };
    d.oncancel = () => res(false);
    d.showModal(); d.querySelector('[data-cf="1"]').focus();
  });
}
const ini = (n) => n.split(/\s+/).map(w => w[0]).join('').slice(0, 2).toUpperCase();
const validEmail = (v) => /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(v);
const domainOf = (v) => (v.split('@')[1] || '').toLowerCase();
// a field's error under it; returns false when there is one
function fieldErr(input, msg) {
  input.classList.toggle('is-bad', !!msg);
  const e = input.parentElement.querySelector('.ferr'); if (e) e.textContent = msg || '';
  return !msg;
}
function tabs(el, items, cur, onPick) {
  el.innerHTML = items.map(([k, label, n]) => '<button class="ptab" type="button" role="tab" data-k="' + k + '" aria-selected="' + (k === cur) + '">' + label + ' <span class="n">' + n + '</span></button>').join('');
  el.onclick = (e) => { const b = e.target.closest('[data-k]'); if (b) onPick(b.dataset.k); };
}
"""

PEOPLE = dict(
  active='people', title='Invite and manage people',
  css=ADMIN_CSS + r"""
  .prow{grid-template-columns:minmax(170px,1.2fr) minmax(0,1.2fr) minmax(0,1.3fr) 250px}
""",
  body=r"""
    <div class="head">
      <div><p class="label" id="pOrg">Oslo</p><h1>Invite and manage people</h1><p>Invite teammates, change their access, and see who’s still invited.</p></div>
      <span class="spacer"></span>
      <button class="btn btn--primary" id="inviteBtn" type="button">+ Invite teammate</button>
    </div>
    <section class="sec">
      <div class="ptabs" id="pTabs" role="tablist" aria-label="People"></div>
      <div class="rhead prow" id="pHead"><span>Person</span><span>Position</span><span>Workspace access</span><span></span></div>
      <div class="roster" id="pList"></div>
    </section>

    <dialog class="dlg dlg--wide" id="accDlg" aria-labelledby="accTitle">
      <div class="dlg__b" style="display:grid;gap:14px">
        <div class="dtop"><div><h3 id="accTitle">Access</h3><span class="rhelp" id="accSub"></span></div><span class="spacer"></span><button class="dx" type="button" data-close aria-label="Close">×</button></div>
        <div class="wsp"><p class="label">Workspace access</p><div class="wsp" id="accWs"></div><span class="ferr" id="accErr"></span>
          <p class="rhelp"><b>Admin</b> everything, plus settings and people · <b>Editor</b> adds sources and approves answers · <b>Viewer</b> asks lojo and reads Knowledge.</p></div>
        <p class="rhelp" id="accNote">Untick every workspace to remove them from Oslo. Changes are logged.</p>
      </div>
      <div class="dlg__f"><button class="btn btn--secondary" type="button" data-close id="accCancel">Cancel</button><button class="btn btn--primary" type="button" data-accsave>Save access</button></div>
    </dialog>

    <dialog class="dlg drawer" id="invDlg" aria-labelledby="invTitle">
      <form id="invForm" novalidate style="display:contents">
      <div class="dlg__b">
        <div class="dtop"><h3 id="invTitle">Invite a teammate</h3><span class="spacer"></span><button class="dx" type="button" data-close aria-label="Close">×</button></div>
        <div class="fld"><label for="invEmail">Work email</label><input class="text" id="invEmail" type="email" autocomplete="off" placeholder="name@oslo.com"><span class="ferr"></span></div>
        <div class="fld"><label for="invName">Name</label><input class="text" id="invName" autocomplete="off" placeholder="First and last name"><span class="ferr"></span></div>
        <div class="fnote" id="invGuest" hidden><span>!</span><span>This email isn’t on <b>oslo.com</b>. They’ll join as a guest and only see the workspaces you pick.</span></div>
        <div class="wsp"><p class="label">Workspace access</p><div class="wsp" id="invWs"></div><span class="ferr" id="invWsErr"></span>
          <p class="rhelp"><b>Admin</b> everything, plus settings and people · <b>Editor</b> adds sources and approves answers · <b>Viewer</b> asks lojo and reads Knowledge</p></div>
        <div class="wsp"><p class="label">What they’ll receive</p><div class="mail" id="invMail"></div></div>
      </div>
      <div class="dlg__f"><button class="btn btn--secondary" type="button" data-close>Cancel</button><button class="btn btn--primary" type="submit">Send invitation</button></div>
      </form>
    </dialog>
""",
  js=ADMIN_JS + r"""
const ORG = 'oslo.com';
let pTab = location.hash === '#invited' ? 'invited' : 'member';
const wsName = (id) => (ST.workspaces.find(w => w.id === id) || { name: id }).name;
// Editors and Viewers see the same list, without inviting or changing access
const MANAGE = window.LOJO_ROLE === 'admin';
if (!MANAGE) {
  $('inviteBtn').hidden = true;
  const h = document.querySelector('.head h1'), tip = h.querySelector('.htip');
  h.firstChild.textContent = 'People ';
  document.title = document.title.replace('Invite and manage people', 'People');
  if (tip) { tip.dataset.tip = 'Who’s in Oslo and what they can do. Only Admins invite people and change access.'; tip.setAttribute('aria-label', tip.dataset.tip); }
}
const chips = (ws) => Object.keys(ws).map(id => '<span class="wsc">' + esc(wsName(id)) + ' <em>· ' + ROLES[ws[id]][0] + '</em></span>').join('');
function render() {
  const mem = ST.people.filter(x => x.status === 'member'), inv = ST.people.filter(x => x.status === 'invited');
  tabs($('pTabs'), [['member', 'Members', mem.length], ['invited', 'Invited', inv.length]], pTab, (k) => { pTab = k; history.replaceState(null, '', k === 'invited' ? '#invited' : '#'); render(); });
  const list = pTab === 'member' ? mem : inv;
  $('pHead').hidden = !list.length;
  $('pList').innerHTML = list.length ? list.map((x, i) => {
    const admin = Object.values(x.ws).includes('admin'), pending = x.status === 'invited';
    return '<div class="rrow2 prow"><div class="who"><span class="av av--p ' + (pending ? 'is-pending' : tone(x.name)) + '">' + ini(x.name) + '</span><div><b>' + esc(x.name) + (admin ? ' <span class="badge badge--rose">Admin</span>' : '') + (x.guest ? ' <span class="badge badge--muted">Guest</span>' : '') + '</b><span>' + esc(x.email) + '</span></div></div>' +
      '<div class="cell">' + (pending ? '<span>Adds their position when they accept</span>' : '<b>' + esc(x.title || '') + '</b><span>' + esc(x.about || '') + '</span>') + '</div>' +
      '<div class="wsl">' + chips(x.ws) + '</div>' +
      '<div class="rstat">' + (pending ? '<span class="badge badge--amber">Invited ' + esc(x.sent) + '</span>' + (MANAGE ? '<button class="btn btn--secondary" type="button" data-resend="' + x.id + '">Resend</button><button class="btn btn--ghost" type="button" data-revoke="' + x.id + '">Revoke</button>' : '') : '<button class="btn btn--secondary" type="button" data-access="' + x.id + '">' + (MANAGE ? 'Edit access' : 'View access') + '</button>') + '</div></div>';
  }).join('') : '<div class="empty2"><b>' + (pTab === 'invited' ? 'No open invitations.' : 'No members yet.') + '</b>' + (MANAGE ? 'Invite a teammate to share the work.' : 'An Admin invites people to Oslo.') + '</div>';
}
$('pList').addEventListener('click', (e) => {
  const a = e.target.closest('[data-access]'); if (a) return openAccess(ST.people.find(p => p.id === a.dataset.access));
  if (!MANAGE) return;
  const r = e.target.closest('[data-resend]'), v = e.target.closest('[data-revoke]');
  if (r) { const x = ST.people.find(p => p.id === r.dataset.resend); x.sent = 'just now'; save(); render(); toast('Invitation resent to ' + x.email + '. The link works for 1 day.'); }
  if (v) { const i = ST.people.findIndex(p => p.id === v.dataset.revoke), x = ST.people[i]; ST.people.splice(i, 1); save(); render(); toast('Invitation to ' + x.email + ' revoked'); }
});

// ---------- edit a member's access: a role per workspace, or none
const acc = $('accDlg'); let accP = null, accPick = {};
function renderAcc() {
  $('accWs').innerHTML = ST.workspaces.map(w => {
    const on = w.id in accPick;
    return '<div class="wso' + (on ? ' is-on' : '') + '"><input type="checkbox" id="acc_' + w.id + '" data-aws="' + w.id + '"' + (on ? ' checked' : '') + (MANAGE ? '' : ' disabled') + '>' +
      '<label class="n" for="acc_' + w.id + '"><b>' + esc(w.name) + '</b><span>' + esc(w.region) + '</span></label>' +
      '<span class="rseg">' + Object.keys(ROLES).map(k => '<button type="button" data-arole="' + k + '" data-for="' + w.id + '" aria-pressed="' + (accPick[w.id] === k) + '"' + (on && MANAGE ? '' : ' disabled') + '>' + ROLES[k][0] + '</button>').join('') + '</span></div>';
  }).join('');
}
function openAccess(p) {
  accP = p; accPick = { ...p.ws }; $('accErr').textContent = '';
  $('accTitle').textContent = 'Access for ' + p.name; $('accSub').textContent = p.email + (p.title ? ' · ' + p.title : '');
  // Editors and Viewers see someone's access but can't change it
  acc.querySelector('[data-accsave]').hidden = !MANAGE; $('accCancel').textContent = MANAGE ? 'Cancel' : 'Close';
  $('accNote').textContent = MANAGE ? 'Untick every workspace to remove them from Oslo. Changes are logged.' : 'Only Admins change access.';
  renderAcc(); acc.showModal();
}
acc.addEventListener('click', async (e) => {
  if (e.target === acc || e.target.closest('[data-close]')) { acc.close(); return; }
  const r = e.target.closest('[data-arole]'); if (r && !r.disabled) { accPick[r.dataset.for] = r.dataset.arole; $('accErr').textContent = ''; renderAcc(); }
  if (e.target.closest('[data-accsave]')) {
    const ids = new Set([...Object.keys(accP.ws), ...Object.keys(accPick)]);
    for (const id of ids) if (accP.ws[id] === 'admin' && accPick[id] !== 'admin' && admins(id).length === 1) { $('accErr').textContent = 'Every workspace needs at least one Admin. Make someone else Admin of ' + wsName(id) + ' first.'; return; }
    if (!Object.keys(accPick).length && !(await confirmDlg('Remove ' + esc(accP.name) + ' from Oslo?', 'They lose access to every workspace straight away. Their approved answers stay. This is logged.', 'Remove', true))) return;
    ids.forEach(id => setRole(accP, id, accPick[id] || null));
    if (!Object.keys(accP.ws).length) { ST.people.splice(ST.people.indexOf(accP), 1); }
    save(); acc.close(); render(); toast('Access updated for ' + accP.name);
  }
});
$('accWs').addEventListener('change', (e) => {
  const c = e.target.closest('[data-aws]'); if (!c || !MANAGE) return;
  if (c.checked) accPick[c.dataset.aws] = 'viewer'; else delete accPick[c.dataset.aws];
  renderAcc();
});

// ---------- invite drawer
const dlg = $('invDlg');
let pick = {};
function renderWs() {
  $('invWs').innerHTML = ST.workspaces.map(w => {
    const on = w.id in pick, role = pick[w.id] || 'viewer';
    return '<div class="wso' + (on ? ' is-on' : '') + '"><input type="checkbox" id="ws_' + w.id + '" data-ws="' + w.id + '"' + (on ? ' checked' : '') + '>' +
      '<label class="n" for="ws_' + w.id + '"><b>' + esc(w.name) + '</b><span>' + esc(w.region) + '</span></label>' +
      '<span class="rseg" role="group" aria-label="Role in ' + esc(w.name) + '">' + Object.keys(ROLES).map(k => '<button type="button" data-role="' + k + '" data-for="' + w.id + '" aria-pressed="' + (on && role === k) + '"' + (on ? '' : ' disabled') + '>' + ROLES[k][0] + '</button>').join('') + '</span></div>';
  }).join('');
}
function renderMail() {
  const name = $('invName').value.trim(), ids = Object.keys(pick);
  $('invMail').innerHTML = '<b>Eric Ouisse invited ' + (name ? esc(name.split(' ')[0]) : 'you') + ' to join Oslo on lojo</b>' +
    (ids.length ? '<div class="wsl">' + chips(pick) + '</div>' : '<p>Pick at least one workspace.</p>') +
    '<p>They add their position and a short description when they accept. The link works for 1 day.</p>';
  const em = $('invEmail').value.trim();
  $('invGuest').hidden = !(validEmail(em) && domainOf(em) !== ORG);
}
function openInvite() {
  pick = { [ST.workspaces[0].id]: 'viewer' };
  $('invForm').reset(); [$('invEmail'), $('invName')].forEach(i => fieldErr(i, '')); $('invWsErr').textContent = '';
  renderWs(); renderMail(); dlg.showModal(); $('invEmail').focus();
}
$('inviteBtn').addEventListener('click', openInvite);
dlg.addEventListener('click', (e) => {
  if (e.target === dlg || e.target.closest('[data-close]')) { dlg.close(); return; }
  const r = e.target.closest('[data-role]'); if (r && !r.disabled) { pick[r.dataset.for] = r.dataset.role; renderWs(); renderMail(); }
});
$('invWs').addEventListener('change', (e) => {
  const c = e.target.closest('[data-ws]'); if (!c) return;
  if (c.checked) pick[c.dataset.ws] = 'viewer'; else delete pick[c.dataset.ws];
  $('invWsErr').textContent = ''; renderWs(); renderMail();
});
['invEmail', 'invName'].forEach(id => $(id).addEventListener('input', (e) => { fieldErr(e.target, ''); renderMail(); }));
$('invForm').addEventListener('submit', (e) => {
  e.preventDefault();
  const em = $('invEmail').value.trim().toLowerCase(), name = $('invName').value.trim();
  const taken = ST.people.find(p => p.email.toLowerCase() === em);
  let ok = fieldErr($('invEmail'), !em ? 'Enter their work email.' : !validEmail(em) ? 'That doesn’t look like an email address.' : taken ? (taken.status === 'invited' ? 'Already invited. Resend it from Invited.' : 'Already a member.') : '');
  ok = fieldErr($('invName'), name ? '' : 'Enter their name.') && ok;
  if (!Object.keys(pick).length) { $('invWsErr').textContent = 'Pick at least one workspace.'; ok = false; }
  if (!ok) { (document.querySelector('#invForm .is-bad') || $('invEmail')).focus(); return; }
  ST.people.push({ id: 'p' + Date.now(), name, email: em, ws: { ...pick }, status: 'invited', sent: 'just now', guest: domainOf(em) !== ORG });
  save(); dlg.close(); pTab = 'invited'; history.replaceState(null, '', '#invited'); render();
  toast('Invitation sent to ' + em);
});
if (MANAGE && new URLSearchParams(location.search).get('invite')) openInvite();
render();
""")

SUPER = dict(
  active='companies', title='Companies', persona='super',
  css=ADMIN_CSS + r"""
  .crow{grid-template-columns:minmax(150px,1.2fr) minmax(0,1.4fr) 96px 64px 270px;gap:6px 14px}
  .crow .num{text-align:left}
  .lin{position:relative}
  .lin .pop{left:auto;right:0;width:250px}
""",
  body=r"""
    <div class="head">
      <div><p class="label">lojo back office</p><h1>Companies</h1><p>Every company on lojo, who owns it, and invitations still waiting. Log in to a workspace to help its team. Every login goes in the audit log.</p></div>
      <span class="spacer"></span>
      <button class="btn btn--primary" id="inviteBtn" type="button">+ Invite company admin</button>
    </div>
    <section class="sec">
      <div class="ptabs" id="cTabs" role="tablist" aria-label="Companies"></div>
      <div class="rhead crow" id="cHead"><span>Company</span><span>Admin</span><span>Workspaces</span><span>Users</span><span style="text-align:right">Status</span></div>
      <div class="roster" id="cList"></div>
    </section>

    <dialog class="dlg dlg--wide" id="invDlg" aria-labelledby="invTitle">
      <form id="invForm" novalidate>
      <div class="dlg__b" style="display:grid;gap:14px">
        <div class="dtop"><div><p class="label">New company</p><h3 id="invTitle">Invite a company admin</h3></div><span class="spacer"></span><button class="dx" type="button" data-close aria-label="Close">×</button></div>
        <p style="margin:0">They set up the company, create workspaces and invite their team.</p>
        <div class="fgrid">
          <div class="fld"><label for="cName">Company name</label><input class="text" id="cName" autocomplete="off" placeholder="Skagen Maritime"><span class="ferr"></span></div>
          <div class="fld"><label for="cDomain">Email domain</label><input class="text" id="cDomain" autocomplete="off" placeholder="skagenmaritime.no"><span class="ferr"></span></div>
          <div class="fld"><label for="oName">Admin name</label><input class="text" id="oName" autocomplete="off" placeholder="Tone Skagen"><span class="ferr"></span></div>
          <div class="fld"><label for="oEmail">Admin email</label><input class="text" id="oEmail" type="email" autocomplete="off" placeholder="tone@skagenmaritime.no"><span class="ferr"></span></div>
        </div>
      </div>
      <div class="dlg__f"><button class="btn btn--secondary" type="button" data-close>Cancel</button><button class="btn btn--primary" type="submit">Send invitation</button></div>
      </form>
    </dialog>

""",
  js=ADMIN_JS + r"""
let cTab = 'all';
const cls = (i) => ' c' + (i % 4 + 1);
function render() {
  const all = ST.companies, act = all.filter(c => c.status === 'active'), inv = all.filter(c => c.status === 'invited');
  tabs($('cTabs'), [['all', 'All', all.length], ['active', 'Active', act.length], ['invited', 'Invited', inv.length]], cTab, (k) => { cTab = k; render(); });
  const list = cTab === 'all' ? all : cTab === 'active' ? act : inv;
  $('cHead').hidden = !list.length;
  $('cList').innerHTML = list.length ? list.map(c => {
    const i = all.indexOf(c), pending = c.status === 'invited';
    return '<div class="rrow2 crow is-click" data-open="' + c.id + '" tabindex="0" role="button" aria-label="Open ' + esc(c.name) + '">' +
      '<div class="who"><span class="av av--org ' + tone(c.name) + '">' + ini(c.name) + '</span><div><b>' + esc(c.name) + '</b><span>' + esc(c.domain) + '</span></div></div>' +
      '<div class="cell"><b>' + esc(c.admin) + '</b><span>' + esc(c.email) + '</span></div>' +
      '<span class="num' + (pending ? ' is-none' : '') + '">' + (pending ? '—' : c.ws.length) + '</span>' +
      '<span class="num' + (pending ? ' is-none' : '') + '">' + (pending ? '—' : c.users) + '</span>' +
      '<div class="rstat">' + (pending ? '<span class="badge badge--amber">Invited ' + esc(c.sent) + '</span><button class="btn btn--secondary" type="button" data-resend="' + c.id + '">Resend</button><button class="btn btn--ghost" type="button" data-revoke="' + c.id + '">Revoke</button>' : '<span class="badge badge--ok">Active</span>' + loginBtn(c)) + '</div></div>';
  }).join('') : '<div class="empty2"><b>Nothing here.</b>' + (cTab === 'invited' ? 'Every invited admin has accepted.' : 'Invite a company admin to get started.') + '</div>';
}
// support access: the super admin opens a workspace as its admin; every login is logged
function loginBtn(c) {
  if (!c.ws.length) return '';
  return '<div class="lin"><button class="btn btn--secondary btn--sm" type="button" data-login="' + c.id + '" aria-haspopup="true" aria-expanded="false">Log in</button>' +
    '<div class="pop" hidden><div class="pop__h">Log in to a ' + esc(c.name) + ' workspace</div>' +
    c.ws.map(w => '<button class="pop__row" type="button" data-ws-login="' + esc(w) + '">' + esc(w) + '</button>').join('') + '</div></div>';
}
function shutLogin(keep) { $('cList').querySelectorAll('.lin .pop').forEach(p => { if (p !== keep) { p.hidden = true; p.previousElementSibling.setAttribute('aria-expanded', 'false'); } }); }
function loginTo(c, ws) {
  plog('Logged in to ' + ws + ' (' + c.name + ')', 'login'); save();
  try { sessionStorage.setItem('lojo-imp', JSON.stringify({ company: c.name, ws })); } catch (e) {}
  location.href = 'dashboard.html?as=admin';
}
document.addEventListener('click', (e) => { if (!e.target.closest('.lin')) shutLogin(); });
document.addEventListener('keydown', (e) => { if (e.key === 'Escape') shutLogin(); });
function resend(c) { c.sent = 'just now'; plog('Resent the invitation to ' + c.admin + ' (' + c.name + ')', 'invite'); save(); render(); toast('Invitation resent to ' + c.email + '. The link works for 1 day.'); }
function revoke(c) { ST.companies.splice(ST.companies.indexOf(c), 1); plog('Revoked the invitation for ' + c.name, 'revoke'); save(); render(); toast('Invitation to ' + c.name + ' revoked'); }
$('cList').addEventListener('click', (e) => {
  const r = e.target.closest('[data-resend]'), v = e.target.closest('[data-revoke]'), o = e.target.closest('[data-open]');
  const lb = e.target.closest('[data-login]'), lw = e.target.closest('[data-ws-login]');
  if (lw) return loginTo(ST.companies.find(c => c.id === lw.closest('.lin').querySelector('[data-login]').dataset.login), lw.dataset.wsLogin);
  if (lb) { const c = ST.companies.find(x => x.id === lb.dataset.login), p = lb.nextElementSibling; if (c.ws.length === 1) return loginTo(c, c.ws[0]); shutLogin(p); p.hidden = !p.hidden; lb.setAttribute('aria-expanded', !p.hidden); return; }
  if (e.target.closest('.lin')) return;
  if (r) return resend(ST.companies.find(c => c.id === r.dataset.resend));
  if (v) return revoke(ST.companies.find(c => c.id === v.dataset.revoke));
  if (o) location.href = 'company.html?id=' + o.dataset.open;
});
$('cList').addEventListener('keydown', (e) => { const o = e.target.closest('[data-open]'); if (o && e.target === o && (e.key === 'Enter' || e.key === ' ') && e.target === o) { e.preventDefault(); location.href = 'company.html?id=' + o.dataset.open; } });

// ---------- invite a company admin
const dlg = $('invDlg'), F = ['cName', 'cDomain', 'oName', 'oEmail'];
const openInv = () => { $('invForm').reset(); F.forEach(id => fieldErr($(id), '')); dlg.showModal(); $('cName').focus(); };
$('inviteBtn').addEventListener('click', openInv);
if (new URLSearchParams(location.search).get('invite')) openInv();
dlg.addEventListener('click', (e) => { if (e.target === dlg || e.target.closest('[data-close]')) dlg.close(); });
F.forEach(id => $(id).addEventListener('input', (e) => fieldErr(e.target, '')));
// the domain fills in from the admin's email if left empty
$('oEmail').addEventListener('blur', () => { const d = domainOf($('oEmail').value.trim()); if (d && !$('cDomain').value.trim()) $('cDomain').value = d; });
$('invForm').addEventListener('submit', (e) => {
  e.preventDefault();
  const v = Object.fromEntries(F.map(id => [id, $(id).value.trim()]));
  const dom = v.cDomain.toLowerCase().replace(/^@/, ''), em = v.oEmail.toLowerCase();
  const onLojo = ST.companies.find(c => c.domain === dom);
  let ok = fieldErr($('cName'), v.cName ? '' : 'Enter the company name.');
  ok = fieldErr($('cDomain'), !dom ? 'Enter the email domain.' : !/^[a-z0-9-]+(\.[a-z0-9-]+)+$/.test(dom) ? 'Use a domain like company.com.' : onLojo ? onLojo.name + ' already uses this domain.' : '') && ok;
  ok = fieldErr($('oName'), v.oName ? '' : 'Enter the admin’s name.') && ok;
  ok = fieldErr($('oEmail'), !em ? 'Enter the admin’s email.' : !validEmail(em) ? 'That doesn’t look like an email address.' : dom && domainOf(em) !== dom ? 'The email should end in @' + dom + '.' : '') && ok;
  if (!ok) { document.querySelector('#invForm .is-bad').focus(); return; }
  ST.companies.push({ id: 'c' + Date.now(), name: v.cName, domain: dom, admin: v.oName, email: em, ws: [], users: 0, status: 'invited', sent: 'just now' });
  plog('Invited ' + v.oName + ' as admin of ' + v.cName, 'invite');
  save(); dlg.close(); cTab = 'invited'; render();
  toast('Invitation sent to ' + em);
});
render();
""")

# ============================================================ SETTINGS (MVP)
# only what the four-week build has
SETTINGS = dict(
  active='settings', title='Settings',
  css=ADMIN_CSS + r"""
  .sgrid{display:grid;grid-template-columns:230px minmax(0,1fr);gap:22px;align-items:start}
  .snav{position:sticky;top:110px;padding:12px}
  .snav h4{margin:12px 8px 6px;font-size:.66rem;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--muted)}
  .snav h4:first-child{margin-top:4px}
  .snav a{display:flex;align-items:center;justify-content:space-between;gap:8px;height:34px;padding:0 10px;border-radius:9px;color:var(--ink);font-weight:500;font-size:.88rem;text-decoration:none}
  .snav a:hover{background:var(--bg-soft)}
  .snav a[aria-current="true"]{background:#FFF0E8;color:#8A4B2F;font-weight:700}
  .snav a.is-later{color:var(--muted);cursor:default}
  .snav a.is-later:hover{background:none}
  .snav em{font-style:normal;font-size:.62rem;font-weight:700;letter-spacing:.06em;text-transform:uppercase;color:var(--muted);border:1px solid var(--line-2);border-radius:999px;padding:1px 7px}
  .spane{display:grid;gap:18px}
  .spane h2{font-family:var(--display);font-weight:700;font-size:1.3rem;margin:0}
  .spane > p{margin:-10px 0 0;color:var(--muted)}
  .srow{display:flex;align-items:center;gap:16px;padding:14px 0;border-top:1px solid var(--line)}
  .srow:first-of-type{border-top:0}
  .srow > div{flex:1;min-width:0}
  .srow b{display:block;font-size:.9rem}
  .srow span{display:block;color:var(--muted);font-size:.8rem}
  .sw{position:relative;width:40px;height:22px;border-radius:999px;border:0;background:var(--line-2);cursor:pointer;flex:none;transition:background-color .15s ease}
  .sw::after{content:"";position:absolute;top:3px;left:3px;width:16px;height:16px;border-radius:50%;background:#fff;box-shadow:0 1px 2px rgba(0,0,0,.2);transition:transform .15s ease}
  .sw[aria-checked="true"]{background:var(--ink)}
  .sw[aria-checked="true"]::after{transform:translateX(18px)}
  .sw:disabled{opacity:.45;cursor:default}
  .fixed{font-size:.72rem;font-weight:700;color:var(--muted);white-space:nowrap}
  .prov{padding:14px 16px;border-radius:12px;background:var(--bg-soft)}
  .prov small{display:block;font-size:.66rem;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--muted);margin-bottom:4px}
  .prov b{font-size:.9rem}
  .meav{width:64px;height:64px;border-radius:50%;display:grid;place-items:center;background:var(--brand-gradient);color:#fff;font-family:var(--display);font-weight:800;font-size:1.2rem}
  .later{display:grid;gap:8px;padding:16px;border:1.5px dashed var(--line-2);border-radius:14px;color:var(--muted);font-size:.86rem}
  .later b{color:var(--ink)}
  .later ul{margin:0;padding-left:18px}
  .danger{border-color:rgba(198,69,69,.25)}
  .meth{display:flex;align-items:center;gap:10px}
  .mrow{grid-template-columns:minmax(0,1fr) auto auto}
  .caps{width:100%;border-collapse:collapse;font-size:.86rem}
  .caps th{font-size:.66rem;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--muted);text-align:center;padding:8px;border-bottom:1px solid var(--line)}
  .caps th:first-child{text-align:left}
  .caps td{padding:10px 8px;border-bottom:1px solid var(--line);text-align:center}
  .caps td:first-child{text-align:left}
  .caps .yes{color:var(--success);font-weight:800}
  .caps .no{color:var(--muted)}
  .alog{list-style:none;margin:0;padding:0;display:grid;gap:8px}
  .alog li{padding:10px 12px;border-radius:10px;background:var(--bg-soft)}
  .alog b{display:block;font-size:.86rem;font-weight:600}
  .alog span{font-size:.76rem;color:var(--muted)}
  @media (max-width:860px){ .mrow{grid-template-columns:1fr} }
  @media (max-width:900px){ .sgrid{grid-template-columns:1fr} .snav{position:static} }
""",
  body=r"""
    <div class="head">
      <div><p class="label">Oslo</p><h1>Settings</h1><p>How you appear to your team.</p></div>
    </div>
    <div class="sgrid">
      <nav class="card snav" id="snav" aria-label="Settings"></nav>
      <section class="sec spane" id="spane" aria-live="polite"></section>
    </div>
""",
  js=ADMIN_JS + r"""
ST.prefs = ST.prefs || { drafts: true, weekly: true, gaps: false, declined: false, target: 20, suggest: true };
const ROLE = window.LOJO_ROLE;
const ME = ST.people.find(p => p.id === ({ admin: 'p1', editor: 'p2', viewer: 'p4' })[ROLE]);
// [id, label, group, later?]
const NAVS = [
  ['YOU', [['profile', 'Profile']]],
];
let cur = (location.hash || '#profile').slice(1);
function nav() {
  $('snav').innerHTML = NAVS.map(([g, items]) => '<h4>' + g + '</h4>' +
    items.map(([id, l, later]) => '<a href="#' + id + '"' + (cur === id ? ' aria-current="true"' : '') + '>' + l + (later ? '<em>Full build</em>' : '') + '</a>').join('')).join('');
}
const row = (t, d, right) => '<div class="srow"><div><b>' + t + '</b><span>' + d + '</span></div>' + right + '</div>';
const fixed = '<span class="fixed">Fixed</span>';
const PANES = {
  profile: () => '<h2>Profile</h2><p>How you appear to your team, and on answers you approve.</p>' +
    '<div class="meth"><span class="meav">' + ini(ME.name) + '</span><button class="btn btn--secondary btn--sm" type="button" data-photo>Change photo</button></div>' +
    '<div class="fgrid"><div class="fld"><label for="pfName">Name</label><input class="text" id="pfName" value="' + esc(ME.name) + '"><span class="ferr"></span></div>' +
    '<div class="fld"><label for="pfEmail">Work email</label><input class="text" id="pfEmail" value="' + esc(ME.email) + '" disabled><span class="fhint">Managed by Oslo · you sign in with Google</span></div></div>' +
    '<div class="fld"><label for="pfTitle">Position</label><input class="text" id="pfTitle" value="' + esc(ME.title || '') + '"></div>' +
    '<div class="fld"><label for="pfAbout">Description</label><textarea class="text" id="pfAbout" style="height:auto;min-height:72px;padding:10px 13px">' + esc(ME.about || '') + '</textarea></div>' +
    '<div class="prov"><small>Shown on answers you approve</small><b id="pfProv"></b></div>' +
    '<div><button class="btn btn--primary" type="button" data-save="profile">Save</button></div>',
};
function render() {
  if (!PANES[cur]) cur = 'profile';
  nav(); $('spane').innerHTML = PANES[cur]();
  if (cur === 'profile') prov();
}
function prov() { const n = $('pfName').value.trim() || ME.name, t = $('pfTitle').value.trim(); $('pfProv').textContent = '✓ Approved by ' + n + (t ? ', ' + t : '') + ' · ' + new Date().toLocaleDateString('en-GB', { day: 'numeric', month: 'short' }); }
window.addEventListener('hashchange', () => { cur = location.hash.slice(1); render(); });

$('spane').addEventListener('input', (e) => { if (cur === 'profile') prov(); fieldErr(e.target, ''); });
$('spane').addEventListener('click', async (e) => {
  const t = e.target;
  if (t.closest('[data-photo]')) toast('Photo upload works in the full product');
  const sv = t.closest('[data-save]'); if (!sv) return;
  if (sv.dataset.save === 'profile') {
    const n = $('pfName').value.trim(); if (!fieldErr($('pfName'), n ? '' : 'Enter your name.')) return;
    ME.name = n; ME.title = $('pfTitle').value.trim(); ME.about = $('pfAbout').value.trim();
    try { const u = JSON.parse(sessionStorage.getItem('lojo-user')) || {}; u.name = n; u.email = ME.email; sessionStorage.setItem('lojo-user', JSON.stringify(u)); } catch (err) {}
    save(); $('meName').textContent = n; $('topAva').textContent = ini(n); toast('Profile saved');
  }
});
render();
""")

# ============================================================ SUPER ADMIN: company, audit log, account
PLATFORM = dict(
  active='pdash', title='Dashboard', persona='super',
  css=ADMIN_CSS + r"""
  .hello h1{font-family:var(--display);font-weight:700;font-size:1.55rem;letter-spacing:-.02em;margin:0;color:#8E2F45}
  .hello p{margin:2px 0 0;font-size:.74rem;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:var(--muted)}

  .kpis{display:grid;grid-template-columns:repeat(5,1fr);gap:12px;margin-bottom:22px}
  .kpi{padding:16px 18px;border:1px solid var(--line);border-radius:16px;background:var(--panel);text-align:center}
  .kpi small{display:block;font-size:.66rem;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--muted)}
  .kpi b{display:block;font-family:var(--display);font-size:1.9rem;line-height:1.15;margin:6px 0 2px}
  .kpi span{font-size:.8rem;color:var(--muted)}
  .pgrid{display:grid;grid-template-columns:minmax(0,1.5fr) minmax(0,1fr);gap:22px;align-items:start}
  .sec h2{font-family:var(--display);font-weight:700;font-size:1.1rem;margin:0 0 12px;display:flex;align-items:center;gap:8px}
  .sec h2 a{margin-left:auto;font-family:var(--body);font-size:.8rem}
  .ctab{width:100%;border-collapse:collapse;font-size:.86rem}
  .ctab th{font-size:.66rem;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--muted);text-align:right;padding:0 8px 8px}
  .ctab th:first-child,.ctab td:first-child{text-align:left}
  .ctab td{padding:10px 8px;border-top:1px solid var(--line);text-align:right;font-variant-numeric:tabular-nums}
  .ctab tr.is-click{cursor:pointer}
  .ctab tr.is-click:hover td{background:var(--bg-soft)}
  .ctab .who .av{width:30px;height:30px;border-radius:9px;font-size:.7rem}
  .alog{list-style:none;margin:0;padding:0;display:grid;gap:8px}
  .alog li{padding:10px 12px;border-radius:10px;background:var(--bg-soft)}
  .alog b{display:block;font-size:.86rem;font-weight:600}
  .alog span{font-size:.76rem;color:var(--muted)}
  .attn{display:flex;align-items:center;gap:12px;padding:12px 0;border-top:1px solid var(--line)}
  .attn:first-of-type{border-top:0}
  .attn div{flex:1;min-width:0}
  .attn b{display:block;font-size:.88rem}
  .attn span{font-size:.78rem;color:var(--muted)}
  @media (max-width:980px){ .kpis{grid-template-columns:repeat(2,1fr)} .pgrid{grid-template-columns:1fr} }
""",
  body=r"""
    <div class="head">
      <div class="hello"><div><h1 id="pHi">Good morning, Sadaf <span aria-hidden="true">👋</span></h1><p id="pDate"></p></div></div>
      <span class="spacer"></span>
      <a class="btn btn--primary" href="superadmin.html?invite=1">+ Invite company admin</a>
    </div>
    <div class="kpis" id="pKpis"></div>
    <section class="sec"><h2>Companies <a href="superadmin.html">All companies →</a></h2><table class="ctab" id="pTable"></table></section>
""",
  js=ADMIN_JS + r"""
function render() {
  const hr = new Date().getHours(), me = (ST.staff || []).find(x => x.id === 's1') || { name: 'Sadaf Farman' };
  $('pHi').innerHTML = (hr < 12 ? 'Good morning' : hr < 18 ? 'Good afternoon' : 'Good evening') + ', ' + esc(me.name.split(' ')[0]) + ' <span aria-hidden="true">👋</span>';
  $('pDate').textContent = new Date().toLocaleDateString('en-GB', { weekday: 'long', day: 'numeric', month: 'long' });
  const act = ST.companies.filter(c => c.status === 'active'), inv = ST.companies.filter(c => c.status === 'invited');
  const sum = (i) => act.reduce((a, c) => a + ((CO_USAGE[c.id] || [])[i] || 0), 0);
  const people = act.reduce((a, c) => a + c.users, 0), ws = act.reduce((a, c) => a + c.ws.length, 0);
  $('pKpis').innerHTML = [
    ['Active companies', act.length, inv.length + ' invitation' + (inv.length === 1 ? '' : 's') + ' open'],
    ['People', people, 'in ' + ws + ' workspaces'],
    ['Approved answers', sum(2), 'from ' + sum(0) + ' documents'],
    ['Ask lojo questions', sum(3), 'this month'],
    ['Processing cost', '$' + (sum(0) * 1.84).toFixed(2), '$1.84 per item read · lojo only'],
  ].map(([l, n, sub]) => '<div class="kpi"><small>' + l + '</small><b>' + n + '</b><span>' + sub + '</span></div>').join('');
  $('pTable').innerHTML = '<thead><tr><th>Company</th><th>People</th><th>Documents</th><th>Approved</th><th>Questions</th><th>Cost</th></tr></thead><tbody>' +
    ST.companies.map((c, i) => { const u = CO_USAGE[c.id], p = c.status === 'invited';
      return '<tr class="is-click" data-open="' + c.id + '"><td><div class="who"><span class="av av--org ' + tone(c.name) + '">' + ini(c.name) + '</span><div><b>' + esc(c.name) + '</b><span>' + (p ? 'Invited ' + esc(c.sent) : esc(c.domain)) + '</span></div></div></td>' +
        [p ? '—' : c.users, u ? u[0] : '—', u ? u[2] : '—', u ? u[3] : '—', u ? '$' + (u[0] * 1.84).toFixed(2) : '—'].map(v => '<td>' + v + '</td>').join('') + '</tr>'; }).join('') + '</tbody>';
}
document.addEventListener('click', (e) => {
  const o = e.target.closest('[data-open]'); if (o) location.href = 'company.html?id=' + o.dataset.open;
});
render();
""")

COMPANY = dict(
  active='companies', title='Company', persona='super',
  css=ADMIN_CSS + r"""
  .crumb{font-size:.82rem;color:var(--muted);margin:0 0 6px}
  .crumb a{color:var(--muted)}
  .cgrid{display:grid;grid-template-columns:minmax(0,1.4fr) minmax(0,1fr);gap:22px;align-items:start}
  .kpis{display:grid;grid-template-columns:repeat(4,1fr);gap:12px}
  .kpi{padding:14px 16px;border:1px solid var(--line);border-radius:14px;background:var(--panel)}
  .kpi b{display:block;font-family:var(--display);font-size:1.5rem;line-height:1.1}
  .kpi span{font-size:.78rem;color:var(--muted)}
  .sec h2{font-family:var(--display);font-weight:700;font-size:1.1rem;margin:0 0 12px}
  .srow{display:flex;align-items:center;gap:16px;padding:12px 0;border-top:1px solid var(--line)}
  .srow:first-of-type{border-top:0}
  .srow > div{flex:1;min-width:0}
  .srow b{display:block;font-size:.9rem}
  .srow span{display:block;color:var(--muted);font-size:.8rem}
  .fixed{font-size:.72rem;font-weight:700;color:var(--muted);white-space:nowrap}
  .alog{list-style:none;margin:0;padding:0;display:grid;gap:8px}
  .alog li{padding:10px 12px;border-radius:10px;background:var(--bg-soft)}
  .alog b{display:block;font-size:.86rem;font-weight:600}
  .alog span{font-size:.76rem;color:var(--muted)}
  @media (max-width:980px){ .cgrid{grid-template-columns:1fr} .kpis{grid-template-columns:repeat(2,1fr)} }
""",
  body=r"""
    <div class="head">
      <div><p class="crumb"><a href="superadmin.html">Companies</a> ›</p><h1 id="cName">Company</h1><p id="cSub"></p></div>
      <span class="spacer"></span>
      <div id="cActs" style="display:flex;gap:8px"></div>
    </div>
    <div id="cBody"></div>
""",
  js=ADMIN_JS + r"""
const c = ST.companies.find(x => x.id === new URLSearchParams(location.search).get('id')) || ST.companies[0];
// counts only: super admins never see a company's sources, drafts or answers
const USAGE = CO_USAGE;
function render() {
  const pending = c.status === 'invited', u = USAGE[c.id] || [0, 0, 0, 0];
  document.title = c.name + ' · lojo';
  $('cName').textContent = c.name;
  $('cSub').innerHTML = esc(c.domain) + ' · ' + (pending ? '<span class="badge badge--amber">Invited ' + esc(c.sent) + '</span>' : '<span class="badge badge--ok">Active</span> since ' + esc(c.since));
  $('cActs').innerHTML = pending ? '<button class="btn btn--ghost" type="button" data-act="revoke">Revoke</button><button class="btn btn--secondary" type="button" data-act="resend">Resend invitation</button>' : '';
  $('cBody').innerHTML = (pending ? '<div class="sec"><div class="empty2"><b>Waiting for ' + esc(c.admin) + ' to accept.</b>Workspaces, people and usage show up once they set up ' + esc(c.name) + '. The link works for 1 day.</div></div>' :
    '<div class="kpis" style="margin-bottom:22px">' + [[c.ws.length, 'Workspaces'], [c.users, 'People'], [u[0], 'Documents'], [u[2], 'Approved answers']].map(([n, l]) => '<div class="kpi"><b>' + n + '</b><span>' + l + '</span></div>').join('') + '</div>') +
    '<div class="cgrid"><div>' +
      '<section class="sec"><h2>Admin</h2><div class="who"><span class="av av--p ' + tone(c.admin) + '">' + ini(c.admin) + '</span><div><b>' + esc(c.admin) + ' <span class="badge badge--rose">Admin</span></b><span>' + esc(c.email) + '</span></div></div></section>' +
      (pending ? '' : '<section class="sec"><h2>Workspaces</h2><div class="wsl">' + c.ws.map(w => '<span class="wsc">' + esc(w) + '</span>').join('') + '</div></section>' +
      '<section class="sec"><h2>Processing cost <span class="rhelp" style="font-weight:500">· lojo only, metered on every model call</span></h2><div>' +
        '<div class="srow"><div><b>Items read</b><span>Documents, emails, pages and calls</span></div><b>' + u[0] + '</b></div>' +
        '<div class="srow"><div><b>Total so far</b><span>Indexing, question finding, drafting, rewrites and Ask lojo</span></div><b>$' + (u[0] * 1.84).toFixed(2) + '</b></div>' +
        '<div class="srow"><div><b>Per item read</b><span>Average</span></div><b>$1.84</b></div></div></section>' +
      '<section class="sec"><h2>Usage this month</h2><div>' +
        '<div class="srow"><div><b>Questions found</b><span>From their documents</span></div><b>' + u[1] + '</b></div>' +
        '<div class="srow"><div><b>Approved answers</b><span>Reviewed by a person</span></div><b>' + u[2] + '</b></div>' +
        '<div class="srow"><div><b>Ask lojo questions</b><span>From their team</span></div><b>' + u[3] + '</b></div></div></section>') +
    '</div><div>' +
      '<section class="sec"><h2>Privacy</h2><div class="lock"><span>🔒</span><span>Sources, drafts and answers belong to ' + esc(c.name) + '. lojo staff see counts only.</span></div></section>' +
      '<section class="sec"><h2>History</h2>' + hist() + '</section>' +
    '</div></div>';
}
function hist() {
  const L = ST.platformLog.filter(x => x.msg.includes(c.name));
  return L.length ? '<ul class="alog">' + L.map(x => '<li><b>' + esc(x.msg) + '</b><span>' + esc(x.by) + ' · ' + esc(x.at) + '</span></li>').join('') + '</ul>' : '<p class="rhelp">Nothing yet.</p>';
}
$('cActs').addEventListener('click', async (e) => {
  const a = e.target.closest('[data-act]'); if (!a) return;
  if (a.dataset.act === 'resend') { c.sent = 'just now'; plog('Resent the invitation to ' + c.admin + ' (' + c.name + ')', 'invite'); save(); render(); toast('Invitation resent to ' + c.email); }
  if (a.dataset.act === 'revoke' && await confirmDlg('Revoke the invitation for ' + esc(c.name) + '?', 'The link stops working and ' + esc(c.name) + ' leaves the list. This is logged.', 'Revoke', true)) {
    ST.companies.splice(ST.companies.indexOf(c), 1); plog('Revoked the invitation for ' + c.name, 'revoke'); save(); location.href = 'superadmin.html';
  }
});
render();
""")

AUDIT = dict(
  active='auditlog', title='Audit log', persona='super',
  css=ADMIN_CSS + r"""
  .lrow{grid-template-columns:minmax(0,1fr) 180px 150px}
  .lrow .k{justify-self:start}
  @media (max-width:860px){ .lrow{grid-template-columns:1fr} }
""",
  body=r"""
    <div class="head">
      <div><p class="label">lojo back office</p><h1>Audit log</h1><p>Everything done in this admin area: who did it and when. Entries can’t be edited or deleted.</p></div>
    </div>
    <section class="sec">
      <div class="ptabs" id="lTabs" role="tablist" aria-label="Filter"></div>
      <div class="rhead lrow"><span>What happened</span><span>Who</span><span>When</span></div>
      <div class="roster" id="lList"></div>
    </section>
""",
  js=ADMIN_JS + r"""
const KINDS = { all: 'All', invite: 'Invitations', accept: 'Accepted', revoke: 'Revoked', login: 'Workspace logins' };
let f = 'all';
function render() {
  const L = ST.platformLog;
  tabs($('lTabs'), Object.keys(KINDS).map(k => [k, KINDS[k], k === 'all' ? L.length : L.filter(x => x.kind === k).length]), f, (k) => { f = k; render(); });
  const list = f === 'all' ? L : L.filter(x => x.kind === f);
  $('lList').innerHTML = list.length ? list.map(x => '<div class="rrow2 lrow"><div class="cell"><b>' + esc(x.msg) + '</b><span>' + esc(KINDS[x.kind] || 'Change') + '</span></div><span>' + esc(x.by) + '</span><span class="rhelp">' + esc(x.at) + '</span></div>').join('')
    : '<div class="empty2"><b>Nothing here yet.</b>Actions in Companies show up here.</div>';
}
render();
""")

ACCOUNT = dict(
  active='', title='Profile', persona='super',
  css=ADMIN_CSS + r"""
  .srow{display:flex;align-items:center;gap:16px;padding:14px 0;border-top:1px solid var(--line)}
  .srow:first-of-type{border-top:0}
  .srow > div{flex:1;min-width:0}
  .srow b{display:block;font-size:.9rem}
  .srow span{display:block;color:var(--muted);font-size:.8rem}
  .sw{position:relative;width:40px;height:22px;border-radius:999px;border:0;background:var(--line-2);cursor:pointer;flex:none}
  .sw::after{content:"";position:absolute;top:3px;left:3px;width:16px;height:16px;border-radius:50%;background:#fff;transition:transform .15s ease}
  .sw[aria-checked="true"]{background:var(--ink)}
  .sw[aria-checked="true"]::after{transform:translateX(18px)}
  .fixed{font-size:.72rem;font-weight:700;color:var(--muted);white-space:nowrap}
  .later{display:grid;gap:8px;padding:16px;border:1.5px dashed var(--line-2);border-radius:14px;color:var(--muted);font-size:.86rem}
  .later b{color:var(--ink)}
  .sec h2{font-family:var(--display);font-weight:700;font-size:1.2rem;margin:0 0 4px}
  .sec > p{margin:0 0 14px;color:var(--muted)}
""",
  body=r"""
    <div class="head">
      <div><p class="label">lojo back office</p><h1>Profile</h1><p>Your lojo staff account.</p></div>
    </div>
    <section class="sec" id="aProfile"></section>
""",
  js=ADMIN_JS + r"""
const me = ST.staff.find(s => s.id === 's1');
function render() {
  $('aProfile').innerHTML = '<h2>Profile</h2><p>How you appear in the audit log and in invitations.</p>' +
    '<div class="fgrid"><div class="fld"><label for="aName">Name</label><input class="text" id="aName" value="' + esc(me.name) + '"><span class="ferr"></span></div>' +
    '<div class="fld"><label for="aEmail">lojo email</label><input class="text" id="aEmail" value="' + esc(me.email) + '" disabled><span class="fhint">Signs in with Google for lojo.ai</span></div></div>' +
    '<div class="fld" style="margin-top:14px"><label for="aTitle">Position</label><input class="text" id="aTitle" value="' + esc(me.title || '') + '"></div>' +
    '<div class="srow" style="margin-top:8px"><div><b>Role</b><span>' + STAFF_ROLES[me.role][1] + '</span></div><span class="badge badge--rose">' + STAFF_ROLES[me.role][0] + '</span></div>' +
    '<div style="margin-top:8px"><button class="btn btn--primary" type="button" data-save>Save</button></div>';
}
document.addEventListener('click', (e) => {
  if (e.target.closest('#aProfile [data-save]')) {
    const n = $('aName').value.trim(); if (!fieldErr($('aName'), n ? '' : 'Enter your name.')) return;
    me.name = n; me.title = $('aTitle').value.trim(); save(); $('meName').textContent = n; $('topAva').textContent = ini(n); toast('Profile saved');
  }
});
$('aProfile').addEventListener('input', (e) => fieldErr(e.target, ''));
render();
""")

# ============================================================ EMAILS (design use cases)
# every email the MVP sends, previewed as it would arrive
EMAILS_PAGE = dict(
  active='states', title='Emails',
  css=r"""
  .egrid{display:grid;grid-template-columns:300px minmax(0,1fr);gap:22px;align-items:start}
  .elist{position:sticky;top:110px;padding:10px;max-height:calc(100vh - 140px);overflow:auto}
  .elist h4{margin:12px 8px 6px;font-size:.66rem;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--muted)}
  .elist h4:first-child{margin-top:4px}
  .elist a{display:block;padding:8px 10px;border-radius:9px;color:var(--ink);font-weight:500;text-decoration:none}
  .elist a:hover{background:var(--bg-soft)}
  .elist a b{display:block;font-size:.86rem;font-weight:600}
  .elist a span{display:block;font-size:.74rem;color:var(--muted);overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
  .elist a[aria-current="true"]{background:#FFF0E8}
  .elist a[aria-current="true"] b{color:#8A4B2F}
  .meta2{display:grid;grid-template-columns:90px 1fr;gap:6px 12px;font-size:.84rem;padding:16px 18px;border-bottom:1px solid var(--line)}
  .meta2 dt{color:var(--muted)}
  .meta2 dd{margin:0}
  .meta2 .subj{font-weight:700}
  .why{display:flex;gap:10px;flex-wrap:wrap;padding:12px 18px;border-bottom:1px solid var(--line);background:var(--bg-soft);font-size:.8rem;color:var(--muted)}
  .why b{color:var(--ink);font-weight:600}
  .inbox{padding:28px 18px;background:#F4F1EE}
  .mail2{max-width:560px;margin:0 auto;background:#fff;border-radius:16px;border:1px solid var(--line);overflow:hidden;color:#241A14}
  .mail2__top{display:flex;align-items:center;gap:10px;padding:20px 28px 0}
  .mail2__top img{width:36px;height:30px;object-fit:contain}
  .mail2__top b{font-family:var(--display);font-size:1.05rem}
  .mail2__body{padding:18px 28px 26px}
  .mail2 h2{font-family:var(--display);font-weight:700;font-size:1.35rem;line-height:1.25;margin:0 0 12px}
  .mail2 p{margin:0 0 12px;font-size:.92rem;line-height:1.6;color:#4A3B32}
  .mail2 .cta{display:inline-block;margin:6px 0 14px;padding:11px 20px;border-radius:999px;background:#241A14;color:#fff;font-weight:700;font-size:.9rem;text-decoration:none}
  .mail2 .box{padding:12px 14px;border-radius:12px;background:#F7F4F1;margin:0 0 14px;font-size:.88rem}
  .mail2 .box b{display:block}
  .mail2 ul{margin:0 0 14px;padding-left:20px;font-size:.9rem;line-height:1.7;color:#4A3B32}
  .mail2 .chips{display:flex;flex-wrap:wrap;gap:6px;margin:0 0 14px}
  .mail2 .chip2{display:inline-flex;height:26px;align-items:center;padding:0 10px;border-radius:999px;border:1px solid rgba(36,26,20,.16);font-size:.78rem;font-weight:600}
  .mail2 .chip2 em{font-style:normal;color:#6E5A4E;font-weight:500;margin-left:4px}
  .mail2 .small{font-size:.78rem;color:#6E5A4E}
  .mail2__foot{padding:16px 28px;border-top:1px solid rgba(36,26,20,.08);font-size:.74rem;color:#6E5A4E;line-height:1.5}
  :root[data-theme="dark"] .inbox{background:#1E1714}
  /* on a persona's journey the invitation shows on its own, like opening it in a mail app */
  body.mailonly .side,body.mailonly .mnav,body.mailonly .mscrim,body.mailonly .fab,body.mailonly .head,body.mailonly #elist,body.mailonly .why{display:none}
  body.mailonly .main{margin-left:0}
  body.mailonly .wrap{max-width:760px;margin:0 auto;padding-top:28px}
  body.mailonly .egrid{grid-template-columns:1fr}
  .eback{display:inline-flex;align-items:center;gap:6px;margin:0 0 14px;font-weight:600;font-size:.88rem;color:var(--muted);text-decoration:none}
  .eback:hover{color:var(--ink)}
  @media (max-width:900px){ .egrid{grid-template-columns:1fr} .elist{position:static;max-height:none} }
""",
  body=r"""
    <div class="head">
      <div><p class="label"><a href="states.html">Design use cases</a> ›</p><h1>Emails</h1><p>Every email lojo sends in this phase, who gets it and what triggers it. Previews use the demo data.</p></div>
    </div>
    <div class="egrid">
      <nav class="card elist" id="elist" aria-label="Emails"></nav>
      <section class="card" id="epane" aria-live="polite"></section>
    </div>
""",
  js=r"""
const OFF = 'You get this because you review answers in Oslo.';
const ACC = 'You get this because of a change to your lojo account. If you didn’t expect it, reply and we’ll look into it.';
const STAFF = 'Sent to lojo staff only.';
// invitations name the person, never the company or workspace
const invite = (name) => '<h2>Hello ' + name + ',</h2><p>You have been invited to join lojo.ai. Please click on the link below to accept the invitation and set up your password.</p><a class="cta" href="#">Let’s set up</a><p>If you have any questions, please contact <a href="mailto:support@lojo.ai">support@lojo.ai</a>.</p><p>Best,<br>The lojo Team</p>';
// key, group, list label, to, trigger, subject, preheader, body html, footer
const EMAILS = [
  ['admin-invite', 'Joining lojo', 'Company admin invitation', 'The future company admin', 'Super admin sends “Invite a company admin”, or resends it', 'You’re invited to join lojo.ai', 'Accept the invitation and set up your password.',
    invite('Eric Ouisse'), ''],
  ['team-invite', 'Joining lojo', 'Teammate invitation', 'A new teammate', 'An Admin sends an invitation from People, or resends it', 'You’re invited to join lojo.ai', 'Accept the invitation and set up your password.',
    invite('Lena Okafor'), ''],
  ['viewer-invite', 'Joining lojo', 'Teammate invitation (Viewer)', 'A new teammate', 'An Admin sends an invitation from People, or resends it', 'You’re invited to join lojo.ai', 'Accept the invitation and set up your password.',
    invite('Jonas Lie'), ''],
  ['verify', 'Joining lojo', 'Confirm your email', 'Someone signing in with email', 'Signing in with email for the first time', 'Confirm your email for lojo', 'One click and you’re in.',
    '<h2>Confirm your email</h2><p>Click below to confirm eric@oslo.com and finish signing in.</p><a class="cta" href="#">Confirm email</a><p class="small">This link works for 24 hours. If you didn’t try to sign in, you can ignore this email.</p>', ACC],
  ['reset', 'Your account', 'Reset password', 'Anyone who signs in with email', '“Forgot password?” on the sign-in page', 'Reset your lojo password', 'The link works for 1 hour.',
    '<h2>Reset your password</h2><p>Someone asked to reset the password for eric@oslo.com. If that was you, choose a new one below.</p><a class="cta" href="#">Choose a new password</a><p class="small">This link works for 1 hour. If you didn’t ask, ignore this email and your password stays the same.</p>', ACC],
  ['role', 'Your account', 'Your role changed', 'The person whose role changed', 'An Admin changes their role in Members and roles or Edit access', 'Your role in Oslo is now Viewer', 'Eric Ouisse changed your access.',
    '<h2>Your role in Oslo changed</h2><p>Hi Lena, Eric Ouisse changed your role in Oslo from <b>Editor</b> to <b>Viewer</b>.</p><div class="box"><b>As a Viewer you can</b>Ask lojo and read approved answers in Knowledge.</div><p>You can no longer add sources or review drafts. Answers you already approved stay as they are.</p><a class="cta" href="#">Open lojo</a><p class="small">Questions? Ask Eric Ouisse, an Admin of Oslo.</p>', ACC],
  ['removed', 'Your account', 'Removed from a workspace', 'The person removed', 'An Admin removes them in Members and roles or Edit access', 'You no longer have access to Oslo', 'Eric Ouisse removed your access.',
    '<h2>You no longer have access to Oslo</h2><p>Hi Jonas, Eric Ouisse removed you from Oslo on lojo. You can’t sign in to it any more.</p><p>Answers you approved stay in Oslo’s knowledge, with your name on them.</p><p class="small">If you think this is a mistake, ask Eric Ouisse.</p>', ACC],
  ['deleted', 'Your account', 'Workspace deleted', 'Everyone in the workspace', 'An Admin deletes a workspace in Data and export', 'Oslo — Sandbox was deleted', 'Its documents, drafts and answers are gone.',
    '<h2>Oslo — Sandbox was deleted</h2><p>Eric Ouisse deleted the workspace Oslo — Sandbox. Its documents, questions, drafts and approved answers were deleted for everyone.</p><p>Your other workspaces aren’t affected.</p><a class="cta" href="#">Open lojo</a>', ACC],
  ['drafts', 'Review', 'Drafts waiting', 'Admins and Editors', 'A new batch of drafts lands in Build', '10 drafts are ready for review', 'Approve, edit or reject them in Build.',
    '<h2>10 drafts are ready for review</h2><p>lojo drafted answers to questions your team keeps asking. Each one shows the sources it came from.</p><ul><li>Is SSO included on the Growth plan? <span class="small">· sources disagree</span></li><li>How long do refunds take?</li><li>What are the API rate limits?</li></ul><a class="cta" href="#">Review in Build</a>', OFF],
  ['weekly', 'Review', 'Friday review reminder', 'Admins and Editors', 'Fridays, while the week’s target isn’t met', 'Friday review: 7 of 20 drafts done', '13 drafts left this week.',
    '<h2>13 drafts left this week</h2><p>Your team reviewed <b>7 of 20</b> drafts so far. Approved answers go straight to Ask lojo.</p><div class="box"><b>Waiting the longest</b>Is SSO included on the Growth plan? · 4 days</div><a class="cta" href="#">Review now</a>', OFF],
  ['gaps', 'Review', 'New gaps found', 'Admins and Editors', 'lojo finds things the documents mention but never explain', 'lojo found 3 gaps in your documents', 'Send a document or explain them yourself.',
    '<h2>3 things your documents never explain</h2><p>They’re mentioned, but no document says what they are. Answers that rely on them can’t be approved yet.</p><ul><li>The Enterprise plan</li><li>Chargeback fee</li><li>Data retention period</li></ul><a class="cta" href="#">See gaps in Insights</a>', OFF],
  ['declined', 'Review', 'Ask lojo declined a question', 'Admins and Editors', 'Ask lojo couldn’t answer from approved knowledge', 'Ask lojo couldn’t answer a question', 'Decide whether it matters.',
    '<h2>Ask lojo couldn’t answer this</h2><div class="box"><b>“Do we support Apple Pay in Germany?”</b>Asked by Jonas Lie · today</div><p>Nothing approved answers it yet, so lojo said so instead of guessing. It’s now a question in Insights.</p><a class="cta" href="#">Decide in Insights</a>', OFF],
  ['accepted', 'lojo staff', 'Admin accepted', 'Super admins', 'A company admin accepts their invitation', 'Oslo is active on lojo', 'Eric Ouisse accepted the invitation.',
    '<h2>Oslo is active</h2><p>Eric Ouisse accepted the invitation and set up Oslo. You’ll see its numbers on the company page.</p><a class="cta" href="#">Open Oslo in Companies</a>', STAFF],
  ['expiring', 'lojo staff', 'Invitation about to expire', 'Super admins', '4 hours before a company admin’s 1-day link runs out', 'The invitation to Halvorsen Legal expires in 4 hours', 'Martin Halvorsen hasn’t accepted yet.',
    '<h2>Halvorsen Legal hasn’t joined yet</h2><p>Martin Halvorsen’s invitation expires in 4 hours. Resend it for another day, or revoke it.</p><a class="cta" href="#">Open Companies</a>', STAFF],
  ['summary', 'lojo staff', 'Weekly platform summary', 'Super admins', 'Mondays', 'lojo this week: 1 new company, 1 open invitation', 'Usage across all companies.',
    '<h2>lojo this week</h2><ul><li>1 company became active: Oslo</li><li>1 invitation is still open: Halvorsen Legal</li><li>48 questions asked in Ask lojo across all companies</li></ul><p class="small">Counts only. lojo staff never see a company’s sources or answers.</p><a class="cta" href="#">Open Companies</a>', STAFF],
];
let cur = (location.hash || '#admin-invite').slice(1);
const JOIN = { 'admin-invite': ['admin', 'eric@oslo.com', 'Eric Ouisse'], 'team-invite': ['editor', 'lena@oslo.com', 'Lena Okafor'], 'viewer-invite': ['viewer', 'jonas@oslo.com', 'Jonas Lie'] };
const MAILONLY = new URLSearchParams(location.search).has('journey');
document.body.classList.toggle('mailonly', MAILONLY);
if (MAILONLY) document.querySelector('.egrid').insertAdjacentHTML('beforebegin', '<a class="eback" href="auth.html?s=persona">← Back</a>');
function render() {
  const e = EMAILS.find(x => x[0] === cur) || EMAILS[0]; cur = e[0];
  const groups = [...new Set(EMAILS.map(x => x[1]))];
  $('elist').innerHTML = groups.map(g => '<h4>' + esc(g) + '</h4>' + EMAILS.filter(x => x[1] === g).map(x => '<a href="#' + x[0] + '"' + (x[0] === cur ? ' aria-current="true"' : '') + '><b>' + esc(x[2]) + '</b><span>' + esc(x[5]) + '</span></a>').join('')).join('');
  const [, , , to, trig, subj, pre, html, foot] = e;
  const j = MAILONLY && JOIN[cur];
  $('epane').innerHTML = '<dl class="meta2"><dt>From</dt><dd>lojo &lt;hello@lojo.ai&gt;</dd><dt>To</dt><dd>' + esc(j ? j[2] + ' <' + j[1] + '>' : to) + '</dd><dt>Subject</dt><dd class="subj">' + esc(subj) + '</dd>' + (MAILONLY ? '' : '<dt>Preview</dt><dd>' + esc(pre) + '</dd>') + '</dl>' +
    '<div class="why"><span><b>Sent when:</b> ' + esc(trig) + '</span></div>' +
    '<div class="inbox"><div class="mail2"><div class="mail2__top"><img src="assets/lojo-logo.svg" alt=""><b>lojo.ai</b></div><div class="mail2__body">' + html + '</div><div class="mail2__foot">' + (foot ? foot + '<br>' : '') + '© 2026 lojo.ai. All rights reserved.</div></div></div>';
}
window.addEventListener('hashchange', () => { cur = location.hash.slice(1); render(); });
// on a persona's journey the invitation's button carries on to setting a password
$('epane').addEventListener('click', (e) => {
  if (!e.target.closest('.cta')) return;
  e.preventDefault();
  const j = JOIN[cur];
  if (j && window.LOJO_JOURNEY === j[0]) location.href = 'auth.html?s=set&from=invite&journey=' + j[0] + '&email=' + encodeURIComponent(j[1]);
  else toast('In the real email this opens lojo');
});
render();
""")

RO_PAGE = dict(
  active='readout', title='Readout',
  css=r"""
  .rofind{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:12px;margin-bottom:14px}
  .rofind div{padding:16px 18px;border:1px solid var(--line);border-radius:14px;background:var(--panel)}
  .rofind b{display:block;font-family:var(--display);font-size:1.8rem;line-height:1.1}
  .rofind b.hi{color:var(--rose)}
  .rofind span{font-size:.84rem;color:var(--muted)}
  .rolist{margin:6px 0 0;padding-left:20px;line-height:1.9;font-size:.92rem}
  .rodec{display:grid;grid-template-columns:1fr 1fr;gap:12px}
  .rodec button{display:grid;gap:4px;padding:18px 20px;border-radius:14px;border:1.5px solid var(--line-2);background:var(--panel);text-align:left;font:inherit;cursor:pointer}
  .rodec button b{font-family:var(--display);font-size:1.05rem}
  .rodec button span{font-size:.84rem;color:var(--muted)}
  .rodec button[aria-pressed="true"]{border-color:var(--ink);box-shadow:0 0 0 3px rgba(36,26,20,.08)}
  .rodone{margin-top:12px;padding:12px 14px;border-radius:12px;background:rgba(63,143,95,.08);color:var(--success);font-weight:600;font-size:.88rem}
  .sec h2{font-family:var(--display);font-weight:700;font-size:1.15rem;margin:0 0 14px}
  @media (max-width:900px){ .rofind{grid-template-columns:repeat(2,1fr)} .rodec{grid-template-columns:1fr} }
  @media print{ .side,.fab,.head .btn,.mnav{display:none!important} .main{margin:0} }
""",
  body=r"""
    <div class="head">
      <div><p class="label"><a href="knowledge.html">Knowledge</a> › Week 4</p><h1>Readout</h1><p>What four weeks produced, and your decision.</p></div>
      <span class="spacer"></span>
      <button class="btn btn--secondary" type="button" id="roPrint">Print</button>
    </div>
    <section class="sec"><h2>What we found</h2><div class="rofind" id="roFind"></div><ul class="rolist" id="roList"></ul>
      <p class="rhelp" style="margin-top:10px"><a href="knowledge.html">See it all in Knowledge →</a></p></section>
    <section class="sec"><h2>Your decision</h2><div class="rodec" id="roDec">
      <button type="button" data-dec="go"><b>Continue to the full build</b><span>Keep the approved answers and go on with lojo.</span></button>
      <button type="button" data-dec="stop"><b>Not now</b><span>Keep an export of everything approved.</span></button>
    </div><div id="roDone"></div></section>
""",
  js=r"""
if (window.LOJO_ROLE && window.LOJO_ROLE !== 'admin') noAccess(window.LOJO_ROLE, 'readout.html');
function render() {
  const c = counts(), human = tasks().human, ch = ST.chat || { asked: 0, answered: 0, declined: 0 };
  $('roFind').innerHTML = [[c.questions, 'questions your documents answer', 1], [c.gaps, 'gaps: referred to, never explained'], [c.approved + ' / ' + c.drafts, 'answers approved'], [ch.answered + ' / ' + ch.asked, 'Ask lojo questions answered']]
    .map(([n, l, hi]) => '<div><b' + (hi ? ' class="hi"' : '') + '>' + n + '</b><span>' + l + '</span></div>').join('');
  $('roList').innerHTML = '<li>Your reviewers approved ' + c.approved + ' drafts.</li><li>Ask lojo was asked ' + ch.asked + ' questions: it answered ' + ch.answered + ' from approved answers and declined ' + ch.declined + ', each recorded as a question.</li>' +
    '<li>' + human + ' questions have no answer in the sources, or were sent to a person, and wait for someone to write them.</li>';
  document.querySelectorAll('[data-dec]').forEach(b => b.setAttribute('aria-pressed', ST.decision === b.dataset.dec));
  $('roDone').innerHTML = ST.decision ? '<div class="rodone">✓ ' + (ST.decision === 'go' ? 'You chose to continue. lojo will be in touch to plan the full build.' : 'You chose not now. Your export of approved answers is ready in Distribute.') + '</div>' : '';
}
$('roDec').addEventListener('click', (e) => { const b = e.target.closest('[data-dec]'); if (!b) return; ST.decision = b.dataset.dec; save(); render(); toast('Decision saved'); });
$('roPrint').addEventListener('click', () => print());
render();
""")

# ============================================================ SOPs (LOJ-29, R1)
SOPS = dict(
  active='sops', title='SOPs',
  css=r"""
  .seclbl{font-size:.68rem;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--muted);margin:0 0 10px}
  /* four ways in, one click each */
  .starts{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:12px;margin:0 0 26px}
  .st{display:grid;grid-template-columns:38px minmax(0,1fr);gap:4px 12px;align-items:start;padding:16px;border-radius:14px;border:1px solid var(--line-2);background:var(--panel);color:var(--ink);font:inherit;text-align:left;cursor:pointer;text-decoration:none;transition:border-color .15s ease,box-shadow .15s ease}
  .st:hover{border-color:rgba(232,93,117,.5);box-shadow:0 10px 24px -18px rgba(232,93,117,.8);text-decoration:none}
  .st__ic{grid-row:span 2;width:38px;height:38px;border-radius:11px;display:grid;place-items:center;background:#FFF0E8;color:#8A4B2F}
  .st__ic svg{width:19px;height:19px;fill:none;stroke:currentColor;stroke-width:1.8;stroke-linecap:round;stroke-linejoin:round}
  .st b{font-size:.92rem;line-height:1.3}
  .st span:last-child{font-size:.8rem;color:var(--muted);line-height:1.4;font-weight:500}
  .st.is-main{border-color:rgba(232,93,117,.4);background:linear-gradient(135deg,#FFF5F1,#FFFFFF)}
  .st.is-main .st__ic{background:var(--brand-gradient);color:#fff}
  /* the lifecycle doubles as the filter */
  .flow{display:flex;align-items:center;gap:6px;flex-wrap:wrap;margin:0 0 14px}
  .flow button{display:inline-flex;align-items:center;gap:8px;height:36px;padding:0 14px;border-radius:999px;border:1px solid var(--line-2);background:var(--panel);font:inherit;font-size:.84rem;font-weight:600;color:var(--ink);cursor:pointer}
  .flow button:hover{border-color:rgba(36,26,20,.3)}
  .flow button[aria-pressed="true"]{background:var(--ink);border-color:var(--ink);color:#fff}
  .flow button em{font-style:normal;font-size:.72rem;font-weight:700;min-width:20px;height:20px;padding:0 6px;border-radius:999px;display:grid;place-items:center;background:var(--bg-soft);color:var(--muted)}
  .flow button[aria-pressed="true"] em{background:rgba(255,255,255,.18);color:#fff}
  .flow i{width:8px;height:8px;border-radius:50%;flex:none}
  .flow .arr{color:var(--line-2);font-size:.9rem}
  .flow .sep{width:1px;height:22px;background:var(--line-2);margin:0 6px}
  .dot-draft{background:#B9ADA6}.dot-review{background:var(--info)}.dot-approved{background:var(--success)}.dot-due{background:var(--warning)}.dot-retired{background:#D8D0CB}
  .stbl{width:100%;border-collapse:collapse}
  .stbl th{text-align:left;font-size:.68rem;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--muted);padding:12px 16px;border-bottom:1px solid var(--line)}
  .stbl td{padding:14px 16px;border-bottom:1px solid var(--line);vertical-align:middle;font-size:.86rem}
  .stbl tr:last-child td{border-bottom:0}
  .stbl tbody tr{cursor:pointer}
  .stbl tbody tr:hover td{background:var(--bg-soft)}
  .stbl tbody tr:focus-visible{outline:2px solid var(--rose);outline-offset:-2px}
  .stbl .t b{display:block;font-size:.94rem}
  .stbl .t small{display:flex;align-items:center;gap:6px;color:var(--muted);font-size:.78rem;margin-top:2px}
  .stbl tr.is-retired .t b{color:var(--muted);text-decoration:line-through}
  .sid{font:600 .72rem/1 ui-monospace,Menlo,monospace;color:var(--muted);background:var(--bg-soft);border-radius:6px;padding:4px 6px;white-space:nowrap}
  .who{display:flex;align-items:center;gap:8px;white-space:nowrap}
  .avs{width:26px;height:26px;border-radius:50%;flex:none;display:grid;place-items:center;color:#fff;font:800 .62rem var(--display)}
  .late{color:var(--error);font-weight:700}
  .ext{display:inline-flex;align-items:center;gap:4px}
  .ext svg,.ic14{width:13px;height:13px;fill:none;stroke:currentColor;stroke-width:2;stroke-linecap:round;stroke-linejoin:round}
  /* ---------- one SOP ---------- */
  body.is-detail #sopHead,body.is-detail #sopList{display:none}
  .back{display:inline-flex;gap:6px;align-items:center;font-size:.84rem;color:var(--muted);margin:0 0 12px}
  .dhead{display:flex;align-items:flex-start;gap:16px;flex-wrap:wrap;margin-bottom:16px}
  .dhead__t{flex:1 1 380px;min-width:0}
  .dhead__m{display:flex;align-items:center;gap:8px;flex-wrap:wrap}
  .dhead h1{font-family:var(--display);font-weight:700;font-size:1.75rem;letter-spacing:-.02em;margin:8px 0 4px}
  .dhead .orig{margin:0;color:var(--muted);font-size:.86rem}
  .dhead__a{display:flex;gap:8px;flex-wrap:wrap;align-items:center;position:relative}
  .ver{font-weight:700;font-size:.82rem}
  /* lifecycle: where this SOP is, and what comes next */
  .life{display:flex;list-style:none;margin:0 0 16px;padding:0;border:1px solid var(--line);border-radius:14px;background:var(--panel);overflow:hidden}
  .life li{flex:1;position:relative;display:flex;align-items:center;gap:8px;padding:12px 14px 12px 22px;font-size:.8rem;font-weight:600;color:var(--muted);white-space:nowrap}
  .life li:first-child{padding-left:16px}
  .life li + li::before{content:"";position:absolute;left:-7px;top:50%;width:12px;height:12px;border-top:1px solid var(--line-2);border-right:1px solid var(--line-2);transform:translateY(-50%) rotate(45deg);background:inherit}
  .life b{width:20px;height:20px;border-radius:50%;flex:none;display:grid;place-items:center;font-size:.66rem;background:var(--bg-soft);color:var(--muted)}
  .life .is-done{color:var(--ink)}
  .life .is-done b{background:rgba(63,143,95,.14);color:var(--success)}
  .life .is-cur{background:#FFF0E8;color:#8A4B2F}
  .life .is-cur b{background:var(--rose);color:#fff}
  .life small{display:block;font-weight:500;font-size:.72rem;opacity:.8}
  .banner{display:flex;align-items:center;gap:12px;flex-wrap:wrap;padding:12px 16px;border-radius:12px;margin:0 0 16px;font-size:.88rem}
  .banner > span{flex:1;min-width:220px}
  .banner--info{background:rgba(62,111,166,.08);color:#2D5482}
  .banner--warn{background:var(--amber-soft);color:#7A560F}
  .banner--ok{background:rgba(63,143,95,.09);color:#2F6E48}
  .banner--muted{background:var(--bg-soft);color:var(--muted)}
  .dgrid{display:grid;grid-template-columns:minmax(0,1fr) 300px;gap:20px;align-items:start}
  .doc{padding:6px 26px 26px}
  .ctl{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:1px;margin:20px 0 6px;border:1px solid var(--line);border-radius:12px;overflow:hidden;background:var(--line)}
  .ctl div{background:var(--panel);padding:10px 12px;min-width:0}
  .ctl dt{font-size:.64rem;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--muted)}
  .ctl dd{margin:2px 0 0;font-size:.86rem;font-weight:600}
  .ctl .ctl__t{grid-column:span 2}
  .ssec{padding:20px 0 4px;border-top:1px solid var(--line);margin-top:16px;scroll-margin-top:20px}
  .ssec:first-of-type{border-top:0}
  .ssec h2{display:flex;align-items:center;gap:10px;margin:0 0 8px;font-family:var(--display);font-weight:700;font-size:1.02rem}
  .ssec h2 .n{width:22px;height:22px;border-radius:7px;display:grid;place-items:center;background:var(--bg-soft);font-size:.7rem;color:var(--muted)}
  .ssec p{margin:0;font-size:.92rem;line-height:1.6}
  .ssec.is-miss{border:1.5px dashed rgba(217,154,43,.6);border-radius:12px;padding:14px 16px;margin-top:16px;background:rgba(217,154,43,.05)}
  .ssec.is-miss p{color:#8A6212}
  .ssec textarea{width:100%}
  .views{display:inline-flex;margin-left:auto;padding:3px;border-radius:999px;background:var(--bg-soft);gap:2px}
  .views button{height:28px;padding:0 12px;border:0;border-radius:999px;background:none;font:inherit;font-size:.76rem;font-weight:600;color:var(--muted);cursor:pointer;white-space:nowrap}
  .views button[aria-pressed="true"]{background:var(--panel);color:var(--ink);box-shadow:0 1px 3px rgba(36,26,20,.15)}
  .views button[disabled]{cursor:not-allowed;opacity:.55}
  .views button small{font-size:.62rem;font-weight:700;margin-left:4px}
  /* step-by-step */
  .steps{list-style:none;margin:6px 0 0;padding:0;display:grid;gap:10px;counter-reset:s}
  .step{display:grid;grid-template-columns:30px minmax(0,1fr);gap:4px 12px;padding:14px 16px;border:1px solid var(--line);border-radius:12px;background:var(--panel);counter-increment:s}
  .step::before{content:counter(s);grid-row:span 3;width:30px;height:30px;border-radius:50%;display:grid;place-items:center;background:var(--ink);color:#fff;font:700 .8rem var(--display)}
  .step.is-hl{border-color:rgba(232,93,117,.55);box-shadow:0 0 0 3px rgba(232,93,117,.12)}
  .step__t{font-size:.94rem;font-weight:600;line-height:1.45}
  .step__t[contenteditable="true"]{outline:1.5px dashed var(--line-2);border-radius:6px;padding:2px 4px;margin:-2px -4px}
  .step__m{display:flex;flex-wrap:wrap;gap:6px;align-items:center}
  .role{font-size:.72rem;font-weight:700;color:var(--muted)}
  .cite{display:inline-flex;align-items:center;gap:5px;height:24px;padding:0 8px;border-radius:7px;border:1px solid var(--line-2);font-size:.72rem;font-weight:600;color:var(--ink);background:var(--panel);white-space:nowrap;text-decoration:none}
  a.cite:hover{border-color:var(--rose);text-decoration:none}
  .cite svg{width:12px;height:12px;fill:none;stroke:currentColor;stroke-width:2;stroke-linecap:round;stroke-linejoin:round;color:var(--muted)}
  .cite--rule{border-color:rgba(63,143,95,.35);background:rgba(63,143,95,.06);color:#2F6E48}
  .cite--rule svg{color:var(--success)}
  .brs{display:grid;grid-template-columns:1fr 1fr;gap:8px;margin-top:6px}
  .br{padding:10px 12px;border-radius:10px;background:var(--bg-soft);font-size:.86rem}
  .br b{display:block;font-size:.7rem;font-weight:800;letter-spacing:.08em;text-transform:uppercase;color:var(--info);margin-bottom:2px}
  .subs{margin:4px 0 0;padding-left:18px;font-size:.86rem;color:var(--muted);display:grid;gap:2px}
  /* checklist */
  .chk{list-style:none;margin:6px 0 0;padding:0;border:1px solid var(--line);border-radius:12px;overflow:hidden}
  .chk li{display:grid;grid-template-columns:22px minmax(0,1fr) auto;gap:12px;align-items:start;padding:12px 16px;border-top:1px solid var(--line)}
  .chk li:first-child{border-top:0}
  .chk .box{width:18px;height:18px;margin-top:2px;border:1.5px solid var(--line-2);border-radius:5px}
  .chk small{display:block;color:var(--muted);font-size:.8rem}
  /* hierarchical */
  .tree,.tree ul{list-style:none;margin:0;padding:0}
  .tree{margin-top:6px;font-size:.9rem}
  .tree > li{padding:8px 0 8px 18px;border-left:2px solid var(--line-2);position:relative}
  .tree > li::before{content:"";position:absolute;left:-2px;top:20px;width:12px;border-top:2px solid var(--line-2)}
  .tree > li > b{font-weight:700}
  .tree ul{margin:6px 0 0 14px;padding-left:14px;border-left:1px dashed var(--line-2);display:grid;gap:4px;color:var(--muted)}
  .tree em{font-style:normal;font-weight:700;color:var(--info)}
  /* right rail */
  .rail{position:sticky;top:20px;display:grid;gap:14px}
  .rbox{padding:16px 18px}
  .rbox h3{margin:0 0 10px;font-size:.68rem;font-weight:800;letter-spacing:.12em;text-transform:uppercase;color:var(--muted);display:flex;align-items:center}
  .rbox h3 span{margin-left:auto;letter-spacing:0;text-transform:none;font-weight:600;font-size:.76rem}
  .toc{list-style:none;margin:0;padding:0;display:grid;gap:1px}
  .toc a{display:flex;align-items:center;gap:8px;padding:5px 8px;border-radius:8px;font-size:.84rem;font-weight:500;color:var(--ink)}
  .toc a:hover{background:var(--bg-soft);text-decoration:none}
  .toc i{width:16px;height:16px;border-radius:50%;flex:none;display:grid;place-items:center;font-style:normal;font-size:.6rem;font-weight:800;background:rgba(63,143,95,.14);color:var(--success)}
  .toc .is-miss i{background:var(--amber-soft);color:#8A6212}
  .toc .is-miss{color:#8A6212}
  .rlist{list-style:none;margin:0;padding:0;display:grid;gap:8px;font-size:.84rem}
  .rlist a{color:var(--ink);font-weight:600}
  .rlist small{display:block;color:var(--muted);font-size:.76rem}
  .vers li{display:grid;grid-template-columns:auto 1fr;gap:0 10px}
  .vers b{font:700 .78rem ui-monospace,Menlo,monospace}
  .live{display:grid;gap:6px;font-size:.84rem}
  .live div{display:flex;align-items:center;gap:8px}
  .live i{width:8px;height:8px;border-radius:50%;background:var(--line-2)}
  .live.is-on i{background:var(--success)}
  .live span{margin-left:auto;color:var(--muted);font-size:.76rem}
  .editbar{position:sticky;bottom:16px;z-index:20;display:flex;gap:10px;align-items:center;margin-top:18px;padding:12px 14px;border-radius:14px;background:var(--ink);color:#fff;box-shadow:0 20px 40px -20px rgba(36,26,20,.6)}
  .editbar span{flex:1;font-size:.86rem}
  .editbar .btn--secondary{background:transparent;color:#fff;border-color:rgba(255,255,255,.3)}
  .xpop{position:absolute;right:0;top:calc(100% + 6px);z-index:30;width:200px;background:var(--panel);border:1px solid var(--line);border-radius:12px;box-shadow:0 24px 50px -24px rgba(36,26,20,.45);padding:6px}
  /* drafting: the template fills in, one section at a time */
  .drafting{max-width:560px;margin:40px auto;padding:28px}
  .drafting h2{font-family:var(--display);font-size:1.3rem;margin:0 0 4px}
  .drafting ol{list-style:none;margin:18px 0 0;padding:0;display:grid;gap:6px}
  .drafting li{display:flex;align-items:center;gap:10px;font-size:.9rem;color:var(--muted)}
  .drafting li i{width:18px;height:18px;border-radius:50%;flex:none;display:grid;place-items:center;font-style:normal;font-size:.62rem;font-weight:800;background:var(--bg-soft)}
  .drafting li.is-done{color:var(--ink)}
  .drafting li.is-done i{background:rgba(63,143,95,.14);color:var(--success)}
  .drafting li.is-miss i{background:var(--amber-soft);color:#8A6212}
  .drafting li.is-now i{border:2px solid var(--rose);border-right-color:transparent;animation:spin .7s linear infinite}
  /* dialogs */
  .dlg--xl{width:min(680px,calc(100vw - 32px))}
  .impl{list-style:none;margin:0;padding:0;display:grid;gap:8px}
  .impl li{display:grid;grid-template-columns:36px minmax(0,1fr) auto;gap:4px 12px;align-items:center;padding:12px;border:1px solid var(--line);border-radius:12px}
  .impl .mono{width:36px;height:36px;border-radius:10px;font-size:.66rem;color:var(--muted);background:var(--bg-soft)}
  .impl b{display:block;font-size:.9rem}
  .impl small{display:block;color:var(--muted);font-size:.78rem}
  .impl .acts2{display:flex;gap:6px}
  .askin{display:flex;gap:8px;align-items:center}
  .askin span{font-weight:600;white-space:nowrap}
  .sugg{display:flex;gap:6px;flex-wrap:wrap;margin-top:10px}
  .diff{display:grid;gap:8px;font-size:.88rem}
  .diff del,.diff ins{display:block;padding:8px 10px;border-radius:8px;text-decoration:none}
  .diff del{background:rgba(198,69,69,.08);color:#9A3333}
  .diff del::before{content:"− ";font-weight:800}
  .diff ins{background:rgba(63,143,95,.1);color:#2F6E48}
  .diff ins::before{content:"+ ";font-weight:800}
  .diff small{font-size:.7rem;font-weight:800;letter-spacing:.08em;text-transform:uppercase;color:var(--muted)}
  :root[data-theme="dark"] .st.is-main{background:rgba(232,93,117,.08)}
  :root[data-theme="dark"] .st__ic,:root[data-theme="dark"] .life .is-cur{background:rgba(232,93,117,.14);color:#FFB199}
  :root[data-theme="dark"] .banner--info{color:#9FC0E6}
  :root[data-theme="dark"] .banner--warn,:root[data-theme="dark"] .ssec.is-miss p{color:#E8C27A}
  :root[data-theme="dark"] .banner--ok,:root[data-theme="dark"] .cite--rule{color:#8FD1A8}
  .ssec h2{flex-wrap:wrap}
  @media (max-width:1100px){.starts{grid-template-columns:1fr 1fr}.dgrid{grid-template-columns:minmax(0,1fr)}.rail{position:static}}
  @media (max-width:760px){.starts{grid-template-columns:1fr}.ctl{grid-template-columns:1fr 1fr}.life{flex-wrap:wrap}.life li{flex:1 1 45%;white-space:normal;padding-left:14px}.life li + li::before{display:none}.brs{grid-template-columns:1fr}.stbl .hide-s{display:none}.doc{padding:4px 16px 18px}.views{margin-left:0;overflow-x:auto;max-width:100%}.back{margin-left:56px;margin-top:8px}}
  @media print{.side,.fab,.mnav,.dhead__a,.rail,.life,.banner,.back,.views,.toast{display:none!important}.main{margin:0}.dgrid{display:block}.doc{border:0;padding:0}}
""",
  body=r"""
    <div class="head" id="sopHead">
      <div>
        <p class="label">Decide</p>
        <h1>SOPs</h1>
        <p>Approved, owned procedures your team follows. Every step cites where it came from, and rules link to approved answers instead of being copied.</p>
      </div>
    </div>
    <div id="sopList">
      <section id="starts" aria-labelledby="startH">
        <p class="seclbl" id="startH">Start an SOP</p>
        <div class="starts">
          <a class="st is-main" href="build.html?tab=approved&amp;sop=new"><span class="st__ic"><svg viewBox="0 0 24 24"><path d="M9 11l3 3 8-8"/><path d="M20 12v7a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h9"/></svg></span><b>From approved answers</b><span>Pick an answer in Build and press Link to SOP</span></a>
          <button class="st" type="button" data-start="import"><span class="st__ic"><svg viewBox="0 0 24 24"><path d="M12 3v12M7 10l5 5 5-5M5 21h14"/></svg></span><b>Import a document</b><span id="impHint">Documents lojo marked as procedures</span></button>
          <button class="st" type="button" data-start="ask"><span class="st__ic"><svg viewBox="0 0 24 24"><path d="M12 3l1.8 4.7L18.5 9.5l-4.7 1.8L12 16l-1.8-4.7L5.5 9.5l4.7-1.8z"/></svg></span><b>Ask lojo to write one</b><span>In Ask lojo: “Write the SOP for refund escalations”</span></button>
          <button class="st" type="button" data-start="ext"><span class="st__ic"><svg viewBox="0 0 24 24"><path d="M10 13a5 5 0 0 0 7.5.5l3-3a5 5 0 0 0-7-7l-1.7 1.7"/><path d="M14 11a5 5 0 0 0-7.5-.5l-3 3a5 5 0 0 0 7 7l1.7-1.7"/></svg></span><b>Link an external SOP</b><span>Keep it in Notion or Drive, with an owner and review date</span></button>
        </div>
      </section>
      <div class="flow" id="flow" aria-label="Filter by stage"></div>
      <section class="card" style="overflow:auto"><table class="stbl">
        <thead><tr><th>SOP</th><th>Stage</th><th class="hide-s">Version</th><th class="hide-s">Owner</th><th>Next review</th><th class="hide-s">Steps</th></tr></thead>
        <tbody id="rows"></tbody>
      </table></section>
    </div>
    <div id="sopDetail" hidden></div>
    <dialog class="dlg dlg--wide" id="sDlg" aria-labelledby="sDlgH"></dialog>
""",
  js=r"""
const P = new URLSearchParams(location.search);
const ROLE = window.LOJO_ROLE || 'admin', ME = ROLE_PERSON[ROLE] || 'p1';
const VIEWER = ROLE === 'viewer';
const person = (id) => ST.people.find(p => p.id === id) || { name: 'Someone' };
const inits = (n) => n.split(/\s+/).map(w => w[0]).join('').slice(0, 2).toUpperCase();
const avatar = (id) => { const n = person(id).name; return '<span class="avs ' + tone(n) + '">' + inits(n) + '</span>'; };
const statusBadge = (s) => '<span class="badge badge--' + SOP_STATUS[s.status][1] + '">' + SOP_STATUS[s.status][0] + '</span>';
const IC = {
  call: '<svg viewBox="0 0 24 24"><path d="M5 4h3l2 5-2.5 1.5a11 11 0 0 0 6 6L15 14l5 2v3a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2"/></svg>',
  mail: '<svg viewBox="0 0 24 24"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/></svg>',
  doc: '<svg viewBox="0 0 24 24"><path d="M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8z"/><path d="M14 3v5h5"/></svg>',
  answer: '<svg viewBox="0 0 24 24"><path d="M9 11l3 3 8-8"/><path d="M20 12v7a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h9"/></svg>',
  out: '<svg viewBox="0 0 24 24"><path d="M14 4h6v6M20 4l-9 9M18 14v5a1 1 0 0 1-1 1H5a1 1 0 0 1-1-1V7a1 1 0 0 1 1-1h5"/></svg>',
};
const FROM = { answers: 'Built from approved answers', import: 'Imported from a document', ask: 'Written by lojo on request', external: 'External' };
const missingOf = (s) => s.from === 'external' ? [] : SOP_SECTIONS.filter(([k]) => k === 'steps' ? !s.steps.length : k !== 'history' && !s.sec[k]).map(x => x[0]);
const visible = () => ST.sops.filter(s => !VIEWER || ['approved', 'due'].includes(s.status));
const linkedAnswers = (s) => [...new Set(s.steps.filter(x => x.ans).map(x => x.ans).concat(Object.keys(ST.sopLinks).filter(r => ST.sopLinks[r].sop === s.id)))];
const isLate = (s) => s.status === 'due';
let filter = 'all', view = null, editing = false, xOpen = false;

/* ---------------- list ---------------- */
const STAGES = ['draft', 'review', 'approved', 'due', 'retired'];
function renderList() {
  const all = visible(), n = (k) => all.filter(s => s.status === k).length;
  const stages = VIEWER ? ['approved', 'due'] : STAGES;
  $('flow').innerHTML = '<button type="button" data-f="all" aria-pressed="' + (filter === 'all') + '">All <em>' + all.length + '</em></button><span class="sep"></span>' +
    stages.map((k, i) => (k === 'retired' ? '<span class="sep"></span>' : i ? '<span class="arr" aria-hidden="true">→</span>' : '') +
      '<button type="button" data-f="' + k + '" aria-pressed="' + (filter === k) + '"><i class="dot-' + k + '"></i>' + SOP_STATUS[k][0] + ' <em>' + n(k) + '</em></button>').join('');
  const list = all.filter(s => filter === 'all' || s.status === filter);
  $('rows').innerHTML = list.length ? list.map(s => {
    const ext = s.from === 'external';
    return '<tr tabindex="0" data-id="' + s.id + '"' + (s.status === 'retired' ? ' class="is-retired"' : '') + '><td class="t"><b>' + esc(s.title) + '</b><small><span class="sid">' + s.id + '</span>' +
      (ext ? '<span class="ext">' + IC.out + 'External · ' + esc(s.ext.app) + '</span>' : esc(FROM[s.from])) + '</small></td>' +
      '<td>' + statusBadge(s) + (s.status !== 'retired' && missingOf(s).length ? ' <span class="badge badge--amber">' + missingOf(s).length + ' missing</span>' : '') + '</td>' +
      '<td class="hide-s ver">' + (ext ? '—' : 'v' + s.ver) + '</td><td class="hide-s"><span class="who">' + avatar(s.owner) + esc(person(s.owner).name) + '</span></td>' +
      '<td>' + (s.status === 'retired' ? '<span class="sub">—</span>' : s.next ? '<span' + (isLate(s) ? ' class="late"' : '') + '>' + esc(s.next) + (isLate(s) ? ' · overdue' : '') + '</span>' : '<span class="sub">After approval</span>') + '</td>' +
      '<td class="hide-s">' + (ext ? '<span class="sub">In ' + esc(s.ext.app) + '</span>' : s.steps.length) + '</td></tr>';
  }).join('') : '<tr><td colspan="6"><div class="empty"><b>No SOPs at this stage.</b>Pick another stage, or start one above.</div></td></tr>';
}
$('flow').addEventListener('click', (e) => { const b = e.target.closest('[data-f]'); if (b) { filter = b.dataset.f; renderList(); } });
$('rows').addEventListener('click', (e) => { const r = e.target.closest('tr[data-id]'); if (r) openSop(r.dataset.id); });
$('rows').addEventListener('keydown', (e) => { const r = e.target.closest('tr[data-id]'); if (r && (e.key === 'Enter' || e.key === ' ')) { e.preventDefault(); openSop(r.dataset.id); } });

/* ---------------- one SOP ---------------- */
function openSop(id, push = true) {
  view = id; editing = false; xOpen = false;
  if (push) history.pushState({ id }, '', 'sops.html?id=' + encodeURIComponent(id));
  render(); scrollTo(0, 0);
}
window.addEventListener('popstate', () => { view = new URLSearchParams(location.search).get('id'); editing = false; render(); });
const LIFE = [['draft', 'Draft'], ['review', 'In review'], ['approved', 'Approved'], ['due', 'Due for review'], ['end', 'Revised or retired']];
function lifeHtml(s) {
  const at = s.status === 'retired' ? 4 : LIFE.findIndex(x => x[0] === s.status);
  const note = { draft: 'Being written', review: 'Waiting for the approver', approved: 'In use · v' + s.ver, due: 'Was due ' + s.next, end: s.status === 'retired' ? 'Retired' : 'Any change goes back to review' };
  return '<ol class="life" aria-label="Lifecycle">' + LIFE.map(([k, l], i) => '<li class="' + (i < at ? 'is-done' : i === at ? 'is-cur' : '') + '"' + (i === at ? ' aria-current="step"' : '') + '><b>' + (i < at ? '✓' : i + 1) + '</b><span>' + l + (i === at ? '<small>' + esc(note[k]) + '</small>' : '') + '</span></li>').join('') + '</ol>';
}
function cite(st) {
  const src = '<span class="cite" title="Source">' + IC[st.src[0]] + esc(st.src[1]) + '</span>';
  if (!st.ans) return src;
  return '<a class="cite cite--rule" href="build.html?tab=approved&amp;sel=' + st.ans + '" title="The rule lives in this approved answer. It isn’t copied here.">' + IC.answer + 'Rule · ' + esc(st.src[0] === 'answer' ? st.src[1] : allQuestions().find(q => q.id === DRAFTS.find(x => x.id === st.ans).qid).q.replace(/\?$/, '')) + '</a>' + (st.src[0] === 'answer' ? '' : src);
}
function stepsHtml(s) {
  const hl = P.get('step') !== null && P.get('id') === s.id ? +P.get('step') : -1;
  if (s.fmt === 'check') return '<ul class="chk">' + s.steps.map((st, i) => '<li><i class="box" aria-hidden="true"></i><span><span class="step__t" data-i="' + i + '"' + (editing ? ' contenteditable="true"' : '') + '>' + esc(st.t) + '</span><small>' + esc(st.who) + '</small></span><span class="step__m">' + cite(st) + '</span></li>').join('') + '</ul>';
  if (s.fmt === 'tree') return '<ul class="tree">' + s.steps.map((st, i) => '<li><b class="step__t" data-i="' + i + '"' + (editing ? ' contenteditable="true"' : '') + '>' + (i + 1) + '. ' + esc(st.t) + '</b> <span class="role">· ' + esc(st.who) + '</span>' +
    ((st.br || st.sub) ? '<ul>' + (st.br || []).map(b => '<li><em>' + esc(b[0]) + ':</em> ' + esc(b[1]) + '</li>').join('') + (st.sub || []).map(x => '<li>' + esc(x) + '</li>').join('') + '</ul>' : '') + '</li>').join('') + '</ul>';
  return '<ol class="steps">' + s.steps.map((st, i) => '<li class="step' + (i === hl ? ' is-hl' : '') + '"><span class="step__t" data-i="' + i + '"' + (editing ? ' contenteditable="true"' : '') + '>' + esc(st.t) + '</span>' +
    '<span class="step__m"><span class="role">' + esc(st.who) + '</span>' + cite(st) + '</span>' +
    (st.br ? '<div class="brs">' + st.br.map(b => '<div class="br"><b>' + esc(b[0]) + '</b>' + esc(b[1]) + '</div>').join('') + '</div>' : '') +
    (st.sub ? '<ul class="subs">' + st.sub.map(x => '<li>' + esc(x) + '</li>').join('') + '</ul>' : '') + '</li>').join('') + '</ol>';
}
function canApprove(s) { return ME === s.approver; }
function actionsHtml(s) {
  if (VIEWER) return exportBtn(s);
  if (editing) return '';
  const ext = s.from === 'external';
  const b = (a, l, cls) => '<button class="btn ' + (cls || 'btn--secondary') + '" type="button" data-a="' + a + '">' + l + '</button>';
  if (s.status === 'review') return (canApprove(s) ? '<button class="btn btn--primary" type="button" data-a="approve">Approve and publish v' + nextVer(s, true) + '</button>' : '') + b('edit', 'Edit');
  if (s.status === 'draft') return b('submit', 'Send for review', 'btn--primary') + b('edit', 'Edit');
  if (s.status === 'due') return (ext ? '' : b('revise', 'Revise · starts v' + nextVer(s), 'btn--primary')) + exportBtn(s) + b('retire', 'Retire', ext ? 'btn--secondary' : 'btn--ghost');
  if (s.status === 'approved') return (ext ? '<a class="btn btn--primary" href="https://' + esc(s.ext.url) + '" target="_blank" rel="noopener">' + IC.out.replace('<svg', '<svg class="ic14"') + 'Open in ' + esc(s.ext.app) + '</a>' : b('revise', 'Edit · starts v' + nextVer(s))) + exportBtn(s) + b('retire', 'Retire', 'btn--ghost');
  return exportBtn(s);
}
function exportBtn(s) {
  if (s.from === 'external') return '';
  return '<button class="btn btn--secondary" type="button" data-a="export" aria-expanded="' + xOpen + '">Export</button>' +
    (xOpen ? '<div class="xpop" role="menu"><button class="pop__row" type="button" data-a="pdf" role="menuitem">PDF</button><button class="pop__row" type="button" data-a="word" role="menuitem">Word (.doc)</button></div>' : '');
}
function nextVer(s, publish) {
  if (publish) return s.ver.startsWith('0.') ? '1.0' : s.ver;
  const [a, b] = s.ver.split('.').map(Number); return a + '.' + (b + 1);
}
function bannerHtml(s) {
  const miss = missingOf(s), names = miss.map(k => SOP_SECTIONS.find(x => x[0] === k)[1]);
  let h = '';
  if (s.status === 'review') h += '<div class="banner banner--info"><span>' + (canApprove(s) ? '<b>Your approval is needed.</b> ' : '<b>Waiting for ' + esc(person(s.approver).name) + ' to approve.</b> ') + (s.by ? 'Sent by ' + esc(s.by) + ' ' + esc(s.sent || '') + '. ' : '') + 'Nobody sees it in Ask lojo until it’s approved.</span></div>';
  if (miss.length && s.status !== 'retired') h += '<div class="banner banner--warn"><span><b>' + miss.length + ' section' + (miss.length === 1 ? '' : 's') + ' missing:</b> ' + esc(names.join(', ')) + '. The document didn’t cover ' + (miss.length === 1 ? 'it' : 'them') + '.</span></div>';
  if (s.status === 'due') h += '<div class="banner banner--warn"><span><b>Review was due ' + esc(s.next) + '.</b> Revise it or retire it. It stays in use meanwhile.</span></div>';
  if (s.status === 'retired') h += '<div class="banner banner--muted"><span>Retired. Archived, never deleted.</span></div>';
  if (s.from === 'external' && s.status !== 'retired') h += '<div class="banner banner--muted"><span>This SOP lives in ' + esc(s.ext.app) + '. lojo keeps its owner and review date, and approved answers can link to it.</span></div>';
  return h;
}
function render() {
  document.body.classList.toggle('is-detail', !!view);
  $('sopDetail').hidden = !view;
  if (!view) { renderList(); return; }
  const s = sopById(view);
  if (!s || (VIEWER && !['approved', 'due'].includes(s.status))) { $('sopDetail').innerHTML = '<a class="back" href="sops.html" data-back>← SOPs</a><div class="card empty"><b>This SOP isn’t available.</b>It may be waiting for approval.</div>'; return; }
  const ext = s.from === 'external', miss = missingOf(s), ans = linkedAnswers(s);
  let h = '<a class="back" href="sops.html" data-back>← SOPs</a>' +
    '<div class="dhead"><div class="dhead__t"><div class="dhead__m"><span class="sid">' + s.id + '</span>' + statusBadge(s) + (ext ? '' : '<span class="ver">v' + s.ver + '</span>') + '</div><h1>' + esc(s.title) + '</h1>' +
    '<p class="orig">' + (ext ? 'External · ' + esc(s.ext.app) : esc(FROM[s.from])) + ' · owned by ' + esc(person(s.owner).name) + '</p></div><div class="dhead__a">' + actionsHtml(s) + '</div></div>' +
    lifeHtml(s) + bannerHtml(s);
  const ctl = [['Title', s.title, 'ctl__t'], ['ID', s.id], ['Version', ext ? '—' : 'v' + s.ver], ['Effective', s.eff || 'On approval'], ['Owner', person(s.owner).name], ['Approver', person(s.approver).name], ['Next review', (s.next || 'On approval') + ' · every ' + SOP_RISK[s.risk] + ' mo, ' + s.risk.toLowerCase() + ' risk']];
  let doc = '<dl class="ctl" aria-label="Control header">' + ctl.map(([k, v, c]) => '<div' + (c ? ' class="' + c + '"' : '') + '><dt>' + k + '</dt><dd title="' + esc(v) + '">' + esc(v) + '</dd></div>').join('') + '</dl>';
  if (ext) doc += '<section class="ssec"><h2>Where it lives</h2><p><a href="https://' + esc(s.ext.url) + '" target="_blank" rel="noopener">' + esc(s.ext.url) + '</a></p></section>';
  else SOP_SECTIONS.forEach(([k, l], i) => {
    const m = miss.includes(k);
    let inner;
    if (k === 'steps') inner = s.steps.length ? stepsHtml(s) : '<p>No steps yet.</p>';
    else if (k === 'history') inner = '<ul class="rlist vers">' + s.hist.slice().reverse().map(x => '<li><b>v' + x[0] + '</b><span>' + esc(x[3]) + '<small>' + esc(x[2]) + ' · ' + esc(x[1]) + '</small></span></li>').join('') + '</ul>';
    else if (editing) inner = '<textarea class="text" data-sec="' + k + '" rows="2" placeholder="Write the ' + l.toLowerCase() + '">' + esc(s.sec[k] || '') + '</textarea>';
    else inner = '<p>' + (m ? 'Missing. The document didn’t say.' : esc(s.sec[k])) + '</p>';
    const vw = k === 'steps' && s.steps.length ? '<span class="views" role="group" aria-label="Show the procedure as">' + Object.keys(SOP_FORMATS).map(f => '<button type="button" data-fmt="' + f + '" aria-pressed="' + (s.fmt === f) + '">' + SOP_FORMATS[f] + '</button>').join('') + '</span>' : '';
    doc += '<section class="ssec' + (m ? ' is-miss' : '') + '" id="s-' + k + '"><h2><span class="n">' + (i + 1) + '</span>' + l + vw + '</h2>' + inner + '</section>';
  });
  if (editing) doc += '<div class="editbar"><span>' + (s.status === 'approved' || s.status === 'due' ? 'Saving starts v' + nextVer(s) + ' and sends it for review. v' + s.ver + ' stays in use until then.' : 'Edit the sections and steps, then save.') + '</span><button class="btn btn--secondary" type="button" data-a="cancel">Cancel</button><button class="btn btn--grad" type="button" data-a="save">' + (s.status === 'approved' || s.status === 'due' ? 'Save as v' + nextVer(s) + ' and send for review' : 'Save changes') + '</button></div>';
  const isLive = ['approved', 'due'].includes(s.status);
  const rail = (ext ? '' : '<div class="card rbox"><h3>Sections <span>' + (10 - miss.length) + ' of 10</span></h3><ol class="toc">' + SOP_SECTIONS.map(([k, l]) => '<li' + (miss.includes(k) ? ' class="is-miss"' : '') + '><a href="#s-' + k + '"><i>' + (miss.includes(k) ? '!' : '✓') + '</i>' + l + '</a></li>').join('') + '</ol></div>') +
    (ans.length ? '<div class="card rbox"><h3>Linked answers <span>' + ans.length + '</span></h3><ul class="rlist">' + ans.map(r => { const d = DRAFTS.find(x => x.id === r); const st = decision(d).status;
      return '<li><a href="build.html?sel=' + r + '">' + esc(allQuestions().find(q => q.id === d.qid).q) + '</a><small>' + (st === 'approved' ? 'Approved answer' : 'In review in Build') + '</small></li>'; }).join('') + '</ul><p class="sub" style="margin-top:10px">Rules stay in these answers and aren’t copied into the SOP.</p></div>' : '') +
    (s.hist.length > 1 || s.diff ? '<div class="card rbox"><h3>Versions <span>' + s.hist.length + '</span></h3><ul class="rlist vers">' + s.hist.slice().reverse().slice(0, 3).map((x, i) => '<li><b>v' + x[0] + '</b><span>' + esc(x[3]) + '<small>' + esc(x[1]) + (i === 0 && isLive ? ' · current' : '') + '</small></span></li>').join('') + '</ul>' +
      (s.diff ? '<button class="btn btn--secondary btn--sm" type="button" data-a="diff" style="margin-top:12px">Compare v' + s.hist[s.hist.length - 2][0] + ' → v' + s.hist[s.hist.length - 1][0] + '</button>' : '') + '</div>' : '') +
    '<div class="card rbox"><h3>Available in</h3><div class="live' + (isLive ? ' is-on' : '') + '">' + ['Ask lojo', 'Brain API', 'MCP'].map(x => '<div><i></i>' + x + '<span>' + (isLive ? 'Live' : 'After approval') + '</span></div>').join('') + '</div></div>';
  h += '<div class="dgrid"><article class="card doc">' + doc + '</article><aside class="rail">' + rail + '</aside></div>';
  $('sopDetail').innerHTML = h;
  if (P.get('step') !== null) { const el = document.querySelector('.step.is-hl'); if (el) el.scrollIntoView({ block: 'center' }); }
}
function readEdits(s) {
  document.querySelectorAll('#sopDetail [data-sec]').forEach(t => { s.sec[t.dataset.sec] = t.value.trim() || null; });
  document.querySelectorAll('#sopDetail .step__t[data-i]').forEach(t => { s.steps[+t.dataset.i].t = t.textContent.replace(/^\d+\.\s*/, '').trim(); });
}
function act(a) {
  const s = sopById(view); if (!s) return;
  if (a === 'export') { xOpen = !xOpen; render(); return; }
  xOpen = false;
  if (a === 'pdf') { render(); setTimeout(print, 50); return; }
  if (a === 'word') { exportWord(s); render(); return; }
  if (a === 'edit' || a === 'revise') { editing = true; render(); const t = document.querySelector('#sopDetail [contenteditable], #sopDetail textarea'); if (t) t.focus(); return; }
  if (a === 'cancel') { editing = false; render(); return; }
  if (a === 'save') {
    const before = s.steps.map(x => x.t);
    readEdits(s); editing = false;
    if (s.status === 'approved' || s.status === 'due') {
      const v = nextVer(s), changed = s.steps.map((x, i) => [i + 1, before[i], x.t]).filter(x => x[1] !== x[2]);
      s.diff = changed.length ? changed : null;
      s.ver = v; s.status = 'review'; s.by = person(ME).name; s.sent = 'just now'; s.hist.push([v, 'Today', person(ME).name, 'Revision sent for review']);
      toast('Saved as v' + v + '. It’s waiting for ' + person(s.approver).name.split(' ')[0] + '’s approval.');
    } else toast('Saved');
    save(); render(); return;
  }
  if (a === 'approve') {
    const v = nextVer(s, true); s.ver = v; s.status = 'approved'; s.eff = sopToday(); s.next = sopPlus(SOP_RISK[s.risk]);
    const last = s.hist[s.hist.length - 1]; if (last && last[0] !== v) s.hist.push([v, 'Today', person(ME).name, 'Approved and published']); else if (last) last[3] += ', approved by ' + person(ME).name;
    save(); render(); toast('Published v' + v + '. Ask lojo, the Brain API and MCP use it now.'); return;
  }
  if (a === 'submit') { s.status = 'review'; s.by = person(ME).name; s.sent = 'just now'; save(); render(); toast('Sent to ' + person(s.approver).name + ' for approval'); return; }
  if (a === 'diff') return openDiff(s);
  if (a === 'retire') return openRetire(s);
}
$('sopDetail').addEventListener('click', (e) => {
  const bk = e.target.closest('[data-back]'); if (bk) { e.preventDefault(); view = null; history.pushState({}, '', 'sops.html'); render(); return; }
  const f = e.target.closest('[data-fmt]'); if (f) { const s = sopById(view); if (editing) readEdits(s); s.fmt = f.dataset.fmt; save(); render(); return; }
  const b = e.target.closest('[data-a]'); if (b) act(b.dataset.a);
});
document.addEventListener('click', (e) => { if (xOpen && !e.target.closest('.dhead__a')) { xOpen = false; render(); } });
document.addEventListener('keydown', (e) => { if (e.key === 'Escape' && xOpen) { xOpen = false; render(); } });
function exportWord(s) {
  const secs = SOP_SECTIONS.map(([k, l], i) => '<h2>' + (i + 1) + '. ' + l + '</h2>' + (k === 'steps' ? '<ol>' + s.steps.map(x => '<li>' + esc(x.t) + ' <i>(' + esc(x.who) + ' · ' + esc(x.src[1]) + ')</i></li>').join('') + '</ol>'
    : k === 'history' ? '<ul>' + s.hist.map(x => '<li>v' + x[0] + ' · ' + esc(x[1]) + ' · ' + esc(x[2]) + ': ' + esc(x[3]) + '</li>').join('') + '</ul>' : '<p>' + esc(s.sec[k] || '—') + '</p>')).join('');
  const html = '<html><head><meta charset="utf-8"><title>' + esc(s.title) + '</title></head><body><h1>' + s.id + ' · ' + esc(s.title) + '</h1><p>Version ' + s.ver + ' · Effective ' + esc(s.eff || '—') + ' · Owner ' + esc(person(s.owner).name) + ' · Approver ' + esc(person(s.approver).name) + ' · Next review ' + esc(s.next || '—') + '</p>' + secs + '</body></html>';
  const a = document.createElement('a'); a.href = URL.createObjectURL(new Blob([html], { type: 'application/msword' })); a.download = s.id + ' v' + s.ver + '.doc'; a.click();
  toast('Downloaded ' + s.id + ' v' + s.ver + '.doc');
}

/* ---------------- dialogs ---------------- */
const dlg = $('sDlg');
const shut = () => dlg.close();
dlg.addEventListener('close', () => dlg.classList.remove('dlg--xl'));
dlg.addEventListener('click', (e) => { if (e.target === dlg || e.target.closest('[data-close]')) shut(); });
const foot = (go, label, cls) => '<div class="dlg__f"><button class="btn btn--secondary" type="button" data-close>Cancel</button>' + (go ? '<button class="btn ' + (cls || 'btn--primary') + '" type="button" id="' + go + '">' + label + '</button>' : '') + '</div>';
function openDiff(s) {
  const a = s.hist[s.hist.length - 2], b = s.hist[s.hist.length - 1];
  dlg.innerHTML = '<div class="dlg__b"><p class="label">' + s.id + '</p><h3 id="sDlgH">v' + a[0] + ' → v' + b[0] + '</h3><p>' + esc(b[3]) + ' · ' + esc(b[2]) + ', ' + esc(b[1]) + '</p><div class="diff">' +
    s.diff.map(([n, o, x]) => '<small>Step ' + n + '</small>' + (o ? '<del>' + esc(o) + '</del>' : '') + '<ins>' + esc(x) + '</ins>').join('') + '</div></div><div class="dlg__f"><button class="btn btn--primary" type="button" data-close>Close</button></div>';
  dlg.showModal();
}
function openRetire(s) {
  dlg.innerHTML = '<div class="dlg__b"><h3 id="sDlgH">Retire ' + esc(s.title) + '?</h3><p style="margin:0">It stops being used in Ask lojo, the Brain API and MCP. Old versions are archived, never deleted.</p></div>' + foot('rtGo', 'Retire', 'btn--danger');
  dlg.showModal();
  $('rtGo').addEventListener('click', () => { s.status = 'retired'; s.hist.push([s.ver, 'Today', person(ME).name, 'Retired']); save(); shut(); render(); toast('Retired'); });
}
// documents lojo has marked as procedures; a person can correct the mark
const IMPORTS = [
  { id: 'i1', name: 'Customer onboarding playbook', app: 'Notion', why: 'Numbered steps, roles and a checklist', title: 'Onboard a Scale customer', area: 'ONB', missing: ['defs', 'records'], rids: ['r6'],
    sec: { purpose: 'Get every Scale customer live in their first 30 days.', scope: 'New Scale customers, from signature to go-live.', resp: 'The onboarding manager runs the steps. The Head of Support Operations owns this SOP.', prereq: 'A signed Scale contract and a named onboarding manager.', cautions: 'Don’t book training before SSO works.', refs: 'Customer onboarding playbook (Notion) · Onboarding checklist.pdf' },
    steps: [['Name an onboarding manager within one working day of signature.', 'Sales lead'], ['Book the 60-minute kickoff with the customer’s admins.', 'Onboarding manager', 'r6'], ['Set up SSO before any training.', 'Customer IT'], ['Run two admin training sessions.', 'Onboarding manager', 'r6'], ['Confirm go-live with the customer by email.', 'Onboarding manager']] },
  { id: 'i2', name: 'Refund escalations (Ops wiki)', app: 'Notion', why: 'Steps with an approval over a limit', title: 'Escalate a large refund', area: 'BIL', missing: ['cautions'], rids: ['r2'],
    sec: { purpose: 'Get refunds over €500 approved within one working day.', scope: 'Refunds over €500 on any plan.', resp: 'Agent requests, Support Team Lead approves, Finance pays.', defs: 'Large refund: over €500 in one payment.', prereq: 'The refund worked out with SOP-BIL-001.', records: 'Approval and payout date on the ticket.', refs: 'Refund escalations (Notion)' },
    steps: [['Work out the refund with SOP-BIL-001.', 'Agent', 'r2'], ['If it’s over €500, ask the Support Team Lead in #refunds.', 'Agent'], ['The lead approves or declines within one working day.', 'Support Team Lead'], ['Finance pays and the agent confirms to the customer.', 'Finance']] },
  { id: 'i3', name: 'Security overview.pdf', app: 'Upload', why: 'Mostly facts, one short procedure', title: 'Export a workspace’s data', area: 'SEC', missing: ['resp', 'prereq', 'records'], rids: ['r15'],
    sec: { purpose: 'Give customers their data when they ask.', scope: 'Any workspace, on request from one of its admins.', defs: 'Export: all workspace data as one JSON file.', cautions: 'Only an admin of that workspace can ask for it.', refs: 'Security overview.pdf p. 8' },
    steps: [['Check the person asking is an admin of the workspace.', 'Agent'], ['Point them to Settings → Data → Export.', 'Agent', 'r15'], ['They download the JSON file.', 'Customer']] },
];
const impLeft = () => IMPORTS.filter(x => !(ST.sopImp || {})[x.id]);
function openImport() {
  const L = impLeft();
  dlg.classList.add('dlg--xl');
  dlg.innerHTML = '<div class="dlg__b"><h3 id="sDlgH">Import a document as an SOP</h3><p>lojo read your sources and marked these as procedures. It maps each into the 10 sections and flags what’s missing.</p>' +
    (L.length ? '<ul class="impl">' + L.map(x => '<li><span class="mono">' + (x.app === 'Notion' ? 'N' : 'PDF') + '</span><span><b>' + esc(x.name) + '</b><small>' + esc(x.app) + ' · ' + esc(x.why) + '</small></span><span class="acts2"><button class="btn btn--ghost btn--sm" type="button" title="lojo stops suggesting it" data-notproc="' + x.id + '">Not a procedure</button><button class="btn btn--primary btn--sm" type="button" data-imp="' + x.id + '">Import</button></span></li>').join('') + '</ul>'
      : '<div class="empty"><b>Nothing left to import.</b>New procedures show up here as lojo reads your sources.</div>') +
    '<p class="sub" style="margin:14px 0 0">Not listed? <a href="sources.html?src=upload">Upload it in Sources</a> and it shows up here.</p></div><div class="dlg__f"><button class="btn btn--secondary" type="button" data-close>Close</button></div>';
  dlg.showModal();
}
dlg.addEventListener('click', (e) => {
  const np = e.target.closest('[data-notproc]'); if (np) { ST.sopImp = ST.sopImp || {}; ST.sopImp[np.dataset.notproc] = 'no'; save(); openImport(); toast('Marked as not a procedure'); updImpHint(); return; }
  const im = e.target.closest('[data-imp]'); if (!im) return;
  const x = IMPORTS.find(y => y.id === im.dataset.imp); ST.sopImp = ST.sopImp || {}; ST.sopImp[x.id] = 'yes';
  const s = draftSop({ title: x.title, rids: x.rids, fmt: 'steps', from: 'import', by: person(ME).name, missing: x.missing, area: x.area, sec: x.sec,
    steps: x.steps.map(([t, who, ans]) => ({ t, who, ans, src: ['doc', x.name] })) });
  s.hist = [['0.1', 'Today', 'lojo', 'Imported from ' + x.name + ' (' + x.app + ')']];
  save(); shut(); drafting(s, 'Mapping ' + x.name + ' into the 10 sections');
});
function openExt() {
  dlg.innerHTML = '<div class="dlg__b" style="display:grid;gap:14px"><div><h3 id="sDlgH">Link an external SOP</h3><p style="margin:0">It stays where it is. lojo tracks its owner and review date, and approved answers can link to it.</p></div>' +
    '<div class="fld"><label for="exT">Title</label><input class="text" id="exT" placeholder="Handle a data breach"></div>' +
    '<div class="fld"><label for="exU">Link</label><input class="text" id="exU" placeholder="https://notion.so/…"></div>' +
    '<div class="fgrid"><div class="fld"><label for="exO">Owner</label><select class="text" id="exO">' + ST.people.filter(p => p.status === 'member').map(p => '<option value="' + p.id + '"' + (p.id === ME ? ' selected' : '') + '>' + esc(p.name) + '</option>').join('') + '</select></div>' +
    '<div class="fld"><label for="exR">Review every</label><select class="text" id="exR">' + Object.keys(SOP_RISK).map(k => '<option value="' + k + '"' + (k === 'Medium' ? ' selected' : '') + '>' + SOP_RISK[k] + ' months · ' + k.toLowerCase() + ' risk</option>').join('') + '</select></div></div></div>' + foot('exGo', 'Add SOP');
  dlg.showModal(); $('exT').focus();
  $('exGo').addEventListener('click', () => {
    const t = $('exT').value.trim(), u = $('exU').value.trim();
    if (!t) { $('exT').focus(); return; } if (!/^https?:\/\/\S+\.\S+/.test(u)) { $('exU').focus(); toast('Paste a full link'); return; }
    const host = u.replace(/^https?:\/\//, ''), app = /notion/.test(host) ? 'Notion' : /google|drive|docs\./.test(host) ? 'Google Drive' : /sharepoint|office/.test(host) ? 'SharePoint' : 'the web';
    const s = { id: 'SOP-EXT-' + String(Math.max(0, ...ST.sops.map(x => +x.id.split('-').pop() || 0)) + 1).padStart(3, '0'), title: t, status: 'approved', ver: '—', eff: sopToday(), next: sopPlus(SOP_RISK[$('exR').value]), owner: $('exO').value, approver: 'p1', risk: $('exR').value, from: 'external', ext: { app, url: host }, sec: {}, steps: [], hist: [] };
    ST.sops.unshift(s); save(); shut(); openSop(s.id); toast('External SOP added');
  });
}
$('starts').addEventListener('click', (e) => { const b = e.target.closest('[data-start]'); if (!b) return; ({ import: openImport, ask: askLojo, ext: openExt })[b.dataset.start](); });
// the doc puts "write the SOP for X" in Companion, so the card opens Ask lojo with the sentence started
function askLojo() { window.__openAsk(); const t = $('askIn'); t.value = 'Write the SOP for '; t.dispatchEvent(new Event('input')); t.focus(); t.setSelectionRange(t.value.length, t.value.length); }
function updImpHint() { const n = impLeft().length; $('impHint').textContent = n ? n + ' document' + (n === 1 ? '' : 's') + ' look like procedures' : 'Nothing new to import'; }
// the agent fills the template, one section at a time, then the SOP opens in review
function drafting(s, line) {
  view = s.id; history.pushState({ id: s.id }, '', 'sops.html?id=' + s.id);
  document.body.classList.add('is-detail'); $('sopDetail').hidden = false;
  const miss = missingOf(s);
  $('sopDetail').innerHTML = '<div class="card drafting" role="status"><p class="label">SOP builder agent</p><h2>' + esc(line || 'Drafting ' + s.title) + '</h2><p class="sub">Every step cites its source. It goes to review like any draft.</p><ol>' +
    SOP_SECTIONS.map(([k, l]) => '<li data-k="' + k + '"><i></i>' + l + '</li>').join('') + '</ol></div>';
  const lis = [...document.querySelectorAll('.drafting li')];
  lis.forEach((li, i) => setTimeout(() => { if (i) { const p = lis[i - 1], m = miss.includes(p.dataset.k); p.className = m ? 'is-miss' : 'is-done'; p.querySelector('i').textContent = m ? '!' : '✓'; } li.className = 'is-now'; }, i * 160));
  setTimeout(() => { editing = false; render(); scrollTo(0, 0); toast(miss.length ? 'Drafted. ' + miss.length + ' section' + (miss.length === 1 ? '' : 's') + ' missing' : 'Drafted and sent to review'); }, SOP_SECTIONS.length * 160 + 300);
}

/* ---------------- start ---------------- */
if (VIEWER) $('starts').hidden = true;
updImpHint();
view = P.get('id');
if (view && P.get('new')) { const s = sopById(view); history.replaceState({ id: view }, '', 'sops.html?id=' + view); if (s) drafting(s, 'Drafting ' + s.title + ' from ' + linkedAnswers(s).length + ' related answers'); else render(); }
else render();
""")

PAGES = {'readout': RO_PAGE, 'emails': EMAILS_PAGE, 'platform': PLATFORM, 'superadmin': SUPER, 'company': COMPANY, 'auditlog': AUDIT, 'account': ACCOUNT, 'people': PEOPLE, 'settings': SETTINGS, 'states': STATES, 'dashboard': OVERVIEW, 'sources': DOCUMENTS, 'insights': QUESTIONS_PAGE, 'build': REVIEW, 'distribute': APPROVED, 'chat': CHAT, 'knowledge': READOUT, 'sops': SOPS, 'activity': ACTIVITY}
for name, p in PAGES.items():
    html = page(p['active'], p['title'], p['css'], p['body'], p['js'], p.get('desc', ''), p.get('persona', 'admin'))
    with open(os.path.join(OUT, name + '.html'), 'w') as f:
        f.write(html)
    print('wrote', name + '.html', len(html))
