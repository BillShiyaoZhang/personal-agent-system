class ChatAppMgr:
    """
    Class for managing chat apps. The chat manager can list installable apps, list local apps, install apps, connect apps with models, open apps, and uninstall apps.

    For the first implementation, we only consider Ollama models.
    """

    def __init__(self):
        """
        Initialize the chat manager.
        Args:
            installable_apps (list): List of apps, as ChatAppDefinition, that can be installed.
            local_apps (list): List of apps, as ChatAppDefinition, that are already installed.
        """
        self.installable_apps = []
        self.local_apps = []

    def list_installable_apps(self):
        # TODO: Get a real list of downloadable apps
        return self.installable_apps

    def list_local_apps(self):
        # TODO: Get a real list of local apps
        return self.local_apps

    def install_app(self, app):
        """
        Install a chat app.
        Args:
            app (ChatAppDefinition): The app to install.
        """
        if app in self.installable_apps:
            app.install()
            self.local_apps.append(app)
        else:
            print(f"{app.name} not found")

    def connect(self, app, model):
        """
        Connect a chat app with a model.

        For the first implementation, we only consider Ollama models.

        Args:
            app (ChatAppDefinition): The app to connect.
            model (str): The name of the model in Ollama.
        """
        if app in self.local_apps:
            if model in app.models:
                app.selectedModel = model
            else:
                print(f"{model} not found in {app.name}")
        else:
            print(f"{app.name} not found")

    def open_app(self, app):
        """
        Open a chat app.
        Args:
            app (ChatAppDefinition): The app to open.
        """
        if app in self.local_apps:
            app.open()
        else:
            print(f"{app.name} not found")

    def uninstall_app(self, app):
        """
        Uninstall a chat app.
        Args:
            app (ChatAppDefinition): The app to uninstall.
        """
        if app in self.local_apps:
            app.uninstall()
            self.local_apps.remove(app)
        else:
            print(f"{app.name} not found")
