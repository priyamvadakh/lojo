import { create } from 'storybook/theming';

// Storybook UI theme, using the lojo token values (design-system/tokens.css)
export default create({
  base: 'light',
  brandTitle: '<span style="display:inline-flex;align-items:center;gap:8px;font-family:Outfit,system-ui,sans-serif;font-weight:800;font-size:22px;letter-spacing:-.02em;color:#241A14"><img src="brand/lojo-icon-128.png" alt="" width="28" height="28" style="border-radius:24%">lojo.ai <span style="color:#6E5A4E;font-weight:700;font-size:13px;letter-spacing:0">Design System</span></span>',
  brandUrl: 'https://priyamvadakh.github.io/lojo/',
  brandTarget: '_blank',

  colorPrimary: '#E85D75',
  colorSecondary: '#E85D75',

  appBg: '#F7F4F1',
  appContentBg: '#FFFFFF',
  appPreviewBg: '#FDFCFB',
  appBorderColor: 'rgba(36,26,20,.08)',
  appBorderRadius: 12,

  fontBase: '"Manrope", system-ui, sans-serif',
  fontCode: 'ui-monospace, SFMono-Regular, Menlo, monospace',

  textColor: '#241A14',
  textMutedColor: '#6E5A4E',
  textInverseColor: '#FFFFFF',

  barBg: '#FFFFFF',
  barTextColor: '#6E5A4E',
  barSelectedColor: '#B73C54',
  barHoverColor: '#B73C54',

  inputBg: '#FFFFFF',
  inputBorder: 'rgba(36,26,20,.16)',
  inputTextColor: '#241A14',
  inputBorderRadius: 11,
});
