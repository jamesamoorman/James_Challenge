# James_Challenge
Comcast SED Challenge

For this challenge I (James) will attempt to spin up an EC2 instance that will
host a web application using AWS CDK. This application will be secured so that 
only appropriate ports are publicly available and that any http requests are 
redirected to https.

References
* SetUp
  * Working with CDK Python: https://docs.aws.amazon.com/cdk/v2/guide/work-with-cdk-python.html
  * I chose to use PyCharm as my IDE
  * GitHub Repository: 
  * 
* IaC
  * https://awstip.com/create-an-ec2-instance-using-aws-cdk-python-fb65de626543
  * https://unbiased-coder.com/setup-aws-ec2-instance-cdk-python/

Infrastructure as Code
* I chose to use Cloud Development Kit (CDK) as Infrastructure as Code to create the EC2 Instance.

# Welcome to your CDK Python project!

This is a blank project for CDK development with Python.

The `cdk.json` file tells the CDK Toolkit how to execute your app.

This project is set up like a standard Python project.  The initialization
process also creates a virtualenv within this project, stored under the `.venv`
directory.  To create the virtualenv it assumes that there is a `python3`
(or `python` for Windows) executable in your path with access to the `venv`
package. If for any reason the automatic creation of the virtualenv fails,
you can create the virtualenv manually.

To manually create a virtualenv on MacOS and Linux:

```
$ python -m venv .venv
```

After the init process completes and the virtualenv is created, you can use the following
step to activate your virtualenv.

```
$ source .venv/bin/activate
```

If you are a Windows platform, you would activate the virtualenv like this:

```
% .venv\Scripts\activate.bat
```

Once the virtualenv is activated, you can install the required dependencies.

```
$ pip install -r requirements.txt
```

At this point you can now synthesize the CloudFormation template for this code.

```
$ cdk synth
```

To add additional dependencies, for example other CDK libraries, just add
them to your `setup.py` file and rerun the `pip install -r requirements.txt`
command.

## Useful commands

 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation

Enjoy!