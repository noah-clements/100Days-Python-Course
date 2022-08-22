from turtle import Turtle

UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:
    
    def __init__(self, starting_segments=3, color="white") -> None:
        self.color = color
        self.starting_segments = starting_segments
        self.segments = []
        self.create_snake(starting_segments)
        self.head = self.segments[0]
        
    
    def __repr__(self) -> str:
        return "<Snake with %s segments, color:%s>" % (len(self.segments), self.color)
    
    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.color(self.color)
        new_segment.pensize(width=20)
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)
        
    
    def create_snake(self, num_segments):
        for i in range(num_segments):
            self.add_segment(((i * -20), 0))
            

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            # self.segments[0].speed(speed)
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(15)
        # self.head.left(90)
        
    def enlarge(self):
        # add a new segment to the snake
        self.add_segment(self.segments[-1].position())
    
    def reset(self):
        self.segments.clear()
        self.create_snake(self.starting_segments)
        self.head = self.segments[0]
            
    
        
