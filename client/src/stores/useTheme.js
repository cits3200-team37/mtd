import { ref, watch } from "vue";

export default function useTheme() {
  const defaultTheme = "dark";
  const theme = ref(localStorage.getItem("user-theme") || defaultTheme);

  watch(theme, (newTheme) => {
    localStorage.setItem("user-theme", newTheme);
    document.body.setAttribute("data-theme", newTheme);
  });

  const setTheme = (newTheme) => {
    theme.value = newTheme;
  };

  return { theme, setTheme };
}
