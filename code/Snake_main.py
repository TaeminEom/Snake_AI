import pygame as pg
import numpy as np
import random as rd

from snake import Snake, SCREEN_SIZE, PIXEL_SIZE

pg.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

size = [SCREEN_SIZE * PIXEL_SIZE, SCREEN_SIZE * PIXEL_SIZE + 30]
screen = pg.display.set_mode(size)

pg.display.set_caption("Snake Game")

clock = pg.time.Clock()

gap = int(PIXEL_SIZE / 10)

done = False


def drawing_game(A, screen, gap, PIXEL_SIZE, BLUE, BLACK, WHITE, GREEN, num):
    screen.fill(BLACK)

    for i in range(SCREEN_SIZE + 1):
        pg.draw.line(screen, WHITE, [0, 30 + i * PIXEL_SIZE], [SCREEN_SIZE * PIXEL_SIZE, 30 + i * PIXEL_SIZE], 1)
        pg.draw.line(screen, WHITE, [i * PIXEL_SIZE, 30], [i * PIXEL_SIZE, 30 + SCREEN_SIZE * PIXEL_SIZE], 1)

    for i in range(A.lenth - 1):
        if (A.snake_body[i][0] == A.snake_body[i + 1][0] and A.snake_body[i][1] - A.snake_body[i + 1][1] == 1):
            pg.draw.rect(screen, BLUE, [int(A.snake_body[i][0]) * PIXEL_SIZE + gap,
                                        30 + int(A.snake_body[i][1] + 1) * PIXEL_SIZE - gap, PIXEL_SIZE - 2 * gap,
                                        -PIXEL_SIZE])
        if (A.snake_body[i][0] == A.snake_body[i + 1][0] and A.snake_body[i][1] - A.snake_body[i + 1][1] == -1):
            pg.draw.rect(screen, BLUE,
                         [int(A.snake_body[i][0]) * PIXEL_SIZE + gap, 30 + int(A.snake_body[i][1]) * PIXEL_SIZE + gap,
                          PIXEL_SIZE - 2 * gap, PIXEL_SIZE])
        if (A.snake_body[i][1] == A.snake_body[i + 1][1] and A.snake_body[i][0] - A.snake_body[i + 1][0] == 1):
            pg.draw.rect(screen, BLUE, [int(A.snake_body[i][0] + 1) * PIXEL_SIZE - gap,
                                        30 + int(A.snake_body[i][1]) * PIXEL_SIZE + gap, -PIXEL_SIZE,
                                        PIXEL_SIZE - 2 * gap])
        if (A.snake_body[i][1] == A.snake_body[i + 1][1] and A.snake_body[i][0] - A.snake_body[i + 1][0] == -1):
            pg.draw.rect(screen, BLUE,
                         [int((A.snake_body[i][0]) * PIXEL_SIZE + gap), 30 + int(A.snake_body[i][1]) * PIXEL_SIZE + gap,
                          PIXEL_SIZE, PIXEL_SIZE - 2 * gap])
    pg.draw.rect(screen, BLUE,
                 [int(A.snake_body[i + 1][0]) * PIXEL_SIZE + gap, 30 + int(A.snake_body[i + 1][1]) * PIXEL_SIZE + gap,
                  PIXEL_SIZE - 2 * gap, PIXEL_SIZE - 2 * gap])

    pg.draw.rect(screen, GREEN,
                 [int(A.prey_position[0]) * PIXEL_SIZE + gap, 30 + int(A.prey_position[1]) * PIXEL_SIZE + gap,
                  PIXEL_SIZE - 2 * gap, PIXEL_SIZE - 2 * gap])

    text_to_screen(screen, "세대 : {} / 객체 : {} / 점수 : {}".format(generation, num, int(score[num-1]/10-1)), 10, 5, 15, WHITE)

    pg.display.flip()

