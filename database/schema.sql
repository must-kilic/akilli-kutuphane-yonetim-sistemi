-- =========================
-- DATABASE: library_db
-- =========================

-- USER TABLOSU
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    role VARCHAR(20) CHECK (role IN ('USER', 'ADMIN')) NOT NULL
);

-- AUTHOR TABLOSU
CREATE TABLE authors (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);

-- CATEGORY TABLOSU
CREATE TABLE categories (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);

-- BOOK TABLOSU
CREATE TABLE books (
    id SERIAL PRIMARY KEY,
    title VARCHAR(150) NOT NULL,
    author_id INT REFERENCES authors(id),
    category_id INT REFERENCES categories(id),
    available BOOLEAN DEFAULT TRUE
);

-- LOAN TABLOSU
CREATE TABLE loans (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id),
    book_id INT REFERENCES books(id),
    loan_date DATE DEFAULT CURRENT_DATE,
    return_date DATE,
    due_date DATE
);

-- FINE TABLOSU
CREATE TABLE fines (
    id SERIAL PRIMARY KEY,
    loan_id INT REFERENCES loans(id),
    amount NUMERIC(10,2),
    paid BOOLEAN DEFAULT FALSE
);

-- =========================
-- TRIGGER FUNCTION (GEÇ İADE CEZASI)
-- =========================
CREATE OR REPLACE FUNCTION calculate_fine()
RETURNS TRIGGER AS $$
DECLARE
    late_days INT;
BEGIN
    IF NEW.return_date > NEW.due_date THEN
        late_days := NEW.return_date - NEW.due_date;
        INSERT INTO fines (loan_id, amount)
        VALUES (NEW.id, late_days * 5);
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- TRIGGER
CREATE TRIGGER trg_calculate_fine
AFTER UPDATE OF return_date
ON loans
FOR EACH ROW
EXECUTE FUNCTION calculate_fine();

-- =========================
-- STORED PROCEDURE (KİTAP ÖDÜNÇ)
-- =========================
CREATE OR REPLACE PROCEDURE borrow_book(
    p_user_id INT,
    p_book_id INT
)
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO loans (user_id, book_id, due_date)
    VALUES (p_user_id, p_book_id, CURRENT_DATE + INTERVAL '14 days');

    UPDATE books
    SET available = FALSE
    WHERE id = p_book_id;
END;
$$;
