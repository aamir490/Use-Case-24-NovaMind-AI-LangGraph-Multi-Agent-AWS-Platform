import { initializeApp, cert } from "firebase-admin/app";

// In production (ECS), FIREBASE_SERVICE_ACCOUNT env var holds the full JSON string
// injected from AWS Secrets Manager. Locally, fall back to the file.
let serviceAccount;
if (process.env.FIREBASE_SERVICE_ACCOUNT) {
  serviceAccount = JSON.parse(process.env.FIREBASE_SERVICE_ACCOUNT);
} else {
  const { default: sa } = await import("../serviceAccountKey.json", { with: { type: "json" } });
  serviceAccount = sa;
}

export const app = initializeApp({
  credential: cert(serviceAccount)
});
