
DROP TABLE IF EXISTS test_results;

CREATE TABLE test_results (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    test_name TEXT NOT NULL,
    status TEXT CHECK(status IN ('PASS', 'FAIL')) NOT NULL,
    module TEXT,
    duration REAL,
    timestamp TEXT
);
