import slack
import datetime


class MeetingMinder:
    def __init__(self, token, channel):
        self.channel = channel
        self.client = slack.WebClient(token=token)

    def listen(self, command):
        if (command == 'next'):
            meeting = self.getMeeting(1)
            result = {
                'day': meeting.strftime("%x"),
                'time': meeting.strftime("%X")
            }
            text = 'Your next meeting is {} at {}'.format(
                result['day'], result['time'])
            self.client.chat_postMessage(channel=self.channel, text=text)

    def getMeeting(self, order):
        # sends a request to meetings.amazon.com to get
        # the Nth meeting from now
        # then sends the result back to user
        now = datetime.datetime.now()
        next_meeting = datetime.datetime(2022, 10, 10, 11, 10, 10)  # update

        return next_meeting
