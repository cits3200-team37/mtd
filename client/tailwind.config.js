/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{vue,js}",
  ],
  theme: {
    extend: {
      colors: {
        "navbar-primary": "#1f1f1f",
        "navbar-icon": "#A4A4A4",
        "dark-background": "#313338",
      }
    },
  },
  plugins: [],
}