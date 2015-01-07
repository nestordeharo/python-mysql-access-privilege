#!/usr/bin/env python
# coding=utf-8
import sys

## Module for whitelist ip, create user and assign privileges
def Db_User_Privileges(ip_list, user_password, db_table_privileges):

  def function_error(message):
    print message
    sys.exit(1)
  ## End function_error

  ## Verify if variables has specific type
  if not isinstance(ip_list, list):
    function_error('The ip_list variable is not a list')

  elif not ip_list:
    function_error('The ip_list is empty')

  elif not isinstance(user_password, dict):
    function_error('The user_password variable is not a dictionary')

  elif not user_password:
    function_error('The user_password dictionary is empty')

  elif not isinstance(db_table_privileges, dict):
    function_error('The db_table_privileges variable is not a dictionary')

  elif not db_table_privileges:
    function_error('The user_password variable is not a dictionary')

  output = ''

  for individual_ip in ip_list:
    for user, password in user_password.iteritems():

      if not user or not password:
        function_error('User or password are empty')

      ## To avoid problems, we convert the variables into string
      individual_ip = str(individual_ip)
      user          = str(user)
      password      = str(password)

      ## Create the user for each ip address and assign a password
      output += "CREATE USER '%s'@'%s' IDENTIFIED BY '%s'; " % (user, individual_ip, password)

      for db, table_privilege in db_table_privileges.iteritems():

        if not db or not table_privilege:
          function_error('Database or Table dictionary are empty')

        if '*' in table_privilege.keys() and len(table_privilege.keys()) > 1:
          function_error('* should be alone for database: '+db)

        for table, privileges in table_privilege.iteritems():
          if not isinstance(privileges, list):
            function_error('Privileges is not a list')

          elif not table or not privileges:
            function_error('Table or Privileges list are empty')

          privileges = [x.upper() for x in privileges]

          if ('ALL' in privileges or 'ALL PRIVILEGES' in privileges) and len(privileges) > 1:
            function_error('ALL privileges should be used alone')

          output += "GRANT %s ON %s.%s TO '%s'@'%s';" % (', '.join(privileges), db, table, user, individual_ip)

  ## Print the information
  output += ' FLUSH PRIVILEGES;'

  print output

  return True
## End function
