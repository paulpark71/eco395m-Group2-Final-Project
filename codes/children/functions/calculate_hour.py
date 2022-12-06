"""
    Input: dataset on business hours in a week
    Output: total business hours in a week
"""


def calculate_hour(weekday):
    business_hours = [0, 0, 0, 0, 0, 0, 0]
    total = 0
    weeklist = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    ]
    for num, week in enumerate(weekday):
        l = weeklist[num]
        for e in week.split(","):
            Hour_end = 0
            Minitues_end = 0
            Hour_start = 0
            Minitues_start = 0
            if "Closed" in e:
                Hour_end = 0
                Minitues_end = 0
                Hour_start = 0
                Minitues_start = 0
                business_hours[num] = 0
            elif "Open 24 hours" in e:
                business_hours[num] = 24
            else:
                if "," in e:
                    Hour_end = 0
                    Minitues_end = 0
                    Hour_start = 0
                    Minitues_start = 0
                else:
                    start_time = (
                        e.replace(" ", "").replace(str(l + ":"), "").split("–")[0]
                    )
                    end_time = (
                        e.replace(" ", "").replace(str(l + ":"), "").split("–")[1]
                    )
                    if "AM" in start_time:
                        Hour_start = float(start_time.replace("AM", "").split(":")[0])
                        Minitues_start = (
                            float(start_time.replace("AM", "").split(":")[1]) / 60
                        )
                    elif "PM" in start_time:
                        Hour_start = (
                            float(start_time.replace("PM", "").split(":")[0]) + 12
                        )
                        Minitues_start = (
                            float(start_time.replace("PM", "").split(":")[1]) / 60
                        )
                    elif "AM" and "PM" not in start_time:
                        if "12" in start_time.split(":")[0]:
                            Hour_start = 12
                            Minitues_start = float(start_time.split(":")[1]) / 60
                        elif "AM" in end_time:
                            Hour_start = float(start_time.split(":")[0])
                            Minitues_start = float(start_time.split(":")[1]) / 60
                        elif "PM" in end_time:
                            Hour_start = float(start_time.split(":")[0]) + 12
                            Minitues_start = float(start_time.split(":")[1]) / 60
                    if "AM" in end_time:
                        Hour_end = float(end_time.replace("AM", "").split(":")[0])
                        Minitues_end = (
                            float(end_time.replace("AM", "").split(":")[1]) / 60
                        )
                    elif "PM" in end_time:
                        Hour_end = float(end_time.replace("PM", "").split(":")[0]) + 12
                        Minitues_end = (
                            float(end_time.replace("PM", "").split(":")[1]) / 60
                        )
                    business_hours[num] = (
                        (Hour_end + Minitues_end)
                        - (Hour_start + Minitues_start)
                        + business_hours[num]
                    )
    for e in business_hours:
        total = e + total
    return total
