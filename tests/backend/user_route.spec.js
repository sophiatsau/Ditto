const { test, expect, request } = require("@playwright/test");

// Helper function to login and get cookies
// async function loginAndGetCookies() {
//   const loginRequest = await request.newContext();
//   const response = await loginRequest.post("/auth/login", {
//     form: {
//       email: "demo@aa.io",
//       password: "password",
//     },
//   });

//   expect(response.status()).toBe(200);

//   // Get cookies from the login response
//   const cookies = await loginRequest.cookies();
//   await loginRequest.dispose();
//   return cookies;
// }
// test.beforeAll(async () => {
//   // Login and get cookies before all tests
//   cookies = await loginAndGetCookies();
// });

// test.describe("User api endpoint", () => {
//   // individual test
//   test("GET /users/ - Query for all users and returns them in a list of user dictionaries", async ({
//     request,
//   }) => {
//     const response = await request.get("/users/");
//     expect(response.status()).toBe(200);

//     const contentType = response.headers()["content-type"];
//     expect(contentType).toContain("application/json");

//     const data = await response.json();
//     expect(data).toHaveProperty("users");
//     console.log(data.users);

//     expect(Array.isArray(data.users)).toBeTruthy();
//   });
// });
