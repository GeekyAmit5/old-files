import random
import datetime
import os
import fileinput
import sys


# class customer:
#     customers = 0

#     def __init__(self, fname, lname, gender, age, uid, pwd, idtype, idno):
#         self.uid = uid
#         self.pwd = pwd
#         self.idtype = idtype
#         self.idno = idno
#         self.cid = getCustomerID()
#         self.acno = getAcccountNumber()
#         self.fname = fname
#         self.lname = lname
#         self.dob = dob
#         self.idtype = idtype
#         self.idno = idno
#         self.gender = gender
#         self.age = (datetime.datetime.today()-dob).days//365

#     def detail(self):
#         print(f"Name : {self.fname} {self.lname}")
#         print(f"Date of Birth : {self.dob}")
#         print(f"Age : {self.age}")
#         print(f"Gender : {self.gender}")
#         print(f"ID Proof type : {self.idtype}")
#         print(f"ID Proof Number : {self.idno}")

#     # def getAcccountNumber(self):
#     #     while True:
#     #         acno = random.randint(1000,9999)
#     #         if

#     def getCustomerID(self):
#         pass

#     def detail(self):
#         super().detail()
#         print(f"Account Number : {self.acno}")
#         print(f"Customer ID : {self.cid}")


# # dob = datetime.datetime(1997, 12, 5)
# # dob = datetime.datetime(2011, 7, 26)
# # now = datetime.datetime.today()
# # print(dob)
# # print(now)
# # print(now-dob)
# # print((now-dob).days//365)
# # x, y, z = input("x,y : ").split()
# # print(x, y, z)


# if __name__ == "__main__":
#     print("Enter details")
#     fn = input("First Name : ")
#     ln = input("Last Name : ")
#     age = input(" Age : ")
#     gender = input("Gender : ")
#     idtype = input("ID Type : ")
#     idno = input("ID Number : ")
#     uid = input("User ID : ")
#     pwd = input("Password : ")

# c1 = customer(fn, ln, gender, age, uid, pwd, idtype, idno)
# print("Account created Successfuly")
# print("Account details are : ")
# c1.detail()


# def pwdCheck(pwd):
#     i = 0
#     while True:
#         i += 1
#         Pwd = input("Enter the password : ")
#         if pwd != Pwd:
#             if i < 3:
#                 print("Password is Incorrect\n{} attempts left!".format(3 - i))
#                 continue
#             return False
#         return True


# def accOptions(d):
#     a = int(input(
#         "Press 0 to Log Out\nPress 1 to Transfer Amount\nPress 2 to request Amount"))
#     if a == 1:
#         acn = int(input("Enter Benificiary Ac/No. : "))
#         for i in l:
#             if i["accno"] == acn:
#                 print("Name = ", i["name"])
#                 bl = float(input("Enter Amount :"))
#                 if d["bal"] < bl:
#                     print("Insufficient Balance")
#                     accOptions(d)
#                 else:
#                     d["bal"] -= bl
#                     i["bal"] += bl
#                     print("Transaction Successful")
#                     print("Transaction ID =  ", random.randint(100000, 1000000))
#                     print("Balance left = ", d["bal"])
#                 break
#         else:
#             print("Account number does not exist!")
#             accOptions(d)
#     if a == 2:
#         acn = int(input("Enter Ac/No. : "))
#         for i in l:
#             if i["accno"] == acn:
#                 print("Name = ", i["name"])
#                 bl = float(input("Enter Amount :"))
#                 if i["bal"] < bl:
#                     print("Insufficient Balance")
#                     accOptions(d)
#                 else:
#                     if pwdCheck(i["pwd"]):
#                         i["bal"] -= bl
#                         d["bal"] += bl
#                         print("Transaction Successful")
#                         print("Transaction ID =  ",
#                               random.randint(1000000, 10000000))
#                         print("Balance  = ", d["bal"])
#                     break
#         else:
#             print("Account number does not exist!")
#             accOptions(d)
#     print("Successfully Log out")


# def accDetails(i):
#     print("Account Details are : ")
#     for x, y in i.items():
#         if x == "pwd":
#             continue
#         print(x, " = ", y)


# def process():
#     c = int(input("Press 0 to Create Account\nPress 1 to Login\n"))
#     if c:
#         uid = input("Enter User ID : ")
#         for i in l:
#             if i["name"] == uid:
#                 if pwdCheck(i["pwd"]):
#                     print("Login Successful")
#                     accDetails(i)
#                     accOptions(i)
#                     break
#                 print("Login Blocked")
#                 break
#         else:
#             print("User ID does not exist!")
#             process()
#     else:
#         l.append({"accno": random.randint(100, 999), "name": input("Enter Name :"), "password": input("Enter Password :"),
#                   "bal": 0})
#         print("Your Account  Created Successfully")
#         for z in l:
#             print(z)
#         accDetails(l[-1])
#         process()


