from behave import *

from one_d_spreadsheet import get_output_lines


@when("I receive")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.input_lines = (row["in"] for row in context.table)


@then("I send")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    for expected_line, actual_line in zip(
            (row["out"] for row in context.table),
            (str(line) for line in get_output_lines(context.input_lines))
    ):
        assert expected_line == actual_line
