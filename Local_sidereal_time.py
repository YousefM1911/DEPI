def calculate_julian_day(year, month, day):
    """
    Calculate the Julian Day (J0) for a given date at 0h UT using the formula from Boulet (1991).
    """
    # Apply the formula using integer division (//) instead of math.floor
    J0 = (367 * year - (7 * (year + (month + 9) // 12)) // 4  + (275 * month) // 9 + day + 1_721_013.5)
    return J0

def calculate_T0(J0):
    """
    Calculate T0, the number of Julian centuries since J2000.0.
    """
    T0 = (J0 - 2_451_545.0) / 36_525.0
    return T0

def calculate_theta_G0(T0):
    """
    Calculate the Greenwich Sidereal Time at 0h UT (θ_G0) in degrees.
    """
    theta_G0 = 100.4606184 + 36_000.77005361 * T0 + 0.000387933 * T0**2 - (T0**3) / 38_710_000
    theta_G0 = theta_G0 % 360  # Reduce modulo 360 to ensure 0° ≤ θ_G0 ≤ 360°
    return theta_G0

def calculate_theta_G(theta_G0, UT):
    """
    Calculate the Greenwich Sidereal Time at the given UT (θ_G) in degrees.
    """
    theta_G = theta_G0 + 1.002737909 * UT * 15  # Convert UT hours to degrees
    theta_G = theta_G % 360  # Reduce modulo 360 to ensure 0° ≤ θ_G ≤ 360°
    return theta_G

def calculate_local_sidereal_time(theta_G, longitude):
    """
    Calculate the Local Sidereal Time (θ) in degrees.
    """
    theta = theta_G + longitude
    theta = theta % 360  # Reduce modulo 360 to ensure 0° ≤ θ ≤ 360°
    return theta

def LST(year, month, day, ut, EL):
    """
    Calculate the Local Sidereal Time (LST) using Algorithm 5.3.
    """
    # Step 1: Compute J0
    J0 = calculate_julian_day(year, month, day)

    # Step 2: Calculate T0
    T0 = calculate_T0(J0)

    # Step 3: Compute θ_G0
    theta_G0 = calculate_theta_G0(T0)

    # Step 4: Calculate θ_G
    theta_G = calculate_theta_G(theta_G0, ut)

    # Step 5: Calculate the Local Sidereal Time θ
    theta = calculate_local_sidereal_time(theta_G, EL)

    return theta

def main():
    # User Inputs
    print("Enter the date (year, month, day):")
    year = int(input("Year: "))
    month = int(input("Month: "))
    day = int(input("Day: "))

    print("Enter the universal time (UT) in hours, minutes, seconds:")
    hour = int(input("Hour (0-23): "))
    minute = int(input("Minute (0-59): "))
    second = int(input("Second (0-59): "))

    print("Enter the longitude (degrees, minutes, seconds) and direction (E/W):")
    degrees = int(input("Degrees: "))
    minutes = int(input("Minutes: "))
    seconds = int(input("Seconds: "))
    direction = input("Direction (E/W): ").upper()

    # Convert longitude to decimal degrees
    EL = degrees + minutes / 60 + seconds / 3600
    if direction == 'W':
        EL = -EL  # West longitude is negative

    # Convert universal time to decimal hours
    ut = hour + minute / 60 + second / 3600

    # Calculate Local Sidereal Time (LST)
    lst_deg = LST(year, month, day, ut, EL)
    lst_hr = lst_deg / 15  # Convert LST from degrees to hours

    # Round outputs
    J0 = calculate_julian_day(year, month, day)
    lst_deg_rounded = round(lst_deg, 4)  
    lst_hr_rounded = round(lst_hr, 5)  

    # Output the results
    print("\n-----------------------------------------------------")
    print(" Local Sidereal Time Calculation")
    print("\n Input data:")
    print(f"\n Year = {year}")
    print(f" Month = {month}")
    print(f" Day = {day}")
    print(f" UT (hr) = {ut}")
    print(f" Longitude (deg) = {EL}")
    print("\n Intermediate Results:")
    print(f"\n Julian Day (J0) = {J0}")
    print("\n Solution:")
    print(f"\n Local Sidereal Time (deg) = {lst_deg_rounded}")
    print(f"\n Local Sidereal Time (hr) = {lst_hr_rounded}")

# Run the program
if __name__ == "__main__":
    main()