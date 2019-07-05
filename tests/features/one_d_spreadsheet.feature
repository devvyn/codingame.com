# Created by devvyn-70504 at 2019-07-04
Feature: 1D Spreadsheet puzzle
  Calculation resolves correctly.

  Background: one_d_spreadsheet module
    Given module loaded: one_d_spreadsheet

  Scenario: Simple dependency
    When I send these inputs
      | line      |
      | VALUE 3 _ |
      | ADD $0 4  |
    Then I receive these outputs
      | line |
      | 3    |
      | 7    |

  Scenario: Double dependency
    When I send these inputs
      | line       |
      | VALUE 20 _ |
      | ADD $0 100 |
      | ADD $1 1   |
    Then I receive these outputs
      | line |
      | 20   |
      | 120  |
      | 121  |

  Scenario: Subtraction
    When I send these inputs
      | line       |
      | VALUE 12 _ |
      | SUB $0 3   |
    Then I receive these outputs
      | line |
      | 12   |
      | 9    |
