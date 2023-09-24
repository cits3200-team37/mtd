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
      },
      colors: {
        "navbar-primary": `rgb(var(--navbar-color))`,
        "navbar-icon": `rgb(var(--navbar-icon-color))`,
        "dark-background": "#313338",

      },
    },
  },
  plugins: [],
};
