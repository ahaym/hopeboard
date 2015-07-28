CREATE TABLE tablex (a INTEGER, b TEXT)
CREATE TABLE peopletracker (indx INTEGER PRIMARY KEY, lastname varchar(120), firstname varchar(120), DOB date, gender varchar(1), imgfilename varchar(32), agency varchar(120), agencycontactperson varchar(120), agencyID varchar(32))

INSERT INTO "peopletracker" ("lastname", "firstname","DOB")
SELECT "lastname", "firstname", "DOB"
FROM "patients2"


AND Date = "Jan-08-1999"


