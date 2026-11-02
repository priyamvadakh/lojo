/** @type { import('@storybook/html-vite').StorybookConfig } */
const config = {
  stories: ['../design-system/**/*.stories.js'],
  addons: [],
  // lojo logo files, served at /brand/
  staticDirs: [{ from: '../assets', to: '/brand' }, { from: '../prototype/assets', to: '/brand/prototype' }],
  framework: { name: '@storybook/html-vite', options: {} },
};
export default config;
