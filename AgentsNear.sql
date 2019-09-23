CREATE FUNCTION PointInCircle(agent_lat FLOAT, agent_long FLOAT, prop_lat FLOAT, prop_long FLOAT, radius FLOAT)
RETURNS BOOLEAN AS 
$$ SELECT POWER(POWER((agent_lat - prop_lat), 2) + POWER((agent_long - prop_long), 2), 0.5) < radius $$ 
LANGUAGE SQL;

SELECT "name", "streetNumber", "address", "city", "phoneNumber", "email" FROM "ApplicantAgents" WHERE PointInCircle("latitude", "longitude", 70, 50, 999)