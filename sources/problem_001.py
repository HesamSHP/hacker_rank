#Let's learn about list comprehensions!
# You are given three integers  and  representing the dimensions of a cuboid along with an integer.
# Print a list of all possible coordinates given by  on a 3D grid where the sum of  is not equal to.
# Here, . Please use list comprehensions rather than multiple loops, as a learning exercise.

if __name__ == '__main__':
    x = 1 #int(input())
    y = 2 #int(input())
    z = 3 #int(input())
    n = 3 #int(input())

    cube = [[i,j,k] for i in range(x) for j in range(y) for k in range(z) if i+j+k != n]

    print(cube)


