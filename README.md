
# GCP Service Account User Cleanup

This Python script is designed to remove a specified group email from the `roles/iam.serviceAccountUser` role in multiple Google Cloud Platform (GCP) projects. It uses the Google Cloud Resource Manager API and the Google API Python Client library to interact with the GCP resources.
I made this script to handle an urgent request that came in, I recommend adding error handling not hard-coding your service account credential, using an environment variable.

This will work as is, improve 

## Prerequisites

Before running the script, you'll need to set up the following:

1. **Python 3.x**: Make sure you have Python 3.x installed on your system.
2. **Google Cloud SDK**: Install the Google Cloud SDK and authenticate with your GCP account.
3. **Service Account Key**: Create a service account key file in JSON format and download it to your local machine. This key file will be used to authenticate with the GCP APIs.
4. To run this script, the service account specified in the [`KEY_FILE`] needs to have the `roles/resourcemanager.projectIamAdmin` role. This role provides permissions to view and manage a project's IAM policy.

This role includes the following permissions which are necessary for the script:

- [`resourcemanager.projects.getIamPolicy`]: This permission is required to fetch the IAM policy of the project.
- [`resourcemanager.projects.setIamPolicy`] This permission is required to update the IAM policy of the project.

Please ensure that the service account has been granted this role in all the projects specified in the [`PROJECTS_AND_GROUPS`] list.

## Installation

1. Clone this repository or download the source code.
2. Navigate to the project directory.
3. Create a virtual environment (optional but recommended): python3 -m venv env source env/bin/activate # On Windows, use env\Scripts\activate
4. Install the required Python packages using the `requirements.txt` file: pip install -r requirements.txt


## Usage

1. Open the `main.py` file and replace the `KEY_FILE` variable with the path to your service account key file.
2. In the `projects_groups.py` file, update the `PROJECTS_AND_GROUPS` list with the project IDs and group emails you want to remove from the `roles/iam.serviceAccountUser` role.
3. Run the script: python3 main.py
   
The script will iterate through the list of projects and groups, remove the specified group email from the `roles/iam.serviceAccountUser` role, and print a message indicating the action taken for each project.
