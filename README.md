[](videos/Cool.mp4)

# About

This is my manim hello world project.

# Development(Linux)

Dependencies:

```bash
sudo apt install python3-dev python3-pip python3-venv ffmpeg
```

Create new virtual environment:

```bash
python3 -m venv manim-env
```

Enter in virtual environment:

```bash
source manim-env/bin/activate
```

Install manim:

```bash
pip install manim
```

# Run

```bash
manim -pql main.py MyScene
```

> [!NOTE]
> For more info see:
>
> ```bash
> manim --help
> ```
>
> ```bash
> manim render --help
> ```
