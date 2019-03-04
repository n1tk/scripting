#!/usr/bin/env python
import os, sys

"""
@Author Sergiu Buciumas <buciuser@gmail.com>
define the parameters for the user creation
function takes 4 parameters as input and creates the user
"""

username = sys.argv[1]
name = sys.argv[2]


def create_user(*nparams):
    """username: stand for the user to be created
    password: the password for the username to be used
    path: is the path where the home directory for the user reside
    name: the full name for the username aka comments or FQN
    """
    return os.system("useradd -r " + " -s "+ "/bin/nologin " + " -m " +  " -c \"" + name + " \"" + " -U " + username)


if __name__ == '__main__':
    # Calling createUser() function
    create_user(username, name)
