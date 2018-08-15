# Created by Nick.Hartley at 5/25/2018
Feature: Creating a certificate in the retail portal of CertCapture
  As a user of CertCapture
  I should be able to utilize the retail portal
  In order to create a certificate

  Scenario: I create a certificate via retail
    Given I navigate to CertCapture
    And I log into CertCapture
    And I navigate to retail
    And I close the retail search modal
    And I click the new exemption button
    Then I complete the new customer form and click next
    And I select a retail jurisdiction
    And I switch to retail iframe and click "Save and Continue"
    And I select a retail exempt reason
    Then I select a taxable purchase reason and click "Save and Continue"
    And I complete the retail signature page and click "Save and Continue"
    Then I close retail creation success modal
