//let {defineSupportCode} = require('cucumber');
const { Given, When, Then } = require("cucumber");
const fs = require('fs');
const chai  = require('chai');
const expect = chai.expect;
let num;


Given('I log {string}', function(line) {
  console.log(line)
});


When('I navigate to {string}', function(site) {
  return browser.get(site);
});


Then('the title should be {string}', function(title) {
  return expect(browser.getTitle()).to.eventually.eql(title);
});


Given('I go to {string}', async (string) => {

  let raw = fs.readFileSync('C:\\users\\nick.hartley\\desktop\\auto\\send_single_request\\request.json');
  let data = JSON.parse(raw);
  url = data.url;
  await browser.get(url);

});


Given('I accept terms and conditions', {timeout: 60*1000}, async () => {
    let checkbox = '#dialogContent_1 > div:nth-child(1) > div > md-checkbox';
    let button = '#dialogContent_1 > div.border_top.mt20.pt10.layout-row > button';

    browser.wait(ExpectedConditions.elementToBeClickable($(checkbox)), 60000);
    await $(checkbox).click();

    browser.wait(ExpectedConditions.elementToBeClickable($(button)), 60000);
    await $(button).click();
    /*browser.wait(ExpectedConditions.visibilityOf($('body > div.layout-fill.layout-column > md-content > app-content > div > div > div > ui-view > div.p10.layout-max-width.nowrap.sk-font.ng-scope > form > div > div.float_left.header_border.full_width > label:nth-child(6)'), 60000));
    await $('body > div.layout-fill.layout-column > md-content > app-content > div > div > div > ui-view > div.p10.layout-max-width.nowrap.sk-font.ng-scope > form > div > div.float_left.header_border.full_width > label:nth-child(6)').getText().then(function(text) {
    console.log(text);
    num = parseInt(text);
    });*/
});


Given('I click the "incomplete" link', {timeout: 60*1000}, async () => {
    await browser.sleep(3000);
    let incompleteLink = '#request-dashboard-incomplete-document-filter';

    browser.wait(ExpectedConditions.elementToBeClickable($(incompleteLink)), 60000);
    await $(incompleteLink).click();
});


Given('I click the "create" button', {timeout: 60*1000}, async () => {
    let incompleteLink = '#request-dashboard-incomplete-document-filter';
    let createButton = '#request-dashboard-create-certificate';

    browser.wait(ExpectedConditions.elementToBeClickable($(incompleteLink)), 60000);
    await $(incompleteLink).click();

    browser.wait(ExpectedConditions.elementToBeClickable($(createButton)), 60000);
    await $(createButton).click();
});


Given('I click the add a document link', {timeout: 60*1000}, async () => {
    let addDocumentLink = 'body > div.layout-fill.layout-column > md-content > app-content > div ' +
        '> div > div > ui-view > div.p10.layout-max-width.nowrap.sk-font.ng-scope > div.mt30 > div > a';

    browser.wait(ExpectedConditions.visibilityOf($(addDocumentLink), 60000));
    await $(addDocumentLink).click();
});


Given('I click the add a document button', {timeout: 60*1000}, async () => {
    let addDocumentButton = '#request-dashboard-add-any-document > button';

    browser.wait(ExpectedConditions.elementToBeClickable($(addDocumentButton), 60000));
    await $(addDocumentButton).click()
});


Given('I select a document type: {string}', {timeout: 60*1000}, async (type) => {
    let docTypeSelect = '#documents-create-doc-type-select';
    let option = '.ng-scope .md-ink-ripple';

    browser.wait(ExpectedConditions.elementToBeClickable($(docTypeSelect)), 60000);
    await $(docTypeSelect).click();

    browser.wait(ExpectedConditions.elementToBeClickable(element(by.cssContainingText(option, type))), 60000);
    await element(by.cssContainingText(option, type)).click();
});


Given('I select an exposure zone: {string}', {timeout: 60*1000}, async (zone) => {
    let exposureZoneSelect = '#documents-create-exposure-zone-select';
    let option = '.ng-scope .md-ink-ripple';

    browser.wait(ExpectedConditions.elementToBeClickable($(exposureZoneSelect)), 60000);
    await $(exposureZoneSelect).click();

    browser.wait(ExpectedConditions.elementToBeClickable(element(by.cssContainingText(option, zone))), 60000);
    await element(by.cssContainingText(option, zone)).click();
});



