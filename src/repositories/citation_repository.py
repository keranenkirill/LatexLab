from config import db
from sqlalchemy import text

def create_citation(citation: dict):
    sql = text("""
        INSERT INTO citations (type, author, title, year, booktitle, journal, volume, pages, publisher)
        VALUES (:type, :author, :title, :year, :booktitle, :journal, :volume, :pages, :publisher)
    """)
    db.session.execute(sql, {
        "type": citation['type'],
        "author": citation['author'],
        "title": citation['title'],
        "year": citation['year'],
        "booktitle": citation.get('booktitle', None),
        "journal": citation.get('journal', None),
        "volume": citation.get('volume', None),
        "pages": citation.get('pages', None),
        "publisher": citation.get('publisher', None)
    })
    db.session.commit()

