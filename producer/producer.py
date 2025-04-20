import json
import time
import random
from datetime import datetime, timedelta
from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Catégories et produits fictifs
categories = {
    'Informatique': ['Ordinateur', 'Clavier', 'Souris', 'Écran'],
    'Téléphonie': ['Téléphone', 'Accessoires téléphone'],
    'Maison': ['Lampe', 'Table', 'Chaise', 'Tapis'],
}

# Pays associés à chaque région
pays_par_region = {
    'Europe': ['France', 'Allemagne', 'Espagne', 'Italie', 'Royaume-Uni'],
    'Asie': ['Chine', 'Inde', 'Japon', 'Corée du Sud', 'Singapour'],
    'Amérique': ['États-Unis', 'Canada', 'Mexique', 'Brésil', 'Argentine'],
    'Afrique': ['Nigeria', 'Afrique du Sud', 'Égypte', 'Kenya', 'Ghana', 'Algérie'],  # Algérie ajoutée ici
}

regions = list(pays_par_region.keys())

# Prix unitaire des produits
prix_unitaire = {
    'Ordinateur': 800.0,
    'Clavier': 30.0,
    'Souris': 20.0,
    'Écran': 250.0,
    'Téléphone': 500.0,
    'Accessoires téléphone': 15.0,
    'Lampe': 45.0,
    'Table': 120.0,
    'Chaise': 75.0,
    'Tapis': 150.0,
}

def generate_random_datetime():
    # Définir les bornes pour les dates de 2023 à 2024
    start_date = datetime(2023, 1, 1)
    end_date = datetime(2024, 12, 31, 23, 59, 59)

    # Calculer le nombre total de secondes dans cette période
    total_seconds = int((end_date - start_date).total_seconds())

    # Tirer un nombre de secondes aléatoire
    random_seconds = random.randint(0, total_seconds)

    # Ajouter ce nombre de secondes à la date de départ
    random_date = start_date + timedelta(seconds=random_seconds)

    return random_date.strftime("%Y-%m-%d %H:%M:%S")

def generate_vente():
    # Choisir une catégorie aléatoire et un produit associé
    category = random.choice(list(categories.keys()))
    produit = random.choice(categories[category])
    
    # Quantité aléatoire entre 1 et 10
    quantity = random.randint(1, 10)

    # Calcul du montant total
    montant = round(prix_unitaire[produit] * quantity, 2)

    # Choisir une région et un pays dans cette région
    region = random.choice(regions)
    pays = random.choice(pays_par_region[region])

    return {
        'date_heure': generate_random_datetime(),
        'montant': montant,
        'quantité': quantity,
        'produit': produit,
        'categorie': category,
        'region': region,
        'pays': pays
    }

if __name__ == "__main__":
    while True:
        vente = generate_vente()
        print(f"Envoi : {vente}")
        producer.send('ventes', vente)
        time.sleep(2)  # Envoi toutes les 2 secondes
