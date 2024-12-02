import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation

class GameOfLife3D:
    def __init__(self, size):
        self.size = size
        self.grid = np.random.choice([0, 1], size=(size, size, size), p=[0.9, 0.1])
        self.cell_ages = np.zeros((size, size, size))  # Track cell ages

    def count_neighbors(self, x, y, z):
        """计算一个细胞周围26个位置的活细胞数量"""
        count = 0
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                for k in [-1, 0, 1]:
                    if i == 0 and j == 0 and k == 0:
                        continue
                    ni = (x + i) % self.size
                    nj = (y + j) % self.size
                    nk = (z + k) % self.size
                    count += self.grid[ni, nj, nk]
        return count

    def update(self):
        """更新网格状态"""
        new_grid = np.zeros_like(self.grid)
        new_ages = np.zeros_like(self.cell_ages)
        for x in range(self.size):
            for y in range(self.size):
                for z in range(self.size):
                    neighbors = self.count_neighbors(x, y, z)
                    # 3D生命游戏规则
                    if self.grid[x, y, z] == 1:
                        if neighbors in [4, 5]:  # 存活条件
                            new_grid[x, y, z] = 1
                            new_ages[x, y, z] = self.cell_ages[x, y, z] + 1
                    else:
                        if neighbors == 5:  # 繁殖条件
                            new_grid[x, y, z] = 1
        
        self.grid = new_grid
        self.cell_ages = new_ages
        return self.grid

    def animate(self, num_frames=50):
        """创建3D动画"""
        print("Starting animation setup...")
        fig = plt.figure(figsize=(12, 12))
        ax = fig.add_subplot(111, projection='3d')
        
        def update(frame):
            print(f"\nFrame {frame}: Starting update")
            ax.clear()
            # 获取活细胞的坐标
            x, y, z = np.where(self.grid == 1)
            print(f"Frame {frame}: Found {len(x)} active cells")
            
            if len(x) > 0:
                # 根据细胞年龄设置颜色
                colors = []
                for i in range(len(x)):
                    age = self.cell_ages[x[i], y[i], z[i]]
                    # 使用从蓝到红的渐变色
                    colors.append(plt.cm.viridis(min(age/10, 1.0)))
                
                ax.scatter(x, y, z, c=colors, marker='o', s=100, alpha=0.6)
                print(f"Frame {frame}: Plotted active cells")
            
            # 设置更好的视角
            ax.view_init(elev=30, azim=frame % 360)
            
            # 添加网格线
            ax.grid(True)
            ax.set_xlim(0, self.size)
            ax.set_ylim(0, self.size)
            ax.set_zlim(0, self.size)
            
            # 设置标签
            ax.set_xlabel('X')
            ax.set_ylabel('Y')
            ax.set_zlabel('Z')
            
            self.update()
            print(f"Frame {frame}: Grid updated")
        
        print("Setting up animation...")
        ani = animation.FuncAnimation(fig, update, frames=num_frames, 
                                    interval=200, blit=False)
        print("Saving animation to GIF...")
        ani.save('game_of_life_3d.gif', writer='pillow', fps=15)
        print("Animation saved successfully!")
        plt.close()

if __name__ == "__main__":
    game = GameOfLife3D(20)
    game.animate()
