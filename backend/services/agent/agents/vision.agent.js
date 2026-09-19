import { getModel } from "../config/llmModels.js"
import { uploadToS3 } from "../utils/uploadToS3.js"
import { getFromS3 } from "../utils/getFromS3.js"
import { deductCredits } from "../utils/deductCredits.js"
import { checkAgentLimit } from "../config/agentLimit.js"

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

        // Step 2 — generate image using Stability AI REST API
        const formData = new FormData()
        formData.append("prompt", prompt)
        formData.append("output_format", "png")
        formData.append("width", "1024")
        formData.append("height", "1024")

        const stabilityResponse = await fetch(
            "https://api.stability.ai/v2beta/stable-image/generate/core",
            {
                method: "POST",
                headers: {
                    Authorization: `Bearer ${process.env.STABILITY_API_KEY}`,
                    Accept: "image/*"
                },
                body: formData
            }
        )

        if (!stabilityResponse.ok) {
            const errText = await stabilityResponse.text()
            throw new Error(`Stability AI error: ${stabilityResponse.status} — ${errText}`)
        }

        const imageBuffer = Buffer.from(await stabilityResponse.arrayBuffer())
        // Step 3 — upload to S3
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
