import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class GameOfLife:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = np.random.choice([0, 1], size=(height, width), p=[0.85, 0.15])

    def update(self):
        """应用生命游戏规则更新网格"""
        # 计算每个细胞周围的邻居数量
        new_grid = self.grid.copy()
        for i in range(self.height):
            for j in range(self.width):
                # 计算周围8个位置的活细胞数量
                total = 0
                for di in [-1, 0, 1]:
                    for dj in [-1, 0, 1]:
                        if di == 0 and dj == 0:
                            continue
                        ni = (i + di) % self.height
                        nj = (j + dj) % self.width
                        total += self.grid[ni, nj]
                
                # 应用生命游戏规则
                if self.grid[i, j] == 1:
                    if total < 2 or total > 3:
                        new_grid[i, j] = 0  # 死亡：孤独或过度拥挤
                else:
                    if total == 3:
                        new_grid[i, j] = 1  # 繁殖：正好三个邻居
        
        self.grid = new_grid
        return self.grid

    def animate(self, num_frames=200):
        """创建动画"""
        fig, ax = plt.subplots(figsize=(10, 10))
        ax.set_xticks([])
        ax.set_yticks([])
        img = ax.imshow(self.grid, interpolation='nearest')
        
        def update_frame(frame):
            self.update()
            img.set_array(self.grid)
            return [img]
        
        anim = FuncAnimation(fig, update_frame, frames=num_frames, 
                           interval=100, blit=True)
        anim.save('game_of_life.gif', writer='pillow')
        plt.close()

if __name__ == "__main__":
    # 创建一个100x100的生命游戏
    game = GameOfLife(100, 100)
    game.animate()
