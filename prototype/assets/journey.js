// prototype only: each persona from the picker after sign in, new or returning, walks its own path from first contact to their home page
(function () {
  const J = {
    admin: { who: 'Eric Ouisse · Admin', steps: [['emails', 'Invitation email'], ['set', 'Set password'], ['profile', 'Your profile'], ['onboarding', 'Create workspace'], ['dashboard', 'Dashboard']] },
    editor: { who: 'Lena Okafor · Editor', steps: [['emails', 'Invitation email'], ['set', 'Set password'], ['profile', 'Your profile'], ['loop', 'Loop setup'], ['dashboard', 'Dashboard']] },
    viewer: { who: 'Jonas Lie · Viewer', steps: [['emails', 'Invitation email'], ['set', 'Set password'], ['profile', 'Your profile'], ['knowledge', 'Knowledge']] },
    'admin-return': { who: 'Eric Ouisse · Admin', steps: [['login', 'Sign in'], ['dashboard', 'Dashboard']] },
    'editor-return': { who: 'Lena Okafor · Editor', steps: [['login', 'Sign in'], ['dashboard', 'Dashboard']] },
    'viewer-return': { who: 'Jonas Lie · Viewer', steps: [['login', 'Sign in'], ['knowledge', 'Knowledge']] },
  };
  const P = new URLSearchParams(location.search);
  const ss = (k, v) => { try { if (v === undefined) return sessionStorage.getItem(k); if (v === null) sessionStorage.removeItem(k); else sessionStorage.setItem(k, v); } catch (e) {} };
  let role = P.get('journey');
  if (role && J[role]) ss('lojo-journey', role); else role = ss('lojo-journey');
  if (document.body.dataset.persona === 'super') { ss('lojo-journey', null); role = null; }
  window.LOJO_JOURNEY = J[role] ? role : null;
  if (!window.LOJO_JOURNEY) return;

  const page = (location.pathname.split('/').pop() || '').replace('.html', '');
  const here = page === 'auth' ? P.get('s') : page === 'onboarding' && (P.has('loop') || P.has('inside')) ? 'loop' : page;
  const steps = J[role].steps, i = steps.findIndex(s => s[0] === here);
  if (i < 0 || document.body.classList.contains('mailonly')) return;
  const last = i === steps.length - 1;

  const css = document.createElement('style');
  css.textContent = '.jrny{position:fixed;left:50%;bottom:16px;transform:translateX(-50%);z-index:80;display:flex;align-items:center;gap:12px;max-width:calc(100vw - 32px);padding:7px 7px 7px 16px;border-radius:999px;background:#241a14;color:#fff;font:600 .78rem/1.2 Manrope,system-ui,sans-serif;box-shadow:0 14px 30px -16px rgba(36,26,20,.7)}' +
    '.jrny ol{display:flex;gap:6px;margin:0;padding:0;list-style:none;overflow-x:auto}' +
    '.jrny li{white-space:nowrap;padding:5px 10px;border-radius:999px;color:rgba(255,255,255,.55)}' +
    '.jrny li.is-done{color:rgba(255,255,255,.8)}.jrny li.is-done::before{content:"✓ "}' +
    '.jrny li.is-cur{background:#fff;color:#241a14}' +
    '.jrny em{font-style:normal;color:rgba(255,255,255,.7);white-space:nowrap}' +
    '.jrny button{height:28px;padding:0 12px;border:0;border-radius:999px;background:rgba(255,255,255,.14);color:#fff;font:inherit;cursor:pointer;white-space:nowrap}' +
    '.jrny button:hover{background:rgba(255,255,255,.24)}' +
    '@media (max-width:700px){.jrny em{display:none}}';
  document.head.appendChild(css);
  const bar = document.createElement('div');
  bar.className = 'jrny'; bar.setAttribute('role', 'status'); bar.setAttribute('aria-label', 'Prototype journey');
  bar.innerHTML = '<em>' + J[role].who + '</em><ol>' + steps.map((s, k) => '<li class="' + (k < i ? 'is-done' : k === i ? 'is-cur' : '') + '"' + (k === i ? ' aria-current="step"' : '') + '>' + (k + 1) + '. ' + s[1] + '</li>').join('') + '</ol>' +
    (last ? '<button type="button" data-j="end" aria-label="End the journey">Done ×</button>' : '');
  document.body.appendChild(bar);
  if (last) bar.querySelector('[data-j="end"]').addEventListener('click', () => { ss('lojo-journey', null); bar.remove(); });
})();
