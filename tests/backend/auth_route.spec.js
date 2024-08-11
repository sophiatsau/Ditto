const { test, expect } = require("@playwright/test");

test.describe("Flask App", () => {
  // endpoint auth is located
  const baseURL = "http://127.0.0.1:8000";

  test("should Authenticates a user.", async ({ request }) => {
    const response = await request.get(`${baseURL}/api/`, {});
    console.log("=========".repeat(4));
    console.log("response: ", response);
    console.log("=========".repeat(4));

    expect(response.status()).toBe(200);
    expect(response)
  });
});
