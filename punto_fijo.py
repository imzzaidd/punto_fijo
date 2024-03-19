#------------------------------------------------------------------------------------------------- 
                            #INSTITUTO POLITÉCNICO NACIONAL

    #UNIDAD PROFESIONAL INTERDISCIPLINARIA DE INGENIERÍA Y CIENCIAS SOCIALES Y ADMINISTRATIVAS
            
                                #INGENIERÍA EN INFORMÁTICA
                                
            #ALUMNO: GARCÍA HERNÁNDEZ ZAID ARATH
            #BOLETA: 2022602229
            #SECUENCIA: 5NV51
            #MATERIA: MÉTODOS NUMÉRICOS
#--------------------------------------------------------------------------------------------------
#LIBRERIAS

import math

#CLASE PRINCIPAL
class PuntoFijo:
    def __init__(self, funcion_iteracion):
        self.funcion_iteracion = funcion_iteracion
    def encontrar_raiz(self, estimacion_inicial, tolerancia=1e-10, max_iter=1000):
        iteracion = 0
        x_actual = estimacion_inicial
        while iteracion < max_iter:
            x_siguiente = self.funcion_iteracion(x_actual)
            error = abs(x_siguiente - x_actual)
            print(f"Iteración {iteracion + 1}: Raíz aproximada = {x_siguiente:.10f}, Error = {error:.10f}")
            if error < tolerancia:
                print("La ejecución se detuvo ya que el error es menor que la tolerancia.")
                return x_siguiente
            x_actual = x_siguiente
            iteracion += 1
        print("El punto fijo no converge dentro del número máximo de iteraciones.")
        return None
#VALORES ACEPTADOS
def funcion_iteracion(x):
    result = (x**3 - 5) / 2
    if result < -1e100:
        result = -1e100
    elif result > 1e100:
        result = 1e100
    return result
#OUTPUT
if __name__ == "__main__":
    print("Función f(x) = x^3 - 2*x - 5 para encontrar su raíz.")
    estimacion_inicial = float(input("Ingrese la estimación inicial de la raíz: "))
    punto_fijo = PuntoFijo(funcion_iteracion)
    print("\nUtilizando el método del Punto Fijo con la función de iteración:")
    punto_fijo.encontrar_raiz(estimacion_inicial)
