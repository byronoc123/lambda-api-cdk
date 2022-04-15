import aws_cdk as core
import aws_cdk.assertions as assertions
from lambda_api_cdk.lambda_api_cdk_stack import LambdaApiCdkStack
import pytest


def test_lambda_created():
    app = core.App()
    stack = LambdaApiCdkStack(app, "lambda-api-cdk")
    template = assertions.Template.from_stack(stack)

    template.has_resource_properties(
        "AWS::Lambda::Function",
        {
            "Handler": "hello_.handler",
            "Runtime": "python3.9",
        },
    )