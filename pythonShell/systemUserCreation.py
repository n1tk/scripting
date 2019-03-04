#!/usr/bin/env python
import os, sys

"""
@Author Sergiu Buciumas <buciuser@gmail.com>
define the parameters for the user creation
function takes 2 parameters as input and creates the user
https://superuser.com/a/515909/447483
https://superuser.com/questions/77617/how-can-i-create-a-non-login-user
"""

username = sys.argv[1]
name = sys.argv[2]


def create_user(*nparams):
    """username: stand for the user to be created
    name: the full name for the username aka comments or FQN
    The -r flag will create a system user - one which does not have a password, a home dir and is unable to login.
    return os.system("useradd -r -M" + " -s "+ "/bin/false" + " -c \"" + name + " \"" + " -U " + username)
    """
    return os.system("useradd -r -M" + " -s " + "/bin/nologin" + " -c \"" + name + " \"" + " -U " + username)


if __name__ == '__main__':
    # Calling createuser() function
    create_user(username, name)
