"""
TODO 4.5. Métriques de journalisation
- Ce fichier est fourni à titre d'exemple. 
- Vous pouvez vous en insipirer pour créer votre visualisation propre à vos métriques.
"""


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


__name__ = "metrics"
__author__ = "CDL & <votre nom>"
__version__ = 1.0


# Exemples de données
data = {
    "timestamp": ["2024-03-19 10:00:01", "2024-03-19 10:05:00", "2024-03-19 10:10:45",
                  "2024-03-19 10:15:30", "2024-03-19 10:20:15"],
    "severity": ["INFO", "DEBUG", "CRITICAL", "INFO", "DEBUG"]
}

# Créer un DataFrame
df = pd.DataFrame(data)
df["timestamp"] = pd.to_datetime(df["timestamp"])

# Ajouter une colonne "count" pour faciliter la visualisation
df['count'] = 1

# Visualisation avec Seaborn
plt.figure(figsize=(10, 6))
sns.lineplot(x="timestamp", y=np.cumsum(
    df['count']), hue="severity", data=df, marker="o")

plt.title("Logs Severity Over Time")
plt.xlabel("Time")
plt.ylabel("Cumulative Count")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