Given('I select an exempt reason: {string}', {timeout: 60*1000}, async (reason) => {
    await browser.sleep(3000);
    let exemptReasonSelect = '#documents-create-exempt-reason-select';
    let option = '.ng-scope .md-ink-ripple';

    browser.wait(ExpectedConditions.elementToBeClickable($(exemptReasonSelect)), 60000);
    await $(exemptReasonSelect).click();

    browser.wait(ExpectedConditions.elementToBeClickable(element(by.cssContainingText(option, reason))), 60000);
    await element(by.cssContainingText(option, reason)).click();
});


Given('I click next', {timeout: 60*1000}, async () => {
    let nextButton = 'body > div.layout-fill.layout-column > md-content > app-content > div > div > div > ui-view ' +
        '> div > div.layout-row.flex > md-card > form > div.layout-align-start-center.layout-row > button';

    browser.wait(ExpectedConditions.elementToBeClickable($(nextButton)), 60000);
    await $(nextButton).click();
});


Given('I switch to gencert iframe', {timeout: 60*1000}, async () => {
    browser.sleep(8000);
    let driver = browser.driver;
    let loc = by.css('#gencert_iframe');
    let el = driver.findElement(loc);
    //browser.refresh();
    driver.switchTo().frame(el);
});


Given('I complete the AGRICULTURE business information page, and click next', {timeout: 60*1000}, async () => {
    browser.sleep(5000);

    let selectOne = element(by.name('Is_this_certificate_being_used_for_a_single_transaction_or_as_a_blanket_certificate_')).element(by.model('field.selected_option'));
    let selectTwo = element(by.name('Choose_one_transaction_type_for_this_certificate')).element(by.model('field.selected_option'));
    let businessOfSellingField = element(by.name('I_am_engaged_in_the_business_of_selling')).$('div > input');
    let licenseNumberField = element(by.name('Purchaser_state_tax_id2')).$('div > input');
    let describePropertyField = element(by.name('Description_of_property_to_be_purchased')).$('div > input');
    let exemptionSelectField = element(by.name('Select_the_box_indicating_one_of_the_more_common_exemptions_below_or_use_the_other_options_to_cite_the_appropriate_authority_for_another_exemption_')).$('div > md-select');

    let optionOne = element(by.xpath('//body/div[3]/md-select-menu/md-content/md-option[1]'));
    let optionTwo = $('body > div:last-child > md-select-menu > md-content > md-option:nth-child(3)');
    let exemptionSelectOption = $('body > div:last-child > md-select-menu > md-content > md-option:nth-child(3)');

    let nextButton = $('#go_btn');


    browser.wait(ExpectedConditions.elementToBeClickable(selectOne), 60000);
    await selectOne.click();
    browser.wait(ExpectedConditions.elementToBeClickable(optionOne), 60000);
    await optionOne.click();


    browser.wait(ExpectedConditions.elementToBeClickable(selectTwo), 60000);
    await selectTwo.click();
    browser.wait(ExpectedConditions.elementToBeClickable(optionTwo), 60000);
    await optionTwo.click();


    browser.wait(ExpectedConditions.elementToBeClickable(businessOfSellingField), 60000);
    await businessOfSellingField.click();
    await businessOfSellingField.sendKeys('Things and stuff');


    browser.wait(ExpectedConditions.elementToBeClickable(licenseNumberField), 60000);
    await licenseNumberField.click();
    await licenseNumberField.sendKeys('246805648');


    browser.wait(ExpectedConditions.elementToBeClickable(describePropertyField), 60000);
    await describePropertyField.click();
    await describePropertyField.sendKeys('Resale');


    browser.wait(ExpectedConditions.elementToBeClickable(exemptionSelectField), 60000);
    await exemptionSelectField.click();
    browser.wait(ExpectedConditions.elementToBeClickable(exemptionSelectOption), 60000);
    await exemptionSelectOption.click();


    browser.wait(ExpectedConditions.elementToBeClickable(nextButton), 60000);
    await nextButton.click();
});


