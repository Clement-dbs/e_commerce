## 📘 TP complet – PostgreSQL : Analyse des ventes d’un site e-commerce

**Niveau :** Intermédiaire
**Rôle cible :** Data Analyst

---

# 1️⃣ Contexte

Vous travaillez pour une entreprise fictive de e-commerce :

**SuperShop Analytics**

La direction souhaite analyser :

* les ventes par produit et par catégorie,
* le comportement des clients,
* le chiffre d’affaires par période,
* les produits et clients “top” ou “en difficulté”.

Votre mission :

1. Concevoir le **schéma relationnel** de la base.
2. Créer les tables dans PostgreSQL.
3. Insérer un jeu de données fourni (valeurs déjà écrites en SQL, `INSERT` à compléter).
4. Écrire des requêtes SQL d’analyse : jointures, sous-requêtes, agrégats, logique conditionnelle.

---

# 2️⃣ Modèle métier – Tables à concevoir (sans schéma imposé)

Vous devez **déduire vous-mêmes** :

* noms de colonnes,
* types SQL,
* contraintes (NOT NULL, UNIQUE, CHECK, FOREIGN KEY…),
* clés primaires et étrangères.

> Pour chaque table, il sera pertinent de prévoir **une colonne identifiant unique** (clé primaire auto-incrémentée ou autre).

---

## 2.1. Catégories de produits (`categories`)

Chaque produit appartient à une **catégorie**.

Pour chaque catégorie, on souhaite stocker :

* un **nom de catégorie**

  * texte relativement court
  * obligatoire
  * deux catégories ne doivent pas avoir le même nom

* une **description**

  * texte plus long
  * facultatif

À vous de définir :

* la colonne d’identifiant,
* les types SQL,
* les contraintes (NOT NULL, UNIQUE…).

---

## 2.2. Produits (`products`)

Les produits sont les articles vendus sur le site.

On souhaite stocker au minimum :

* un **nom de produit**

  * texte court
  * obligatoire

* un **prix**

  * numérique
  * strictement positif

* un **stock disponible**

  * entier
  * ≥ 0

* une **catégorie d’appartenance**

  * clé étrangère vers la table des catégories

À vous de définir :

* la colonne d’identifiant,
* les types,
* les contraintes (CHECK pour prix/stock, FK, etc.).

---

## 2.3. Clients (`customers`)

Les clients sont les utilisateurs qui passent des commandes.

Pour chaque client, on conserve :

* un **prénom**

* un **nom**

  * tous deux obligatoires

* une **adresse e-mail**

  * obligatoire
  * unique

* une **date/heure de création de compte**

  * obligatoire

À vous de définir :

* la clé primaire,
* les types,
* les contraintes (UNIQUE sur l’email, NOT NULL, etc.).

---

## 2.4. Commandes (`orders`)

Les commandes représentent les achats effectués par les clients.

Pour chaque commande, on conserve :

* le **client** qui a passé la commande

  * clé étrangère vers `customers`

* la **date/heure de commande**

  * obligatoire

* le **statut de la commande** 


  * texte court
  * valeurs possibles limitées à :

    * `PENDING`
    * `PAID`
    * `SHIPPED`
    * `CANCELLED`
  * obligatoire
  * doit respecter cette liste strictement 
  # AJOUT -> Création un type **orders**
  

À vous de définir :

* la clé primaire,
* la clé étrangère vers `customers`,
* la contrainte de validation du statut.

---

## 2.5. Lignes de commande (`order_items`)

Chaque commande contient une ou plusieurs lignes.

Pour chaque ligne :

* la **commande** concernée

  * clé étrangère vers `orders`

* le **produit** concerné

  * clé étrangère vers `products`

* la **quantité**

  * entière
  * strictement positive

* le **prix unitaire facturé**

  * numérique
  * strictement positif
  * peut être différent du prix actuel du produit (promo, remise, etc.)

À vous de définir :

* la clé primaire de la ligne,
* les FKs,
* les contraintes (CHECK, NOT NULL…).

---

# 3️⃣ Partie 1 – Création du schéma SQL

