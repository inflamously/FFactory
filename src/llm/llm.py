import subprocess

class OllamaModelDetail:
    def __init__(self, detail):
        self.format = detail.format
        self.family = detail.family
        self.parameter_size = detail.parameter_size
        self.quantization_level = detail.quantization_level


class OllamaModelDescription:
    def __init__(self, model):
        self.__model = model
        self.name = model.model
        self.details: OllamaModelDetail = model.details

    def __repr__(self):
        return "{}:{}:{}".format(self.name, self.details.parameter_size, self.details.format)


def run_ollama():
    try:
        print("setting up ollama")
        ollama_process = subprocess.run("ollama -v", capture_output=True, timeout=30)
        result = ollama_process.stdout.decode("utf-8")
        if "could not connect to a running Ollama instance" in result:
            print("ollama service must be running")
            exit(1)
    except Exception as e:
        if e is subprocess.TimeoutExpired:
            print("ollama could not be found or started")
            exit(1)
        print("an exception occured", e)