Given('I provide signer information on the signature page', {timeout: 60*1000}, async () => {
    let signerNameField = $('#signer_name');
    let signerTitleField = element(by.name('title'));


    browser.wait(ExpectedConditions.elementToBeClickable(signerNameField), 60000);
    await signerNameField.click();
    await signerNameField.sendKeys('Guy One');

    browser.wait(ExpectedConditions.elementToBeClickable(signerTitleField), 60000);
    await signerTitleField.click();
    await signerTitleField.sendKeys('Owner');
});


Given('I provide an expiration date on the signature page', {timeout: 60*1000}, async () => {
    let expirationDateField = element(by.model('expire_date')).$('div > input');


    browser.wait(ExpectedConditions.elementToBeClickable(expirationDateField), 60000);
    await expirationDateField.click();
    await expirationDateField.sendKeys('2022-01-01');  // YYYY-MM-DD

    await browser.actions().mouseMove({x: 200, y:0}).click().perform();
});


Given('I provide a signature on the signature page', {timeout: 60*1000}, async () => {
    let signatureCanvas = $('#gencert_signature > canvas');


    browser.wait(ExpectedConditions.visibilityOf(signatureCanvas, 60000));
    await browser.actions()
        .mouseMove(signatureCanvas)
        .mouseMove({x: -100, y: 0})
        .mouseDown()
        .mouseMove({x: 15,y: 17})
        .mouseMove({x: 15,y: -38})
        .mouseMove({x: -19,y: -10})
        .mouseMove({x: -7,y: 8})
        .mouseMove({x: 20,y: 15})
        .mouseMove({x: -7,y: 18})
        .mouseMove({x: 20,y: -20})
        .mouseUp()
        .perform();
    await browser.actions()
        .mouseMove({x: 10, y: 0})
        .mouseDown()
        .mouseMove({x: -8,y: 14})
        .mouseMove({x: 10,y: -25})
        .mouseMove({x: -12,y: 20})
        .mouseMove({x: -17,y: 8})
        .mouseMove({x: 20,y: -15})
        .mouseMove({x: -7,y: 12})
        .mouseMove({x: 10,y: -16})
        .mouseUp()
        .perform();
    await browser.actions()
        .mouseMove(signatureCanvas)
        .mouseMove({x: 20, y: 35})
        .click()
        .perform();
    await browser.sleep(2000);
});


Given('I click the next button on the signature page', {timeout: 60*1000}, async () => {
    let nextButton = $('#signer_go_btn');


    browser.wait(ExpectedConditions.elementToBeClickable(nextButton), 60000);
    await nextButton.click();

    await browser.sleep(3000);  // Exiting too quickly after clicking next stops certificate generation
});

// This only works with TAXABLE exempt reason
Given('I select a description, then click next', {timeout: 60*1000}, async () => {
    //browser.wait(ExpectedConditions.visibilityOf(element(by.css('#gencert_iframe')), 60000));
    browser.sleep(5000);
    let driver = browser.driver;
    let loc = by.css('#gencert_iframe');
    let el = driver.findElement(loc);
    //browser.refresh();
    driver.switchTo().frame(el);

    //driver.findElement(by.tagName('body')).sendKeys('my test string');

    let dropdownField = element(by.model('field.selected_option'));
    browser.wait(ExpectedConditions.elementToBeClickable(dropdownField), 60000);
    await dropdownField.click();

    let dropdownOption = 'option in field.options';
    browser.wait(ExpectedConditions.elementToBeClickable(element(by.repeater(dropdownOption).row(0))), 60000);
    await element(by.repeater(dropdownOption).row(0)).click();

    //let selectOption = '#select_option_365';
    //browser.wait(ExpectedConditions.elementToBeClickable($(selectOption)), 60000);
    //await $(selectOption).click();

    let goButton = '#go_btn';
    browser.wait(ExpectedConditions.elementToBeClickable($(goButton)), 60000);
    await $(goButton).click();
  
    //browser.switchTo().defaultContent();
    //browser.waitForAngular();
  
  //browser.wait(ExpectedConditions.elementToBeClickable($('#gencert > div > md-content > section > div > div.tab-pane.flex.active > div > md-card > md-card-footer > div > div > a'), 60000));
  //await $('#gencert > div > md-content > section > div > div.tab-pane.flex.active > div > md-card > md-card-footer > div > div > a').click();
  
  
  //browser.switchTo().defaultContent();
    //browser.waitForAngular();
});


