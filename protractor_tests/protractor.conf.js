module.exports.config = {
    framework: 'custom',
    frameworkPath: 'node_modules/protractor-cucumber-framework',
    
    cucumberOpts: {
    format: ['json:reports/json/example.json'],
    require: ['features/support/**/*.js', 'features/step-definitions/**/*.js'],
    strict: true
    },
    
    capabilities: {
    browserName: 'chrome',
    specs: 'features/**/example.feature'
    },
    
    onPrepare: function () {
        browser.ignoreSynchronization = true;
        browser.manage().window().maximize();
    }
};
