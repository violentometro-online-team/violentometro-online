import json
import boto3
import os

ENDPOINT_NAME = os.environ["ENDPOINT_NAME"]
runtime = boto3.client("runtime.sagemaker")


def lambda_handler(event, context):
    payload = event

    response = runtime.invoke_endpoint(
        EndpointName=ENDPOINT_NAME,
        ContentType="application/json",
        Accept="application/json",
        Body=json.dumps(payload),
    )
    response_body = json.loads(response["Body"].read())

    return response_body
