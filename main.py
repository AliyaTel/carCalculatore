import calculate

if __name__ == '__main__':
    calc = calculate.Calculate(years=10)
    calc.add_car(
        calculate.Car("Toyota Corolla", price=30000, fuel_economy=7,
                      service_cost=200, insurance_cost=2500)
    )
    calc.add_car(
        calculate.ElectricCar("Tesla model 3", 200000, 5500, 15)
    )
    calc.add_car(
        calculate.Car("Range Rover", 650000, 4,
                      service_cost=3000, insurance_cost=7000)
    )
    calc.add_car(
        calculate.Car("Bentley", 650000, 4,
                      service_cost=3000, insurance_cost=7000)
    )
    calc.print_cars()


