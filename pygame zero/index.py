import pgzrun



WIDTH = 800
HEIGHT = 600
bird_y = 200
bird_y_speed = 0

playing_area_width = 300
playing_area_height = 388

def draw():
    # etc.

    pipe_width = 54
    pipe_space_height = 100
    pipe_space_y = 150

    screen.draw.filled_rect(
        Rect(
            (playing_area_width, 0),
            (pipe_width, pipe_space_y)
        ),
        color=(94, 201, 72)
    )

    screen.draw.filled_rect(
        Rect(
            (playing_area_width, pipe_space_y + pipe_space_height),
            (pipe_width, playing_area_height - pipe_space_y - pipe_space_height)
        ),
        color=(94, 201, 72)
    )


pgzrun.go()