import pandas as p
import re

file_path = "client.csv"
data_frame = p.read_csv(file_path)

# ma_date = data_frame['birthdate'][0]
# annee = ma_date[6 :]
# jour = ma_date[3 : -5]
# mois = ma_date[:2]
# print("la date en francais : {0}-{1}-{2}".format(jour, mois, annee))

# transform date to object in dataframe
data_frame['birthdate'] = p.to_datetime(data_frame['birthdate'], format="%m-%d-%Y")
# modifie le format
data_frame['birthdate'] = data_frame['birthdate'].dt.strftime("%d-%m-%Y")
print(data_frame)

#
maReg = "^[A-Za-z]{1,50}[- ']{0,1}[A-Za-z]{1,50}$"
print(data_frame['lastname'][0])