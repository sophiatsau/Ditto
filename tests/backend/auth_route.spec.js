const { test, expect, request } = require("@playwright/test");

test("should login a user", async ({ request }) => {
  const baseURL = "http://127.0.0.1:8000/api";

  // Retrieve CSRF token by making an initial request to get the cookie
  const csrfTokenResponse = await request.get(`${baseURL}/auth/unauthorized`); // Adjust the route if necessary
  const setCookieHeaders = csrfTokenResponse.headers()["set-cookie"];

  if (!setCookieHeaders) {
    throw new Error("No set-cookie headers found");
  }

  const csrfToken = setCookieHeaders
    .split(";")
    .find((cookie) => cookie.trim().startsWith("csrf_token"))
    .split("=")[1];

  // Define login credentials
  const loginPayload = {
    email: "demo@aa.io",
    password: "password",
    csrf_token: csrfToken,
  };

  // Send login request
  const loginResponse = await request.post(`${baseURL}/api/auth/login`, {
    headers: {
      "Content-Type": "application/json",
      "X-CSRF-Token": csrfToken,
      Cookie: `csrf_token=${csrfToken}`,
    },
    data: JSON.stringify(loginPayload),
  });

  // Verify response
  expect(loginResponse.status()).toBe(200);
  const loginData = await loginResponse.json();
  expect(loginData).toHaveProperty("id"); // Adjust based on your user model
  expect(loginData).toHaveProperty("email", "test@example.com");
});
