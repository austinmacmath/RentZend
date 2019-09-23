CREATE FUNCTION PointInsideCircle(x1 FLOAT, y1 FLOAT, x2 FLOAT, y2 FLOAT, radius FLOAT, x float)
RETURNS BOOLEAN AS 
$$ SELECT POWER(POWER((x1 - x2), 2) + POWER((y1 - y2), 2), 0.5) > radius $$ 
LANGUAGE SQL;

SELECT * FROM "ApplicantAgents"

SELECT "name" FROM "ApplicantAgents" WHERE PointInsideCircle("latitude", "longitude", 43, -85, 5, 4)

SELECT PointInsideCircle(CAST("latitude" AS NUMERIC), CAST ("longitude" AS NUMERIC), 43, -85, 5) FROM "ApplicantAgents";

CREATE FUNCTION PointInCircle(agent_lat FLOAT, agent_long FLOAT, prop_lat FLOAT, prop_long FLOAT, radius FLOAT)
RETURNS BOOLEAN AS 
$$ SELECT POWER(POWER((agent_lat - prop_lat), 2) + POWER((agent_long - prop_long), 2), 0.5) < radius $$ 
LANGUAGE SQL;

SELECT "name" FROM "ApplicantAgents" WHERE PointInCircle("latitude", "longitude", 43, -85, 4)