def input_setting(A):  # 16개 배열
    neural_input = [[A.check_wall_straight], [A.check_wall_right], [A.check_wall_left], [A.check_prey_straight],
                    [A.check_prey_right], [A.check_prey_left]]
    neural_input += [[A.check_body_straight], [A.check_body_right], [A.check_body_left]]
    neural_input += [[A.check_body_straight_number], [A.check_body_right_number], [A.check_body_left_number]]
    neural_input += [[A.check_prey_quadrant[0]], [A.check_prey_quadrant[1]], [A.check_prey_quadrant[2]],
                     [A.check_prey_quadrant[3]]]
    return np.array(neural_input)

def set_score(A, score):
    best_score_object = 0
    for i in range(1, A_len):
        if score[best_score_object] < score[i]:
            best_score_object = i
    # score_distance_array = [0점인 객체], [1점인 객체], [2점인 객체], ...
    # [n점인 객체] = [첫번째로 짧게 이동한 객체의 번호, 두번째로 짧게 이동한 객체의 번호, ...]
    score_distance_array = np.full((int(score[best_score_object] / A_len) + 1, 1), -1)
    score_distance_array = score_distance_array.tolist()

    for i in range(A_len):  # score_distance_array에 따라 객체번호를 배열
        prey_count = int(score[i] / A_len)
        if score_distance_array[prey_count] == -1:
            score_distance_array[prey_count] = i
        else:
            score_distance_array[prey_count].append(i)

    for i in range(0, int(score[best_score_object] / 50) + 1):
        if len(score_distance_array[i]) == 1:  # 리스트의 길이가 1이면 정렬을 할 필요가 없음
            continue
        for j in range(len(score_distance_array[i])):  # 각 객체번호가 나열된 리스트에서 이동거리가 작은 순으로 삽입정렬
            lowest_distance_address = j + 1
            for k in range(j + 2, len(score_distance_array[i])):
                dis_1 = score[score_distance_array[i][lowest_distance_address]]
                dis_2 = score[score_distance_array[i][k]]
                if dis_1 > dis_2:
                    lowest_distance_address = k
            temp = score_distance_array[i][j]
            score_distance_array[i][j] = score_distance_array[i][lowest_distance_address]
            score_distance_array[i][lowest_distance_address] = temp

    tscore = np.zeros(A_len)
    score_distance_array_shape = list_shape(score_distance_array)
    for i in range(score_distance_array_shape[0]):
        if score_distance_array[i][0] == -1:
            continue
        for j in range(len(score_distance_array[i])):
            tscore[score_distance_array[i][j]] = score[score_distance_array[i][j]] + 50 - j

    return tscore

def list_shape(arr):
    arr = np.array(arr)
    return arr.shape

def random_choice(a, b):
    if rd.random() > 0.7:
        return a
    else:
        return b

def initial_setting():
    global w1
    global w2

    w1 = np.random.randn(A_len, 16, 16)
    w2 = np.random.randn(A_len, 3, 16)

def gen(num_to_next, num_output):
    score_bundle = []
    for i in range(num_output+num_to_next):
        score_bundle += [i] * score[i]

    tw1 = np.zeros((num_output, 16, 16))
    tw2 = np.zeros((num_output, 3, 16))

    for i in range(num_output):
        select1 = score_bundle[rd.randint(0, len(score_bundle) - 1)]
        select2 = score_bundle[rd.randint(0, len(score_bundle) - 1)]

        for j in range(16):  # 가중치
            for k in range(16):
                tw1[i][j][k] = random_choice(w1[select1][j][k], w1[select2][j][k])
            for k in range(3):
                tw2[i][k][j] = random_choice(w2[select1][k][j], w2[select2][k][j])

    for i in range(num_output):
        w1[num_to_next + i] = tw1[i]
        w2[num_to_next + i] = tw2[i]
    '''
    for i in range(num_output):
        for j in range(16):
            for k in range(16):
                if rd.random() < 0.1:
                    w1[num_to_next + i][j][k] = rd.random() * 4 - 2
            for k in range(3):
                if rd.random() < 0.1:
                    w2[num_to_next + i][k][j] = rd.random() * 4 - 2
    '''

def relu(arr):
    return arr * (arr > 0)

def softmax(arr):
    return np.exp(arr) / np.sum(np.exp(arr))

