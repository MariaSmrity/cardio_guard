# Calculate risk points according to blood pressure
# Return risk points as an integer
def bp_risk(bp_sys, bp_dia):
    if bp_sys < 140 and bp_dia < 90:
        return 0
    elif bp_sys < 160 and bp_dia < 100:
        return 1
    elif bp_sys < 180 and bp_dia < 110:
        return 2
    else:
        return 3

# Calculate the combination risk of BMI and blood pressure
# Return the sum of both risks as an integer
def total_risk(bmi, bp_risk):
    if bp_risk == 0:
        if bmi >= 30:
            return 1
        else:
            return 0
    else:
        if bmi < 25:
            return bp_risk
        elif bmi < 30:
            return bp_risk + 1
        elif bmi < 35:
            return bp_risk + 2
        else:
            return bp_risk + 3
        
# Calculate the risk points of a patient
def calculate_risk(bmi, bp_sys, bp_dia):
    return total_risk(bmi, bp_risk(bp_sys, bp_dia))

