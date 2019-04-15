from faker import Faker
from faker.providers import internet

fake = Faker()
fake.add_provider(internet)

my_country = [
'US','Germany','Italy',
'Austria','Canada','Spain',
'UK','Ireland']

request = {
    "IP Adresse": fake.ipv4_private(),
    "Country": fake.word(ext_word_list=my_country)
    }

print(request)