**Objectif :** traduire le modèle métier en SQL.

Travail demandé :

1. Concevoir au brouillon votre schéma relationnel (tables, colonnes, PK, FK…).
2. Écrire un script SQL `schema.sql` pour :

   * (facultatif selon le contexte) créer la base,
   * créer les tables `categories`, `products`, `customers`, `orders`, `order_items` avec :

     * PRIMARY KEY,
     * FOREIGN KEY,
     * NOT NULL,
     * UNIQUE,
     * CHECK (prix > 0, stock ≥ 0, quantité > 0, etc.).

---

# 4️⃣ Partie 2 – Jeu de données fourni (fichier `.sql` à compléter)

Le jeu de données ci-dessous est fourni **en SQL**, mais les instructions `INSERT INTO` sont **à compléter par vous**.

* Les **colonnes d’ID ne sont volontairement pas mentionnées** : elles doivent être gérées automatiquement par la base (SERIAL, IDENTITY, …).
* Vous devez compléter **le nom de la table** et **la liste des colonnes métiers** dans la partie `INSERT INTO … ( ... )`.
* Vous **ne réécrivez pas les valeurs** : elles sont déjà prêtes.

**Fichier conseillé :** `data.sql`

```sql
-- ===========================================
--  DONNÉES : CATEGORIES
--  Objectif : insérer les catégories de produits
--  TODO : compléter le nom de la table et la liste des colonnes (hors colonne d'identifiant)
-- Exemple attendu :
--   INSERT INTO categories (name, description) VALUES ...
-- ===========================================

INSERT INTO /* TODO: nom_de_table_et_colonnes_ex: categories(name, description) */ VALUES
  ('Électronique',       'Produits high-tech et accessoires'),
  ('Maison & Cuisine',   'Électroménager et ustensiles'),
  ('Sport & Loisirs',    'Articles de sport et plein air'),
  ('Beauté & Santé',     'Produits de beauté, hygiène, bien-être'),
  ('Jeux & Jouets',      'Jouets pour enfants et adultes');



-- ===========================================
--  DONNÉES : PRODUITS
--  Objectif : insérer les produits
--  Colonnes métiers attendues (à déduire) :
--    - nom du produit
--    - prix
--    - stock
--    - catégorie (clé étrangère vers la table des catégories)
--  TODO : compléter le INSERT INTO avec le nom de la table et la liste des colonnes (hors ID)
-- ===========================================

INSERT INTO /* TODO: ex: products(name, price, stock, category_id) */ VALUES
  ('Casque Bluetooth X1000',        79.99,  50,  'Électronique'),
  ('Souris Gamer Pro RGB',          49.90, 120,  'Électronique'),
  ('Bouilloire Inox 1.7L',          29.99,  80,  'Maison & Cuisine'),
  ('Aspirateur Cyclonix 3000',     129.00,  40,  'Maison & Cuisine'),
  ('Tapis de Yoga Comfort+',        19.99, 150,  'Sport & Loisirs'),
  ('Haltères 5kg (paire)',          24.99,  70,  'Sport & Loisirs'),
  ('Crème hydratante BioSkin',      15.90, 200,  'Beauté & Santé'),
  ('Gel douche FreshEnergy',         4.99, 300,  'Beauté & Santé'),
  ('Puzzle 1000 pièces "Montagne"', 12.99,  95,  'Jeux & Jouets'),
  ('Jeu de société "Galaxy Quest"', 29.90,  60,  'Jeux & Jouets');



-- ===========================================
--  DONNÉES : CLIENTS
--  Objectif : insérer les clients
--  Colonnes métiers attendues (à déduire) :
--    - prénom
--    - nom
--    - email
--    - date/heure de création du compte
--  TODO : compléter le INSERT INTO avec le nom de la table et les colonnes (hors ID)
-- ===========================================

INSERT INTO /* TODO: ex: customers(firstname, lastname, email, created_at) */ VALUES
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



-- ===========================================
--  DONNÉES : COMMANDES
--  Objectif : insérer les commandes
--  Colonnes métiers attendues (à déduire) :
--    - client (référence vers la table des clients)
--    - date/heure de la commande
--    - statut (PENDING, PAID, SHIPPED, CANCELLED)
--  Remarque : le client est identifié ici par son email,
--             à vous d'utiliser cet email pour retrouver l'ID du client si nécessaire.
--  TODO : ajuster les colonnes du INSERT INTO selon votre modèle
-- ===========================================

INSERT INTO /* TODO: ex: orders(customer_id, order_date, status) */ VALUES
  ('alice.martin@mail.com',    '2024-03-01 10:20', 'PAID'),
  ('bob.dupont@mail.com',      '2024-03-04 09:12', 'SHIPPED'),
  ('chloe.bernard@mail.com',   '2024-03-08 15:02', 'PAID'),
  ('david.robert@mail.com',    '2024-03-09 11:45', 'CANCELLED'),
  ('emma.leroy@mail.com',      '2024-03-10 08:10', 'PAID'),
  ('felix.petit@mail.com',     '2024-03-11 13:50', 'PENDING'),
  ('hugo.roussel@mail.com',    '2024-03-15 19:30', 'SHIPPED'),
  ('ines.moreau@mail.com',     '2024-03-16 10:00', 'PAID'),
  ('julien.fontaine@mail.com', '2024-03-18 14:22', 'PAID'),
  ('katia.garnier@mail.com',   '2024-03-20 18:00', 'PENDING');



-- ===========================================
--  DONNÉES : LIGNES DE COMMANDE (ORDER_ITEMS)
--  Objectif : insérer le détail des commandes
--  Colonnes métiers attendues (à déduire) :
--    - référence à la commande
--    - référence au produit
--    - quantité
--    - prix unitaire facturé
--  Remarque :
--    - Ici les commandes et produits sont identifiés par email + date et nom de produit.
--      À vous d'écrire les requêtes nécessaires ou d'adapter les insertions
--      pour référencer les bons IDs (order_id, product_id) selon votre modèle.
-- ===========================================

INSERT INTO /* TODO: ex: order_items(order_id, product_id, quantity, unit_price) */ VALUES
  ('alice.martin@mail.com',    '2024-03-01 10:20', 'Casque Bluetooth X1000',         1,  79.99),
  ('alice.martin@mail.com',    '2024-03-01 10:20', 'Puzzle 1000 pièces "Montagne"', 2,  12.99),
  ('bob.dupont@mail.com',      '2024-03-04 09:12', 'Tapis de Yoga Comfort+',        1,  19.99),
  ('chloe.bernard@mail.com',   '2024-03-08 15:02', 'Bouilloire Inox 1.7L',          1,  29.99),
  ('chloe.bernard@mail.com',   '2024-03-08 15:02', 'Gel douche FreshEnergy',        3,   4.99),
  ('david.robert@mail.com',    '2024-03-09 11:45', 'Haltères 5kg (paire)',          1,  24.99),
  ('emma.leroy@mail.com',      '2024-03-10 08:10', 'Crème hydratante BioSkin',      2,  15.90),
  ('julien.fontaine@mail.com', '2024-03-18 14:22', 'Jeu de société "Galaxy Quest"', 1,  29.90),
  ('katia.garnier@mail.com',   '2024-03-20 18:00', 'Souris Gamer Pro RGB',          1,  49.90),
  ('katia.garnier@mail.com',   '2024-03-20 18:00', 'Gel douche FreshEnergy',        2,   4.99);
```


