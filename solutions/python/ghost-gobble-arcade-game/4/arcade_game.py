"""
reglas del juego
"""
def eat_ghost(power_pellet_active, touching_ghost):
    """aqui vemos si podemos comer fantasmas"""
    return power_pellet_active and touching_ghost

def score(touching_power_pellet,touching_dot):
    """puntuacion"""
    return touching_power_pellet or touching_dot
    
def lose(power_pellet_active,touching_ghost):
    """perdemos si la paleta de poder esta inactiva y comemos un fantasma"""
    return touching_ghost and not power_pellet_active
    
def win(has_eaten_all_dots,power_pellet_active, touching_ghost ):
    """verifica si ganamos """
    # Usamos la función lose que definimos arriba para saber si perdió
    perder=lose(power_pellet_active,touching_ghost)
    
    return  has_eaten_all_dots and not perder