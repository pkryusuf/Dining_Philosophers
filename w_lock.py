from threading import Thread, Lock
import random
import time
import os


class DiningPhilosophers:
    def __init__(self, number_of_philosophers, meal_size=9):
        self.meals = [meal_size for _ in range(number_of_philosophers)]
        self.chopsticks = [Lock() for _ in range(number_of_philosophers)]
        self.status = ['T' for _ in range(number_of_philosophers)]
        self.chopstick_holders = [' ' for _ in range(number_of_philosophers)]

    def philosopher(self, i):
        j = (i + 1) % 5
        while self.meals[i] > 0:
            self.status[i] = 'T'
            time.sleep(random.random())
            if not self.chopsticks[i].locked():
                self.chopsticks[i].acquire()
                self.chopstick_holders[i] = '/'
                time.sleep(random.random())
                if not self.chopsticks[j].locked():
                    self.chopsticks[j].acquire()
                    self.chopstick_holders[i] = '/     \\'
                    self.status[i] = 'E'
                    time.sleep(random.random())
                    self.meals[i] -= 1
                    self.chopsticks[j].release()
                    self.chopstick_holders[i] = ' '
                    self.chopsticks[i].release()
                    self.chopstick_holders[i] = ' '
                    self.status[i] = 'T'
                else:
                    self.chopsticks[i].release()
                    self.chopstick_holders[i] = ' '


def main():
    n = 5
    m = 7
    dining_philosophers = DiningPhilosophers(n, m)
    philosophers = [Thread(target=dining_philosophers.philosopher, args=(i,)) for i in range(n)]
    for philosopher in philosophers:
        philosopher.start()

    w, h = 11, 11;
    Matrix = [[0 for x in range(w)] for y in range(h)]

    while sum(dining_philosophers.meals) > 0:
        for a in range(11):
            for b in range(11):
                Matrix[a][b] = "  "

        print("=" * (30))
        Matrix[0][5] = dining_philosophers.status[0]
        Matrix[4][1] = dining_philosophers.status[1]
        Matrix[4][9] = dining_philosophers.status[2]
        Matrix[8][3] = dining_philosophers.status[3]
        Matrix[8][7] = dining_philosophers.status[4]

        Matrix[1][4] = dining_philosophers.chopstick_holders[0]
        Matrix[5][0] = dining_philosophers.chopstick_holders[1]
        Matrix[5][8] = dining_philosophers.chopstick_holders[2]
        Matrix[9][2] = dining_philosophers.chopstick_holders[3]
        Matrix[9][6] = dining_philosophers.chopstick_holders[4]

        Matrix[2][5] = dining_philosophers.meals[0]
        Matrix[6][1] = dining_philosophers.meals[1]
        Matrix[6][9] = dining_philosophers.meals[2]
        Matrix[10][3] = dining_philosophers.meals[3]
        Matrix[10][7] = dining_philosophers.meals[4]

        for i in range(11):
            for k in range(1):
                print(Matrix[i][k], Matrix[i][k + 1], Matrix[i][k + 2], Matrix[i][k + 3], Matrix[i][k + 4],
                      Matrix[i][k + 5], Matrix[i][k + 6], Matrix[i][k + 7], Matrix[i][k + 8], Matrix[i][k + 9],
                      Matrix[i][k + 10])
        for _ in range(5):
            locked_chopsticks = 0
            for i in range(n):
                if dining_philosophers.chopsticks[i].locked():
                    locked_chopsticks += 1
        print("Number of eating philosophers: ", str(dining_philosophers.status.count('E')), " / 5")
        print("Number of locked chopsticks: ", locked_chopsticks, " / 5")
        print("Meals left: ", str(sum(dining_philosophers.meals)), " / ", n*m)


        time.sleep(0.5)
        os.system('cls')
    for philosopher in philosophers:
        philosopher.join()


if __name__ == "__main__":
    main()
