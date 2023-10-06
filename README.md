# MTD simulator

## How to run the client

### 1. Navigate to the client directory

- `cd client`

### 2. Set up environment variables

- Copy the provided `.env.example` file to create your own `.env` file for local development.
  - `cp .env.example .env`

### 3. Install dependencies

- `npm install`
- or
- `yarn install`

### 4. Run the client

- Running these commands will startup a electron instance of the client interface.
- `npm run start`
- or
- `yarn start`
- If you wish to get a pure website view of the client interface, run:
- `npm run dev`
- or
- `yarn dev`

### Accessing Google Cloud Platform API

API currently only supports authenticated calls.

1. Install gcloud cli
2. Run `$(gcloud auth print-identity-token)` to get your bearer token
3. Add bearer token in header of request
