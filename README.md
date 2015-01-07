Python MySQL Simple Account Management Generator
======================

## Description:
This is a simple script in Python that help you to generate MySQL commands for whitelist I.P. addresses, create user with passwords and grant permissions to tables and database.

At the end of this script, you just copy paste the output and integrate into MySQL shell.

## Support Version
Python 2.x.x

## Usage

The function inside the `main.py`: *Db_User_Privileges* needs three different variables:

1) A List of the n different i.p. addresses we want to whitelist

```Python
  ip_list = ['I.P.address1', 'I.P.address2', ... ]
```
2) A dictionary of users and password we are going to introduce in our MySQL server

```Python
  user_password_dict = {'user_1':'strong_password', 'user_2': 'strong_password2', ...}
```
3) A dictionary of databases, tables and permissions we assign for each case

**Note: Use "*" for assign all tables inside the database**

```Python
  db_table_privilege = {
    'db_1':{
      '*': ['SELECT', 'INSERT']
    }, 
    'db_2':{
      'table_1':['SELECT'], 
      'table_2': ['SELECT','INSERT']
    },
    ...
  }
```
Then we need to call the **Db_User_Privileges** function and the script will print the commands you could introduce in the MySQL shell

```Python
  result = Db_User_Privileges(ip_list, user_password_dict, db_table_privilege)
``` 

## Result

Just copy & paste the result and ready to integrate in MySQL shell.

```SQL
  CREATE USER 'user'@'ip_add_1' IDENTIFIED BY 'secret_password';  GRANT ALL PRIVILEGES ON db_2.table_2 TO 'user'@'ip_add_1'; GRANT SELECT, INSERT ON db_2.table_1 TO 'user'@'ip_add_1'; GRANT ALL PRIVILEGES ON db_1.* TO 'user'@'ip_add_1';CREATE USER 'user'@'ip_add_2' IDENTIFIED BY 'secret_password';  GRANT ALL PRIVILEGES ON db_2.table_2 TO 'user'@'ip_add_2'; GRANT SELECT, INSERT ON db_2.table_1 TO 'user'@'ip_add_2'; GRANT ALL PRIVILEGES ON db_1.* TO 'user'@'ip_add_2'; FLUSH PRIVILEGES;
```

*Note: Spaces between commands has been eliminated to diminish problems when execute by MySQL shell*
