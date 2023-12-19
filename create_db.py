import sqlite3

# Создание подключения к базе данных
conn = sqlite3.connect('cinema.db')
cursor = conn.cursor()

# Создание таблиц и связей
cursor.executescript('''
    CREATE TABLE Positions (
        code INTEGER PRIMARY KEY,
        title TEXT,
        salary DECIMAL(10, 2),
        duties TEXT,
        requirements TEXT
    );

    CREATE TABLE Genres (
        code INTEGER PRIMARY KEY,
        name TEXT,
        description TEXT
    );

    CREATE TABLE Movies (
        code INTEGER PRIMARY KEY,
        title TEXT,
        genre_code INTEGER,
        duration INTEGER,
        producer TEXT,
        country TEXT,
        age_restrictions INTEGER,
        description TEXT,
        FOREIGN KEY (genre_code) REFERENCES Genres(code)
    );

    CREATE TABLE Repertoire (
        session_code INTEGER PRIMARY KEY,
        date DATE,
        start_time TIME,
        film_code INTEGER,
        ticket_price DECIMAL(8, 2),
        FOREIGN KEY (film_code) REFERENCES Movies(code)
    );

    CREATE TABLE Places (
        code INTEGER PRIMARY KEY,
        session_code INTEGER,
        place INTEGER,
        FOREIGN KEY (session_code) REFERENCES Repertoire(session_code)
    );

    CREATE TABLE Employees (
        code INTEGER PRIMARY KEY,
        full_name TEXT,
        date_of_birth DATE,
        gender TEXT,
        address TEXT,
        telephone TEXT,
        passport TEXT,
        position_code INTEGER,
        FOREIGN KEY (position_code) REFERENCES Positions(code)
    );

    INSERT INTO Positions (code, title, salary, duties, requirements) VALUES (1, 'Manager', 50000.00, 'Manage staff and operations', 'Bachelor''s degree, leadership skills');
    INSERT INTO Positions (code, title, salary, duties, requirements) VALUES (2, 'Ticket Seller', 30000.00, 'Sell tickets to customers', 'High school diploma, customer service skills');

    INSERT INTO Genres (code, name, description) VALUES (1, 'Action', 'Movies with high-intensity action sequences');
    INSERT INTO Genres (code, name, description) VALUES (2, 'Comedy', 'Movies intended to be humorous');

    INSERT INTO Movies (code, title, genre_code, duration, producer, country, age_restrictions, description) VALUES (1, 'The Avengers', 1, 150, 'Joss Whedon', 'USA', 12, 'Superhero movie');
    INSERT INTO Movies (code, title, genre_code, duration, producer, country, age_restrictions, description) VALUES (2, 'The Hangover', 2, 120, 'Todd Phillips', 'USA', 18, 'Comedy about a bachelor party');

    INSERT INTO Repertoire (session_code, date, start_time, film_code, ticket_price) VALUES (101, '2023-01-10', '18:00:00', 1, 10.00);
    INSERT INTO Repertoire (session_code, date, start_time, film_code, ticket_price) VALUES (102, '2023-01-11', '20:00:00', 2, 8.00);

    INSERT INTO Places (code, session_code, place) VALUES (1, 101, 1);
    INSERT INTO Places (code, session_code, place) VALUES (2, 101, 2);
    INSERT INTO Places (code, session_code, place) VALUES (3, 102, 1);
    INSERT INTO Places (code, session_code, place) VALUES (4, 102, 2);

    -- Пример вставки данных в Employees
    INSERT INTO Employees (code, full_name, date_of_birth, gender, address, telephone, passport, position_code) VALUES (1, 'John Doe', '1990-01-01', 'Male', '123 Main St', '123-456-7890', 'AB123456', 1);
    INSERT INTO Employees (code, full_name, date_of_birth, gender, address, telephone, passport, position_code) VALUES (2, 'Jane Smith', '1985-05-15', 'Female', '456 Oak St', '987-654-3210', 'CD987654', 2);
''')

# Сохранение изменений и закрытие подключения
conn.commit()
conn.close()
