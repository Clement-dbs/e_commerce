CREATE TABLE IF NOT EXISTS categories (
    id_category INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name VARCHAR(20) NOT NULL UNIQUE,
    description TEXT
);

CREATE TABLE IF NOT EXISTS products (
    id_product INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    stock_disponibility INT NOT NULL,
    id_category INT,
    FOREIGN KEY (id_category) REFERENCES categories(id_category) ON DELETE SET NULL
);


CREATE TABLE IF NOT EXISTS customers (
    id_customer INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    first_name VARCHAR(30) NOT NULL,
    last_name VARCHAR(30) NOT NULL,
    email VARCHAR(50) NOT NULL UNIQUE,
    date_of_account_creation TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);


DO $$
BEGIN
   IF NOT EXISTS (SELECT 1 FROM pg_type WHERE typname = 'order_status') THEN
      CREATE TYPE order_status AS ENUM ('PENDING', 'PAID', 'SHIPPED', 'CANCELLED');
   END IF;
END
$$;

CREATE TABLE IF NOT EXISTS orders (
    id_order INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    id_customer INT,
    order_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    status order_status NOT NULL,
    FOREIGN KEY (id_customer) REFERENCES customers(id_customer) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS order_items(
    id_order_items INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    id_order INT NOT NULL,
    id_product INT NOT NULL,
    quantity INT NOT NULL,
    unit_price FLOAT NOT NULL,
    FOREIGN KEY (id_product) REFERENCES products(id_product) ON DELETE SET NULL,
    FOREIGN KEY (id_order) REFERENCES orders(id_order) ON DELETE SET NULL
);

INSERT INTO categories(name, description)  VALUES
  ('Électronique',       'Produits high-tech et accessoires'),
  ('Maison & Cuisine',   'Électroménager et ustensiles'),
  ('Sport & Loisirs',    'Articles de sport et plein air'),
  ('Beauté & Santé',     'Produits de beauté, hygiène, bien-être'),
  ('Jeux & Jouets',      'Jouets pour enfants et adultes');

INSERT INTO products(name, price, stock_disponibility, id_category) VALUES
  ('Casque Bluetooth X1000',        79.99,  4,  (select id_category from categories where name = 'Électronique')),
  ('Souris Gamer Pro RGB',          49.90, 120,  (select id_category from categories where name ='Électronique')),
  ('Bouilloire Inox 1.7L',          29.99,  80,  (select id_category from categories where name ='Maison & Cuisine')),
  ('Aspirateur Cyclonix 3000',     129.00,  40,  (select id_category from categories where name ='Maison & Cuisine')),
  ('Tapis de Yoga Comfort+',        19.99, 150,  (select id_category from categories where name ='Sport & Loisirs')),
  ('Haltères 5kg (paire)',          24.99,  70,  (select id_category from categories where name ='Sport & Loisirs')),
  ('Crème hydratante BioSkin',      15.90, 200,  (select id_category from categories where name ='Beauté & Santé')),
  ('Gel douche FreshEnergy',         4.99, 300,  (select id_category from categories where name ='Beauté & Santé')),
  ('Puzzle 1000 pièces "Montagne"', 12.99,  95,  (select id_category from categories where name ='Jeux & Jouets')),
  ('Jeu de société "Galaxy Quest"', 29.90,  60,  (select id_category from categories where name ='Jeux & Jouets'));
  

INSERT INTO customers(first_name, last_name, email, date_of_account_creation) VALUES
  ('Alice',  'Martin',    'alice.martin@mail.com',    '2024-01-10 14:32'),
  ('Bob',    'Dupont',    'bob.dupont@mail.com',      '2024-02-05 09:10'),
  ('Chloé',  'Bernard',   'chloe.bernard@mail.com',   '2024-03-12 17:22'),
  ('David',  'Robert',    'david.robert@mail.com',    '2024-01-29 11:45'),
  ('Emma',   'Leroy',     'emma.leroy@mail.com',      '2024-03-02 08:55'),
  ('Félix',  'Petit',     'felix.petit@mail.com',     '2024-02-18 16:40'),
  ('Hugo',   'Roussel',   'hugo.roussel@mail.com',    '2024-03-20 19:05'),
  ('Inès',   'Moreau',    'ines.moreau@mail.com',     '2024-01-17 10:15'),
  ('Julien', 'Fontaine',  'julien.fontaine@mail.com', '2024-01-23 13:55'),
  ('Katia',  'Garnier',   'katia.garnier@mail.com',   '2024-03-15 12:00');

INSERT INTO orders (id_customer, order_date, status) VALUES
  ((select id_customer from customers where email = 'alice.martin@mail.com'),    '2024-03-01 10:20', 'PAID'),
  ((select id_customer from customers where email = 'bob.dupont@mail.com'),      '2024-03-04 09:12', 'SHIPPED'),
  ((select id_customer from customers where email = 'alice.martin@mail.com'),   '2024-03-08 15:02', 'PAID'),
  ((select id_customer from customers where email = 'david.robert@mail.com'),    '2024-03-09 11:45', 'CANCELLED'),
  ((select id_customer from customers where email = 'emma.leroy@mail.com'),      '2024-03-10 08:10', 'PAID'),
  ((select id_customer from customers where email = 'felix.petit@mail.com'),     '2024-03-11 13:50', 'PENDING'),
  ((select id_customer from customers where email = 'hugo.roussel@mail.com'),    '2024-03-15 19:30', 'SHIPPED'),
  ((select id_customer from customers where email = 'ines.moreau@mail.com'),     '2024-03-16 10:00', 'PAID'),
  ((select id_customer from customers where email = 'julien.fontaine@mail.com'), '2024-03-18 14:22', 'PAID'),
  ((select id_customer from customers where email = 'katia.garnier@mail.com'),   '2024-03-20 18:00', 'PENDING');

INSERT INTO order_items(id_order, id_product, quantity, unit_price) VALUES
 ((SELECT o.id_order FROM customers c JOIN orders o ON o.id_customer = c.id_customer WHERE c.email = 'alice.martin@mail.com' AND o.order_date = '2024-03-01 10:20:00'), (SELECT id_product FROM products WHERE name = 'Casque Bluetooth X1000'), 1, 79.99),
 ((SELECT o.id_order FROM customers c JOIN orders o ON o.id_customer = c.id_customer WHERE c.email = 'alice.martin@mail.com' AND o.order_date = '2024-03-01 10:20:00'), (SELECT id_product FROM products WHERE name = 'Puzzle 1000 pièces "Montagne"'), 2, 12.99),
 ((SELECT o.id_order FROM customers c JOIN orders o ON o.id_customer = c.id_customer WHERE c.email = 'bob.dupont@mail.com' AND o.order_date = '2024-03-04 09:12:00'), (SELECT id_product FROM products WHERE name = 'Tapis de Yoga Comfort+' ), 1, 19.99),
 ((SELECT o.id_order FROM customers c JOIN orders o ON o.id_customer = c.id_customer WHERE c.email = 'david.robert@mail.com' AND o.order_date = '2024-03-09 11:45:00'), (SELECT id_product FROM products WHERE name = 'Haltères 5kg (paire)' ), 1, 24.99),
 ((SELECT o.id_order FROM customers c JOIN orders o ON o.id_customer = c.id_customer WHERE c.email = 'emma.leroy@mail.com' AND o.order_date = '2024-03-10 08:10:00'), (SELECT id_product FROM products WHERE name = 'Crème hydratante BioSkin' ), 2, 15.90),
 ((SELECT o.id_order FROM customers c JOIN orders o ON o.id_customer = c.id_customer WHERE c.email = 'julien.fontaine@mail.com' AND o.order_date = '2024-03-18 14:22:00'), (SELECT id_product FROM products WHERE name = 'Jeu de société "Galaxy Quest"' ), 1, 29.90),
 ((SELECT o.id_order FROM customers c JOIN orders o ON o.id_customer = c.id_customer WHERE c.email = 'katia.garnier@mail.com' AND o.order_date = '2024-03-20 18:00:00'), (SELECT id_product FROM products WHERE name = 'Souris Gamer Pro RGB' ), 1, 49.90),
 ((SELECT o.id_order FROM customers c JOIN orders o ON o.id_customer = c.id_customer WHERE c.email = 'katia.garnier@mail.com' AND o.order_date = '2024-03-20 18:00:00'), (SELECT id_product FROM products WHERE name = 'Gel douche FreshEnergy' ), 2, 4.99);
