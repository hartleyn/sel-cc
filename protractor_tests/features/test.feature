#features/test.feature
Feature: Running Cucumber with Protractor
    As a user of Protractor
    I should be able to use Cucumber
    In order to run my E2E tests

    Scenario: I create the first certificate
        Given I retrieve campaign request code "1"
        And I accept terms and conditions
        And I click the "incomplete" link
        And I click the "create" button
        And I select an exempt reason: "AGRICULTURE"
        And I click next
        And I switch to gencert iframe
        And I complete the AGRICULTURE business information page, and click next
        And I provide signer information on the signature page
        And I provide an expiration date on the signature page
        And I provide a signature on the signature page
        And I click the next button on the signature page
