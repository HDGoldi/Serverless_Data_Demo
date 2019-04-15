from kiner.producer import KinesisProducer
from faker import Faker
from faker.providers import internet

p = KinesisProducer('testing-stream-2', batch_size=500, max_retries=5, threads=25)

fake = Faker()
fake.add_provider(internet)

my_country = [
'US','Germany','Italy',
'Austria','Canada','Spain',
'UK','Ireland']


#use 60000 for simulation of about 1000 messages per second
for i in range(10):
    request = {
        "IP Adresse": fake.ipv4_private(),
        "Country": fake.word(ext_word_list=my_country)
        }
    p.put_record(request)
    print(request)

p.close()