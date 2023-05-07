

from core.domain.repositories.get_joke import GetJokeDefinition

class GetJokeUseCase():
    def __init__(self, get_joke_impl: GetJokeDefinition):
        self.get_joke_impl = get_joke_impl
    
    def run(self):
        return self.get_joke_impl.get_joke()