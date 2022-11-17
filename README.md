# HMS
Hospital management system
This project is integrated with MySQL
Four Tables required in the database HMS are:
Accounts:
+-------------+-------------+------+-----+---------+-------+
| Field       | Type        | Null | Key | Default | Extra |
+-------------+-------------+------+-----+---------+-------+
| Username    | varchar(20) | NO   |     | NULL    |       |
| Password    | varchar(20) | NO   |     | NULL    |       |
| Permissions | char(1)     | NO   |     | NULL    |       |
+-------------+-------------+------+-----+---------+-------+

PMS(Patient Management System):
+--------------+------------+------+-----+---------+-------+
| Field        | Type       | Null | Key | Default | Extra |
+--------------+------------+------+-----+---------+-------+
| PID          | varchar(4) | NO   | PRI | NULL    |       |
| Patient_name | char(20)   | NO   |     | NULL    |       |
| Illness      | char(30)   | NO   |     | NULL    |       |
| PhoneNo      | bigint(11) | NO   |     | NULL    |       |
| Gender       | char(1)    | YES  |     | NULL    |       |
+--------------+------------+------+-----+---------+-------+

DMS(Doctor Management System):
+------------+-------------+------+-----+---------+-------+
| Field      | Type        | Null | Key | Default | Extra |
+------------+-------------+------+-----+---------+-------+
| DocID      | varchar(4)  | NO   | PRI | NULL    |       |
| Doc_name   | char(20)    | NO   |     | NULL    |       |
| Department | char(20)    | NO   |     | NULL    |       |
| email      | varchar(50) | YES  |     | NULL    |       |
| Gender     | char(1)     | YES  |     | NULL    |       |
+------------+-------------+------+-----+---------+-------+

DrugMS(Drugs Management System):
+-------------+------------+------+-----+---------+-------+
| Field       | Type       | Null | Key | Default | Extra |
+-------------+------------+------+-----+---------+-------+
| DrugID      | varchar(4) | NO   | PRI | NULL    |       |
| DrugName    | char(20)   | NO   |     | NULL    |       |
| Department  | char(20)   | NO   |     | NULL    |       |
| Composition | char(20)   | NO   |     | NULL    |       |
| Expiry      | date       | NO   |     | NULL    |       |
+-------------+------------+------+-----+---------+-------+

This project works on these Tables inside the HMS database.

Created by Meghraj Nair

Installation:

1) pip install requirements.txt
2) python Sign_in.py
