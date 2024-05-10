import random


class GrammarGenerator:
    def __init__(self):
        self.rules = {}

    def add_rule(self, non_terminal, expansions):
        if isinstance(expansions, str):
            expansions = [expansions]
        if non_terminal in self.rules:
            self.rules[non_terminal].extend(expansions)
        else:
            self.rules[non_terminal] = expansions

    def generate_grammar(self):
        grammar = []
        for non_terminal, expansions in self.rules.items():
            grammar.append(f"{non_terminal} -> {' | '.join(expansions)}")
        return '\n'.join(grammar)

    def generate_string(self, non_terminal='S'):
        expansion = random.choice(self.rules[non_terminal])
        if expansion == 'ε':
            return ''

        generated_string = []
        for symbol in expansion.split():
            if symbol in self.rules:
                generated_string.append(self.generate_string(symbol))
            else:
                generated_string.append(symbol)

        return ''.join(generated_string)
