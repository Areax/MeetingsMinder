import json
import boto3
import datetime
import urllib3

def lambda_handler(event, context):
    # TODO implement
    client = boto3.client("sqs", region_name='us-east-1')    
    handler = meeting_minder("https://api.iad.beta.ras.meetings.enterprise-engineering.aws.dev/beta", "alias")
    
    try:
        response = client.send_message(
            QueueUrl="https://sqs.us-east-1.amazonaws.com/845988471096/MeetingsMinderQueue", 
            MessageBody=handler.getMeeting()
        ) 
        return response
    except:
        raise
    
class meeting_minder:
    def __init__(self, api_url, alias):
        self.api_url = api_url
        self.alias = alias
        
    def getMeeting(self):
        now = datetime.datetime.now()
        payload = json.dumps({ "requestedOnBehalfOf": self.alias, "startTime": "1658380328000", "endTime": "1658466728000", "maxResults" "1"})
        http = urllib3.PoolManager()
        full_url = self.api_url + "/api/meetings/find"
        response = http.request('POST',
                        full_url,
                        body = payload,
                        headers = {'Content-Type': 'application/json'},
                        retries = False)
        next_meeting = '{"userId": "jasperz"}'
        print(response.status)
        print(response.data)

        return next_meeting
        