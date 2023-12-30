-- Table: students
DROP TABLE IF EXISTS students;
CREATE TABLE students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_name VARCHAR(255) UNIQUE NOT NULL,
    group_id INTEGER,
    FOREIGN KEY (group_id) REFERENCES groups (group_name)
      ON DELETE CASCADE
      ON UPDATE CASCADE
);

-- Table: groups
DROP TABLE IF EXISTS groups;
CREATE TABLE groups (
    group_name INTEGER UNIQUE NOT NULL
);

-- Table: tutors
DROP TABLE IF EXISTS tutors;
CREATE TABLE tutors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tutor_name VARCHAR(255) UNIQUE NOT NULL
);

-- Table: lessons
DROP TABLE IF EXISTS lessons;
CREATE TABLE lessons (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    lesson VARCHAR(255) UNIQUE NOT NULL,
    tutor_id INTEGER,
    FOREIGN KEY (tutor_id) REFERENCES tutors (id)
      ON DELETE CASCADE
      ON UPDATE CASCADE
);

-- Table: marks
DROP TABLE IF EXISTS marks;
CREATE TABLE marks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER,
    lesson_id INTEGER,
    rate INTEGER NOT NULL,
    date_of DATE NOT NULL,
    FOREIGN KEY (student_id) REFERENCES students (id)
      ON DELETE CASCADE
      ON UPDATE CASCADE,
    FOREIGN KEY (lesson_id) REFERENCES lessons (id)
      ON DELETE CASCADE
      ON UPDATE CASCADE
);