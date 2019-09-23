SELECT SUBSTRING("ownerMailingAddress", 0, POSITION('                              ' IN "ownerMailingAddress")) AS "Address Line 1" FROM "CRSData";

SELECT SUBSTRING("ownerMailingAddress", POSITION('                                ' IN "ownerMailingAddress") + 32, POSITION(',' IN "ownerMailingAddress") - (POSITION('                                ' IN "ownerMailingAddress") + 32)) AS "City" FROM "CRSData";

SELECT SUBSTRING("ownerMailingAddress", POSITION(', ' IN "ownerMailingAddress") + 2, 2) AS "State" FROM "CRSData";

SELECT SUBSTRING("ownerMailingAddress", POSITION(', ' IN "ownerMailingAddress") + 6, 10) AS "ZIP Code" FROM "CRSData";

SELECT * FROM "CRSData"; 

SELECT SUBSTRING("ownerMailingAddress", 0, POSITION('                              ' IN "ownerMailingAddress")) AS "Address Line 1" FROM "CRSData";

CREATE VIEW "view" AS SELECT DISTINCT "extraFeatures" AS "First Name", 
	"extraFeatures" AS "Last Name", 
	"ownerName" AS "Company Name",
	SUBSTRING("ownerMailingAddress", 0, POSITION('                              ' IN "ownerMailingAddress")) AS "Address Line 1",
	SUBSTRING("ownerMailingAddress", POSITION('                                ' IN "ownerMailingAddress") + 32, POSITION(',' IN "ownerMailingAddress") - (POSITION('                                ' IN "ownerMailingAddress") + 32)) AS "City", 
	SUBSTRING("ownerMailingAddress", POSITION(', ' IN "ownerMailingAddress") + 2, 2) AS "State",
	SUBSTRING("ownerMailingAddress", POSITION(', ' IN "ownerMailingAddress") + 6, 10) AS "ZIP Code"
	FROM "CRSData";

SELECT "First Name", "Last Name", STRING_AGG(DISTINCT "Company Name", ', ') AS "Company Name", "Address Line 1", "City" ,"State", "ZIP Code" FROM "view" GROUP BY "First Name", "Last Name",  "Address Line 1", "City" ,"State", "ZIP Code"