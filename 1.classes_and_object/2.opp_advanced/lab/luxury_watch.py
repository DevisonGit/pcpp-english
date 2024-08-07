class LuxuryWatch:
    watches_created = 0

    def __init__(self):
        LuxuryWatch.watches_created += 1

    @classmethod
    def get_number_of_watches_created(cls):
        return cls.watches_created

    @classmethod
    def create_with_engraving(cls, engraving_text):
        if cls.validate_engraving_text(engraving_text):
            watch = cls()
            watch.engraving_text = engraving_text
            return watch
        else:
            raise ValueError("Engraving text must be alphanumeric and not longer than 40 characters.")

    @staticmethod
    def validate_engraving_text(text):
        if len(text) > 40:
            return False
        if not text.isalnum():
            return False
        return True


# Create a watch with no engraving
watch1 = LuxuryWatch()
print(f"Number of watches created: {LuxuryWatch.get_number_of_watches_created()}")

# Create a watch with correct text for engraving
try:
    watch2 = LuxuryWatch.create_with_engraving("MyLuxuryWatch2024")
    print(f"Number of watches created: {LuxuryWatch.get_number_of_watches_created()}")
except ValueError as e:
    print(e)

# Try to create a watch with incorrect text
try:
    watch3 = LuxuryWatch.create_with_engraving("foo@baz.com")
    print(f"Number of watches created: {LuxuryWatch.get_number_of_watches_created()}")
except ValueError as e:
    print(f"Failed to create watch with engraving: {e}")

# Check the final number of watches created
print(f"Final number of watches created: {LuxuryWatch.get_number_of_watches_created()}")
