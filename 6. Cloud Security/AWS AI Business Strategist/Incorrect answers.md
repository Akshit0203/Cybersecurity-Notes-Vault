# Incorrect Answers

---

## Question 1

**Which AWS resource defines the dimensions of responsible AI and organizes them into questions a team can work through across the lifecycle?**

- **A. The AWS Well-Architected Framework Responsible AI Lens** ✅
- B. Configurable safeguards on model inputs and outputs in Amazon Bedrock
- C. The custom model lifecycle in Amazon SageMaker AI
- D. The AWS Cloud Adoption Framework (AWS CAF)

> [!tip] Why A is correct
> The Responsible AI Lens defines the responsible AI dimensions and organizes them into focus areas aligned to the stages of the lifecycle, so a team can work through them as questions.

---

## Question 2

**An organization is planning an AI system that will affect who receives a service. A leader proposes handling responsible AI in a compliance review scheduled just before launch. What is the strongest argument against waiting?**

- **A. A review at the end can only approve, delay, or reject, while the decisions that determine governance have already been made** ✅
- B. Compliance reviews are not a valid governance mechanism at any stage
- C. Waiting means the organization will not be able to measure the system's accuracy
- D. Responsible AI practices apply only to generative AI systems, so timing does not matter

> [!tip] Why A is correct
> Governance by design exists because choices about data, permitted actions, and explainability are cheap to shape during planning and expensive to retrofit once the system is built.

---

## Question 3

**An organization introduces a model into an existing lending decision process. Which statement best describes its regulatory position?**

- A. Obligations no longer apply, because the decision is now automated
- B. Only AI-specific regulations apply, replacing the previous lending rules
- C. The organization must wait for a regulator to specify how AI rules apply before acting
- **D. Existing lending obligations continue to apply to the decision, with AI-specific expectations added on top** ✅

> [!tip] Why D is correct
> Introducing AI brings the process into scope of the obligations that already governed the decision, and adds expectations such as disclosure or a route to human review.

---

## Question 4

**An organization reviews and approves a high-risk AI system before launch, then treats governance for it as complete. What is the flaw in this approach?**

- A. Pre-launch approval is unnecessary if the system will be monitored afterward
- **B. Most AI risks in production emerge silently after launch, so ongoing controls and monitoring are required** ✅
- C. The approval should have been given by a regulator rather than the organization
- D. High-risk systems should never be approved for production

> [!tip] Why B is correct
> Data shifts, usage changes, and drift degrade a system without raising errors, so a system needs measurement, thresholds, and an accountable owner for its whole life.

---

## Question 5

**An organization wants to compare the likely cost of building a custom model against buying a managed capability, before it commits to either. Which tool is the natural fit?**

- **A. AWS Pricing Calculator** ✅
- B. Amazon SageMaker AI
- C. AWS Marketplace
- D. Amazon Bedrock

> [!tip] Why A is correct
> AWS Pricing Calculator estimates the cost of a solution before you commit, so it lets you compare acquisition options on cost alongside capability and timeline.

---

## Question 6

**An organization's durable advantage would come from a model built on data only it holds, and it is willing to invest to own that capability. Which path fits that intent?**

- A. AWS Marketplace to acquire a third-party solution
- B. Amazon Bedrock as a managed capability
- C. Amazon Bedrock as a managed capability
- **D. Amazon SageMaker AI, the custom machine learning lifecycle** ✅

> [!tip] Why D is correct
> When the differentiator is a model or data the organization owns, the custom path is what turns that asset into a capability competitors cannot simply acquire.

---

## Question 7

**Which term describes the process of using a trained AI model to generate outputs based on new input data?**

- A. Amazon QuickSight
- **B. Amazon SageMaker AI** ✅
- C. AWS Pricing Calculator
- D. AWS Marketplace

> [!tip] Why B is correct
> Amazon SageMaker AI supports the full custom machine learning lifecycle, including training a model on your own data, deploying it, and monitoring it after it is live.

---

## Question 8

**A model deployed several months ago still returns results without any errors, but the business outcomes it supports have gradually worsened. What best explains this, and what is the appropriate response?**

- A. The model has reached the end of its supported life and must be replaced with a different solution type.
- **B. Live data or the underlying relationship has drifted from the training baseline, so monitoring should detect it and the model should be retrained on more recent data.** ✅
- C. The system is under-provisioned, so adding capacity will restore the quality of the results.
- D. The gradual change is expected variation, so no action is warranted until an error is raised.

