from behave import *

from one_d_spreadsheet import get_output_lines

use_step_matcher("parse")


@when("I send these inputs")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.input_lines = (line for line in context.table)


@then("I receive these outputs")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert context.table == get_output_lines(context.input_lines)  # FIXME: get text lines


@given("the script 1d_spreadsheet")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    # import
    pass