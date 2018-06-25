# Tietokantataulut


```
CREATE TABLE account (
	id INTEGER NOT NULL,
	date_created DATETIME,
	date_modified DATETIME,
	name VARCHAR(144) NOT NULL,
	username VARCHAR(144) NOT NULL,
	password VARCHAR(144) NOT NULL,
	PRIMARY KEY (id)
);
CREATE TABLE kategoria (
	id INTEGER NOT NULL,
	date_created DATETIME,
	date_modified DATETIME,
	name VARCHAR(144) NOT NULL,
	account_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(account_id) REFERENCES account (id)
);
CREATE TABLE tehtava (
	id INTEGER NOT NULL,
	date_created DATETIME,
	date_modified DATETIME,
	name VARCHAR(144) NOT NULL,
	done BOOLEAN NOT NULL,
	importance INTEGER NOT NULL,
	account_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	CHECK (done IN (0, 1)),
	FOREIGN KEY(account_id) REFERENCES account (id)
);
CREATE TABLE task_category (
	tehtava_id INTEGER,
	kategoria_id INTEGER,
	FOREIGN KEY(tehtava_id) REFERENCES tehtava (id) ON DELETE CASCADE,
	FOREIGN KEY(kategoria_id) REFERENCES kategoria (id) ON DELETE CASCADE
);
´´´
