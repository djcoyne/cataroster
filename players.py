"""
This file defines a player class and the attributes/functions available for that class
"""
import classes

class Character:
  def __init__(self, name, cl, spec, **kwargs):
    self.n = name
    self.c = cl
    self.s = spec
    self.a = None

    if self.c=='Death Knight':
      if self.s=='Blood':
        if 'role' in kwargs:
          self.r = kwargs.get('role')
          self.a=classes.DKBlood(role=self.r)
        else:
          self.a=classes.DKBlood()
      elif self.s=='Frost':
        self.a=classes.DKFrost()
      elif self.s=='Unholy':
        self.a=classes.DKUnholy()
      else:
        print("Invalid Class/Spec Pairing")
           
    elif self.c=='Druid':
      if self.s=='Feral':
        if 'role' in kwargs:
          self.r = kwargs.get('role')
          self.a=classes.DrFeral(role=self.r)
        else:
          self.a=classes.DrFeral()
      elif self.s=='Balance':
        self.a=classes.DrBalance()
      elif self.s=='Restoration':
        self.a=classes.DrResto()
      else:
        print("Invalid Class/Spec Pairing") 

    elif self.c=='Hunter':
      if self.s=='BM':
        self.a=classes.HBM()
      elif self.s=='Marksmanship':
        self.a=classes.HMarks()
      elif self.s=='Survival':
        self.a=classes.HSurv()
      else:
        print("Invalid Class/Spec Pairing")
        
    elif self.c=='Mage':
      if self.s=='Arcane':
        self.a=classes.MArcane()
      elif self.s=='Fire':
        self.a=classes.MFire()
      elif self.s=='Frost':
        self.a=classes.MFrost()
      else:
        print("Invalid Class/Spec Pairing")
        
    elif self.c=='Paladin':
      if self.s=='Protection':
        self.a=classes.PalProt()
      elif self.s=='Holy':
        self.a=classes.PalHoly()
      elif self.s=='Retribution':
        self.a=classes.PalRet()
      else:
        print("Invalid Class/Spec Pairing")
        
    elif self.c=='Priest':
      if self.s=='Discipline':
        self.a=classes.PrDisc()
      elif self.s=='Holy':
        self.a=classes.PrHoly()
      elif self.s=='Shadow':
        self.a=classes.PrShadow()
      else:
        print("Invalid Class/Spec Pairing")       

    elif self.c=='Rogue':
      if self.s=='Assassination':
        self.a=classes.RAss()
      elif self.s=='Combat':
        self.a=classes.RCombat()
      elif self.s=='Subtlety':
        self.a=classes.RSubtlety()
      else:
        print("Invalid Class/Spec Pairing")    

    elif self.c=='Shaman':
      if self.s=='Enhancement':
        self.a=classes.SEnhance()
      elif self.s=='Elemental':
        self.a=classes.SElemental()
      elif self.s=='Restoration':
        self.a=classes.SResto()
      else:
        print("Invalid Class/Spec Pairing")        

    elif self.c=='Warlock':
      if self.s=='Affliction':
        self.a=classes.WkAff()
      elif self.s=='Demonology':
        self.a=classes.WkDemo()
      elif self.s=='Destruction':
        self.a=classes.WkDestro()
      else:
        print("Invalid Class/Spec Pairing")
        
    elif self.c=='Warrior':
      if self.s=='Arms':
        self.a=classes.WaArms()
      elif self.s=='Fury':
        self.a=classes.WaFury()
      elif self.s=='Protection':
        self.a=classes.WaProt()
      else:
        print("Invalid Class/Spec Pairing")
      
    else:
      print("Invalid Class")
    
  def buff_check(self):
    print(self.n+" provides:")
    for x in self.a.buffs:
      print(x)


class Player:
  def __init__(self, name, **kwargs):
    self.name = name
    self.charlist = []

  def add_character(self, name, cl, spec, **kwargs):
    if 'role' in kwargs:
      self.r = kwargs.get('role')
      self.charlist.append(Character(name, cl, spec, role=self.r))
    else:
      self.charlist.append(Character(name, cl, spec))
