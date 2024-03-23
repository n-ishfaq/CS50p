def convert(time_str):
    hours, minutes = map(int, time_str.split(':'))
    return hours + minutes / 60.0

def meal_time_check(time):
    breakfast_range = (7.0, 8.0)
    lunch_range = (12.0, 13.0)
    dinner_range = (18.0, 19.0)
    time_hours = convert(time)
    if breakfast_range[0] <= time_hours <= breakfast_range[1]:
        print("It's breakfast time!")
    elif lunch_range[0] <= time_hours <= lunch_range[1]:
        print("It's lunch time!")
    elif dinner_range[0] <= time_hours <= dinner_range[1]:
        print("It's dinner time!")

def main():
    time = input("Enter the current time (24-hour format, e.g., 07:30): ")
    meal_time_check(time)

if __name__ == "__main__":
    main()
