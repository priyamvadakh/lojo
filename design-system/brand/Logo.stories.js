import { LogoMark, LogoLockup, CLOUD } from './logo.js';
import { Guidelines } from '../guidelines.js';

const tile = (tone, inner, cap) => `<figure style="margin:0;display:grid;gap:var(--space-8)"><div class="logo-tile logo-tile--${tone}">${inner}</div><figcaption class="sub">${cap}</figcaption></figure>`;
const grid = (items) => `<div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(240px,1fr));gap:var(--space-16);max-width:980px">${items.join('')}</div>`;

export default { title: 'Foundations/Logo' };

export const Logo = {
  render: () => grid([
    tile('light', LogoLockup(), 'Lockup: icon + “lojo.ai” wordmark (sidebar, emails)'),
    tile('light', LogoMark({ size: 64 }), 'App icon: favicon, avatars, small spaces'),
    tile('brand', `<img src="${CLOUD}" alt="" width="56" height="56">`, 'Cloud mark: white, only on the brand gradient (Ask lojo button)'),
  ]),
};

export const Backgrounds = {
  render: () => grid([
    tile('light', LogoLockup(), 'On white'),
    tile('soft', LogoLockup(), 'On cream'),
    tile('dark', LogoLockup(), 'On dark: wordmark switches to light ink'),
  ]),
};

export const Sizes = {
  render: () => `<div class="logo-row">${[16, 26, 44, 64, 128].map((s) => `<figure>${LogoMark({ size: s })}<figcaption>${s}px</figcaption></figure>`).join('')}</div><p class="sub" style="margin-top:var(--space-16)">Smallest: 16px (favicon). Sidebar uses 26px with the wordmark.</p>`,
};

export const ClearSpace = {
  render: () => `<div class="logo-space">${LogoLockup()}</div><p class="sub" style="margin-top:var(--space-16)">Keep clear space of at least half the icon height on every side. Nothing else sits inside the dashed area.</p>`,
};

export const Guideline = {
  name: 'Do and don’t',
  parameters: { controls: { disable: true }, actions: { disable: true }, interactions: { disable: true } },
  render: () => Guidelines({
    intro: 'The icon is a raster image: always use the supplied files, never redraw it.',
    rules: [
      {
        do: { example: LogoLockup(), text: 'Use the icon and wordmark at their natural proportions.' },
        dont: { example: `<span class="logo-lockup"><img class="logo-mark" src="brand/lojo-icon-320.png" alt="" width="60" height="26"><b>lojo.ai</b></span>`, text: 'Don’t stretch or squash the icon.' },
      },
      {
        do: { example: `<div class="logo-tile logo-tile--dark" style="min-height:0;min-width:0">${LogoLockup()}</div>`, text: 'Place it on plain light, cream or dark backgrounds.' },
        dont: { example: `<div class="logo-tile" style="min-height:0;min-width:0;background:var(--brand-gradient)">${LogoLockup()}</div>`, text: 'Don’t put the coral icon on the brand gradient. Use the white cloud mark there.' },
      },
      {
        do: { example: `<span class="logo-lockup">${LogoMark({ size: 26 })}<b>lojo.ai</b></span>`, text: 'Write the name in lowercase: lojo.ai or lojo.' },
        dont: { example: `<span class="logo-lockup">${LogoMark({ size: 26 })}<b>LOJO.AI</b></span><span class="logo-lockup"><b>Lojo</b></span>`, text: 'Don’t capitalise it or set the wordmark without the icon.' },
      },
      {
        do: { example: LogoMark({ size: 16 }) + LogoMark({ size: 26 }), text: 'Use 16px or larger.' },
        dont: { example: LogoMark({ size: 10 }), text: 'Don’t go below 16px: the cloud shape stops reading.' },
      },
    ],
  }),
};
