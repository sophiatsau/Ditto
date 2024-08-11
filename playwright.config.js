// playwright.config.js
import { devices } from "@playwright/test";

const frontendConfig = {
  testDir: "./tests/frontend",
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
    // Base URL to use in actions like `await page.goto('/')`.
    baseURL: "http://127.0.0.1:8000/",
    // run test without opening the browser
    headless: true,
    // ignore errors
    ignoreHTTPSErrors: true,
    // error logs for failed test
    trace: "on-first-retry",
  },
  projects: [
    {
      name: "chromium",
      use: { ...devices["Desktop Chrome"] },
    },
  ],
};

const backendConfig = {
  testDir: "./tests/backend",
  // untill timeout / failure
  timeout: 30000,
  // expectation(assertions)
  expect: {
    // max time to wait for assertions
    timeout: 5000,
  },
  // display the results , only uncomment when test are done being written bc its to troublesome if not
  // reporter: "html",
  // settings
  use: {
    // Base URL to use in actions like `await page.goto('/')`.
    baseURL: "http://127.0.0.1:8000/api",
    // run test without opening the browser
    headless: true,
    // ignore errors
    ignoreHTTPSErrors: true,
    // error logs for failed test
    trace: "on-first-retry",
  },
  projects: [
    {
      name: "chromium",
      use: { ...devices["Desktop Chrome"] },
    },
  ],
};

const selectedConfig =
  process.env.TEST_ENV === "backend" ? backendConfig : frontendConfig;

export default selectedConfig;
