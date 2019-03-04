import csv

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine(
    'postgres://dvzeebgbtgejnj:8fd31663266b81198d9b6eed848c39a1100adb5982afc1306c4ea34b290d6a0f@ec2-54-163-234-88.compute-1.amazonaws.com:5432/d9uk68nilkcqn4')
db = scoped_session(sessionmaker(bind=engine))


def main():
    f = open("books.csv", "r")  # needs to be opened during reading csv
    reader = csv.reader(f)
    next(reader)
    for isbn, title, author, year in reader:
        db.execute("INSERT INTO books (isbn, title, author, year) VALUES (:isbn, :title, :author, :year)",
                   {"isbn": isbn, "title": title, "author": author, "year": year})
        db.commit()
        print(
            f"Added book with ISBN: {isbn} Title: {title}  Author: {author}  Year: {year}")


if __name__ == '__main__':
    main()
