/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{vue,js}",
  ],
  theme: {
    extend: {
      colors: {
        "navbar-primary": "#282C34",
        "navbar-icon": "#A4A4A4",
      }
    },
  },
  plugins: [],
}