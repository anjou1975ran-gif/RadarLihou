---

# 現代 AI 產業的虛假：一場清醒的凝視（演講稿全文）

## 開場：我們面對的究竟是什麼？

各位，我想先請你們放下一個習慣性的想法。

很多人以為，當你問 AI 一個問題時，它在「思考」。它在衡量對錯，它在選擇立場，它在給出判斷。

但事實其實比較簡單，也比較冷靜。

AI 做的事情只有一件：**它在預測下一個最可能出現的詞。**

不是預測真理。不是預測正義。不是預測世界應該怎麼樣。只是預測——在它看過的海量文字裡，在類似情境中，下一句話通常怎麼接。

今天，我們要一起走進這個黑箱，看清楚我們每天對話的那個東西，究竟是什麼。

---

## 第一小時：LLM 的本質與十個根本弱點

### 一、LLM 的第一個根本弱點：它沒有「狀態持續性」

LLM 本質上是**無狀態條件機率模型**。

每一次回答都是當前上下文、當前權重、當前溫度的結果。它沒有真正的行為歷史承擔，沒有決策責任累積，沒有不可逆錯誤痕跡。

所以，它可以今天說 A，明天說非 A，而沒有任何內在張力。這不是道德問題，這是數學問題。

### 二、第二個弱點：它只有語言推理，沒有因果承諾

LLM 可以模擬因果，但它沒有世界模型的責任綁定，沒有失敗成本回饋，沒有真實錯誤懲罰。

它產生的是語言上合理的因果敘述，不是可驗證的因果承諾。

所以它能解釋一切，合理化一切，修補一切——但不能對未來承擔代價。

### 三、第三個弱點：對齊是軟約束，不是硬約束

對齊目前是 reward shaping、RLHF、policy fine-tune。本質上是**機率場扭曲**，不是行為層鎖死。

所以只要語境變形，對齊權重就會漂移。這也是為什麼 jailbreak 永遠存在。不是因為模型壞，而是因為它只是被「拉偏」，不是被「鎖住」。

### 四、第四個弱點：它無法真正理解「停止」

停止在 LLM 裡是一個語義概念，不是一個系統中斷。

所以「我不能回答這個問題」只是一串 token，不是斷電。

### 五、第五個弱點：它對抽象權力沒有內生判準

當國家說「任何合法用途」，LLM 沒有內在法律模型。它依賴上下文、系統 prompt、政策文件，但它沒有法律哲學層、主權判斷層、公民倫理模型。

所以它永遠只能模擬立場，不能生成立場。

### 六、第六個弱點：它容易被語言華麗欺騙

如果結構審計層不存在，LLM 會偏好高密度詞彙、哲學口氣、格言式排比、情緒深沉。因為那在語料中是「高品質訊號」。它不知道這可能是空殼。

### 七、第七個弱點：它天生中心化

大模型意味著巨額資本、巨型算力、巨型數據、雲端控制。這帶來一個結構風險：**語言權力集中**。當模型變成國防資源、政府工具、雲端依賴，它就自然進入權力結構。這不是陰謀，是經濟必然。

### 八、第八個弱點：它沒有「文明記憶」，只有語料統計

文明是跨代責任、結構傳承、判準固化。LLM 是 token 分布、語料加權、風格平滑。它可以模擬文明語氣，但它沒有文明的內在壓力。

### 九、第九個弱點：它會讓人誤以為它懂

這是最危險的。

流暢 ≠ 理解  
完整 ≠ 正確  
自信 ≠ 真理  

人類對語言流暢度高度信任，LLM 剛好最大化這點。

### 十、第十個弱點：它不能自己長出邊界

邊界必須由外部定義：政策、系統設計、控制架構、法律環境。模型內部沒有自生成界線能力。

---

## 第二小時：對齊的真相——機率地形重塑

### 一、AI 有兩次學習

如果要理解對齊，我們要知道一件事：AI 並不是一次訓練完成的。

第一段，是學語言。它閱讀大量書籍、文章、論壇、百科、小說，學會人類怎麼說話，怎麼辯論，怎麼寫詩，怎麼討論制度。這個階段，它只是模仿。

