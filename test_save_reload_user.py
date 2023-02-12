




from models.user import User
from models.amenity import Amenity
from models.review import Review
from models.city import City

method = getattr(User, "all")
print(method())