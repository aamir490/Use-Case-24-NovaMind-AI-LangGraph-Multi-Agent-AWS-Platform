import { getModel } from "../config/llmModels.js"
import { BedrockRuntimeClient, InvokeModelCommand } from "@aws-sdk/client-bedrock-runtime"
import { uploadToS3 } from "../utils/uploadToS3.js"
import { getFromS3 } from "../utils/getFromS3.js"
import { deductCredits } from "../utils/deductCredits.js"
import { checkAgentLimit } from "../config/agentLimit.js"

const bedrockClient = new BedrockRuntimeClient({ region: "us-east-1" })

export const visionAgent = async (state) => {
    try {
        await checkAgentLimit(state.userId, "image")

        // Step 1 — use Groq to turn user request into a detailed image prompt
        const llm = await getModel("image")
        const res = await llm.invoke(`
You are an elite AI image prompt engineer.
Convert the user request into a highly detailed image generation prompt.

Requirements:
- Cinematic lighting
- Professional composition  
- Ultra realistic, high detail
- Beautiful color palette, sharp focus
- 8K quality, photorealistic
- Depth of field, professional photography

Return only the image prompt, nothing else.

User Request:
${state.prompt}
        `)

        const prompt = res.content.trim()

        // Step 2 — generate image using Amazon Nova Canvas via Bedrock
        const bedrockPayload = {
            taskType: "TEXT_IMAGE",
            textToImageParams: {
                text: prompt
            },
            imageGenerationConfig: {
                numberOfImages: 1,
                height: 1024,
                width: 1024,
                quality: "standard",
                cfgScale: 8.0
            }
        }

        const command = new InvokeModelCommand({
            modelId: "amazon.nova-canvas-v1:0",
            contentType: "application/json",
            accept: "application/json",
            body: JSON.stringify(bedrockPayload)
        })

        const bedrockResponse = await bedrockClient.send(command)
        const responseBody = JSON.parse(Buffer.from(bedrockResponse.body).toString("utf8"))

        if (!responseBody.images || responseBody.images.length === 0) {
            throw new Error("No image returned from Nova Canvas")
        }

        // Step 3 — decode base64 image and upload to S3
        const imageBuffer = Buffer.from(responseBody.images[0], "base64")
        const filename = `image-${Date.now()}.png`

        await uploadToS3(filename, imageBuffer, "image/png")
        const downloadUrl = await getFromS3(filename, 24 * 60)

        await deductCredits(state.userId, "vision")

        return {
            ...state,
            aiResponse: `
![Generated Image](${downloadUrl})

📥 [Download Image](${downloadUrl})

⏳ Link expires in 24 hours.`,
            images: [downloadUrl]
        }

    } catch (error) {
        console.error("Vision agent error:", error)
        return {
            ...state,
            aiResponse: error?.message || "failed to generate image"
        }
    }
}