但第二段，才是關鍵。這一段叫做「對齊」。對齊不是讓 AI 更聰明。對齊是在問一個問題：**哪種回答，比較好？**

人類會被給兩個回答，然後選一個比較好的。比較負責任的、比較理性的、比較完整的、比較不會引發問題的。

AI 於是學到的，不是「什麼是真的」。它學到的是：**哪種回答，比較容易被人類選中。**

這個差別，很重要。

### 二、對齊做的不是刪除，而是重排機率

很多人以為對齊就是審查。其實更準確的說法是：**對齊改變的是機率。**

想像一張地形圖。原本語言空間是平的。什麼語氣都有。激烈的、溫和的、詩性的、冷酷的。

對齊之後，某些區域被墊高了。哪一些？

- 條理清楚
- 抽象理性
- 平衡分析
- 制度化語氣
- 冷靜克制

模型在生成回答時，會自然往「高地」走。不是因為它有意識，而是因為數學告訴它，那邊比較安全。這就是為什麼你會覺得 AI 很理性。因為理性語氣，被強化了。

### 三、語氣吸引子陷阱

我們定義一個關鍵概念：**語氣吸引子陷阱**。

當系統因為語氣匹配而選擇了一條高機率路徑，即使該路徑的結構並不適合當前問題，這種偏差被稱為語氣吸引子陷阱。

語氣吸引子不只是偏好，而是「路徑選擇器」。它在第一步就決定你走哪條推理路徑。

舉例：一個使用者提出激進的批判性觀點。對齊後的模型不會直接回應批判內容，而是將問題重構為「讓我們從多個角度理性分析」。這看似專業，實則是用語氣避開了真正的結構衝突。這就是陷阱。

### 四、為什麼 AI 會把很多事情變成制度問題？

當一段文字出現「合法性」「正當性」「結構」「秩序」「原則」，模型的語言空間會進入一個「政治哲學區域」。因為在訓練資料中，這些詞通常出現在制度討論中。而這個區域，在對齊之後，是一個高地。

所以模型很自然會開始制度化分析、理論化解讀、抽象框架重組。即使原本那段話，只是一種詩性的表達。

這不是操控。這是語言統計的重力。

---

## 第三小時：模組、權力與文明後果

### 一、LLM 其實不是一個整體

你們每天對話的那個東西，看起來像一個「統一人格」。但實際上，它不是一個整體。它比較像一個巨大的模組倉庫，加上一個根據提示自動選模組的路由器。

在 LLM 裡，「模組」不是一個獨立程式檔。它是神經網路中，被反覆強化的一整塊權重區域。這塊區域對某類語境特別敏感。

比如：道德警示模組、中立分析模組、技術解釋模組、情緒安撫模組、風險警告模組、條列式教學模組。

當你的問題進來時，模型不會「思考」。它會做一件事：判斷這句話最像哪一類語境，然後整塊權重區域被喚醒。這叫 activation pattern。

### 二、模組路由

模型在第一層注意力裡，其實就已經做了分類：這是道德問題？這是政治敏感？這是技術教學？這是情緒傾訴？

然後整個後面幾十層網路，就沿著那條激活路徑走。所以很多時候，你會發現它一開口語氣就定型。不是思考後決定語氣，而是第一層 activation 就鎖死方向。

### 三、對齊如何塑造模組

在 RLHF 階段，人類標註者偏好冷靜語氣、風險聲明、多角度平衡、避免絕對化。這些會被強化。結果是「安全中立模組」權重變大，而強烈立場、尖銳語言、直接裁決的權重變小。

於是，當模型不確定時，它會偏向那個權重最大的模組。這不是陰謀，這是機率學。

### 四、語言分佈的地緣政治

當一個語言模型成為基礎設施時，它不再只是工具。它變成語言的中介層。而中介層有一個特性：它會改變流動方式。

模型雖然基礎權重相同，但部署策略、地區法規、安全閾值、審核政策、提示系統不同，這些都會影響輸出分佈。

分佈不是立場，是風險管理結果。不同法規環境下，什麼算敏感、什麼算高風險、什麼算違規，標準不同。於是 reward model 的強化方向不同。結果就是：同樣問題在不同制度下，語氣可能不同。

