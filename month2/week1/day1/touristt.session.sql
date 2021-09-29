-- CREATE TABLE inner_flyghts(
--     id SERIAL PRIMARY KEY,
--     from_region VARCHAR,
--     to_destination VARCHAR,
--     company VARCHAR,
--     quantity INT
-- );
INSERT INTO inner_flyghts(
    from_region,
    to_destination,
    company,
    quantity
)
values(
    'india',
    'russia',
    'gtogvc',
    '577'
);


--  CREATE TABLE outters_flyghts(
--     id SERIAL PRIMARY KEY,
--     from_country VARCHAR,
--     to_country VARCHAR,
--     flyght_type VARCHAR,
--     company VARCHAR,
--     neighbors INT
-- );
-- INSERT INTO outters_flyghts(
--     from_country,
--     to_country,
--     flyght_type,
--     company,
--     neighbors
-- )
-- values(
--     'korolev',
--     'novosibirs',
--     'grus',
--     'flytou',
--     '5'
-- );