create_tb = "CREATE TABLE bank_users(id_card CHAR(15) PRIMARY KEY, u_name VARCHAR(10) NOT NULL, phone_number CHAR(11) NOT NULL, password CHAR(32) NOT NULL, money INT DEFAULT 0)"
drop_tb = "DROP TABLE bank_users"
sign_up = "INSERT INTO bank_users(id_card,u_name,phone_number,password) VALUES ('{}','{}','{}','{}')"
drop_user = "DELETE FROM bank_users WHERE id_card = '{}'AND password = '{}'"
find_all = "SELECT * FROM bank_users"
find_money = "SELECT money FROM bank_users WHERE id_card = '{}'"
sign_in = "SELECT u_name FROM bank_users WHERE id_card = '{}'AND password = '{}'"
change_money = "UPDATE  bank_users  SET money = {}  WHERE  id_card = '{}' "
change_passwd = "UPDATE  bank_users  SET password = '{}'  WHERE  id_card = '{}'AND password = '{}'"