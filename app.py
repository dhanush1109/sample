import streamlit as st

# Initialize session state variables
if "player_money" not in st.session_state:
    st.session_state.player_money = 500
if "player_points" not in st.session_state:
    st.session_state.player_points = 0
if "current_round" not in st.session_state:
    st.session_state.current_round = 1
if "game_started" not in st.session_state:
    st.session_state.game_started = False

# Welcome message and game introduction
def welcome_message():
    st.title("Welcome to Financial Pathways Simulator!")
    st.subheader("“Learn, Save, Invest, and Master Your Money Journey!”")
    st.write("In this game, you'll make financial decisions to earn points and grow your savings.")
    st.write("You start with ₹500. Make wise decisions and see how much you can save!")
    if st.button("Start the Game"):
        st.session_state.game_started = True
        st.session_state.current_round = 1
        st.session_state.player_points = 0
        st.session_state.player_money = 500

# Scenarios and options for each round
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
        "question": "Your friend’s birthday is coming up, and everyone is contributing ₹300 for a gift. What do you do?",
        "options": [
            ("Contribute ₹300 and avoid conflicts with friends.", 5, -300),
            ("Suggest a less expensive gift everyone can afford.", 7.5, 0),
            ("Politely decline to contribute, explaining your goals.", 10, 0),
            ("Borrow ₹300 and repay later.", 2.5, -300),
        ],
        "tip": "Balance social obligations with financial priorities. Be honest about your limits!"
    },
    {
        "question": "You’ve earned ₹1,000 helping your neighbor. How will you allocate it?",
        "options": [
            ("Spend ₹700, save ₹200, invest ₹100.", 5, 0),
            ("Spend ₹500, save ₹300, invest ₹200.", 7.5, 0),
            ("Save ₹600, invest ₹300, spend ₹100.", 10, 0),
            ("Spend it all on shopping.", 2.5, 0),
        ],
        "tip": "Budgeting ensures your money goes toward needs and future goals."
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
        "question": "A financial advisor introduces mutual funds. You have ₹2,000 saved. What will you do?",
        "options": [
            ("Invest ₹2,000 after researching mutual funds.", 10, -2000),
            ("Invest ₹1,000 and save the rest.", 7.5, -1000),
            ("Avoid investing because you’re unsure.", 5, 0),
            ("Spend all ₹2,000 on personal desires.", 2.5, -2000),
        ],
        "tip": "Investing early can grow your wealth over time thanks to compounding returns."
    },
    {
        "question": "Your friends are going to an amusement park for ₹800. You’re saving for a new phone. What do you do?",
        "options": [
            ("Go to the park and postpone saving for the phone.", 5, -800),
            ("Skip the park and explain your savings goal to friends.", 10, 0),
            ("Ask your parents for ₹800 to avoid missing out.", 2.5, 0),
            ("Split the ticket cost with a friend and still go.", 7.5, -400),
        ],
        "tip": "Set boundaries and prioritize long-term goals over short-term fun."
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
        "question": "Your phone breaks, and repair costs ₹4,000. What’s your next step?",
        "options": [
            ("Use your trip savings to repair the phone.", 7.5, -4000),
            ("Postpone the repair and save more.", 10, 0),
            ("Borrow ₹4,000 from your parents.", 5, 0),
            ("Replace the phone with an expensive model.", 2.5, -5000),
        ],
        "tip": "Emergencies can derail plans, but careful decisions help minimize impact."
    },
    {
        "question": "You want to save for college in 5 years. How do you plan?",
        "options": [
            ("Open a recurring deposit account and save monthly.", 10, 0),
            ("Invest in a long-term mutual fund.", 7.5, 0),
            ("Save irregularly, whenever possible.", 5, 0),
            ("Spend money now and plan later.", 2.5, 0),
        ],
        "tip": "Setting long-term goals helps you stay disciplined in financial planning."
    }
]

# Display scenario and options
def display_scenario(round_num):
    scenario = scenarios[round_num - 1]
    st.subheader(f"Round {round_num}")
    st.write(scenario["question"])

    for idx, (option_text, points, money_change) in enumerate(scenario["options"], start=1):
        if st.button(option_text, key=f"option_{round_num}_{idx}"):
            st.session_state.player_points += points
            st.session_state.player_money += money_change
            st.session_state.current_round += 1
            break

    st.write(f"**Tip:** {scenario['tip']}")

# Game logic
if st.session_state.game_started:
    if st.session_state.current_round <= len(scenarios):
        display_scenario(st.session_state.current_round)
    else:
        st.subheader("Game Over!")
        st.write(f"**Final Score:** {st.session_state.player_points} points")
        st.write(f"**Final Savings:** ₹{st.session_state.player_money}")
        st.write("Remember, every financial decision shapes your future. Stay informed, stay smart!")
        st.session_state.game_started = False
else:
    welcome_message()