Given('I complete the signature page, then click next', {timeout: 60*1000}, async () => {
    let signerNameInput = '#signer_name';
    let signerTitleInput = '#signerForm > div.gencert-fill > div:nth-child(2) > input';
    let signatureCanvas = '#gencert_signature > canvas';
    let submitButton = '#signer_go_btn';

    browser.wait(ExpectedConditions.elementToBeClickable($(signerNameInput), 60000));
    await $(signerNameInput).click();
    await $(signerNameInput).sendKeys('Guy One');

    browser.wait(ExpectedConditions.elementToBeClickable($(signerTitleInput), 60000));
    await $(signerTitleInput).click();
    await $(signerTitleInput).sendKeys('Owner');

    browser.wait(ExpectedConditions.visibilityOf($(signatureCanvas), 60000));
    await browser.actions()
        .mouseMove($(signatureCanvas))
        .mouseMove({x: -100, y: 0})
        .mouseDown()
        .mouseMove({x: 15,y: 17})
        .mouseMove({x: 15,y: -38})
        .mouseMove({x: -19,y: -10})
        .mouseMove({x: -7,y: 8})
        .mouseMove({x: 20,y: 15})
        .mouseMove({x: -7,y: 18})
        .mouseMove({x: 20,y: -20})
        .mouseUp()
        .perform();
    await browser.actions()
        .mouseMove({x: 10, y: 0})
        .mouseDown()
        .mouseMove({x: -8,y: 14})
        .mouseMove({x: 10,y: -25})
        .mouseMove({x: -12,y: 20})
        .mouseMove({x: -17,y: 8})
        .mouseMove({x: 20,y: -15})
        .mouseMove({x: -7,y: 12})
        .mouseMove({x: 10,y: -16})
        .mouseUp()
        .perform();
    await browser.actions()
        .mouseMove($(signatureCanvas))
        .mouseMove({x: 20, y: 35})
        .click()
        .perform();
    await browser.sleep(2000);

    browser.wait(ExpectedConditions.elementToBeClickable($(submitButton), 60000));
    await $(submitButton).click();
    browser.switchTo().defaultContent();
    browser.waitForAngular();
});


Given('I check for certificate creation', {timeout: 60*1000}, async () => {
    let docCount = 'body > div.layout-fill.layout-column > md-content > app-content > div > div > div > ui-view ' +
        '> div.p10.layout-max-width.nowrap.sk-font.ng-scope > form > div ' +
        '> div.float_left.header_border.full_width > label:nth-child(6)';

    browser.wait(ExpectedConditions.visibilityOf($(docCount), 60000));
    await $(docCount).getText().then(function(text) {
    expect(String(++num)).to.equal(text);
    });
});


Given('I proceed as guest', async () => {
    let termsAndConditionsCheckbox = "#dialogContent_12 > div.hide-sm.hide-xs.layout-align-center-stretch.layout-row > div:nth-child(3) > easy-create > div.easy-create.not-authenticated-dashboard-widget.proceed-as-guest.same-size.layout-column > form > div > md-checkbox > div.md-container.md-ink-ripple";
    let goButton = "#dialogContent_12 > div.hide-sm.hide-xs.layout-align-center-stretch.layout-row > div:nth-child(3) " +
        "> easy-create > div.easy-create.not-authenticated-dashboard-widget.proceed-as-guest.same-size.layout-column " +
        "> form > div > div.layout-align-end-center.layout-row > button";

    browser.wait(ExpectedConditions.visibilityOf($(termsAndConditionsCheckbox), 60000));
    await $(termsAndConditionsCheckbox).click();

    await browser.sleep(2000);
    await $(goButton).click();
});


