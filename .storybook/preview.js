import '../design-system/tokens.css';
import '../design-system/base.css';

/** @type { import('@storybook/html-vite').Preview } */
const preview = {
  globalTypes: {
    theme: {
      description: 'Light or dark tokens',
      toolbar: { title: 'Theme', icon: 'mirror', items: ['light', 'dark'], dynamicTitle: true },
    },
  },
  initialGlobals: { theme: 'light' },
  decorators: [
    (story, { globals }) => {
      document.documentElement.setAttribute('data-theme', globals.theme === 'dark' ? 'dark' : 'light');
      return story();
    },
  ],
  parameters: {
    layout: 'padded',
    backgrounds: { disable: true },
    options: { storySort: { order: ['Home', 'Foundations', ['Theme', 'Tokens', 'Logo'], 'Components'] } },
  },
};
export default preview;
