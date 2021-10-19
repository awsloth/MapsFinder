import sys
import json

import pygame
from pygame.locals import *

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 400

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

label = pygame.font.SysFont("ComicSansMS", 8)

class Location:
    def __init__(self, lat, lng, p_id, name, colour=(255, 0, 0)):
        self.lat = lat
        self.lng = lng
        self.p_id = p_id
        self.name = name
        self.colour = colour

    def x_dist(self, node):
        return abs(self.lng - node.lng)

    def y_dist(self, node):
        return abs(self.lat - node.lat)

    def draw(self, centre_loc, surface, scale):
        x = SCREEN_WIDTH / 2 - (self.lng - centre_loc.lng)*scale
        y = (self.lat - centre_loc.lat)*scale + SCREEN_HEIGHT / 2

        pygame.draw.circle(surface, self.colour, (x, y), 2)

        render = label.render(self.name, True, (0, 0, 0))

        x_pos = x + 3
        y_pos = y - 1

        if x + 3 + render.get_width() > SCREEN_WIDTH:
            x_pos = x - render.get_width() - 3

        if y - 1 + render.get_height() > SCREEN_HEIGHT:
            y_pos = y - render.get_height() - 1

        surface.blit(render, (x_pos, y_pos))

        return x, y

with open("info.json", "r") as f:
    info = json.loads(f.read())

start = info['start']
end = info['end']

nodes = [
    Location(*start['location'].values(), start['place_id'], start['name'], (0, 255, 0)),
    Location(*end['location'].values(), end['place_id'], end['name'], (0, 255, 0))
]

nodes += [Location(*x['location'].values(), x['place_id'], x['name']) for x in info['places']]

lats = [x.lat for x in nodes]
lngs = [x.lng for x in nodes]
lat_dist = max(lats) - min(lats)
lng_dist = max(lngs) - min(lngs)
mid_lat = lat_dist / 2 + min(lats)
mid_lng = lng_dist / 2 + min(lngs)

middle_node = Location(mid_lat, mid_lng, "i", "Middle")

max_x_gap = max([node.x_dist(middle_node) for node in nodes])
max_y_gap = max([node.y_dist(middle_node) for node in nodes])

scale = min(
    [
        SCREEN_WIDTH / (2 * max_x_gap),
        SCREEN_HEIGHT / (2 * max_y_gap)
    ]
)

while 1:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((255, 255, 255))

    for node in nodes:
        node.draw(middle_node, screen, scale)

    pygame.display.flip()