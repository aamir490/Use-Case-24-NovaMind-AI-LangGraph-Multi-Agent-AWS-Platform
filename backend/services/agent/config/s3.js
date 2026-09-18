import { S3Client } from "@aws-sdk/client-s3";

// On AWS ECS: credentials come from the IAM Task Role automatically.
// On local dev: credentials come from AWS_ACCESS_KEY_ID and AWS_SECRET_KEY env vars.
export const s3 = new S3Client({
    region: process.env.AWS_REGION,
    ...(process.env.AWS_ACCESS_KEY_ID && process.env.AWS_SECRET_KEY
        ? {
            credentials: {
                accessKeyId: process.env.AWS_ACCESS_KEY_ID,
                secretAccessKey: process.env.AWS_SECRET_KEY
            }
          }
        : {}
    )
})