import pandas as pd

# Lire les tables à partir de l'URL spécifiée
dfs = pd.read_html("https://topforeignstocks.com/indices/components-of-the-sp-500-index/")

# Afficher le nombre de tables trouvées
print(f"Nombre de tables trouvées : {len(dfs)}")

# Si plusieurs tables sont trouvées, vous pouvez les parcourir pour choisir celle qui vous intéresse
for i, df in enumerate(dfs):
    print(f"Table {i}:")
    print(df)  # Afficher la table DataFrame
