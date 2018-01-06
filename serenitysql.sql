DROP DATABASE IF EXISTS serenity;
CREATE DATABASE serenity;
USE serenity;


DROP TABLE IF EXISTS ROOM;
DROP TABLE IF EXISTS PLAYER;
DROP TABLE IF EXISTS OBJECT;
DROP TABLE IF EXISTS ITEM;
DROP TABLE IF EXISTS DESCRIPTION;
DROP TABLE IF EXISTS MOVEMENT;


CREATE USER 'dbuser09'@'localhost' IDENTIFIED BY 'dbpass';
GRANT SELECT, INSERT, UPDATE, DELETE ON serenity.* TO dbuser09@localhost;

CREATE TABLE DESCRIPTION (
	description_id INT(2)NOT NULL,
	descript VARCHAR(1000) NOT NULL,
	PRIMARY KEY (description_id)
);

CREATE TABLE ROOM (
	room_id int(2) NOT NULL,
	name VARCHAR(1000) NOT NULL,
	shortdescription VARCHAR(1000) NOT NULL,
	description_id INT NOT NULL,
	locked INT,
	fire INT,
	dark INT,
	visited INT,
	PRIMARY KEY (room_id),
	FOREIGN KEY (description_id) REFERENCES DESCRIPTION(description_id)
);

CREATE TABLE OBJECT (
	object_id INT NOT NULL,
	name VARCHAR(100) NOT NULL,
	room_id INT,
	description_id INT NOT NULL,
	PRIMARY KEY (object_id),
	FOREIGN KEY (room_id) REFERENCES ROOM(room_id),
	FOREIGN KEY (description_id) REFERENCES DESCRIPTION(description_id)
);

CREATE TABLE PLAYER (
	player_id INT(2) NOT NULL,
	room_id INT(2) NOT NULL,
	mask INT,
	PRIMARY KEY (player_id),
	FOREIGN KEY (room_id) REFERENCES ROOM(room_id)
);

CREATE TABLE ITEM (
	item_id INT(2) NOT NULL,
	name VARCHAR(1000) NOT NULL,
	player_id INT(2),
	room_id INT(2),
	object_id INT(2),
	description_id INT NOT NULL,
	PRIMARY KEY (item_id),
	FOREIGN KEY (room_id) REFERENCES ROOM(room_id),
	FOREIGN KEY (object_id) REFERENCES OBJECT(object_id),
	FOREIGN KEY (player_id) REFERENCES PLAYER(player_id),
	FOREIGN KEY (description_id) REFERENCES DESCRIPTION(description_id)
);


