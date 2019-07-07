from behave import *


@when("the inputs are")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.input_lines = (row["in"] for row in context.table)


@then("the outputs are")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    for expected_line, actual_line in zip(
            (row["out"] for row in context.table),
            (str(line) for line in context.get_output_lines(context.input_lines))
    ):
        assert expected_line == actual_line
