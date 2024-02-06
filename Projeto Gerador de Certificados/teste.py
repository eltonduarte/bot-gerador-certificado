import pandas as pd

# Suponha que 'df' seja o seu DataFrame
data = {'Nome': ['João', 'Maria', 'José'],
        'Idade': [30, 25, 40],
        'Cargo': ['Gerente', 'Analista', 'Diretor']}
df = pd.DataFrame(data)

# Iterando sobre duas séries do DataFrame
for index, row in df.iterrows():
    print("Nome:", row['Nome'])
    print("Idade:", row['Idade'])
    print("Cargo:", row['Cargo'])
    print("\n")
