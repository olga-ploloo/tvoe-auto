from django.db import models

#class AutoModel(models.Model):
with open('output1.csv', 'w') as f:
    f.write('Title, Bel, Dol, Euro, Year')
df = pd.DataFrame[text_name, price_bel, price_doll, price_euro, text_years]
df.to_csv("output1.csv", index=False, mode='a', header=False)