CREATE TABLE MOVEMENT (
	mista INT NOT NULL,
	minne INT NOT NULL,
	direction VARCHAR(5),
	PRIMARY KEY (mista, direction),
	FOREIGN KEY (mista) REFERENCES ROOM(room_id),
	FOREIGN KEY (minne) REFERENCES ROOM(room_id)
);
INSERT INTO DESCRIPTION VALUES(1, "You've woken up in a big hall-like room that says 'Serenity' with big white letters on the wall. You are inside what appears to be some kind of a sleeping pod. Overall there are 5 pods in the room. 2 on your left and equally 2 on your right... There's also a computer in the room. There's a door to the east");
INSERT INTO DESCRIPTION VALUES(2, "You've entered a hallway. This is the northern part of a long hallway, but it appears to be completely dark. On your northern side there is a shimmering green light next to a door. It appears to be coming from a password terminal.");
INSERT INTO DESCRIPTION VALUES(3, "You've entered a small room with two big windows on the front. The view through the windows is phenomenal. You can see a vast, complete darkness with nothing but small bright spots of light. You're staring at a barren view of space. Under the windows there is a control panel which operates the ship. Next to the control panel is a screen that shows an error text: 'MAIN ENGINE MALFUNCTION'. Right under your right hand there is a light switch and there's a breathing mask hanging on the wall. A light on the control panel has started blinking. There's a door behind you to the south.");
INSERT INTO DESCRIPTION VALUES(4, "This is a nearly empty room. There are multiple docking piers in the room, but most of them are empty. It seems like there has been some kind of small ships attached to the piers. But all except one are gone. The remaining ship appears to be a broken escape pod. There's a door to the west and a door to the south");
INSERT INTO DESCRIPTION VALUES(5, "This is a small room. It's quite dark and dreary. there is a cabinet on the wall and it has a description on the front which says 'oxygen cabinet'. There's a door to the north and a door to the west.");
INSERT INTO DESCRIPTION VALUES(6, "You've entered a corridor. This is the middle part of a long corridor. You can hear a strong flow of oxygen, the air conditioning seems to be on. It's chilly and bright here, but there appears to be nothing of interest in here. The corridor continues to north and south and there's a door to the east.");
INSERT INTO DESCRIPTION VALUES(7, "You've entered a corridor. This is the southern part of a long corridor. You can see the back wall of the spaceship and there seems to be a hatch with a lever on the wall. The corridor splits into two directions. There are doors to the east and west.");
INSERT INTO DESCRIPTION VALUES(8, "This is a big room with a lot of space. You can see different crew belongings and there is a steel reinforced cabinet on the furthest wall. There's a door to the west and a door to the south.");
INSERT INTO DESCRIPTION VALUES(9, "You've entered the captain's quarters. A warm and cozy room with a table and some kind of a manual on it. There's also a coffee machine. There's a door to the north");
INSERT INTO DESCRIPTION VALUES(10, "You've entered a large engine room. This is the upper level of the engine room. You can smell the acrid engine oil and a smoky nuance, but the fire seems to be extinguished. There is a massive engine made of steel in the middle of the room. There are stairs that go down and a door to the east.");
INSERT INTO DESCRIPTION VALUES(11, "You've entered a large engine room. This is the lower level of the engine room. You can see useless scrap metal scattered around the room. The only object of interest is a Hyper-X 1872 placed on a table. There are stairs that go back up.");
INSERT INTO DESCRIPTION VALUES(12, "This pod seems to be closed. It has a number 1 on the cover.");
INSERT INTO DESCRIPTION VALUES(13, "This pod seems to be closed. It has a number 2 on the cover.");
INSERT INTO DESCRIPTION VALUES(14, "You woke up in this pod. It has a number 3 on the cover.");
INSERT INTO DESCRIPTION VALUES(15, "This pod seems to be closed. It has a number 4 on the cover");
INSERT INTO DESCRIPTION VALUES(16, "This pod seems to be closed. It has a number 5 on the cover.");
INSERT INTO DESCRIPTION VALUES(17, "This seems to be an ordinary computer.");
INSERT INTO DESCRIPTION VALUES(18, "This appears to be a terminal for a locked steel door.");
INSERT INTO DESCRIPTION VALUES(19, "This appears to be an ordinary light switch.");
INSERT INTO DESCRIPTION VALUES(20, "This is the USS Serenity control panel.");
INSERT INTO DESCRIPTION VALUES(21, "This seems to be a broken escape pod. The engine hood is open and there's a part that seems to be loose.");
INSERT INTO DESCRIPTION VALUES(22, "This seems to be a cabinet. It may contain something.");
INSERT INTO DESCRIPTION VALUES(23, "This is an oxygen switch.");
INSERT INTO DESCRIPTION VALUES(24, "This seems to be an ordinary cabinet.");
INSERT INTO DESCRIPTION VALUES(25, "This is seems to be an escape hatch.");
INSERT INTO DESCRIPTION VALUES(26, "It's an ordinary coffee machine.");
INSERT INTO DESCRIPTION VALUES(27, "This appears to be a broken hyperdrive engine. It's missing a part.");
INSERT INTO DESCRIPTION VALUES(28, "This is a mask that is suitable for space and perhaps other life threatening situations. It seems to be missing an oxygen source.");
INSERT INTO DESCRIPTION VALUES(29, "This is an Oxygen tank. It is attachable to a breathing mask and will work as an oxygen source.");
INSERT INTO DESCRIPTION VALUES(30, "This is a mask that has an oxygen tank as its oxygen source. It is suitable for space and perhaps other life threatening situations.");
INSERT INTO DESCRIPTION VALUES(31, "It seems to be some kind of a tool.");
INSERT INTO DESCRIPTION VALUES(32, "The Hyper-X 1872 is an electronic multipurpose tool, It can be used for multiple different tasks, such as removing and attaching parts.");
INSERT INTO DESCRIPTION VALUES(33, "This is a functioning part from the escape pod engine.");
INSERT INTO DESCRIPTION VALUES(34, "You've entered a hallway. This is the northern part of a long hallway which continues further to south. You can see doors to west, north and east.");
INSERT INTO DESCRIPTION VALUES(35, "This seems to be a broken escape pod.");
INSERT INTO DESCRIPTION VALUES(36, "The engine seems to be running.");
INSERT INTO DESCRIPTION VALUES(37, "You've entered a small room with two big windows on the front. The view through the windows is phenomenal. You can see a vast, complete darkness with nothing but small bright spots of light. You're staring at a barren view of space. Under the windows there is a control panel which operates the ship. Next to the control panel is a screen that shows an error text: 'MAIN ENGINE MALFUNCTION'. Right under your right hand there is a light switch. A light on the control panel has started blinking. There's a door behind you to the south.");
INSERT INTO DESCRIPTION VALUES(38, "You've entered the captain's quarters. A warm and cozy room with a table. There's also a coffee machine. There's a door to the north.");
INSERT INTO DESCRIPTION VALUES(39, "You've entered a large engine room. This is the lower level of the engine room. You can see useless scrap metal scattered around the room. There are stairs that go back up.");
INSERT INTO DESCRIPTION VALUES(40, "You've entered a small room with two big windows on the front. The view through the windows is phenomenal. You can see a vast, complete darkness with nothing but small bright spots of light. You're staring at a barren view of space. Under the windows there is a control panel which operates the ship. You can hear the engine humming. Right under your right hand there is a light switch. The light on the control panel is green. There's a door behind you to the south.");

