import requests

class ModelMgr:
    """Manage LLM models that users can select from.

    For the first implementation, we only consider Ollama models.
    """

    def __init__(self):
        # Initialize the list of local models
        self.local_models = self.get_local_models()

    def download_model(self, model_name):
        """Download a model from Ollama"""
        payload = {"model": model_name}
        response = requests.post("http://localhost:11434/api/pull", json=payload)
        if response.status_code == 200:
            print(f"Model {model_name} downloaded successfully.")
            # Update the local_models list
            self.local_models = self.get_local_models()
            return True
        else:
            print(f"Failed to download model {model_name}: {response.status_code}")
            return False

    def remove_local_model(self, model_name):
        """Remove a local model from the manager"""
        payload = {"model": model_name}
        response = requests.delete("http://localhost:11434/api/delete", json=payload)
        if response.status_code == 200:
            print(f"Model {model_name} removed successfully.")
            # Update the local_models list
            self.local_models = [model for model in self.local_models if model != model_name]
        else:
            print(f"Failed to remove model {model_name}: {response.status_code}")

    def get_local_models(self):
        """Get the list of local models"""
        # Scan the default storage path of Ollama to get the list of local models
        response = requests.get("http://localhost:11434/api/tags")
        if response.status_code == 200:
            models = response.json().get('models', [])
            self.local_models = [model['name'] for model in models]
        else:
            print(f"Failed to fetch local models: {response.status_code}")
        return self.local_models

    def show_model_details(self, model_name):
        """Show details of a specific local model"""
        payload = {"model": model_name}
        response = requests.post("http://localhost:11434/api/show", json=payload)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Failed to fetch details for model {model_name}: {response.status_code}")

    def get_downloadable_models(self):
        """Get the list of downloadable models"""
        print("Not implemented yet")
        return None