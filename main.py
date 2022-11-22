from maze import maze

maze = maze([
    ["W","W","B","B","B"],
    ["B","W","W","B","B"],
    ["B","W","W","W","W"],
    ["B","W","W","W","W"],
    ["B","W","B","B","W"],
],[0,0],[4,4])

maze.show_env()

maze.train(10,0.2,0.2)
