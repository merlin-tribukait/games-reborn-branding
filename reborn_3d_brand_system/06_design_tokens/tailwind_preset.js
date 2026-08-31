// Tailwind CSS Preset for GAMES REBORN
module.exports = {
  theme: {
    extend: {
      colors: {
        brand: {
          primary: '#ff2d55',
          secondary: '#ffb703',
          metallic: '#8f96a3',
          bg: '#060709',
          surface: '#12121c',
        }
      },
      fontFamily: {
        sans: ['Inter', 'sans-serif'],
        mono: ['JetBrains Mono', 'monospace'],
      },
      boxShadow: {
        'glow': '0 0 24px #ff2d5560',
        'glow-lg': '0 0 40px #ff2d5590',
      }
    }
  }
};
