#!/bin/bash

gunicorn -w 4 -b 0.0.0.0:8001 app:app
