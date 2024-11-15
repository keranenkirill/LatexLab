-- Päätaulu, jossa kaikkia lainauksia koskevat yhteiset tiedot
CREATE TABLE citation (
	id SERIAL PRIMARY KEY,
	author VARCHAR(255) NOT NULL,
	title VARCHAR(255) NOT NULL,
	year INTEGER NOT NULL
);

-- article-tyyppisten lainauksien lisätietoja koskeva taulu
CREATE TABLE article (
	id INTEGER PRIMARY KEY REFERENCES citation(id) ON DELETE CASCADE,
	journal VARCHAR(255) NOT NULL,
	volume INTEGER,
	pages VARCHAR(50)
);

-- book-tyyppisten lainauksien lisätietoja koskeva taulu
CREATE TABLE book (
	id INTEGER PRIMARY KEY REFERENCES citation(id) ON DELETE CASCADE,
	publisher VARCHAR(255)
);

-- inproceedings-tyyppisten lainauksien lisätietoja koskeva taulu
CREATE TABLE inproceedings (
	id INTEGER PRIMARY KEY REFERENCES citation(id) ON DELETE CASCADE,
	booktitle VARCHAR(255) NOT NULL
);
