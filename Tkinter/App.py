import tkinter as tk
import random

# Constants
WIDTH, HEIGHT = 400, 500
CAR_SPEED = 10
OBSTACLE_SPEED = 5

class Game(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Car Race Game")
        self.geometry(f"{WIDTH}x{HEIGHT}")

        # Create a canvas for the game
        self.canvas = tk.Canvas(self, bg="gray", width=WIDTH, height=HEIGHT)
        self.canvas.pack()
        
        self.canvas.focus_set()

        self.car = self.canvas.create_rectangle(WIDTH // 2 - 25, HEIGHT - 60, WIDTH // 2 + 25, HEIGHT - 40, fill="blue")
        self.obstacle = self.canvas.create_rectangle(random.randint(50, WIDTH - 50), 0, random.randint(50, WIDTH - 50) + 50, 30, fill="red")

        self.bind("<Left>", self.move_left)
        self.bind("<Right>", self.move_right)

        self.update_game()

    def move_left(self, event):
        if self.canvas.coords(self.car)[0] > 10:
            self.canvas.move(self.car, -CAR_SPEED, 0)

    def move_right(self, event):
        if self.canvas.coords(self.car)[2] < WIDTH - 10:
            self.canvas.move(self.car, CAR_SPEED, 0)

    def update_game(self):
        self.canvas.move(self.obstacle, 0, OBSTACLE_SPEED)

        if self.canvas.coords(self.obstacle)[3] > HEIGHT:
            self.canvas.delete(self.obstacle)
            self.obstacle = self.canvas.create_rectangle(random.randint(50, WIDTH - 50), 0, random.randint(50, WIDTH - 50) + 50, 30, fill="red")

        # Check collision
        if self.canvas.coords(self.car)[2] > self.canvas.coords(self.obstacle)[0] and self.canvas.coords(self.car)[0] < self.canvas.coords(self.obstacle)[2] and self.canvas.coords(self.car)[3] > self.canvas.coords(self.obstacle)[1]:
            print("Game Over!")
            self.destroy()

        self.after(100, self.update_game)

if __name__ == "__main__":
    game = Game()
    game.mainloop()
