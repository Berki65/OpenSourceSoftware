"""
Assignment from Berkay Bentetik - 24170078
Python Lab 03 - Turtle Runaway
"""

import tkinter as tk
import turtle
import time
import math
import random

class RunawayGame:
    def __init__(self, screen, runner, chaser, catch_radius=30):
        self.screen = screen
        self.canvas = screen.getcanvas()
        self.runner = runner
        self.chaser = chaser
        self.catch_radius2 = catch_radius**2
        self.game_over = False
        self.level = 1
        self.score = 0

        # Color for computer
        self.runner_colors = ['green', 'blue', 'yellow', 'purple', 'orange', 'red']
        self.current_color_index = 0
        self.total_rounds = len(self.runner_colors)

        # Initialize player and computer
        self.runner.shape('turtle')
        self.runner.color(self.runner_colors[self.current_color_index])
        self.runner.penup()

        self.chaser.shape('turtle')
        self.chaser.color('red')
        self.chaser.penup()

        # Instantiate turtles for drawing UI elements
        self.level_drawer = turtle.RawTurtle(screen)
        self.level_drawer.hideturtle()
        self.level_drawer.penup()

        self.time_drawer = turtle.RawTurtle(screen)
        self.time_drawer.hideturtle()
        self.time_drawer.penup()

        self.round_drawer = turtle.RawTurtle(screen)
        self.round_drawer.hideturtle()
        self.round_drawer.penup()

        # Define border for 700x700px
        self.min_x = -350
        self.max_x = 350
        self.min_y = -350
        self.max_y = 350

        # Update the level display
        self.level_drawer.clear()
        self.level_drawer.penup()
        self.level_drawer.setpos(-330, 310)
        self.level_drawer.write(f'Level: {self.level}', font=('Arial', 15, 'bold'))

    def is_catched(self):
        p = self.runner.pos()
        q = self.chaser.pos()
        dx, dy = p[0] - q[0], p[1] - q[1]
        return dx**2 + dy**2 < self.catch_radius2

    def start(self, init_dist=400, ai_timer_msec=100):
        self.ai_timer_msec = ai_timer_msec
        self.reset_game()

    def reset_game(self):
        # Deactivate key input during reset
        self.chaser.deactivate_keys()

        # Reset positions and headings
        self.runner.setpos((-200, 0))
        self.runner.setheading(0)
        self.chaser.setpos((+200, 0))
        self.chaser.setheading(180)

        # Reset timer
        self.start_time = time.time()
        self.game_over = False

        # Update runner speed based on level
        self.runner.increase_speed(self.level * 5)

        # Update color computer round based
        if self.current_color_index < len(self.runner_colors):
            color = self.runner_colors[self.current_color_index]
            self.runner.color(color)
            self.current_color_index += 1
        else:
            color = self.runner_colors[-1]
            self.runner.color(color)

        # Update level display
        self.level_drawer.clear()
        self.level_drawer.penup()
        self.level_drawer.setpos(-330, 310)
        self.level_drawer.write(f'Level: {self.level}', font=('Arial', 14, 'bold'))

        # Activate key input after reset is complete
        self.chaser.activate_keys()

        # Start the game loop
        self.screen.ontimer(self.step, self.ai_timer_msec)

    def step(self):
        if self.game_over:
            return

        self.runner.run_ai(self.chaser.pos(), self.chaser.heading())
        self.chaser.run_ai(self.runner.pos(), self.runner.heading())

        # Ensure turtles stay within boundaries
        self.check_boundary(self.runner)
        self.check_boundary(self.chaser)

        is_catched = self.is_catched()
        elapsed_time = time.time() - self.start_time

        # Update elapsed time display
        self.time_drawer.clear()
        self.time_drawer.penup()
        self.time_drawer.setpos(150, 310)
        self.time_drawer.write(f'Elapsed time: {elapsed_time:.2f} sec',
                               font=('Arial', 14, 'bold'))

        if is_catched:
            self.game_over = True
            self.score += elapsed_time  # Add elapsed time to total score
            self.level += 1  # Increase level

            # Current Level top left
            self.level_drawer.clear()
            self.level_drawer.penup()
            self.level_drawer.setpos(-330, 310)
            self.level_drawer.write(f'Level: {self.level}', font=('Arial', 14, 'bold'))

            self.time_drawer.clear()
            self.time_drawer.penup()
            self.time_drawer.setpos(0, 0)
            self.time_drawer.write(f' CAUGHT!!!! \n Next Level: {self.level}',
                                   align='center', font=('Arial', 20, 'bold'))

            # Deactivate key input when the round ends
            self.chaser.deactivate_keys()

            # Delay before starting the next round
            self.screen.ontimer(self.reset_game, 1000)
        else:
            self.screen.ontimer(self.step, self.ai_timer_msec)

    def check_boundary(self, turtle_obj):
        x, y = turtle_obj.pos()
        x = max(self.min_x, min(self.max_x, x))
        y = max(self.min_y, min(self.max_y, y))
        turtle_obj.setpos(x, y)

