from mongoengine import connect, Document, StringField, ListField, IntField, URLField

# Підключення до бази даних
connect(
    host="mongodb+srv://dmytromalilo:ppVIDJe39t4rixWX@cluster0.v2zc9.mongodb.net/movieRatingDB?retryWrites=true&w=majority&appName=Cluster0"
)

# Модель для колекції Movies
class Movie(Document):
    show_id = StringField(required=True, unique=True)  # Унікальний ідентифікатор
    type = StringField(required=True, choices=["Movie", "TV Show"])  # Тип
    title = StringField(required=True)  # Назва
    director = StringField()  # Режисер
    cast = ListField(StringField())  # Список акторів
    country = StringField()  # Країна
    date_added = StringField()  # Дата додавання
    release_year = IntField()  # Рік випуску
    duration = StringField()  # Тривалість
    listed_in = ListField(StringField())  # Жанри
    description = StringField()  # Опис
    cast_count = IntField()  # Кількість акторів
    poster_url = URLField()  # URL до постера

    meta = {
        'collection': 'Movies'  # Назва колекції у MongoDB
    }

# Додавання нового запису
new_movie = Movie(
    show_id="s20",
    type="Movie",
    title="Dick Johnson Is Dead",
    director="Kirsten Johnson",
    cast=[],
    country="United States",
    date_added="September 25, 2021",
    release_year=2020,
    duration="90 min",
    listed_in=["Documentaries"],
    description="As her father nears the end of his life, filmmaker Kirsten Johnson stages his death...",
    cast_count=0,
    poster_url="https://www.themoviedb.org/movie/653574-dick-johnson-is-dead"
)

# Збереження запису в базу даних
try:
    new_movie.save()
    print(f"Movie '{new_movie.title}' added successfully!")
except Exception as e:
    print(f"An error occurred while adding the movie: {e}")
