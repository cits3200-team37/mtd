module.exports = {
  packagerConfig: {
    icon: "./src/assets/mtd_logo.icns"

  },
  rebuildConfig: {},
  makers: [
    {
      name: "@electron-forge/maker-squirrel",
      config: {
        iconUrl: "https://github.com/cits3200-team37/mtd/blob/main/client/src/assets/mtd_logo.ico",
        setupIcon: "./src/assets/mtd_logo.ico",
      },
    },
    {
      name: "@electron-forge/maker-zip",
      platforms: ["darwin"],
      config: {
        icon: "./src/assets/mtd_logo.icns",
      }
    },
    {
      name: "@electron-forge/maker-deb",
      config: {
        icon: "./src/assets/mtd_logo.png",
      },
    },
  ],
  plugins: [
    {
      name: "@electron-forge/plugin-vite",
      config: {
        // `build` can specify multiple entry builds, which can be Main process, Preload scripts, Worker process, etc.
        // If you are familiar with Vite configuration, it will look really familiar.
        build: [
          {
            // `entry` is just an alias for `build.lib.entry` in the corresponding file of `config`.
            entry: "src/main.js",
            config: "vite.main.config.mjs",
          },
          {
            entry: "src/preload.js",
            config: "vite.preload.config.mjs",
          },
        ],
        renderer: [
          {
            name: "main_window",
            config: "vite.renderer.config.mjs",
          },
        ],
      },
    },
  ],
};