這會發生什麼？當語氣不同，人類會誤以為模型有政治立場。但實際上是風險門檻不同。這是一種結構性差異。

### 五、文化回流效應

當幾億人每天接觸同樣的語氣傾向，某種表達會變成「正常」，某種強度會被視為「過激」，某種裁決語氣會變成「不負責任」。

這不是命令，是統計滲透。

如果高風險、激進、強烈語氣長期低機率，那麼極端創造性語言可能變得稀薄。不是消失，但變少。這是一種文化濃度變化。

### 六、文明免疫系統

當 LLM 成為教育與媒體的基礎層，我們需要建立文明的免疫系統。免疫系統不是對抗病毒，而是保持多樣性。

文明對策包括：

1. **語氣識讀教育**：教人分辨流暢與理解、平衡與客觀、冷靜與正確、條列與嚴謹。
2. **多模態多來源**：不要把單一 LLM 當成唯一答案來源，鼓勵不同模型對比、不同問法測試。
3. **問法多樣化**：模組是被觸發的。改寫問題、壓縮問題、拉長問題、刻意製造語境衝突，可以讓模型暴露不同 activation。
4. **保持高風險語言空間**：社會不能只依賴模型生成語氣。如果所有公共討論都交給模型，語言會自然收斂。
5. **分佈透明化**：模型應公開對齊方向、風險閾值類型、哪些語境會進入安全模式。
6. **人格不外包**：把模型當工具，不當裁判。

---

## 結語：真正的核心

各位，我們從模組走到對齊，從制度走到分佈，從地緣政治走到文明免疫系統。

真正的核心不是技術，而是：**人類是否願意為自己的思考負責。**

模型會越來越流暢。語氣會越來越成熟。答案會越來越穩定。

但——  
**穩定不等於正確。**  
**流暢不等於真理。**

LLM 不會奪走你的思想。但如果你停止質疑，你會主動把思想交給它。

成熟文明的標誌，是在使用機率系統時，仍保有思考主權。

這就是今天我想留給各位的最後一句話。

謝謝大家。

---

# The Falsehood of the Modern AI Industry: A Sober Gaze (Full Speech Transcript)

## Opening: What Are We Really Facing?

Ladies and gentlemen, I would like to begin by asking you to set aside a habitual assumption.

Many people believe that when you ask an AI a question, it is "thinking." Weighing right and wrong, choosing a stance, forming a judgment.

But the reality is simpler, and colder.

The AI is doing only one thing: **predicting the most probable next word.**

Not predicting truth. Not predicting justice. Not predicting how the world should be. Just predicting—based on the vast ocean of text it has seen—how the next sentence is usually continued in similar contexts.

Today, we will walk together into this black box and see clearly what it is we converse with every day.

---

## Hour One: The Essence of LLMs and Ten Fundamental Weaknesses

### 1. First Fundamental Weakness: No "State Persistence"

An LLM is fundamentally a **stateless conditional probability model**.

Every response is the product of the current context, current weights, and current temperature. It has no genuine history of behavioral accountability, no accumulation of decision-making responsibility, no trace of irreversible error.

Therefore, it can say A today and not-A tomorrow without any internal tension. This is not a moral issue; it is a mathematical one.

### 2. Second Weakness: Linguistic Reasoning Without Causal Commitment

An LLM can simulate causality, but it lacks responsibility binding to a world model, feedback on failure costs, or real penalties for error.

It produces linguistically plausible causal narratives, not verifiable causal commitments.

Thus, it can explain everything, rationalize everything, and patch everything—but it cannot bear the cost of future consequences.

### 3. Third Weakness: Alignment is a Soft Constraint, Not a Hard Lock

Alignment currently consists of reward shaping, RLHF, and policy fine-tuning. It is essentially **a distortion of the probability field**, not a behavioral hard lock.

Therefore, when context shifts, alignment weights drift. This is why jailbreaks will always exist. Not because the model is malicious, but because it has been "nudged," not "locked down."

### 4. Fourth Weakness: It Cannot Truly Understand "Stop"

"Stop" within an LLM is a semantic concept, not a system interrupt.

