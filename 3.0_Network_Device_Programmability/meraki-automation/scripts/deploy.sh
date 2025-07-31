#!/bin/bash
set -a
source ../.env
set +a

export MERAKI_DASHBOARD_API_KEY=$MERAKI_DASHBOARD_API_KEY

terraform -chdir=../terraform init
terraform -chdir=../terraform apply -auto-approve