---

# 5️⃣ Partie 3 – Requêtes SQL de base

1. Lister tous les clients triés par date de création de compte (plus anciens → plus récents).
    SELECT * FROM customers ORDER BY date_of_account_creation ASC

2. Lister tous les produits (nom + prix) triés par prix décroissant.
    SELECT name, price FROM products ORDER BY price DESC

3. Lister les commandes passées entre deux dates (par exemple entre le 1er et le 15 mars 2024).
    SELECT * FROM orders WHERE order_date BETWEEN '2024-03-01 00:00:00' AND '2024-03-15 00:00:00'
    
4. Lister les produits dont le prix est strictement supérieur à 50 €.
    SELECT * FROM products WHERE price > 50

5. Lister tous les produits d’une catégorie donnée (par exemple “Électronique”).
    SELECT * FROM products WHERE (SELECT name FROM categorie WHERE name = "Électronique")

---

# 6️⃣ Partie 4 – Jointures simples

1. Lister tous les produits avec le nom de leur catégorie.
2. Lister toutes les commandes avec le nom complet du client (prénom + nom).
3. Lister toutes les lignes de commande avec :

   * le nom du client,
   * le nom du produit,
   * la quantité,
   * le prix unitaire facturé.
4. Lister toutes les commandes dont le statut est `PAID` ou `SHIPPED`.

