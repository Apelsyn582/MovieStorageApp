from mongoengine import connect, Document, StringField, ListField, DateTimeField
from datetime import datetime
from bcrypt import hashpw, gensalt
import uuid

# Підключення до MongoDB
connect(
    host="mongodb+srv://dmytromalilo:ppVIDJe39t4rixWX@cluster0.v2zc9.mongodb.net/movieRatingDB?retryWrites=true&w=majority&appName=Cluster0"
)

# Модель для користувача
class User(Document):
    user_id = StringField(required=True, unique=True)  # Унікальний ідентифікатор
    username = StringField(required=True, unique=True)  # Унікальне ім'я користувача
    email = StringField(required=True, unique=True)  # Електронна пошта
    password_hash = StringField(required=True)  # Хеш пароля
    created_at = DateTimeField(default=datetime.utcnow)  # Дата створення
    favorites = ListField(StringField())  # Список ID улюблених фільмів
    watchlist = ListField(StringField())  # Список ID фільмів для перегляду

    meta = {
        'collection': 'Users'  # Назва колекції
    }

# Функція для створення нового користувача
#def create_user(username, email, password):
#    hashed_password = hashpw(password.encode('utf-8'), gensalt()).decode('utf-8')

#    new_user = User(
#        user_id=str(uuid.uuid4()),  # Генеруємо унікальний user_id
 #       username=username,
#        email=email,
#        password_hash=hashed_password,
#        favorites=[],
#        watchlist=[]
#    )
#    try:
 #       new_user.save()
 #       print(f"User '{username}' added successfully!")
 #   except Exception as e:
 #       print(f"Error: {e}")

# Використання
#create_user("User123", "user123@example.com", "secure_password")