> [!tip] Why B is correct
> Drift degrades accuracy silently, which is why live inputs and outputs are compared against the training baseline and the model is refreshed when it falls behind.

---

## Question 9

**An internal assistant gives factually current answers, but its replies are long and inconsistently formatted when the business needs short, uniform responses. Which technique addresses this, and why?**

- A. Retrieval Augmented Generation, because the assistant needs access to more of the organization's content.
- B. Reducing the amount of content supplied with each request, because the response length follows the input length.
- **C. Fine-tuning, because the required change is in how the model responds rather than in the facts it has.** ✅
- D. Applying safeguards to the assistant's output, because unwanted content should be filtered.

> [!tip] Why C is correct
> Tone, format, and specialized task behavior are behavior gaps, and fine-tuning with labeled examples is what changes how the model responds.

---

## Question 10

**A retail company collects sales data manually across its stores. The manual collection produces inconsistent data. The company pilots an AI-powered demand forecasting system at select stores. Now the company wants to scale the system to all store locations. The company must establish reliable, consistent data inputs to reduce overstock costs and maintain reliable forecasts. Which solution will meet these requirements?**

| Option | Correct | My Answer | Rationale |
|--------|:-------:|:---------:|-----------|
| A. Validate store-level transactions. Review forecast exceptions. Correct data issues for each planning cycle. | | | Reactive approach — does not establish a consistent data quality foundation before scaling. |
| B. Monitor forecast accuracy by store. Review performance trends. Re-train the model when prediction quality declines. | | | The company has a source-data problem that re-training cannot fix. |
| C. Select a forecasting model that supports varied store data. Standardize outputs. Centralize post-deployment tuning. | | ❌ | Accommodating inconsistent inputs is not a data quality strategy — unreliable source data will degrade forecasts. |
| **D. Standardize data collection practices. Apply consistent data quality checks. Maintain reliable inputs.** | ✅ | | Foundational data governance from the ML Lens of the AWS Well-Architected Framework — ensures reliable uniform inputs before scaling. |

> [!important] Key Takeaway
> Standardize data **inputs** before scaling — no model can fix inconsistent source data.

---

## Question 11

**A company ran several successful targeted AI pilots. Now the company wants to scale AI across the whole company in a unified way. Currently, each pilot team manages its own oversight independently. Most employees outside the pilot teams do not have experience using AI tools. Company leaders do not want to disrupt ongoing operations. Which scaling approach will meet these requirements?**

| Option | Correct | My Answer | Rationale |
|--------|:-------:|:---------:|-----------|
| A. Use external consultants to lead scaling. Maintain existing governance practices. Train workforce champions. | | | Staffing solution, not transformation — keeps fragmented governance intact. |
| **B. Use pilot results to set rollout criteria. Establish shared oversight practices. Prepare employees for new responsibilities. Release capabilities in stages.** | ✅ | | Phased scaling: addresses governance, readiness, and deployment in stages. |
| C. Centralize AI decisions to one team. Apply oversight to high-risk use cases. Provide training after rollout. | | | Leaves most use cases ungoverned; training after rollout leaves employees unprepared. |
| D. Move selected pilot models into production. Assign local teams to manage governance. Expand training as issues arise. | | ❌ | Reactive training and local governance without shared standards continues inconsistent oversight. |

> [!important] Key Takeaway
> Scale in phases: set criteria from pilots → establish shared oversight → prepare people → release in stages.

---

## Question 12

**A retail company establishes a small AI team. The team launches a product recommendation system for the company's ecommerce website. The team has limited experience in cross-functional deployments. Company leadership needs to assign the team its next AI initiative. The initiative must help the company develop operational maturity for customer-facing AI applications while building capabilities incrementally. Which initiative will meet these requirements?**

| Option | Correct | My Answer | Rationale |
|--------|:-------:|:---------:|-----------|
| A. Build an internal meeting summarization tool for a high-priority BU. | | | Low-risk internal tool — limited business impact and minimal production complexity. |
| **B. Launch an AI assistant that automatically answers customer questions about specific products.** | ✅ | | Controlled, customer-facing use case — provides meaningful production experience with manageable scope. |
| C. Expand the existing recommendation system to additional product categories. | | ❌ | Scales an existing capability — does not build cross-functional deployment skills. |
| D. Launch a real-time personalized shopping assistant across all channels with multiple integrated AI models. | | | Too complex for a small team — skips incremental capability-building. |

> [!important] Key Takeaway
> The next initiative should stretch the team into **new cross-functional territory** with manageable scope, not just scale what already works.
