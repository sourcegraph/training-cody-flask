from flask import Blueprint, jsonify
from flask_refactor.models.pet import Pet

api_bp = Blueprint('api', __name__, url_prefix='/api')

@api_bp.route('/pets/random', methods=['GET'])
def random_pet():
    """Return a randomly generated pet"""
    # Create a random pet using our Pet class
    pet = Pet.random()
    # Convert to dictionary for JSON serialization
    return jsonify(pet.to_dict())

@api_bp.route('/pets/random/batch/<int:count>', methods=['GET'])
def random_pets_batch(count):
    """Return multiple randomly generated pets
    
    Args:
        count: Number of pets to generate (limited to 50 max)
    """
    if count > 50:
        count = 50  # Limit to 50 pets maximum
    
    # Generate multiple pets and convert each to a dictionary
    pets = [Pet.random().to_dict() for _ in range(count)]
    return jsonify(pets)
