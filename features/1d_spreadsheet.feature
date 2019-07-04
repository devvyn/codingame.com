# Created by devvyn-70504 at 2019-07-04
Feature: 1D Spreadsheet puzzle
  Calculation resolves correctly.

  Background: module loaded
    Given the script 1d_spreadsheet

  Scenario: Simple dependency
    When I send these inputs
      | line      |
      | VALUE 3 _ |
      | ADD $0 4  |

    Then I receive these outputs
      | line |
      | 3    |
      | 7    |