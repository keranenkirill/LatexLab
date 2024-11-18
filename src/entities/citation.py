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