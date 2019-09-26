# -*- coding: utf-8 -*-
from gestion_plataforma import Plataforma
from gestion_proyectos import EstadosProyecto
from gestion_usuarios import Trabajador, Empresa,Categoria

def main():
    
    plataforma = Plataforma('Mi Plataforma')
    empresa1 = Empresa('CIF1', 'Cervezas Alhambra', 'Zaragoza', '97654587', Categoria.QUIMICA, 'ca@google.com', 'Hacemos cervezas')
    empresa2 = Empresa('CIF2', 'Adidas', 'Zaragoza', '9765487785', Categoria.TI, 'adidas@google.com', 'Hacemos zapatillas para luego beber cerveza')
    empresa3 = Empresa('CIF3', 'Amylum', 'Zaragoza', '976858585', Categoria.AGRICOLA, 'Amylum@google.com', 'Producimos cebada')
    
    #
    trabajador1 = Trabajador('25774884E', 'David', 'Su casa', 'Su telefono', Categoria.TI, 'david@gmail.com', 'David')
    trabajador2 = Trabajador('25774884E', 'Miguel', 'Su casa', 'Su telefono', Categoria.QUIMICA, 'david@gmail.com', 'David')
    trabajador3 = Trabajador('25774884E', 'Inigo', 'Su casa', 'Su telefono', Categoria.AGRICOLA, 'david@gmail.com', 'David')
    

    
if __name__ == "__main__":
    print("Arrancamos ...")
    main()
    