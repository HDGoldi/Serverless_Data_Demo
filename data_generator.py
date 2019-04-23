from faker import Faker
from faker.providers import internet
import time

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


@staticmethod
def get_kinesis_record():
    """
    Generate an item with a random hash key on a large range, and a unique sort key, and  a created date
    """
    item = {'hashKey': randrange(0, 5000000), 'sortKey': str(uuid.uuid4()), 'created': datetime.datetime.utcnow().isoformat()}
    raw_data = json.dumps(item)
    encoded_data = bytes(raw_data)
    kinesis_record = {
        'Data': encoded_data,
        'PartitionKey': str(item['hashKey']),
    }

    return kinesis_record

print(get_kinesis_record)