INSERT INTO ROOM VALUES(1, "Cryo Room", "You are in Cryo Room.", 1, 0, 0, 0, 0);
INSERT INTO ROOM VALUES(2, "North Corridor", "You are in North Corridor.", 2, 0, 0, 0, 0);
INSERT INTO ROOM VALUES(3, "Flight Deck", "You are in Flight Deck.", 3, 1, 0, 0, 0);
INSERT INTO ROOM VALUES(4, "Escape Pod Room", "You are in Escape Pod Room.", 4, 0, 0, 1, 0);
INSERT INTO ROOM VALUES(5, "Pressure Room", "You are in Pressure Room.", 5, 0, 0, 0, 0);
INSERT INTO ROOM VALUES(6, "Middle Corridor", "You are in Middle Corridor.", 6, 0, 0, 1, 0);
INSERT INTO ROOM VALUES(7, "South Corridor", "You are in South Corridor.", 7, 0, 0, 0, 0);
INSERT INTO ROOM VALUES(8, "Crew Quarters", "You are in Crew Quarters.", 8, 0, 0, 0, 0);
INSERT INTO ROOM VALUES(9, "Captain's Quarters", "You are in Captain's Quarters", 9, 0, 0, 0, 0);
INSERT INTO ROOM VALUES(10, "Upper Engine Room", "You are in Upper Engine Room.", 10, 0, 1, 0, 0);
INSERT INTO ROOM VALUES(11, "Lower Engine Room", "You are in Lower Engine Room.", 11, 0, 1, 0, 0);

INSERT INTO PLAYER VALUES(1,1,0);

INSERT INTO OBJECT VALUES(1, "sleeping pod 1", 1, 12);
INSERT INTO OBJECT VALUES(2, "sleeping pod 2", 1, 13);
INSERT INTO OBJECT VALUES(3, "sleeping pod 3", 1, 14);
INSERT INTO OBJECT VALUES(4, "sleeping pod 4", 1, 15);
INSERT INTO OBJECT VALUES(5, "sleeping pod 5", 1, 16);
INSERT INTO OBJECT VALUES(6, "computer", 1, 17);
INSERT INTO OBJECT VALUES(7, "Flight Deck password terminal", 2, 18);
INSERT INTO OBJECT VALUES(8, "light switch", 3, 19);
INSERT INTO OBJECT VALUES(9, "Spaceship control panel", 3, 20);
INSERT INTO OBJECT VALUES(10, "escape pod", 4, 21);
INSERT INTO OBJECT VALUES(11, "oxygen cabinet", 5, 22);
INSERT INTO OBJECT VALUES(12, "oxygen switch", NULL, 23);
INSERT INTO OBJECT VALUES(13, "steel reinforced cabinet", 8, 24);
INSERT INTO OBJECT VALUES(14, "escape hatch", 7, 25);
INSERT INTO OBJECT VALUES(15, "coffee machine", 9, 26);
INSERT INTO OBJECT VALUES(16, "hyperdrive engine", 10, 27);

INSERT INTO ITEM VALUES (1, "shotgun", NULL, NULL, NULL, 1);
INSERT INTO ITEM VALUES (2, "breathing mask", NULL, 3, NULL, 28);
INSERT INTO ITEM VALUES (3, "oxygen tank", NULL, NULL, NULL, 29);
INSERT INTO ITEM VALUES (4, "breathing mask with oxygen tank", NULL, NULL, NULL, 30);
INSERT INTO ITEM VALUES	(5, "engine part", NULL, NULL, NULL, 33);
INSERT INTO ITEM VALUES (6, "Hyper-X 1872", NULL, 11, NULL, 31);
INSERT INTO ITEM VALUES (7, "Hyper-X manual", NULL, 9, NULL, 32);

INSERT INTO MOVEMENT VALUES(1,2,"east"); 
INSERT INTO MOVEMENT VALUES(2,1,"west");
INSERT INTO MOVEMENT VALUES(2,3,"north");
INSERT INTO MOVEMENT VALUES(3,2,"south");
INSERT INTO MOVEMENT VALUES(2,4,"east");
INSERT INTO MOVEMENT VALUES(4,2,"west");
INSERT INTO MOVEMENT VALUES(4,5,"south");
INSERT INTO MOVEMENT VALUES(5,4,"north");
INSERT INTO MOVEMENT VALUES(5,6,"west");
INSERT INTO MOVEMENT VALUES(6,5,"east");
INSERT INTO MOVEMENT VALUES(6,2,"north");
INSERT INTO MOVEMENT VALUES(2,6,"south");
INSERT INTO MOVEMENT VALUES(6,7,"south");
INSERT INTO MOVEMENT VALUES(7,6,"north");
INSERT INTO MOVEMENT VALUES(7,8,"east");
INSERT INTO MOVEMENT VALUES(8,7,"west");
INSERT INTO MOVEMENT VALUES(8,9,"south");
INSERT INTO MOVEMENT VALUES(9,8,"north");
INSERT INTO MOVEMENT VALUES(7,10,"west");
INSERT INTO MOVEMENT VALUES(10,7,"east");
INSERT INTO MOVEMENT VALUES(10,11,"down");
INSERT INTO MOVEMENT VALUES(11,10,"up");