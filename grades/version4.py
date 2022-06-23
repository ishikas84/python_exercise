from decimal import Decimal, ROUND_HALF_UP


def percent_to_grade(score, *, suffix=False, round=False):
    if round:
        score = Decimal(str(score)).quantize(Decimal('0'), rounding=ROUND_HALF_UP)
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


def calculate_gpa(grades):
    gpa_dict = {"A+": 4.33, "A": 4.0, "A-": 3.67,
                "B+": 3.33, "B": 3.00, "B-": 2.67,
                "C+": 2.33, "C": 2.00, "C-": 1.67,
                "D+": 1.33, "D": 1.00, "D-": 0.67,
                "F": 0
                }
    total_scores = sum(gpa_dict[grade] for grade in grades)
    return total_scores / len(grades)
