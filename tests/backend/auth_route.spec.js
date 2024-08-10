const { test, expect, request } = require("@playwright/test");

test("should login a user", async ({ request }) => {
  const baseURL = "http://127.0.0.1:8000";

  // Retrieve CSRF token by making an initial request to get the cookie
  const csrfTokenResponse = await request.get(
    `${baseURL}/api/auth/unauthorized`
  ); // Adjust the route if necessary
  const setCookieHeaders = csrfTokenResponse.headers()["set-cookie"];

  // console.log("set-cookie headers:", setCookieHeaders.split(";").find((cookie) => cookie.trim().startsWith("csrf_token")).split("=")[1]);

  if (!setCookieHeaders) {
    throw new Error("No set-cookie headers found");
  }

  const csrfToken = setCookieHeaders
    .split(";")
    .find((cookie) => cookie.trim().startsWith("csrf_token"))
    .split("=")[1];

  console.log("=".repeat(10));
  console.log("CSRF Token:", csrfToken);

  // Define login credentials
  const loginPayload = {
    email: "demo@aa.io",
    password: "password",
    csrf_token: csrfToken,
  };

  console.log("=".repeat(10));
  console.log("Login Payload:", loginPayload);

  // Send login request
  const loginResponse = await request.post(`${baseURL}/api/auth/login`, {
    headers: {
      "Content-Type": "application/json",
      "X-CSRF-Token": csrfToken,
      Cookie: `csrf_token=${csrfToken}`,
    },
    data: JSON.stringify(loginPayload),
  });
  console.log("=".repeat(10));
  console.log("Login Response Status:", loginResponse.status());
  console.log("=".repeat(10));
  console.log("Login Response Headers:", loginResponse.headers());
  console.log("=".repeat(10));
  console.log("Login Response Body:", await loginResponse.text());
  console.log("=".repeat(10));

  // Verify response
  expect(loginResponse.status()).toBe(200);
  const loginData = await loginResponse.json();
  expect(loginData).toHaveProperty("id"); // Adjust based on your user model
  expect(loginData).toHaveProperty("email", "test@example.com");
});

// test("should fail to login with incorrect credentials", async ({ request }) => {
//   const baseURL = "http://127.0.0.1:3000";

//   // Retrieve CSRF token
//   const csrfTokenResponse = await request.get(
//     `${baseURL}/api/auth/unauthorized`
//   ); // Adjust the route if necessary
//   const setCookieHeader = csrfTokenResponse.headers()["set-cookie"][0];
//   const csrfToken = setCookieHeader
//     .split(";")
//     .find((cookie) => cookie.trim().startsWith("csrf_token"))
//     .split("=")[1];

//   // Define incorrect login credentials
//   const loginPayload = {
//     email: "wrong@example.com",
//     password: "wrongpassword",
//     csrf_token: csrfToken,
//   };

//   // Send login request
//   const loginResponse = await request.post(`${baseURL}/api/auth/login`, {
//     headers: {
//       "Content-Type": "application/json",
//       Cookie: `csrf_token=${csrfToken}`,
//     },
//     data: JSON.stringify(loginPayload),
//   });

//   // Verify response
//   expect(loginResponse.status()).toBe(401);
//   const errorData = await loginResponse.json();
//   expect(errorData).toHaveProperty("errors");
// });
