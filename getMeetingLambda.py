import json

def lambda_handler(event, context):
    # TODO implement
    
    nextMeetingObject = getMeeting("chhapgar")
    
    if nextMeetingObject['status'] == '404':
        print(nextMeetingObject['data'])
    else:
        nextMeeting = nextMeetingObject['data']
        
        if len(nextMeeting['meetings']) == 0:
            print("Hey! You do not have any meetings tomorrow!")
            
        if len(nextMeeting['meetings']) > 0:
            print("Hey! Your next meeting tomorrow morning is at", nextMeeting['meetings'][0]['start_time'], "at", nextMeeting['meetings'][0]['location'])
        
        return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
    
def getMeeting(alias):
    json_file_path = "./response.txt"

    with open(json_file_path, 'r') as j:
        contents = json.loads(j.read())
    
    if alias in contents:
        return {
            "status":"200",
            "data":contents[alias]
        }
    else:
        return{
            "status":"404",
            "data":"The alias is not valid :("
        }