Given('I select exposure zones', {timeout: 60*1000}, async () => {
    let exposureZoneSpan = "body > div.layout-fill.layout-column > md-content > div.main.ng-scope > div > ui-view > div > div.layout-align-space-between-stretch.layout-row > div.layout-align-start-start.layout-row > div.seller-description.layout-align-start-start.layout-column > div:nth-child(1) > span";
    let checkbox = "body > div.layout-fill.layout-column > md-content > div.main.ng-scope > div > ui-view > div " +
        "> form > div.x-overflow.dashboard-required > table.table-fill.hide-xs > tbody > tr:nth-child(1) " +
        "> td:nth-child(1) > md-checkbox > div.md-container.md-ink-ripple";
    let checkboxTwo = "body > div.layout-fill.layout-column > md-content > div.main.ng-scope > div > ui-view > div " +
        "> form > div.x-overflow.dashboard-required > table.table-fill.hide-xs > tbody > tr:nth-child(2) " +
        "> td:nth-child(1) > md-checkbox > div.md-container.md-ink-ripple";
    let button = 'body > div.layout-fill.layout-column > md-content > div.main.ng-scope > div > ui-view > div > form ' +
        '> div.layout-row > md-card:nth-child(1) > div.layout-align-space-between-end.layout-row > button';

    browser.wait(ExpectedConditions.visibilityOf($(exposureZoneSpan), 60000));

    await $(checkbox).click();

    await $(checkboxTwo).click();

    browser.wait(ExpectedConditions.visibilityOf($(button), 60000));
    await $(button).click();
  
});


Given('I click save and continue on the tax information page', {timeout: 60*1000}, async () => {
    let phoneNumber = 'gc_p_phone_number';

    browser.wait(ExpectedConditions.visibilityOf(element(by.id(phoneNumber)), 60000));
    await element(by.id(phoneNumber)).click();
});


Given('I retrieve campaign request code {string}', function(reqNum) {
  let number = parseInt(reqNum);
  number--;
  console.log(number);

  let raw = fs.readFileSync('C:\\users\\nick.hartley\\desktop\\auto\\campaigns\\requests.json');
  let data = JSON.parse(raw);
  let urls = data.urls;
  console.log(urls[number]);
  browser.get(urls[number]);
  browser.sleep(2000);
});


Given('I start campaign response', {timeout: 60*1000}, async () => {
  let raw = fs.readFileSync('C:\\users\\nick.hartley\\desktop\\auto\\campaigns\\requests.json');
  let data = JSON.parse(raw);
  let urls = data.urls;
  console.log(urls);

  for (let i = 0; i < urls.length; i++) {
    console.log(urls[i]);
  }

  browser.get('https://beta.certexpress.com/?r=mY-X9-RG-7L');
});


Given('I navigate to CertCapture', {timeout: 60*1000}, async () => {
    let raw = fs.readFileSync('C:\\users\\nick.hartley\\desktop\\auto\\test_assets\\test_config.json');
    let data = JSON.parse(raw);
    let cc_url = data.capture_env;

    browser.get(cc_url);
});


Given('I log into CertCapture', {timeout: 60*1000}, async () => {
    let loginField = '#email';
    let passwordField = '#password';
    let nextButton = '#sso_check_btn';
    let loginButton = '#login_btn';

    browser.wait(ExpectedConditions.visibilityOf($(loginField), 60000));
    await $(loginField).click();
    await $(loginField).sendKeys('hartley_automation');

    browser.wait(ExpectedConditions.visibilityOf($(nextButton), 60000));
    await $(nextButton).click();

    browser.wait(ExpectedConditions.visibilityOf($(passwordField), 60000));
    await $(passwordField).click();
    await $(passwordField).sendKeys('The@uto3ntry');

    browser.wait(ExpectedConditions.visibilityOf($(loginButton), 60000));
    await $(loginButton).click()
});


Given('I change account', {timeout: 60*1000}, async () => {
    let accountDropdown = '#dropdownCompanyButton';
    let accountInput = '#companyInput';
    let accountLink = '#company-drop > li:nth-child(1) > a:nth-child(1)';

    browser.wait(ExpectedConditions.elementToBeClickable($(accountDropdown), 60000));
    await $(accountDropdown).click();

    browser.wait(ExpectedConditions.visibilityOf($(accountInput), 60000));
    await $(accountInput).click();
    await $(accountInput).sendKeys('6_8_9_Smoke_Test_IE11');

    await browser.sleep(2000)

    await browser.actions().sendKeys(browser.Key.RETURN).perform();

    //browser.wait(ExpectedConditions.elementToBeClickable($(accountLink), 60000));
    //await $(accountLink).click();
});


