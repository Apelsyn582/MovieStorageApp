from mongoengine import connect, Document, StringField, DateTimeField
from datetime import datetime
import uuid

# Підключення до бази даних
connect(
    host="mongodb+srv://dmytromalilo:ppVIDJe39t4rixWX@cluster0.v2zc9.mongodb.net/movieRatingDB?retryWrites=true&w=majority&appName=Cluster0"
)

# Модель для лайкнутих фільмів
class LikedMovie(Document):
    title = StringField(required=True)
    rate = StringField(required=True)
    date = StringField(required=True)
    file = StringField(required=True)

    liked_at = DateTimeField(default=datetime.utcnow)  # Дата лайку
    meta = {
        'collection': 'LikedMovies'  # Назва колекції у MongoDB
    }

# Додавання нового лайку
#new_like = LikedMovie(
#    user_id="unique_user_id",
#    movie_id="unique_movie_id"
#)

#try:
#    new_like.save()
#    print(f"Like added successfully for user '{new_like.user_id}' and movie '{new_like.movie_id}'!")
#except Exception as e:
#    print(f"Error: {e}")