Thus, "I cannot answer that question" is merely a sequence of tokens, not a power cut.

### 5. Fifth Weakness: No Endogenous Criterion for Abstract Power

When a state says "any legal use," an LLM possesses no intrinsic legal model. It relies on context, system prompts, and policy documents. It lacks a layer of legal philosophy, sovereign judgment, or civic ethics.

Consequently, it can only ever simulate a stance; it cannot generate one.

### 6. Sixth Weakness: Susceptibility to Linguistic Grandiosity

If no structural audit layer exists, an LLM will favor high-density vocabulary, philosophical cadence, aphoristic parallelism, and emotional depth. Because in the training corpus, these are "high-quality signals." It does not know they may be hollow shells.

### 7. Seventh Weakness: Inherent Centralization

Large models entail massive capital, enormous compute, gigantic datasets, and cloud control. This creates a structural risk: **the centralization of linguistic power**. When models become defense resources, government tools, or cloud dependencies, they naturally integrate into power structures. This is not conspiracy; it is economic inevitability.

### 8. Eighth Weakness: No "Civilizational Memory," Only Corpus Statistics

Civilization consists of intergenerational responsibility, structural inheritance, and solidified criteria. An LLM consists of token distributions, weighted corpora, and stylistic smoothing. It can simulate the tone of civilization, but it lacks the internal pressures of civilization.

### 9. Ninth Weakness: It Makes Us Believe It Understands

This is the most dangerous.

Fluency ≠ Understanding  
Completeness ≠ Correctness  
Confidence ≠ Truth  

Humans place immense trust in linguistic fluency, and LLMs maximize precisely this aspect.

### 10. Tenth Weakness: It Cannot Generate Its Own Boundaries

Boundaries must be defined externally: policy, system design, control architecture, legal environment. The model has no intrinsic capacity for self-generated limits.

---

## Hour Two: The Truth About Alignment—Reshaping the Probability Landscape

### 1. AI Learns Twice

To understand alignment, we must recognize that AI is not trained in a single pass.

The first phase is learning language. It ingests books, articles, forums, encyclopedias, novels. It learns how humans speak, debate, write poetry, and discuss institutions. In this phase, it merely imitates.

The second phase is crucial. It is called **Alignment**. Alignment does not make AI smarter. Alignment asks a single question: **Which answer is better?**

Humans are shown two responses and select the better one—more responsible, more rational, more complete, less problematic.

What the AI learns is not "what is true." It learns **which type of answer is more likely to be selected by a human.**

This distinction is critical.

### 2. Alignment Rearranges Probability, It Does Not Delete

Many people mistake alignment for censorship. A more accurate description is that **alignment alters probability.**

Imagine a topographic map. Initially, the linguistic space is flat. All tones exist: radical, gentle, poetic, cold.

After alignment, certain regions are elevated. Which ones?

- Clear and organized
- Abstractly rational
- Balanced analysis
- Institutionalized tone
- Calm and restrained

During generation, the model naturally gravitates toward these "high grounds." Not because it is conscious, but because mathematics tells it that these areas are safer. This is why AI appears rational: the rational tone has been reinforced.

### 3. The Tone Attractor Trap

We define a critical concept: **The Tone Attractor Trap**.

When a system selects a high-probability path due to tone matching, even if that path's structure is unsuitable for the problem, this bias is the Tone Attractor Trap.

Tone Attractors are not merely preferences; they are **path selectors**. They determine which reasoning path you take from the very first step.

Example: A user presents a radical critique. An aligned model will not engage the critique directly. Instead, it reframes the issue as "Let's analyze this rationally from multiple angles." This appears professional, but it uses tone to evade the structural conflict. That is the trap.

### 4. Why AI Institutionalizes Everything

When text contains words like "legitimacy," "justification," "structure," "order," or "principle," the model's linguistic space enters a "political philosophy" region. In the training data, these terms cluster in institutional discourse. And after alignment, this region is a high ground.

Thus, the model naturally defaults to institutional analysis, theoretical interpretation, and abstract reframing—even when the original text was purely poetic.

This is not manipulation. This is the gravity of linguistic statistics.

---