Given('I navigate to retail', {timeout: 60*1000}, async () => {
    let retailLink = '#menu_container > ul > li:nth-child(8) > a';

    browser.wait(ExpectedConditions.elementToBeClickable($(retailLink), 60000));
    await $(retailLink).click();
});


Given('I close the retail search modal', {timeout: 60*1000}, async () => {
    let modalClose = '#exemption_search_modal_close';

    browser.wait(ExpectedConditions.elementToBeClickable($(modalClose), 60000));
    await $(modalClose).click();
});


Given('I click the new exemption button', {timeout: 60*1000}, async () => {
    let newExemption = '#show_customer_modal';

    browser.sleep(3000);

    browser.wait(ExpectedConditions.elementToBeClickable($(newExemption), 60000));
    await $(newExemption).click();
});


Given('I complete the new customer form and click next', {timeout: 60*1000}, async () => {
    let nameOfBusiness = '#CustomerName';
    let addressLine1 = '#CustomerAddressLine1';
    let businessCity = '#CustomerCity';
    let businessState = '#CustomerStateId';
    let colorado = '#CustomerStateId > option:nth-child(11)'
    let businessZipCode = '#CustomerZip';
    let nextButton = '#add_customer_btn';

    await browser.sleep(2000);

    browser.wait(ExpectedConditions.visibilityOf($(nameOfBusiness), 60000));
    await $(nameOfBusiness).click();
    await $(nameOfBusiness).sendKeys('Jane Doe');


    browser.wait(ExpectedConditions.visibilityOf($(addressLine1), 60000));
    await $(addressLine1).click();
    await $(addressLine1).sendKeys('1 1st st');

    //await browser.sleep(2000);

    browser.wait(ExpectedConditions.visibilityOf($(businessCity), 60000));
    await $(businessCity).click();
    await $(businessCity).sendKeys('New York');

    //await browser.sleep(2000);

    browser.wait(ExpectedConditions.visibilityOf($(businessState), 60000));
    await $(businessState).click();

    //await browser.sleep(2000);

    browser.wait(ExpectedConditions.visibilityOf($(colorado), 60000));
    await $(colorado).click();

    //await browser.sleep(2000);

    browser.wait(ExpectedConditions.visibilityOf($(businessZipCode), 60000));
    await $(businessZipCode).click();
    await $(businessZipCode).sendKeys('10038');

    //await browser.sleep(2000);

    browser.wait(ExpectedConditions.visibilityOf($(nextButton), 60000));
    await $(nextButton).click();
});


Given('I select a retail document type', {timeout: 60*1000}, async () => {
    let dropdown = '#doc_type_selector';
    let docType = '#doc_type_selector > option:nth-child(3)';

    browser.wait(ExpectedConditions.visibilityOf($(dropdown), 60000));
    await $(dropdown).click();

    browser.wait(ExpectedConditions.visibilityOf($(docType), 60000));
    await $(docType).click();
});


Given('I select a retail jurisdiction', {timeout: 60*1000}, async () => {
    let dropdown = '#set_zone';
    let arizona = '#set_zone > option:nth-child(3)';

    //await browser.sleep(2000);

    browser.wait(ExpectedConditions.visibilityOf($(dropdown), 60000));
    await $(dropdown).click();

    browser.wait(ExpectedConditions.visibilityOf($(arizona), 60000));
    await $(arizona).click();

    /*
    await browser.sleep(2000);

    await browser.actions()
        .mouseMove($(dropdown))
        .mouseMove({x: 0, y: -20})
        .click()
        .perform();

    await browser.sleep(2000);
    */
});



