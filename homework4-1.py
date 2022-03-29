from audioop import add
import sqlalchemy
import pandas as pd
if __name__ == "__main__":
    with open("requirements.txt") as f:
        file = f.readlines()
        password_psql = file[0]
    db = f"postgresql://postgres:{password_psql}@localhost:5432/postgres"
    engine = sqlalchemy.create_engine(db)
    connection = engine.connect()

    def filling_in_the_table():
        with open("Albums.txt") as f:
            file = f.read().split("\n")
            file = [i.split(',') for i in file]
            for i in file:
                name = i[0]
                year = int(i[1])
                connection.execute(f"""INSERT INTO albums(album_name, year_)
                VALUES('{name}',{year});
                """)

        with open("Artists.txt") as f:
            file = f.read().split("\n")
            for i in file:
                connection.execute(f"""INSERT INTO artists(artist_name)
                VALUES('{i}');
                """)

        with open("genre.txt") as f:
            file = f.read().split("\n")
            for i in file:
                connection.execute(f"""INSERT INTO genre(genre_name)
                VALUES('{i}');
                """)

        with open("collection.txt") as f:
            file = f.read().split("\n")
            file = [i.split(',') for i in file]
            for i in file:
                name = i[0]
                year = int(i[1])
                connection.execute(f"""INSERT INTO collection(name_, year_)
                VALUES('{name}', {year});
                """)

        with open("Tracks.txt") as f:
            file = f.read().split("\n")
            file = [i.split(',') for i in file]
            for i in file:
                name = i[0]
                time = float(i[1])
                album_id = int(i[2])
                connection.execute(f"""INSERT INTO track(track_name, track_time, albums_id)
                VALUES('{name}', {time}, {album_id});
                """)

        with open("GenreArtists.txt") as f:
            file = f.read().split("\n")
            file = [i.split(',') for i in file]
            for i in file:
                genre_id = int(i[0])
                artist_id = int(i[1])
                connection.execute(f"""INSERT INTO genreartists(genres_id, artists_id)
                VALUES({genre_id},{artist_id});
                """)

        with open("ArtistsAlbum.txt") as f:
            file = f.read().split("\n")
            file = [i.split(',') for i in file]
            for i in file:
                artist_id = int(i[0])
                album_id = int(i[1])
                connection.execute(f"""INSERT INTO artistsalbums(artists_id, albums_id)
                VALUES({artist_id},{album_id});
                """)
            
        with open("CollectionTrack.txt") as f:
            file = f.read().split("\n")
            file = [i.split(',') for i in file]
            for i in file:
                collection_id = int(i[0])
                track_id = int(i[1])
                connection.execute(f"""INSERT INTO collectiontrack(collections_id, tracks_id)
                VALUES({collection_id},{track_id});
                """)
    # filling_in_the_table()




