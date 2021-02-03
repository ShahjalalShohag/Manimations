from manimlib.imports import *
class subgraph(Scene):
	def point_along_line(a, b, d):
		v = b - a
		v = v / np.linalg.norm(v)
		return a + v * d
	def graph(n, edge, pos):
		node = []
		for i in range(n + 1):
			node.append(Circle(radius = 0.25, color = BLACK, arc_center = pos[i]))
		index = [TextMobject("$%i$"% i) for i in range(n + 1)]
		for i in range(1, n + 1):
			index[i].shift(node[i].get_center())
			index[i].scale(0.6)
			index[i].set_color(BLACK);
		g1 = VGroup(
			*[Line(subgraph.point_along_line(pos[i[0]], pos[i[1]], node[i[0]].get_arc_length() / 2 / PI), 
				subgraph.point_along_line(pos[i[1]], pos[i[0]], node[i[1]].get_arc_length() / 2 / PI), color = BLACK) for i in edge],
			*[node[i] for i in range(1, n + 1)],
			*[index[i] for i in range(1, n + 1)],
			)
		return g1
	def construct(self):
		n = 5
		pos = []
		for i in range(n + 1):
			pos.append(np.array([0, 0, 0]))
		pos[1] = np.array([0, 2, 0])
		pos[2] = pos[1] + DOWN + LEFT
		pos[3] = pos[1] + DOWN + RIGHT
		pos[4] = pos[2] + DOWN + LEFT
		pos[5] = pos[3] + DOWN + RIGHT
		edge = [(1, 2), (1, 3), (2, 3), (2, 4), (3, 5), (2, 5), (4, 5)]
		g1 = subgraph.graph(n, edge, pos)
		g1.move_to(LEFT * 3)

		edge = [(1, 3), (3, 5), (2, 4)]
		g2 = subgraph.graph(n, edge, pos)
		g2.move_to(RIGHT * 3)

		t1 = TextMobject("A", color = BLACK)
		t1.next_to(g1, DOWN, buff = 0.5)

		t2 = TextMobject("B", color = BLACK)
		t2.next_to(g2, DOWN, buff = 0.5)
		
		self.play(GrowFromCenter(g1),
			GrowFromCenter(g2), 
			Write(t1),
			Write(t2))
		self.wait(2)

		t = TextMobject("B is a subgraph of A")
		t.shift(DOWN * 3)
		t.set_color(GREEN)

		self.play(
			FadeToColor(g2[0], GREEN),
			FadeToColor(g2[1], GREEN),
			FadeToColor(g2[2], GREEN),
			ReplacementTransform(g2[0].copy(), g1[1]),
			ReplacementTransform(g2[1].copy(), g1[4]),
			ReplacementTransform(g2[2].copy(), g1[3]),
			FadeToColor(g1[1], GREEN),
			FadeToColor(g1[4], GREEN),
			FadeToColor(g1[3], GREEN),
			Write(t)
			)
		self.wait()
		self.play(Uncreate(g1),
			Uncreate(g2),
			Uncreate(t1),
			Uncreate(t2),
			Uncreate(t)
			)
		return

class subgraph2(Scene):
	def construct(self):
		n = 5
		pos = []
		for i in range(n + 1):
			pos.append(np.array([0, 0, 0]))
		pos[1] = np.array([0, 2, 0])
		pos[2] = pos[1] + DOWN + LEFT
		pos[3] = pos[1] + DOWN + RIGHT
		pos[4] = pos[2] + DOWN + LEFT
		pos[5] = pos[3] + DOWN + RIGHT
		edge = [(1, 2), (1, 3), (2, 3), (2, 4), (3, 5), (2, 5), (4, 5)]
		g1 = subgraph.graph(n, edge, pos)
		g1.move_to(LEFT * 3)

		edge = [(1, 3), (3, 5), (2, 4), (3, 4)]
		g2 = subgraph.graph(n, edge, pos)
		g2.move_to(RIGHT * 3)

		t1 = TextMobject("A", color = BLACK)
		t1.next_to(g1, DOWN, buff = 0.5)

		t2 = TextMobject("B", color = BLACK)
		t2.next_to(g2, DOWN, buff = 0.5)
		
		self.play(GrowFromCenter(g1),
			GrowFromCenter(g2), 
			Write(t1),
			Write(t2))
		self.wait(2)

		t = TextMobject("B is not a subgraph of A")
		t.set_color(RED)
		t.shift(DOWN * 3)
		self.play(
			FadeToColor(g2[0], GREEN),
			FadeToColor(g2[1], GREEN),
			FadeToColor(g2[2], GREEN),
			FadeToColor(g2[3], RED),
			ReplacementTransform(g2[0].copy(), g1[1]),
			ReplacementTransform(g2[1].copy(), g1[4]),
			ReplacementTransform(g2[2].copy(), g1[3]),
			FadeToColor(g1[1], GREEN),
			FadeToColor(g1[4], GREEN),
			FadeToColor(g1[3], GREEN),
			Write(t)
			)
		self.wait()
		self.play(Uncreate(g1),
			Uncreate(g2),
			Uncreate(t1),
			Uncreate(t2),
			Uncreate(t)
			)
		return
class subgraph3(MovingCameraScene):
	CONFIG={
    "camera_config":{"background_color":WHITE},
   }
	def construct(self):
		self.camera_frame.scale(0.85)
		subgraph.construct(self)
		subgraph2.construct(self)

