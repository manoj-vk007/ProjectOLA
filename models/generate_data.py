import pandas as pd
import numpy as np

np.random.seed(42)

n = 10000

temperature = np.random.uniform(25, 45, n)
soc = np.random.uniform(20, 100, n)
voltage = np.random.uniform(320, 420, n)
speed = np.random.uniform(0, 120, n)

# Synthetic battery health (target)
soh = (
    100
    - 0.6 * (temperature - 25)
    - 0.15 * (100 - soc)
    - 0.02 * speed
    - 0.01 * (420 - voltage)
    + np.random.normal(0, 1.5, n)
)

soh = np.clip(soh, 60, 100)

df = pd.DataFrame({
    "temperature": temperature,
    "soc": soc,
    "voltage": voltage,
    "speed": speed,
    "soh": soh
})

df.to_csv("data/training_data.csv", index=False)

print(df.head())
print("Dataset saved.")