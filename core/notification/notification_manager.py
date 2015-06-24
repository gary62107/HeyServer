from app.settings import NOTIFICATION_THREAD_MAX_COUNT
from core.notification.android_notification_object import AndroidNotificationObject
from core.utility.notification_queue import NotificationQueue


class NotificationManager(NotificationQueue):
    def __init__(self, filters):
        NotificationQueue.__init__(self, NOTIFICATION_THREAD_MAX_COUNT)
        self._filters = filters

    def push(self, subject):
        self._push(AndroidNotificationObject(subject))