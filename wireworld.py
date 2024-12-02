import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class WireWorld:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = np.zeros((height, width), dtype=int)
        self.setup_initial_state()
        
    def setup_initial_state(self):
        """设置初始状态 - 创建一个简单的电子振荡器"""
        # 创建导线（状态1）
        mid = self.height // 2
        self.grid[mid, mid-5:mid+5] = 1
        # 添加电子头（状态2）和电子尾（状态3）
        self.grid[mid, mid-1] = 2
        self.grid[mid, mid-2] = 3

    def count_electron_heads(self, x, y):
        """计算周围8个格子中电子头的数量"""
        count = 0
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                if i == 0 and j == 0:
                    continue
                ni = (x + i) % self.height
                nj = (y + j) % self.width
                if self.grid[ni, nj] == 2:
                    count += 1
        return count

    def update(self):
        """更新网格状态"""
        new_grid = np.zeros_like(self.grid)
        for i in range(self.height):
            for j in range(self.width):
                current = self.grid[i, j]
                if current == 0:  # 空格子保持空
                    new_grid[i, j] = 0
                elif current == 1:  # 导线
                    # 如果有1或2个相邻的电子头，变成电子头
                    heads = self.count_electron_heads(i, j)
                    if heads in [1, 2]:
                        new_grid[i, j] = 2
                    else:
                        new_grid[i, j] = 1
                elif current == 2:  # 电子头变成电子尾
                    new_grid[i, j] = 3
                elif current == 3:  # 电子尾变回导线
                    new_grid[i, j] = 1
        
        self.grid = new_grid
        return self.grid

    def animate(self, num_frames=100):
        """创建动画"""
        fig, ax = plt.subplots(figsize=(10, 10))
        ax.set_xticks([])
        ax.set_yticks([])
        cmap = plt.cm.colors.ListedColormap(['black', 'yellow', 'blue', 'red'])
        img = ax.imshow(self.grid, interpolation='nearest', cmap=cmap)
        
        def update_frame(frame):
            self.update()
            img.set_array(self.grid)
            return [img]
        
        anim = FuncAnimation(fig, update_frame, frames=num_frames, 
                           interval=100, blit=True)
        anim.save('wireworld.gif', writer='pillow')
        plt.close()

if __name__ == "__main__":
    wire = WireWorld(50, 50)
    wire.animate()
