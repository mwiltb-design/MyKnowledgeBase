import os
import subprocess
import sys
import json
import time
from datetime import datetime

# CONFIGURATION
MAX_TURNS = 5
TURN_TIMEOUT = 60  # Increased to 60s for Windows overhead
FINAL_SYNTHESIS_TIMEOUT = 90

def run_research(project_folder):
    """The Knowledge Ratchet: High-speed, tool-focused research loop."""
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
        with open(log_file, 'w', encoding='utf-8') as f:
            f.write(f"# Research Log\nStarted: {datetime.now()}\n")

    print(f"\n>>> Starting Knowledge Ratchet: {os.path.basename(project_folder)} <<<")
    
    for turn in range(1, MAX_TURNS + 1):
        print(f"\n[Turn {turn}/{MAX_TURNS}] Running agent...")
        
        with open(task_file, 'r', encoding='utf-8') as f: task_content = f.read()
        with open(log_file, 'r', encoding='utf-8') as f: log_content = f.read()

        # Directive-focused prompt to force tool usage and prevent "Chatbot" behavior
        prompt = (
            f"DIRECTIVE: Execute research for the following goal.\n"
            f"GOAL: {task_content}\n\n"
            f"RESEARCH HISTORY:\n{log_content}\n\n"
            f"CRITICAL INSTRUCTIONS:\n"
            f"1. Do NOT introduce yourself or talk about your persona.\n"
            f"2. Use tools (grep_search, read_file) IMMEDIATELY to find data in the workspace.\n"
            f"3. If you find the answer, output 'RESEARCH_COMPLETE' followed by a summary.\n"
            f"4. If not done, provide a concise list of facts found and what you will search next.\n"
            f"5. All output must be technical and concise."
        )

        # Escaping for Windows Shell
        # We use a temporary file for the prompt to avoid command line length limits or character escaping issues
        temp_prompt_path = os.path.join(project_folder, "temp_prompt.txt")
        with open(temp_prompt_path, "w", encoding='utf-8') as f:
            f.write(prompt)

        try:
            # Using a safer way to pass the prompt
            # We already have a temp file, but let's fix the direct call just in case
            # Note: We'll stick to the list-based Popen which is generally safer for complex args
            
            process = subprocess.Popen(
                ["gemini", "--approval-mode", "yolo", "-p", prompt],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                shell=True
            )
            
            stdout, stderr = process.communicate(timeout=TURN_TIMEOUT)
            
            # Record results
            with open(log_file, 'a', encoding='utf-8') as f:
                f.write(f"\n\n--- Turn {turn} Findings ---\n{stdout}\n")
                if stderr:
                    f.write(f"\n[System Notes]: {stderr}\n")
            
            if "RESEARCH_COMPLETE" in stdout:
                print(f"Goal achieved in {turn} turns.")
                break
                
        except subprocess.TimeoutExpired:
            print(f"Turn {turn} timed out. Logging partial results...")
            process.kill()
            continue
        except Exception as e:
            print(f"Error in turn {turn}: {e}")
            break
        finally:
            if os.path.exists(temp_prompt_path):
                os.remove(temp_prompt_path)

    # Final Synthesis
    print("\n>>> Synthesizing Final Report <<<")
    with open(log_file, 'r', encoding='utf-8') as f: log_final = f.read()
    
    synthesis_prompt = (
        f"Synthesize this research log into a high-density 'Report.md'.\n"
        f"LOG:\n{log_final}\n\n"
        f"REQUIREMENTS:\n"
        f"- Summary (3 bullet points)\n"
        f"- Detailed Findings Table\n"
        f"- List of Recommended [[Wikilinks]]\n"
        f"Output ONLY the markdown content for the report."
    )
    
    try:
        process = subprocess.Popen(
            ["gemini", "--approval-mode", "yolo", "-p", synthesis_prompt],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            shell=True
        )
        report_out, _ = process.communicate(timeout=FINAL_SYNTHESIS_TIMEOUT)
        with open(report_file, 'w', encoding='utf-8') as f:
            f.write(report_out)
        print(f"Success! Report saved to: {report_file}")
    except Exception as e:
        print(f"Synthesis failed: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python Research_Core.py Projects/[FolderName]")
    else:
        run_research(sys.argv[1])
