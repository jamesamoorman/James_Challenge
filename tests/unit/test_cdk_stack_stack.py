import aws_cdk as core
import aws_cdk.assertions as assertions

from WebApplication.cdk_stack_stack import CdkStackStack

# example tests. To run these tests, uncomment this file along with the example
# resource in WebApplication/ec2.py
def test_sqs_queue_created():
    app = core.App()
    stack = CdkStackStack(app, "cdk-stack")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
