from datetime import date

def calculate_age(birth_date):
    """
    Calculates the age in years based on the given birth date.
    
    Args:
        birth_date (date): The date of birth.
        
    Returns:
        int: The age in years.
    """
    today = date.today()
    age = today.year - birth_date.year
    
    # Adjust the age if the birthday hasn't occurred yet this year
    if today.month < birth_date.month or (today.month == birth_date.month and today.day < birth_date.day):
        age -= 1
    
    return age

if __name__ == "__main__":
    # Get the birth date from the user
    year = int(input("Enter your birth year: "))
    month = int(input("Enter your birth month: "))
    day = int(input("Enter your birth day: "))
    
    birth_date = date(year, month, day)
    
    # Calculate and print the age
    age = calculate_age(birth_date)
    print(f"Your age is: {age} years")
