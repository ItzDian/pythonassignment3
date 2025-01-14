print("*** Welcome to RMIT Spaceship")
print("Good morning captain William and vice captain Diablo")
start_button = input("Do you want to start: ")


# Menu
def button():
    """
    This function is used as a main menu to call other functions
    :return: none
    """
    print("1. Check time and distance")
    print("2. Check fuel")
    print("3. Check health of spaceship")
    print("4. Check health of crew members")
    print("5. Exit")


if start_button == 'yes' or 'Yes':
    print("Menu")
    print(button())

choose = input("Which one do you want to see: ")
if choose == '1':
    from basic_info import distance_and_time_cal
    print(distance_and_time_cal(230000000, 11.11))
elif choose == '2':
    from basic_info import fuel_cal
    print(fuel_cal(100, 5))
elif choose == '3':
    from basic_info import spaceship_health
    print(spaceship_health(100, problems={"fan": 20, "heat": 30, "vision": 40, "radar": 40}))
elif choose == '4':
    from basic_info import health_of_crew_members
    print(health_of_crew_members(10))
else:
    print('Stop the process')
