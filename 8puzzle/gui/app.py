import sys
import os
import time
import random
import threading
import tkinter as tk
from tkinter import ttk, filedialog, messagebox

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from puzzle.state import State
from puzzle.solver import Puzzle
from puzzle.algorithms import Algorithms, Heuristics

class PuzzleApp:
    def __init__(self, root):
        self.root = root
        self.root.title("8-Puzzle Solver")
        self.root.configure(bg="#f0f0f0")

        self.selected_algorithm = tk.StringVar(value=Algorithms.BFS.name)
        self.selected_heuristic = tk.StringVar(value=Heuristics.NONE.name)
        self.initial_state = None
        self.goal_state = State([[1,2,3],[4,5,6],[7,8,0]])
        self.solution_path = []
        self.current_step = 0
        self.puzzle = None
        self.start_time = None
        self.timer_running = False

        self.build_main_area()
        self.build_controls()

    def build_main_area(self):
        self.title_label = tk.Label(
            self.root, text="8-Puzzle Solver", font=("Segoe UI", 20, "bold"), bg="#f0f0f0", fg="#333")
        self.title_label.pack(pady=10)

        self.info_label = tk.Label(
            self.root, text="Escolha o algoritmo e heurística para começar", font=("Segoe UI", 11), bg="#f0f0f0")
        self.info_label.pack(pady=5)

        self.board_frame = tk.Frame(self.root, bg="#f0f0f0")
        self.board_frame.pack(pady=20)

        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                btn = tk.Button(
                    self.board_frame, text="", width=4, height=2,
                    font=("Segoe UI", 26, "bold"), bg="#ffffff", fg="#333",
                    relief="raised", borderwidth=3
                )
                btn.grid(row=i, column=j, padx=5, pady=5, ipadx=10, ipady=10)
                self.buttons[i][j] = btn

        self.status_label = tk.Label(
            self.root, text="Passos: 0 | Tempo: 0.00s", font=("Segoe UI", 10), bg="#f0f0f0", fg="#555")
        self.status_label.pack(pady=5)

    def build_controls(self):
        self.navbar = tk.Frame(self.root, bg="#f0f0f0")
        self.navbar.pack(pady=10)

        tk.Label(self.navbar, text="Algoritmo:", font=("Segoe UI", 10), bg="#f0f0f0").grid(row=0, column=0, padx=5)
        tk.OptionMenu(self.navbar, self.selected_algorithm, "A_STAR", "BFS", "DFS").grid(row=0, column=1, padx=5)

        tk.Label(self.navbar, text="Heurística:", font=("Segoe UI", 10), bg="#f0f0f0").grid(row=0, column=2, padx=5)
        tk.OptionMenu(self.navbar, self.selected_heuristic, self.selected_heuristic.get(), *[h.name for h in Heuristics]).grid(row=0, column=3, padx=5)

        tk.Button(self.navbar, text="Gerar Tabuleiro", command=self.generate_random, bg="#2196f3", fg="white", font=("Segoe UI", 10, "bold")).grid(row=0, column=4, padx=10)
        tk.Button(self.navbar, text="Resolver", command=self.solve, bg="#4caf50", fg="white", font=("Segoe UI", 10, "bold")).grid(row=0, column=5, padx=10)

    def update_board(self, state: State):
        for i in range(3):
            for j in range(3):
                val = state.board[i][j]
                btn = self.buttons[i][j]
                if val == 0:
                    btn.config(text="", bg="#d3d3d3", relief="sunken")
                else:
                    btn.config(text=str(val), bg="#ffffff", relief="raised")

    def generate_random(self):
        try:
            nums = list(range(9))
            random.shuffle(nums)
            self.initial_state = State([nums[i:i+3] for i in range(0, 9, 3)])
            self.update_board(self.initial_state)
            self.status_label.config(text="Tabuleiro gerado. Pronto para resolver!")
        except Exception as e:
            messagebox.showerror("Erro ao gerar aleatoriamente", str(e))

    def solve(self):
        try:
            if not self.initial_state:
                messagebox.showerror("Erro", "Escolha um estado inicial primeiro.")
                return

            algorithm = Algorithms[self.selected_algorithm.get()]
            heuristic = Heuristics[self.selected_heuristic.get()]

            if algorithm in {Algorithms.A_STAR} and heuristic == Heuristics.NONE:
                messagebox.showerror("Erro", "Selecione uma heurística para o algoritmo escolhido.")
                return

            self.puzzle = Puzzle(self.initial_state, self.goal_state, algorithm=algorithm, heuristic=heuristic)

            def run_solver():
                """
                Executa a resolução do puzzle em uma thread separada para evitar travamento da interface.
                """
                try:
                    self.start_time = time.time()
                    self.timer_running = True
                    self.update_timer()
                    path = self.puzzle.solve()
                    self.timer_running = False

                    if path is None:
                        messagebox.showerror("Erro", "Não foi possível encontrar uma solução.")
                        return

                    self.solution_path = path
                    self.current_step = 0
                    self.animate_solution()
                except Exception as e:
                    self.timer_running = False
                    messagebox.showerror("Erro durante a resolução", str(e))

            threading.Thread(target=run_solver).start()
        except Exception as e:
            messagebox.showerror("Erro ao iniciar a resolução", str(e))


    def animate_solution(self):
        try:
            if not self.solution_path or self.current_step >= len(self.solution_path):
                return
            state = self.solution_path[self.current_step]
            self.update_board(state)
            self.current_step += 1
            self.status_label["text"] = f"Passos: {self.current_step} | Tempo: {time.time() - self.start_time:.2f}s"
            self.root.after(500, self.animate_solution)
        except Exception as e:
            messagebox.showerror("Erro durante a animação", str(e))


    def update_timer(self):
        if self.timer_running:
            elapsed = time.time() - self.start_time
            self.status_label["text"] = f"Passos: {self.current_step} | Tempo: {elapsed:.2f}s"
            self.root.after(100, self.update_timer)


def main():
    root = tk.Tk()
    app = PuzzleApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
