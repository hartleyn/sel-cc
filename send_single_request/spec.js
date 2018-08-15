// spec.js
describe('Create certificate from request code', function() {
	const fs = require('fs');
	
	let raw = fs.readFileSync('C:\\users\\nick.hartley\\desktop\\auto\\send_single_request\\request.json');
	let data = JSON.parse(raw);
	url = data.url
	console.log(url);
	
	var clickButton = function(elem) {
		elem.click()
		browser.sleep(5000)
	}
	
	it('Ensure that a certificate can be created from request code', function() {
		browser.get(url);
		browser.manage().window().maximize()
		
		var elem = element(by.xpath('//*[@id="dialogContent_12"]/div[3]/div[3]/easy-create/div[3]/form/div/md-checkbox/div[1]'))
		elem.click();
	
		//browser.sleep(5000)
		element(by.xpath('//md-dialog-content[@id="dialogContent_12"]/div[3]/div[3]/easy-create/div[3]/form/div/div[3]/button')).click();
		
		//browser.sleep(5000);
		
		element(by.xpath('/html/body/div[1]/md-content/div[1]/div/ui-view/div/form/div[1]/table[1]/tbody')).all(by.repeater('certificateOrExposure in dashboard')).all(by.tagName('md-checkbox')).each(function(box) {
			box.click();
			browser.sleep(3000);
		});
		
		var button = element(by.xpath('/html/body/div[1]/md-content/div[1]/div/ui-view/div/form/div[3]/md-card[1]/div[2]/button'))
		browser.call(clickButton, button)
		
	});
	
	
	
	/*
	it('Ensure that the "SAVE AND CONTINUE" button can be clicked', function() {
		//console.log('trying to click first button');
		
		var button = element(by.xpath('/html/body/div[1]/md-content/div[1]/div/ui-view/div/form/div[3]/md-card[1]/div[2]/button/span'))
		button.click()
		
		browser.sleep(3000);
	});
	
	
	
	it('Ensure that the "SAVE AND CONTINUE" button can be clicked', function() {
		//browser.sleep(3000);
		element.all(by.id('purchaser_go_btn')).all(by.tagName('span')).each(function(box) {
			box.click()
		});
		
	});
	
	it('Ensure that an exempt reason can be selected', function() {
		browser.sleep(8000);
		browser.sleep(2000);
		element(by.xpath('//form[@id="gcform"]/div[1]/md-list/md-list-item[1]/div/button')).click()
		browser.sleep(3000);
	});
	*/
});