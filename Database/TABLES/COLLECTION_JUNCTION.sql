DO $$
BEGIN
	RAISE INFO 'CREATE of COLLECTION_JUNCTION';

	CREATE TABLE FIND.COLLECTION_JUNCTION
	(
		DATA_MODIFIED_TS TIMESTAMP NOT NULL,
		INDICATOR_ID INT NOT NULL,
		COLLECTION_ID INT NOT NULL,
		CONSTRAINT COLLECTION_JUNCTION_PK PRIMARY KEY ( INDICATOR_ID, COLLECTION_ID )
	)
	WITH (
		OIDS=FALSE
	);
END $$;
