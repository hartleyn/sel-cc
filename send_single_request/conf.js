// conf.js
exports.config = {
  framework: 'jasmine',
  seleniumAddress: 'http://localhost:4444/wd/hub',
  specs: ['spec.js'],
  
  getPageTimeout: 60000,
  allScriptsTimeout: 500000,
  framework: 'custom',
  // path relative to the current config file
  frameworkPath: require.resolve('C:\\Program Files\\nodejs\\node_modules\\protractor-cucumber-framework'),
  capabilities: {
    'browserName': 'chrome'
  },

  // Spec patterns are relative to this directory.
  specs: [
    'features/*.feature'
  ],
  
  cucumberOpts: {
    require: 'features/step_definitions/stepDefinitions.js',
    tags: false,
    format: 'json:./reports/json/new_report.json',
    profile: false,
    'no-source': true
  }
}