# fh = open("python/oop/bank/data.txt")
# l = []
# for line in fh:
#     acc = dict()
#     words = line.split()
#     for word in words:
#         val = word.split("=")
#         acc[val[0]] = val[1]
#     l.append(acc)


# process()


# # This is a game called tic tac toe
# # you can play with friend or AI


# import math
# import random
# import pygame
# import time
# import os
# import sys
# import pkg_resources.py2_warn
# import re
# import fileinput


# def drawGrid(color):
#     s = 15
#     e = 380
#     d = 122
#     w = 5
#     for i in range(4):
#         pygame.draw.line(win, color,
#                          (s+d*i, s), (s+d*i, e), w)
#     for i in range(4):
#         pygame.draw.line(win, color,
#                          (s, s+d*i), (e, s+d*i), w)


# def opponent(turn):
#     if turn == X:
#         return O
#     return X


# def winCheck(turn, x, y):
#     for i in range(3):
#         if grid[x][i] != turn:
#             break
#     else:
#         return True
#     for i in range(3):
#         if grid[i][y] != turn:
#             break
#     else:
#         return True
#     if x == y:
#         for i in range(3):
#             if grid[i][i] != turn:
#                 break
#         else:
#             return True
#     if x + y == 2:
#         for i in range(3):
#             if grid[2-i][i] != turn:
#                 break
#         else:
#             return True
#     return False


# def reset():
#     global grid, turn, undoaix, undoaiy, undox, undoy, depth
#     undoaix, undoaiy, undox, undoy = -1, -1, -1, -1
#     depth = 0
#     for i in range(3):
#         for j in range(3):
#             grid[i][j] = " "
#     turn = opponent(last_turn)


# def undo(x, y):
#     global grid, turn, depth
#     grid[x][y] = " "
#     turn = opponent(turn)
#     win.blit(undopic, (18+122*x, 18+122*y))
#     depth -= 1
#     if turn == X:
#         drawGrid(red)
#     else:
#         drawGrid(green)


# def playSound(sound):
#     if sound_on:
#         sound.play()


# def button(rect, buttoncolor, textsize, textcolor, text):
#     pygame.draw.rect(win, buttoncolor, rect)
#     win.blit(pygame.font.SysFont(None, textsize).render(
#         text, True, textcolor), [rect.x+10, rect.y+10])


# def endText(msg):
#     reset()
#     win.blit(pygame.font.SysFont(None, 100).render(
#         msg, True, white), [200 - 20*len(msg), 170])
#     button(rect6, white, 40, black, "Play Again!")
#     button(rect7, white, 40, black, "Main Menu")
#     while True:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 playSound(click)
#                 mx, my = pygame.mouse.get_pos()
#                 if rect6.collidepoint((mx, my)):
#                     game()
#                 elif rect7.collidepoint((mx, my)):
#                     main()
#         pygame.display.update()
#         Clock.tick(fps)


# def minimaxPro(x, y, alpha, beta, isMaximizing):
#     global depth
#     if winCheck(X, x, y):
#         return 1
#     elif winCheck(O, x, y):
#         return - 1
#     elif depth == 9:
#         return 0
#     elif isMaximizing:
#         bestScore = -math.inf
#         for i in range(3):
#             for j in range(3):
#                 if grid[i][j] == " ":
#                     grid[i][j] = X
#                     depth += 1
#                     score = minimaxPro(i, j, alpha, beta, False)
#                     grid[i][j] = " "
#                     depth -= 1
#                     bestScore = max(score, bestScore)
#                     alpha = max(alpha, score)
#                     if beta <= alpha:
#                         break
#         return bestScore
#     else:
#         bestScore = math.inf
#         for i in range(3):
#             for j in range(3):
#                 if grid[i][j] == " ":
#                     grid[i][j] = O
#                     depth += 1
#                     score = minimaxPro(i, j, alpha, beta, True)
#                     grid[i][j] = " "
#                     depth -= 1
#                     bestScore = min(score, bestScore)
#                     beta = min(beta, score)
#                     if beta <= alpha:
#                         break
#         return bestScore