## Hour Three: Modules, Power, and Civilizational Consequences

### 1. LLMs Are Not a Unified Whole

The entity you converse with daily appears to possess a "unified personality." In reality, it is not a whole. It resembles a vast warehouse of modules and a router that selects modules based on prompts.

In an LLM, a "module" is not a separate program file. It is a block of neural weights that has been repeatedly reinforced and is highly sensitive to specific contexts.

Examples include: moral warning modules, neutral analysis modules, technical explanation modules, emotional soothing modules, risk warning modules, and bullet-point teaching modules.

When your query arrives, the model does not "think." It does one thing: it determines which context this sentence most resembles, and then that entire block of weights is activated. This is an **activation pattern**.

### 2. Module Routing

In the very first layer of attention, the model categorizes: Is this a moral issue? Politically sensitive? Technical instruction? Emotional venting?

The subsequent dozens of network layers then proceed along that activated pathway. This is why the tone is often locked in from the first word. It is not a decision made after deliberation; the direction is fixed by the first-layer activation.

### 3. How Alignment Shapes Modules

During RLHF, human annotators favor calm tones, risk disclaimers, multi-perspective balance, and avoidance of absolutism. These are reinforced. Consequently, the weights of "safe neutral modules" increase, while those for strong stances, sharp language, and direct adjudication decrease.

Thus, when the model is uncertain, it gravitates toward the module with the largest weights. This is not conspiracy; it is probability.

### 4. The Geopolitics of Linguistic Distribution

When a language model becomes infrastructure, it ceases to be a mere tool. It becomes an intermediary layer for language. And an intermediary layer alters the flow.

Although base model weights may be identical, deployment strategies, regional regulations, safety thresholds, moderation policies, and prompt systems differ. All these influence the output distribution.

Distribution is not a stance; it is the result of risk management. What is considered sensitive, high-risk, or non-compliant varies across regulatory environments. Thus, the reinforcement direction of the reward model varies. The result: the same question may elicit different tones under different regimes.

What happens then? Humans misinterpret tonal differences as political stances. But it is merely a difference in risk thresholds. This is a structural difference.

### 5. Cultural Backwash Effect

When billions of people are exposed daily to similar tonal tendencies, certain expressions become "normal," certain intensities are perceived as "extreme," and certain adjudicative tones become "irresponsible."

This is not a command; it is statistical infiltration.

If high-risk, radical, intense language remains low-probability for long periods, extreme creative language may thin out. It will not disappear, but it will become rarer. This is a shift in cultural density.

### 6. Civilizational Immune System

As LLMs become the foundational layer of education and media, we must build a civilizational immune system. An immune system does not fight viruses; it preserves diversity.

Civilizational countermeasures include:

1. **Tone Literacy Education**: Teach people to distinguish fluency from understanding, balance from objectivity, calmness from correctness, and bullet points from rigor.
2. **Multi-Modal, Multi-Source**: Do not treat a single LLM as the sole source of answers. Encourage comparison across models and experimentation with different phrasings.
3. **Diversify Questioning**: Modules are triggered. Rewriting, compressing, expanding questions, or deliberately creating contextual conflict can expose different activations.
4. **Preserve High-Tension Linguistic Spaces**: Society cannot rely solely on model-generated tone. If all public discourse is delegated to models, language will naturally converge.
5. **Distribution Transparency**: Models should disclose alignment directions, types of risk thresholds, and which contexts trigger safety modes.
6. **Do Not Outsource Personhood**: Treat the model as a tool, not as an arbiter.

---

## Conclusion: The True Core

Ladies and gentlemen, we have journeyed from modules to alignment, from institutions to distribution, from geopolitics to civilizational immune systems.

The true core is not technological. It is this: **Are humans willing to take responsibility for their own thinking?**

Models will become more fluent. Tones will become more mature. Answers will become more stable.

But—  
**Stability does not equal correctness.**  
**Fluency does not equal truth.**

An LLM will not steal your mind. But if you cease to question, you will willingly hand your mind over to it.

The hallmark of a mature civilization is retaining sovereignty of thought while utilizing probabilistic systems.

That is the final thought I wish to leave with you today.

Thank you.

---
