from abc import ABC, abstractmethod

class MailProviderInterface(ABC):
    @abstractmethod
    def send(self, subject, body, to_email):
        pass