Given('I switch to retail iframe and click "Save and Continue"', {timeout: 60*1000}, async () => {
    await browser.sleep(5000);

    let loc = by.css('#gencert_iframe');
    let el = browser.driver.findElement(loc);
    await browser.driver.switchTo().frame(el);

    await browser.sleep(2000);

    let saveAndContinue = '#purchaserForm > md-card-footer > div > button:nth-child(2)';
    browser.wait(ExpectedConditions.elementToBeClickable($(saveAndContinue), 60000));
    await $(saveAndContinue).click();
});


Given('I select a retail exempt reason', {timeout: 60*1000}, async () => {
    let taxableButton = '#gcform > div.ng-scope > md-list > md-list-item:nth-child(1) > div > button';

    browser.wait(ExpectedConditions.visibilityOf($(taxableButton), 60000));
    await $(taxableButton).click();
});


Given('I select a taxable purchase reason and click "Save and Continue"', {timeout: 60*1000}, async () => {
    let dropdown = '//*[@id="certificate_form"]/div/div/div[2]/div/div/div/ng-form/md-input-container/md-select';
    let reason = 'option in field.options';
    let saveAndContinue = '#gencert > div > md-content > section > div > div.tab-pane.flex.active > div > md-card ' +
        '> md-card-footer > div.hide-xs.layout-align-end-center.layout-row > div > button:nth-child(2)';

    await browser.sleep(2000);

    browser.wait(ExpectedConditions.elementToBeClickable(element(by.xpath(dropdown)), 60000));
    await element(by.xpath(dropdown)).click();

    browser.wait(ExpectedConditions.elementToBeClickable(element(by.repeater(reason).row(0)), 60000));
    await element(by.repeater(reason).row(0)).click();

    browser.wait(ExpectedConditions.visibilityOf($(saveAndContinue), 60000));
    await $(saveAndContinue).click();
});


Given('I complete the retail signature page and click "Save and Continue"', {timeout: 60*1000}, async () => {
    let signerName = '#signer_name';
    let signerTitle = '#input_405';
    let signatureCanvas = '#gencert_signature > canvas';
    let saveAndContinue = '#signerForm > div.hide-xs.layout-align-end-center.layout-row > button:nth-child(3)';

    // Wait 10 seconds to compensate for long loading time
    await browser.sleep(10000);

    browser.wait(ExpectedConditions.visibilityOf($(signerName), 60000));
    await $(signerName).click();
    await $(signerName).sendKeys('Guy One');

    browser.wait(ExpectedConditions.visibilityOf($(signerTitle), 60000));
    await $(signerTitle).click();
    await $(signerTitle).sendKeys('Owner');

    browser.wait(ExpectedConditions.visibilityOf($(signatureCanvas), 60000));
    await browser.actions()
        .mouseMove($(signatureCanvas))
        .mouseMove({x: -100, y: 0})
        .mouseDown()
        .mouseMove({x: 15,y: 17})
        .mouseMove({x: 15,y: -38})
        .mouseMove({x: -19,y: -10})
        .mouseMove({x: -7,y: 8})
        .mouseMove({x: 20,y: 15})
        .mouseMove({x: -7,y: 18})
        .mouseMove({x: 20,y: -20})
        .mouseUp()
        .perform();
    await browser.actions()
        .mouseMove({x: 10, y: 0})
        .mouseDown()
        .mouseMove({x: -8,y: 14})
        .mouseMove({x: 10,y: -25})
        .mouseMove({x: -12,y: 20})
        .mouseMove({x: -17,y: 8})
        .mouseMove({x: 20,y: -15})
        .mouseMove({x: -7,y: 12})
        .mouseMove({x: 10,y: -16})
        .mouseUp()
        .perform();
    await browser.actions()
        .mouseMove($(signatureCanvas))
        .mouseMove({x: 20, y: 35})
        .click()
        .perform();
    await browser.sleep(2000);

    browser.wait(ExpectedConditions.visibilityOf($(saveAndContinue), 60000));
    await $(saveAndContinue).click();
});


Given('I close retail creation success modal', {timeout: 60*1000}, async () => {
    let close = '#creation_results_modal > div > div > div.modal-header.dynamic-align > button';

    // Wait 25 seconds to compensate for document processing time
    await browser.sleep(25000);

    await browser.driver.switchTo().defaultContent();

    browser.wait(ExpectedConditions.elementToBeClickable($(close), 60000));
    await $(close).click();
});
