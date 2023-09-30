import { app, BrowserWindow, ipcMain } from "electron";
const path = require("path");
require("update-electron-app")({
  updateInterval: "1 hour"
});
// Handle creating/removing shortcuts on Windows when installing/uninstalling.
if (require("electron-squirrel-startup")) {
  app.quit();
}

const createWindow = () => {
  // Create the browser window.
  const mainWindow = new BrowserWindow({
    width: 1000,
    minHeight: 700,
    height: 700,
    minHeight: 500,
    center: true,
    frame: false,
    titleBarStyle: "hiddenInset",
    webPreferences: {
      preload: path.join(__dirname, "preload.js"),
      nodeIntegration: true,
      contextIsolation: true,
    },
  });

  // and load the index.html of the app.
  if (MAIN_WINDOW_VITE_DEV_SERVER_URL) {
    mainWindow.loadURL(MAIN_WINDOW_VITE_DEV_SERVER_URL);
  } else {
    mainWindow.loadFile(
      path.join(__dirname, `../renderer/${MAIN_WINDOW_VITE_NAME}/index.html`),
    );
  }
};

// handle ipc calls regarding windows and linux window management
const handleWindowMinimise = async () => {
  BrowserWindow.getFocusedWindow().minimize();
};
const handleWindowClose = async () => {
  if (BrowserWindow.getFocusedWindow().closable) {
    BrowserWindow.getFocusedWindow().close();
  }
};
const handleWindowMaximise = async () => {
  if (BrowserWindow.getFocusedWindow().maximizable) {
    BrowserWindow.getFocusedWindow().maximize();
  }
};
// This method will be called when Electron has finished
// initialization and is ready to create browser windows.
// Some APIs can only be used after this event occurs.
app.on("ready", createWindow);

// Quit when all windows are closed, except on macOS. There, it's common
// for applications and their menu bar to stay active until the user quits
// explicitly with Cmd + Q.
app.on("window-all-closed", () => {
  if (process.platform !== "darwin") {
    app.quit();
  }
});

app.on("activate", async () => {
  // On OS X it's common to re-create a window in the app when the
  // dock icon is clicked and there are no other windows open.
  if (BrowserWindow.getAllWindows().length === 0) {
    await createWindow();
  }
});

// In this file you can include the rest of your app's specific main process
// code. You can also put them in separate files and import them here.
ipcMain.on("window-minimise", handleWindowMinimise);
ipcMain.on("window-close", handleWindowClose);
ipcMain.on("window-maximise", handleWindowMaximise);
ipcMain.handle("operating-system", (event, args) => {
  return process.platform;
});
ipcMain.handle("process-version", (event, args) => {
  return app.getVersion();
});
