"""
CISC 121 — Quick Sort Visualizer (Enhanced Version)
Features:
- Step-by-step visualization
- Next / Previous buttons
- Autoplay feature
- Clear color-coded legend
- Detailed comments explaining the algorithm
- Custom arrays or random generation
"""

import random
import io
import time
from typing import List, Dict
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("Agg")
import gradio as gr

# ---------------------------------------------------------
# Draw array as a bar chart with highlights
# ---------------------------------------------------------
def draw_array(arr: List[int], highlight, title=""):
    """
    arr: list of integers representing the array at this step
    highlight: list of indices to highlight (pivot, active comparisons, swaps)
    title: text explaining what is happening in this step
    """

    fig, ax = plt.subplots(figsize=(7, 3))
    x = list(range(len(arr)))
    bars = ax.bar(x, arr)

    # Color default bars
    for bar in bars:
        bar.set_color("C0")

    # Highlight special bars
    for i in highlight:
        if 0 <= i < len(bars):
            bars[i].set_color("C3")  # red highlight

    ax.set_title(title)
    ax.set_xticks(x)
    ax.set_ylim(0, max(arr) * 1.25 if arr else 1)
    ax.grid(axis="y", linestyle="--", alpha=0.5)

    buf = io.BytesIO()
    plt.tight_layout()
    plt.savefig(buf, format="png")
    plt.close(fig)
    buf.seek(0)
    return Image.open(buf)

# ---------------------------------------------------------
# Quick Sort Frame Generator
# ---------------------------------------------------------
def quick_sort_frames(arr: List[int]) -> List[Dict]:
    """
    Runs quicksort, storing each step in a frame:
    - array state
    - highlighted indices
    - descriptive message
    """

    frames = []
    A = arr.copy()

    def capture(message, indices=None):
        frames.append({
            "arr": A.copy(),
            "highlight": indices or [],
            "message": message
        })

    def partition(lo, hi):
        pivot = A[hi]
        capture(f"Choosing pivot A[{hi}] = {pivot}", [hi])
        i = lo

        for j in range(lo, hi):
            capture(f"Comparing A[{j}] = {A[j]} with pivot {pivot}", [j, hi])

            if A[j] < pivot:
                capture(f"Swapping A[{i}] = {A[i]} and A[{j}] = {A[j]}", [i, j])
                A[i], A[j] = A[j], A[i]
                i += 1

        capture(f"Moving pivot into place: Swap A[{i}] with A[{hi}]", [i, hi])
        A[i], A[hi] = A[hi], A[i]

        return i

    def quick(lo, hi):
        if lo < hi:
            p = partition(lo, hi)
            quick(lo, p - 1)
            quick(p + 1, hi)
        else:
            if lo == hi:
                capture(f"Element at index {lo} is in correct position", [lo])

    capture("Starting Quick Sort")
    quick(0, len(A) - 1)
    capture("Quick Sort Complete")
    return frames

# ---------------------------------------------------------
# UI Logic
# ---------------------------------------------------------
def generate_array(length, minv, maxv):
    return [random.randint(minv, maxv) for _ in range(length)]

def prepare(length, minv, maxv, custom):
    if custom and custom.strip():
        try:
            arr = [int(x) for x in custom.split(",")]
        except:
            arr = generate_array(length, minv, maxv)
    else:
        arr = generate_array(length, minv, maxv)

    frames = quick_sort_frames(arr)
    first = frames[0]
    img = draw_array(first["arr"], first["highlight"], first["message"])
    arr_str = ", ".join(map(str, first["arr"]))
    return frames, 0, img, first["message"], arr_str

def show_frame(frames, idx):
    idx = max(0, min(idx, len(frames) - 1))
    f = frames[idx]
    img = draw_array(f["arr"], f["highlight"], f["message"])
    arr_str = ", ".join(map(str, f["arr"]))
    return img, f["message"], arr_str, idx

def next_frame(frames, idx):
    return show_frame(frames, idx + 1)

def prev_frame(frames, idx):
    return show_frame(frames, idx - 1)

def autoplay(frames, start_idx):
    """
    Automatically steps through frames with slight delay.
    """
    results = []
    idx = start_idx
    for _ in range(start_idx, len(frames)):
        f = frames[idx]
        img = draw_array(f["arr"], f["highlight"], f["message"])
        arr_str = ", ".join(map(str, f["arr"]))
        results.append((img, f["message"], arr_str, idx))
        idx += 1
        time.sleep(0.15)  # playback speed
    return results[-1] if results else None

# ---------------------------------------------------------
# Build UI
# ---------------------------------------------------------
with gr.Blocks(title="Quick Sort Visualizer — Enhanced") as demo:

    gr.Markdown("## 🔵 Enhanced Quick Sort Visualizer")

    with gr.Row():
        gr.Markdown("""
        ### Legend  
        - 🔵 Blue Bars → Normal elements  
        - 🔴 Red Bars → Pivot / Swap / Comparison  
        """)

    with gr.Row():
        with gr.Column():
            length = gr.Slider(3, 25, value=10, step=1, label="Array Length")
            minv = gr.Number(value=1, label="Minimum Value")
            maxv = gr.Number(value=30, label="Maximum Value")
            custom = gr.Textbox(label="Custom Array (optional)", placeholder="e.g. 5,3,1,4,2")
            gen_btn = gr.Button("Generate")
            next_btn = gr.Button("Next ▶")
            prev_btn = gr.Button("◀ Previous")
            auto_btn = gr.Button("Autoplay ▶▶")

        with gr.Column():
            image_out = gr.Image(type="pil", label="Visualization")
            msg_out = gr.Textbox(label="Description")
            arr_out = gr.Textbox(label="Current Array")

    frames_state = gr.State([])
    index_state = gr.State(0)

    gen_btn.click(prepare,
        inputs=[length, minv, maxv, custom],
        outputs=[frames_state, index_state, image_out, msg_out, arr_out])

    next_btn.click(next_frame,
        inputs=[frames_state, index_state],
        outputs=[image_out, msg_out, arr_out, index_state])

    prev_btn.click(prev_frame,
        inputs=[frames_state, index_state],
        outputs=[image_out, msg_out, arr_out, index_state])

    auto_btn.click(autoplay,
        inputs=[frames_state, index_state],
        outputs=[image_out, msg_out, arr_out, index_state])

if __name__ == "__main__":
    demo.launch(share=True)
