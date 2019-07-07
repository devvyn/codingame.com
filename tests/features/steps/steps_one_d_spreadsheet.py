from behave import given

# noinspection PyUnresolvedReferences
import tests.steps_io


@given("module loaded: one_d_spreadsheet")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    from one_d_spreadsheet import get_output_lines
    context.get_output_lines = get_output_lines
