from typing import Generator, Iterable, Iterator, List
import sys
import re

def get_calculated_results(operations_text:Iterable[str])->Iterator[int]:

    def parse_operation(text:str)->tuple:
        operation = text.split(' ')
        return operation[0], tuple(operation[1:])


    def parse_arg(arg:str, results:list):
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
            'reference': lambda x: results[int(x)],  # FIXME: don't rely on external state
            'nothing': lambda x: None,
        }
        for arg_type, arg_value in arg_dict.items():
            return parsing_formulae[arg_type](arg_value)


    def calculate_operation(operator, args, results)->int:
        operation_formulae = {
            'VALUE': lambda x, y: x,
            'ADD': lambda x, y: x + y,
            'SUB': lambda x, y: x - y,
            'MULT': lambda x, y: x * y
        }
        return operation_formulae[operator](
            *(parse_arg(arg, results) for arg in args)
        )


    def calculate_operations(operations:Iterable)->List[int]:
        # @TODO: Here's where JIT evaluation is needed
        #   Especially where there's a loop here!
        results = []
        for operator, args in operations:
            result = calculate_operation(operator, args, results)
            results.append(result)
        return results


    operations = (parse_operation(string) for string in operations_text)
    return calculate_operations(operations)


def solve_1d_spreadsheet_puzzle():
    """ Solve the '1D Spreadsheet' puzzle on codingame.com. Read from stdin, print to stdout. """
    print(
        '\n'.join(
            (
                str(result) for result in get_calculated_results(
                    (
                        input()
                        for _ in range(int(input()))
                    )
                )
            )
        )
    )


if __name__ == '__main__':
    solve_1d_spreadsheet_puzzle()
