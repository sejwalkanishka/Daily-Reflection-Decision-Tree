


START([Start: Reflect on your day])

A1[How was your day?<br>Productive / Tough / Mixed / Frustrating]

A1 --> D1{Decision}

D1 -->|Productive / Mixed| A1H[What caused success?<br>Effort / Team / Luck / Adaptation]
D1 -->|Tough / Frustrating| A1L[Reaction to problems?<br>Fix / Wait / Blame / Stuck]

A1H --> R1[Reflection:<br>High ownership → Internal locus]
A1L --> R2[Reflection:<br>External reaction → Growth opportunity]

R1 --> B1[Bridge → Contribution]
R2 --> B1

B1 --> A2[Interaction today?<br>Helped / Did job / Expected recognition / Frustrated]

A2 --> D2{Decision}

D2 -->|Helped| A2H[Why help?<br>Values / Team / Habit / Asked]
D2 -->|Others| A2L[What frustrated you?<br>Recognition / Effort / Workload / Fairness]

A2H --> R3[Reflection:<br>Contribution mindset]
A2L --> R4[Reflection:<br>Entitlement signals]

R3 --> B2[Bridge → Radius]
R4 --> B2

B2 --> A3[Who did you think about?<br>Self / Team / Colleague / Customer]

A3 --> D3{Decision}

D3 -->|Team/Colleague/Customer| A3H[Impact on others?<br>Positive / Neutral / Unsure / Improve]
D3 -->|Self| A3L[Main concern?<br>Stress / Goals / Workload / Challenges]

A3H --> R5[Reflection:<br>Other-focused growth]
A3L --> R6[Reflection:<br>Self-focused awareness]

R5 --> SUM[Summary:<br>Internal + Contribution + Others]
R6 --> SUM

SUM --> END([End: See you tomorrow])
```



