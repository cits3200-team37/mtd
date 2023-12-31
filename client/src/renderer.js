/**
 * This file will automatically be loaded by vite and run in the "renderer" context.
 * To learn more about the differences between the "main" and the "renderer" context in
 * Electron, visit:
 *
 * https://electronjs.org/docs/tutorial/application-architecture#main-and-renderer-processes
 *
 * By default, Node.js integration in this file is disabled. When enabling Node.js integration
 * in a renderer process, please be aware of potential security implications. You can read
 * more about security risks here:
 *
 * https://electronjs.org/docs/tutorial/security
 *
 * To enable Node.js integration in this file, open up `main.js` and enable the `nodeIntegration`
 * flag:
 *
 * ```
 *  // Create the browser window.
 *  mainWindow = new BrowserWindow({
 *    width: 800,
 *    height: 600,
 *    webPreferences: {
 *      nodeIntegration: true
 *    }
 *  });
 * ```
 */

import { createApp } from "vue";
import App from "./App.vue";
import { createPinia } from "pinia";
import router from "./router";
import "./style.css";

const pinia = createPinia();
createApp(App).use(router).use(pinia).mount("#app");

const handleMinimise = () => {
  try {
    window.electronAPI.windowMinimise();
  } catch (error) {
    console.log(error);
  }
};
const handleClose = () => {
  try {
    window.electronAPI.windowClose();
  } catch (error) {
    console.log(error);
  }
};

const handleMaximise = () => {
  try {
    window.electronAPI.windowMaximise();
  } catch (error) {
    console.log(error);
  }
};

export { handleClose, handleMinimise, handleMaximise };
