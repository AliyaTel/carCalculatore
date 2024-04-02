import pytest
from calculate import Car, ElectricCar, Calculate


@pytest.fixture(scope="session")
def car():
    print("\ncreate a new car\n")
    return Car("Toyota Corolla", price=30000, fuel_economy=7, service_cost=200,
               insurance_cost=2500)


@pytest.fixture
def electric_car():
    return ElectricCar("Tesla", 10000, 5000, 1500)


@pytest.fixture
def calculator(car):
    res = Calculate()
    res.add_car(car)
    return res
