from api import generatecharacterquestion

score = 0
question_num = 1
answer = ''
stat_type = ''

# [statname, [char1name, char1imgurl, char1stat], [char2name, char2imgurl, char2stat]]
def play_superhero_game():
    global answer, stat_type
    quesiton_data = generatecharacterquestion()
    name1, img1, stat1 = quesiton_data[1]
    name2, img2, stat2 = quesiton_data[2]

    if stat1 > stat2:
        answer = name1
    elif stat1 < stat2:
        answer = name2
    else:
        answer = 'both'     # both choices are right for ties
    stat_type = quesiton_data[0]
    return ((name1, img1), (name2, img2))

def get_score():
    return score

def get_question_num():
    return question_num

def get_stat_type():
    return stat_type

def check_answer(user_answer):
    global answer, score, question_num
    if answer == user_answer or answer == 'both':
        score += 1
    question_num += 1
    print(f'question# in game.py: {question_num}')
    return answer == user_answer

def change_answer(new_ans):
    global answer
    answer = new_ans

def reset():
    global answer, score, question_num, stat_type
    score = 0
    question_num = 1
    answer = ''
    stat_type = ''