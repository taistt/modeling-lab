from manim import *

class RankGeometry(Scene):
    def construct(self):
        # Title
        title = Text("Geometrical Interpretation of Matrix Rank", font_size=32)
        title.to_edge(UP)
        self.play(Write(title))

        # Create coordinate grid
        grid = NumberPlane(
            x_range=[-4, 4, 1],
            y_range=[-3, 3, 1],
            background_line_style={"stroke_opacity": 0.5}
        )
        self.play(Create(grid))

        v1 = Arrow(
            ORIGIN, RIGHT * 2, buff=0, color=BLUE, stroke_width=6
        )
        v2 = Arrow(
            ORIGIN, UP * 2, buff=0, color=GREEN, stroke_width=6
        )

        self.play(GrowArrow(v1), GrowArrow(v2))

        rank_label = MathTex(r"\operatorname{rank}(A)=2").to_corner(UR)
        description = Text("Rank 2: the image is a plane", font_size=24)
        description.to_edge(DOWN)

        self.play(Write(rank_label), Write(description))
        self.wait(2)

        rank1_label = MathTex(r"\operatorname{rank}(A)=1").to_corner(UR)
        description1 = Text(
            "Rank 1: the image collapses to a line", font_size=24
        ).to_edge(DOWN)

        self.play(
            grid.animate.apply_matrix([[1, 0], [0, 0]]),
            v2.animate.put_start_and_end_on(ORIGIN, RIGHT * 2),
            Transform(rank_label, rank1_label),
            Transform(description, description1),
            run_time=2
        )
        self.wait(2)

        rank0_label = MathTex(r"\operatorname{rank}(A)=0").to_corner(UR)
        description0 = Text(
            "Rank 0: the image is only the origin", font_size=24
        ).to_edge(DOWN)

        self.play(
            grid.animate.apply_matrix([[0, 0], [0, 0]]),
            v1.animate.put_start_and_end_on(ORIGIN, ORIGIN),
            v2.animate.put_start_and_end_on(ORIGIN, ORIGIN),
            Transform(rank_label, rank0_label),
            Transform(description, description0),
            run_time=2
        )
        self.wait(3)

        self.play(
            FadeOut(grid),
            FadeOut(v1),
            FadeOut(v2),
            FadeOut(rank_label),
            FadeOut(description),
            FadeOut(title)
        )

        takeaway = VGroup(
            Text("Matrix rank", font_size=36),
            MathTex(r"\operatorname{rank}(A)=\dim(\operatorname{Im}(A))"),
            Text("Rank tells us how many independent dimensions remain.",
                 font_size=24)
        ).arrange(DOWN, buff=0.5)

        self.play(Write(takeaway))
        self.wait(3)
