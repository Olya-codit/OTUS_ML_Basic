"""
Объявите следующие исключения:
- LowFuelError
- NotEnoughFuel
- CargoOverload
"""


class LowFuelError(Exception):
    """Ошибка: недостаточный уровень топлива для запуска."""
    pass


class NotEnoughFuel(Exception):
    """Ошибка: недостаточно топлива для преодоления заданной дистанции."""
    pass


class CargoOverload(Exception):
    """Ошибка: превышена грузоподъемность."""
    pass
