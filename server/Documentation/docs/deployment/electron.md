# Electron

For our app verion we are using [Electron Forge](https://www.electronforge.io/), this is a package that has been built by the [Electron](https://www.electronjs.org/) team that aims to make it easier to get applications up and running quicker.

We have used this with Vite + Vue 3 to create a simple application that can be run on Windows, Mac and Linux.

## Deployment of releases
There is a [GitHub action](https://github.com/cits3200-team37/mtd/blob/main/.github/workflows/release.yml) that has been written that will automate the building process on all platforms when code is pushed to the master branch.
This will create a release and upload it to the github releases page. Please note that if an update is to occur you need to update the version number inside the `package.json` file.

**Note: as of 16th October 2023 GitHub has no free tier M1 machine running with arm that is able to be ran on GitHub actions.**

Currently there is an object that is specified inside the `forge.config.js` that will allow you to specify some properties of deployment.

```json
publishers: [
    {
      name: "@electron-forge/publisher-github",
      config: {
        repository: {
          owner: "cits3200-team37",
          name: "mtd",
        },
        prerelease: true,
      },
    },
  ]
```

Note the use of the prerelease flag, this is to ensure that when a release is pushed to GitHub it isnt automatically releases and needs to be signed off by the admin.