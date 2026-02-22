
import pandas as pd 

df = pd.read_csv('BullishAndBaerishWhaletransactions.csv')

class Whale:
    def __init__(self, address, amount):
        self.address = address  #self sagt compiler beziehe dich auf das attribut des spezifischen objekts 
        self.amount = amount
        self.is_significant = false # Standardmäßig auf False setzen

    def __control_significance(self):
        if self.amount > 1000000:  # Beispiel: Signifikante Transaktionen sind über 1 Million
            self.is_significant = True


for index, row in df.iterrows():
    Whale(row['address'], row['transaction_type'], row['amount'])