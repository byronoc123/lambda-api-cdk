#!/usr/bin/env python3

import aws_cdk as cdk

from lambda_api_cdk.lambda_api_cdk_stack import LambdaApiCdkStack


app = cdk.App()
LambdaApiCdkStack(app, "lambda-api-cdk")

app.synth()
