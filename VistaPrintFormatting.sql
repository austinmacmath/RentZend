SELECT SUBSTRING("ownerMailingAddress", 0, POSITION('                              ' IN "ownerMailingAddress")) AS "Address Line 1" FROM "CRSData";

SELECT SUBSTRING("ownerMailingAddress", POSITION('                                ' IN "ownerMailingAddress") + 32, POSITION(',' IN "ownerMailingAddress") - (POSITION('                                ' IN "ownerMailingAddress") + 32)) AS "City" FROM "CRSData";

SELECT SUBSTRING("ownerMailingAddress", POSITION(', ' IN "ownerMailingAddress") + 2, 2) AS "State" FROM "CRSData";

SELECT SUBSTRING("ownerMailingAddress", POSITION(', ' IN "ownerMailingAddress") + 6, 10) AS "ZIP Code" FROM "CRSData";

SELECT * FROM "CRSData"; 