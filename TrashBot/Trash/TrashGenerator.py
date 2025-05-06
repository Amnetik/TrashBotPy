import os
from .PseudoRandom import NonRepeatingRandom
import requests

class TrashGenerator:
    def __init__(self, name):
        self._name = name
    
    def get_trash(self) -> str:
        return ''
    
    def __repr__(self):
        return self.__str__()
    
    def __str__(self):
        return self._name
    
class TrashGeneratorByList(TrashGenerator):
    def __init__(self, name: str, filename: str):
        super().__init__(name)
        self._line_count = 0
        self._path = os.path.join(os.path.dirname(__file__), 'TrashByList', filename)
        if not os.path.exists(self._path):
            self._path = None
            return
        with open(self._path, 'r+', encoding='utf-8') as f:
            f.seek(0)
            self._line_count = len([l for l in f.readlines() if l.strip() != ''])
        self._pseudo_random = NonRepeatingRandom(self._line_count)
            
    def get_trash(self):
        if self._line_count == 0:
            return ''
        random_line_index = self._pseudo_random.get_next()
        try:
            with open(self._path, 'r+', encoding='utf-8') as f:
                f.seek(0)
                return f.readlines()[random_line_index].strip()
        except Exception as e:
            raise e
       
class TrashGeneratorByPrompt(TrashGenerator):
    def get_trash(self):
        # Send a GET request to a URL
        url = 'https://evilinsult.com/generate_insult.php?lang=en&type=text'  # Replace with your desired URL
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Read the result (response content)
            print("Response Text:")
            print(response.text)  # The raw content of the response (HTML, JSON, etc.)