from behave import *

from one_d_spreadsheet import get_output_lines

use_step_matcher("parse")


@when("I send these inputs")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.input_lines = (line["line"] for line in context.table)


@then("I receive these outputs")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    for expected_line, actual_line in zip(
            (row["line"] for row in context.table),
            (str(line) for line in get_output_lines(context.input_lines))
    ):
        assert expected_line == actual_line

