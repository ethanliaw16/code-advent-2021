import sys

def reachable_points_from(point, edges):
    reachable_points = []
    for edge in edges:
        if point in edge:
            for vertex in edge:
                if point != vertex:
                    reachable_points.append(vertex)
    return reachable_points

def destination_of_edge(edge):
    return edge.split("-")[1]

def allowed_neighbors(point, edges, visited, restricted):
    all_points = reachable_points_from(point, edges)
    allowed_points = []
    for vertex in all_points:
        if vertex in visited:
            if not vertex in restricted:
                allowed_points.append(vertex)
        else:
            allowed_points.append(vertex)
            #visited.append(vertex)
    return allowed_points

def allowed_neighbors_2(point, edges, visited, restricted, exception):
    all_points = reachable_points_from(point, edges)
    allowed_points = []
    exceptions = []
    for vertex in all_points:
        new_exception = exception
        if vertex in visited:
            if not vertex in restricted:
                allowed_points.append(vertex)
                exceptions.append(new_exception)
            elif new_exception == 'unused' and vertex != 'start' and vertex != 'end':
                allowed_points.append(vertex)
                new_exception = vertex
                exceptions.append(new_exception)
        else:
            allowed_points.append(vertex)
            exceptions.append(new_exception)
            #visited.append(vertex)
    return [allowed_points, exceptions]

def all_paths(paths, edges, visited, restricted, start_to_end):
    new_paths = []
    new_visited = []
    if paths == []:
        return start_to_end
    for i in range(len(paths)):
        path = paths[i]
        if path[-1] != "end":
            #print(f"Path is {path}, last is {path[-1]}, enumerating paths from here")
            allowed = allowed_neighbors(path[-1], edges, visited[i], restricted)
            #print(f"Allowed neighbors from {path[-1]} are {allowed}")
            for point in allowed:
                new_paths.append(path + [point])
                new_visited.append(visited[i] + [point])
        else:
            #print(f"New start to end path: {path}")
            if path in start_to_end:
                print(f"Uh Oh, {path} is a dupe")
                break
            start_to_end.append(path)
            #print(f"{len(start_to_end)} total finished paths")
            #for finished_path in start_to_end:
            #    print(finished_path)
    
    return all_paths(new_paths, edges, new_visited, restricted, start_to_end)

def all_paths_with_exception(paths, edges, visited, restricted, start_to_end, exception):
    new_paths = []
    new_visited = []
    new_exceptions = []
    if paths == []:
        return start_to_end
    for i in range(len(paths)):
        path = paths[i]
        if path[-1] != "end":
            #print(f"Path is {path}, last is {path[-1]}, enumerating paths from here")
            #print(f"path {i}: exceptions are {exception}")
            info_for_neighbors = allowed_neighbors_2(path[-1], edges, visited[i], restricted, exception[i])
            allowed = info_for_neighbors[0]
            exception_for_allowed = info_for_neighbors[1]
            #print(f"Allowed neighbors from {path[-1]} are {allowed}")
            for point in allowed:
                new_paths.append(path + [point])
                new_visited.append(visited[i] + [point])
            #print(f"Exceptions for possible points at this path: {exception_for_allowed}")
            for exception_for_neighbor in exception_for_allowed:
                new_exceptions.append(exception_for_neighbor)

        else:
            #print(f"New start to end path: {path}")
            if path in start_to_end:
                print(f"Uh Oh, {path} is a dupe")
                break
            start_to_end.append(path)
            if (i % 1000 == 0):
                print(f"{len(start_to_end)} total finished paths")
            #for finished_path in start_to_end:
            #    print(finished_path)
    
    return all_paths_with_exception(new_paths, edges, new_visited, restricted, start_to_end, new_exceptions)



#def path_to_end_from(current_path, edges, visited, restricted):
#    allowed_paths = allowed_paths_from_point(current_path[-1], edges, visited, restricted)
#    for path in allowed_paths:
#        if path.split("-")[1] == "end":
#            return ["end"]
        

edges = []
points = []
restricted_points = []

def is_restricted(point):
    for character in point:
        if not character.islower():
            return False
    return True

for line in sys.stdin:
    if line[:-1] == '':
        break
    edges.append(line[:-1].split("-"))
    points_in_line = line[:-1].split("-")
    for point in points_in_line:
        if not point in points:
            points.append(point)
        if is_restricted(point) and not point in restricted_points:
            restricted_points.append(point) 

start_to_end = []
print(f"Edges: {edges}")
print(f"Points: {points}")
print(f"Restricted points: {restricted_points}")
print(f"Edges we can go on from the starting point: {reachable_points_from(points[0], edges)}")
print(f"Testing recursion: {len(all_paths_with_exception([[points[0]]], edges, [[points[0]]], restricted_points, start_to_end, ['unused']))}")