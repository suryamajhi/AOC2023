lines = open('input.txt').read().splitlines()

matrix = []
for line in lines:
    positions, velocities = line.split('@')
    x, y, z = positions.split(',')
    x1 = int(x)
    y1 = int(y)
    z1 = int(z)

    vx, vy, vz = velocities.split(',')
    x2 = x1 + int(vx)
    y2 = y1 + int(vy)
    z2 = z1 + int(vz)
    matrix.append([x1, y1, z1, x2, y2, z2])

start = 200000000000000
end = 400000000000000
ans = 0
for i, line in enumerate(matrix):
    x1, y1, z1, x2, y2, z2 = line
    for j in range(i + 1, len(matrix)):
        x3, y3, z3, x4, y4, z4 = matrix[j]

        dt = ((x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4))
        if dt != 0:
            x = ((x1 * y2 - y1 * x2)* (x3 - x4) - (x1 - x2) * (x3*y4 - y3*x4)) / ((x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4))
            y = ((x1 * y2 - y1 * x2)* (y3 - y4) - (y1 - y2) * (x3*y4 - y3*x4)) / ((x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4))

            futureA = (x > x2) == (x2 > x1) and (y > y2) == (y2 > y1)
            futureB = (x > x4) == (x4 > x3) and (y > y4) == (y4 > y3)
            if start <= x <= end and start <= y <= end and futureA and futureB:
                ans += 1

            # print((x, y))

print(ans)
