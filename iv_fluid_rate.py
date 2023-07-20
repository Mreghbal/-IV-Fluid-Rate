def iv_fluid_rate(weight, age, drop_factor, infusion_time, blood_loss, maintenance_rate):
    """
    Calculate the IV fluid rate based on various parameters including weight, age, drop factor,
    infusion time, blood loss, and maintenance rate.
    
    Parameters:
        - weight (float): The patient's weight in kilograms.
        - age (int): The patient's age in years.
        - drop_factor (int): The drop factor in drops per milliliter.
        - infusion_time (int): The desired infusion time in minutes.
        - blood_loss (float): The estimated blood loss in milliliters.
        - maintenance_rate (float): The maintenance fluid rate in milliliters per kilogram per hour.
    
    Returns:
        - float: The total IV fluid rate in milliliters per hour.
    """
    # Convert weight to grams
    weight_g = weight * 1000
    
    # Calculate the infusion volume in milliliters
    infusion_volume_ml = weight_g * 0.03 + blood_loss
    
    # Calculate the maintenance fluid volume in milliliters
    maintenance_volume_ml = weight * maintenance_rate * infusion_time / 60
    
    # Calculate the total fluid volume in milliliters
    total_volume_ml = infusion_volume_ml + maintenance_volume_ml
    
    # Calculate the infusion time in hours
    infusion_time_h = infusion_time / 60
    
    # Calculate the IV fluid rate in milliliters per hour
    iv_rate_ml_h = total_volume_ml / infusion_time_h
    
    # Calculate the number of drops per minute
    drops_per_min = iv_rate_ml_h * drop_factor / 60
    
    return iv_rate_ml_h, drops_per_min


# Example usage
weight = 70.5 # Weight in kilograms
age = 35 # Age in years
drop_factor = 20 # Drop factor in drops per milliliter
infusion_time = 90 # Infusion time in minutes
blood_loss = 250 # Estimated blood loss in milliliters
maintenance_rate = 4 # Maintenance fluid rate in milliliters per kilogram per hour

iv_rate_ml_h, drops_per_min = iv_fluid_rate(weight, age, drop_factor, infusion_time, blood_loss, maintenance_rate)

print(f"IV Fluid Rate: {iv_rate_ml_h} mL/h")
print(f"Drops per Minute: {drops_per_min} drops/min")
