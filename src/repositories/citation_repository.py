from config import db
from sqlalchemy import text

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


def get_citations():
    result = db.session.execute(text(
        "SELECT id, type, author, title, year, booktitle, journal, volume, pages, publisher FROM citations"))
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

def update_citation(citation_id: int, new_info: dict):



    fields = """
    id,
    type,
    author,
    title,
    year,
    booktitle,
    journal,
    volume,
    pages,
    publisher
    """.splitlines()

    sql = """
    SELECT  {fields[0]},
            {fields[1]},
            {fields[2]},
            {fields[3]},
            {fields[4]},
            {fields[5]},
            {fields[6]},
            {fields[7]},
            {fields[8]}
    FROM    citations
    WHERE   id = :id
    """

    old_info = db.session.execute(text(sql)).fetchall()

    new_fields = []

    for i in range(10):
        if new_info[i] == "":
            new_fields[0] = 1
