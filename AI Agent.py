def ask_question(question, options):
    print("\n" + question)
    for i, opt in enumerate(options, 1):
        print(f"{i}. {opt}")
    
    while True:
        try:
            choice = int(input("Select option: "))
            if 1 <= choice <= len(options):
                return options[choice - 1]
        except:
            pass
        print("Invalid input. Try again.")


def reflection_agent():
    print("=== Daily Reflection Agent ===")

    # Axis 1: Locus
    day = ask_question(
        "How was your day?",
        ["Productive", "Tough", "Mixed", "Frustrating"]
    )

    if day in ["Productive", "Mixed"]:
        cause = ask_question(
            "What caused success?",
            ["My effort", "Team support", "Luck", "Adaptation"]
        )
        axis1 = "Internal"
        print("Reflection: You showed ownership.")
    else:
        cause = ask_question(
            "How did you react?",
            ["Fix it", "Wait for help", "Blame situation", "Feel stuck"]
        )
        axis1 = "External"
        print("Reflection: Opportunity to increase control.")

    # Axis 2: Orientation
    interact = ask_question(
        "How did you interact today?",
        ["Helped someone", "Did my job", "Expected recognition", "Felt others lacked effort"]
    )

    if interact == "Helped someone":
        axis2 = "Contribution"
        print("Reflection: Contribution mindset.")
    else:
        axis2 = "Entitlement"
        print("Reflection: Watch expectation patterns.")

    # Axis 3: Radius
    focus = ask_question(
        "Who did you think about most?",
        ["Myself", "Team", "Colleague", "Customer"]
    )

    if focus == "Myself":
        axis3 = "Self"
        print("Reflection: Expand perspective.")
    else:
        axis3 = "Others"
        print("Reflection: Strong external awareness.")

    # Summary
    print("\n=== Summary ===")
    print(f"Locus: {axis1}")
    print(f"Orientation: {axis2}")
    print(f"Radius: {axis3}")
    print("Keep improving daily!")


if __name__ == "__main__":
    reflection_agent()
