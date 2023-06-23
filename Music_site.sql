create table if not exists Genre (
	id SERIAL primary key,
	name VARCHAR(30) not NULL
);


create table if not exists Performer (
	id SERIAL primary key,
	name VARCHAR(40) not NULL
);

create table if not exists GenrePerformer (
	Genre_id INTEGER references Genre(id),
	Performer_id INTEGER references Performer(id),
	constraint pk_GenrePerformer primary key (Genre_id, Performer_id)
);

create table if not exists Album (
	id SERIAL primary key,
	name VARCHAR(40) unique not null,
	release_date INTEGER check(release_date>1900)
);

create table if not exists PerformerAlbum (
	Performer_id INTEGER references Performer(id),
	Album_id INTEGER references Album(id),
	constraint pk_PerformerAlbum primary key (Performer_id, Album_id)
);

create table if not exists Track (
	id SERIAL primary key,
	name VARCHAR(50) unique not null,
	duration INTEGER,
	Album_id INTEGER references Album(id)
);

create table if not exists Collection (
	id SERIAL primary key,
	name VARCHAR(40) unique not null,
	release_date INTEGER check(release_date>1900)
);

create table if not exists TrackCollection (
	Track_id INTEGER references Track(id),
	Collection_id INTEGER references Collection(id),
	constraint pk_TrackCollection primary key (Track_id, Collection_id)
);