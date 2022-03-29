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

'''1'''
def count_artists_name():
    res = connection.execute(
        """SELECT genre_name, COUNT(artist_name) FROM artists
        LEFT JOIN genreartists ON artist_id = artists_id
        LEFT JOIN genre ON genres_id = genre_id
        GROUP BY genre_id
        ORDER BY genre_id
        ;""") 
    print(list(res))
count_artists_name()

'''2'''
def count_track():
    res = connection.execute(
        """SELECT album_name, year_, COUNT(track_name) FROM albums
        LEFT JOIN track ON album_id = albums_id
        WHERE year_ BETWEEN 2019 AND 2020
        GROUP BY album_id;""") 
    print(list(res))
count_track()

'''3'''
def avr_track_time():
    res = connection.execute(
        """SELECT album_id, album_name, ROUND(AVG(track_time), 2) FROM albums
        LEFT JOIN track ON album_id = albums_id
        GROUP BY album_id
        ORDER BY album_id;""") 
    print(list(res))
avr_track_time()

'''4'''
def artists_20():
    res = connection.execute(
        """SELECT artist_id, artist_name FROM artists
        LEFT JOIN artistsalbums ON artist_id = artists_id
        LEFT JOIN albums ON albums_id = album_id
        WHERE artist_id NOT IN(SELECT artist_id FROM artists
        LEFT JOIN artistsalbums ON artist_id = artists_id
        LEFT JOIN albums ON albums_id = album_id
        WHERE year_ = 2020)
        GROUP BY artist_id
        ORDER BY artist_id
        ;""") 
    print(list(res))
artists_20()

'''5'''
def collection_name():
    c_name = (input('Введите имя артиста: ').title())
    res = connection.execute(
        f"""SELECT collection_id, name_ FROM collection
        LEFT JOIN collectiontrack ON collection_id = collections_id
        LEFT JOIN track ON tracks_id = track_id
        LEFT JOIN albums ON albums_id = album_id
        LEFT JOIN artistsalbums a ON album_id = a.albums_id
        LEFT JOIN artists ON artists_id = artist_id
        WHERE artist_name = '{c_name}'
        GROUP BY artist_id, collection_id
        ORDER BY artist_id
        ;""") 
    print(list(res))
collection_name()

'''6'''
def album_names():
    res = connection.execute(
        """SELECT album_id, album_name FROM albums
        LEFT JOIN artistsalbums ON albums.album_id = artistsalbums.albums_id
        LEFT JOIN artists ON artistsalbums.artists_id = artists.artist_id
        LEFT JOIN genreartists ON artists.artist_id = genreartists.artists_id
        LEFT JOIN genre ON genreartists.genres_id = genre.genre_id
        GROUP BY album_name, album_id
        HAVING COUNT(DISTINCT genre_name) > 1
        ORDER BY album_id
        ;""") 
    print(list(res))
album_names()

'''7'''
def track_not_in_collection():
    res = connection.execute(
        """SELECT track_id, track_name FROM track
        LEFT JOIN collectiontrack ON track_id = tracks_id
        LEFT JOIN collection ON collections_id = collection_id
        WHERE track_id NOT IN(SELECT tracks_id FROM collectiontrack)
        GROUP BY track_id
        ORDER BY track_id
        ;""") 
    print(list(res))
track_not_in_collection()

'''8'''
def track_time_min():
    res = connection.execute(
        """SELECT artist_name, track_time FROM artists
        LEFT JOIN artistsalbums ON artist_id = artists_id
        LEFT JOIN albums ON albums_id = album_id
        LEFT JOIN track t ON album_id = t.albums_id
        WHERE track_time IN(SELECT MIN(track_time) FROM track)
        GROUP BY  artist_name, track_time
        ORDER BY artist_name
        ;""") 
    print(list(res))
track_time_min()

'''9'''
def album_track_min():
    res = connection.execute(
        """SELECT album_name FROM albums
        LEFT JOIN track ON album_id = albums_id
        GROUP BY album_id
        HAVING COUNT(track_id) =(
            SELECT COUNT(track_id) FROM track 
            LEFT JOIN albums ON albums_id = album_id        
            GROUP BY album_id, albums_id
            ORDER BY COUNT(track_id)
            LIMIT 1       )
        ORDER BY album_id
        ;""") 
    print(list(res))
album_track_min()