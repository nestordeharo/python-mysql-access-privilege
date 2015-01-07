Python MySQL Simple Account Management Generator
======================

## Description:
This is a simple script in Python that help you to generate the command for whitelist I.P. addresses, create user with passwords and grant permissions.

At the end of this script, you just copy paste the output and integrate into MySQL.

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
