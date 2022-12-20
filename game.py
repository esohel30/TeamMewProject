from api import generatecharacterquestion

score = 0
question_num = 1
answer = ''
stat_type = ''
playing_a_game = False

# [statname, [char1name, char1imgurl, char1stat], [char2name, char2imgurl, char2stat]]
def play_superhero_game():
    global answer, stat_type,playing_a_game
    quesiton_data = generatecharacterquestion()
    name1, img1, stat1 = quesiton_data[1]
    name2, img2, stat2 = quesiton_data[2]

    playing_a_game = True

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

def increment_score():
    global score
    score +=1
    
def increment_qnum():
    global question_num
    question_num += 1

def check_answer(user_answer):
    global answer, score, question_num
    if answer == user_answer or answer == 'both':
        increment_score()
    increment_qnum()
    print(f'question# in game.py: {question_num}')
    return answer == user_answer

def pokemon_check_answer(user_answer, correct_answer):
    global answer, score, question_num
    iscorrect = False
    userans = user_answer.lower()
    if len(correct_answer) > 1:
        str_correct = str(correct_answer[0]) + str(correct_answer[1])
        if "/" in str_correct: #Later do some error handling and other fixing of code for situations if user inputs invalid stuff
            if "/" in userans:
                if userans.split("/")[0] in str_correct and userans.split("/")[1] in str_correct:
                    increment_score()
                    iscorrect = True
        elif str_correct == userans:
            increment_score()
            iscorrect = True
    else:
        if userans == correct_answer[0]:
            increment_score()
            iscorrect = True
    increment_qnum()
    return iscorrect
        

def playing_game():
    return playing_a_game
        

def change_answer(new_ans):
    global answer
    answer = new_ans

def reset():
    global answer, score, question_num, stat_type, playing_a_game
    score = 0
    question_num = 1
    answer = ''
    stat_type = ''
    playing_a_game = False