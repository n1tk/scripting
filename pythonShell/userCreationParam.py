#!/usr/bin/env python
import os, sys

"""
@Author Sergiu Buciumas <buciuser@gmail.com>
define the parameters for the user creation
function takes 4 parameters as input and creates the user
"""

username = sys.argv[1]
password = sys.argv[2]
user_path = sys.argv[3]
name = sys.argv[4]


def create_user(*nparams):
    """username: stand for the user to be created
    password: the password for the username to be used
    path: is the path where the home directory for the user reside
    name: the full name for the username aka comments or FQN
    """
    return os.system("useradd -p " + password + " -s "+ "/bin/nologin " + " -m " + " -d " + user_path + " -c \"" + name + " \"" + " -U " + username)


if __name__ == '__main__':
    # Calling createUser() function
    create_user(username, password, user_path, name)
