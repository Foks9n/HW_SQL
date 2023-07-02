-- Название и продолжительность самого длинного трека
select name, duration from track
order by duration desc 
limit 1;

-- Название треков, продолжительность которых не менее 3,5 минут
select name  from track
where duration >= '00:03:30';

-- Названия сборников, вышедших в период с 2018 по 2020 год включительно
select name from collection
where release_date between 2018 and 2020;

-- Исполнители, чьё имя состоит из одного слова
select name from performer
where name not like '% %';

-- Название треков, которые содержат слово «мой» или «my»
select name from track
WHERE name LIKE 'my %' OR name LIKE '% my' OR name LIKE '% my %' OR name = 'my'
OR name LIKE 'мой %' OR name LIKE '% мой' OR name LIKE '% мой %' OR name = 'мой';

-- Количество исполнителей в каждом жанре
select name, count(performer_id) from genre
join genreperformer on genre.id = genreperformer.genre_id
group by name;

-- Количество треков, вошедших в альбомы 2019–2020 годов
select count(track.name) from track
join album on track.album_id = album.id
where release_date between 2019 and 2020;

-- Средняя продолжительность треков по каждому альбому
select album.id, avg(duration)  from track
join album on track.album_id = album.id
group by album.id;

-- Все исполнители, которые не выпустили альбомы в 2020 году
select performer.name from performer
join performeralbum on performer.id  = performeralbum.performer_id
join album on album.id = performeralbum.album_id
where release_date != 2020
group by performer.name;

-- Названия сборников, в которых присутствует конкретный исполнитель (Arda)
select collection.name from collection
join trackcollection on collection.id = trackcollection.collection_id
join track on track.id = trackcollection.track_id
join album on track.album_id = album.id
join performeralbum on album.id = performeralbum.album_id 
join performer on performer.id = performeralbum.performer_id
where performer.name = 'Arda'
group by collection.name;

-- Названия альбомов, в которых присутствуют исполнители более чем одного жанра
select album.name from album
join performeralbum on album.id = performeralbum.album_id
join performer on performer.id = performeralbum.performer_id
join genreperformer on performer.id = genreperformer.performer_id
join genre on genre.id = genreperformer.genre_id 
group by album.name
having count(genre.name) > 1;

-- Наименования треков, которые не входят в сборники
select track.name from track
left join trackcollection on track.id = trackcollection.track_id
where trackcollection.collection_id is null;

-- Исполнитель или исполнители, написавшие самый короткий по продолжительности трек, — теоретически таких треков может быть несколько
select performer.name, track.duration from track
join album on track.album_id = album.id
join performeralbum on album.id = performeralbum.album_id
join performer on performer.id = performeralbum.performer_id
where track.duration = (select min(track.duration) from track);

-- Названия альбомов, содержащих наименьшее количество треков
select distinct album.name from album
left join track on track.album_id = album.id
where track.album_id in (
	select track.album_id from track
	group by track.album_id
	having count(track.album_id) = (
		select count(track.id) from track
		group by track.album_id
		order by count
		limit 1
)
);





