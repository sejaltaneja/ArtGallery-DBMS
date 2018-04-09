import sqlite3

conn=sqlite3.connect("ArtGallery.db")

conn.execute("DROP TABLE IF EXISTS Artist")
conn.execute("DROP TABLE IF EXISTS Customer")
conn.execute("DROP TABLE IF EXISTS ArtWork")
conn.execute("DROP TABLE IF EXISTS Purchase")

conn.execute("Create table Artist (AName varchar(25) PRIMARY KEY,  Age int, Birthplace varchar(15), Style varchar(15));")
conn.execute("Create table ArtWork (Title varchar(25) PRIMARY KEY, AName varchar(25), Year int, Type varchar(15), Price real);")
conn.execute("Create table Customer (CName varchar(25) PRIMARY KEY, Address varchar(40) DEFAULT None, Pno int DEFAULT None, Amount real DEFAULT 0 );")
conn.execute("Create table Purchase (Cname varchar(25), Title varchar(25), Price real, Date varchar(10));")

