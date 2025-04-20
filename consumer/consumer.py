from kafka import KafkaConsumer
from pymongo import MongoClient
import json

# Connexion Kafka
consumer = KafkaConsumer(
    'ventes',
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

# Connexion MongoDB avec auth
client = MongoClient("mongodb://ilhem:ilhem@localhost:27017/")
db = client['streaming']
collection = db['ventes_stream']

print("🟢 Consommateur connecté à MongoDB. En attente des messages...")

for message in consumer:
    vente = message.value
    print("💾 Vente reçue :", vente)
    collection.insert_one(vente)
