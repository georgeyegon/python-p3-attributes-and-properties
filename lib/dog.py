class Dog:
    APPROVED_BREEDS = ['Labrador', 'Poodle', 'Bulldog']  # Example breeds

    def __init__(self, name, breed=None):
        if not isinstance(name, str) or not (1 <= len(name) <= 25):
            print("Name must be string between 1 and 25 characters.")
            return
        self.name = name

        if breed not in self.APPROVED_BREEDS:
            print("Breed must be in list of approved breeds.")
            return
        self.breed = breed
