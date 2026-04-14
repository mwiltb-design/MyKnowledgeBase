import os
import subprocess
import sys
import json
from datetime import datetime

import os
import subprocess
import sys
import json
import time
from datetime import datetime

MAX_TURNS = 5
TURN_TIMEOUT = 20  # seconds per turn

def run_research(project_folder):
    """The Knowledge Ratchet: 20s turns, max 5 turns."""
    if not os.path.exists(project_folder):
        print(f"Error: Project folder '{project_folder}' not found.")
        return

    task_file = os.path.join(project_folder, 'Task.md')
    log_file = os.path.join(project_folder, 'Log.md')
    report_file = os.path.join(project_folder, 'Report.md')
    
    if not os.path.exists(task_file):
        print(f"Error: No 'Task.md' found in {project_folder}.")
        return

    # Initialize Log if it doesn't exist
    if not os.path.exists(log_file):
        with open(log_file, 'w') as f:
            f.write(f"# Research Log\nStarted: {datetime.now()}\n")

    print(f"--- Starting Knowledge Ratchet for: {os.path.basename(project_folder)} ---")
    
    for turn in range(1, MAX_TURNS + 1):
        print(f"\n[Turn {turn}/{MAX_TURNS}] Analyzing and searching...")
        
        # Read Task and current Log for context
        with open(task_file, 'r') as f: task_content = f.read()
        with open(log_file, 'r') as f: log_content = f.read()

        prompt = (
            f"You are the Research Lab Agent. This is Turn {turn} of {MAX_TURNS}.\n"
            f"GOAL: {task_content}\n\n"
            f"PREVIOUS PROGRESS:\n{log_content}\n\n"
            f"INSTRUCTIONS:\n"
            f"1. Use tools (grep_search, read_file) to find more data.\n"
            f"2. Update '{log_file}' with your findings. Be specific.\n"
            f"3. If research is complete, output 'COMPLETED' as the last line.\n"
            f"4. If not complete, summarize what you'll search for next.\n"
            f"NOTE: You have {TURN_TIMEOUT} seconds for this turn. BE FAST."
        )

        try:
            # Use --approval-mode yolo and pass the prompt directly to -p
            # This is the most reliable way to avoid interactive prompts
            process = subprocess.Popen(
                ['gemini', '--approval-mode', 'yolo', '-p', prompt],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                shell=True
            )
            stdout, stderr = process.communicate(timeout=TURN_TIMEOUT + 10)
            
            # Update the log
            with open(log_file, 'a') as f:
                f.write(f"\n--- Turn {turn} Results ---\n{stdout}\n")
            
            if "COMPLETED" in stdout:
                print(f"Research goal reached in {turn} turns.")
                break
                
        except subprocess.TimeoutExpired:
            print(f"Turn {turn} timed out. Moving to next turn...")
            continue
        except Exception as e:
            print(f"Error in turn {turn}: {e}")
            break

    # Final Synthesis: Generate the Report.md
    print("\n--- Generating Final Report ---")
    with open(log_file, 'r') as f: log_final = f.read()
    
    synthesis_prompt = (
        f"Synthesize the following research log into a final structured 'Report.md'.\n"
        f"LOG:\n{log_final}\n\n"
        f"FORMAT: Summary (3 bullets), Findings Table, and Recommended [[Wikilinks]]."
    )
    
    try:
        process = subprocess.Popen(
            ['gemini', '--approval-mode', 'yolo', '-p', synthesis_prompt],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            shell=True
        )
        report_out, _ = process.communicate()
        with open(report_file, 'w') as f:
            f.write(report_out)
        print(f"Report saved to: {report_file}")
    except Exception as e:
        print(f"Failed to generate report: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python Research_Core.py Projects/[FolderName]")
    else:
        run_research(sys.argv[1])

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python Research_Core.py Projects/[FolderName]")
    else:
        run_research(sys.argv[1])
