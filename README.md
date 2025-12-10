 # Quick Sort Visualizer 


The reason I picked quick sort is because quick sort was the first ever sorting mechanism that I learned, Quick sort is the first sorting that I understood and implemented into my personal code, and I remember while trying to learn it I had to go through multiple videos to understand, therefore with this application, it may help someone in my situtaion in the future.


# video/Example of app


https://github.com/user-attachments/assets/390a4fc2-09c3-443a-b1ed-6675bbd8c13c


[Array size 3 example.pdf](https://github.com/user-attachments/files/24067200/Array.size.3.example.pdf)



## Problem Breakdown & Computational Thinking (You can add a flowchart and write the
four pillars of computational thinking briefly in bullets)

Decomposition: Break Quick Sort into smaller, manageable steps:


Input Handling
- Accept a list of integers from the user (comma-separated string → converted to a list).

Pivot Selection
- Choose a pivot (last element in the array for simplicity).

Partitioning
- Compare each element to the pivot.
- Elements smaller than the pivot move to the left partition; larger elements move to the right.

Swapping / Rearranging
- Swap elements as needed so that the pivot ends up in the correct position.

Recursion
- Repeat Quick Sort on the left subarray.
- Repeat Quick Sort on the right subarray.

Visualization
- After every comparison, swap, or pivot placement, capture the current state for the user to see.

Output
- Display all recorded steps as visual bar-charts in sequence.

# FlowChart:

      ┌─────────────────────────────┐
      │ User inputs number list     │
      └───────────────┬─────────────┘
                      ▼
         ┌────────────────────────┐
         │ Convert input to array │
         └────────────┬───────────┘
                      ▼
      ┌─────────────────────────────────┐
      │ Perform Quick Sort recursively │
      │ • choose pivot                 │
      │ • partition elements           │
      │ • record visualization step    │
      └────────────┬──────────────────┘
                   ▼
      ┌─────────────────────────┐
      │ Generate plot for step │
      └──────────┬──────────────┘
                 ▼
      ┌─────────────────────────────┐
      │ Add image to step gallery   │
      └──────────┬──────────────────┘
                 ▼
      ┌─────────────────────────┐
      │ Display final sequence │
      └─────────────────────────┘


## Steps to Run

1. Go to huggingface.co website or click on my hugging gace link
2.  drag to select size of array ( 3 - 25)
3.  select minimum value
4.  select maximum value
5.  add your own array values (optional)
6.  click generate to create the simulation.
7.  click next to view the next step in the sort (click previous if you need to go back)

You're Done!!!


## Hugging Face Link

https://huggingface.co/spaces/AmiraliB999/Cisc121-Quicksort

## Author & Acknowledgment.
Amirali Berenjimonfared 25sy@queensu.ca

AI Level 4 (Chat GPT Ai) was used inside of this project

Python Version: 3.12.11 UI Framework: Gradio

Course information : CISC 121
Prompts Used:

[prompts for cisc 121 - app project.pdf](https://github.com/user-attachments/files/24067210/prompts.for.cisc.121.-.app.project.pdf)


