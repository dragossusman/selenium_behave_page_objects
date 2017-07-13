Feature: run selenium tests using behave

Scenario: check the homepage opened correctly
Given auto1 homepage is opened in browser
Then check the title of the page

Scenario: open the home page, click BMW filter and check it was selected
When the bmw checkbox is clicked
Then the bmw filter appears selected

Scenario: open the home page, click BMW filter and verify only bmw cars are available in list
Then only bmw cars are displayed in list

Scenario: open the home page, click BMW filter and verify each car has an image
Then each car in list has images

Scenario: open the home page, click BMW filter and verify each car has complete information
Then each car in list has complete information