def neural_network(input, num):
    ww1 = w1[num]
    ww2 = w2[num]
    if weight_num == 1:
        neural = np.matmul(ww2, input)
        neural = relu(neural)
        neural = softmax(neural)
    if weight_num == 2:
        neural = np.matmul(ww1, input)
        neural = relu(neural)
        neural = softmax(neural)
        neural = np.matmul(ww2, neural)
        neural = relu(neural)
    
    result = [neural[0][0]] + [neural[1][0]] + [neural[2][0]]
    if result[0] >= result[1] and result[0] >= result[2]:
        return "s"
    if result[1] > result[0] and result[1] > result[2]:
        return "r"
    if result[2] > result[0] and result[2] > result[1]:
        return "l"

def text_to_screen(screen, text, x, y, size, color, font_type="NanumSquareRoundB.ttf"):
    text = str(text)
    font = pg.font.Font(font_type, size)
    text = font.render(text, True, color)
    screen.blit(text, (x, y))

def gen_to_next(A_len, score, num_to_next):
    arr = np.zeros(A_len)
    for i in range(A_len):
        arr[i] = i
    for i in range(num_to_next):
        best = i
        for j in range(i + 1, A_len):
            a = score[int(arr[best])]
            b = score[int(arr[j])]
            if a < b:
                best = j
        temp = arr[i]
        arr[i] = arr[best]
        arr[best] = temp

    temp = []
    for i in range(num_to_next):
        temp = w1[i]
        w1[i] = w1[int(arr[i])]
        w1[int(arr[i])] = temp
        temp = w2[i]
        w2[i] = w2[int(arr[i])]
        w2[int(arr[i])] = temp

def number_set(num1, num2, d):
    print("[", end="")
    if num1 < 10:
        print("0", end="")
    print("%.2f, " % (num1), end="")
    print("%.2f, " % (d * 10), end="")
    print("%2d" % (num2), end="], ")

def retrieve(name):
    file = open(name, "r")
    read = file.read()
    read = read.split("\n")
    temp = []
    for i in range(len(read)):
        if read[i] == '':
            temp += [i]
    for i in reversed(temp):
        del read[i]
    for i in range(len(read)):
        read[i] = read[i].split(" ")
    for i in range(A_len):
        for j in range(16):
            for k in range(16):
                w1[i][j][k] = float(read[i * 16 + j][k])
    for i in range(A_len):
        for j in range(3):
            for k in range(16):
                w2[i][j][k] = float(read[A_len * 16 + i * 3 + j][k])

def save(A_len, weight_num, score_mean_r, score_mean, score_best):
    file = open("save_weight_" + "%d_" % (weight_num) + str(score_mean_r) + ".txt", 'w')
    for i in range(A_len):
        for j in range(16):
            for k in range(16):
                file.write("{} ".format(w1[i][j][k]))
            file.write("\n")
        file.write("\n")

    file.write("\n")
    for i in range(A_len):
        for j in range(3):
            for k in range(16):
                file.write("{} ".format(w2[i][j][k]))
            file.write("\n")
        file.write("\n")
    file.write("socre_mean : " + str(score_mean) + "\n")
    file.write("score_best : " + str(score_best) + "\n")
    file.close()

def round_dot1(num):
	return round(num * 100 - num * 100 % 1) / 100

def set_deviation(A_len):
    mw1 = w1.sum(axis=0) / A_len
    mw2 = w2.sum(axis=0) / A_len

    dw1 = np.zeros((16, 16))
    dw2 = np.zeros((3, 16))
    for i in range(A_len):
        for j in range(16):
            for k in range(16):
                dw1[j][k] += abs(mw1[j][k] - w1[i][j][k])
    dw1 /= A_len
    for i in range(A_len):
        for j in range(3):
            for k in range(16):
                dw2[j][k] += abs(mw2[j][k] - w2[i][j][k])
    dw2 /= A_len

    deviation = (np.sum(dw1) + np.sum(dw2)) / (16 * 16 + 3 * 16)
    return deviation

num_to_next = 10  # 다음 세대로 이동할 상위 개체수
num_output = 40  # 생성 될 자손의 수

A_len = num_to_next + num_output

generation = 0
confirm = 0

