# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 18:36:58 2019

@author: CTA
"""
from enum import Enum
import random

class Usuario():
    """Entidad que representa un usuario de la plataforma"""
    def __init__(self, id, nombre, direccion, telefono, categoria, mail):
        self.__id =id
        self.__nombre = nombre
        self.__direccion = direccion
        self.__telefono = telefono
        self.__categoria = categoria
        self.__mail = mail
        
    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def direccion(self):
        return self.direccion
    
    @property
    def telefono(self):
        return self.__telefono
    
    @property
    def categoria(self):
        return self.__categoria
    
    @property
    def mail(self):
        return self.__mail
        

class Empresa(Usuario):
    """Entidad que representa una empresa cateforizada que
    puede dar de alta proyectos en la plataforma"""
    
    def __init__(self, cif, nombre, direccion, telefono, categoria, mail, descripcion):
        super().__init__(self, cif, nombre, direccion, telefono, categoria, mail, descripcion)
        self.__descripcion = descripcion
        """Constructor que inicializa los datos basicos de una empresa"""
        
    @property
    def descripcion(self):
        return self.__descripcion

    @descripcion.setter
    def descripcion(self, descripcion):
        self.__descripcion = descripcion 
    
    
class Trabajador(Usuario):
    """Entidad que representa un trabajador que quiere participar en los proyectos 
    de la plataforma """
    
    
    def __init__(self, dni, nombre, direccion, telefono, categoria, mail, descripcion):
        super().__init__(self, dni, nombre, direccion, telefono, categoria, mail, descripcion)
        self.__descripcion = descripcion
        self.score = 5
        self.proyectos = {}
        """Constructor que inicializa los datos basicos de un trabajador"""
        
        
    def __cmp__( self, other ) :
        if self.__score < other.__score :
            rst = -1
        elif self.__score > other.__score :
            rst = 1
        else :
           a = random.random() * 2
           if a == 2:
               rst = -1
           else:
               rst = 1
        return rst
    
        
    @property
    def descripcion(self):
        return self.__descripcion

    @descripcion.setter
    def descripcion(self, descripcion):
        self.__descripcion = descripcion
        
    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, score):
        self.__score = score   
        
    @property
    def proyectos(self):
        return self.proyectos

    @proyectos.setter
    def proyectos(self, proyectos):
        self.__proyectos = proyectos       
        
        
class Categoria(Enum):
    "Enum para representar las distintas categorias de proyectos y empresas"
    TI = 1
    INGENIERIA = 2
    AGRICOLA = 3 
    QUIMICA = 4
    
            
