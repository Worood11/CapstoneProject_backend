\c capstone_projectdb;

DROP TABLE IF EXISTS bookstores CASCADE;

CREATE TABLE bookstores (
    id SERIAL PRIMARY KEY,
    name_en TEXT NOT NULL,
    name_ar TEXT NOT NULL,
    city_en TEXT NOT NULL,
    city_ar TEXT NOT NULL,
    description_en TEXT,
    description_ar TEXT,
    map_url TEXT,
    image TEXT
);

INSERT INTO bookstores (name_en, name_ar, city_en, city_ar,description_en, description_ar, map_url, image)
/*Riyadh*/
VALUES
(),