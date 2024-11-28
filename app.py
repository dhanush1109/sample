import streamlit as st

# Initialize global variables
if "player_money" not in st.session_state:
    st.session_state.player_money = 500
if "player_points" not in st.session_state:
    st.session_state.player_points = 0
if "current_round" not in st.session_state:
    st.session_state.current_round = 1
if "game_started" not in st.session_state:
    st.session_state.game_started = False

# Welcome message
if not st.session_state.game_started:
    st.title("Welcome to Financial Pathways Simulator!")
    st.subheader("“Learn, Save, Invest, and Master Your Money Journey!”")
    st.write("In this game, you'll make financial decisions to earn points and grow your savings.")
    st.write("You start with ₹500. Make wise decisions and see how much you can save!")

    if st.button("Start the Game"):
        st.session_state.game_started = True
        st.session_state.current_round = 1
        st.session_state.player_points = 0
        st.session_state.player_money = 500
        st.experimental_rerun()

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
        "question": "Your friend’s birthday is coming up, and everyone is contributing ₹300. What do you do?",
        "options": [
            ("Contribute ₹300 and avoid conflicts.", 5, -300),
            ("Suggest a less expensive gift everyone can afford.", 7.5, 0),
            ("Politely decline and explain your financial goals.", 10, 0),
            ("Borrow ₹300 and repay later.", 2.5, -300),
        ],
        "tip": "Balance social obligations with financial priorities."
    },
    {
        "question": "You’ve earned ₹1,000 helping your neighbor. How will you allocate it?",
        "options": [
            ("Spend ₹700, save ₹200, invest ₹100.", 5, 0),
            ("Spend ₹500, save ₹300, invest ₹200.", 7.5, 0),
            ("Save ₹600, invest ₹300, spend ₹100.", 10, 0),
            ("Spend it all on shopping.", 2.5, -1000),
        ],
        "tip": "Budgeting ensures money is allocated to both needs and goals."
    },
    {
        "question": "You earn ₹3,000 in a job, and 10% will be deducted as taxes. What do you do?",
        "options": [
            ("Ignore taxes and expect full payment.", 2.5, 0),
            ("Ask your employer to explain taxes.", 7.5, 0),
            ("Research taxes online and plan your budget.", 10, 0),
            ("Quit the job because of the tax deduction.", 5, -3000),
        ],
        "tip": "Understanding taxes is essential for income management."
    },
    {
        "question": "You damage your bicycle. A friend suggests buying insurance. What do you do?",
        "options": [
            ("Ignore the advice and take the risk.", 2.5, 0),
            ("Research insurance and buy a basic plan.", 7.5, -200),
            ("Use savings to repair and buy insurance.", 10, -500),
            ("Borrow money for repairs and skip insurance.", 5, -300),
        ],
        "tip": "Insurance helps manage risks and reduce unexpected costs."
    },
    {
        "question": "A financial advisor introduces mutual funds. You have ₹2,000 saved. What do you do?",
        "options": [
            ("Invest ₹2,000 after research.", 10, -2000),
            ("Invest ₹1,000 and save the rest.", 7.5, -1000),
            ("Avoid investing because you’re unsure.", 5, 0),
            ("Spend all ₹2,000 on desires.", 2.5, -2000),
        ],
        "tip": "Investing early, even with small amounts, helps grow wealth."
    },
    {
        "question": "Friends are going to an amusement park for ₹800. You’re saving for a phone. What do you do?",
        "options": [
            ("Go and postpone saving for the phone.", 5, -800),
            ("Skip the park and explain your goal.", 10, 0),
            ("Ask parents for ₹800 to avoid missing out.", 2.5, 0),
            ("Split the ticket cost with a friend.", 7.5, -400),
        ],
        "tip": "Set boundaries and prioritize long-term goals."
    },
    {
        "question": "A classmate needs ₹300 for books. You’ve saved ₹1,500. What do you do?",
        "options": [
            ("Lend ₹300 and trust repayment.", 7.5, -300),
            ("Give ₹300 as a gift.", 10, -300),
            ("Politely decline to stay focused on your goals.", 5, 0),
            ("Lend ₹300 with interest.", 2.5, -300),
        ],
        "tip": "Helping others is noble but balance generosity with responsibility."
    },
    {
        "question": "Your phone repair costs ₹4,000. You’ve saved ₹5,000 for a trip. What’s next?",
        "options": [
            ("Use savings to repair the phone.", 7.5, -4000),
            ("Postpone the repair and save more.", 10, 0),
            ("Borrow ₹4,000 from parents.", 5, 0),
            ("Replace the phone with an expensive model.", 2.5, -10000),
        ],
        "tip": "Emergencies can derail plans, but careful choices minimize impact."
    },
    {
        "question": "You want to save for college in 5 years. What’s your plan?",
        "options": [
            ("Open a recurring deposit account.", 10, 0),
            ("Invest in a long-term mutual fund.", 7.5, 0),
            ("Save irregularly, whenever possible.", 5, 0),
            ("Spend now and plan later.", 2.5, 0),
        ],
        "tip": "Long-term goals require focus and disciplined saving."
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
            st.stop()  # Stops execution to avoid proceeding prematurely.

    st.write(f"**Tip:** {scenario['tip']}")

# Display the current round or end the game
if st.session_state.game_started:
    if st.session_state.current_round <= len(scenarios):
        display_scenario(st.session_state.current_round)
    else:
        st.subheader("Game Over!")
        st.write(f"**Final Score:** {st.session_state.player_points} points")
        st.write(f"**Final Savings:** ₹{st.session_state.player_money}")
        st.write("Remember, every financial decision shapes your future. Stay informed, stay smart!")
        st.session_state.game_started = False