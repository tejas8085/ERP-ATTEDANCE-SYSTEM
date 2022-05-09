def score_grade(score):
    if score <= 40:
        return "Fail"
    elif score <=60:
        return "C"
    elif score <=80:
        return "B"
    elif score <=90:
        return "A"
    else:
        return "O"
