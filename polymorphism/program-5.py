# 5.	Create a base class Notification with a method send(). Derive EmailNotification, SMSNotification, and PushNotification. Override send() to display the appropriate notification method.

class Notification:
    def __init__(self, recipient, message):
        self.recipient = recipient
        self.message = message

    def send(self):
        print(f"Sending generic notification to {self.recipient}: {self.message}")


class EmailNotification(Notification):
    def send(self):
        print(f"[EMAIL] Dispatching email to <{self.recipient}> with subject 'Alert': \"{self.message}\"")


class SMSNotification(Notification):
    def send(self):
        print(f"[SMS] Sending text message to mobile number {self.recipient}: \"{self.message}\"")


class PushNotification(Notification):
    def send(self):
        print(f"[PUSH] Triggering FCM push notification to device token {self.recipient}: \"{self.message}\"")


def notify_user(notification_obj):
    notification_obj.send()


notifications = [
    EmailNotification("student@university.edu", "Your assignment has been graded."),
    SMSNotification("+91-9876543210", "OTP for login is 482910. Valid for 5 minutes."),
    PushNotification("fcm_token_a1b2c3d4", "You have 1 new message in Discussion Forum.")
]

print("Notification Dispatch")
for n in notifications:
    notify_user(n)
