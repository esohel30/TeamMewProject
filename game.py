from api import generatecharacterquestion

SCORE = 0
QUESTION_NUM = 1
ANSWER = ''

def play_superhero_game(is_new_game):
    # if is_new_game:

    quesiton_data = generatecharacterquestion()

def check_answer(user_answer):
    global ANSWER, SCORE, QUESTION_NUM
    if ANSWER == user_answer:
        SCORE += 1
    QUESTION_NUM += 1
    print(f'question# in game.py: {QUESTION_NUM}')
    return ANSWER == user_answer