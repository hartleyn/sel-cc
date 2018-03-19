// spec.js
describe('Protractor Demo App', function() {
	const fs = require('fs');
	
	let raw = fs.readFileSync('C:\\users\\nick.hartley\\desktop\\auto\\send_single_request\\request.json');
	let data = JSON.parse(raw);
	url = data.url
	console.log(url);

	it('Ensure that a certificate can be created from request code.', function() {
		browser.get(url);
		
		//expect(browser.getTitle()).toEqual('Super Calculator');
		
	});
});