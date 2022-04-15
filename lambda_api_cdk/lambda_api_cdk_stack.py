from constructs import Construct
from aws_cdk import (
    CfnOutput,
    Stack,
    aws_lambda as _lambda,
    aws_apigateway as apigw
)


class LambdaApiCdkStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        hello_lambda = _lambda.Function(
            self, 'HelloHandler',
            runtime = _lambda.Runtime.PYTHON_3_9,
            code = _lambda.Code.from_asset('lambda'),
            handler = 'hello_.handler',
        )

        api_gw = apigw.LambdaRestApi(
            self, 'Endpoint',
            handler = hello_lambda,
        )

        api_url = CfnOutput(self, "ApiEndpoint", value=api_gw.url,)

        print("API-URL", api_url.value)
