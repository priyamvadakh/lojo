import './logo.css';
const ICON = 'brand/lojo-icon-320.png';
export const CLOUD = 'brand/prototype/lojo-cloud.png';
/** The app icon on its own */
export const LogoMark = ({ size = 44 } = {}) => `<img class="logo-mark" src="${ICON}" alt="lojo" width="${size}" height="${size}">`;
/** Icon + wordmark, as used in the sidebar */
export const LogoLockup = ({ size = 26, fontSize = '' } = {}) =>
  `<span class="logo-lockup">${LogoMark({ size })}<b${fontSize ? ` style="font-size:${fontSize}"` : ''}>lojo.ai</b></span>`;
