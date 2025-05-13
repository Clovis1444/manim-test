from datetime import datetime, timedelta
import manim


class MyScene(manim.Scene):
    def construct(self):
        # Calendar
        calendar = manim.ImageMobject("images/calendar13_05.png")
        calendar.set(height=manim.config.frame_height * 0.25)

        self.add(calendar)

        # Date rect
        dateRect = manim.Rectangle(manim.DARK_BLUE, 0.4, 0.6)
        dateRect.move_to((-0.555, 0.675, 0))
        # Draw date rect
        self.play(manim.Create(dateRect))

        # Date text
        dateText = manim.Text("29.04.2025", font_size=8)
        dateText.move_to(dateRect)
        # Draw date text
        self.play(manim.Create(dateText))

        self.wait(2)

        # Fade calendar
        # Move date rect to ORIGIN, resize to size 1
        # Move date text to ORIGIN, scale 2.5
        self.play(
            calendar.animate.fade(1),
            dateRect.animate.move_to(manim.ORIGIN).set(width=1, height=1),
            dateText.animate.move_to(manim.ORIGIN).scale(2.5),
        )

        self.wait(2)

        # Count text
        DC = "Days count: "
        c = 1
        countText = manim.Text(DC + str(c), font_size=20)
        countText.shift(manim.UP * 1)
        # Draw count text
        self.play(manim.Write(countText))

        self.wait(2)

        # Loop through dates
        currentDate = datetime(2025, 4, 29)
        endDate = datetime(2025, 5, 13)
        while currentDate < endDate:
            c += 1
            currentDate += timedelta(days=1)

            newCountText = manim.Text(DC + str(c), font_size=20)
            newCountText.shift(manim.UP * 1)

            newDateText = manim.Text(currentDate.strftime("%d.%m.%Y"), font_size=8)
            newDateText.scale(2.5)

            # Update date
            # Update counter
            self.play(
                manim.Transform(countText, newCountText),
                manim.Transform(dateText, newDateText),
            )
            self.wait(1)
        self.wait(1)

        # Final text
        finalText = manim.Text("Since 29.04.2025: " + str(c) + " days", font_size=20)

        # Transform count text into final text
        # Fade date rect
        # Fade date text
        self.play(
            manim.Transform(countText, finalText),
            dateRect.animate.fade(1),
            dateText.animate.fade(1),
        )

        self.wait(5)
