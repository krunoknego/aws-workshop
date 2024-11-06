# aws-workshop

## Getting Started with CDK (Read this first)

All necessary commands are in skeleton/Makefile.
To start the project `cd skeleton && make start`


Using `make cli` will get you into the container.

Once in the container following commands need to be executed:
- `pip install requirements-dev.txt requirements.txt`
- `python3 -m venv .venv`
- `source .venv/bin/activate`
- `cdk bootstrap`

## Code Structure

skeleton/project/project contains the Stack. Stack is where the infrastructure is defined.

skeleton/project/lambda contains the source code for the Lambdas. This can be changed by editing the Stack.

skeleton/project/app.py is the entrypoint. All cdk commands first will search for this file.

## Additional Resources

- https://docs.aws.amazon.com/cdk/v2/guide/work-with-cdk-python.html

## Tips

- import boto3 stubs for typehints
- use python cast to avoid problems with the jsii
