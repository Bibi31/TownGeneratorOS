"""Perlin noise implementation."""
from typing import List


class PerlinNoise:
    """Perlin noise generator."""
    
    _PERMUTATION = [
        151, 160, 137, 91, 90, 15,
        131, 13, 201, 95, 96, 53, 194, 233, 7, 225, 140, 36, 103, 30, 69, 142, 8, 99, 37, 240, 21, 10, 23,
        190, 6, 148, 247, 120, 234, 75, 0, 26, 197, 62, 94, 252, 219, 203, 117, 35, 11, 32, 57, 177, 33,
        88, 237, 149, 56, 87, 174, 20, 125, 136, 171, 168, 68, 175, 74, 165, 71, 134, 139, 48, 27, 166,
        77, 146, 158, 231, 83, 111, 229, 122, 60, 211, 133, 230, 220, 105, 92, 41, 55, 46, 245, 40, 244,
        102, 143, 54, 65, 25, 63, 161, 1, 216, 80, 73, 209, 76, 132, 187, 208, 89, 18, 169, 200, 196,
        135, 130, 116, 188, 159, 86, 164, 100, 109, 198, 173, 186, 3, 64, 52, 217, 226, 250, 124, 123,
        5, 202, 38, 147, 118, 126, 255, 82, 85, 212, 207, 206, 59, 227, 47, 16, 58, 17, 182, 189, 28, 42,
        223, 183, 170, 213, 119, 248, 152, 2, 44, 154, 163, 70, 221, 153, 101, 155, 167, 43, 172, 9,
        129, 22, 39, 253, 19, 98, 108, 110, 79, 113, 224, 232, 178, 185, 112, 104, 218, 246, 97, 228,
        251, 34, 242, 193, 238, 210, 144, 12, 191, 179, 162, 241, 81, 51, 145, 235, 249, 14, 239, 107,
        49, 192, 214, 31, 181, 199, 106, 157, 184, 84, 204, 176, 115, 121, 50, 45, 127, 4, 150, 254,
        138, 236, 205, 93, 222, 114, 67, 29, 24, 72, 243, 141, 128, 195, 78, 66, 215, 61, 156, 180
    ]
    
    _ease: List[float] = None
    
    def __init__(self, seed: int):
        """Initialize Perlin noise with a seed."""
        self.p = [self._PERMUTATION[(i + seed) % 256] for i in range(256)]
        self.p = self.p + self.p
        
        if PerlinNoise._ease is None:
            PerlinNoise._ease = []
            for i in range(256):
                t = i / 256
                PerlinNoise._ease.append(t * t * t * (t * (6 * t - 15) + 10))
    
    def _dot(self, hash_val: int, x: float, y: float) -> float:
        """Compute dot product."""
        h = hash_val & 3
        if h == 0:
            return x + y
        elif h == 1:
            return x - y
        elif h == 2:
            return -x + y
        elif h == 3:
            return -x - y
        else:
            return 0
    
    def _interpolate(self, a: float, b: float, w: float) -> float:
        """Linear interpolation."""
        return a + (b - a) * w
    
    def noise(self, x: float, y: float, grid_size: float = 1.0) -> float:
        """Generate Perlin noise at given coordinates."""
        j0 = int(x)
        j1 = j0 + 1
        
        fx = x - j0
        wx = self._ease[int(fx * 256)]
        
        i0 = int(y)
        i1 = i0 + 1
        
        fy = y - i0
        wy = self._ease[int(fy * 256)]
        
        aa = self.p[self.p[j0] + i0]
        ab = self.p[self.p[j1] + i0]
        ba = self.p[self.p[j0] + i1]
        bb = self.p[self.p[j1] + i1]
        
        v0 = self._dot(aa, fx, fy)
        v1 = self._dot(ab, fx - 1, fy)
        val0 = self._interpolate(v0, v1, wx)
        v0 = self._dot(ba, fx, fy - 1)
        v1 = self._dot(bb, fx - 1, fy - 1)
        val1 = self._interpolate(v0, v1, wx)
        
        return self._interpolate(val0, val1, wy)
    
    def noise_map(self, width: int, height: int, grid_size: float = 1.0) -> List[List[float]]:
        """Generate a 2D map of Perlin noise."""
        grid = [[0.0 for _ in range(width)] for _ in range(height)]
        
        x_step = grid_size / width
        y_step = grid_size / height
        
        y = 0.0
        for i in range(height):
            i0 = int(y)
            i1 = i0 + 1
            
            fy = y - i0
            wy = self._ease[int(fy * 256)]
            
            x = 0.0
            for j in range(width):
                j0 = int(x)
                j1 = j0 + 1
                
                fx = x - j0
                wx = self._ease[int(fx * 256)]
                
                aa = self.p[self.p[j0] + i0]
                ab = self.p[self.p[j1] + i0]
                ba = self.p[self.p[j0] + i1]
                bb = self.p[self.p[j1] + i1]
                
                v0 = self._dot(aa, fx, fy)
                v1 = self._dot(ab, fx - 1, fy)
                val0 = self._interpolate(v0, v1, wx)
                v0 = self._dot(ba, fx, fy - 1)
                v1 = self._dot(bb, fx - 1, fy - 1)
                val1 = self._interpolate(v0, v1, wx)
                
                grid[i][j] = self._interpolate(val0, val1, wy)
                
                x += x_step
            
            y += y_step
        
        return grid
    
    def noise_high(self, x: float, y: float, octaves: int, grid_size: float = 1.0, 
                   persistence: float = 0.5) -> float:
        """Generate high-octave Perlin noise."""
        result = self.noise(x, y, grid_size)
        
        amplitude = persistence
        for i in range(1, octaves):
            grid_size *= 2
            result += self.noise(x, y, grid_size) * amplitude
            amplitude *= persistence
        
        return result
    
    def noise_map_high(self, width: int, height: int, octaves: int, 
                       grid_size: float = 1.0, persistence: float = 0.5) -> List[List[float]]:
        """Generate a 2D map of high-octave Perlin noise."""
        result = self.noise_map(width, height, grid_size)
        
        amplitude = persistence
        for i in range(1, octaves):
            grid_size *= 2
            o = self.noise_map(width, height, grid_size)
            for y in range(height):
                for x in range(width):
                    result[y][x] += o[y][x] * amplitude
            amplitude *= persistence
        
        return result
