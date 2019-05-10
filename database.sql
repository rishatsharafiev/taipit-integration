/* drop tables */
DROP TABLE IF EXISTS result_queue;

/* create queue table */
CREATE TABLE result_queue (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    result_id varchar(255) NOT NULL,
    status varchar(100) CHECK( status IN ('NEW', 'PROGRESS', 'DONE', 'UPDATED', 'ERROR') ) NOT NULL DEFAULT 'NEW'
);