print("몇개의 가중치 연결망을 사용하실 건가요?(1 or 2) : ", end="")
global weight_num
weight_num = int(input())
print("저장된 가중치 정보를 불러올까요?(Y or N) : ", end="")
check = input().upper()
if check == 'Y':
    print("저장된 가중치 파일의 이름을 입력해 주세요. : ", end="")
    name = input()
generation_limit = int(input("한 개체군이 진행할 세대의 횟수를 적어주세요.(30 , 45, ext...) : "))
A_len = int(input("한 개체군의 개체수를 입력해 주세요.(10, 50, 100, ext...) : "))
num_to_next = int(A_len/5)
num_output = A_len - num_to_next
loof_check = input("한 개체군의 총 발전이 끝난 후 다른 개체군을 계속 학습시킬까요?(Y or N) : ").upper()



print("z:가속하기")
print("x:감속하기")
print("c:가속하고 화면 출력하지 않기 : 더 빨라짐")
print("v:c의 역할 수행 + 한 세대 끝나면 감속함")
print("[평균점수, 평균편차, 최고점수]")
roof = 0
global score
while not done:
    roof += 1
    generation = 0
    initial_setting()
    if check == 'Y' and roof == 1:
        retrieve(name)
    score_mean = []
    score_best = []
    while not done and generation < generation_limit:
        score = np.full(A_len, 10)
        generation += 1
        if confirm == -2:
            confirm = 1
        for i in range(A_len):
            A = []
            A = Snake()
            position_record = []
            next = False
            while not A.check_die() and not done and not next:
                for event in pg.event.get():  # X를 누를 시 종료
                    if event.type == pg.QUIT:
                        done = True
                    if event.type == pg.KEYDOWN:
                        if event.key == ord('z'):
                            confirm = 0
                        if event.key == ord('x'):
                            confirm = 1
                        if event.key == ord('c'):
                            confirm = -1
                        if event.key == ord('v'):
                            confirm = -2

                if confirm == 1:
                    pg.time.delay(int(1000 / 60))
                if confirm == 0:
                    pg.time.delay(1)

                position_record.append(A.snake_body[0].tolist())
                record_lenth = list_shape(position_record)
                record_lenth = record_lenth[0]
                count = 0
                for j in range(0, record_lenth - 1):
                    if A.snake_body[0].tolist() == position_record[j]:
                        count += 1
                if count > 5:
                    next = True

                if (A.snake_body[0].tolist() == A.prey_position.tolist()):  # 먹이를 먹을 시 길이 증가
                    A.lenth += 1
                    A.snake_body[A.lenth - 1] = A.L[0]
                    A.prey_set()
                    score[i] += A_len / 5
                    position_record = []

                neural_input = input_setting(A)
                output = neural_network(neural_input, i)
                if output == "s":  # 신경망을 통해 결과 도출
                    A.straight()
                if output == "r":
                    A.right()
                if output == "l":
                    A.left()
                A.reset_value()
                A.set_value()
                if confirm != -1 and confirm != -2:
                    drawing_game(A, screen, gap, PIXEL_SIZE, BLUE, BLACK, WHITE, GREEN, i + 1)

        score_mean += [(np.sum(score) - 500) / (10 * A_len)]
        if len(score_mean) % 10 == 1 and len(score_mean) != 1:
            print("")
        temp = score[0]
        for i in score:
            if i > temp:
                temp = i
        score_best += [int(temp / 10 - 1)]
        number_set(score_mean[len(score_mean) - 1], score_best[len(score_best) - 1], set_deviation(A_len))
        # score = set_score(score)
        if done == False:
            gen_to_next(A_len, score, num_to_next)
            gen(num_to_next, num_output)

    print("\n")
    del score_mean[len(score_mean) - 1]
    del score_best[len(score_best) - 1]
    score_mean_recent = 0
    for i in range(len(score_mean) - 5, len(score_mean)):
        score_mean_recent += score_mean[i]
    score_mean_recent = (score_mean_recent / 5)
    score_mean_recent = round_dot1(score_mean_recent)

    save(A_len, weight_num, score_mean_recent, score_mean, score_best)
    if loof_check == "Y":
        continue
    break

pg.quit()