# run with: behave mh.feature

Feature: testing mh

  # test features of the mh interface
  Scenario: test import
    Given we have installed mh
    When we get the version
    Then we have a version

  Scenario: test a mh variable
    Given we have installed mh
    When we get a mh variable
    Then we get the correct value

  Scenario: test a mh function
    Given we have installed mh
    When we call a mh function
    Then we get the correct return

  Scenario: test calling a mh member function
    Given we have an mh object
    When we call a function
    Then we get the correct result

