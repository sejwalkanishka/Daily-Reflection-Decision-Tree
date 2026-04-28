# 🌳 Daily Reflection Decision Tree
Deterministic behavioral reflection system built using a structured decision tree across locus, orientation, and radius psychological frameworks. Includes a CLI-based AI agent with guardrails to prevent hallucination.


---

## 🚀 Overview

This project implements a **rule-based decision tree** that guides users through structured self-reflection. Unlike traditional AI systems, this model is fully deterministic—every input maps to a predefined output, ensuring **consistency, explainability, and zero ambiguity**.

The system is designed as a **progressive reflection flow**:

* Starts with personal accountability (Locus)
* Moves to behavioral intent (Orientation)
* Expands to social awareness (Radius)

## 🧠 Problem Statement

How can we model human daily reflection in a structured, deterministic, and explainable way without relying on probabilistic AI systems?

This project answers that using a knowledge-engineered decision tree.

## 🌍 Why This Matters

Most reflection tools are vague, inconsistent, and heavily dependent on subjective interpretation.

This system introduces:
- Determinism → same input = same output
- Explainability → every decision is traceable
- Psychological grounding → based on locus, orientation, and radius frameworks

  ## 📊 Tree Structure Format

The decision tree is implemented using a structured TSV format with the following fields:

- id → unique node identifier  
- parentId → parent node  
- type → question / decision / reflection / bridge / summary  
- text → content  
- options → predefined choices  
- target → routing logic  
- signal → psychological axis indicator  
---

## 🧠 Key Highlights

* ✅ Deterministic decision-making (no randomness)
* ✅ Based on behavioral psychology frameworks
* ✅ Structured, multi-level reflection system
* ✅ Explainable and reproducible outputs
* ✅ Includes CLI-based AI agent (Part B)

---

## 🤖 AI Usage Philosophy

AI was used strictly as a **supporting tool**, not as a decision-maker.

To ensure reliability and prevent hallucination:

* Guardrails were applied to restrict AI outputs
* Negative prompting was used to avoid assumptions
* All logic was manually validated for consistency

---

## 🤖 AI Usage & Hallucination Control

AI was used strictly as an assistive tool during ideation.

To ensure reliability:

- Enforced deterministic outputs only
- Restricted responses to predefined options
- Used negative prompting to prevent assumption generation
- Rejected AI outputs that introduced ambiguity or non-determinism

Final system logic was fully human-validated.

## ⚙️ Design Principles

- Determinism over randomness  
- Clarity over complexity  
- Signal extraction over generic reflection  
- Structured flow over open-ended responses

  ## 🔍 Example Flow

Input:
- Day: Tough  
- Reaction: Blame situation  
- Interaction: Expected recognition  
- Focus: Myself  

Output:
- Locus: External  
- Orientation: Entitlement  
- Radius: Self  

Reflection:
Opportunity to increase ownership, contribution mindset, and external awareness.

## 📁 Project Structure

```
reflection-tree/
│
├── README.md
├── reflection-tree.tsv
├── agent.py
├── diagram.md
```

---

## 🎯 Objective

To demonstrate how **structured thinking + deterministic systems** can model human reflection in a clear, logical, and scalable way.

---

## ⚡ How to Run (Agent)

```bash
python agent.py
```

---

## 📌 Note

This project focuses on **clarity over complexity**, emphasizing strong foundational logic rather than unnecessary abstraction.

Built as part of DeepThought CultureTech selection assignment.
