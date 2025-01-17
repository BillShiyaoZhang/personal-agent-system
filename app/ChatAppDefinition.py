from abc import ABC, abstractmethod

class ChatAppDefinition(ABC):
    """
    Abstract class for defining a chat app. Each chat app should have a name, description, and a list of models.  The chat app can be installed, removed, and opened.
    """

    def __init__(self, name, description, models):
        """
        Initialize the chat app.
        Args:
            name (str): The name of the chat app.
            description (str): The description of the chat app.
            models (list): A list of models that can be used with this chat app.
        """
        self.name = name
        self.description = description
        self.models = models
        self.selectedModel = None

    @abstractmethod
    def install(self):
        """
        Install the chat app.
        """
        pass

    @abstractmethod
    def uninstall(self):
        """
        Uninstall the chat app.
        """
        pass

    @abstractmethod
    def open(self):
        """
        Open the chat app.
        """
        pass

