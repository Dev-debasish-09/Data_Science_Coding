# . Facebook: 
# Given a list of coordinates, 
# write a function to find the k closest points (measured by Euclidean distance) to the origin. 
# For example, if k = 3 and the points are: [[2, -1], [3, 2], [4, 1], [-1, -1], [-2, 2]], 
# then return [[-1,1], [2, -1], [-2, 2]].


def k_closest_points(points, k):
    distance_dict = {}
    for i in points:
        distance_dict[tuple(i)] = i[0]**2 + i[1]**2
    sorted_points = sorted(distance_dict.items(),key=lambda x:abs(x[1]))
    closet = [list(point) for point,dist in sorted_points[:k]]
    return closet

# Test case
points = [[2, -1], [3, 2], [4, 1], [-1, -1], [-2, 2]]
k = 3
print(k_closest_points(points, k))  # Output: [[-1, -1], [2, -1], [-2, 2]]
