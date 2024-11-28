import streamlit as st

# Initialize global variables
if "player_money" not in st.session_state:
    st.session_state.player_money = 500
if "player_points" not in st.session_state:
    st.session_state.player_points = 0
if "current_round" not in st.session_state:
    st.session_state.current_round = 1

# Scenarios and options
scenarios = [
    {
        "question": "Your favorite cafe has launched a special dessert for ₹250. What do you do?",
        "options": [
            ("Buy the dessert and enjoy it guilt-free.", 2.5, -250),
            ("Treat yourself but save ₹250 for future expenses.", 5, -250),
            ("Avoid the temptation and save all ₹500.", 7.5, 0),
            ("Buy ingredients and learn to make it, saving in the long run.", 10, -200),
        ],
        "tip": "Sometimes it’s okay to spend, but finding creative ways to save can teach valuable skills!"
    },
    {
        "question": "Your friend's birthday is coming up, and everyone is contributing ₹300 for a gift. What do you do?",
        "options": [
            ("Contribute ₹300 to avoid conflicts.", 5, -300),
            ("Suggest a less expensive gift everyone can afford.", 7.5, 0),
            ("Politely decline and explain your financial goals.", 10, 0),
            ("Borrow ₹300 and repay later.", 2.5, -300),
        ],
        "tip": "Balance social obligations with financial priorities. Honesty can inspire others!"
    },
    {
        "question": "You earned ₹1,000 helping your neighbor. How will you allocate your money?",
        "options": [
            ("Spend ₹700, save ₹200, invest ₹100.", 5, 0),
            ("Spend ₹500, save ₹300, invest ₹200.", 7.5, 0),
            ("Save ₹600, invest ₹300, spend ₹100.", 10, 0),
            ("Spend it all on shopping.", 2.5, 0),
        ],
        "tip": "Budgeting ensures that your money is allocated to both needs and future goals."
    },
    {
        "question": "You earn ₹3,000 in a part-time job, and your employer deducts 10% as taxes. What do you do?",
        "options": [
            ("Ignore taxes and expect full payment.", 2.5, 0),
            ("Ask your employer to explain how taxes work.", 7.5, 0),
            ("Research taxes and plan your budget accordingly.", 10, 0),
            ("Quit the job because of the tax deduction.", 5, 0),
        ],
        "tip": "Understanding taxes is essential for managing income and planning savings."
    },
    {
        "question": "You damaged your bicycle. A friend suggests buying insurance. What do you do?",
        "options": [
            ("Ignore the advice and take the risk.", 2.5, 0),
            ("Research insurance and buy a basic plan.", 7.5, -200),
            ("Use savings to repair the bike and buy insurance.", 10, -400),
            ("Borrow money for repairs but skip insurance.", 5, -400),
        ],
        "tip": "Insurance helps manage risks and reduce unexpected financial burdens."
    },
    {
        "question": "A financial advisor introduces mutual funds. You have ₹2,000 saved. What do you do?",
        "options": [
            ("Invest ₹2,000 after researching mutual funds.", 10, 0),
            ("Invest ₹1,000 and save the rest.", 7.5, 0),
            ("Avoid investing because you're unsure.", 5, 0),
            ("Spend all ₹2,000 on personal desires.", 2.5, -2000),
        ],
        "tip": "Investing early can grow your wealth over time through compounding returns."
    },
    {
        "question": "Your friends are going to an amusement park. The ticket costs ₹800. What do you do?",
        "options": [
            ("Go to the park and postpone saving for the phone.", 5, -800),
            ("Skip the park and explain your savings goal.", 10, 0),
            ("Ask your parents for ₹800.", 2.5, 0),
            ("Split the ticket cost with a friend and still go.", 7.5, -400),
        ],
        "tip": "Setting boundaries and prioritizing long-term goals over short-term fun is crucial."
    },
    {
        "question": "A classmate needs ₹300 to buy books. You’ve saved ₹1,500. What will you do?",
        "options": [
            ("Lend ₹300 and trust them to repay.", 7.5, -300),
            ("Give ₹300 as a gift.", 10, -300),
            ("Politely decline, focusing on your goals.", 5, 0),
            ("Lend ₹300 but charge interest.", 2.5, -300),
        ],
        "tip": "Helping others is noble, but balance generosity with personal responsibilities."
    },
    {
        "question": "You’ve saved ₹5,000 for a family trip, but your phone breaks. Repair costs ₹4,000. What’s next?",
        "options": [
            ("Use trip savings to repair the phone.", 7.5, -4000),
            ("Postpone the repair and save more.", 10, 0),
            ("Borrow ₹4,000 from your parents.", 5, 0),
            ("Replace the phone with an expensive model.", 2.5, -5000),
        ],
        "tip": "Careful decisions during emergencies help minimize financial impact."
    },
    {
        "question": "You want to save for college in 5 years. How do you plan your finances?",
        "options": [
            ("Open a recurring deposit and save monthly.", 10, 0),
            ("Invest in a long-term mutual fund.", 7.5, 0),
            ("Save irregularly, whenever possible.", 5, 0),
            ("Spend money now and plan later.", 2.5, 0),
        ],
        "tip": "Setting long-term goals helps you stay focused and disciplined in financial planning."
    }
]

# Helper function to display the current round's scenario
def display_scenario(round_num):
    scenario = scenarios[round_num - 1]
    st.subheader(f"Round {round_num}")
    st.write(scenario["question"])

    for idx, (option_text, points, money_change) in enumerate(scenario["options"], start=1):
        if st.button(option_text, key=f"option_{round_num}_{idx}"):
            st.session_state.player_points += points
            st.session_state.player_money += money_change
            st.session_state.current_round += 1
            st.experimental_rerun()

    st.write(f"**Tip:** {scenario['tip']}")

# Display the current round or end the game
if st.session_state.current_round <= len(scenarios):
    display_scenario(st.session_state.current_round)
else:
    st.subheader("Game Over!")
    st.write(f"**Final Score:** {st.session_state.player_points} points")
    st.write(f"**Final Savings:** ₹{st.session_state.player_money}")
    st.write("Remember, every financial decision shapes your future. Stay informed, stay smart!")