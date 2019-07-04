from typing import Callable, Generator, Iterable, Iterator, List, Union, Tuple
import sys
import re

def get_calculated_results(operations_text:Iterable[str])->Iterator[int]:

    def parse_operation(text:str)->Tuple[str, str, str]:
        operation = text.split(' ')
        return operation[0], tuple(operation[1:])



    def calculate_operations(operations:Iterable)->List[int]:
        
        def calculate_operation(operator, args, results)->int:
            
            ArgParseCallArg = Union[Generator[int, None, None], int, None]
            ArgParseCallable = Callable[[str], ArgParseCallArg]
            ArgParseCall = Tuple[ArgParseCallable, ArgParseCallArg]
            
            def parse_arg(arg:str, results:list) -> ArgParseCall:
                
                def resolve_reference(index:int, results:list) -> int:
                    yield results[index]
                
                
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
                    'reference': lambda x: next(resolve_reference(int(x), results)),  # FIXME: don't rely on external state
                    'nothing': lambda _: None,
                }
                for arg_type, arg_values in arg_dict.items():
                    return (parsing_formulae[arg_type], arg_value)  # Return first (and only)
                
                
            def evaluate_generator(parse_arg_call:ArgParseCall):
                return [callable(argument) for callable, argument in parse_arg_call][0]
            
            
            operation_formulae = {
                'VALUE': lambda x, y: x,
                'ADD': lambda x, y: x + y,
                'SUB': lambda x, y: x - y,
                'MULT': lambda x, y: x * y
            }
            return (
                operation_formulae[operator](
                    *(
                        evaluate_generator(parse_arg(arg, results))
                        for arg in args
                    )
                )
            )


        # @TODO: Here's where JIT evaluation is needed
        #   Especially where there's a loop here!
        results = []
        for operator, args in operations:
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