class SmartMover(turtle.RawTurtle):
    def __init__(self, screen, min_x, max_x, min_y, max_y, step_move=10, step_turn=10):
        super().__init__(screen)
        self.screen = screen
        self.min_x = min_x
        self.max_x = max_x
        self.min_y = min_y
        self.max_y = max_y
        self.step_move = step_move
        self.initial_step_move = step_move
        self.step_turn = step_turn

    def increase_speed(self, level):
        # Increase speed based on level
        self.step_move = self.initial_step_move + (level - 1) * 3

    # Updated AI to allow moving backward
    def run_ai(self, opp_pos, opp_heading):

        # Get current position
        x, y = self.pos()

        # Calculate distances to walls
        distance_left = x - self.min_x
        distance_right = self.max_x - x
        distance_bottom = y - self.min_y
        distance_top = self.max_y - y

        # Wall avoidance threshold
        threshold = 100  # Increased threshold for earlier avoidance

        # Initialize wall avoidance vector
        wall_avoidance_vector = [0, 0]

        # Calculate wall repulsion vectors
        if distance_left < threshold:
            wall_avoidance_vector[0] += (threshold - distance_left)
        if distance_right < threshold:
            wall_avoidance_vector[0] -= (threshold - distance_right)
        if distance_bottom < threshold:
            wall_avoidance_vector[1] += (threshold - distance_bottom)
        if distance_top < threshold:
            wall_avoidance_vector[1] -= (threshold - distance_top)

        # Normalize wall avoidance vector
        wall_avoidance_magnitude = math.hypot(wall_avoidance_vector[0], wall_avoidance_vector[1])
        if wall_avoidance_magnitude > 0:
            wall_avoidance_vector[0] /= wall_avoidance_magnitude
            wall_avoidance_vector[1] /= wall_avoidance_magnitude

        # Calculate escape vector from chaser
        dx = self.xcor() - opp_pos[0]
        dy = self.ycor() - opp_pos[1]
        escape_vector = [dx, dy]
        escape_magnitude = math.hypot(dx, dy)
        if escape_magnitude > 0:
            escape_vector[0] /= escape_magnitude
            escape_vector[1] /= escape_magnitude

        # Combine wall avoidance and escape vectors
        combined_vector = [
            wall_avoidance_vector[0] * 2 + escape_vector[0],
            wall_avoidance_vector[1] * 2 + escape_vector[1]
        ]

        # Add randomness to avoid predictability
        random_angle = random.uniform(-30, 30)
        cos_angle = math.cos(math.radians(random_angle))
        sin_angle = math.sin(math.radians(random_angle))
        rotated_vector = [
            combined_vector[0] * cos_angle - combined_vector[1] * sin_angle,
            combined_vector[0] * sin_angle + combined_vector[1] * cos_angle
        ]

        # Calculate desired heading
        desired_heading = math.degrees(math.atan2(rotated_vector[1], rotated_vector[0]))

        # Normalize desired_heading to [0, 360)
        desired_heading %= 360

        # Calculate the smallest angle difference
        angle_diff = (desired_heading - self.heading() + 360) % 360
        if angle_diff > 180:
            angle_diff -= 360

        # Determine whether to move forward or backward
        # Calculate the angle between runner's heading and vector to chaser
        angle_to_chaser = math.degrees(math.atan2(opp_pos[1] - y, opp_pos[0] - x))
        relative_angle = (angle_to_chaser - self.heading() + 360) % 360
        if relative_angle > 180:
            relative_angle -= 360

        # If the chaser is in front and close, move backward
        distance_to_chaser = math.hypot(opp_pos[0] - x, opp_pos[1] - y)
        if abs(relative_angle) < 60 and distance_to_chaser < 150:
            # Move backward
            move_distance = -self.step_move
        else:
            # Move forward
            move_distance = self.step_move

        # Turn towards desired heading
        if angle_diff > 0:
            self.left(min(angle_diff, self.step_turn))
        else:
            self.right(min(-angle_diff, self.step_turn))

        # Move forward or backward
        self.forward(move_distance)

class ManualMover(turtle.RawTurtle):
    def __init__(self, screen, step_move=10, step_turn=10):
        super().__init__(screen)
        self.screen = screen
        self.canvas = screen.getcanvas()
        self.step_move = step_move
        self.step_turn = step_turn
        self.keys_pressed = set()
        self.keys_enabled = True

        # Register event handlers for key press and release
        self.canvas.bind('<KeyPress>', self.key_press)
        self.canvas.bind('<KeyRelease>', self.key_release)
        self.canvas.focus_set()

        # Start the movement update loop
        self.update_movement()

    def key_press(self, event):
        if self.keys_enabled:
            self.keys_pressed.add(event.keysym)

    def key_release(self, event):
        if self.keys_enabled and event.keysym in self.keys_pressed:
            self.keys_pressed.remove(event.keysym)

    def update_movement(self):
        # Movement
        if self.keys_enabled:
            if 'Up' in self.keys_pressed:
                self.forward(self.step_move)
            if 'Down' in self.keys_pressed:
                self.backward(self.step_move)
            if 'Left' in self.keys_pressed:
                self.left(self.step_turn)
            if 'Right' in self.keys_pressed:
                self.right(self.step_turn)

        self.screen.ontimer(self.update_movement, 50)

    def deactivate_keys(self):
        self.keys_enabled = False
        self.keys_pressed.clear()

    def activate_keys(self):
        self.keys_enabled = True

    def run_ai(self, opp_pos, opp_heading):
        pass

if __name__ == '__main__':
    # Use 'TurtleScreen' instead of 'Screen' to prevent an exception from the singleton 'Screen'
    root = tk.Tk()
    canvas = tk.Canvas(root, width=700, height=700)
    canvas.pack()
    root.title("Berkis Turtle Catcher")
    screen = turtle.TurtleScreen(canvas)

    # Set background image
    screen.bgpic('ocean.gif')

    # Define boundaries (assuming canvas is 700x700)
    min_x = -350
    max_x = 350
    min_y = -350
    max_y = 350

    # Create the runner and chaser
    runner = SmartMover(screen, min_x, max_x, min_y, max_y)
    runner.color('green')

    chaser = ManualMover(screen)

    game = RunawayGame(screen, runner, chaser)
    game.start()
    screen.mainloop()