from sqlalchemy import text
from config import db

from entities.citation import Citation


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


def del_citation(citation_id: int):
    sql = text("DELETE FROM citations WHERE id = :id")
    db.session.execute(sql, {"id": citation_id})
    db.session.commit()


def get_all_citations():
    result = db.session.execute(text(
        """SELECT id, type, author, title, year, booktitle, journal, volume, pages, publisher 
        FROM citations"""))
    citations = result.fetchall()

    return [
        Citation(
            citation[0],   # id
            citation[1],   # type
            citation[2],   # author
            citation[3],   # title
            citation[4],   # year
            citation[5],   # booktitle
            citation[6],   # journal
            citation[7],   # volume
            citation[8],   # pages
            citation[9]    # publisher
        )
        for citation in citations
    ]


def get_citation(citation_id):
    result = db.session.execute(text(
        """SELECT id, type, author, title, year, booktitle, journal, volume, pages, publisher 
        FROM citations WHERE id = :id"""), {'id': citation_id})
    citation = result.fetchone()
    return Citation(
        citation.id,       # id
        citation.type,     # type
        citation.author,   # author
        citation.title,    # title
        citation.year,     # year
        citation.booktitle,# booktitle
        citation.journal,  # journal
        citation.volume,   # volume
        citation.pages,    # pages
        citation.publisher # publisher
    )

def update_citation(citation_id: int, citation: dict):

    sql = text("""
    UPDATE  citations
    SET     type = :type,
        author = :author,
        title = :title,
        year = :year,
        booktitle = :booktitle,
        journal = :journal,
        volume = :volume,
        pages = :pages,
        publisher = :publisher
    WHERE   id = :id
    """)

    db.session.execute(sql, {
        "type": citation["type"],
        "author": citation["author"],
        "title": citation["title"],
        "year": citation["year"],
        "booktitle": citation.get("booktitle", None),
        "journal": citation.get("journal", None),
        "volume": citation.get("volume", None),
        "pages": citation.get("pages", None),
        "publisher": citation.get("publisher", None),
        "id": citation_id
    })
    db.session.commit()
