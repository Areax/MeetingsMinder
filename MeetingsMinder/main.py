import json
import boto3
import datetime
import urllib3

def lambda_handler(event, context):
    # TODO implement
    client = boto3.client("sqs", region_name='us-east-1')    
    handler = meeting_minder("https://api.iad.beta.ras.meetings.enterprise-engineering.aws.dev/beta", event['userId'])
    meeting_response = handler.getMeeting(1)
    sqs_message = json.dumps({'dateTime':meeting_response['start_time'], 'title':meeting_response['subject'], 'venue':meeting_response['location'], 'guests': [event['userId'] + "@amazon.com"], 'description': 'next meeting'})
    try:
        response = client.send_message(
            QueueUrl="https://sqs.us-east-1.amazonaws.com/845988471096/MeetingsMinderQueue", 
            MessageBody=sqs_message
        ) 
        return response
    except:
        raise
    
class meeting_minder:
    def __init__(self, api_url, alias):
        self.api_url = api_url
        self.alias = alias
        
    def getMeeting(self, order):
        # sends a request to meetings.amazon.com to get
        # the Nth meeting from now
        # then sends the result back to user
        # now = datetime.datetime.now()
        # payload = {}
        # response = requests.get(self.api_url, params=payload)
        # res = response.json()
        # next_meeting = datetime.datetime(2022, 10, 10, 11, 10, 10)  # update
        json_file_path = "./MeetingsMinder/response.txt"

        with open(json_file_path, 'r') as j:
            contents = json.loads(j.read())

        if self.alias in contents:
            print(contents[self.alias])
            return contents[self.alias]['meetings'][order - 1]
        else:
            return json.dumps({
            "status":"404",
            "data":"The alias is not valid :("
            })