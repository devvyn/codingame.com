import re
from typing import Callable, Generator, Iterable, Iterator, List, Union, Tuple


def get_output_lines(operations_text: Iterable[str]) -> Iterator[int]:
    def parse_operation(text: str) -> Tuple[str, Tuple[str, ...]]:
        operation = text.split(' ')
        return operation[0], tuple(operation[1:])

    def calculate_operations(operation_iterable: Iterable) -> List[int]:

        def calculate_operation(operator_arg, calculation_args, results_state) -> int:

            arg_parse_call_arg = Union[Generator[int, None, None], int, None]
            arg_parse_callable = Callable[[str], arg_parse_call_arg]
            arg_parse_call = Tuple[arg_parse_callable, arg_parse_call_arg]

            def parse_arg(arg: str, results_state_parse_arg: list) -> arg_parse_call:
                def resolve_reference(index: int, results_state_resolve: list):
                    yield results_state_resolve[index]

                arg_dict = {
                    key: value for key, value in
                    (re.compile(r'(?P<number>-?[0-9]+)|(?:\$)(?P<reference>[0-9]+)|(?P<nothing>_)')
                     .fullmatch(arg)
                     .groupdict()
                     .items())
                    if value is not None
                }
                # @TODO: Here's where JIT evaluation is needed
                parsing_formulae = {
                    'number': lambda x: int(x),
                    'reference': lambda x: next(resolve_reference(int(x), results_state_parse_arg)),
                    # FIXME: don't rely on external state
                    'nothing': lambda _: None,
                }
                for arg_type, arg_value in arg_dict.items():
                    return parsing_formulae[arg_type], arg_value  # Return first (and only)

            def evaluate_generator(parse_arg_call: arg_parse_call):
                return [callable_obj(argument) for callable_obj, argument in parse_arg_call][0]

            operation_formulae = {
                'VALUE': lambda x, y: x,
                'ADD': lambda x, y: x + y,
                'SUB': lambda x, y: x - y,
                'MULT': lambda x, y: x * y
            }
            return (
                operation_formulae[operator_arg](
                    *(
                        evaluate_generator(parse_arg(arg, results_state))
                        for arg in calculation_args
                    )
                )
            )

        # @TODO: Here's where JIT evaluation is needed
        #   Especially where there's a loop here!
        results = []
        for operator, args in operation_iterable:
            results.append(calculate_operation(operator, args, results))
        return results

    operations = (
        parse_operation(string)
        for string in operations_text
    )
    return calculate_operations(operations)


def solve_1d_spreadsheet_puzzle():
    """ Solve the '1D Spreadsheet' puzzle on codingame.com.
    https://www.codingame.com/ide/puzzle/1d-spreadsheet

    Read from stdin, print to stdout.
    """
    print(
        '\n'.join(
            (
                str(result) for result
                in get_output_lines((input() for _ in range(int(input()))))
            )
        )
    )


if __name__ == '__main__':
    solve_1d_spreadsheet_puzzle()
