from manimlib.imports import *
class Morph(MovingCameraScene):
  CONFIG={
    "camera_config":{"background_color":WHITE},
  }
  def construct(self):
    n, k = 6, 4
    a = [1, 1, 5, 4, 3, 6]
    ob = [TextMobject("$%i$"% i,color = BLACK) for i in a]
    g = VGroup(*[i for i in ob])
    g.arrange_submobjects()
    self.camera_frame.scale(.5)
    self.play(
      GrowFromCenter(g)
      )
    self.wait(0.5)
    op = [(1, [3, 4, 1, 6]), 
          (0, [5, 3, 4, 5]),
          (2, [4, 5, 1, 1])]
    self.camera_frame.save_state()
    target = ScreenRectangle()
    target.set_width(1.95)
    target.move_to((ob[2].get_center() + ob[3].get_center()) / 2 + DOWN * .3)
    self.play(
      ReplacementTransform(self.camera_frame, target)
    )
    self.wait(0.5)
    ob2 = [TextMobject("$%i$"% i, color = BLACK) for i in op[0][1]]
    for i in range(4):
      ob2[i].next_to(ob[i + 1].get_center(), DOWN, buff = 0.5)
      self.play(
        ReplacementTransform(ob[i + 1].copy(), ob2[i])
        )
    self.wait(0.5)
    self.play(Restore(self.camera_frame))
    self.wait(0.5)
    self.play(
      *[FadeOutAndShift(ob[i + 1], UP) for i in range(4)],
      ob2[0].move_to, ob[1],
      ob2[1].move_to, ob[2],
      ob2[2].move_to, ob[3],
      ob2[3].move_to, ob[4],
    )
    for i in range(4):
      ob[i + 1] = ob2[i]
    self.wait(0.5)    

    target.move_to((ob[1].get_center() + ob[2].get_center()) / 2 + DOWN * .3)
    self.play(
      ReplacementTransform(self.camera_frame, target)
    )
    self.wait(0.5)
    ob2 = [TextMobject("$%i$"% i, color = BLACK) for i in op[1][1]]
    for i in range(4):
      ob2[i].next_to(ob[i].get_center(), DOWN, buff = 0.5)
    self.play(
      ReplacementTransform(ob[0].copy(), ob2[0]),
      ReplacementTransform(ob[3].copy(), ob2[3]),
    )
    for i in range(1, 3):
      self.play(
        ReplacementTransform(ob[i].copy(), ob2[i])
        )
    self.wait(0.5)
    self.play(Restore(self.camera_frame))
    self.wait(0.5)
    self.play(
      *[FadeOutAndShift(ob[i], UP) for i in range(4)],
      ob2[0].move_to, ob[0],
      ob2[1].move_to, ob[1],
      ob2[2].move_to, ob[2],
      ob2[3].move_to, ob[3],
    )

    for i in range(4):
      ob[i] = ob2[i]
    self.wait(0.5)    

    target.move_to((ob[3].get_center() + ob[4].get_center()) / 2 + DOWN * .3)
    self.play(
      ReplacementTransform(self.camera_frame, target)
    )
    self.wait(0.5)
    ob2 = [TextMobject("$%i$"% i, color = BLACK) for i in op[2][1]]
    for i in range(4):
      ob2[i].next_to(ob[i + 2].get_center(), DOWN, buff = 0.5)
    self.play(
      ReplacementTransform(ob[4].copy(), ob2[2]),
      ReplacementTransform(ob[5].copy(), ob2[3]),
    )
    for i in range(2):
      self.play(
        ReplacementTransform(ob[i + 2].copy(), ob2[i])
        )
    self.wait(0.5)
    self.play(Restore(self.camera_frame))
    self.wait(0.5)
    self.play(
      *[FadeOutAndShift(ob[i + 2], UP) for i in range(4)],
      ob2[0].move_to, ob[2],
      ob2[1].move_to, ob[3],
      ob2[2].move_to, ob[4],
      ob2[3].move_to, ob[5],
    )
    for i in range(4):
      ob[i + 2] = ob2[i]
    self.wait(0.5)  
    self.play(
      *[FadeOutAndShiftDown(ob[i]) for i in range(6)]
      )
    self.wait()