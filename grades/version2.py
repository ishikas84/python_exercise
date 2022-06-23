def percent_to_grade(score, *, suffix=False):
    score_dict = {"A+": 97, "A": 93, "A-": 90,
                  "B+": 87, "B": 83, "B-": 80,
                  "C+": 77, "C": 73, "C-": 70,
                  "D+": 67, "D": 63, "D-": 60,
                  }
    values = score_dict.values()
    keys = list(score_dict.keys())
    for i, value in enumerate(values):
        if value <= score:
            break
    if score < 60:
        return "F"
    return keys[i] if suffix else keys[i][0]
