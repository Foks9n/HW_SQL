insert into genre(name) values
('Hard Rock'),
('Industrial Metal'),
('Heavy Metal'),
('Punk Rock'),
('Metal'),
('Power Metal');

insert into performer(name) values
('Rammstein'), --hard rock - industrial metal - metal
('Порнофильмы'), --punk rock
('Static - X'), --industrial metal
('System of a Down'), --Metal - hard rock
('Bullet for my Valentine'), --hard rock
('AC / DC'), --hard rock
('Guns N Roses'), --hard rock - heavy metal
('Arda');

insert into genreperformer values
(1, 1),
(1, 4),
(1, 5),
(1, 6),
(1, 7),
(2, 1),
(2, 3),
(3, 7),
(4, 2),
(5, 1),
(5, 4),
(6, 8);

insert into album(name, release_date) values
('Sehnsucht', 1997), --rammsstein
('Это пройдет', 2020),
('Shadow Zone', 2003), -- static-X
('Mezmerize', 2005),
('Fever', 2010),
('Back in Black', 1980),
('Appetite for Destruction', 1987),
('О скитаниях вечных и о земле', 2004);

insert into performeralbum values
(1, 1),
(2, 2),
(3, 3),
(4, 4),
(5, 5),
(6, 6),
(7, 7),
(8, 8);

insert into track(name, duration, album_id) values
('Du hast', '00:03:54', 1),
('Engel', '00:04:24', 1),
('Это пройдет', '00:03:55', 2),
('Чужое горе', '00:03:24', 2),
('Доброе сердце', '00:04:11', 2),
('The Only', '00:02:55', 3),
('Monster', '00:02:14', 3),
('B.Y.O.B', '00:04:16', 4),
('Cigaro', '00:02:11', 4),
('Your Betrayal', '00:05:41', 5),
('The Last Flight', '00:06:16', 5),
('Hells Bells', '00:05:46', 6),
('Shoot to Thrill', '00:05:49', 6),
('Welcome To The Jungle', '00:04:39', 7),
('Paradise City', '00:06:57', 7),
('Первая зима', '00:04:49', 8),
('О скитаниях...', '00:07:39', 8),
('Ради звезд', '00:05:16', 8),
('Let me put my love into you', '00:04:11', 6);

insert into collection(name, release_date) values
('The last millennium', 2005),
('Russian Rock', 2020),
('Heavy Music', 2015),
('Germany Classic', 2019);

insert into trackcollection values
(1, 1),
(2, 1),
(12, 1),
(13, 1),
(14, 1),
(15, 1),
(3, 2),
(4, 2),
(5, 2),
(16, 2),
(17, 2),
(18, 2),
(6, 3),
(7, 3),
(8, 3),
(9, 3),
(16, 3),
(17, 3),
(18, 3),
(1, 4),
(2, 4);