# def AI():
#     global turn, undoaix, undoaiy, winx, tie, depth
#     if depth == 9 and level > 0:
#         x = random.randint(0, 2)
#         if x == 1:
#             y = 1
#         else:
#             y = random.choice([0, 2])
#     elif random.choice([1, 1, level, level >= 2, level == 3]):
#         bestScore = -math.inf
#         for i in range(3):
#             for j in range(3):
#                 if grid[i][j] == " ":
#                     grid[i][j] = X
#                     depth += 1
#                     score = minimaxPro(i, j, -math.inf, math.inf, False)
#                     grid[i][j] = " "
#                     depth -= 1
#                     if score > bestScore:
#                         bestScore = score
#                         x, y = i, j
#     else:
#         while True:
#             x, y = random.randint(0, 2), random.randint(0, 2)
#             if grid[x][y] == " ":
#                 break
#     grid[x][y] = X
#     undoaix, undoaiy = x, y
#     win.blit(cross, (27+122*x, 27+122*y))
#     pygame.time.delay(200)
#     pygame.display.update()
#     playSound(gameplay)
#     depth += 1
#     if winCheck(X, x, y):
#         winx += 1
#         endText("AI WIN!")
#     elif depth == 9:
#         tie += 1
#         endText("TIE!")
#     else:
#         turn = O
#         drawGrid(green)


# def game():
#     global grid, turn, undox, undoy, winx, wino, tie, undoaix, undoaiy, last_turn, depth
#     t0 = time.time()
#     win.blit(background, (0, 0))
#     if turn == X:
#         last_turn = X
#         drawGrid(red)
#         if level != -1:
#             AI()
#     else:
#         last_turn = O
#         drawGrid(green)
#     win.blit(pygame.font.SysFont(
#         None, 50).render("SCORE", True, white), [30, 385])
#     win.blit(pygame.font.SysFont(
#         None, 40).render("YOU:", True, green), [80, 416])
#     win.blit(pygame.font.SysFont(
#         None, 40).render("TIE:", True, white), [91, 470])
#     if level != -1:
#         win.blit(pygame.font.SysFont(
#             None, 40).render("AI:", True, red), [109, 441])
#     else:
#         win.blit(pygame.font.SysFont(
#             None, 40).render("FRIEND:", True, red), [34, 441])
#     win.blit(pygame.font.SysFont(
#         None, 45).render(str(wino), True, green), [150, 416])
#     win.blit(pygame.font.SysFont(
#         None, 45).render(str(winx), True, red), [150, 441])
#     win.blit(pygame.font.SysFont(
#         None, 45).render(str(tie), True, white), [150, 470])
#     while True:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 mx, my = pygame.mouse.get_pos()
#                 x, y = (mx-15)//122, (my-15)//122
#                 if 0 <= x <= 2 and 0 <= y <= 2 and grid[x][y] == " ":
#                     playSound(gameplay)
#                     t0 = time.time()
#                     grid[x][y] = turn
#                     undox, undoy = x, y
#                     if turn == X:
#                         win.blit(cross, (27+122*x, 27+122*y))
#                     else:
#                         win.blit(nought, (25+122*x, 25+122*y))
#                     pygame.display.update()
#                     depth += 1
#                     if winCheck(turn, x, y):
#                         if turn == X:
#                             winx += 1
#                         else:
#                             wino += 1
#                         if level != -1:
#                             endText("YOU WIN!")
#                         else:
#                             endText(turn+" WIN!")
#                     elif depth == 9:
#                         tie += 1
#                         endText("TIE!")
#                     else:
#                         turn = opponent(turn)
#                         if turn == X:
#                             drawGrid(red)
#                         else:
#                             drawGrid(green)
#                         pygame.display.update()
#                         if level != -1:
#                             AI()
#                 elif rect6.collidepoint((mx, my)):
#                     reset()
#                     game()
#                 elif rect7.collidepoint((mx, my)):
#                     if not depth:
#                         main()
#                     else:
#                         if undox != -1:
#                             undo(undox, undoy)
#                             undox = -1
#                             if undoaix != -1:
#                                 undo(undoaix, undoaiy)
#                                 undoaix = -1
#         if not depth:
#             button(rect6, white, 40, black, "Swap turn")
#             button(rect7, white, 40, black, "Main Menu")
#         else:
#             button(rect6, white, 40, black, "Clear")
#             if undox != -1:
#                 button(rect7, white, 40, black, "Undo")
#             else:
#                 button(rect7, white, 40, (128, 128, 128), "Undo")
#         if depth and time_on and time.time() - t0 > time_limit:
#             if level != -1:
#                 winx += 1
#                 endText("AI WIN!")
#             else:
#                 if turn == X:
#                     winx += 1
#                 else:
#                     wino += 1
#                 endText(opponent(turn)+" WIN!")
#         pygame.display.update()
#         Clock.tick(fps)


