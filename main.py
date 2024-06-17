import google.cloud.resourcemanager as resource_manager_client
from google.oauth2 import service_account
from googleapiclient import discovery
from projects_groups import PROJECTS_AND_GROUPS

# Replace with the path to your JSON key file
KEY_FILE = '/home/user/path_to/creds.json'

# Load the credentials from the JSON key file
credentials = service_account.Credentials.from_service_account_file(KEY_FILE)

# Create Cloud Resource Manager API client
crm_api = discovery.build('cloudresourcemanager', 'v1', credentials=credentials)
projects_api = crm_api.projects()

for project_id, group_email in PROJECTS_AND_GROUPS:
    # Get the project
    project = resource_manager_client.fetch_project(project_id)

    # Get the IAM policy for the project
    policy = crm_api.projects().getIamPolicy(resource=project.project_id, body={}).execute()

    # Find the binding for the service account user role
    service_account_binding = next((binding for binding in policy['bindings']
                                    if 'roles/iam.serviceAccountUser' in binding['role']), None)

    if service_account_binding:
        # Remove the group from the service account user role
        service_account_binding['members'] = [member for member in service_account_binding['members']
                                              if member != f'group:{group_email}']

        # Update the IAM policy
        updated_policy = crm_api.projects().setIamPolicy(
            resource=project.project_id, body={'policy': policy}).execute()

        print(f'Removed {group_email} from the service account user role in project {project_id}')
    else:
        print(f'No service account user role found in project {project_id}')
