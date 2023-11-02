import Lab2.Excercise1.bmi as bmi


print("test_bmi")


def test_bmi_normal_weight():
    test = 0

    result = bmi.calculate_bmi(1.2, 30)

    assert (result == test)


def test_bmi_over_weight():
    test = 1

    result = bmi.calculate_bmi(1.2, 50)

    assert (result == test)


def test_bmi_under_weight():
    test = -1

    result = bmi.calculate_bmi(1.2, 25)

    assert (result == test)
