#!/bin/bash

gcloud builds submit --tag gcr.io/app-test-438216/app-test
gcloud run deploy app-test --image gcr.io/app-test-438216/app-test --allow-unauthenticated --region us-central1
