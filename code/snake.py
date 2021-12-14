import numpy as np
import math
import random as rd

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

SCREEN_SIZE = 25  # 9이상의 홀수여야함
PIXEL_SIZE = 20


def array_compare(a, b):
    if a.tolist() == b.tolist():
        return True
    else:
        return False


class Snake():

    def __init__(self):
        self.set_body(3)

        self.snake_direction = 90  # (0)동 (180)서 (270)남 (90)북
        self.check_wall_straight = -1
        self.check_wall_right = -1
        self.check_wall_left = -1

        self.check_prey_straight = -1
        self.check_prey_right = -1
        self.check_prey_left = -1

        self.check_body_straight = -1
        self.check_body_right = -1
        self.check_body_left = -1

        self.check_body_straight_number = -1
        self.check_body_right_number = -1
        self.check_body_left_number = -1

        self.prey_relative_position = np.zeros(2)
        self.check_prey_quadrant = np.full(4, 1)

        self.distance = 0
        self.prey_set()
        self.L = np.zeros((2, 2))
        self.L[1] = self.snake_body[1]

    def set_body(self, len):
        self.lenth = len
        self.snake_body = np.zeros((900, 2))

        self.snake_body[0] = [(SCREEN_SIZE + 1) / 2, (SCREEN_SIZE + 1) / 2]
        self.snake_body[1] = [(SCREEN_SIZE + 1) / 2, (SCREEN_SIZE + 1) / 2 + 1]
        self.snake_body[2] = [(SCREEN_SIZE + 1) / 2, (SCREEN_SIZE + 1) / 2 + 2]
        self.snake_body[3] = [(SCREEN_SIZE + 1) / 2, (SCREEN_SIZE + 1) / 2 + 3]
        self.snake_body[4] = [(SCREEN_SIZE + 1) / 2, (SCREEN_SIZE + 1) / 2 + 4]
        self.snake_body[5] = [(SCREEN_SIZE + 1) / 2, (SCREEN_SIZE + 1) / 2 + 5]
        self.snake_body[6] = [(SCREEN_SIZE + 1) / 2, (SCREEN_SIZE + 1) / 2 + 6]
        self.snake_body[7] = [(SCREEN_SIZE + 1) / 2, (SCREEN_SIZE + 1) / 2 + 7]
        self.snake_body[8] = [(SCREEN_SIZE + 1) / 2, (SCREEN_SIZE + 1) / 2 + 8]
        self.snake_body[9] = [(SCREEN_SIZE + 1) / 2, (SCREEN_SIZE + 1) / 2 + 9]
        self.snake_body[10] = [(SCREEN_SIZE + 1) / 2, (SCREEN_SIZE + 1) / 2 + 10]
        self.snake_body[11] = [(SCREEN_SIZE + 1) / 2, (SCREEN_SIZE + 1) / 2 + 11]
        self.snake_body[12] = [(SCREEN_SIZE + 1) / 2 + 1, (SCREEN_SIZE + 1) / 2 + 11]
        self.snake_body[13] = [(SCREEN_SIZE + 1) / 2 + 2, (SCREEN_SIZE + 1) / 2 + 11]
        self.snake_body[14] = [(SCREEN_SIZE + 1) / 2 + 3, (SCREEN_SIZE + 1) / 2 + 11]
        self.snake_body[15] = [(SCREEN_SIZE + 1) / 2 + 4, (SCREEN_SIZE + 1) / 2 + 11]
        self.snake_body[16] = [(SCREEN_SIZE + 1) / 2 + 5, (SCREEN_SIZE + 1) / 2 + 11]
        self.snake_body[17] = [(SCREEN_SIZE + 1) / 2 + 6, (SCREEN_SIZE + 1) / 2 + 11]
        self.snake_body[18] = [(SCREEN_SIZE + 1) / 2 + 7, (SCREEN_SIZE + 1) / 2 + 11]
        self.snake_body[19] = [(SCREEN_SIZE + 1) / 2 + 8, (SCREEN_SIZE + 1) / 2 + 11]
        self.snake_body[20] = [(SCREEN_SIZE + 1) / 2 + 9, (SCREEN_SIZE + 1) / 2 + 11]
        self.snake_body[21] = [(SCREEN_SIZE + 1) / 2 + 10, (SCREEN_SIZE + 1) / 2 + 11]
        self.snake_body[22] = [(SCREEN_SIZE + 1) / 2 + 11, (SCREEN_SIZE + 1) / 2 + 11]
        self.snake_body[23] = [(SCREEN_SIZE + 1) / 2 + 11, (SCREEN_SIZE + 1) / 2 + 10]
        self.snake_body[24] = [(SCREEN_SIZE + 1) / 2 + 11, (SCREEN_SIZE + 1) / 2 + 9]
        self.snake_body[25] = [(SCREEN_SIZE + 1) / 2 + 11, (SCREEN_SIZE + 1) / 2 + 8]
        self.snake_body[26] = [(SCREEN_SIZE + 1) / 2 + 11, (SCREEN_SIZE + 1) / 2 + 7]
        self.snake_body[27] = [(SCREEN_SIZE + 1) / 2 + 11, (SCREEN_SIZE + 1) / 2 + 6]
        self.snake_body[28] = [(SCREEN_SIZE + 1) / 2 + 11, (SCREEN_SIZE + 1) / 2 + 5]
        self.snake_body[29] = [(SCREEN_SIZE + 1) / 2 + 11, (SCREEN_SIZE + 1) / 2 + 4]
        self.snake_body[30] = [(SCREEN_SIZE + 1) / 2 + 11, (SCREEN_SIZE + 1) / 2 + 3]
        self.snake_body[31] = [(SCREEN_SIZE + 1) / 2 + 11, (SCREEN_SIZE + 1) / 2 + 2]
        self.snake_body[32] = [(SCREEN_SIZE + 1) / 2 + 11, (SCREEN_SIZE + 1) / 2 + 1]
        self.snake_body[33] = [(SCREEN_SIZE + 1) / 2 + 11, (SCREEN_SIZE + 1) / 2]
        self.snake_body[34] = [(SCREEN_SIZE + 1) / 2 + 10, (SCREEN_SIZE + 1) / 2]
        self.snake_body[35] = [(SCREEN_SIZE + 1) / 2 + 10, (SCREEN_SIZE + 1) / 2 + 1]
        self.snake_body[36] = [(SCREEN_SIZE + 1) / 2 + 10, (SCREEN_SIZE + 1) / 2 + 2]
        self.snake_body[37] = [(SCREEN_SIZE + 1) / 2 + 10, (SCREEN_SIZE + 1) / 2 + 3]
        self.snake_body[38] = [(SCREEN_SIZE + 1) / 2 + 10, (SCREEN_SIZE + 1) / 2 + 4]
        self.snake_body[39] = [(SCREEN_SIZE + 1) / 2 + 10, (SCREEN_SIZE + 1) / 2 + 5]
        self.snake_body[40] = [(SCREEN_SIZE + 1) / 2 + 10, (SCREEN_SIZE + 1) / 2 + 6]
        self.snake_body[41] = [(SCREEN_SIZE + 1) / 2 + 10, (SCREEN_SIZE + 1) / 2 + 7]
        self.snake_body[42] = [(SCREEN_SIZE + 1) / 2 + 10, (SCREEN_SIZE + 1) / 2 + 8]
        self.snake_body[43] = [(SCREEN_SIZE + 1) / 2 + 10, (SCREEN_SIZE + 1) / 2 + 9]
        self.snake_body[44] = [(SCREEN_SIZE + 1) / 2 + 10, (SCREEN_SIZE + 1) / 2 + 10]
        self.snake_body[45] = [(SCREEN_SIZE + 1) / 2 + 10, (SCREEN_SIZE + 1) / 2 + 11]
        self.snake_body[46] = [(SCREEN_SIZE + 1) / 2 + 9, (SCREEN_SIZE + 1) / 2 + 11]
        self.snake_body[47] = [(SCREEN_SIZE + 1) / 2 + 9, (SCREEN_SIZE + 1) / 2 + 10]
        self.snake_body[48] = [(SCREEN_SIZE + 1) / 2 + 9, (SCREEN_SIZE + 1) / 2 + 9]
        self.snake_body[49] = [(SCREEN_SIZE + 1) / 2 + 9, (SCREEN_SIZE + 1) / 2 + 8]
        self.snake_body[50] = [(SCREEN_SIZE + 1) / 2 + 9, (SCREEN_SIZE + 1) / 2 + 7]
        self.snake_body[51] = [(SCREEN_SIZE + 1) / 2 + 9, (SCREEN_SIZE + 1) / 2 + 6]
        self.snake_body[52] = [(SCREEN_SIZE + 1) / 2 + 9, (SCREEN_SIZE + 1) / 2 + 5]
        self.snake_body[53] = [(SCREEN_SIZE + 1) / 2 + 9, (SCREEN_SIZE + 1) / 2 + 4]
        self.snake_body[54] = [(SCREEN_SIZE + 1) / 2 + 9, (SCREEN_SIZE + 1) / 2 + 3]
        self.snake_body[55] = [(SCREEN_SIZE + 1) / 2 + 9, (SCREEN_SIZE + 1) / 2 + 2]
        self.snake_body[56] = [(SCREEN_SIZE + 1) / 2 + 9, (SCREEN_SIZE + 1) / 2 + 1]
        self.snake_body[57] = [(SCREEN_SIZE + 1) / 2 + 9, (SCREEN_SIZE + 1) / 2]
        self.snake_body[58] = [(SCREEN_SIZE + 1) / 2 + 8, (SCREEN_SIZE + 1) / 2]
        self.snake_body[59] = [(SCREEN_SIZE + 1) / 2 + 8, (SCREEN_SIZE + 1) / 2 + 1]
        self.snake_body[60] = [(SCREEN_SIZE + 1) / 2 + 8, (SCREEN_SIZE + 1) / 2 + 2]
        self.snake_body[61] = [(SCREEN_SIZE + 1) / 2 + 8, (SCREEN_SIZE + 1) / 2 + 3]
        self.snake_body[62] = [(SCREEN_SIZE + 1) / 2 + 8, (SCREEN_SIZE + 1) / 2 + 4]
        self.snake_body[63] = [(SCREEN_SIZE + 1) / 2 + 8, (SCREEN_SIZE + 1) / 2 + 5]
        self.snake_body[64] = [(SCREEN_SIZE + 1) / 2 + 8, (SCREEN_SIZE + 1) / 2 + 6]
        self.snake_body[65] = [(SCREEN_SIZE + 1) / 2 + 8, (SCREEN_SIZE + 1) / 2 + 7]
        self.snake_body[66] = [(SCREEN_SIZE + 1) / 2 + 8, (SCREEN_SIZE + 1) / 2 + 8]
        self.snake_body[67] = [(SCREEN_SIZE + 1) / 2 + 8, (SCREEN_SIZE + 1) / 2 + 9]
        self.snake_body[68] = [(SCREEN_SIZE + 1) / 2 + 8, (SCREEN_SIZE + 1) / 2 + 10]
        self.snake_body[69] = [(SCREEN_SIZE + 1) / 2 + 8, (SCREEN_SIZE + 1) / 2 + 11]
        self.snake_body[70] = [(SCREEN_SIZE + 1) / 2 + 7, (SCREEN_SIZE + 1) / 2 + 11]
        self.snake_body[71] = [(SCREEN_SIZE + 1) / 2 + 7, (SCREEN_SIZE + 1) / 2 + 10]
        self.snake_body[72] = [(SCREEN_SIZE + 1) / 2 + 7, (SCREEN_SIZE + 1) / 2 + 9]
        self.snake_body[73] = [(SCREEN_SIZE + 1) / 2 + 7, (SCREEN_SIZE + 1) / 2 + 8]
        self.snake_body[74] = [(SCREEN_SIZE + 1) / 2 + 7, (SCREEN_SIZE + 1) / 2 + 7]
        self.snake_body[75] = [(SCREEN_SIZE + 1) / 2 + 7, (SCREEN_SIZE + 1) / 2 + 6]
        self.snake_body[76] = [(SCREEN_SIZE + 1) / 2 + 7, (SCREEN_SIZE + 1) / 2 + 5]
        self.snake_body[77] = [(SCREEN_SIZE + 1) / 2 + 7, (SCREEN_SIZE + 1) / 2 + 4]
        self.snake_body[78] = [(SCREEN_SIZE + 1) / 2 + 7, (SCREEN_SIZE + 1) / 2 + 3]
        self.snake_body[79] = [(SCREEN_SIZE + 1) / 2 + 7, (SCREEN_SIZE + 1) / 2 + 2]
        self.snake_body[80] = [(SCREEN_SIZE + 1) / 2 + 7, (SCREEN_SIZE + 1) / 2 + 1]
        self.snake_body[81] = [(SCREEN_SIZE + 1) / 2 + 7, (SCREEN_SIZE + 1) / 2]
        self.snake_body[82] = [(SCREEN_SIZE + 1) / 2 + 6, (SCREEN_SIZE + 1) / 2]
        self.snake_body[83] = [(SCREEN_SIZE + 1) / 2 + 6, (SCREEN_SIZE + 1) / 2 + 1]
        self.snake_body[84] = [(SCREEN_SIZE + 1) / 2 + 6, (SCREEN_SIZE + 1) / 2 + 2]
        self.snake_body[85] = [(SCREEN_SIZE + 1) / 2 + 6, (SCREEN_SIZE + 1) / 2 + 3]
        self.snake_body[86] = [(SCREEN_SIZE + 1) / 2 + 6, (SCREEN_SIZE + 1) / 2 + 4]
        self.snake_body[87] = [(SCREEN_SIZE + 1) / 2 + 6, (SCREEN_SIZE + 1) / 2 + 5]
        self.snake_body[88] = [(SCREEN_SIZE + 1) / 2 + 6, (SCREEN_SIZE + 1) / 2 + 6]
        self.snake_body[89] = [(SCREEN_SIZE + 1) / 2 + 6, (SCREEN_SIZE + 1) / 2 + 7]
        self.snake_body[90] = [(SCREEN_SIZE + 1) / 2 + 6, (SCREEN_SIZE + 1) / 2 + 8]
        self.snake_body[91] = [(SCREEN_SIZE + 1) / 2 + 6, (SCREEN_SIZE + 1) / 2 + 9]
        self.snake_body[92] = [(SCREEN_SIZE + 1) / 2 + 6, (SCREEN_SIZE + 1) / 2 + 10]
        self.snake_body[93] = [(SCREEN_SIZE + 1) / 2 + 6, (SCREEN_SIZE + 1) / 2 + 11]
        self.snake_body[94] = [(SCREEN_SIZE + 1) / 2 + 5, (SCREEN_SIZE + 1) / 2 + 11]
        self.snake_body[95] = [(SCREEN_SIZE + 1) / 2 + 5, (SCREEN_SIZE + 1) / 2 + 10]
        self.snake_body[96] = [(SCREEN_SIZE + 1) / 2 + 5, (SCREEN_SIZE + 1) / 2 + 9]
        self.snake_body[97] = [(SCREEN_SIZE + 1) / 2 + 5, (SCREEN_SIZE + 1) / 2 + 8]
        self.snake_body[98] = [(SCREEN_SIZE + 1) / 2 + 5, (SCREEN_SIZE + 1) / 2 + 7]
        self.snake_body[99] = [(SCREEN_SIZE + 1) / 2 + 5, (SCREEN_SIZE + 1) / 2 + 6]
        self.snake_body[100] = [(SCREEN_SIZE + 1) / 2 + 5, (SCREEN_SIZE + 1) / 2 + 5]
        self.snake_body[101] = [(SCREEN_SIZE + 1) / 2 + 5, (SCREEN_SIZE + 1) / 2 + 4]
        self.snake_body[102] = [(SCREEN_SIZE + 1) / 2 + 5, (SCREEN_SIZE + 1) / 2 + 3]
        self.snake_body[103] = [(SCREEN_SIZE + 1) / 2 + 5, (SCREEN_SIZE + 1) / 2 + 2]
        self.snake_body[104] = [(SCREEN_SIZE + 1) / 2 + 5, (SCREEN_SIZE + 1) / 2 + 1]
        self.snake_body[105] = [(SCREEN_SIZE + 1) / 2 + 5, (SCREEN_SIZE + 1) / 2]
        self.snake_body[106] = [(SCREEN_SIZE + 1) / 2 + 4, (SCREEN_SIZE + 1) / 2]
        self.snake_body[107] = [(SCREEN_SIZE + 1) / 2 + 4, (SCREEN_SIZE + 1) / 2 + 1]
        self.snake_body[108] = [(SCREEN_SIZE + 1) / 2 + 4, (SCREEN_SIZE + 1) / 2 + 2]
        self.snake_body[109] = [(SCREEN_SIZE + 1) / 2 + 4, (SCREEN_SIZE + 1) / 2 + 3]
        self.snake_body[110] = [(SCREEN_SIZE + 1) / 2 + 4, (SCREEN_SIZE + 1) / 2 + 4]
        self.snake_body[111] = [(SCREEN_SIZE + 1) / 2 + 4, (SCREEN_SIZE + 1) / 2 + 5]
        self.snake_body[112] = [(SCREEN_SIZE + 1) / 2 + 4, (SCREEN_SIZE + 1) / 2 + 6]
        self.snake_body[113] = [(SCREEN_SIZE + 1) / 2 + 4, (SCREEN_SIZE + 1) / 2 + 7]
        self.snake_body[114] = [(SCREEN_SIZE + 1) / 2 + 4, (SCREEN_SIZE + 1) / 2 + 8]
        self.snake_body[115] = [(SCREEN_SIZE + 1) / 2 + 4, (SCREEN_SIZE + 1) / 2 + 9]
        self.snake_body[116] = [(SCREEN_SIZE + 1) / 2 + 4, (SCREEN_SIZE + 1) / 2 + 10]
        self.snake_body[117] = [(SCREEN_SIZE + 1) / 2 + 4, (SCREEN_SIZE + 1) / 2 + 11]
        self.snake_body[118] = [(SCREEN_SIZE + 1) / 2 + 3, (SCREEN_SIZE + 1) / 2 + 11]
        self.snake_body[119] = [(SCREEN_SIZE + 1) / 2 + 3, (SCREEN_SIZE + 1) / 2 + 10]
        self.snake_body[120] = [(SCREEN_SIZE + 1) / 2 + 3, (SCREEN_SIZE + 1) / 2 + 9]
        self.snake_body[121] = [(SCREEN_SIZE + 1) / 2 + 3, (SCREEN_SIZE + 1) / 2 + 8]
        self.snake_body[122] = [(SCREEN_SIZE + 1) / 2 + 3, (SCREEN_SIZE + 1) / 2 + 7]
        self.snake_body[123] = [(SCREEN_SIZE + 1) / 2 + 3, (SCREEN_SIZE + 1) / 2 + 6]
        self.snake_body[124] = [(SCREEN_SIZE + 1) / 2 + 3, (SCREEN_SIZE + 1) / 2 + 5]
        self.snake_body[125] = [(SCREEN_SIZE + 1) / 2 + 3, (SCREEN_SIZE + 1) / 2 + 4]
        self.snake_body[126] = [(SCREEN_SIZE + 1) / 2 + 3, (SCREEN_SIZE + 1) / 2 + 3]
        self.snake_body[127] = [(SCREEN_SIZE + 1) / 2 + 3, (SCREEN_SIZE + 1) / 2 + 2]
        self.snake_body[128] = [(SCREEN_SIZE + 1) / 2 + 3, (SCREEN_SIZE + 1) / 2 + 1]
        self.snake_body[129] = [(SCREEN_SIZE + 1) / 2 + 3, (SCREEN_SIZE + 1) / 2]
        self.snake_body[130] = [(SCREEN_SIZE + 1) / 2 + 2, (SCREEN_SIZE + 1) / 2]
        self.snake_body[131] = [(SCREEN_SIZE + 1) / 2 + 2, (SCREEN_SIZE + 1) / 2 + 1]
        self.snake_body[132] = [(SCREEN_SIZE + 1) / 2 + 2, (SCREEN_SIZE + 1) / 2 + 2]
        self.snake_body[133] = [(SCREEN_SIZE + 1) / 2 + 2, (SCREEN_SIZE + 1) / 2 + 3]
        self.snake_body[134] = [(SCREEN_SIZE + 1) / 2 + 2, (SCREEN_SIZE + 1) / 2 + 4]
        self.snake_body[135] = [(SCREEN_SIZE + 1) / 2 + 2, (SCREEN_SIZE + 1) / 2 + 5]
        self.snake_body[136] = [(SCREEN_SIZE + 1) / 2 + 2, (SCREEN_SIZE + 1) / 2 + 6]
        self.snake_body[137] = [(SCREEN_SIZE + 1) / 2 + 2, (SCREEN_SIZE + 1) / 2 + 7]
        self.snake_body[138] = [(SCREEN_SIZE + 1) / 2 + 2, (SCREEN_SIZE + 1) / 2 + 8]
        self.snake_body[139] = [(SCREEN_SIZE + 1) / 2 + 2, (SCREEN_SIZE + 1) / 2 + 9]
        self.snake_body[140] = [(SCREEN_SIZE + 1) / 2 + 2, (SCREEN_SIZE + 1) / 2 + 10]
        self.snake_body[141] = [(SCREEN_SIZE + 1) / 2 + 2, (SCREEN_SIZE + 1) / 2 + 11]
        self.snake_body[142] = [(SCREEN_SIZE + 1) / 2 + 1, (SCREEN_SIZE + 1) / 2 + 11]
        self.snake_body[143] = [(SCREEN_SIZE + 1) / 2 + 1, (SCREEN_SIZE + 1) / 2 + 10]
        self.snake_body[144] = [(SCREEN_SIZE + 1) / 2 + 1, (SCREEN_SIZE + 1) / 2 + 9]
        self.snake_body[145] = [(SCREEN_SIZE + 1) / 2 + 1, (SCREEN_SIZE + 1) / 2 + 8]
        self.snake_body[146] = [(SCREEN_SIZE + 1) / 2 + 1, (SCREEN_SIZE + 1) / 2 + 7]
        self.snake_body[147] = [(SCREEN_SIZE + 1) / 2 + 1, (SCREEN_SIZE + 1) / 2 + 6]
        self.snake_body[148] = [(SCREEN_SIZE + 1) / 2 + 1, (SCREEN_SIZE + 1) / 2 + 5]
        self.snake_body[149] = [(SCREEN_SIZE + 1) / 2 + 1, (SCREEN_SIZE + 1) / 2 + 4]
        self.snake_body[150] = [(SCREEN_SIZE + 1) / 2 + 1, (SCREEN_SIZE + 1) / 2 + 3]
        self.snake_body[151] = [(SCREEN_SIZE + 1) / 2 + 1, (SCREEN_SIZE + 1) / 2 + 2]
        self.snake_body[152] = [(SCREEN_SIZE + 1) / 2 + 1, (SCREEN_SIZE + 1) / 2 + 1]
        self.snake_body[153] = [(SCREEN_SIZE + 1) / 2 + 1, (SCREEN_SIZE + 1) / 2]

    # 먹이를 먹은 후 이동함수를 사용할때 lenth를 증가시킨 후 이동함수를 사용해야함.
    def straight(self):
        for i in reversed(range(self.lenth - 1)):
            self.snake_body[i + 1] = self.snake_body[i]

        self.snake_body[0] += self.forward_face()
        self.L[0] = self.L[1]
        self.L[1] = self.snake_body[self.lenth - 1]

        self.distance += 1

    def right(self):
        for i in reversed(range(self.lenth - 1)):
            self.snake_body[i + 1] = self.snake_body[i]

        self.snake_direction -= 90
        self.snake_body[0] += self.forward_face()
        self.L[0] = self.L[1]
        self.L[1] = self.snake_body[self.lenth - 1]

        self.distance += 1

    def left(self):
        for i in reversed(range(self.lenth - 1)):
            self.snake_body[i + 1] = self.snake_body[i]

        self.snake_direction += 90
        self.snake_body[0] += self.forward_face()
        self.L[0] = self.L[1]
        self.L[1] = self.snake_body[self.lenth - 1]

        self.distance += 1

    def prey_set(self):
        doing = True
        while (doing):
            check = True
            self.prey_position = np.zeros(2)
            self.prey_position[0] = rd.randrange(1, 21)
            self.prey_position[1] = rd.randrange(1, 21)
            for i in range(self.lenth):
                if (self.prey_position.tolist() == self.snake_body[i].tolist()):
                    check = False
            if check == True:
                doing = False

    def forward_face(self):
        sx = round(math.cos(math.radians(self.snake_direction)))
        sy = -round(math.sin(math.radians(self.snake_direction)))
        return np.array([sx, sy])

    def specific_face(self, direc):
        sx = round(math.cos(math.radians(self.snake_direction + direc)))
        sy = -round(math.sin(math.radians(self.snake_direction + direc)))
        return np.array([sx, sy])

    def set_value(self):
        for i in range(1, SCREEN_SIZE+1):
            # print(array_compare(self.snake_body[0]+i*self.forward_face(),self.prey_position))
            if array_compare(self.snake_body[0] + i * self.forward_face(), self.prey_position):
                self.check_prey_straight = (SCREEN_SIZE - i) / SCREEN_SIZE
                break
            if array_compare(self.snake_body[0] + i * self.specific_face(-90), self.prey_position):
                self.check_prey_right = (SCREEN_SIZE - i) / SCREEN_SIZE
                break
            if array_compare(self.snake_body[0] + i * self.specific_face(90), self.prey_position):
                self.check_prey_left = (SCREEN_SIZE - i) / SCREEN_SIZE
                break

        for i in range(SCREEN_SIZE):
            check_body_f = self.snake_body[0] + i * self.forward_face()
            check_body_r = self.snake_body[0] + i * self.specific_face(-90)
            check_body_l = self.snake_body[0] + i * self.specific_face(90)
            ss = SCREEN_SIZE

            for j in range(3, self.lenth):
                if (array_compare(check_body_f, self.snake_body[j])) and self.check_body_straight == -1:
                    self.check_body_straight = (SCREEN_SIZE - i) / SCREEN_SIZE
                    self.check_body_straight_number = j/self.lenth
                if (array_compare(check_body_r, self.snake_body[j])) and self.check_body_right == -1:
                    self.check_body_right = (SCREEN_SIZE - i) / SCREEN_SIZE
                    self.check_body_right_number = j/self.lenth
                if (array_compare(check_body_l, self.snake_body[j]) and self.check_prey_left == -1):
                    self.check_body_left = (SCREEN_SIZE - i) / SCREEN_SIZE
                    self.check_body_left_number = j/self.lenth

            if ((check_body_f[0] == -1 or check_body_f[0] == ss or check_body_f[1] == -1 or check_body_f[
                1] == ss)):
                self.check_wall_straight = (SCREEN_SIZE - i) / SCREEN_SIZE
            if ((check_body_r[0] == -1 or check_body_r[0] == ss or check_body_r[1] == -1 or check_body_r[
                1] == ss)):
                self.check_wall_right = (SCREEN_SIZE - i) / SCREEN_SIZE
            if ((check_body_l[0] == -1 or check_body_l[0] == ss or check_body_l[1] == -1 or check_body_l[
                1] == ss)):
                self.check_wall_left = (SCREEN_SIZE - i) / SCREEN_SIZE

        if (self.check_wall_straight == -1):
            self.check_wall_straight = 0
        if (self.check_wall_right == -1):
            self.check_wall_right = 0
        if (self.check_wall_left == -1):
            self.check_wall_left = 0
        if (self.check_body_straight == -1):
            self.check_body_straight = 0
        if (self.check_body_right == -1):
            self.check_body_right = 0
        if (self.check_body_left == -1):
            self.check_body_left = 0
        if (self.check_prey_straight == -1):
            self.check_prey_straight = 0
        if (self.check_prey_right == -1):
            self.check_prey_right = 0
        if (self.check_prey_left == -1):
            self.check_prey_left = 0

        self.prey_relative_position = self.prey_position - self.snake_body[0]
        if (np.sum(self.prey_relative_position * self.forward_face()) <= 0):
            self.check_prey_quadrant[0] = 0
            self.check_prey_quadrant[1] = 0
        if (np.sum(self.prey_relative_position * self.forward_face()) >= 0):
            self.check_prey_quadrant[2] = 0
            self.check_prey_quadrant[3] = 0
        if (np.sum(self.prey_relative_position * self.specific_face(-90)) <= 0):
            self.check_prey_quadrant[0] = 0
            self.check_prey_quadrant[3] = 0
        if (np.sum(self.prey_relative_position * self.specific_face(90)) <= 0):
            self.check_prey_quadrant[1] = 0
            self.check_prey_quadrant[2] = 0

    def reset_value(self):
        self.check_wall_straight = -1
        self.check_wall_right = -1
        self.check_wall_left = -1

        self.check_prey_straight = -1
        self.check_prey_right = -1
        self.check_prey_left = -1

        self.check_body_straight = -1
        self.check_body_right = -1
        self.check_body_left = -1

        self.check_body_straight_number = -1
        self.check_body_right_number = -1
        self.check_body_left_number = -1

        self.prey_relative_position = np.zeros(2)
        self.check_prey_quadrant = np.full(4, 1)

    def check_die(self):
        if self.check_body_straight == 1:
            return True
        if self.check_body_right == 1:
            return True
        if self.check_body_left == 1:
            return True
        if self.check_wall_straight == 1:
            return True
        if self.check_wall_right == 1:
            return True
        if self.check_wall_left == 1:
            return True
        return False
