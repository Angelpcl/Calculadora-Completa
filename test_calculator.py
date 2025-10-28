import unittest
import time
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    # 1. Prueba Unitaria (Unit Test)
    def test_unit_add(self):
        """Verifica la función estática Calculator.add()."""
        
        # Suma Básica: 5 + 3 = 8
        self.assertEqual(Calculator.add(5, 3), 8)
        
        # Números Negativos: -1 + 10 = 9
        self.assertEqual(Calculator.add(-1, 10), 9)
        
        # Números Decimales: 1.5 + 2.5 = 4.0. Se usa assertAlmostEqual por floats
        self.assertAlmostEqual(Calculator.add(1.5, 2.5), 4.0)
        
        # Suma a Cero: 0 + 7 = 7
        self.assertEqual(Calculator.add(0, 7), 7)

    # 2. Prueba de Integración (Integration Test)
    def test_integration_chained_operations(self):
        """Verifica la secuencia de operaciones y la gestión del estado."""
        calc = Calculator()
        
        # Escenario Principal: 2 * 3 + 4 = 10
        calc.append_number(2)
        calc.choose_operation('*')
        calc.append_number(3)
        # Al elegir '+' se ejecuta la operación anterior (2 * 3 = 6)
        calc.choose_operation('+') 
        calc.append_number(4)
        calc.compute()
        
        # El resultado se almacena como string en current_operand
        self.assertEqual(calc.current_operand, '10.0', "2 * 3 + 4 debería ser 10")
        
        # Escenario Encadenado: 10 / 2 - 1 + 6 = 10
        calc.clear()
        calc.append_number(10)
        calc.choose_operation('/')
        calc.append_number(2) # (10 / 2 = 5)
        calc.choose_operation('-')
        calc.append_number(1) # (5 - 1 = 4)
        calc.choose_operation('+')
        calc.append_number(6) # (4 + 6 = 10)
        calc.compute()
        self.assertEqual(calc.current_operand, '10.0', "10 / 2 - 1 + 6 debería ser 10")

    # 3. Prueba de Rendimiento (Performance / Stress Test)
    def test_performance_compute(self):
        """Mide la velocidad de ejecución de compute() bajo carga."""
        iterations = 100000 # Carga de trabajo extrema
        # Establece un umbral de tiempo máximo (adaptado para Python)
        MAX_TIME_MS = 250
        
        start_time = time.time()
        
        for _ in range(iterations):
            calc = Calculator()
            calc.append_number(10)
            calc.choose_operation('+')
            calc.append_number(5)
            calc.compute()

        end_time = time.time()
        total_time_ms = (end_time - start_time) * 1000
        
        print(f"\n[Performance Test] Tiempo total para {iterations} ejecuciones: {total_time_ms:.2f} ms")
        self.assertLess(total_time_ms, MAX_TIME_MS, f"El tiempo ({total_time_ms:.2f} ms) excede el umbral de prueba, indicando una posible ralentización.")

# Para ejecutar las pruebas desde la terminal: python -m unittest test_calculator.py
if __name__ == '__main__':
    unittest.main()