# Shared light/dark theme pieces, used by build.py (app screens) and stamped into onboarding.html / login.html.

HEAD_JS = """<script>
  (function () {
    var pref = 'system';
    try { pref = localStorage.getItem('lojo-theme') || 'system'; } catch (e) {}
    var dark = pref === 'dark' || (pref === 'system' && window.matchMedia && matchMedia('(prefers-color-scheme: dark)').matches);
    document.documentElement.setAttribute('data-theme', dark ? 'dark' : 'light');
    document.documentElement.setAttribute('data-theme-pref', pref);
  })();
</script>"""

SEG_CSS = r"""
  .theme-toggle{position:relative;display:inline-flex;align-items:center;justify-content:space-between;width:58px;height:30px;padding:0 7px;border-radius:999px;border:1px solid var(--line-2);background:var(--bg-soft);color:var(--muted);cursor:pointer;flex:none}
  .theme-toggle svg{position:relative;z-index:1;width:14px;height:14px;fill:none;stroke:currentColor;stroke-width:2;stroke-linecap:round;stroke-linejoin:round;transition:color .2s ease}
  .theme-toggle::before{content:"";position:absolute;top:3px;left:3px;width:22px;height:22px;border-radius:50%;background:var(--panel);box-shadow:0 1px 3px rgba(0,0,0,.18);transition:transform .25s cubic-bezier(.2,.8,.2,1)}
  .theme-toggle .t-sun{color:#C98A2E}
  :root[data-theme="dark"] .theme-toggle::before{transform:translateX(28px);background:#4A3A31}
  :root[data-theme="dark"] .theme-toggle .t-sun{color:var(--muted)}
  :root[data-theme="dark"] .theme-toggle .t-moon{color:#F2EBE5}

  .side .theme-toggle{flex-direction:column;width:30px;height:58px;padding:7px 0}
  :root[data-theme="dark"] .side .theme-toggle::before{transform:translateY(28px)}
"""

SEG_HTML = """<button class="theme-toggle" type="button" data-theme-toggle aria-label="Switch to dark mode" title="Dark mode"><svg class="t-sun" viewBox="0 0 24 24"><circle cx="12" cy="12" r="4"/><path d="M12 2.5v2M12 19.5v2M4.6 4.6l1.4 1.4M18 18l1.4 1.4M2.5 12h2M19.5 12h2M4.6 19.4 6 18M18 6l1.4-1.4"/></svg><svg class="t-moon" viewBox="0 0 24 24"><path d="M20.5 14.2A8.5 8.5 0 0 1 9.8 3.5a8.5 8.5 0 1 0 10.7 10.7z"/></svg></button>"""

SEG_JS = r"""
(function themeToggle() {
  const root = document.documentElement;
  const sync = () => {
    const dark = root.getAttribute('data-theme') === 'dark';
    document.querySelectorAll('[data-theme-toggle]').forEach(b => { b.setAttribute('aria-pressed', dark); b.setAttribute('aria-label', dark ? 'Switch to light mode' : 'Switch to dark mode'); b.title = dark ? 'Light mode' : 'Dark mode'; });
  };
  sync();
  document.addEventListener('click', (e) => {
    if (!e.target.closest('[data-theme-toggle]')) return;
    const next = root.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
    root.setAttribute('data-theme', next);
    try { localStorage.setItem('lojo-theme', next); } catch (err) {}
    sync();
  });
})();
"""

# tokens + overrides for things that use fixed light colours
DARK_BASE = r"""
  :root[data-theme="dark"]{
    --ink:#F2EBE5; --bg:#15100D; --bg-soft:#231B16; --panel:#1C1612;
    --line:rgba(255,236,222,.08); --line-2:rgba(255,236,222,.16); --muted:#B3A398; --cream:#F6EEE6;
    --amber-soft:#3B2F1A; --success:#6BC08F; --error:#EC7B7B; --info:#86AEDD;
    color-scheme:dark;
  }
  :root[data-theme="dark"] body{background-color:#120E0B;background-image:radial-gradient(rgba(255,236,222,.06) 1px,transparent 1.3px)}
  :root[data-theme="dark"] a:where(:not(.nav-item):not(.btn):not(.also):not(.tile):not(.pop__row):not(.logo):not(.stat)){color:#F29BAA}
  :root[data-theme="dark"] .btn--grad{color:#15100D}
  :root[data-theme="dark"] .btn--primary kbd{background:rgba(21,16,13,.1);border-color:rgba(21,16,13,.3);color:#15100D}
  :root[data-theme="dark"] .btn--primary,:root[data-theme="dark"] .chip[aria-pressed="true"],:root[data-theme="dark"] .ptab[aria-selected="true"],:root[data-theme="dark"] .ptab[aria-selected="true"] .n,:root[data-theme="dark"] .toast{color:#15100D}
  :root[data-theme="dark"] .btn--secondary:hover{background:var(--bg-soft)}
  :root[data-theme="dark"] .btn--danger{background:transparent}
  :root[data-theme="dark"] .text{background:var(--bg-soft);color:var(--ink)}
  :root[data-theme="dark"] .text::placeholder{color:#7F7068}
  :root[data-theme="dark"] .badge--rose{background:rgba(232,93,117,.18);color:#F29BAA}
  :root[data-theme="dark"] .badge--amber{color:#E3C27A}
  :root[data-theme="dark"] .badge--muted{background:rgba(255,236,222,.08)}
"""

