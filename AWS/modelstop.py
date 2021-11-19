
import boto3
import time


def stop_model(model_arn):

    client=boto3.client('rekognition')

    print('Stopping model:' + model_arn)

    try:
        response=client.stop_project_version(ProjectVersionArn=model_arn)
        status=response['Status']
        print ('Status: ' + status)
    except Exception as e:  
        print(e)  

    print('Done...')
    
def main():
    
    model_arn='arn:aws:rekognition:us-east-1:128503088615:project/Senior_Research/version/Senior_Research.2021-11-18T22.44.11/1637293451417'
    stop_model(model_arn)

if __name__ == "__main__":
    main() 