---

# 7️⃣ Partie 5 – Jointures avancées

1. Afficher le détail complet de chaque commande avec :

   * date de commande,
   * nom du client,
   * liste des produits,
   * quantité,
   * prix unitaire facturé,
   * montant total de la ligne (quantité × prix unitaire).

2. Calculer le **montant total de chaque commande** et afficher uniquement :

   * l’ID de la commande,
   * le nom du client,
   * le montant total de la commande.

3. Afficher les commandes dont le montant total **dépasse 100 €**.

4. Lister les catégories avec leur **chiffre d’affaires total** (somme du montant des lignes sur tous les produits de cette catégorie).

---

# 8️⃣ Partie 6 – Sous-requêtes

1. Lister les produits qui ont été vendus **au moins une fois**.
2. Lister les produits qui **n’ont jamais été vendus**.
3. Trouver le client qui a **dépensé le plus** (TOP 1 en chiffre d’affaires cumulé).
4. Afficher les **3 produits les plus vendus** en termes de quantité totale.
5. Lister les commandes dont le montant total est **strictement supérieur à la moyenne** de toutes les commandes.

---

# 9️⃣ Partie 7 – Statistiques & agrégats

1. Calculer le **chiffre d’affaires total** (toutes commandes confondues, hors commandes annulées si souhaité).
2. Calculer le **panier moyen** (montant moyen par commande).
3. Calculer la **quantité totale vendue par catégorie**.
4. Calculer le **chiffre d’affaires par mois** (au moins sur les données fournies).
5. Formater les montants pour n’afficher que **deux décimales**.

---

# 🔟 Partie 8 – Logique conditionnelle (CASE)

1. Pour chaque commande, afficher :

   * l’ID de la commande,
   * le client,
   * la date,
   * le statut,
   * une version “lisible” du statut en français via `CASE` :

     * `PAID` → “Payée”
     * `SHIPPED` → “Expédiée”
     * `PENDING` → “En attente”
     * `CANCELLED` → “Annulée”

2. Pour chaque client, calculer le **montant total dépensé** et le classer en segments :

   * `< 100 €`  → “Bronze”
   * `100–300 €` → “Argent”
   * `> 300 €`  → “Or”

   Afficher : prénom, nom, montant total, segment.

---

# 1️⃣1️⃣ Partie 9 – Challenge final

Proposer et écrire **5 requêtes d’analyse avancées** supplémentaires parmi, par exemple :

1. Top 5 des clients les plus actifs (nombre de commandes).
2. Top 5 des clients qui ont dépensé le plus (CA total).
3. Les 3 catégories les plus rentables (CA total).
4. Les produits qui ont généré au total **moins de 10 €** de CA.
5. Les clients n’ayant passé **qu’une seule commande**.
6. Les produits présents dans des commandes **annulées**, avec le montant “perdu”.

## Extension TP – Générer un rapport texte avec psycopg

### Objectif

Écrire un script Python qui :

* se connecte à la base `supershop`,
* exécute plusieurs requêtes SQL déjà vues dans le TP,
* écrit un fichier `rapport_supershop.txt` contenant :

  * des phrases en français (ex. *« Article le plus commandé : … »*),
  * le résultat (valeurs numériques, noms, etc.).

### Sections proposées dans le rapport

Par exemple :

1. Chiffre d’affaires total.
2. Panier moyen.
3. Article le plus commandé (en quantité totale).
4. Top 3 clients par montant dépensé.
5. Chiffre d’affaires par catégorie.