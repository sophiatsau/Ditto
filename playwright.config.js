// playwright.config.js
module.exports = {
  // where to look for test
  testDir: "./tests",
  // untill timeout / failure
  timeout: 30000,
  // expectation(assertions)
  expect: {
    // max time to wait for assertions
    timeout: 5000,
  },
  // display the results
  reporter: "html",
  // settings
  use: {
    // run test without opening the browser
    headless: true,
    // ignore errors
    ignoreHTTPSErrors: true,
    // error logs for failed test
    trace: "on-first-retry",
  },
};
