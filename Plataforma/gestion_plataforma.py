# -*- coding: utf-8 -*-
#import gestion_usuarios
from gestion_proyectos import EstadosProyecto, Proyecto
import random
class Plataforma:
    """
    Clase plataforma: 
        
    """
    max_candidatos_proyecto = 3
    # estados = Nuevo / Abierto / Cerrado
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__empresas = []
        self.__trabajadores = []
        self.__proyectos = []
    
# =============================================================================
#     @property
#     def valoracion(self):
#         return self.__valoracion
#     
#     @valoracion.setter
#     def valoracion(self,valoracion):
#         self.__valoracion = valoracion
#     
# =============================================================================
    
    def anadir_empresa(self,empresa):
        self.__empresas.append(empresa)
        return True
    
    def anadir_trabajador(self,trabajador):
        self.__empresas.append(trabajador)
        return True

    def anadir_proyecto(self,proyecto):
        self.__proyectos.append(proyecto)
        return True

    def anadir_candidato_a_proyecto(self,candidato,id_proyecto):
        """
        Añade candidato a un proyecto, si:
            a) el proyecto no esta Cerrado, Y
            b) el proyecto no tiene ya 3 candidatos
        """
        proyecto_destino = filter(lambda p: p.id == id_proyecto, self.__proyectos)
        if proyecto_destino == None:
            return False
        else: 
            if proyecto_destino.estado =="Cerrado" or proyecto_destino.numero_candidatos >= self.max_candidatos_proyecto:
                return False
            else:
                proyecto_destino.anadir_candidato(candidato)
    
    def adjudicar_proyecto(self, proyecto):
        if proyecto.candidatos != None and len(proyecto.candidatos) > 0:
            listado = proyecto.candidatos.sort()
            ganador = listado[0]
            proyecto.ganador(ganador)
        
    def cerrar_proyecto(self, proyecto):
        proyecto.estado = EstadosProyecto.Cerrado
        valor = self.valorar_proyecto(proyecto)
        proyecto.ganador.score +=valor
    
    def valorar_proyecto(self,proyecto):
        valor = random.randint(1,10)
        return valor