# def difficulty():
#     global level
#     win.blit(background, (0, 0))
#     win.blit(pygame.font.SysFont(
#         None, 60).render("Select Difficulty!", True, white), [40, 60])
#     button(rect1, white, 50, black, "Easy")
#     button(rect2, white, 50, black, "Medium")
#     button(rect3, white, 50, black, "Hard")
#     button(rect4, white, 50, black, "Impossible")
#     button(rect5, white, 50, black, "Main Menu")
#     while True:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 playSound(click)
#                 mx, my = pygame.mouse.get_pos()
#                 if rect1.collidepoint((mx, my)):
#                     level = 0
#                     game()
#                 elif rect2.collidepoint((mx, my)):
#                     level = 1
#                     game()
#                 elif rect3.collidepoint((mx, my)):
#                     level = 2
#                     game()
#                 elif rect4.collidepoint((mx, my)):
#                     level = 3
#                     game()
#                 elif rect5.collidepoint((mx, my)):
#                     main()
#         pygame.display.update()
#         Clock.tick(fps)


# def about():
#     win.blit(background, (0, 0))
#     win.blit(pygame.font.SysFont(
#         None, 80).render("Developer", True, white), [70, 30])
#     win.blit(pygame.font.SysFont(
#         None, 80).render("AMIT MISHRA", True, green), [20, 100])
#     win.blit(pygame.font.SysFont(
#         None, 80).render("IIT DELHI", True, white), [70, 170])
#     win.blit(pygame.font.SysFont(
#         None, 65).render("MSc Mathematics", True, white), [20, 240])
#     button(rect5, white, 50, black, "MAIN MENU")
#     while True:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 playSound(click)
#                 mx, my = pygame.mouse.get_pos()
#                 if rect5.collidepoint((mx, my)):
#                     main()
#         pygame.display.update()
#         Clock.tick(fps)


# def options():
#     global sound_on, time_on
#     win.blit(background, (0, 0))
#     win.blit(pygame.font.SysFont(
#         None, 100).render("OPTIONS", True, white), [30, 80])
#     button(rect2, white, 50, black, "ABOUT")
#     button(rect5, white, 50, black, "MAIN MENU")
#     while True:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 playSound(click)
#                 mx, my = pygame.mouse.get_pos()
#                 if rect2.collidepoint((mx, my)):
#                     about()
#                 elif rect3.collidepoint((mx, my)):
#                     if time_on:
#                         time_on = False
#                     else:
#                         time_on = True
#                     fh = fileinput.input("data/settings.txt", inplace=True)
#                     for line in fh:
#                         if line.startswith("time"):
#                             words = line.split()
#                             line = line.replace(
#                                 str(int(words[-1])), str(1-int(words[-1])))
#                         sys.stdout.write(line)
#                 elif rect4.collidepoint((mx, my)):
#                     if sound_on:
#                         sound_on = False
#                         pygame.mixer.music.pause()
#                     else:
#                         sound_on = True
#                         pygame.mixer.music.play(-1)
#                     fh = fileinput.input("data/settings.txt", inplace=True)
#                     for line in fh:
#                         if line.startswith("sound"):
#                             words = line.split()
#                             line = line.replace(
#                                 str(int(words[-1])), str(1-int(words[-1])))
#                         sys.stdout.write(line)
#                 elif rect5.collidepoint((mx, my)):
#                     main()
#         if time_on:
#             button(rect3, green, 50, black, "TIME LIMIT 3 sec")
#         else:
#             button(rect3, red, 50, black, "TIME LIMIT OFF")
#         if sound_on:
#             button(rect4, green, 50, black, "SOUNDS ON")
#         else:
#             button(rect4, red, 50, black, "SOUNDS OFF")
#         pygame.display.update()
#         Clock.tick(fps)


class button:
    def __init__(self, rect, color, textsize, text, textcolor):
        self.rect = rect
        self.color = color

    def show(self):
        pygame.draw.rect(win, buttoncolor, rect)
        win.blit(pygame.font.SysFont(None, textsize).render(
            text, True, textcolor), [rect.x+10, rect.y+10])


def main():
    win.blit(bg, (0, 0))
    win.blit(pygame.font.SysFont(
        None, 80).render("Welcome to SBI", True, green), [100, 100])
    # button(rect2, white, 50, black, "TWO PLAYER")
    # button(rect3, white, 50, black, "YOU VS AI")
    # button(rect4, white, 50, black, "OPTIONS")
    # button(rect5, white, 50, black, "EXIT!")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # if event.type == pygame.MOUSEBUTTONDOWN:
            #     # playSound(click)
            #     mx, my = pygame.mouse.get_pos()
            #     if rect2.collidepoint((mx, my)):
            #         level = -1
            #         game()
            #     elif rect3.collidepoint((mx, my)):
            #         difficulty()
            #     elif rect4.collidepoint((mx, my)):
            #         options()
            #     elif rect5.collidepoint((mx, my)):
            #         pygame.quit()
            #         sys.exit()
        pygame.display.update()
        Clock.tick(fps)


main()
