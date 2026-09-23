# Architecture poster

Created with the built-in image-generation tool, using the user-supplied NovaMind poster as a visual reference and the repository analysis as the technical source. The README uses `novamind-aws-architecture-poster.png`.

Generation brief: Match the reference's landscape ten-panel layout, navy NovaMind AI header and footer, Built by Aamir branding, colored numbered bars, pale panels, AWS-style service icons, provider logos and readable arrows. Include frontend access, AWS infrastructure with five services, shared AWS services, eight LangGraph specialists, external providers, detailed PDF RAG, security/logging, backend CI/CD, frontend deployment and user results. Correct the reference's Vision/Image Analyzer provider assignments and omit unsupported WAF, JWT sessions, alarms and citations.

Correction brief: Preserve the poster design. Replace sequential microservice arrows with independent Gateway branches to Auth, Chat, Agent and Billing. API requests originate at the browser, not S3. Avoid asserting HTTPS on the configurable API endpoint. Label GitHub Actions Build & deploy rather than Build & test.

The poster's marks are generated illustrations. For the diagram embedding original AWS asset files, use the separately retained `novamind-aws-architecture.svg` and its renderer, `scripts/render_architecture.py`. That renderer does not regenerate this poster.
