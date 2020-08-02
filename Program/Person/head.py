class face():
    def __init__(self):
        pass
class hair():
    def __init__(self):
        pass
class eye():
    def __init__(self):
        pass
class left_eye(eye):
    def __init__(self):
        super().__init__()
class right_eye(eye):
    def __init__(self):
        super().__init__()
class nose():
    def __init__(self):
        pass
class mouth():
    def __init__(self):
        pass
class ear():
    def __init__(self):
        pass
class left_ear():
    def __init__(self):
        super().__init__()
class right_ear():
    def __init__(self):
        super().__init__()
class neck():
    def __init__(self):
        pass
class head():
    def __init__(self,face,hair,left_eye,right_eye,nose,mouth,left_ear,right_ear,neck):
        self.face=face
        self.hair=hair
        self.left_eye=left_eye
        self.right_eye=right_eye
        self.nose=nose
        self.mouth=mouth
        self.left_ear=left_ear
        self.right_ear=right_ear
        self.neck=neck
    def say(self):
        print("说话")