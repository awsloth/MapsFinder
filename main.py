import json
from os import stat

with open("info.json", "r") as f:
    info = json.loads(f.read())

with open("matrix.json", "r") as f:
    matrix = json.loads(f.read())

def create_matrix(grid):
    matrix = []
    for row in grid['rows']:
        matrix.append([x['duration']['value'] for x in row['elements']])

    return matrix

def format_mat(matrix):
    return "\n".join([" ".join([y.rjust(4, " ") for y in map(str, x)]) for x in matrix])


class Node:
    def __init__(self, lat, lng, plc_id, name) -> None:
        self.lat = lat
        self.lng = lng
        self.plc_id = plc_id
        self.name = name

nodes = [Node(*item['location'], item['place_id'], item['name']) for item in info['places']]
start = Node(*info['start']['location'], info['start']['place_id'], info['start']['name'])
end = Node(*info['end']['location'], info['end']['place_id'], info['end']['name'])

inner_matrix = create_matrix(matrix['inner'])
start_matrix = create_matrix(matrix['start'])
end_matrix = create_matrix(matrix['end'])

print(format_mat(inner_matrix))