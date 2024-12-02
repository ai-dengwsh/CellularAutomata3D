import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import colorsys

class LangtonsAnt:
    def __init__(self, width, height, num_ants=3):
        self.width = width
        self.height = height
        self.grid = np.zeros((height, width))
        
        self.ants = []
        for i in range(num_ants):
            pos = [
                height // 2 + np.random.randint(-height//4, height//4),
                width // 2 + np.random.randint(-width//4, width//4)
            ]
            hue = i / num_ants
            rgb = colorsys.hsv_to_rgb(hue, 0.8, 0.8)
            
            self.ants.append({
                'pos': pos,
                'direction': np.random.randint(0, 4),
                'color': rgb,
                'trail': np.zeros((height, width))
            })
            
        self.directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    def move(self):
        for ant in self.ants:
            current_color = self.grid[ant['pos'][0], ant['pos'][1]]
            
            self.grid[ant['pos'][0], ant['pos'][1]] = 1 - current_color
            ant['trail'][ant['pos'][0], ant['pos'][1]] = 1
            
            ant['direction'] = (ant['direction'] + (1 if current_color == 0 else -1)) % 4
            
            ant['pos'][0] = (ant['pos'][0] + self.directions[ant['direction']][0]) % self.height
            ant['pos'][1] = (ant['pos'][1] + self.directions[ant['direction']][1]) % self.width

    def animate(self, num_frames=500):
        fig, ax = plt.subplots(figsize=(10, 10))
        
        ax.set_xticks([])
        ax.set_yticks([])
        
        combined_trails = np.zeros((self.height, self.width, 3))
        img = ax.imshow(combined_trails, interpolation='nearest')
        ax.set_title('Ant Trails', fontsize=12)
        
        def update_frame(frame):
            nonlocal combined_trails
            for _ in range(50):
                self.move()
            
            combined_trails.fill(0)
            for ant in self.ants:
                for i in range(3):
                    combined_trails[:,:,i] += ant['trail'] * ant['color'][i]
            
            max_val = combined_trails.max()
            if max_val > 0:
                combined_trails /= max_val
                
            img.set_array(combined_trails)
            
            return [img]
        
        anim = FuncAnimation(fig, update_frame, frames=num_frames,
                           interval=50, blit=True)
        anim.save('langtons_ants.gif', writer='pillow', fps=30)
        plt.close()

if __name__ == "__main__":
    ants = LangtonsAnt(200, 200, num_ants=3)
    ants.animate()
