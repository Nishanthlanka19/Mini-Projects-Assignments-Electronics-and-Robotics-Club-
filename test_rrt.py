from myrrt import RRT, visualize #IMPORTS THE FUNCTIONS FROM RRT FILE

def test_rrt():
    
    obstacle_list = [
            [(2, 10), (7, 10), (6, 7), (4, 7), (4, 9), (2, 9)],
            [(3, 1), (3, 6), (4, 6), (4, 1)],
            [(7, 3), (7, 8), (9, 8), (9, 3)],
        ]

    start = (1, 1)
    goal = (10, 10)
    
    path = RRT(start,goal,obstacle_list)
     
    visualize(path,obstacle_list)

test_rrt()