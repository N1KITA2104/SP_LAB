from grammar import *

# Створення генератора граматики та друк правил і генерація рядків
generator = GrammarGenerator()

# Додавання базових правил
generator.add_rule('S0', 'ε')
generator.add_rule('S1', 'kk')
generator.add_rule('S2', 'kg')
generator.add_rule('S3', 'g')
generator.add_rule('S4', 'gk')
# Побудова складніших конструкцій
generator.add_rule('S5', ['S2 S6'])
generator.add_rule('S6', ['S2 S6', 'S3'])
# ((kg)+g)*:
generator.add_rule('S7', ['S5', 'ε'])
# g(gk)*:
generator.add_rule('S8', ['S3 S9'])
generator.add_rule('S9', ['S4 S9', 'ε'])
# (kk|ε):
generator.add_rule('S10', ['S1', 'S0'])
# Загальне правило
generator.add_rule('S', ['S10 S7 S8'])

print(generator.generate_grammar())
print("\nGenerated strings:")
for _ in range(5):
    print(generator.generate_string())
