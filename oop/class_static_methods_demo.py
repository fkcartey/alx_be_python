class Calculator:
    """A class demonstrating static and class methods."""
    
    # Class Attribute
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """Static Method: Performs addition without accessing class data."""
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """Class Method: Accesses the class attribute 'calculation_type'."""
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
