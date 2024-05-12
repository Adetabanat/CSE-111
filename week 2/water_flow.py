
def water_column_height(tower_height, tank_height):
    # Calculate the height of the water column using the given formula
    # height of the water column=h
    h = tower_height + (3 * tank_height) / 4
    return h

def pressure_gain_from_water_height(height):
    # Calculate the pressure caused by Earth's gravity on the water column
    #pressure caused by Earth's gravity = P
    P = (height * 998.2 * 9.80665) / 1000
    return P

def pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity):
    # Calculate the pressure loss due to friction within the pipe
    # pressure loss due=PL
    PL = (-friction_factor * pipe_length * 998.2 * fluid_velocity**2) / (2000 * pipe_diameter)
    return PL

def kpa_to_psi(pressure_kpa):
    # Convert pressure from kPa to psi
    pressure_psi = pressure_kpa * 0.1450377377
    return pressure_psi

EARTH_ACCELERATION_OF_GRAVITY = 9.8066500
WATER_DENSITY = 998.2000000
WATER_DYNAMIC_VISCOSITY = 0.0010016

def pressure_loss_from_fittings(fluid_velocity, quantity_fittings):
    lost_pressure = -0.04 * WATER_DENSITY * fluid_velocity**2 * quantity_fittings / 2000
    return lost_pressure


def reynolds_number(hydraulic_diameter, fluid_velocity):
    reynolds = WATER_DENSITY * hydraulic_diameter * fluid_velocity / WATER_DYNAMIC_VISCOSITY
    return reynolds



def pressure_loss_from_pipe_reduction(larger_diameter, fluid_velocity, reynolds_number, smaller_diameter):
   k1= 0.1 + 50 / reynolds_number 
   k2=(larger_diameter / smaller_diameter)**4-1
   k=k1*k2
   lost_pressure = (-k * WATER_DENSITY * fluid_velocity**2)/2000 
   return lost_pressure


PVC_SCHED80_INNER_DIAMETER = 0.28687 # (meters)  11.294 inches
PVC_SCHED80_FRICTION_FACTOR = 0.013  # (unitless)
SUPPLY_VELOCITY = 1.65               # (meters / second)

HDPE_SDR11_INNER_DIAMETER = 0.048692 # (meters)  1.917 inches
HDPE_SDR11_FRICTION_FACTOR = 0.018   # (unitless)
HOUSEHOLD_VELOCITY = 1.75            # (meters / second)


def main():
    tower_height = float(input("Height of water tower (meters): "))
    tank_height = float(input("Height of water tank walls (meters): "))
    length1 = float(input("Length of supply pipe from tank to lot (meters): "))
    quantity_angles = int(input("Number of 90° angles in supply pipe: "))
    length2 = float(input("Length of pipe from supply to house (meters): "))

    water_height = water_column_height(tower_height, tank_height)
    pressure = pressure_gain_from_water_height(water_height)

    diameter = PVC_SCHED80_INNER_DIAMETER
    friction = PVC_SCHED80_FRICTION_FACTOR
    velocity = SUPPLY_VELOCITY
    reynolds = reynolds_number(diameter, velocity)
    loss = pressure_loss_from_pipe(diameter, length1, friction, velocity)
    pressure += loss

    loss = pressure_loss_from_fittings(velocity, quantity_angles)
    pressure += loss

    loss = pressure_loss_from_pipe_reduction(diameter,
            velocity, reynolds, HDPE_SDR11_INNER_DIAMETER)
    pressure += loss

    diameter = HDPE_SDR11_INNER_DIAMETER
    friction = HDPE_SDR11_FRICTION_FACTOR
    velocity = HOUSEHOLD_VELOCITY
    loss = pressure_loss_from_pipe(diameter, length2, friction, velocity)
    pressure += loss

   

    # Convert pressure from kPa to psi
    pressure_psi = kpa_to_psi(pressure)
    pressure += loss

    print(f"Pressure at house: {pressure_psi:.1f} psi")
    print(f"Pressure at house: {pressure:.1f} kilopascals")


if __name__ == "__main__":
    main()