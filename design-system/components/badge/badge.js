import './badge.css';
/** Badge: same markup as the prototype's .badge */
export const Badge = ({ label = 'Badge', tone = 'rose' } = {}) => `<span class="badge badge--${tone}">${label}</span>`;
