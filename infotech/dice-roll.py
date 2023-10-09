import random
import tkinter as tk
from tkinter import ttk

class DiceRoller:
    def __init__(self, master):
        self.master = master
        self.master.title("Dice Rolling App")

        self.num_dice_label = ttk.Label(self.master, text="Number of Dice:")
        self.num_dice_spinbox = ttk.Spinbox(self.master, from_=1, to=10, width=5)
        self.roll_button = ttk.Button(self.master, text="Roll Dice", command=self.roll_dice)
        self.result_label = ttk.Label(self.master, text="")
        self.stats_button = ttk.Button(self.master, text="Show Statistics", command=self.display_statistics)

        self.num_dice_label.grid(row=0, column=0, padx=10, pady=10, sticky="E")
        self.num_dice_spinbox.grid(row=0, column=1, padx=10, pady=10)
        self.roll_button.grid(row=1, column=0, columnspan=2, pady=10)
        self.result_label.grid(row=2, column=0, columnspan=2, pady=10)
        self.stats_button.grid(row=3, column=0, columnspan=2, pady=10)

        self.rolls_history = []
        self.distribution = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

    def roll_dice(self):
        try:
            num_dice = int(self.num_dice_spinbox.get())
        except ValueError:
            self.result_label["text"] = "Please enter a valid number."
            return

        if num_dice <= 0:
            self.result_label["text"] = "Please enter a positive number."
            return

        dice_results = [random.randint(1, 6) for _ in range(num_dice)]
        self.rolls_history.extend(dice_results)
        self.update_distribution(dice_results)

        result_text = f"Result of rolling {num_dice} dice: {dice_results}"
        self.result_label["text"] = result_text

    def display_statistics(self):
        total_rolls = len(self.rolls_history)
        total_sum = sum(self.rolls_history)
        average = total_sum / total_rolls if total_rolls > 0 else 0

        stats_text = f"\n--- Statistics ---\nTotal Rolls: {total_rolls}\nTotal Sum: {total_sum}\nAverage: {average:.2f}\n"
        self.result_label["text"] = stats_text

        distribution_text = "\n--- Distribution ---\n"
        for value, count in self.distribution.items():
            distribution_text += f"{value}: {count} times\n"
        self.result_label["text"] += distribution_text

    def update_distribution(self, dice_results):
        for value in dice_results:
            self.distribution[value] += 1

def main():
    root = tk.Tk()
    app = DiceRoller(root)
    root.mainloop()

if __name__ == "__main__":
    main()
