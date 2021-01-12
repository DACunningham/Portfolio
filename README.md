Welcome to the AWS CodeStar sample web application
==================================================

To Install This Porject
-----------------------
We use mini conda and poetry for our environment management.
1. Install mini conda
2. Create an environment called 'portfolio'
3. Install poetry
4. Install dependencies from 'poetry.lock' file

Sometimes an error can occur where poetry complains that python.exe or pythonw.exe are not present in: 'C:\Users\<username>\miniconda3\envs\portfolio\Lib\venv\scripts\nt'.  If this is the case then copy these files from: 'C:\Users\Dexter\miniconda3\envs\portfolio' to the '.\Lib\venv\scripts\nt' location.

This sample code helps get you started with a simple Django web application
deployed by AWS Elastic Beanstalk and AWS CloudFormation.

Using the Stocks App
-----------
There is no easy way around getting the data required from T212 as they do not have an API to call so, the only information one can attain easily and securely is in the contract statements and monthly emails they send.  This requires a user to have access to all of their emails from T212 and then upload them to the app.  To do this a few things must be checked / done:

1. Check a user can retireve all emails from T212 - specifically the emails ref contract statements
2. Provide user ability to upload '.eml' and '.msg' files to input data into the system
3. Provide instructions on how to get emails from web email clients.  May have to accept that non - gmail accounts will have to create a gmail account and send all emails to there so, that they can be downloaded immidiately.
4. An idea could be to have the app set up a gmail account automatically for the user and then use google's api to get the message data from there.  All the user would have to do manually would be to set up an automatic forward of all T212 emails to the new account.  All data can then be parsed automatically with no manual steps with no security holes.
- A work flow could be... Create portfolio user, app creates gmail & gives address to user, user forwards all emails to app, app gets email info from google api
- I don't think this idea will work as OAuth requires human interaction to complete the auth process.
5. a better idea could be to have email addresses set up in AWS programatically which the user sends their emails to.  I can then access them directly via botto3 api and not worry about Outh.


What's Here
-----------

This sample includes:

* README.md - this file
* ebdjango/ - this directory contains your Django project files. Note that this
  directory contains a Django config file (settings.py) that includes a pre-defined
  SECRET_KEY. Before running in a production environment, you should replace this
  application key with one you generate
  (see https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/#secret-key for details)
* helloworld/ - this directory contains your Django application files
* manage.py - this Python script is used to start your Django web application
* .ebextensions/ - this directory contains the Django configuration file that
  allows AWS Elastic Beanstalk to deploy your Django application
* buildspec.yml - this file is used by AWS CodeBuild to build and test
  your application
* requirements.txt - this file is used to install Python dependencies needed by
  the Django application
* template.yml - this file contains the description of AWS resources used by AWS
  CloudFormation to deploy your infrastructure
* template-configuration.json - this file contains the project ARN with placeholders used for tagging resources with the project ID

Getting Started
---------------

These directions assume you want to develop on your local computer, and not
from the Amazon EC2 instance itself. If you're on the Amazon EC2 instance, the
virtual environment is already set up for you, and you can start working on the
code.

To work on the sample code, you'll need to clone your project's repository to your
local computer. If you haven't, do that first. You can find instructions in the AWS CodeStar user guide at https://docs.aws.amazon.com/codestar/latest/userguide/getting-started.html#clone-repo.

1. Create a Python virtual environment for your Django project. This virtual
   environment allows you to isolate this project and install any packages you
   need without affecting the system Python installation. At the terminal, type
   the following command:

        $ python3 -m venv ./venv

2. Activate the virtual environment:

        $ source ./venv/bin/activate

3. Install Python dependencies for this project:

        $ pip install -r requirements.txt

4. (Optional) Enable Django's debug mode for development:

        $ export DJANGO_DEBUG=True

5. Start the Django development server:

        $ python manage.py runserver

6. Open http://127.0.0.1:8000/ in a web browser to view your application.

What Do I Do Next?
------------------

Once you have a virtual environment running, you can start making changes to
the sample Django web application. We suggest making a small change to
/helloworld/templates/index.html first, so you can see how changes pushed to
your project's repository are automatically picked up and deployed to the Amazon EC2
instance by AWS Elastic Beanstalk. (You can watch the progress on your project dashboard.)
Once you've seen how that works, start developing your own code, and have fun!

To run your tests locally, go to the root directory of the sample code and run
the `python manage.py test` command, which AWS CodeBuild also runs through
your `buildspec.yml` file.

To test your new code during the release process, modify the existing tests or
add tests to the tests directory. AWS CodeBuild will run the tests during the
build stage of your project pipeline. You can find the test results
in the AWS CodeBuild console.

Learn more about AWS CodeBuild and how it builds and tests your application here:
https://docs.aws.amazon.com/codebuild/latest/userguide/concepts.html

Learn more about AWS CodeStar by reading the user guide.  Ask questions or make
suggestions on our forum.

User Guide: http://docs.aws.amazon.com/codestar/latest/userguide/welcome.html
Forum: https://forums.aws.amazon.com/forum.jspa?forumID=248

How Do I Add Template Resources to My Project?
------------------

To add AWS resources to your project, you'll need to edit the `template.yml`
file in your project's repository. You may also need to modify permissions for
your project's worker roles. After you push the template change, AWS CodeStar
and AWS CloudFormation provision the resources for you.

See the AWS CodeStar user guide for instructions to modify your template:
https://docs.aws.amazon.com/codestar/latest/userguide/how-to-change-project.html#customize-project-template

What Should I Do Before Running My Project in Production?
------------------

AWS recommends you review the security best practices recommended by the framework
author of your selected sample application before running it in production. You
should also regularly review and apply any available patches or associated security
advisories for dependencies used within your application.

Best Practices: https://docs.aws.amazon.com/codestar/latest/userguide/best-practices.html?icmpid=docs_acs_rm_sec
