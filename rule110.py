import numpy as np
import matplotlib.pyplot as plt

class Rule110:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = np.zeros((height, width), dtype=int)
        
        # 初始化第一行，设置一个简单的模式
        self.grid[0, -10:] = [1, 1, 0, 1, 0, 1, 1, 0, 0, 1]

    def apply_rule(self, left, center, right):
        """应用Rule 110规则"""
        pattern = (left << 2) | (center << 1) | right
        # Rule 110的规则表: 01110110
        return (110 >> pattern) & 1

    def generate(self):
        """生成整个图案"""
        for i in range(self.height-1):
            for j in range(self.width):
                # 获取左中右三个相邻单元的状态
                left = self.grid[i, (j-1) % self.width]
                center = self.grid[i, j]
                right = self.grid[i, (j+1) % self.width]
                
                # 应用规则并更新下一行
                self.grid[i+1, j] = self.apply_rule(left, center, right)
        
        return self.grid

    def plot(self, save_path=None):
        """绘制并保存结果"""
        plt.figure(figsize=(12, 12))
        plt.imshow(self.grid, cmap='binary', interpolation='nearest')
        plt.axis('off')
        if save_path:
            plt.savefig(save_path, bbox_inches='tight', pad_inches=0, dpi=300)
            plt.close()
        else:
            plt.show()

    def animate(self, num_frames=200):
        """创建动画展示生成过程"""
        fig, ax = plt.subplots(figsize=(12, 12))
        ax.set_xticks([])
        ax.set_yticks([])
        
        # 初始化显示
        img = ax.imshow(np.zeros((self.height, self.width)), 
                       cmap='binary', interpolation='nearest')
        
        current_grid = np.zeros((self.height, self.width), dtype=int)
        current_grid[0, -10:] = [1, 1, 0, 1, 0, 1, 1, 0, 0, 1]
        
        def update(frame):
            if frame > 0:
                # 更新下一行
                for j in range(self.width):
                    left = current_grid[frame-1, (j-1) % self.width]
                    center = current_grid[frame-1, j]
                    right = current_grid[frame-1, (j+1) % self.width]
                    current_grid[frame, j] = self.apply_rule(left, center, right)
            
            img.set_array(current_grid)
            return [img]
        
        from matplotlib.animation import FuncAnimation
        anim = FuncAnimation(fig, update, frames=self.height,
                           interval=50, blit=True)
        anim.save('rule110_evolution.gif', writer='pillow', fps=30)
        plt.close()

if __name__ == "__main__":
    # 创建一个400x400的图案
    automaton = Rule110(400, 400)
    # 生成静态图案
    automaton.generate()
    automaton.plot("rule110_pattern.png")
    # 创建动画展示生成过程
    automaton.animate()
