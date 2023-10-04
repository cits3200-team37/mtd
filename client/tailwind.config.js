/** @type {import('tailwindcss').Config} */
export default {
  content: ["./index.html", "./src/**/*.{vue,js}"],
  theme: {
    extend: {
      textColor: {
        "text-color": `rgb(var(--text-color))`,
      },
      backgroundColor: {
        "background-color": 'rgb(var(--background-color))',
        "background-secondary": 'rgb(var(--background-secondary))',
        "simulation-color": `rgb(var(--simulation-color))`,
        'hover-theme': `rgb(var(--hover-bg-color))`,
        "scrollbar-track": 'rgb(var(--scrollbar-track-color))',
        "scrollbar-thumb": 'rgb(var(--scrollbar-thumb-color))',
        "scrollbar-thumb-hover": 'rgb(var(--scrollbar-thumb-hover-color))',
      },
      colors: {
        "navbar-primary": `rgb(var(--navbar-color))`,
        "navbar-icon": `rgb(var(--navbar-icon-color))`,
        "button-color": `rgb(var(--button-color))`,
        "dark-background": "#313338",

      },
    },
  },
  plugins: [],
};
