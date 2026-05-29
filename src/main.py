import pygame
import os

pygame.init()

tileSize = 64

tile = {
    0: "grass",
    1: "dirt",
    2: "wood",
    3: "leaf",
    4: "sky",
    5: "sun",
    6: "rock",
}


class TileMap:
    def __init__(self, path, assets_path):
        self.map = self.load_map(path)
        self.assets = self.load_assets(assets_path)

    def load_map(self, path):
        grid = []
        with open(path, "r") as f:
            for line in f:
                grid.append([int(x) for x in line.split()])
        return grid

    def load_assets(self, path):
        assets = {}

        for id, name in tile.items():
            img_path = os.path.join(path, f"{name}.png")

            assets[id] = pygame.transform.scale(
                pygame.image.load(img_path).convert_alpha(),
                (tileSize, tileSize)
            )

        return assets

    def draw(self, screen):
        for y, row in enumerate(self.map):
            for x, tile_id in enumerate(row):

                img = self.assets.get(tile_id)

                if img:
                    screen.blit(img, (x * tileSize, y * tileSize))

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        pygame.display.set_caption("W tilemap")

        base = os.path.dirname(__file__)

        self.tilemap = TileMap(
            os.path.join(base, "tile.txt"),
            os.path.join(os.path.dirname(base), "assets")
        )

        self.clock = pygame.time.Clock()
        self.running = True

    def run(self):
        while self.running:
            self.events()
            self.draw()

        pygame.quit()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.tilemap.draw(self.screen)
        pygame.display.flip()
        self.clock.tick(60)

if __name__ == "__main__":
    Game().run()
