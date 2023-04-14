import pandas as p
import datetime

file_path = "client.csv"
data = p.read_csv(file_path)

# EXO 1
# print(data.head())

# EXO 2
# data.info()

# EXO 3
# professions = data['profession'].value_counts()
# print(professions)

# EXO 4
# countries = data['country'].value_counts()
# print(countries)

# EXO 5
# people_d =data[data['lastname'].str.startswith('D')].head(10)
# print(people_d)

# EXO 6
# contact_info = data[['firstname', 'lastname', 'email']]
# print(contact_info)

# EXO 7
# sorted_data = data.sort_values(by=['lastname'])
# print(sorted_data)

# EXO 8
# sorted_data.to_csv('sorted_data.csv', index=False)

# EXO 9
# most_common_city = data['city'].mode().iloc[0]
#print("La ville la plus fréquente est : ", most_common_city)

# EXO 10
# data_scientists = data[data['profession'] == "firefighter"]
# print(data_scientists)

# EXO 11
# data['birthdate'] = p.to_datetime(data['birthdate'], format="%m-%d-%Y")

# def calcule_age(birthdate):
#     today = datetime.datetime.now()
#     age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
#     return age

# data['age'] = data['birthdate'].apply(calcule_age)
# print(data['age'])
# age_par_profession = data.groupby('profession')['age'].mean()
# print(age_par_profession)

# EXO 12
# average_salary_by_profession = data.groupby('profession')['salary'].mean()
# print(average_salary_by_profession)

# EXO 13
# high_salary = data[data['salary'] > 5000]
# print(high_salary)

# EXO 14
percentage_by_country = data['country'].value_counts(normalize=True) * 100
print(percentage_by_country)