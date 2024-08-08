class AIModel:
    def __init__(self, model_id, system_instructions=""):
        self.model_id = model_id
        self.system_instructions = system_instructions+" If there is a probability of unsafe content in model response, warn the user and generate a response without unsafe content."

    # load context

    # generate response