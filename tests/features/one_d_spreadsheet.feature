# Created by devvyn-70504 at 2019-07-04
Feature: 1D Spreadsheet puzzle
  Calculation resolves correctly.

  Background:
    Given module loaded: one_d_spreadsheet

  Scenario: Simple dependency
    When the inputs are
      | in        |
      | VALUE 3 _ |
      | ADD $0 4  |
    Then the outputs are
      | out |
      | 3   |
      | 7   |

  Scenario: Double dependency
    When the inputs are
      | in         |
      | VALUE 20 _ |
      | ADD $0 100 |
      | ADD $1 1   |
    Then the outputs are
      | out |
      | 20  |
      | 120 |
      | 121 |

  Scenario: Subtraction
    When the inputs are
      | in         |
      | VALUE 12 _ |
      | SUB $0 3   |
    Then the outputs are
      | out |
      | 12  |
      | 9   |

  Scenario: Multiplication
    When the inputs are
      | in        |
      | VALUE 4 _ |
      | MULT 4 $0 |
    Then the outputs are
      | out |
      | 4   |
      | 16  |

  Scenario: No dependencies
    When the inputs are
      | in       |
      | ADD 1 2  |
      | SUB 3 1  |
      | MULT 2 4 |
    Then the outputs are
      | out |
      | 3   |
      | 2   |
      | 8   |

  Scenario: Coefficients
    When the inputs are
      | in         |
      | VALUE 10 _ |
      | VALUE 3 _  |
      | MULT $0 $1 |
      | VALUE 2 _  |
      | VALUE 4 _  |
      | MULT $3 $4 |
      | ADD $2 $5  |
    Then the outputs are
      | out |
      | 10  |
      | 3   |
      | 30  |
      | 2   |
      | 4   |
      | 8   |
      | 38  |

  Scenario: Fibonacci
    When the inputs are
      | in        |
      | VALUE 0 _ |
      | VALUE 1 _ |
      | ADD $0 $1 |
      | ADD $1 $2 |
      | ADD $2 $3 |
      | ADD $3 $4 |
      | ADD $4 $5 |
      | ADD $5 $6 |
      | ADD $6 $7 |
    Then the outputs are
      | out |
      | 0   |
      | 1   |
      | 1   |
      | 2   |
      | 3   |
      | 5   |
      | 8   |
      | 13  |
      | 21  |

  Scenario: Backward dependency
    When the inputs are
      | in         |
      | ADD $1 20  |
      | VALUE 32 _ |
    Then the outputs are
      | out |
      | 52  |
      | 32  |

  Scenario: Diamond dependency
    When the inputs are
      | in         |
      | SUB $1 4   |
      | VALUE 3 _  |
      | ADD 8 $1   |
      | MULT $0 $2 |
    Then the outputs are
      | out |
      | -1  |
      | 3   |
      | 11  |
      | -11 |

  Scenario: Accounting is easy
    When the inputs are
      | in         |
      | MULT $5 $2 |
      | ADD $5 $0  |
      | VALUE 12 _ |
      | ADD $2 $2  |
      | MULT $3 $2 |
      | SUB $3 $2  |
    Then the outputs are
      | out |
      | 144 |
      | 156 |
      | 12  |
      | 24  |
      | 288 |
      | 12  |

