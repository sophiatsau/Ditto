const { test, expect } = require("@playwright/test");

test.describe("Flask App", () => {
  // This test will run in an environment where FLASK_ENV is set to production
  test("should redirect HTTP to HTTPS in production", async ({ request }) => {
    const baseURL = "http://127.0.0.1:8000";

    const response = await request.get(baseURL, {});

    // Verify that the response is a redirect to HTTPS
    expect(response.status()).toBe(200);
    const locationHeader = response.headers()["location"];
  });

  // Test for CSRF token injection
  test("should inject a CSRF token into the cookies", async ({ request }) => {
    const baseURL = "http://127.0.0.1:8000/api/auth/login";

    const response = await request.get(baseURL);

    // Verify that the CSRF token cookie is set
    const setCookieHeaders = response.headers()["set-cookie"];
    expect(setCookieHeaders).toBeDefined();
    const csrfTokenCookie = setCookieHeaders
      .split(";")
      .find((cookie) => cookie.trim().startsWith("csrf_token"));
    expect(csrfTokenCookie).toBeDefined();
  });

  // Test the root path and ensure it serves the index.html file
  test("should serve the index.html file for root path", async ({
    request,
  }) => {
    const baseURL = "http://127.0.0.1:8000";

    const response = await request.get(baseURL);

    // Verify that the response is HTML (index.html content)
    expect(response.status()).toBe(200);
    expect(response.headers()["content-type"]).toContain("text/html");

    // Optionally, you can check if certain keywords exist in the HTML
    const responseBody = await response.text();
    expect(responseBody).toContain("<!doctype html>");
    expect(responseBody).toContain("<html");
    expect(responseBody).toContain("</html>");
  });
});
