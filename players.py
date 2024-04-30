"""
This file defines a player class and the attributes/functions available for that class
"""
import classes

class Character:
  def __init__(self, n, c, s, **kwargs):
    name = n
    class = c
    spec = s

    if c=='Death Knight':
      if s=='Blood':
        if 'role' in kwargs:
          r = role
          DKBlood(
      
    

  def buff_check(self):
    print(name
    
    

class Player:
  def __init__(self, name, **kwargs):
    self.name = name
    self.charlist = []

  def add_character(self, name, class, spec, **kwargs):
    if 'role' in kwargs:
      r = role
      Character(name, class, spec, role=r)
    else:
      Character(name, class, spec)
    self.charlist.append('name')
      

    
    
