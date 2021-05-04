import pytest
import src.exercise

def test_exercise():
    input_values = ["1","2"]
    input_values_stored = ["1","2"]
    output = []

    def mock_input(s=None):
        if s is not None:
            output.append(s)
            return input_values.pop(0)
        else:
            output.append("")
            return input_values.pop(0)

    src.exercise.input = mock_input
    src.exercise.print = lambda s : output.append(s)

    src.exercise.main()

    assert [output[0],output[1],output[2]] == ["Give the first number:",\
                                               "Give the second number:",\
                                               "The sum of the numbers is " + str(int(input_values_stored[0])+int(input_values_stored[1]))]
