// tailwind.config.js - Dark Reborn 3D Preset
module.exports = {
  theme: {
    extend: {
      colors: {
        reborn: {
          red: '#b81414',
          scarlet: '#ff263b',
          crimson: '#700808',
          titanium: '#8f96a3',
          platinum: '#f5f7fa',
          obsidian: '#060709',
          surface: '#0f1218',
          elevated: '#161a23'
        }
      },
      fontFamily: {
        display: ['Orbitron', 'sans-serif'],
        body: ['Rajdhani', 'sans-serif']
      },
      boxShadow: {
        'reborn-glow': '0 0 35px rgba(184, 20, 20, 0.45)',
        'reborn-laser': '0 0 15px rgba(255, 38, 59, 0.7)'
      }
    }
  }
}
