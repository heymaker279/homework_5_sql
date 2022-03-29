create table if not exists Genre(
	genre_id serial primary key,
	genre_name varchar(80) unique not null
);

create table if not exists Artists(
	artist_id serial primary key,
	artist_name varchar(80) not null
);

create table if not exists GenreArtists(
	genres_id integer not null references Genre(genre_id),
	artists_id integer not null references Artists(artist_id),
	constraint pk primary key (genres_id, artists_id)
);

create table if not exists Albums(
	album_id serial primary key, 
	album_name varchar(80) not null,
	year_ integer not null	
);

create table if not exists ArtistsAlbums( 
	artists_id integer not null references Artists(artist_id),
	albums_id integer not null references Albums(album_id),
	constraint p_k primary key (albums_id, artists_id)	
);

create table if not exists Track( 
	track_id serial primary key, 
	track_name varchar(80) not null,
	track_time numeric(2,1) not null,
	albums_id integer not null references Albums(album_id)
);

create table if not exists Collection(
	collection_id serial primary key,
	name_ varchar(80) not null,
	year_ integer not null
);

create table if not exists CollectionTrack(
	collections_id integer not null references Collection(collection_id),
	tracks_id integer not null references Track(track_id),
	constraint _p_k primary key (collections_id, tracks_id)
);
