from bibtexparser.bibdatabase import BibDatabase
from bibtexparser.bwriter import BibTexWriter

class Citation:
    def __init__(self, id, type, author, title, year, booktitle=None, journal=None, volume=None, pages=None, publisher=None):
        self.id = id
        self.type = type
        self.author = author
        self.title = title
        self.year = year
        self.booktitle = booktitle
        self.journal = journal
        self.volume = volume
        self.pages = pages
        self.publisher = publisher
        self.as_bibtex = self.to_bibtex()

    def __str__(self):
        details = [
            f"ID: {self.id}",
            f"Type: {self.type}",
            f"Author: {self.author}",
            f"Title: {self.title}",
            f"Year: {self.year}",
        ]
        if self.booktitle:
            details.append(f"Booktitle: {self.booktitle}")
        if self.journal:
            details.append(f"Journal: {self.journal}")
        if self.volume:
            details.append(f"Volume: {self.volume}")
        if self.pages:
            details.append(f"Pages: {self.pages}")
        if self.publisher:
            details.append(f"Publisher: {self.publisher}")
        return "\n".join(details)
    
    def to_bibtex(self):
        db = BibDatabase()
        entry = {
            "ID": str(self.id),
            "ENTRYTYPE": self.type,
            "author": self.author,
            "title": self.title,
            "year": str(self.year),
        }
        if self.booktitle:
            entry["booktitle"] = self.booktitle
        if self.journal:
            entry["journal"] = self.journal
        if self.volume:
            entry["volume"] = self.volume
        if self.pages:
            entry["pages"] = self.pages
        if self.publisher:
            entry["publisher"] = self.publisher
        
        db.entries = [entry]
        writer = BibTexWriter()
        return writer.write(db)