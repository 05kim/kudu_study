CREATE TABLE my_kudu_table (
    id BIGINT,
    name STRING,
    age BIGINT,
    PRIMARY KEY (id)
) PARTITION BY HASH (id) PARTITIONS 4 STORED AS KUDU TBLPROPERTIES (
    'kudu.master_addresses' = 'kudu-master-1:7051',
    'kudu.num_tablet_replicas' = '1'
);

INSERT INTO
    my_kudu_table (id, name, age)
VALUES
    (1, 'John Doe', 30),
    (2, 'Jane Smith', 25),
    (3, 'Mike Johnson', 35);