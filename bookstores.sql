\c capstone_projectdb;

DROP TABLE IF EXISTS bookstores CASCADE;

CREATE TABLE bookstores (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    city TEXT NOT NULL,
    description TEXT,
    map_url TEXT,
    image TEXT
);

INSERT INTO bookstores (name, city,description, map_url, image)
/*Riyadh*/
VALUES
('Salwa Bookstore' , 'Riyadh' , 'Our Bookstore is rich with new and used books.', 'https://maps.app.goo.gl/JJZMBD5dvmtk5nRu7' , 'https://www.shutterstock.com/image-vector/bookstore-front-vector-illustration-banner-600nw-551405635.jpg' ),
('BookClub', 'Riyadh', 'Start your journey with us, through thousands of diverse books in various fields, suitable for all age groups.', 'https://maps.app.goo.gl/YqSR1wkFFtHwenpj8', 'https://www.shutterstock.com/image-vector/bookstore-front-vector-illustration-banner-600nw-551405635.jpg'),
('Sophia Bookstore', 'Riyadh', 'Sophia Library has adopted "Have the Courage to Learn" as its motto, believing that knowledge in all its forms helps individuals reach their desired destination.' , 'https://share.google/j7GXXmWMKUoeWQKKS', 'https://www.shutterstock.com/image-vector/bookstore-front-vector-illustration-banner-600nw-551405635.jpg'),
('Deffastore' , 'Riyadh' , 'Daffa Library: An integrated knowledge community that seeks to add an enriching dimension to the bookselling process.', 'https://share.google/pgzNCxT1KyBcglBHO', 'https://www.shutterstock.com/image-vector/bookstore-front-vector-illustration-banner-600nw-551405635.jpg'),
('Tashkeel' , 'Riyadh', 'Tashkeel Arabic Bookstore, your gateway to reading and knowledge, featuring the latest books from around the world in one place.', 'https://share.google/0FJ2m0MkhUIwPsI3g', 'https://www.shutterstock.com/image-vector/bookstore-front-vector-illustration-banner-600nw-551405635.jpg'),
('Heritage Bookstore', 'Riyadh', 'A bookstore in Riyadh specializing in selling books, both new and used, offering a wide variety of publications in various fields.', 'https://share.google/gYYsF2nH6NmjZsXlY' , 'https://www.shutterstock.com/image-vector/bookstore-front-vector-illustration-banner-600nw-551405635.jpg'),
('almohadith bookstore', 'Riyadh' , 'A specialized bookstore offering a wide selection of Islamic books, scholarly references, and authentic religious works for readers and researchers alike.' , 'https://share.google/sxdhQG21iAVwU0h5d', 'https://www.shutterstock.com/image-vector/bookstore-front-vector-illustration-banner-600nw-551405635.jpg'),
('Kunozalkhizanah' , 'Riyadh', 'Specializing in selling used religious and cultural books and novels. We buy used books and private libraries.', 'https://share.google/YYcGPRXiO2mVIPWIf', 'https://www.shutterstock.com/image-vector/bookstore-front-vector-illustration-banner-600nw-551405635.jpg'),


