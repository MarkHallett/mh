
Feature: showing off behave

  Scenario: run a simple test
     Given we have behave installed
      When we implement a test
      Then behave will test it for us!


  @slow
  Scenario: run a slow test
     Given a set up
      When we run the test
      Then it will eventually pass
      # behave --tags=slow
      # behave --tags='not @slow'

  #@wip
  Scenario: current test
    Given a set up
    When we run the current test
    Then it will pass
    # behave -w      # runs wip tests in dev mode

  Scenario Outline: show outline feature
    Given a starting point <x>
    When we multiply by <y>
    Then the product will be <z>

    Examples: Simple
      | x   | y     | z   |
      | two | three | six |
      | three | two | six |


  Scenario: show step text
        Given a lot of data
          """
          a,b,c,d,
          """
        When we add more data
          """
          A,B,C,D
          """
        Then we have even more data
          """
          a,b,c,d,A,B,C,D
          """

  Scenario: show step table
    Given a table
      | name | cost | items |
      | apple | 3 | 4        |
      | pear | 4 | 5         |

    When we calculate the total value
     And we calculate the total items

    Then we get the totals
      |  total | value |
      |  items |  9    |
      |  value | 32    |

  Scenario: show params1
    Given a value "3"
     When squared
     Then the result is "9"

  Scenario: show params2
    Given a value "4"
    When squared
    Then the result is "16"