DARK_APP = r"""
  :root[data-theme="dark"] .side{box-shadow:0 20px 40px -24px rgba(0,0,0,.7)}
  :root[data-theme="dark"] .nav-item.is-active{background:rgba(232,93,117,.16);color:#F29BAA}
  :root[data-theme="dark"] .nav-item.is-active svg{color:#F29BAA}
  :root[data-theme="dark"] .head{background:rgba(18,14,11,.88)}
  :root[data-theme="dark"] .sec__head h2,:root[data-theme="dark"] .hello h1{color:#F29BAA}
  :root[data-theme="dark"] .sec,:root[data-theme="dark"] .card{box-shadow:0 16px 30px -28px rgba(0,0,0,.7)}
  :root[data-theme="dark"] .tile--soft{background:var(--bg-soft)}
  :root[data-theme="dark"] .tile--ok{background:#15241A;border-color:#24402E}
  :root[data-theme="dark"] .tile--ok .tile__val{color:#8FD3A8}
  :root[data-theme="dark"] .tile--warn{background:#2A2012;border-color:#4A3A1E}
  :root[data-theme="dark"] .tile--warn .tile__val{color:#E3C27A}
  :root[data-theme="dark"] .tile--bad{background:#2B1618;border-color:#4C2429}
  :root[data-theme="dark"] .tip{background:#F29BAA;color:#15100D}
  :root[data-theme="dark"] .tip::after{background:#F2EBE5;color:#15100D}
  :root[data-theme="dark"] .next__main{background:linear-gradient(135deg,#2A1B1C,var(--panel) 60%)}
  :root[data-theme="dark"] .todo li.is-hot{background:#2A2012;border-color:#4A3A1E}
  :root[data-theme="dark"] .vs blockquote{background:var(--bg-soft)}
  :root[data-theme="dark"] .vs blockquote.warn{background:#2A2012}
  :root[data-theme="dark"] .scope{background:#15241A;border-color:#24402E}
  :root[data-theme="dark"] .strip{background:rgba(28,22,18,.7)}
  :root[data-theme="dark"] .bulk.is-on{background:#2A1B1C}
  :root[data-theme="dark"] .item.is-picked{background:rgba(232,93,117,.1)}
  :root[data-theme="dark"] .quote.is-warn,:root[data-theme="dark"] .src--warn{background:#2A2012}
  :root[data-theme="dark"] .done-note.ok{background:rgba(107,192,143,.1)}
  :root[data-theme="dark"] .qrow:hover{background:var(--bg-soft)}
  :root[data-theme="dark"] .msg--me,:root[data-theme="dark"] .am--me{color:#15100D}
  :root[data-theme="dark"] .am--miss,:root[data-theme="dark"] .msg--bot.miss{background:#2A2012}
  :root[data-theme="dark"] .fab{box-shadow:0 18px 36px -14px rgba(232,93,117,.5)}
  :root[data-theme="dark"] .gauge .g-bg{stroke:rgba(255,236,222,.1)}
  :root[data-theme="dark"] .mini .m-track{stroke:rgba(255,236,222,.1)}
  :root[data-theme="dark"] .mini text{fill:var(--ink)}
  :root[data-theme="dark"] .loopdlg{background:var(--panel)}
  :root[data-theme="dark"] .lp__n{background:var(--panel)}
  :root[data-theme="dark"] .lp svg circle[fill="#FBF1F2"]{fill:#2A1B1C}
"""
