from flask import Blueprint, jsonify
import random
import uuid

api_bp = Blueprint('api', __name__, url_prefix='/api')

# Pet statuses according to the Swagger Petstore schema
PET_STATUSES = ["available", "pending", "sold"]

def generate_random_pet():
    """Generate a random pet based on the Swagger Petstore schema"""
    return {
        "id": random.randint(1, 10000),
        "name": f"Pet-{uuid.uuid4().hex[:8]}",
        "category": {
            "id": random.randint(1, 5),
            "name": random.choice(["Dogs", "Cats", "Birds", "Reptiles", "Fish"])
        },
        "photoUrls": [
            f"https://example.com/pet/photos/{random.randint(1000, 9999)}.jpg",
            f"https://example.com/pet/photos/{random.randint(1000, 9999)}.jpg"
        ],
        "tags": [
            {
                "id": random.randint(1, 10),
                "name": random.choice(["friendly", "trained", "vaccinated", "young", "senior"])
            },
            {
                "id": random.randint(11, 20),
                "name": random.choice(["playful", "cuddly", "energetic", "calm", "social"])
            }
        ],
        "status": random.choice(PET_STATUSES)
    }

@api_bp.route('/pets/random', methods=['GET'])
def random_pet():
    """Return a randomly generated pet"""
    return jsonify(generate_random_pet())

@api_bp.route('/pets/random/batch/<int:count>', methods=['GET'])
def random_pets_batch(count):
    """Return multiple randomly generated pets
    
    Args:
        count: Number of pets to generate (limited to 50 max)
    """
    if count > 50:
        count = 50  # Limit to 50 pets maximum
    
    pets = [generate_random_pet() for _ in range(count)]
    return jsonify(pets)
