# API deployment

The API is deployed using Google Cloud Run following this [documentation](https://cloud.google.com/run/docs/quickstarts/build-and-deploy/deploy-python-service). Ensure that `gcloud` cli has been installed and you are able to authenticate yourself with the correct permissions

To deploy:

1. Change into the `server` directory
1. run `gcloud run deploy`
1. set name to `mtd-sim-api`, this is the name of the service on the cloud console
1. set region to `australia-southeast1`
