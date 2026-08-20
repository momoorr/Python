import pygame
import random

pygame.init()

# 화면 및 블록 설정
BLOCK_SIZE = 30
COLS, ROWS = 10, 20
WIDTH, HEIGHT = COLS * BLOCK_SIZE, ROWS * BLOCK_SIZE
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("간단한 테트리스")
CLOCK = pygame.time.Clock()

# 색상 정의
BLACK = (20, 20, 20)
GRAY = (50, 50, 50)
COLORS = [
    (0, 255, 255),  # I (청록)
    (255, 255, 0),  # O (노랑)
    (128, 0, 128),  # T (보라)
    (0, 255, 0),    # S (초록)
    (255, 0, 0),    # Z (빨강)
    (0, 0, 255),    # J (파랑)
    (255, 127, 0)   # L (주황)
]

# 테트로미노 모양 정의 (4x4 기준 상대 좌표)
SHAPES = [
    [[1, 5, 9, 13], [4, 5, 6, 7]],                 # I
    [[0, 1, 4, 5]],                                 # O
    [[1, 4, 5, 6], [1, 4, 5, 9], [4, 5, 6, 9], [1, 5, 6, 9]],  # T
    [[4, 5, 1, 2], [0, 4, 5, 9]],                 # S
    [[0, 1, 5, 6], [2, 5, 6, 9]],                 # Z
    [[0, 4, 5, 6], [1, 5, 9, 8], [4, 5, 6, 10], [1, 2, 5, 9]], # J
    [[2, 4, 5, 6], [1, 5, 9, 10], [4, 5, 6, 8], [0, 1, 5, 9]]  # L
]

class Piece:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.type = random.randint(0, len(SHAPES) - 1)
        self.color = COLORS[self.type]
        self.rotation = 0

    def image(self):
        return SHAPES[self.type][self.rotation]

    def rotate(self):
        self.rotation = (self.rotation + 1) % len(SHAPES[self.type])

def create_grid(locked_pos):
    grid = [[BLACK for _ in range(COLS)] for _ in range(ROWS)]
    for (c, r), color in locked_pos.items():
        if r >= 0:
            grid[r][c] = color
    return grid

def convert_piece_format(piece):
    positions = []
    shape = piece.image()
    for i in shape:
        x = i % 4
        y = i // 4
        positions.append((piece.x + x, piece.y + y))
    return positions

def valid_space(piece, locked_pos):
    accepted_pos = [[(j, i) for j in range(COLS) if (j, i) not in locked_pos] for i in range(ROWS)]
    accepted_pos = [item for sub in accepted_pos for item in sub]
    formatted = convert_piece_format(piece)

    for pos in formatted:
        if pos not in accepted_pos and pos[1] >= 0:
            return False
    return True

def clear_rows(grid, locked):
    cleared = 0
    for r in range(ROWS - 1, -1, -1):
        if BLACK not in grid[r]:
            cleared += 1
            for c in range(COLS):
                del locked[(c, r)]
            for (c, y) in sorted(list(locked.keys()), key=lambda item: item[1], reverse=True):
                if y < r:
                    locked[(c, y + 1)] = locked.pop((c, y))
    return cleared

def draw_grid(surface, grid):
    for r in range(ROWS):
        for c in range(COLS):
            pygame.draw.rect(surface, grid[r][c], (c * BLOCK_SIZE, r * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
            pygame.draw.rect(surface, GRAY, (c * BLOCK_SIZE, r * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 1)

def main():
    locked_positions = {}
    current_piece = Piece(3, 0)
    fall_time = 0
    fall_speed = 0.4
    run = True

    while run:
        grid = create_grid(locked_positions)
        fall_time += CLOCK.get_rawtime()
        CLOCK.tick()

        # 자동 낙하
        if fall_time / 1000 >= fall_speed:
            fall_time = 0
            current_piece.y += 1
            if not valid_space(current_piece, locked_positions):
                current_piece.y -= 1
                for pos in convert_piece_format(current_piece):
                    locked_positions[pos] = current_piece.color
                current_piece = Piece(3, 0)
                clear_rows(grid, locked_positions)
                if not valid_space(current_piece, locked_positions):
                    run = False  # 게임 오버

        # 키 입력 이벤트
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    current_piece.x -= 1
                    if not valid_space(current_piece, locked_positions):
                        current_piece.x += 1
                elif event.key == pygame.K_RIGHT:
                    current_piece.x += 1
                    if not valid_space(current_piece, locked_positions):
                        current_piece.x -= 1
                elif event.key == pygame.K_DOWN:
                    current_piece.y += 1
                    if not valid_space(current_piece, locked_positions):
                        current_piece.y -= 1
                elif event.key == pygame.K_UP:
                    old_rotation = current_piece.rotation
                    current_piece.rotate()
                    if not valid_space(current_piece, locked_positions):
                        current_piece.rotation = old_rotation
                elif event.key == pygame.K_SPACE:  # 하드 드롭
                    while valid_space(current_piece, locked_positions):
                        current_piece.y += 1
                    current_piece.y -= 1

        # 현재 블록 그리기
        piece_pos = convert_piece_format(current_piece)
        for c, r in piece_pos:
            if r >= 0:
                grid[r][c] = current_piece.color

        SCREEN.fill(BLACK)
        draw_grid(SCREEN, grid)
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()



### 에러 해결1

#Module Not Found … pygame
# 현재 내 컴에 pygame이라는 라이브러리가 없다. —> 설치해주면 된다.
#import pygame

### Q1

#import란? 
#라이브러리를 결합해주면 명령

### Q2

#라이브러리란?
#Library : 도서관 —> 도서관에 뭐가 있죠?: 책들이 있죠.
