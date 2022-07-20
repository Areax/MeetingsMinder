import slack
import datetime


print(x.year)
print(x.strftime("%A"))


class MeetingMinder:
    def __init__(self, token, channel):
        self.channel = channel
        self.client = slack.WebClient(token=token)

    def getMeeting(self, order):
        # sends a request to meetings.amazon.com to get
        # the Nth meeting from now
        # then sends the result back to user

        now = datetime.datetime.now()

        next_meeting = datetime.datetime(2022, 10, 10, 11, 10, 10)  # update

        result = {
            'day': next_meeting.strftime("%x"),
            'time': next_meeting.strftime("%X")
        }

        text = 'Your next meeting is {} at {}'.format(
            result['day'], result['time'])
        self.client.chat_postMessage(channel=self.channel, text=text)
