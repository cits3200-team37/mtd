# Github Pages

The documentation is been hosted on githubs own pages service. This is a static site that is generated from the markdown files in this directory. The site is generated using [mkdocs](https://www.mkdocs.org/). The theme used is [material](https://squidfunk.github.io/mkdocs-material/).

We are currently using a Github Action to build and deploy the site. The action is defined in `.github/workflows/ci.yml`. The action is triggered on every push to the `main` branch. The action will build the site and push the changes to the `gh-pages` branch. The site is then hosted from the `gh-pages` branch.

For more detailed information about deploying to Github Pages please refer to [Material Theme Deployment](https://squidfunk.github.io/mkdocs-material/publishing-your-site).