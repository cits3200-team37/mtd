/** @type {import('tailwindcss').Config} */
export default {
  content: ["./index.html", "./src/**/*.{vue,js}"],
  theme: {
    extend: {
      colors: {
        "navbar-primary": "#1f1f1f",
        "navbar-icon": "#A4A4A4",

        // Theme Variants
        // Dark Theme:
        "dark-background": "#313338",
        "dark-text": "#ffffff",

        // Light Theme:
        "light-background": "#FFFFE0",
        "light-text": "#333333",

        // Blue Theme:
        "blue-background": "#00A4DB",
        "blue-text": "#f7f7f7",
      },
    },
  },
  plugins: [],
};
