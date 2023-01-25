def study_schedule(permanence_period, target_time):
    counter = 0

    for start, end in permanence_period:
        if (start not in range(0, 24)) or (end not in range(0, 24)):
            return None

        if not target_time:
            return None

        if start <= target_time <= end:
            counter += 1

    return counter
