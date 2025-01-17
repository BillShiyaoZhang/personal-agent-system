class Model:
    """
    Model class represents a LLM model in the system.

    For the first implementation, we only consider Ollama models.
    
    Also, we can add more attributes in the future.
    For example, to include different types of models.
    """

    def __init__(self, name, description=None):
        self.name = name
        self.description = description
        self.tags = []