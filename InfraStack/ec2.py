from aws_cdk import aws_ec2 as ec2
# from aws_cdk import aws_iam as iam
from aws_cdk import (Stack)
# from aws_cdk.aws_iam import ServicePrincipal
from constructs import Construct


class EC2Stack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here
        self.instance_ami = "ubuntu/images/hvm-ssd/ubuntu-jammy-22.04-amd64-server-20230208"
        self.instance_type = "t2.micro"
        self.vpc_id = "	vpc-0d0345ae407ef6676"
        self.security_group_id = "sg-07942fd02314ed303"
        self.key_name = "comcast-challenge-key-pair"
        self.key_type = "rsa"

        cfn_key_pair = ec2.CfnKeyPair(
            self
            , "MyCfnKeyPair"
            , key_name=self.key_name
            , key_type=self.key_type
        )

        # VPC
        vpc = ec2.Vpc.from_lookup(
            self,
            "vpc",
            vpc_id=self.vpc_id
        )

        # Security Group
        security_group = ec2.SecurityGroup.from_security_group_id(
            self,
            "security_group",
            security_group_id=self.security_group_id
        )

        security_group.add_ingress_rule(
            peer=ec2.Peer.any_ipv4(),
            description='inbound SSH',
            connection=ec2.Port.tcp(22)
        )

        security_group.add_ingress_rule(
            peer=ec2.Peer.any_ipv4(),
            description='inbound HTTP access',
            connection=ec2.Port.tcp(80)
        )

        security_group.add_ingress_rule(
            peer=ec2.Peer.any_ipv4(),
            description='HTTPS access',
            connection=ec2.Port.tcp(443)
        )
        '''
        iam_role = iam.Role(
            self,
            "ec2Role",
            assumed_by=ServicePrincipal("ec2.amazons.com"))
        '''
        # EC2 Instance
        instance = ec2.Instance(
            self,
            "instance",
            instance_type=ec2.InstanceType(self.instance_type),
            machine_image=ec2.MachineImage().lookup(name=self.instance_ami),
            vpc=vpc,
            security_group=security_group,
            key_name=cfn_key_pair.key_name
        )
