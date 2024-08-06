class RocketNotReadyError(Exception):
    pass


def personnel_check():
    try:
        print("\tThe captain's name is", crew[0])
        print("\tThe pilot's name is", crew[1])
        print("\tThe mechanic's name is", crew[2])
        print("\tThe navigator's name is", crew[3])
    except IndexError as e:
        raise RocketNotReadyError('Crew is incomplete') from e


def fuel_check():
    try:
        print('Fuel tank is full in {}%'.format(100/0))
    except ZeroDivisionError as e:
        raise RocketNotReadyError('Problem with fuel gauge') from e


def batteries_check():
    try:
        battery_status = "low"  # Change to "low" or "discharged" to simulate an error
        if battery_status != "charged":
            raise ValueError("Battery status is not optimal")
        print("\tBatteries are fully charged")
    except ValueError as e:
        raise RocketNotReadyError('Battery check failed') from e


def circuits_check():
    try:
        circuits_status = "operational"  # Change to "faulty" or "non-operational" to simulate an error
        if circuits_status != "faulty":
            raise ValueError("Circuit status is not optimal")
        print("\tCircuits are fully operational")
    except ValueError as e:
        raise RocketNotReadyError('Circuit check failed') from e


crew = ['John', 'Mary', 'Mike']
fuel = 100
check_list = [personnel_check, fuel_check, batteries_check, circuits_check]

print('Final check procedure')

for check in check_list:
    try:
        check()
    except RocketNotReadyError as f:
        print('RocketNotReady exception: "{}", caused by "{}"'.format(f, f.__cause__))
