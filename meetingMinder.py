# import slack
# import datetime
# import requests
import json


class MeetingMinder:
    # def __init__(self, token, channel, api_url):
    #     self.channel = channel
    #     self.client = slack.WebClient(token=token)
    #     self.api_url = api_url

    def listen(self, alias, command):
        if (command == 'next'):
            meetingObject = self.getMeeting(alias, 1)
            
            if meetingObject['status'] == '200':
                meetingDetails = meetingObject['data']
                if len(meetingDetails['meetings']) > 0:
                    result = {
                        'day': meetingDetails['date'],
                        'time': meetingDetails['meetings'][0]['start_time'],
                        'location':meetingDetails['meetings'][0]['location']
                    }
                    text = 'Your next meeting is on {} at {} at location {}'.format(result['day'], result['time'], result['location'])
                elif len(meetingDetails['meetings']) == 0:
                    text = 'You do not have any meetings tomorrow!'   
            elif meetingObject['status'] == '404':
                text = meetingObject['data']
            
            print(text)
            # self.client.chat_postMessage(channel=self.channel, text=text)

    def getMeeting(self, alias, order):
        # sends a request to meetings.amazon.com to get
        # the Nth meeting from now
        # then sends the result back to user
        # now = datetime.datetime.now()
        # payload = {}
        # response = requests.get(self.api_url, params=payload)
        # res = response.json()
        # next_meeting = datetime.datetime(2022, 10, 10, 11, 10, 10)  # update
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

        # return next_meeting
