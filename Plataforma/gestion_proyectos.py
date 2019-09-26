# -*- coding: utf-8 -*-
#import gestion_usuarios, gestion_empresas
from enum import Enum

class EstadosProyecto(Enum):
    Nuevo = 1
    Abierto = 2
    Cerrado = 0
    

class Proyecto:
    """
    Clase proyecto: 
        Estados del proyecto: Abierto / Adjudicado / Cerrado
        Categorias: Ingenieria / IT / Otros
    """
    # estados = Nuevo / Abierto / Cerrado
    estados_posibles = {'Nuevo','Abierto','Cerrado'}
    def __init__(self,id,empresa,categoria=None,estado="Nuevo"):
        self.__id = id
        self.__empresa= empresa
        self.__categoria = categoria
        self.__estado = estado
        self.__candidatos = []
        self.__ganador = None
        self.__valoracion = 0
        self.__numero_candidatos = 0
    
    @property
    def id(self):
        return self.__id
    
    @property
    def empresa(self):
        return self.__empresa
    
    @property
    def categoria(self):
        return self.__categoria
    @property
    def estado(self):
        return self.__estado

    @property
    def valoracion(self):
        return self.__valoracion
    
    @property
    def candidatos(self):
        return self.__candidatos
    
    @property
    def ganador(self):
        return self.__ganador

    @valoracion.setter
    def valoracion(self,valoracion):
        self.__valoracion = valoracion

    @estado.setter
    def estado(self,estado):
        if self.__estado not in EstadosProyecto:
            raise Exception('Estado no permitido')
        self.__estado = estado

    @ganador.setter
    def ganador(self,ganador):
        self.__ganador = ganador


    @property
    def numero_candidatos(self):
        return self.__numero_candidatos
    
    def anadir_candidato(self,usuario):
        if len(self.__candidatos) < 3:
            self.__candidatos.append(usuario)
            self.__numero_candidatos +=1
            return True
        else:
            return False
    
        
