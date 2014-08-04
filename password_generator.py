# -*- coding: utf-8 -*-

from werkzeug.security import generate_password_hash

password = raw_input("Enter a password: ")
hash = generate_password_hash(password)
print hash
