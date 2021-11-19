
import boto3

def start_model(project_arn, model_arn, version_name, min_inference_units):

    client=boto3.client('rekognition')

    try:
      
        print('Starting model: ' + model_arn)
        response=client.start_project_version(ProjectVersionArn=model_arn, MinInferenceUnits=min_inference_units)
  
        project_version_running_waiter = client.get_waiter('project_version_running')
        project_version_running_waiter.wait(ProjectArn=project_arn, VersionNames=[version_name])

        describe_response=client.describe_project_versions(ProjectArn=project_arn,
            VersionNames=[version_name])
        for model in describe_response['ProjectVersionDescriptions']:
            print("Status: " + model['Status'])
            print("Message: " + model['StatusMessage']) 
    except Exception as e:
        print(e)
        
    print('Done...')
    
def main():
    project_arn='arn:aws:rekognition:us-east-1:128503088615:project/Senior_Research/1637282699632'
    model_arn='arn:aws:rekognition:us-east-1:128503088615:project/Senior_Research/version/Senior_Research.2021-11-18T22.44.11/1637293451417'
    min_inference_units=1 
    version_name='Senior_Research.2021-11-18T22.44.11'
    start_model(project_arn, model_arn, version_name, min_inference_units)

if __name__ == "__main__":
    main()
